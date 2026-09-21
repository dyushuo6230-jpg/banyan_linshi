"""Narrow Project Instance Pilot creation after runtime preflight and checkpoint."""

from __future__ import annotations

from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import shutil
from typing import Any, Mapping

import yaml

from banyan.cursor.adapter import CursorPilotAdapter


ALLOWED_TOP_LEVEL = {
    "PILOT_NOTICE.md", "pilot.yaml", "instance", "mappings", "overlays", "profiles",
    "providers", "runtime", "trace", "index", "generated", "migrations",
}
FORBIDDEN_KEYS = {"secret_body", "secret_hash", "user_name", "user_email", "canonical_content"}


class PilotValidationError(ValueError):
    pass


class PilotActivationCoordinator:
    def __init__(self, adapter: CursorPilotAdapter):
        self.adapter = adapter

    def preflight(self, authorization_ref: str, checkpoint_ref: str) -> dict[str, Any]:
        return self.adapter.pilot_preflight({
            "action_id": "stage17-project-instance-pilot-create",
            "action_type": "protected_write",
            "target_id": ".banyan",
            "target_state": {"secret_risk": False, "conflicted": False},
            "work_mode": "FULL",
            "authorization_ref": authorization_ref,
            "evidence_refs": [checkpoint_ref, "stage17-explicit-gate"],
            "impact_ref": "pilot-shadow-only-preserve-in-place",
            "decision_ref": "stage17-explicit-gate",
            "precondition_results": {
                "evidence_complete": True,
                "impact_reviewed": True,
                "authorization_valid": True,
                "secret_check_passed": True,
                "freshness_valid": True,
                "rollback_ready": True,
            },
        }, stage_gate_ref="stage17-explicit-gate", checkpoint_ref=checkpoint_ref)

    def validate_shadow(self, shadow_root: str | Path) -> dict[str, Any]:
        root = Path(shadow_root).resolve()
        if not root.is_dir():
            raise PilotValidationError("shadow root is missing")
        entries = {path.name for path in root.iterdir()}
        unexpected = entries - ALLOWED_TOP_LEVEL
        if unexpected:
            raise PilotValidationError(f"unexpected pilot entries: {sorted(unexpected)}")
        required = {"PILOT_NOTICE.md", "pilot.yaml", "instance", "mappings", "providers", "runtime", "migrations"}
        missing = required - entries
        if missing:
            raise PilotValidationError(f"missing pilot entries: {sorted(missing)}")
        files = sorted(path for path in root.rglob("*") if path.is_file())
        if not files:
            raise PilotValidationError("shadow pilot has no files")
        manifest: list[dict[str, str]] = []
        for path in files:
            if path.is_symlink():
                raise PilotValidationError("pilot symlinks are forbidden")
            relative = path.relative_to(root).as_posix()
            if relative.startswith(".git/") or path.name == ".git":
                raise PilotValidationError("Git internals are forbidden in pilot")
            raw = path.read_bytes()
            if path.suffix in {".yaml", ".yml", ".json"}:
                value = json.loads(raw) if path.suffix == ".json" else yaml.safe_load(raw)
                self._reject_forbidden_keys(value)
            manifest.append({"path": relative, "sha256": sha256(raw).hexdigest()})
        return {"valid": True, "file_count": len(files), "files": manifest}

    def activate(
        self,
        shadow_root: str | Path,
        target_root: str | Path,
        *,
        preflight_result: Mapping[str, Any],
        checkpoint_ref: str,
        authorization_ref: str,
    ) -> dict[str, Any]:
        validation = self.validate_shadow(shadow_root)
        target = Path(target_root).resolve()
        if target.name != ".banyan":
            raise PilotValidationError("pilot target must be named .banyan")
        if target.exists():
            raise PilotValidationError("pilot target already exists")
        if (preflight_result.get("permission_result") != "ALLOW"
                or preflight_result.get("pilot_scope_authorized") is not True
                or preflight_result.get("general_project_write_allowed") is not False
                or preflight_result.get("executed") is not False):
            raise PilotValidationError("runtime preflight did not allow the scoped pilot request")
        if not authorization_ref or not checkpoint_ref:
            raise PilotValidationError("authorization and checkpoint references are required")

        shutil.copytree(Path(shadow_root), target, copy_function=shutil.copy2)
        self.adapter.control_plane.runtime.emit_audit({
            "event_type": "PROJECT_INSTANCE_PILOT_CREATED",
            "action_id": "stage17-project-instance-pilot-create",
            "occurred_at": datetime.now(timezone.utc).isoformat(),
            "result": "PILOT_CREATED",
            "grants_authorization": False,
            "authorization_ref": authorization_ref,
            "checkpoint_ref": checkpoint_ref,
            "target_id": str(target),
            "file_count": validation["file_count"],
        })
        return {
            "mode": "PILOT",
            "dot_banyan_created": True,
            "pilot_created": True,
            "final_activation": False,
            "canonical_replacement": False,
            "validation": validation,
            "checkpoint_ref": checkpoint_ref,
            "authorization_ref": authorization_ref,
            "rollback_ready": True,
        }

    def review_existing_pilot(
        self,
        shadow_root: str | Path,
        target_root: str | Path,
        *,
        preflight_result: Mapping[str, Any],
    ) -> dict[str, Any]:
        if (preflight_result.get("pilot_scope_authorized") is not True
                or preflight_result.get("general_project_write_allowed") is not False
                or preflight_result.get("final_activation_allowed") is not False):
            raise PilotValidationError("runtime-scoped Pilot gate is invalid")
        shadow = self.validate_shadow(shadow_root)
        target = self.validate_shadow(target_root)
        shadow_hashes = {item["path"]: item["sha256"] for item in shadow["files"]}
        target_hashes = {item["path"]: item["sha256"] for item in target["files"]}
        if shadow_hashes != target_hashes:
            raise PilotValidationError("installed Pilot differs from validated Shadow")
        return {
            "result": "PASS_PILOT_ONLY",
            "pilot_scope_authorized": True,
            "exact_shadow_match": True,
            "file_count": target["file_count"],
            "final_activation": False,
            "general_project_write_allowed": False,
        }

    @classmethod
    def _reject_forbidden_keys(cls, value: Any) -> None:
        if isinstance(value, dict):
            bad = FORBIDDEN_KEYS & set(value)
            if bad:
                raise PilotValidationError(f"forbidden sensitive keys: {sorted(bad)}")
            for child in value.values():
                cls._reject_forbidden_keys(child)
        elif isinstance(value, list):
            for child in value:
                cls._reject_forbidden_keys(child)

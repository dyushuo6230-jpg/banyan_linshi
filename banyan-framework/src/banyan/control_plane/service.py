"""Generic Control Plane composition over the Stage 15 Runtime API."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from banyan.runtime.api import RuntimeAPI
from banyan.runtime.models import ActionRequest, ExecutionScope


PROVENANCE_FIELDS = (
    "stable_id", "classification", "source_role", "authority", "version", "status",
    "freshness", "provenance", "source_refs", "related_refs",
)
SECRET_FIELDS = {"stable_id", "path", "classification", "existence", "restriction_flags"}


class ControlPlaneService:
    """No policy logic lives here; decisions are delegated to RuntimeAPI."""

    def __init__(
        self,
        runtime: RuntimeAPI,
        repository: str | Path,
        *,
        trace_path: str | Path | None = None,
        provider_path: str | Path | None = None,
        provenance: Mapping[str, Mapping[str, Any]] | None = None,
        stages: list[dict[str, Any]] | None = None,
    ):
        self.runtime = runtime
        self.repository = Path(repository).resolve()
        self.trace_path = Path(trace_path) if trace_path else None
        self.provider_path = Path(provider_path) if provider_path else None
        self.provenance = dict(provenance or {})
        self.stage_records = list(stages or [])

    def status(self) -> dict[str, Any]:
        runtime = self.runtime.status()
        return {
            "runtime_health": "HEALTHY",
            "compiled_policy_hash": runtime["policy_hash"],
            "execution_mode": runtime["current_project_execution"],
            "current_project_mutation_allowed": False,
            "open_blockers": ["STAGE17_GATE_REQUIRED", "CURRENT_PROJECT_DRY_RUN_ONLY"],
            "current_stage": "16",
            "latest_run": self.stage_records[-1].get("run_id", "UNKNOWN") if self.stage_records else "UNKNOWN",
            "provider_status": self.providers(),
            "activation_state": "NOT_ACTIVATED",
            "capabilities": self.capabilities(),
        }

    def capabilities(self) -> dict[str, str]:
        return {
            "runtime_status": "AVAILABLE_READ_ONLY",
            "policy_status": "AVAILABLE_READ_ONLY",
            "project_safety": "AVAILABLE_READ_ONLY",
            "preflight": "AVAILABLE_READ_ONLY",
            "commit_plan": "AVAILABLE_READ_ONLY",
            "commit_dry_run": "AVAILABLE_DRY_RUN",
            "current_project_git_mutation": "NOT_AUTHORIZED_IN_STAGE16",
            "canonical_apply": "NOT_AUTHORIZED_IN_STAGE16",
            "dot_banyan_activation": "NOT_AUTHORIZED_IN_STAGE16",
        }

    def policy_status(self) -> dict[str, Any]:
        policy = self.runtime.policy
        return {
            "policy_hash": policy.policy_hash,
            "policy_id": policy.data["policy_id"],
            "schema_version": policy.data["schema_version"],
            "hard_blocks": list(policy.data["hard_blocks"]),
            "current_project_mutation_allowed": False,
            "control_plane_may_bypass": False,
        }

    def project_safety(self) -> dict[str, Any]:
        raw = self.runtime.inspect_project(self.repository)
        name_present = bool(raw.pop("identity_name_present"))
        email_present = bool(raw.pop("identity_email_present"))
        raw.pop("identity_values_recorded", None)
        return {
            "branch": raw["branch"],
            "head": raw["head"],
            "staged_count": raw["staged"],
            "unstaged_count": raw["unstaged"],
            "untracked_count": raw["untracked"],
            "conflicted_count": raw["conflicted"],
            "identity_present": name_present and email_present,
            "identity_ambiguous": name_present != email_present,
            "identity_values_exposed": False,
            "execution_mode": "DRY_RUN_ONLY",
            "mutation_controls": "DISABLED",
        }

    def preflight(self, intent: Mapping[str, Any]) -> dict[str, Any]:
        request = self._action_request(intent)
        result = self.runtime.preflight_action(request).to_dict()
        result["ui_confirmation_is_authorization"] = False
        result["action_state"] = self._action_state(result["permission_result"], dry_run=False)
        return result

    def pilot_preflight(self, intent: Mapping[str, Any], *, stage_gate_ref: str, checkpoint_ref: str) -> dict[str, Any]:
        request = self._action_request(intent)
        result = self.runtime.preflight_pilot_creation(
            request, stage_gate_ref=stage_gate_ref, checkpoint_ref=checkpoint_ref,
        )
        result["ui_confirmation_is_authorization"] = False
        result["action_state"] = "PILOT_SCOPE_AVAILABLE" if result["pilot_scope_authorized"] else "BLOCKED"
        return result

    def _action_request(self, intent: Mapping[str, Any]) -> ActionRequest:
        return ActionRequest(
            action_id=str(intent["action_id"]),
            action_type=str(intent["action_type"]),
            execution_scope=ExecutionScope.CURRENT_PROJECT_DRY_RUN,
            target_id=str(intent.get("target_id", self.repository)),
            target_state=dict(intent.get("target_state", {})),
            work_mode=str(intent.get("work_mode", "STANDARD")),
            evidence_refs=tuple(intent.get("evidence_refs", ())),
            impact_ref=intent.get("impact_ref"),
            decision_ref=intent.get("decision_ref"),
            authorization_ref=intent.get("authorization_ref"),
            precondition_results=dict(intent.get("precondition_results", {})),
        )

    def commit_plan(self, request: Mapping[str, Any]) -> dict[str, Any]:
        plan = self.runtime.plan_commit(
            self.repository,
            dict(request.get("classifications", {})),
            groups=dict(request.get("groups", {})),
            messages=dict(request.get("messages", {})),
        )
        return {**plan, "is_authorization": False, "execution_mode": "DRY_RUN_ONLY"}

    def commit_dry_run(self, request: Mapping[str, Any]) -> dict[str, Any]:
        result = self.runtime.dry_run_commit(
            self.repository,
            dict(request["plan"]),
            authorization_ref=request.get("authorization_ref"),
        )
        return {
            **result,
            "display_label": "DRY_RUN_NOT_COMMIT",
            "actual_commit_created": False,
            "action_state": self._action_state(result["permission_result"], dry_run=True),
        }

    def trace(self, *, offset: int = 0, limit: int = 50) -> dict[str, Any]:
        if self.trace_path is None:
            return {"items": [], "offset": offset, "limit": limit, "has_more": False, "trace_is_authorization": False}
        result = self.runtime.query_trace(self.trace_path, offset=offset, limit=limit)
        result["trace_is_authorization"] = False
        return result

    def provenance_view(self, stable_id: str) -> dict[str, Any]:
        source = dict(self.provenance.get(stable_id, {}))
        if source.get("classification") == "SECRET":
            result = {key: source.get(key, "UNKNOWN") for key in SECRET_FIELDS}
            result["secret_body_rendered"] = False
            return result
        result: dict[str, Any] = {}
        for field in PROVENANCE_FIELDS:
            default: Any = [] if field in {"source_refs", "related_refs"} else "UNKNOWN"
            result[field] = source.get(field, default)
        return result

    def providers(self) -> list[dict[str, Any]]:
        if self.provider_path is None or not self.provider_path.exists():
            return []
        return [
            {**binding, "activation_state": "NOT_ACTIVATED"}
            for binding in self.runtime.list_provider_bindings(self.provider_path)
        ]

    def stages(self, *, offset: int = 0, limit: int = 25) -> dict[str, Any]:
        if offset < 0 or not 1 <= limit <= 100:
            raise ValueError("stage pagination is out of range")
        page = self.stage_records[offset:offset + limit]
        return {"items": page, "offset": offset, "limit": limit, "has_more": offset + limit < len(self.stage_records)}

    def activation_readiness(self) -> dict[str, Any]:
        runtime_result = self.preflight({
            "action_id": "stage16-activation-readiness",
            "action_type": "protected_write",
            "target_id": str(self.repository / ".banyan"),
            "target_state": {},
            "precondition_results": {
                "evidence_complete": True,
                "impact_reviewed": True,
                "authorization_valid": False,
                "secret_check_passed": True,
                "freshness_valid": True,
                "rollback_ready": True,
            },
        })
        return {
            "state": "BLOCKED",
            "activation_state": "NOT_ACTIVATED",
            "blockers": ["STAGE17_GATE_REQUIRED", *runtime_result["reason_codes"]],
            "required_preconditions": ["independent_stage17_gate", "pilot_scope", "project_instance_validation"],
            "required_validations": ["cursor_adapter_port", "pilot_rollback", "dot_banyan_scope"],
            "pilot_stage": "17",
            "stage16_may_activate_dot_banyan": False,
            "runtime_permission_result": runtime_result["permission_result"],
        }

    @staticmethod
    def _action_state(permission: str, *, dry_run: bool) -> str:
        if permission == "ALLOW":
            return "AVAILABLE_DRY_RUN" if dry_run else "AVAILABLE_READ_ONLY"
        if permission in {"BLOCK", "NEEDS_INPUT", "NOT_APPLICABLE"}:
            return permission
        return "BLOCKED"

"""Cursor-facing adapter. It owns no policy, canonical truth, or Git mutation."""

from __future__ import annotations

from typing import Any, Mapping

from banyan.control_plane.service import ControlPlaneService


class CursorPilotAdapter:
    def __init__(self, control_plane: ControlPlaneService):
        self.control_plane = control_plane

    def runtime_status(self) -> dict[str, Any]:
        return self.control_plane.status()

    def project_safety(self) -> dict[str, Any]:
        return self.control_plane.project_safety()

    def preflight(self, intent: Mapping[str, Any]) -> dict[str, Any]:
        return self.control_plane.preflight(intent)

    def pilot_preflight(self, intent: Mapping[str, Any], *, stage_gate_ref: str, checkpoint_ref: str) -> dict[str, Any]:
        return self.control_plane.pilot_preflight(intent, stage_gate_ref=stage_gate_ref, checkpoint_ref=checkpoint_ref)

    def plan(self, request: Mapping[str, Any]) -> dict[str, Any]:
        return self.control_plane.commit_plan(request)

    def dry_run(self, request: Mapping[str, Any]) -> dict[str, Any]:
        return self.control_plane.commit_dry_run(request)

    def provenance(self, stable_id: str) -> dict[str, Any]:
        return self.control_plane.provenance_view(stable_id)

    def activation_readiness(self) -> dict[str, Any]:
        return self.control_plane.activation_readiness()

    @staticmethod
    def capabilities() -> dict[str, bool]:
        return {
            "owns_permission_policy": False,
            "owns_canonical_truth": False,
            "direct_git_mutation": False,
            "direct_project_write": False,
            "calls_control_plane": True,
        }

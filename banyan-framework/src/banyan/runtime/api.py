from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone
from typing import Any

from banyan.commit.executor import CommitExecutor
from banyan.commit.planner import CommitGroup, CommitPlan, CommitPlanner
from banyan.git.adapter import GitAdapter
from banyan.policy import CompiledPolicy
from banyan.providers.loader import ProviderBindingLoader
from banyan.trace.emitter import TraceEmitter
from .evaluator import PermissionEvaluator
from .models import ActionRequest, ActionResult


class RuntimeAPI:
    """Stable machine-callable surface shared by CLI and future control planes."""

    def __init__(self, policy: CompiledPolicy, trace_path: str | Path | None = None):
        self.policy = policy
        self.evaluator = PermissionEvaluator(policy)
        self.trace = TraceEmitter(trace_path) if trace_path else None

    def evaluate_action(self, request: ActionRequest) -> ActionResult:
        result = self.evaluator.evaluate(request)
        if self.trace:
            self.trace.emit(result.audit_event)
        return result

    def preflight_action(self, request: ActionRequest) -> ActionResult:
        return self.evaluate_action(request)

    def preflight_pilot_creation(
        self,
        request: ActionRequest,
        *,
        stage_gate_ref: str,
        checkpoint_ref: str,
    ) -> dict[str, Any]:
        """Bind a Runtime decision to the narrow `.banyan/**` Pilot scope."""
        result = self.preflight_action(request).to_dict()
        target_name = Path(request.target_id).name
        valid_binding = all((
            request.action_type == "protected_write",
            request.execution_scope.value == "CURRENT_PROJECT_DRY_RUN",
            target_name == ".banyan",
            bool(request.authorization_ref),
            bool(stage_gate_ref),
            bool(checkpoint_ref),
            result["permission_result"] == "ALLOW",
            not result["failed_or_missing_preconditions"],
        ))
        scoped = {
            **result,
            "pilot_scope_authorized": valid_binding,
            "pilot_allowed_root": ".banyan",
            "pilot_allowed_glob": ".banyan/**",
            "general_project_write_allowed": False,
            "final_activation_allowed": False,
            "stage_gate_ref": stage_gate_ref,
            "checkpoint_ref": checkpoint_ref,
        }
        if self.trace:
            self.trace.emit({
                "event_type": "PILOT_SCOPE_EVALUATED",
                "action_id": request.action_id,
                "occurred_at": datetime.now(timezone.utc).isoformat(),
                "result": "ALLOW" if valid_binding else "BLOCK",
                "grants_authorization": False,
                "authorization_ref": request.authorization_ref,
                "stage_gate_ref": stage_gate_ref,
                "checkpoint_ref": checkpoint_ref,
                "pilot_scope_authorized": valid_binding,
                "general_project_write_allowed": False,
            })
        return scoped

    def inspect_project(self, repository: str | Path, fixture_root: str | Path | None = None) -> dict[str, Any]:
        return GitAdapter(repository, fixture_root=fixture_root).inspect()

    def plan_commit(
        self,
        repository: str | Path,
        classifications: dict[str, str] | None = None,
        *,
        groups: dict[str, str] | None = None,
        messages: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        return CommitPlanner(GitAdapter(repository)).plan(
            classifications or {}, groups=groups, messages=messages,
        ).to_dict()

    def execute_commit(self, **kwargs: Any) -> dict[str, Any]:
        return CommitExecutor(policy=self.policy, trace=self.trace).execute(**kwargs).to_dict()

    def dry_run_commit(
        self,
        repository: str | Path,
        plan: CommitPlan | dict[str, Any],
        authorization_ref: str | None = None,
    ) -> dict[str, Any]:
        """The only current-project commit execution surface; it is always dry-run."""
        typed_plan = plan if isinstance(plan, CommitPlan) else self._commit_plan_from_dict(plan)
        return self.execute_commit(
            adapter=GitAdapter(repository),
            plan=typed_plan,
            dry_run=True,
            authorization_ref=authorization_ref,
        )

    @staticmethod
    def _commit_plan_from_dict(value: dict[str, Any]) -> CommitPlan:
        allowed = {"groups", "classifications", "blocked_paths", "leftovers"}
        if not isinstance(value, dict) or set(value) != allowed:
            raise ValueError("commit plan fields mismatch")
        groups = tuple(
            CommitGroup(
                group_id=item["group_id"],
                message=item["message"],
                paths=tuple(item["paths"]),
                patches=tuple(item.get("patches", ())),
                patch_paths=tuple(item.get("patch_paths", ())),
            )
            for item in value["groups"]
        )
        return CommitPlan(
            groups,
            dict(value["classifications"]),
            tuple(value["blocked_paths"]),
            tuple(value["leftovers"]),
        )

    @staticmethod
    def query_trace(path: str | Path, *, offset: int = 0, limit: int = 50) -> dict[str, Any]:
        if offset < 0 or not 1 <= limit <= 200:
            raise ValueError("trace pagination is out of range")
        source = Path(path)
        if not source.exists():
            return {"items": [], "offset": offset, "limit": limit, "has_more": False}
        import json
        rows = [json.loads(line) for line in source.read_text(encoding="utf-8").splitlines() if line.strip()]
        for row in rows:
            TraceEmitter.validate(row)
        page = rows[offset:offset + limit]
        return {"items": page, "offset": offset, "limit": limit, "has_more": offset + limit < len(rows)}

    def emit_audit(self, event: dict[str, Any]) -> None:
        if not self.trace:
            raise ValueError("trace path is not configured")
        self.trace.emit(event)

    @staticmethod
    def list_provider_bindings(path: str | Path) -> list[dict[str, Any]]:
        return ProviderBindingLoader().load(path)

    def status(self) -> dict[str, Any]:
        return {
            "runtime_version": "0.1.0",
            "policy_hash": self.policy.policy_hash,
            "current_project_execution": "DRY_RUN_ONLY",
            "fixture_execution": "AVAILABLE_WITH_GATES",
        }

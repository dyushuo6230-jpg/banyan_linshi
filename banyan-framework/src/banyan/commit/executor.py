"""Guarded semantic commit execution for dry-run and isolated fixtures."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any

from banyan.git.adapter import GitAdapter
from banyan.git.index import IndexCheckpoint
from banyan.policy import CompiledPolicy
from banyan.runtime.evaluator import PermissionEvaluator
from banyan.runtime.models import ActionRequest, ExecutionScope
from banyan.trace.emitter import TraceEmitter

from .planner import CommitPlan


@dataclass(frozen=True)
class CommitExecutionResult:
    status: str
    dry_run: bool
    permission_result: str
    commits: tuple[str, ...]
    planned_groups: tuple[dict[str, Any], ...]
    leftovers: tuple[str, ...]
    reason_codes: tuple[str, ...]
    rolled_back: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class CommitExecutor:
    def __init__(self, policy: CompiledPolicy, trace: TraceEmitter | None = None):
        self.policy = policy
        self.evaluator = PermissionEvaluator(policy)
        self.trace = trace

    def execute(
        self,
        *,
        adapter: GitAdapter,
        plan: CommitPlan,
        dry_run: bool,
        authorization_ref: str | None,
        expected_stage_sets: dict[str, tuple[str, ...]] | None = None,
    ) -> CommitExecutionResult:
        if not dry_run and not adapter.is_fixture:
            raise PermissionError("real commit execution is restricted to isolated fixtures")
        if not dry_run and self.trace is None:
            raise ValueError("fixture commit execution requires an audit trace")

        state = adapter.inspect()
        request = ActionRequest(
            action_id="semantic-commit-execute",
            action_type="commit",
            execution_scope=(ExecutionScope.CURRENT_PROJECT_DRY_RUN if dry_run else ExecutionScope.ISOLATED_FIXTURE),
            target_id=str(adapter.repository),
            target_state={
                "identity_present": bool(state["identity_name_present"] and state["identity_email_present"]),
                "conflicted": bool(state["conflicted"]),
                "secret_risk": bool(plan.blocked_paths),
            },
            authorization_ref=authorization_ref,
            precondition_results={
                "evidence_complete": True,
                "impact_reviewed": True,
                "authorization_valid": bool(authorization_ref),
                "secret_check_passed": not bool(plan.blocked_paths),
                "freshness_valid": True,
                "rollback_ready": True,
            },
        )
        permission = self.evaluator.evaluate(request)
        self._emit(permission.audit_event)
        group_records = tuple(
            {"group_id": group.group_id, "message": group.message, "paths": list(group.paths),
             "patch_paths": list(group.patch_paths), "patch_count": len(group.patches)}
            for group in plan.groups
        )
        if permission.permission_result != "ALLOW":
            return CommitExecutionResult(
                "BLOCKED", dry_run, permission.permission_result, (), group_records,
                plan.leftovers, permission.reason_codes,
            )
        if dry_run:
            self._emit_event("COMMIT_DRY_RUN_COMPLETED", "DRY_RUN", adapter, authorization_ref)
            return CommitExecutionResult("DRY_RUN", True, "ALLOW", (), group_records, plan.leftovers, ())

        commits: list[str] = []
        for group in plan.groups:
            checkpoint = IndexCheckpoint.capture(adapter)
            head_before = adapter.run(("rev-parse", "HEAD")).stdout.strip()
            commit_created = False
            try:
                if group.paths:
                    adapter.stage_paths(group.paths)
                for patch in group.patches:
                    adapter.stage_patch(patch)
                explicit_set = tuple(sorted(set(group.paths) | set(group.patch_paths)))
                expected = sorted((expected_stage_sets or {}).get(group.group_id, explicit_set))
                actual = adapter.staged_paths()
                if actual != expected:
                    raise RuntimeError(f"INDEX_SET_MISMATCH: expected={expected}, actual={actual}")
                commits.append(adapter.commit(group.message))
                commit_created = True
                self._emit_event("SEMANTIC_COMMIT_CAPTURED", "EXECUTED", adapter, authorization_ref, commit=commits[-1])
            except Exception as exc:
                if commit_created:
                    adapter.run(("reset", "--soft", head_before), mutate=True)
                    commits.pop()
                checkpoint.restore(adapter)
                self._emit_event("INDEX_ROLLBACK_COMPLETED", "ROLLED_BACK", adapter, authorization_ref, error=str(exc))
                return CommitExecutionResult(
                    "ROLLED_BACK", False, "BLOCK", tuple(commits), group_records,
                    tuple(adapter.changed_paths()), ("INDEX_SET_MISMATCH",), True,
                )

        return CommitExecutionResult(
            "EXECUTED", False, "ALLOW", tuple(commits), group_records,
            tuple(adapter.changed_paths()), (), False,
        )

    def _emit(self, event: dict[str, Any]) -> None:
        if self.trace:
            self.trace.emit(event)

    def _emit_event(
        self,
        event_type: str,
        result: str,
        adapter: GitAdapter,
        authorization_ref: str | None,
        **extra: Any,
    ) -> None:
        self._emit({
            "event_type": event_type,
            "action_id": "semantic-commit-execute",
            "target_id": str(adapter.repository),
            "authorization_ref": authorization_ref,
            "occurred_at": datetime.now(timezone.utc).isoformat(),
            "result": result,
            "grants_authorization": False,
            **extra,
        })

"""Fail-closed runtime permission evaluation."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Callable

from banyan.policy import CompiledPolicy
from .models import ActionRequest, ActionResult, ExecutionScope


RISK_TO_LEVEL = {
    "READ_ONLY": "L0",
    "REVERSIBLE_WRITE": "L1",
    "CANONICAL_WRITE": "L3",
    "PROTECTED_WRITE": "L3",
    "IRREVERSIBLE_OR_EXTERNAL": "L3",
}


class PermissionEvaluator:
    def __init__(self, policy: CompiledPolicy, now: Callable[[], str] | None = None):
        self.policy = policy
        self.now = now or (lambda: datetime.now(timezone.utc).isoformat())

    def evaluate(self, request: ActionRequest) -> ActionResult:
        operation_risks = self.policy.data["operation_risks"]
        risk = operation_risks.get(request.action_type)
        reasons: list[str] = []
        failed: list[str] = []

        if risk is None:
            risk = "PROTECTED_WRITE"
            reasons.append("UNKNOWN_ACTION_FAIL_CLOSED")
            failed.append("known_action_type")

        if request.work_mode not in {"LIGHT", "STANDARD", "FULL"}:
            reasons.append("UNKNOWN_WORK_MODE")
            failed.append("valid_work_mode")

        valid_scopes = {scope.value for scope in ExecutionScope}
        scope_value = request.execution_scope.value if isinstance(request.execution_scope, ExecutionScope) else request.execution_scope
        if scope_value not in valid_scopes:
            reasons.append("UNKNOWN_EXECUTION_SCOPE")
            failed.append("valid_execution_scope")

        required = set(self.policy.data["required_preconditions"])
        preconditions = {name: request.precondition_results.get(name) for name in required}
        preconditions.update(request.precondition_results)
        for name, result in sorted(preconditions.items()):
            if result is not True:
                failed.append(name)
                reasons.append("UNKNOWN_PRECONDITION" if result is None else "FAILED_PRECONDITION")

        if request.target_state.get("secret_risk"):
            failed.append("secret_check_passed")
            reasons.append("SECRET_RISK")
        if request.target_state.get("conflicted"):
            failed.append("conflict_free")
            reasons.append("CONFLICTED_WORKTREE")
        if request.target_state.get("authority_blocked"):
            failed.append("authority_resolved")
            reasons.append("AUTHORITY_BLOCKED")

        mutating = risk != "READ_ONLY"
        if request.execution_scope == ExecutionScope.CURRENT_PROJECT_DRY_RUN and mutating:
            reasons.append("CURRENT_PROJECT_DRY_RUN_ONLY")
        if request.execution_scope == ExecutionScope.AUTHORIZED_PROJECT_EXECUTION:
            failed.append("execution_scope_authorized")
            reasons.append("AUTHORIZED_PROJECT_EXECUTION_DISABLED")

        if mutating and not request.authorization_ref:
            failed.append("authorization_valid")
            reasons.append("MISSING_AUTHORIZATION")
        if request.action_type == "commit" and not request.target_state.get("identity_present", False):
            failed.append("identity_present")
            reasons.append("MISSING_IDENTITY_FOR_COMMIT")

        needs_input_codes = {"UNKNOWN_PRECONDITION", "MISSING_IDENTITY_FOR_COMMIT", "UNKNOWN_WORK_MODE", "UNKNOWN_EXECUTION_SCOPE"}
        if failed:
            decision = "NEEDS_INPUT" if set(reasons) <= needs_input_codes else "BLOCK"
        elif request.execution_scope == ExecutionScope.CURRENT_PROJECT_DRY_RUN and mutating:
            decision = "ALLOW"
        else:
            decision = "ALLOW"

        audit = {
            "event_type": "PERMISSION_EVALUATED",
            "action_id": request.action_id,
            "target_id": request.target_id,
            "risk_class": risk,
            "permission_result": decision,
            "authorization_ref": request.authorization_ref,
            "evidence_refs": list(request.evidence_refs),
            "occurred_at": self.now(),
            "result": decision,
            "grants_authorization": False,
        }
        return ActionResult(
            action_id=request.action_id,
            compiled_policy_hash=self.policy.policy_hash,
            risk_class=risk,
            decision_level=RISK_TO_LEVEL[risk],
            permission_result=decision,
            failed_or_missing_preconditions=tuple(sorted(set(failed))),
            reason_codes=tuple(sorted(set(reasons))),
            audit_event=audit,
            executed=False,
        )

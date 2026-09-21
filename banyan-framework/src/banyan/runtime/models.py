from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class ExecutionScope(str, Enum):
    CURRENT_PROJECT_DRY_RUN = "CURRENT_PROJECT_DRY_RUN"
    ISOLATED_FIXTURE = "ISOLATED_FIXTURE"
    AUTHORIZED_PROJECT_EXECUTION = "AUTHORIZED_PROJECT_EXECUTION"


@dataclass(frozen=True)
class ActionRequest:
    action_id: str
    action_type: str
    execution_scope: ExecutionScope
    target_id: str
    target_state: dict[str, Any] = field(default_factory=dict)
    work_mode: str = "STANDARD"
    evidence_refs: tuple[str, ...] = ()
    impact_ref: str | None = None
    decision_ref: str | None = None
    authorization_ref: str | None = None
    precondition_results: dict[str, bool | None] = field(default_factory=dict)


@dataclass(frozen=True)
class ActionResult:
    action_id: str
    compiled_policy_hash: str
    risk_class: str
    decision_level: str
    permission_result: str
    failed_or_missing_preconditions: tuple[str, ...]
    reason_codes: tuple[str, ...]
    audit_event: dict[str, Any]
    executed: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

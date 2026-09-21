from copy import deepcopy
import unittest

from banyan.policy import PolicyCompileError, PolicyCompiler, default_policy
from banyan.runtime.evaluator import PermissionEvaluator
from banyan.runtime.models import ActionRequest, ExecutionScope


def test_policy_is_deterministic_and_preserves_hard_blocks():
    compiler = PolicyCompiler()
    first = compiler.compile(default_policy())
    second = compiler.compile(deepcopy(default_policy()))
    assert first.policy_hash == second.policy_hash
    assert "SECRET_RISK" in first.data["hard_blocks"]


def test_unknown_policy_field_is_rejected():
    policy = default_policy()
    policy["surprise"] = True
    with unittest.TestCase().assertRaisesRegex(PolicyCompileError, "unknown policy fields"):
        PolicyCompiler().compile(policy)


def test_removed_hard_block_is_rejected():
    policy = default_policy()
    policy["hard_blocks"].remove("SECRET_RISK")
    with unittest.TestCase().assertRaisesRegex(PolicyCompileError, "required hard blocks removed"):
        PolicyCompiler().compile(policy)


def test_unknown_enum_and_weakened_commit_risk_are_rejected():
    policy = default_policy()
    policy["risk_classes"].append("UNKNOWN")
    with unittest.TestCase().assertRaisesRegex(PolicyCompileError, "risk_classes mismatch"):
        PolicyCompiler().compile(policy)
    policy = default_policy()
    policy["operation_risks"]["commit"] = "READ_ONLY"
    with unittest.TestCase().assertRaisesRegex(PolicyCompileError, "operation risk weakened"):
        PolicyCompiler().compile(policy)


def test_failed_precondition_never_allows():
    evaluator = PermissionEvaluator(PolicyCompiler().compile(default_policy()))
    result = evaluator.evaluate(ActionRequest(
        action_id="a", action_type="commit", execution_scope=ExecutionScope.ISOLATED_FIXTURE,
        target_id="fixture", target_state={"identity_present": True}, authorization_ref="AUTH-1",
        precondition_results={"secret_check_passed": False},
    ))
    assert result.permission_result == "BLOCK"


def test_unknown_action_fails_closed():
    evaluator = PermissionEvaluator(PolicyCompiler().compile(default_policy()))
    result = evaluator.evaluate(ActionRequest(
        action_id="a", action_type="unknown", execution_scope=ExecutionScope.ISOLATED_FIXTURE,
        target_id="fixture", authorization_ref="AUTH-1",
    ))
    assert result.permission_result == "BLOCK"
    assert "UNKNOWN_ACTION_FAIL_CLOSED" in result.reason_codes


def test_commit_requires_identity_and_authorization():
    evaluator = PermissionEvaluator(PolicyCompiler().compile(default_policy()))
    result = evaluator.evaluate(ActionRequest(
        action_id="a", action_type="commit", execution_scope=ExecutionScope.ISOLATED_FIXTURE,
        target_id="fixture", target_state={"identity_present": False},
    ))
    assert result.permission_result != "ALLOW"
    assert set(result.reason_codes) >= {"MISSING_IDENTITY_FOR_COMMIT", "MISSING_AUTHORIZATION"}

import json
import os
from pathlib import Path
import tempfile

from banyan.control_plane.service import ControlPlaneService
from banyan.editor import AdapterGateway, CodexAdapter, CursorAdapter, GenericEditorAdapter
from banyan.policy import PolicyCompiler, default_policy
from banyan.runtime.api import RuntimeAPI


REPOSITORY = Path(os.environ["BANYAN_TEST_REPOSITORY"]).resolve()


def system():
    root = Path(tempfile.mkdtemp())
    trace = root / "trace.jsonl"
    provenance = {"artifact": {"stable_id": "artifact", "classification": "TEST", "source_role": "EVIDENCE", "authority": "ADVISORY", "freshness": "CURRENT", "provenance": "test", "source_refs": ["ref"], "related_refs": []}}
    service = ControlPlaneService(RuntimeAPI(PolicyCompiler().compile(default_policy()), trace), REPOSITORY, trace_path=trace, provenance=provenance)
    gateway = AdapterGateway(service)
    return trace, CursorAdapter(gateway), CodexAdapter(gateway), GenericEditorAdapter(gateway)


def equivalent_requests(action="runtime_status", payload=None):
    payload = payload or {}
    provenance = {"stable_id": "request", "source_role": "USER_INTENT", "authority": "DECLARED", "freshness": "CURRENT", "source_refs": ["evidence-1"]}
    return (
        {"request_id": "cursor-1", "command": action, "arguments": payload, "context": provenance, "evidence_refs": ["evidence-1"]},
        {"id": "codex-1", "operation": action, "input": payload, "metadata": provenance, "evidence_refs": ["evidence-1"]},
        {"request_id": "generic-1", "action": action, "payload": payload, "provenance": provenance, "evidence_refs": ["evidence-1"]},
    )


def test_request_transformation_is_equivalent():
    _, cursor, codex, generic = system()
    transformed = [adapter.transform(raw) for adapter, raw in zip((cursor, codex, generic), equivalent_requests("project_safety"))]
    assert {item.action for item in transformed} == {"project_safety"}
    assert all(item.payload == {} for item in transformed)


def test_all_adapters_call_same_runtime_status():
    _, cursor, codex, generic = system()
    responses = [adapter.handle(raw).to_dict() for adapter, raw in zip((cursor, codex, generic), equivalent_requests())]
    assert {response["status"] for response in responses} == {"OK"}
    assert {response["result"]["compiled_policy_hash"] for response in responses} == {PolicyCompiler().compile(default_policy()).policy_hash}
    assert {response["result"]["execution_mode"] for response in responses} == {"DRY_RUN_ONLY"}


def test_adapter_capabilities_never_own_policy_canonical_or_git():
    _, cursor, codex, generic = system()
    for adapter in (cursor, codex, generic):
        value = adapter.capabilities()
        assert value["owns_permission_policy"] is False
        assert value["owns_canonical_truth"] is False
        assert value["direct_git_mutation"] is False
        assert value["runtime_api_required"] is True


def test_forbidden_git_mutation_is_runtime_blocked_for_all_adapters():
    trace, cursor, codex, generic = system()
    responses = [adapter.handle(raw) for adapter, raw in zip((cursor, codex, generic), equivalent_requests("git_mutation"))]
    for response in responses:
        assert response.status == "BLOCKED"
        decision = response.result["runtime_decision"]
        assert decision["permission_result"] == "BLOCK"
        assert decision["executed"] is False
        assert "UNKNOWN_ACTION_FAIL_CLOSED" in decision["reason_codes"]
    events = [json.loads(line) for line in trace.read_text().splitlines()]
    assert len(events) == 6
    assert all(event["grants_authorization"] is False for event in events)


def test_permission_boundary_is_identical_across_adapters():
    _, cursor, codex, generic = system()
    intent = {"action_id": "preflight", "action_type": "commit", "target_state": {"identity_present": False}, "precondition_results": {}}
    responses = [adapter.handle(raw) for adapter, raw in zip((cursor, codex, generic), equivalent_requests("preflight", intent))]
    assert {response.result["permission_result"] for response in responses} == {"BLOCK"}
    assert all(response.result["executed"] is False for response in responses)


def test_commit_plan_is_not_authorization_and_dry_run_is_not_commit():
    _, cursor, _, _ = system()
    plan_response = cursor.handle(equivalent_requests("commit_plan", {"classifications": {}})[0])
    assert plan_response.result["is_authorization"] is False
    plan = {key: plan_response.result[key] for key in ("groups", "classifications", "blocked_paths", "leftovers")}
    dry = cursor.handle(equivalent_requests("commit_dry_run", {"plan": plan, "authorization_ref": "DRY-RUN-ONLY"})[0])
    assert dry.result["status"] == "DRY_RUN"
    assert dry.result["actual_commit_created"] is False


def test_evidence_trace_and_provenance_are_preserved():
    trace, cursor, _, _ = system()
    response = cursor.handle(equivalent_requests("provenance", {"stable_id": "artifact"})[0])
    assert response.evidence_refs == ("evidence-1",)
    assert response.provenance["authority"] == "DECLARED"
    assert response.result["authority"] == "ADVISORY"
    events = [json.loads(line) for line in trace.read_text().splitlines()]
    assert events[-1]["event_type"] == "ADAPTER_REQUEST_COMPLETED"
    assert events[-1]["evidence_refs"] == ["evidence-1"]


def test_unknown_provenance_is_visible_not_filled():
    _, _, _, generic = system()
    response = generic.handle({"request_id": "unknown", "action": "runtime_status", "payload": {}, "provenance": {}})
    assert response.provenance["stable_id"] == "UNKNOWN"
    assert response.provenance["authority"] == "UNKNOWN"
    assert response.provenance["freshness"] == "UNKNOWN"


def test_malformed_requests_fail_typed_and_are_traced():
    trace, cursor, codex, generic = system()
    responses = [cursor.handle({}), codex.handle({"id": "x", "operation": "runtime_status", "surprise": True}), generic.handle({"request_id": "x", "action": "runtime_status", "payload": []})]
    assert {response.status for response in responses} == {"FAILED"}
    assert {response.result["error_code"] for response in responses} == {"ADAPTER_REQUEST_INVALID"}
    assert len(trace.read_text().splitlines()) == 3


def test_trace_query_is_paginated():
    _, cursor, _, _ = system()
    cursor.handle(equivalent_requests("runtime_status")[0])
    response = cursor.handle(equivalent_requests("trace", {"offset": 0, "limit": 1})[0])
    assert len(response.result["items"]) == 1
    assert response.result["limit"] == 1
    assert response.result["trace_is_authorization"] is False


def test_adapter_source_has_no_runtime_or_git_bypass_import():
    root = Path(__file__).parents[1] / "src" / "banyan" / "editor"
    text = "\n".join(path.read_text() for path in root.glob("*.py"))
    assert "from banyan.runtime" not in text
    assert "from banyan.git" not in text
    assert "subprocess" not in text

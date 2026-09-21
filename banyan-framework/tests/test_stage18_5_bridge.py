import json
import os
from pathlib import Path
import subprocess
import tempfile


FRAMEWORK = Path(__file__).parents[1].resolve()
REPOSITORY = Path(os.environ["BANYAN_TEST_REPOSITORY"]).resolve()


def bridge(operation, payload=None, *, provenance=None):
    root = Path(tempfile.mkdtemp())
    trace = root / "trace.jsonl"
    provenance_path = root / "provenance.json"
    provenance_path.write_text(json.dumps(provenance or {}))
    env = dict(os.environ)
    env.update({
        "PYTHONPATH": str(FRAMEWORK / "src"),
        "BANYAN_REPOSITORY": str(REPOSITORY),
        "BANYAN_POLICY": str(FRAMEWORK / "policies" / "default-policy.yaml"),
        "BANYAN_TRACE": str(trace),
        "BANYAN_PROVENANCE": str(provenance_path),
    })
    completed = subprocess.run(
        ["python3", "-m", "banyan.control_plane.bridge"],
        input=json.dumps({"operation": operation, "payload": payload or {}}),
        text=True, capture_output=True, env=env, timeout=10,
    )
    return completed, json.loads(completed.stdout), trace


def test_bridge_calls_preserved_runtime():
    completed, value, _ = bridge("status")
    assert completed.returncode == 0 and value["ok"] is True
    assert value["result"]["execution_mode"] == "DRY_RUN_ONLY"
    assert value["result"]["current_project_mutation_allowed"] is False


def test_bridge_failure_is_typed_and_fail_closed():
    completed, value, _ = bridge("not-an-operation")
    assert completed.returncode == 1 and value["ok"] is False
    assert value["error"]["code"] == "RUNTIME_BRIDGE_FAILURE"


def test_secret_negative_and_unknown_provenance():
    records = {
        "secret": {"stable_id": "secret", "classification": "SECRET", "existence": True, "path": "restricted", "body": "never-expose", "hash": "never-expose"},
        "unknown": {"stable_id": "unknown", "classification": "PUBLIC"},
    }
    _, secret, _ = bridge("provenance_query", {"stable_id": "secret"}, provenance=records)
    serialized = json.dumps(secret)
    assert "never-expose" not in serialized and secret["result"]["secret_body_rendered"] is False
    _, unknown, _ = bridge("provenance_query", {"stable_id": "unknown"}, provenance=records)
    assert unknown["result"]["freshness"] == "UNKNOWN"
    assert unknown["result"]["authority"] == "UNKNOWN"


def test_three_adapters_regress_through_bridge():
    requests = {
        "cursor": {"request_id": "c", "command": "git_mutation", "arguments": {}, "context": {}, "evidence_refs": ["e"]},
        "codex": {"id": "d", "operation": "git_mutation", "input": {}, "metadata": {}, "evidence_refs": ["e"]},
        "generic-editor": {"request_id": "g", "action": "git_mutation", "payload": {}, "provenance": {}, "evidence_refs": ["e"]},
    }
    for kind, request in requests.items():
        completed, value, trace = bridge("adapter_request", {"adapter": kind, "request": request})
        assert completed.returncode == 0 and value["result"]["status"] == "BLOCKED"
        assert value["result"]["result"]["runtime_decision"]["executed"] is False
        assert value["result"]["evidence_refs"] == ["e"]
        events = [json.loads(line) for line in trace.read_text().splitlines()]
        assert events and all(event.get("grants_authorization") is False for event in events)


def test_go_transport_contains_no_policy_or_git_implementation():
    root = FRAMEWORK / "control-plane-go"
    text = "\n".join(path.read_text() for path in root.rglob("*.go") if not path.name.endswith("_test.go"))
    assert "PermissionPolicy" not in text
    assert "git commit" not in text
    assert "os/exec" not in (root / "internal" / "controlplane" / "http" / "router.go").read_text()

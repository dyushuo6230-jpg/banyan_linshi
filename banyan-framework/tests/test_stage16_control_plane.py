import json
import os
from pathlib import Path
import tempfile
from threading import Thread
import urllib.error
import urllib.request

from banyan.control_plane.server import ControlPlaneApplication, create_server, validate_bind_host
from banyan.control_plane.service import ControlPlaneService
from banyan.policy import PolicyCompiler, default_policy
from banyan.runtime.api import RuntimeAPI


REPOSITORY = Path(os.environ["BANYAN_TEST_REPOSITORY"]).resolve()


def service():
    root = Path(tempfile.mkdtemp())
    providers = root / "providers.json"
    providers.write_text(json.dumps({"bindings": [{"id": "local", "provider": "filesystem", "enabled": True}]}))
    trace = root / "trace.jsonl"
    runtime = RuntimeAPI(PolicyCompiler().compile(default_policy()), trace)
    return ControlPlaneService(
        runtime,
        REPOSITORY,
        trace_path=trace,
        provider_path=providers,
        provenance={
            "artifact-1": {"stable_id": "artifact-1", "classification": "PUBLIC", "source_role": "REFERENCE", "authority": "ADVISORY"},
            "secret-1": {"stable_id": "secret-1", "path": "restricted/item", "classification": "SECRET", "existence": True, "restriction_flags": ["NO_BODY"], "body": "must-never-render", "hash": "must-never-render"},
        },
        stages=[{"stage": "15", "run_id": "run-15", "status": "COMPLETED"}, {"stage": "16", "run_id": "run-16", "status": "RUNNING"}],
    )


def test_status_and_policy_are_runtime_backed():
    value = service().status()
    assert value["runtime_health"] == "HEALTHY"
    assert value["execution_mode"] == "DRY_RUN_ONLY"
    assert value["current_project_mutation_allowed"] is False
    assert service().policy_status()["control_plane_may_bypass"] is False


def test_preflight_ui_click_does_not_create_authorization():
    value = service().preflight({
        "action_id": "x", "action_type": "commit", "ui_confirmed": True,
        "target_state": {"identity_present": True},
        "precondition_results": {"evidence_complete": True, "impact_reviewed": True, "authorization_valid": False, "secret_check_passed": True, "freshness_valid": True, "rollback_ready": True},
    })
    assert value["permission_result"] == "BLOCK"
    assert value["ui_confirmation_is_authorization"] is False


def test_project_safety_exposes_presence_not_identity_values():
    value = service().project_safety()
    serialized = json.dumps(value)
    assert "identity_present" in value and "identity_ambiguous" in value
    assert "user.name" not in serialized and "user.email" not in serialized
    assert value["identity_values_exposed"] is False


def test_secret_view_is_metadata_only():
    value = service().provenance_view("secret-1")
    assert value["secret_body_rendered"] is False
    assert "body" not in value and "hash" not in value
    assert set(value) <= {"stable_id", "path", "classification", "existence", "restriction_flags", "secret_body_rendered"}


def test_provenance_preserves_unknown_fields():
    value = service().provenance_view("artifact-1")
    assert value["freshness"] == "UNKNOWN"
    assert value["provenance"] == "UNKNOWN"
    assert value["authority"] == "ADVISORY"
    assert value["source_refs"] == [] and value["related_refs"] == []


def test_plan_is_not_authorization_and_dry_run_does_not_mutate():
    current = service()
    head_before = (REPOSITORY / ".git" / "HEAD").read_bytes()
    index_before = (REPOSITORY / ".git" / "index").read_bytes()
    plan = current.commit_plan({"classifications": {}})
    assert plan["is_authorization"] is False
    typed_plan = {key: plan[key] for key in ("groups", "classifications", "blocked_paths", "leftovers")}
    result = current.commit_dry_run({"plan": typed_plan, "authorization_ref": "STAGE16-DRY-RUN"})
    assert result["display_label"] == "DRY_RUN_NOT_COMMIT"
    assert result["actual_commit_created"] is False
    assert (REPOSITORY / ".git" / "HEAD").read_bytes() == head_before
    assert (REPOSITORY / ".git" / "index").read_bytes() == index_before


def test_activation_readiness_never_creates_dot_banyan():
    target = REPOSITORY / ".banyan"
    assert not target.exists()
    value = service().activation_readiness()
    assert value["state"] == "BLOCKED"
    assert value["stage16_may_activate_dot_banyan"] is False
    assert not target.exists()


def test_local_bind_rejects_public_and_non_loopback():
    assert validate_bind_host("127.0.0.1") == "127.0.0.1"
    assert validate_bind_host("localhost") == "localhost"
    for host in ("0.0.0.0", "192.0.2.1", "example.invalid"):
        try:
            validate_bind_host(host)
            raise AssertionError("unsafe bind was accepted")
        except ValueError:
            pass


def test_api_contract_has_no_mutating_route():
    app = ControlPlaneApplication(service())
    assert app.dispatch("GET", "/api/status")[0] == 200
    assert app.dispatch("POST", "/api/commit/execute", {}) == (404, {"error": "NOT_FOUND"})
    assert app.dispatch("POST", "/api/activate", {}) == (404, {"error": "NOT_FOUND"})


def test_trace_and_stage_surfaces_are_paginated():
    current = service()
    current.preflight({
        "action_id": "trace", "action_type": "inspect",
        "precondition_results": {"evidence_complete": True, "impact_reviewed": True, "authorization_valid": True, "secret_check_passed": True, "freshness_valid": True, "rollback_ready": True},
    })
    trace = current.trace(offset=0, limit=1)
    stages = current.stages(offset=0, limit=1)
    assert len(trace["items"]) == 1 and trace["trace_is_authorization"] is False
    assert len(stages["items"]) == 1 and stages["has_more"] is True


def test_http_and_ui_browser_smoke():
    server = create_server(service(), port=0)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    try:
        html = urllib.request.urlopen(base + "/", timeout=3).read().decode()
        status = json.loads(urllib.request.urlopen(base + "/api/status", timeout=3).read())
        assert "Activation Readiness" in html and "Dry-run Result" in html and "Provenance" in html
        assert status["execution_mode"] == "DRY_RUN_ONLY"
        try:
            urllib.request.urlopen(urllib.request.Request(base + "/api/commit/execute", data=b"{}", method="POST", headers={"Content-Type": "application/json"}), timeout=3)
            raise AssertionError("mutation endpoint unexpectedly exists")
        except urllib.error.HTTPError as exc:
            assert exc.code == 404
    finally:
        server.shutdown()
        server.server_close()


def test_webui_has_required_views_and_no_execute_control():
    root = Path(__file__).parents[1] / "src" / "banyan" / "web"
    html = (root / "index.html").read_text()
    script = (root / "app.js").read_text()
    for label in ("Dashboard", "Runtime / Policy", "Project Safety", "Gate / Blockers", "Preflight", "Commit Plan", "Dry-run Result", "Trace / Audit", "Provenance", "Provider Bindings", "Stage / Run", "Activation Readiness"):
        assert label in html
    assert "/api/commit/execute" not in script
    assert "/api/activate" not in script

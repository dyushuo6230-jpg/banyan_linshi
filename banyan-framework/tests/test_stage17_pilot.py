import json
import os
from pathlib import Path
import tempfile
import unittest

import yaml

from banyan.control_plane.service import ControlPlaneService
from banyan.cursor.adapter import CursorPilotAdapter
from banyan.pilot.instance import PilotActivationCoordinator, PilotValidationError
from banyan.policy import PolicyCompiler, default_policy
from banyan.runtime.api import RuntimeAPI


REPOSITORY = Path(os.environ["BANYAN_TEST_REPOSITORY"]).resolve()
SHADOW = Path(os.environ["BANYAN_STAGE17_SHADOW"]).resolve()


def coordinator(trace_path: Path):
    runtime = RuntimeAPI(PolicyCompiler().compile(default_policy()), trace_path)
    service = ControlPlaneService(runtime, REPOSITORY, trace_path=trace_path)
    adapter = CursorPilotAdapter(service)
    return adapter, PilotActivationCoordinator(adapter)


def test_cursor_adapter_has_no_policy_canonical_or_git_authority():
    adapter, _ = coordinator(Path(tempfile.mkdtemp()) / "trace.jsonl")
    assert adapter.capabilities() == {
        "owns_permission_policy": False,
        "owns_canonical_truth": False,
        "direct_git_mutation": False,
        "direct_project_write": False,
        "calls_control_plane": True,
    }


def test_preflight_runs_through_runtime_and_trace():
    trace = Path(tempfile.mkdtemp()) / "trace.jsonl"
    _, current = coordinator(trace)
    result = current.preflight("AUTH", "CHECKPOINT")
    assert result["permission_result"] == "ALLOW"
    assert result["pilot_scope_authorized"] is True
    assert result["general_project_write_allowed"] is False
    assert result["executed"] is False
    assert "CURRENT_PROJECT_DRY_RUN_ONLY" in result["reason_codes"]
    event = json.loads(trace.read_text().splitlines()[0])
    assert event["event_type"] == "PERMISSION_EVALUATED"
    assert event["grants_authorization"] is False


def test_shadow_validates_and_preserves_unknown():
    _, current = coordinator(Path(tempfile.mkdtemp()) / "trace.jsonl")
    result = current.validate_shadow(SHADOW)
    assert result["valid"] and result["file_count"] >= 10
    project = yaml.safe_load((SHADOW / "profiles/project.yaml").read_text())
    mapping = yaml.safe_load((SHADOW / "mappings/source-mappings.yaml").read_text())
    assert project["canonical_authority"] == "UNKNOWN"
    assert mapping["mappings"][1]["freshness"] == "UNKNOWN"


def test_shadow_contains_no_identity_values_or_secret_body_keys():
    _, current = coordinator(Path(tempfile.mkdtemp()) / "trace.jsonl")
    assert current.validate_shadow(SHADOW)["valid"]
    text = "\n".join(path.read_text() for path in SHADOW.rglob("*") if path.is_file())
    assert "user_name:" not in text and "user_email:" not in text
    assert "secret_body:" not in text and "secret_hash:" not in text


def test_forbidden_sensitive_key_is_rejected():
    root = Path(tempfile.mkdtemp())
    for directory in ("instance", "mappings", "providers", "runtime", "migrations"):
        (root / directory).mkdir()
    (root / "PILOT_NOTICE.md").write_text("pilot")
    (root / "pilot.yaml").write_text("secret_body: forbidden\n")
    _, current = coordinator(root / "trace.jsonl")
    with unittest.TestCase().assertRaisesRegex(PilotValidationError, "forbidden sensitive keys"):
        current.validate_shadow(root)


def test_activation_requires_runtime_allow_checkpoint_and_authorization():
    _, current = coordinator(Path(tempfile.mkdtemp()) / "trace.jsonl")
    target = Path(tempfile.mkdtemp()) / ".banyan"
    with unittest.TestCase().assertRaisesRegex(PilotValidationError, "did not allow"):
        current.activate(SHADOW, target, preflight_result={"permission_result": "BLOCK", "executed": False, "pilot_scope_authorized": False}, checkpoint_ref="C", authorization_ref="A")
    assert not target.exists()


def test_scoped_pilot_creation_copies_only_validated_shadow():
    trace = Path(tempfile.mkdtemp()) / "trace.jsonl"
    _, current = coordinator(trace)
    preflight = current.preflight("AUTH", "CHECKPOINT")
    target = Path(tempfile.mkdtemp()) / ".banyan"
    result = current.activate(SHADOW, target, preflight_result=preflight, checkpoint_ref="CHECKPOINT", authorization_ref="AUTH")
    assert result["pilot_created"] and result["final_activation"] is False
    assert result["canonical_replacement"] is False
    assert (target / "pilot.yaml").exists()
    assert not (target / ".git").exists()


def test_existing_pilot_cannot_be_overwritten():
    _, current = coordinator(Path(tempfile.mkdtemp()) / "trace.jsonl")
    target = Path(tempfile.mkdtemp()) / ".banyan"
    target.mkdir()
    with unittest.TestCase().assertRaisesRegex(PilotValidationError, "already exists"):
        current.activate(SHADOW, target, preflight_result={"permission_result": "ALLOW", "executed": False, "pilot_scope_authorized": True, "general_project_write_allowed": False}, checkpoint_ref="C", authorization_ref="A")


def test_existing_project_layout_is_preserve_in_place():
    data = yaml.safe_load((SHADOW / "pilot.yaml").read_text())
    assert data["existing_project_layout"] == "PRESERVE_IN_PLACE"
    assert data["docs_project_migration"] == "NOT_PERFORMED"
    assert data["legacy_deletion"] == "NOT_PERFORMED"


def test_activation_review_requires_runtime_scoped_gate():
    trace = Path(tempfile.mkdtemp()) / "trace.jsonl"
    _, current = coordinator(trace)
    preflight = current.preflight("AUTH", "CHECKPOINT")
    review = current.review_existing_pilot(SHADOW, SHADOW, preflight_result=preflight)
    assert review["result"] == "PASS_PILOT_ONLY"
    assert review["final_activation"] is False

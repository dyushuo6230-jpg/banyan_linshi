"""Static conformance expectations for Stage 18.5 outputs."""

REQUIRED_FEATURES = {
    "dashboard", "runtime_policy", "project_safety", "gate_blockers",
    "preflight", "commit_plan", "dry_run_result", "trace_audit",
    "provenance", "provider_bindings", "stage_run", "activation_readiness",
}

ALLOWED_DISPOSITIONS = {
    "EQUIVALENT", "IMPROVED_COMPATIBLY",
    "DEFERRED_WITH_REASON", "REMOVED_BY_EXPLICIT_DECISION",
}

FORBIDDEN_ARCHITECTURE_FLAGS = {
    "second_permission_engine",
    "public_bind_default",
    "project_git_mutation",
    "pilot_dot_banyan_mutation",
    "node_required_to_serve_release_ui",
}

def validate_feature_matrix(rows):
    ids = {r["id"] for r in rows}
    assert ids == REQUIRED_FEATURES
    for row in rows:
        assert row["disposition"] in ALLOWED_DISPOSITIONS

def validate_flags(flags):
    bad = FORBIDDEN_ARCHITECTURE_FLAGS & {k for k,v in flags.items() if v}
    assert not bad, sorted(bad)

if __name__ == "__main__":
    rows = [{"id": x, "disposition": "EQUIVALENT"} for x in REQUIRED_FEATURES]
    validate_feature_matrix(rows)
    validate_flags({})
    print("PASS Stage18.5 architecture conformance spec")

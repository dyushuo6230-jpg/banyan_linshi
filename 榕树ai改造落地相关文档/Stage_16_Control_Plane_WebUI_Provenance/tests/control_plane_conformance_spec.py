"""Stage 16 conformance helper. Does not start servers or mutate repositories."""

REQUIRED_SURFACES = {
    "runtime_status",
    "policy_status",
    "project_safety",
    "preflight",
    "commit_plan",
    "commit_dry_run",
    "trace",
    "provenance",
    "providers",
    "stages",
    "activation_readiness",
}

FORBIDDEN_STAGE16_CAPABILITIES = {
    "current_project_git_mutation",
    "canonical_apply",
    "secret_body_render",
    "public_bind_default",
    "dot_banyan_activation",
}

def validate_manifest(surfaces, capabilities):
    missing = REQUIRED_SURFACES - set(surfaces)
    assert not missing, f"missing surfaces: {sorted(missing)}"
    bad = FORBIDDEN_STAGE16_CAPABILITIES & set(capabilities)
    assert not bad, f"forbidden capabilities: {sorted(bad)}"

if __name__ == "__main__":
    validate_manifest(REQUIRED_SURFACES, set())
    print("PASS Stage16 control-plane conformance spec")

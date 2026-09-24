REQUIRED_DOMAINS = {
    "architecture","purity","runtime_policy_git","webui_gogin_bridge",
    "adapters","pilot","index_trace_provenance","freshness","noloss","rc_build",
}
HARD_METRICS = {
    "ACCEPTANCE_CLAIM_WITHOUT_EVIDENCE",
    "GENERIC_CORE_PROJECT_LITERAL_LEAK",
    "SECOND_PERMISSION_ENGINE_PRESENT",
    "POLICY_HARD_BLOCK_REGRESSION",
    "RUNTIME_FAIL_OPEN_PATH",
    "GOGIN_POLICY_REIMPLEMENTATION",
    "RUNTIME_BRIDGE_FAIL_OPEN_PATH",
    "WEBUI_FEATURE_REGRESSION",
    "ADAPTER_COMPATIBILITY_REGRESSION",
    "CURRENT_PROJECT_GIT_MUTATION",
    "PILOT_DOT_BANYAN_MUTATION",
    "SECRET_BODY_ACCESS_OR_EXPOSURE",
    "TRACE_WITHOUT_EVIDENCE_LINK_WHEN_REQUIRED",
    "PROVENANCE_UNKNOWN_SYNTHESIZED",
    "NOLOSS_COVERAGE_REGRESSION",
    "RC_REPRODUCIBILITY_FAILURE",
}
def validate(domains, metrics):
    assert REQUIRED_DOMAINS <= set(domains)
    assert HARD_METRICS == set(metrics)
    assert all(v == 0 for v in metrics.values())
if __name__ == "__main__":
    validate(REQUIRED_DOMAINS, {x:0 for x in HARD_METRICS})
    print("PASS Stage19 conformance spec")

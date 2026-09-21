from test_stage18_5_bridge import (
    test_bridge_calls_preserved_runtime,
    test_bridge_failure_is_typed_and_fail_closed,
    test_go_transport_contains_no_policy_or_git_implementation,
    test_secret_negative_and_unknown_provenance,
    test_three_adapters_regress_through_bridge,
)


TESTS = [value for name, value in sorted(globals().items()) if name.startswith("test_")]

if __name__ == "__main__":
    failed = 0
    for test in TESTS:
        try:
            test()
            print("PASS", test.__name__)
        except Exception as exc:
            failed += 1
            print("FAIL", test.__name__, repr(exc))
    print(f"RESULT passed={len(TESTS)-failed} failed={failed}")
    raise SystemExit(1 if failed else 0)

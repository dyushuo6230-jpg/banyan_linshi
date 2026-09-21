from test_policy_runtime import *
from test_executor_integration import *
from test_adapters_planner import *
from test_trace_provider import test_trace_is_append_only_and_validated
from test_stage18_5_bridge import *
from test_stage18_adapters import *

TESTS = [v for k,v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
if __name__ == "__main__":
    failed=[]
    for test in TESTS:
        try:
            test(); print("PASS", test.__name__)
        except Exception as exc:
            failed.append((test.__name__,repr(exc))); print("FAIL",test.__name__,repr(exc))
    print(f"RESULT passed={len(TESTS)-len(failed)} failed={len(failed)} total={len(TESTS)}")
    raise SystemExit(1 if failed else 0)

"""Dependency-free test runner for Stage 15 validation."""

from __future__ import annotations

import importlib
import inspect
import sys
import traceback


MODULES = [
    "test_policy_runtime",
    "test_adapters_planner",
    "test_trace_provider",
    "test_executor_integration",
]


def main() -> int:
    passed = 0
    failed = 0
    for module_name in MODULES:
        module = importlib.import_module(module_name)
        for name, function in inspect.getmembers(module, inspect.isfunction):
            if not name.startswith("test_"):
                continue
            try:
                function()
                print(f"PASS {module_name}.{name}")
                passed += 1
            except Exception:
                print(f"FAIL {module_name}.{name}")
                traceback.print_exc()
                failed += 1
    print(f"RESULT passed={passed} failed={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())

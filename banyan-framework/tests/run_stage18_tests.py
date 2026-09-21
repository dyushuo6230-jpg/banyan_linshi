"""Dependency-free Stage 18 adapter compatibility test runner."""

from __future__ import annotations

import inspect
import traceback

import test_stage18_adapters as suite


def main() -> int:
    passed = failed = 0
    for name, function in inspect.getmembers(suite, inspect.isfunction):
        if not name.startswith("test_"):
            continue
        try:
            function()
            print(f"PASS {name}")
            passed += 1
        except Exception:
            print(f"FAIL {name}")
            traceback.print_exc()
            failed += 1
    print(f"RESULT passed={passed} failed={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())

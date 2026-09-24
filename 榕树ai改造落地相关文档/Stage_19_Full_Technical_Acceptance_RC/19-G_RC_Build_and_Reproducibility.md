# 19-G RC Build / Reproducibility

Build the release-candidate framework artifacts using documented commands.

Verify:

```text
frontend build
embedded asset manifest
Go web binary build
Python package/runtime tests
Go tests
adapter tests
deterministic/reproducible manifests where defined
release smoke
local-only launch
```

RC artifact ≠ final activation.

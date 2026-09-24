# Stage 03 — ACCEPTANCE REPORT TEMPLATE

> 仅模板。真实执行后生成 `ACCEPTANCE_REPORT.md`。

## Result

- Run ID:
- Upstream Stage 02:
- Result:
- HEAD:
- Drift:

## Contract Freeze Summary

- 35 Capability accounted:
- Frozen:
- Deferred with owner:
- Project overlay contracts:
- Provider port contracts:
- Compatibility contracts:

## Schema Outputs

- Canonical Contract Schema:
- Capability Registry:
- Source Role Schema:
- Artifact Registry Schema:
- Provider Port Schema:
- Project Overlay Schema:
- Reference Integrity:
- Version/Status/Provenance:
- Bootstrap Canonical Contract:
- Existing Layout Contract:
- AI Runtime Governance Contract:

## Hard Metrics

```text
UNMAPPED_HIGH_VALUE_CAPABILITY =
UNOWNED_SCHEMA_COLLISION =
SOURCE_ROLE_WITHOUT_AUTHORITY_RULE =
CONTRACT_WITHOUT_FAILURE_SEMANTICS =
SILENT_CAPABILITY_DROP =
PROJECT_PATH_HARDCODED_IN_CORE_SCHEMA =
```

## Validation

V03-01～V03-20。

## Protected Scope

确认：

```text
13 Secret body untouched
Git identity unchanged
business code untouched
canonical project docs untouched
existing project layout unchanged
no .banyan activation
no migration execution
```

## Open Risks

逐项 owner + blocker before activation。

## NEXT_STAGE_HANDOFF

Stage 04 must consume frozen Stage 03 contracts, not Stage 02 candidate assumptions.

## Stage 04 Entry Gate

PASS / FAIL

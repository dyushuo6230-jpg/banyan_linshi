# RP1 Handover Checkpoint

> **Pack**：`Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0`  
> **Document role**：CONSTRUCTION_EVIDENCE  
> **Runtime / Registry / Semantic authority**：false  
> **Stage completed**：RP1 Framework Artifact Shadow Materialization  
> **RP1 status**：PASS  
> **Next stage only**：RP2 — Artifact Discovery / Registry / Package Alignment

This checkpoint is resumable construction evidence. It is not Artifact Semantic Source.

---

## Frozen facts after RP1

```text
RP1 Artifact files          = SHADOW
authority_class             = NON_AUTHORITATIVE_SHADOW_MATERIALIZATION
CANONICAL_SOURCE            = false
Authority Cutover           = NOT DONE
Registry Cutover            = NOT DONE
Loader Cutover              = NOT DONE
Packaging / Wheel Cutover   = NOT DONE
CLI Artifact Discovery      = NOT DONE
CURRENT                     = unchanged (v1.9.1_FINAL_FREEZE)
Final Activation            = unchanged (NOT_AUTHORIZED)
.banyan                     = unchanged (PILOT_SHADOW)
R0                          = PASS (preserved)
R1                          = PASS (preserved)
migration_artifacts.yaml    = still AUTHORITATIVE R1 registry until RP2
```

43/43 shadow files exist under `banyan-framework/artifacts/**`. Semantic equivalence against the R1 registry is 43/43. Loader still does not read `artifacts/**`. Wheel package-data still excludes `artifacts/**`.

---

## What RP2 is allowed to do

RP2 is the controlled cutover window. Only RP2 may:

- make `artifacts/**` the Artifact Semantic Source
- reframe `migration_artifacts.yaml` to lineage / index / projection
- align Manifest / Schema / Loader / CLI / Wheel
- add `banyan artifact list/show/validate/refs`
- prove clean-room discovery and `runtime_dependency_on_v3_1 = 0`

RP2 must still produce PLAN_CONFORMANCE_CHECK and must not silently create dual Canonical bodies.

---

## What this checkpoint forbids

- Do not start RP2 automatically from RP1 Implementation.
- Do not treat shadow files as Canonical because they now exist.
- Do not delete `.banyan` and re-init.
- Do not follow the old R1 handover sentence that stops before cancelled R2/R3.
- Do not close HD-CLEANUP-001 or HD-CLEANUP-003 as a side effect of RP1 PASS.

---

## Inputs RP2 must read

1. This pack, including `01_decisions/`, `02_mapping/`, and `03_acceptance/`
2. Unique remediation baseline v2.0
3. Current `banyan.registry.migration_artifacts.v1`
4. Current Loader / Manifest / `pyproject.toml` (still R0/R1 authority)

RP1 Implementation is complete. Ready for RP1 Acceptance Review. Stop here.

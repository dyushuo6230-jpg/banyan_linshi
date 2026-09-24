# RP1 Shadow Materialization Acceptance Report

> **Pack**：`Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0`  
> **Document role**：CONSTRUCTION_EVIDENCE  
> **Runtime / Registry / Semantic authority**：false  
> **Stage**：RP1 — Framework Artifact Shadow Materialization  
> **Baseline**：`BANYAN-UNIQUE-REMEDIATION-BASELINE-2026-09-21-V2`  
> **Status**：`PASS`  
> **Date**：2026-09-21

This report is stage acceptance narrative. It is not Artifact Semantic Source, not Registry authority, and not a Loader/Runtime input.

---

## Result

```text
RP1_STATUS = PASS
PLAN_CONFORMANCE_CHECK = PASS
SHADOW_ARTIFACTS_CREATED = 43/43
TEST_FILES_CREATED = 2/2
ACCEPTANCE_FILES_CREATED = 10/10
R0 = PASS
R1 = PASS
RP1 = PASS
SEMANTIC_EQUIVALENCE = 43/43
UNAUTHORIZED_NEW_SEMANTIC = 0
DANGLING_REFERENCE_INTRODUCED = 0
DELETE_COUNT = 0
AUTHORITY_CUTOVER = false
LOADER_CUTOVER = false
WHEEL_CUTOVER = false
REGISTRY_CUTOVER = false
RUNTIME_CUTOVER = false
DOT_BANYAN_CHANGED = false
```

RP1 created 43 independent YAML files under `banyan-framework/artifacts/**` as:

```text
NON_AUTHORITATIVE_SHADOW_MATERIALIZATION
```

Current semantic authority remains `banyan.registry.migration_artifacts.v1`. Creating these files is not Canonical, Registry, Loader, Runtime, or Packaging cutover.

---

## What was implemented

1. Nine frozen category directories under `banyan-framework/artifacts/`.
2. Exactly 43 YAML shadow files, mapped 1:1 from `RP1_SHADOW_PATH_MAPPING.yaml` to matching R1 `artifact_id` entries.
3. Additive tests:
   - `banyan-framework/tests/test_rp1_shadow_materialization.py` (V-01 through V-22)
   - `banyan-framework/tests/run_rp1_tests.py`
4. This pack’s `03_acceptance/` evidence set (10 files).

Physical filenames use kebab-case (`v3_1` → `v3-1` in filenames only). Internal `id` / `artifact_id` / provenance / references keep R1 original values.

Each file is Thin-plus-contract: CURRENT §8 metadata + complete `r1_record` + that entry’s existing `contract` when present. YAML anchors from the registry were expanded to in-file values. Whole registry bodies were not copied.

---

## Preflight freeze (unchanged after implementation)

| File | SHA-256 before and after |
|---|---|
| `migration_artifacts.yaml` | `40252e863411173b73e37d0562c9a128b6d14ebad32efdcc9d9f6d885ec4c1c6` |
| `manifest.yaml` | `dbd835b3110a01909c3beb92d14d0b3dad7f6fadc1cbd5259f1c647fc61e28a1` |
| `schema_index.yaml` | `91e28273b7382438dc46cb14e936e7d469db2ba286741feb60fd783cb5777d78` |
| `loader.py` | `15f4a4c42ecd67026fdda2306b4154b4bb5be8bb72ddfa1beb2adab3e59b8d74` |
| `cli.py` | `905a0d01b5e3a11a3016bb9a80156d2c665b40ee568d003556ab38bc8ba7c9e2` |
| `pyproject.toml` | `5e3dde4ac4c38ce684dc6461f990463c11e9d9edce73567266f88411f37c943d` |
| `.banyan/**` tree (13 files) | `6e4b8d69d1f9df8651cd990f25aa3a4d6bf36ad64412615c0d094ad9efab9c56` |

Manifest still declares 11 assets. Loader still reads `contracts/data` only. `pyproject.toml` package-data is still `banyan.contracts.data: *.yaml, compatibility/*.yaml`. CLI still has `contracts list/validate` and no `artifact list/show/validate/refs`.

---

## Validation

| Gate | Result |
|---|---|
| V-01 paths exist | PASS |
| V-02 YAML count exactly 43 | PASS |
| V-03 YAML parse | PASS |
| V-04 Shadow authority | PASS |
| V-05 ID fidelity | PASS |
| V-06 type/directory | PASS |
| V-07 filename convention | PASS |
| V-08 metadata complete | PASS |
| V-09 UNKNOWN / NOT_APPLICABLE | PASS |
| V-10 SKILL special case | PASS |
| V-11 ROLE SOURCE_ROLE_ONLY | PASS |
| V-12 12 State Domains unmerged | PASS |
| V-13 R1 semantic equality | PASS |
| V-14 Thin-plus-contract | PASS |
| V-15 no fat-copy registry | PASS |
| V-16 UNKNOWN is not authorization | PASS |
| V-17 no new Artifact semantics | PASS |
| V-18 references remain Registry | PASS |
| V-19 no authority cutover | PASS |
| V-20 R0/R1 regression | PASS 16/16 and 22/22 |
| V-21 `.banyan` unchanged | PASS |
| V-22 DELETE_COUNT = 0 | PASS |

Command results are recorded in `RP1_REGRESSION_RESULT.yaml`. Framework runtime suites (Stage 15–18.5) and Go Control Plane tests also passed in this environment.

---

## Explicit non-claims

RP1 did **not**:

- switch Artifact Semantic Authority to `artifacts/**`
- change Loader / CLI / wheel / Manifest / Schema
- modify `.banyan`, CURRENT, Final Activation, or Legacy v3.1
- delete any file
- copy Skill bodies into Framework Core
- execute Cleanup Candidates or UNKNOWN deletions
- enter RP2

Carried gaps, including HD-CLEANUP-001 and HD-CLEANUP-003, remain open. See `RP1_GAP_DELTA.yaml`.

---

## Next

Next stage is **RP2 — Artifact Discovery / Registry / Package Alignment**.

RP1 Implementation is complete and ready for RP1 Acceptance Review. This report does not start RP2.

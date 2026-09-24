# RP1 Implementation Preparation

> **Pack**：`Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0`  
> **Document role**：CONSTRUCTION_EVIDENCE  
> **Runtime / Registry / Semantic authority**：false  
> **Status**：APPROVED_WITH_PACK_LOCATION_CORRECTION  
> **Source**：RP1 IMPLEMENTATION PREPARATION chat, then Human Authority corrected construction-evidence location.  
> **Artifact technical scheme**：unchanged.

This file is the approved implementation-preparation record. It does not authorize Loader, Registry, Runtime, CLI, wheel, or `.banyan` changes. It does not start RP1 Implementation.

Construction evidence for RP1 lives in this pack. Existing R0/R1 files under `banyan-framework/docs/maintainer/` stay in place and are not moved or deleted. New RP1 Plan / Cleanup / Human Decision / Acceptance / Handoff files must not be created there.

---

## 0. Location correction

All RP1 construction-governance / acceptance files that the preparation chat first placed at:

```text
banyan-framework/docs/maintainer/RP1_*
```

are relocated to:

```text
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/
```

This location change does not change:

- the 43 artifact mappings
- kebab-case physical filenames
- Thin-plus-contract
- `authority_class: NON_AUTHORITATIVE_SHADOW_MATERIALIZATION`
- Loader / Registry / CLI / wheel / `.banyan` freeze

`03_acceptance/` files listed below are **future Implementation outputs**. They must not be fabricated in the preparation round.

---

## 1. RP1 construction package file inventory

Two moments:

### 1.1 Preparation round (this pack materialization)

Only the six files under `00_preparation/`, `01_decisions/`, and `02_mapping/`.

### 1.2 Future Implementation round

| Group | Count | Role |
|---|---:|---|
| A. Shadow Artifact YAML | 43 | Non-authoritative projections under `banyan-framework/artifacts/**` |
| B. Additive tests | 2 | Shadow validation; do not edit existing R0/R1 test files |
| C. Construction governance / acceptance evidence | 10 | Universal RP outputs, written into this pack `03_acceptance/` |
| **Future new files** | **55** | Plus 9 frozen category directories created by writing YAML |

`DELETE_COUNT = 0`. No modification of existing Framework files. No wheel / Loader / Registry change.

This pack already holds mapping, template, decisions, and the pre-construction review, so Implementation does not recreate `RP1_HUMAN_DECISIONS.yaml`, `RP1_SHADOW_PATH_MAPPING.yaml`, or the template.

---

## 2. Exact paths for construction governance files

Future Implementation may create these under `03_acceptance/` **after** shadow files and tests exist. Do not create them now.

| # | Exact path | Baseline output | Authority |
|---|---|---|---|
| 1 | `榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/RP1_SHADOW_MATERIALIZATION_ACCEPTANCE_REPORT.md` | Acceptance Report | Stage acceptance narrative; not Artifact semantic source |
| 2 | `.../03_acceptance/RP1_PLAN_CONFORMANCE_CHECK.yaml` | PLAN_CONFORMANCE_CHECK | Construction conformance record |
| 3 | `.../03_acceptance/RP1_GAP_DELTA.yaml` | Gap Delta | Includes HD-CLEANUP-003 and other carried gaps |
| 4 | `.../03_acceptance/RP1_CHANGED_FILES.yaml` | Changed Files | Lists files **created** in Implementation |
| 5 | `.../03_acceptance/RP1_CLEANUP_DELTA.yaml` | Cleanup Delta | Must be `deleted: []` |
| 6 | `.../03_acceptance/RP1_REGRESSION_RESULT.yaml` | Regression Result | R0/R1/RP1 test results |
| 7 | `.../03_acceptance/RP1_NEW_PROPOSAL_REGISTER.yaml` | New Proposals | Non-authoritative; expected `new_proposals: []` |
| 8 | `.../03_acceptance/RP1_ROLLBACK_PLAN.md` | Rollback Plan | Remove Implementation-created `artifacts/**`, tests, and `03_acceptance/` outputs |
| 9 | `.../03_acceptance/RP1_HANDOVER_CHECKPOINT.md` | Next-stage Handoff | Next stage = RP2; Shadow ≠ Cutover |
| 10 | `.../03_acceptance/RP1_SEMANTIC_EQUIVALENCE_REPORT.yaml` | 43-row equivalence table | Not a second semantic body |

Human Decisions, Cleanup Register, Path Mapping, and Template are already in this pack:

| Already materialized | Path |
|---|---|
| Human Decisions | `01_decisions/RP1_HUMAN_DECISIONS.yaml` |
| Cleanup Register | `01_decisions/RP1_CLEANUP_REGISTER.yaml` |
| Path Mapping | `02_mapping/RP1_SHADOW_PATH_MAPPING.yaml` |
| Shadow Template | `02_mapping/RP1_SHADOW_ARTIFACT_TEMPLATE.yaml` |

Future additive tests (Implementation only, not this round):

| Path | Role |
|---|---|
| `banyan-framework/tests/test_rp1_shadow_materialization.py` | Shadow file validation |
| `banyan-framework/tests/run_rp1_tests.py` | Runs existing R0/R1 suites plus the new tests; does not modify `run_r0_tests.py` / `run_r1_tests.py` |

---

## 3. Final 43 Artifact paths

Physical filenames follow HD-RP1-002 kebab-case. Internal `id` / `artifact_id` / provenance / references keep R1 original values, including `v3_1` literals.

Canonical copy: `02_mapping/RP1_SHADOW_PATH_MAPPING.yaml`.

| # | artifact_id (internal, unchanged) | Final path |
|---|---|---|
| 1 | `banyan.migration.role.source_role_model.v1` | `banyan-framework/artifacts/roles/source-role-model.v1.yaml` |
| 2 | `banyan.migration.policy.legacy_governance.v1` | `banyan-framework/artifacts/policies/legacy-governance.v1.yaml` |
| 3 | `banyan.migration.policy.adaptive_decision.v1` | `banyan-framework/artifacts/policies/adaptive-decision.v1.yaml` |
| 4 | `banyan.migration.policy.semantic_commit.v1` | `banyan-framework/artifacts/policies/semantic-commit.v1.yaml` |
| 5 | `banyan.migration.policy.permission_governance.v1` | `banyan-framework/artifacts/policies/permission-governance.v1.yaml` |
| 6 | `banyan.migration.skill.anydesign.v1` | `banyan-framework/artifacts/skills/anydesign.v1.yaml` |
| 7 | `banyan.migration.skill.visual_repair_loop.v1` | `banyan-framework/artifacts/skills/visual-repair-loop.v1.yaml` |
| 8 | `banyan.migration.workflow.v3_1_governance.v1` | `banyan-framework/artifacts/workflows/v3-1-governance.v1.yaml` |
| 9 | `banyan.migration.workflow.adaptive.v1` | `banyan-framework/artifacts/workflows/adaptive.v1.yaml` |
| 10 | `banyan.migration.workflow.decision.v1` | `banyan-framework/artifacts/workflows/decision.v1.yaml` |
| 11 | `banyan.migration.workflow.semantic_commit.v1` | `banyan-framework/artifacts/workflows/semantic-commit.v1.yaml` |
| 12 | `banyan.migration.workflow.change_lifecycle.v1` | `banyan-framework/artifacts/workflows/change-lifecycle.v1.yaml` |
| 13 | `banyan.migration.workflow.parallel_draft.v1` | `banyan-framework/artifacts/workflows/parallel-draft.v1.yaml` |
| 14 | `banyan.migration.workflow.batch_reconciliation.v1` | `banyan-framework/artifacts/workflows/batch-reconciliation.v1.yaml` |
| 15 | `banyan.migration.workflow.context_recovery.v1` | `banyan-framework/artifacts/workflows/context-recovery.v1.yaml` |
| 16 | `banyan.migration.workflow.knowledge_publication.v1` | `banyan-framework/artifacts/workflows/knowledge-publication.v1.yaml` |
| 17 | `banyan.migration.workflow.evidence_learning.v1` | `banyan-framework/artifacts/workflows/evidence-learning.v1.yaml` |
| 18 | `banyan.migration.state.artifact.v1` | `banyan-framework/artifacts/states/artifact.v1.yaml` |
| 19 | `banyan.migration.state.workflow.v1` | `banyan-framework/artifacts/states/workflow.v1.yaml` |
| 20 | `banyan.migration.state.change.v1` | `banyan-framework/artifacts/states/change.v1.yaml` |
| 21 | `banyan.migration.state.decision.v1` | `banyan-framework/artifacts/states/decision.v1.yaml` |
| 22 | `banyan.migration.state.runtime.v1` | `banyan-framework/artifacts/states/runtime.v1.yaml` |
| 23 | `banyan.migration.state.project_pilot.v1` | `banyan-framework/artifacts/states/project-pilot.v1.yaml` |
| 24 | `banyan.migration.state.governance_release.v1` | `banyan-framework/artifacts/states/governance-release.v1.yaml` |
| 25 | `banyan.migration.state.compatibility_migration.v1` | `banyan-framework/artifacts/states/compatibility-migration.v1.yaml` |
| 26 | `banyan.migration.state.capability_lifecycle.v1` | `banyan-framework/artifacts/states/capability-lifecycle.v1.yaml` |
| 27 | `banyan.migration.state.capability_activation.v1` | `banyan-framework/artifacts/states/capability-activation.v1.yaml` |
| 28 | `banyan.migration.state.project_stage.v1` | `banyan-framework/artifacts/states/project-stage.v1.yaml` |
| 29 | `banyan.migration.state.delivery_batch.v1` | `banyan-framework/artifacts/states/delivery-batch.v1.yaml` |
| 30 | `banyan.migration.template.artifact_instance.v1` | `banyan-framework/artifacts/templates/artifact-instance.v1.yaml` |
| 31 | `banyan.migration.template.informed_decision.v1` | `banyan-framework/artifacts/templates/informed-decision.v1.yaml` |
| 32 | `banyan.migration.template.change_workspace.v1` | `banyan-framework/artifacts/templates/change-workspace.v1.yaml` |
| 33 | `banyan.migration.template.design_package.v1` | `banyan-framework/artifacts/templates/design-package.v1.yaml` |
| 34 | `banyan.migration.template.project_guide.v1` | `banyan-framework/artifacts/templates/project-guide.v1.yaml` |
| 35 | `banyan.migration.template.handover_recovery.v1` | `banyan-framework/artifacts/templates/handover-recovery.v1.yaml` |
| 36 | `banyan.migration.template.evidence_record.v1` | `banyan-framework/artifacts/templates/evidence-record.v1.yaml` |
| 37 | `banyan.migration.decision.informed_protocol.v1` | `banyan-framework/artifacts/decision-protocols/informed-protocol.v1.yaml` |
| 38 | `banyan.migration.decision.level_routing.v1` | `banyan-framework/artifacts/decision-protocols/level-routing.v1.yaml` |
| 39 | `banyan.migration.context.new_window_resume.v1` | `banyan-framework/artifacts/context-recovery/new-window-resume.v1.yaml` |
| 40 | `banyan.migration.context.layered_selection.v1` | `banyan-framework/artifacts/context-recovery/layered-selection.v1.yaml` |
| 41 | `banyan.migration.context.freshness_evidence.v1` | `banyan-framework/artifacts/context-recovery/freshness-evidence.v1.yaml` |
| 42 | `banyan.migration.compatibility.v3_1.v1` | `banyan-framework/artifacts/compatibility/v3-1.v1.yaml` |
| 43 | `banyan.migration.compatibility.boundaries.v1` | `banyan-framework/artifacts/compatibility/boundaries.v1.yaml` |

**43 / 43.** No extra subdirectories under the nine category roots.

---

## 4. Shadow Artifact YAML Template

The approved template is stored at:

```text
02_mapping/RP1_SHADOW_ARTIFACT_TEMPLATE.yaml
```

That file is `document_role: CONSTRUCTION_TEMPLATE`. It has no runtime, semantic, registry, loader, or packaging authority.

Structure of each future shadow file:

1. CURRENT v1.9.1 section-8 self-describing metadata, full field set  
2. Complete R1 entry projection in `r1_record`  
3. Existing `contract` block only inside `r1_record`, and only if the R1 item already has it  

Fill rules remain HD-RP1-003=A. Thin-plus-contract remains HD-RP1-007=T. Do not copy whole `workflows.yaml` / `states.yaml` / `source_roles.yaml` / `compatibility/v3_1.yaml` bodies.

YAML anchors from `migration_artifacts.yaml` must be expanded to resolved lists in shadow files.

---

## 5. Shadow Validation plan

Validation is read-only against the current Registry / Loader. Do not register `artifacts/**` in the Manifest. Do not change `validate_framework_contracts()` authority root.

Implementation location (future, not this round): `banyan-framework/tests/test_rp1_shadow_materialization.py`.

| ID | Check | Pass condition |
|---|---|---|
| V-01 | Paths exist | All 43 paths in section 3 exist as files |
| V-02 | No extra files | YAML under `artifacts/**` is exactly 43; no subdirectories; no unmapped names |
| V-03 | YAML parses | Each file `yaml.safe_load` is a mapping |
| V-04 | Shadow marker | `authority_class == NON_AUTHORITATIVE_SHADOW_MATERIALIZATION`; `source_of_truth == banyan.registry.migration_artifacts.v1`; `generated_or_manual == GENERATED` |
| V-05 | ID fidelity | `id == r1_record.artifact_id ==` matching Registry `artifact_id`; kebab filenames do not rewrite internal IDs |
| V-06 | Type/directory | ROLE→roles, POLICY→policies, SKILL→skills, WORKFLOW→workflows, STATE→states, TEMPLATE→templates, DECISION_PROTOCOL→decision-protocols, CONTEXT_RECOVERY→context-recovery, COMPATIBILITY→compatibility |
| V-07 | Filename rule | `{kebab-local}.v1.yaml`; `v3_1` becomes `v3-1` in filenames only |
| V-08 | Section-8 fields complete | Metadata fields from the template all present; schema not shrunk |
| V-09 | Fill legality | Non-DERIVABLE vacancies are only `UNKNOWN` or `NOT_APPLICABLE`; empty string is not “configured” |
| V-10 | SKILL special case | Only `anydesign` / `visual-repair-loop`: `inputs`/`outputs`/`when_to_use` DERIVABLE from contract/triggers; other 41 have `inputs`/`outputs` = `NOT_APPLICABLE` |
| V-11 | ROLE special case | Only ROLE: `forbidden` DERIVABLE; `r1_record.contract.role_kind == SOURCE_ROLE_ONLY` |
| V-12 | STATE unmerged | 12 `r1_record.contract.state_domain` values distinct; `global_enum_merge_forbidden is true` |
| V-13 | Semantic equivalence | `r1_record` keys/values, after expanding anchors, equal the matching `migration_artifacts.yaml` item |
| V-14 | Thin-plus-contract | If R1 has `contract`, shadow `r1_record.contract` equals it; otherwise the key is absent |
| V-15 | No registry body copy | Forbidden collection keys listed in the template are absent |
| V-16 | UNKNOWN is not authorization | `field_fill_policy.unknown_is_not_authorization/allow/configured == true`; `permissions`/`rollback` are not ALLOW/true/configured |
| V-17 | No new semantics | No workflow/skill/role/state-domain IDs beyond R1 |
| V-18 | Refs still point at Registry | `target_registry` / `references` unchanged; not rewritten to `artifacts/**` |
| V-19 | Authority not switched | `manifest.yaml` still 11 assets; Loader still reads `contracts/data`; `pyproject.toml` package-data still excludes `artifacts/**` |
| V-20 | R0/R1 regression | `run_r0_tests.py` 16/16; `run_r1_tests.py` 22/22 |
| V-21 | `.banyan` unchanged | Content/hash unchanged |
| V-22 | Zero deletes | No deleted files in the Implementation round |

Any V-* FAIL blocks Acceptance PASS. Rollback removes only Implementation-created files.

Not in RP1: clean-room discovery from `artifacts/**`; `banyan artifact list/show`; wheel inclusion. Those belong to RP2.

---

## 6. Implementation-round allowlist

Future Implementation may **create** only:

```text
banyan-framework/artifacts/roles/**
banyan-framework/artifacts/policies/**
banyan-framework/artifacts/skills/**
banyan-framework/artifacts/workflows/**
banyan-framework/artifacts/states/**
banyan-framework/artifacts/templates/**
banyan-framework/artifacts/decision-protocols/**
banyan-framework/artifacts/context-recovery/**
banyan-framework/artifacts/compatibility/**

banyan-framework/tests/test_rp1_shadow_materialization.py
banyan-framework/tests/run_rp1_tests.py

榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/RP1_SHADOW_MATERIALIZATION_ACCEPTANCE_REPORT.md
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/RP1_PLAN_CONFORMANCE_CHECK.yaml
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/RP1_GAP_DELTA.yaml
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/RP1_CHANGED_FILES.yaml
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/RP1_CLEANUP_DELTA.yaml
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/RP1_REGRESSION_RESULT.yaml
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/RP1_NEW_PROPOSAL_REGISTER.yaml
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/RP1_ROLLBACK_PLAN.md
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/RP1_HANDOVER_CHECKPOINT.md
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/RP1_SEMANTIC_EQUIVALENCE_REPORT.yaml
```

Allowed directory creation: only `banyan-framework/artifacts/` and its nine frozen category roots, produced by writing YAML.

This preparation round's allowlist was only the six files in `00_preparation/`, `01_decisions/`, and `02_mapping/`.

---

## 7. Blacklist

Blacklist outranks convenience. Touching these stops work and requires a Human Decision.

```text
banyan-framework/pyproject.toml
banyan-framework/src/banyan/contracts/loader.py
banyan-framework/src/banyan/contracts/validator.py
banyan-framework/src/banyan/contracts/__init__.py
banyan-framework/src/banyan/contracts/data/**
banyan-framework/src/banyan/cli.py
any new MANIFEST.in / setup.py / setup.cfg used to include artifacts

banyan-framework/src/banyan/policy/**
banyan-framework/policies/**

.banyan/**

榕树ai改造落地相关文档/00_总纲与审计/CURRENT/**
docs/governance/common_prd_v3.1/**
docs/project/**

banyan-framework/control-plane-go/bin/banyan-control
**/.DS_Store
banyan-framework/src/banyan/web/**
banyan-framework/src/banyan/control_plane/**
banyan-framework/frontend/**
banyan-framework/control-plane-go/**

tools/anydesign/**
.cursor/skills/**

banyan-framework/tests/test_framework_contracts.py
banyan-framework/tests/test_r1_artifact_migration.py
banyan-framework/tests/run_r0_tests.py
banyan-framework/tests/run_r1_tests.py
banyan-framework/docs/maintainer/**
banyan-framework/docs/DOCUMENTATION_SOURCE_OF_TRUTH.yaml
banyan-framework/docs/DOCUMENTATION_INVENTORY.md
banyan-framework/docs/user-guide/**
banyan-framework/README.md

.banyan-refactor/**
榕树ai改造落地相关文档/00_总纲与审计/**
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP0_Rebaseline_v2.0/**
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_R0_Framework_Self_Containment_Remediation_Pack_v1.0/**
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_R1_Artifact_Migration_Completion_Pack_v1.0/**

banyan-framework/src/banyan/runtime/**
banyan-framework/src/banyan/commit/**
banyan-framework/src/banyan/git/**
banyan-framework/src/banyan/editor/**
```

Forbidden actions:

- delete any file
- Authority / Registry / Loader / CLI / Wheel cutover
- mark `artifacts/**` Canonical
- copy whole Registry bodies into shadow files
- rewrite internal `artifact_id` to match kebab filenames
- re-init `.banyan`
- mix `.DS_Store` or Go-binary cleanup into Artifact Materialization
- create new RP1 files under `banyan-framework/docs/maintainer/`
- enter RP2 during RP1

---

## 8. Acceptance inventory after Implementation

After Implementation, these must exist and be inspectable:

**A.** All 43 shadow files in section 3.

**B.** The ten `03_acceptance/` files in section 2.

**C.** The two additive test files.

**D.** Results recorded in `RP1_REGRESSION_RESULT.yaml`:

- `PYTHONPATH=src python3 tests/run_r0_tests.py` → PASS
- `PYTHONPATH=src python3 tests/run_r1_tests.py` → PASS
- `PYTHONPATH=src python3 tests/run_rp1_tests.py` → PASS (V-01…V-22)
- `banyan contracts validate` still validates the 11 contract assets
- `pyproject.toml` package-data still only includes `banyan.contracts.data` YAML

**E.** Cleanup / unchanged lists:

- `deleted: []`
- `.banyan/**` unchanged
- `migration_artifacts.yaml` unchanged
- `loader.py` / `cli.py` / `pyproject.toml` unchanged
- no new files under `banyan-framework/docs/maintainer/`

**F.** Carried gaps, not pass conditions:

- D0 `artifact_root_state` may remain stale until RP10
- Go tests may remain `NOT_RERUN_ENVIRONMENT_BLOCKED`
- `default_policy()` vs YAML dual representation remains (HD-CLEANUP-003)
- `bin/banyan-control` remains (HD-CLEANUP-001)

Exit gates:

```text
EXPECTED = 43
SHADOW_MATERIALIZED = 43
SEMANTIC_EQUIVALENCE_FAILURE = 0
UNAUTHORIZED_NEW_SEMANTIC = 0
DANGLING_REFERENCE_INTRODUCED = 0
R0_R1_AUTHORITY_CHANGED = 0
DOT_BANYAN_CHANGED = 0
DELETE_COUNT = 0
LOADER_READS_ARTIFACTS = false
WHEEL_INCLUDES_ARTIFACTS = false
PLAN_CONFORMANCE_CHECK = PASS
```

---

This preparation file does not start RP1 Implementation.

# RP1 Pre-Construction Review

> **Pack**：`Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0`  
> **Document role**：CONSTRUCTION_EVIDENCE  
> **Runtime / Registry / Semantic authority**：false  
> **Review status**：COMPLETED_THEN_HUMAN_DECISIONS_APPROVED  
> **Baseline**：`BANYAN-UNIQUE-REMEDIATION-BASELINE-2026-09-21-V2`  
> **Principle**：`TOKEN_EFFICIENCY_MUST_NOT_REDUCE_GOVERNANCE_FIDELITY`

This file is the formal record of the RP1 PRE-CONSTRUCTION REVIEW already completed in chat.

It is **not** a new repository scan. Facts, paths, counts, and classifications are copied from that review. Chat wording is construction evidence, not Runtime Authority.

Human Decisions recorded in `01_decisions/RP1_HUMAN_DECISIONS.yaml` approve the mapping, naming, metadata, Thin-plus-contract, packaging freeze, and zero-delete gate. They do not change the facts below.

---

# A. Repository Reality Check

Verification used the workspace tree at review time, not old Acceptance Reports as a substitute for current files.

| # | Item | Fact at review | Evidence path |
|---|---|---|---|
| 1 | Framework tree | `src/`, `policies/`, `tests/`, `docs/`, `frontend/`, `control-plane-go/` exist; **no** `artifacts/` | `banyan-framework/` |
| 2 | `src/banyan/contracts/data/**` | 11 declared assets; current Framework Contract Authority | see section B |
| 3 | `migration_artifacts.yaml` | R1 authoritative registry; 43 entries; `status: FROZEN` | `banyan-framework/src/banyan/contracts/data/migration_artifacts.yaml` |
| 4 | `manifest.yaml` | 11 assets; includes `migration_artifacts.yaml`; `role: AUTHORITATIVE` | `.../manifest.yaml` |
| 5 | `schema_index.yaml` | Includes `banyan.schema.migration_artifacts.v1` | `.../schema_index.yaml` |
| 6 | Artifact Registry | Current R1 registry is `banyan.registry.migration_artifacts.v1`. Separate `banyan.registry.artifacts.v1` holds 11 document types, not the R1 43 | `migration_artifacts.yaml` + `artifacts.yaml` |
| 7 | Artifact Loader | `load_framework_contracts()` reads only Manifest YAML; does **not** read `artifacts/**` | `banyan-framework/src/banyan/contracts/loader.py` |
| 8 | `pyproject.toml` | Package `banyan-framework` `0.1.0`; package-data is `banyan.contracts.data: *.yaml, compatibility/*.yaml` | `banyan-framework/pyproject.toml` |
| 9 | Wheel inclusion | Does **not** include future `artifacts/**`; no `MANIFEST.in` / `setup.py` | `pyproject.toml` |
| 10 | CLI | Has `contracts list/validate`; no `artifact list/show/validate/refs`; no `init/adopt/migrate/reconcile` | `banyan-framework/src/banyan/cli.py` |
| 11 | Tests | R0/R1 runners existed and passed when re-run in the review | `tests/run_r0_tests.py`, `tests/run_r1_tests.py` |
| 12 | `artifacts/**` | MISSING | directory scan `ARTIFACTS_MISSING` |
| 13 | Half-built independent Artifact files | None found | no `artifacts/` matches |
| 14 | Historical leftovers | Dual Control Plane / dual WebUI / compiled Go binary / `.DS_Store`; no half-built `artifacts/` | section E |
| 15 | Superseded by v2.0 Rebaseline | No independent Artifact semantic source in code. Superseded is the old R2/R3 route and the R1 Handover “stop before R2” sentence | `docs/maintainer/R1_HANDOVER_CHECKPOINT.md` |
| 16 | Duplicate authority | Present as a **legal current transition**: R1 body in `migration_artifacts.yaml`; Workflow/State/SourceRole/Compatibility have registry bodies; Runtime Policy has YAML + Python builtin. RP1 must not create a third Canonical | section I |
| 17 | Documented as implemented but missing | No Framework doc claimed `artifacts/**` already exists. `init/adopt/migrate`, `/help`, Canonical Apply, natural-language orchestration are recorded as not implemented | `docs/DOCUMENTATION_SOURCE_OF_TRUTH.yaml` |
| 18 | Implemented but not in R1 43 | `banyan.flow.runtime_request.v1`, 21 state_sets, 35 CAP-*, 11 document Artifact Types, 9 Source Role entries, Runtime/Control Plane. These are **not** missing R1 Artifacts and must not be added to 43 | `workflows.yaml`, `states.yaml`, `capabilities.yaml`, `artifacts.yaml`, `source_roles.yaml` |

`.banyan/` existed with 13 files, `PILOT_SHADOW`, `final_activation: false`. Review was read-only.

Review-time Python re-run:

- `R0 runner 16/16 PASS`
- `R1 runner 22/22 PASS`
- `validate_framework_contracts` `valid=true` (11 assets / 35 capabilities / 35 ports / 263 refs / **43 artifacts**)

Go Control Plane tests: `NOT_RERUN_THIS_ROUND`. `go.mod` requires Go 1.24. This does not overturn historical Acceptance PASS.

---

# B. Current Architecture Snapshot

## B.1 `banyan-framework/` first level at review

```text
banyan-framework/
├── README.md
├── pyproject.toml
├── policies/default-policy.yaml
├── src/banyan/
├── tests/
├── docs/
├── frontend/
└── control-plane-go/
```

`banyan-framework/artifacts/` did not exist.

## B.2 Contract Authority Root

`banyan-framework/src/banyan/contracts/data/` files:

| File | asset_id | Manifest role |
|---|---|---|
| `schema_index.yaml` | `banyan.registry.schema_index.v1` | AUTHORITATIVE |
| `capabilities.yaml` | `banyan.registry.capabilities.v1` | AUTHORITATIVE |
| `artifacts.yaml` | `banyan.registry.artifacts.v1` | AUTHORITATIVE (document types, not R1 43) |
| `source_roles.yaml` | `banyan.registry.source_roles.v1` | AUTHORITATIVE |
| `workflows.yaml` | `banyan.registry.workflows.v1` | AUTHORITATIVE_AND_CODE_PROJECTION |
| `states.yaml` | `banyan.registry.states.v1` | AUTHORITATIVE_AND_CODE_PROJECTION |
| `provider_ports.yaml` | `banyan.registry.provider_ports.v1` | AUTHORITATIVE |
| `project_overlay.yaml` | `banyan.contract.project_overlay.v1` | AUTHORITATIVE |
| `compatibility/v3_1.yaml` | `banyan.compatibility.v3_1.v1` | AUTHORITATIVE |
| `versioning.yaml` | `banyan.registry.versioning.v1` | AUTHORITATIVE_AND_CODE_PROJECTION |
| `migration_artifacts.yaml` | `banyan.registry.migration_artifacts.v1` | AUTHORITATIVE (R1 43 until RP2 Cutover) |

Loader default uses `importlib.resources`. Validator checks shape/refs/35 CAP/35 Port/R1 categories and provenance. It does not execute Workflows.

## B.3 Runtime / CLI / Package

- Runtime execution authority: `src/banyan/runtime/` + `policies/default-policy.yaml` + `src/banyan/policy/compiler.py::default_policy()`
- CLI domains: `policy` / `runtime` / `git` / `commit` / `trace` / `provider` / `contracts`
- Package version: `0.1.0`
- Framework release dimension: `v1.10-additive.1`; Governance pointer: `v1.9.1`

## B.4 `.banyan/` (read-only at review)

13 files, matching the D0 list.

- `pilot.yaml`: `mode: PILOT_SHADOW`, `final_activation: false`
- `instance/project-instance.yaml`: `state: PILOT_SHADOW`, `canonical_replacement: false`
- `runtime/status.yaml`: `current_project_git_execution: DRY_RUN_ONLY`
- `migrations/rollback.yaml` contains `verify_dot_banyan_absent` as Stage 17 pilot rollback simulation, not a current upgrade strategy

---

# C. R0 Preservation Check

| Item | Conclusion |
|---|---|
| Historical result | `PASS_R0_FRAMEWORK_SELF_CONTAINMENT` preserved |
| Review-time re-run | `tests/run_r0_tests.py` → 16/16 PASS |
| Self-containment | Loader/Validator still do not depend on `.banyan-refactor/`, `.banyan/`, or construction packs |
| Contract discovery | Still `src/banyan/contracts/data` + `banyan contracts list/validate` |
| Count drift vs historical R0 report | Historical R0 report said 11/11 tests, 13 v3.1 mappings, and in one wheel paragraph 10 declared assets. Current tree at review: 16 tests (R1 assertions added to `test_framework_contracts.py`), 22 mappings, 11 assets. This is R1 superposition, not R0 failure |
| RP1 constraint | R0 authority must not switch to `artifacts/**` during RP1 |

R0 still holds: Framework contracts are self-contained for discovery/validation; independent Artifact physical form is not yet built.

---

# D. R1 Preservation Check

| Item | Conclusion |
|---|---|
| Historical result | `PASS_R1_ARTIFACT_MIGRATION_COMPLETION` preserved |
| Review-time re-run | `tests/run_r1_tests.py` → 22/22 PASS |
| Counts | ROLE 1 / POLICY 4 / SKILL 2 / WORKFLOW 10 / STATE 12 / TEMPLATE 7 / DECISION_PROTOCOL 2 / CONTEXT_RECOVERY 3 / COMPATIBILITY 2 = **43/43** |
| Origin | LEGACY_MIGRATION 9 / REFRACTOR_ADDITION 20 / GENERALIZED 14; `NEW_PROPOSAL = 0` |
| Matrix | `R1_ARTIFACT_MIGRATION_MATRIX.yaml` is a complete projection, `projection_of: banyan.registry.migration_artifacts.v1` |
| Semantic boundaries | Capability ≠ Skill; Role = SOURCE_ROLE_ONLY; 12 State Domains remain unmerged |
| Not done by R1 | No Workflow executor / Canonical Apply / Collaboration Role Runtime / Help Center |
| Superseded sequencing text | `R1_HANDOVER_CHECKPOINT.md` still says “must stop before R2/R3/D2/D3”. R1 result is preserved; future route is the v2.0 RP route |

R1 was not redesigned. No new Artifact semantics were invented. No missing IDs were fabricated.

---

# E. Historical Wrong-Construction / Cleanup Inventory

The review deleted nothing. `safe_to_delete` / `safe_to_delete_now` are false for every current candidate.

Authoritative machine copy: `01_decisions/RP1_CLEANUP_REGISTER.yaml`.

Summary of the four classes:

### KEEP

Current legal retainers, including:

- `migration_artifacts.yaml` and the other 10 contract assets
- Loader, Validator, CLI, `pyproject.toml`
- `policies/default-policy.yaml`, runtime, commit, policy compiler
- `frontend/`, Go control-plane **source**
- `.banyan/**`
- existing R0/R1 maintainer reports and the R1 matrix
- `docs/governance/common_prd_v3.1/**`
- `tools/anydesign/SKILL.md` and `.cursor/skills/visual-repair-loop/SKILL.md`
- existing R0/R1 tests

### MIGRATE

Valid now, later move or reframe, not delete now:

- semantic-body role of `migration_artifacts.yaml` (RP2)
- overlapping bodies in `workflows.yaml` / `states.yaml` (RP2)
- unaccepted `docs/user-guide/**` (RP10)
- old R2/R3 sentence inside R1 handover (keep file; follow v2.0 route)
- README Python CP as primary start (RP10)
- legacy Python Control Plane + `src/banyan/web`
- `.banyan-refactor/**` as historical evidence

### CLEANUP_CANDIDATE

- `banyan-framework/.DS_Store`
- `banyan-framework/docs/.DS_Store`
- `banyan-framework/src/banyan/contracts/.DS_Store`

HD-CLEANUP-002 later hygiene is approved, **not** in RP1, and must not mix with Artifact Materialization.

### UNKNOWN

- `banyan-framework/control-plane-go/bin/banyan-control` (HD-CLEANUP-001 NEED_MORE_EVIDENCE)
- `default_policy()` vs `policies/default-policy.yaml` (HD-CLEANUP-003 accept current state for RP1)
- `.banyan/mappings/source-mappings.yaml` unofficial role names
- superseded v1.0 baseline filenames not found in the review search
- `.banyan/migrations/rollback.yaml` `verify_dot_banyan_absent`

**Review conclusion:** no file met the seven-part “deletable now” gate. `DELETE_COUNT` for RP1 is 0.

---

# F. R1 43 Artifact Inventory

Source at review: loaded `banyan.registry.migration_artifacts.v1`, matching the v2.0 baseline list and Matrix `summary.by_type`.

| # | artifact_id | type | current_source | current_storage | current_semantic_authority | current_runtime_relationship |
|---|---|---|---|---|---|---|
| 1 | `banyan.migration.role.source_role_model.v1` | ROLE | `source_roles.yaml` + Stage 03 | registry YAML only | FRAMEWORK_CONTRACT → `banyan.registry.source_roles.v1` | `runtime_consumer: null` |
| 2 | `banyan.migration.policy.legacy_governance.v1` | POLICY | v3.1.15 + Stage 07 | registry YAML only | FRAMEWORK_CONTRACT | null; missing `AUTOMATED_GOVERNANCE_EXECUTOR` |
| 3 | `banyan.migration.policy.adaptive_decision.v1` | POLICY | Stage 05 | registry YAML only | FRAMEWORK_CONTRACT | null; missing router |
| 4 | `banyan.migration.policy.semantic_commit.v1` | POLICY | Stage 05/14/15 + default policy + runtime | registry + runtime | FRAMEWORK_CONTRACT | `banyan.commit` + `RuntimeAPI` |
| 5 | `banyan.migration.policy.permission_governance.v1` | POLICY | Stage 14/15 + default policy | registry + runtime | FRAMEWORK_CONTRACT | `PolicyCompiler` + `PermissionEvaluator` |
| 6 | `banyan.migration.skill.anydesign.v1` | SKILL | `tools/anydesign/SKILL.md` | in-place skill, not Framework Core | FRAMEWORK_CONTRACT registration | unbound; missing adapter |
| 7 | `banyan.migration.skill.visual_repair_loop.v1` | SKILL | `.cursor/skills/visual-repair-loop/SKILL.md` | in-place compatibility skill | FRAMEWORK_CONTRACT registration | no Framework native skill runtime |
| 8 | `banyan.migration.workflow.v3_1_governance.v1` | WORKFLOW | v3.1.15 + `workflows.yaml` | registry + workflows.yaml | FRAMEWORK_CONTRACT → workflows registry | NOT_IMPLEMENTED |
| 9 | `banyan.migration.workflow.adaptive.v1` | WORKFLOW | Stage 05 + `banyan.workflow.adaptive.v1` | same | same | NOT_IMPLEMENTED |
| 10 | `banyan.migration.workflow.decision.v1` | WORKFLOW | v3.1 + Stage 05 + `decision_flow` | same | same | NOT_IMPLEMENTED |
| 11 | `banyan.migration.workflow.semantic_commit.v1` | WORKFLOW | Stage 05/15 + workflow id | registry + commit runtime | same | `banyan.commit` + RuntimeAPI |
| 12 | `banyan.migration.workflow.change_lifecycle.v1` | WORKFLOW | v3.1 + Stage 06 | same | same | missing Change workspace / Canonical Apply |
| 13 | `banyan.migration.workflow.parallel_draft.v1` | WORKFLOW | v3.1 + Stage 06 + `parallel_draft_promotion` | same | same | missing parallel draft runtime |
| 14 | `banyan.migration.workflow.batch_reconciliation.v1` | WORKFLOW | v3.1 + Stage 03/06 | same | same | missing batch executor |
| 15 | `banyan.migration.workflow.context_recovery.v1` | WORKFLOW | v3.1 usage + Stage 11/12 | same | same | missing recovery runtime |
| 16 | `banyan.migration.workflow.knowledge_publication.v1` | WORKFLOW | v3.1 + Stage 10 | same | same | missing publisher |
| 17 | `banyan.migration.workflow.evidence_learning.v1` | WORKFLOW | Stage 13 | same | same | missing evidence/learning runtime |
| 18 | `banyan.migration.state.artifact.v1` | STATE | `banyan.state.artifact_status.v1` | registry + states.yaml | FRAMEWORK_CONTRACT → states | contract only |
| 19 | `banyan.migration.state.workflow.v1` | STATE | `banyan.state.adaptive_workflow.v1` | same | same | contract only |
| 20 | `banyan.migration.state.change.v1` | STATE | `banyan.state.change_lifecycle.v1` | same | same | contract only |
| 21 | `banyan.migration.state.decision.v1` | STATE | informed_decision + decision_level | same | same | contract only |
| 22 | `banyan.migration.state.runtime.v1` | STATE | `runtime_status` + runtime models | registry + code projection | same | IMPLEMENTED_CODE_PROJECTION |
| 23 | `banyan.migration.state.project_pilot.v1` | STATE | `project_instance_pilot` | same | same | contract only |
| 24 | `banyan.migration.state.governance_release.v1` | STATE | `framework_release` | same | same | contract only |
| 25 | `banyan.migration.state.compatibility_migration.v1` | STATE | `contract_status` | same | same | contract only |
| 26 | `banyan.migration.state.capability_lifecycle.v1` | STATE | capability_lifecycle | same | same | contract only |
| 27 | `banyan.migration.state.capability_activation.v1` | STATE | capability_activation | same | same | contract only |
| 28 | `banyan.migration.state.project_stage.v1` | STATE | project_stage | same | PROJECT_OVERLAY_CONTRACT index | contract only |
| 29 | `banyan.migration.state.delivery_batch.v1` | STATE | delivery_batch | same | LEGACY_COMPATIBILITY_CONTRACT index | contract only |
| 30 | `banyan.migration.template.artifact_instance.v1` | TEMPLATE | Stage 03 `required_fields` | no independent template file | FRAMEWORK_CONTRACT → migration registry | no generator |
| 31 | `banyan.migration.template.informed_decision.v1` | TEMPLATE | v3.1 | no independent file | same | missing TEMPLATE_GENERATOR |
| 32 | `banyan.migration.template.change_workspace.v1` | TEMPLATE | v3.1 + Stage 06 | no independent file | same | missing generator |
| 33 | `banyan.migration.template.design_package.v1` | TEMPLATE | AnyDesign + Stage 09 | no independent file | same | missing generator |
| 34 | `banyan.migration.template.project_guide.v1` | TEMPLATE | v3.1 + Stage 10 | no independent file | same | missing generator |
| 35 | `banyan.migration.template.handover_recovery.v1` | TEMPLATE | v3.1 + Stage 10/12 | no independent file | same | missing generator |
| 36 | `banyan.migration.template.evidence_record.v1` | TEMPLATE | Stage 13 | no independent file | same | missing generator |
| 37 | `banyan.migration.decision.informed_protocol.v1` | DECISION_PROTOCOL | v3.1 phases | registry `contract.phases` | FRAMEWORK_CONTRACT | missing DECISION_SESSION_EXECUTOR |
| 38 | `banyan.migration.decision.level_routing.v1` | DECISION_PROTOCOL | Stage 05/14 L0–L4 | registry `contract.levels` | same | missing ADAPTIVE_ROUTER |
| 39 | `banyan.migration.context.new_window_resume.v1` | CONTEXT_RECOVERY | v3.1 usage | registry only | same | missing CONTEXT_RECOVERY_RUNTIME |
| 40 | `banyan.migration.context.layered_selection.v1` | CONTEXT_RECOVERY | Stage 11/12 | registry + mandatory_context | same | missing selector/budget/compactor |
| 41 | `banyan.migration.context.freshness_evidence.v1` | CONTEXT_RECOVERY | Stage 11/12 | registry only | same | missing freshness resolver / query |
| 42 | `banyan.migration.compatibility.v3_1.v1` | COMPATIBILITY | `compatibility/v3_1.yaml` (22 mappings) | registry + compatibility YAML | FRAMEWORK_CONTRACT → `banyan.compatibility.v3_1.v1` | contract only |
| 43 | `banyan.migration.compatibility.boundaries.v1` | COMPATIBILITY | Stage 04/07/09/20 + editor adapters | registry + adapters transport | FRAMEWORK_CONTRACT | PARTIALLY_IMPLEMENTED |

**Missing IDs: none.**

Not counted in 43, correctly:

- 35 `CAP-*` (Capability ≠ Skill)
- 9 Source Role entries (the Role artifact is the model)
- 11 document Artifact Types
- `banyan.flow.runtime_request.v1`
- remaining state_sets referenced by Workflow/Policy, not extra State Domains

Every inventory row’s current registry entry is the matching item in `migration_artifacts.yaml`.

---

# G. Proposed Mapping

Now the approved mapping. Machine copy: `02_mapping/RP1_SHADOW_PATH_MAPPING.yaml`.

Common fields for all 43:

- `shadow_or_canonical` = SHADOW
- `registry_relationship` = indexed by `banyan.registry.migration_artifacts.v1`; RP1 file is projection only
- `runtime_relationship` = unchanged; loader/cli/runtime do not execute from `artifacts/**` in RP1
- `migration_method` = SHADOW_PROJECT_R1_RECORD_PLUS_EXISTING_CONTRACT_BLOCK
- `proposed_format` = YAML
- `proposed_filename` = `{kebab-local}.v1.yaml`

Physical paths are listed in `00_preparation/RP1_IMPLEMENTATION_PREPARATION.md` section 3 and the mapping YAML. Filename kebab (`v3-1`) does not rewrite internal `artifact_id` (`v3_1`).

The proposal did not merge State Domains, promote Capability to Skill, treat Source Role as Collaboration/Banyan Role, or mix Role / Permission / Git Identity / Authentication.

---

# H. Naming / Format Proposal

Frozen before this review: Artifact root, nine category names, 43 IDs, self-describing metadata contract, RP1 adds no new semantics.

Approved as HD-RP1-001=A and HD-RP1-002=A:

1. Format: single YAML (`.yaml`)
2. Naming: `banyan.migration.{type}.{local}.{version}` → `{kebab(local)}.{version}.yaml`; `_` → `-`; `v3_1` → `v3-1` in **filenames only**
3. No subdirectories under the nine category roots
4. Metadata + R1 record + existing contract in one file
5. Required shadow marker: `authority_class: NON_AUTHORITATIVE_SHADOW_MATERIALIZATION`
6. RP1 does not modify `pyproject.toml`; shadow files are source-tree only

Rejected for RP1: shrinking the metadata schema; fat-copy of whole registries; wheel inclusion; Loader cutover.

---

# I. RP1 Authority Model

```text
CURRENT SEMANTIC AUTHORITY
  = 43 entries in migration_artifacts.yaml
    + pointed-to registries / preserve-in-place skills / runtime code
  Unchanged during RP1

SHADOW MATERIALIZED ARTIFACT
  = future banyan-framework/artifacts/** files
  = NON_AUTHORITATIVE_SHADOW_MATERIALIZATION
  ≠ Canonical Source
  ≠ second truth

REGISTRY AUTHORITY
  = manifest.yaml + schema_index.yaml + 11 data assets
  RP1 does not change declarations or the Loader scan root

RUNTIME EXECUTION AUTHORITY
  = policy compiler/evaluator + runtime/commit/git + Go control plane
  RP1 does not change execution sources
```

Creating independent files is not Canonical Cutover, Registry Cutover, Runtime Cutover, or Packaging Cutover. Those wait for RP2. `.banyan` is not Framework Artifact truth and is unchanged in RP1.

This pack is construction evidence only. It is not consumed by Loader / Runtime / Registry, so it is not a second Artifact source.

---

# J. Metadata Compatibility Check

Against CURRENT v1.9.1 section 8 and the review’s extension fields. No invented facts.

| Field | vs R1 43 | Class | Note |
|---|---|---|---|
| id | DERIVABLE | from `artifact_id` |
| type | DERIVABLE | from `artifact_type` |
| version | DERIVABLE | ID suffix `.v1`; no independent semver |
| status | DERIVABLE | R1 `MIGRATED_AS_ARTIFACT`, not DRAFT/APPROVED lifecycle |
| scope | UNKNOWN | R1 has registry-level `scope_exclusions`, not per-artifact scope |
| purpose | DERIVABLE | present |
| when_to_use | UNKNOWN / SKILL DERIVABLE | only 2 SKILL `triggers`; other 41 UNKNOWN |
| when_not_to_use | UNKNOWN | absent |
| inputs | NOT_APPLICABLE / SKILL DERIVABLE | only SKILL `contract.inputs` |
| outputs | NOT_APPLICABLE / SKILL DERIVABLE | only SKILL `contract.outputs` |
| permissions | UNKNOWN | must not copy Permission policy into Role/Skill as authorization |
| forbidden | DERIVABLE / UNKNOWN | ROLE `forbidden_promotions`; others UNKNOWN |
| dependencies | DERIVABLE | approximate `references` + `target_registry` |
| source_of_truth | DERIVABLE | RP1 writes `banyan.registry.migration_artifacts.v1` |
| generated_or_manual | DERIVABLE | shadow files GENERATED |
| compatibility | DERIVABLE | `compatibility_status` |
| validation | DERIVABLE | R1 `validation` list |
| rollback | UNKNOWN | absent |
| maintenance_owner | UNKNOWN | not Git contributor |
| last_updated | UNKNOWN | must not use mtime as authority |
| origin | DERIVABLE | present |
| provenance | DERIVABLE | present |
| implementation_status | DERIVABLE | present |
| compatibility_status | DERIVABLE | present |
| missing_layers | DERIVABLE | present, may be `[]` |
| references | DERIVABLE | present |
| supersession | UNKNOWN | R1 entries have no supersedes/superseded_by |
| migration_lineage | UNKNOWN | template requires it for future instances; 43 entries do not fill it |
| token_context_policy | DERIVABLE | `token_context_policy_ref` |

HD-RP1-003=A: keep the full schema; fill DERIVABLE / NOT_APPLICABLE / UNKNOWN; do not invent; UNKNOWN is not authorization.

---

# K. Construction Plan

Nine phases for future Implementation. Not executed in the review or this pack materialization.

1. Preflight / Backup / Inventory Lock  
2. Artifact Schema / Template Preparation (use this pack’s template; do not register it in `schema_index.yaml` without a Human Decision)  
3. 43 Artifact Shadow Materialization  
4. Reference Validation  
5. Semantic Equivalence Validation  
6. Package / Wheel Compatibility Check (check only, no cutover)  
7. Regression  
8. PLAN_CONFORMANCE_CHECK  
9. Acceptance / Handoff into this pack `03_acceptance/`

Each phase’s inputs/actions/outputs/validation/rollback/forbidden/human_decision_trigger remain as written in the implementation-preparation file.

---

# L. Risks

1. Dual-truth window if humans/AIs treat `artifacts/**` as Canonical despite the shadow marker.  
2. Fat-copy of registry bodies would pre-cutover.  
3. Filling CURRENT section-8 by inventing `when_to_use` / owner / rollback.  
4. Moving Skill files into `artifacts/skills/` would break preserve-in-place.  
5. Deleting `.banyan` or running `verify_dot_banyan_absent`.  
6. Following R1 Handover into cancelled R2/R3.  
7. Editing `pyproject.toml` would be RP2.  
8. Confusing `states/workflow.v1.yaml` with `workflows/**`.  
9. Treating the Go binary or dual WebUI as RP1 cleanup.

---

# M. Conflicts

1. Legal current dual body: R1 registry vs `workflows.yaml` / `states.yaml` / `source_roles.yaml` / `compatibility/v3_1.yaml`. RP1 projects; it does not pick a winner.  
2. Runtime policy dual representation: `default_policy()` vs YAML.  
3. Dual Control Plane / dual WebUI, already recorded in D0.  
4. Historical R0 report counts vs review-time tree counts.  
5. R1 Handover “stop before R2/R3” vs v2.0 RP route. Future construction follows v2.0.  
6. User-guide 08 omits implemented `banyan contracts list/validate`.  
7. `.banyan` rollback contains directory removal vs current forbid-reinit.  
8. README still leads with Python Control Plane.

RP1 does not “fix” these by editing Framework code unless Human Authority later says so.

---

# N. Unknowns

Recorded at review, then decided or deferred:

1. Exact filenames/extensions → HD-RP1-001/002 approved.  
2. YAML vs YAML+MD vs JSON → YAML approved.  
3. Category subdirectories → forbidden.  
4. Missing section-8 fields → HD-RP1-003 approved.  
5. Shadow body thickness → HD-RP1-007=T approved.  
6. Whether RP1 edits `schema_index.yaml` → no.  
7. Whether RP1 puts artifacts in the wheel → HD-RP1-006=A, no.  
8. `v3_1` filename form → `v3-1` approved.  
9. Go binary retention → HD-CLEANUP-001 NEED_MORE_EVIDENCE.  
10. Dual `default_policy` → HD-CLEANUP-003 accept for RP1.  
11. `.banyan` mapping role names → out of RP1.  
12. Physical presence of superseded v1.0 baseline files → not found.  
13. Go tests not re-run.  
14. `.DS_Store` hygiene → HD-CLEANUP-002 later, not RP1.

---

# O. Human Decision Questions

Asked in the review; answered by Human Authority. Formal store: `01_decisions/RP1_HUMAN_DECISIONS.yaml`.

| ID | Decision |
|---|---|
| HD-RP1-001 | A |
| HD-RP1-002 | A |
| HD-RP1-003 | A |
| HD-RP1-007 | T |
| HD-RP1-006 | A |
| HD-CLEANUP-001 | NEED_MORE_EVIDENCE |
| HD-CLEANUP-002 | APPROVE_LATER_HYGIENE_CLEANUP; `execute_in_rp1: false` |
| HD-CLEANUP-003 | ACCEPT_CURRENT_STATE_FOR_RP1; `execute_in_rp1: false` |
| HD-CLEANUP-GATE | ZERO_DELETE_IN_RP1; `delete_count: 0` |

Additional authority decision: current semantic authority remains R1 Registry / Contract Authority. All RP1 `artifacts/**` files must carry `authority_class: NON_AUTHORITATIVE_SHADOW_MATERIALIZATION`.

---

# P. Pre-construction PLAN_CONFORMANCE_CHECK

| Check | Result |
|---|---|
| Review only, no Implementation | PASS |
| Did not create `artifacts/**` during review | PASS |
| Did not modify Framework files during review | PASS |
| Did not delete files during review | PASS |
| Did not change `migration_artifacts.yaml` / Registry / Loader / Runtime / CLI | PASS |
| Did not change `.banyan` / did not re-init | PASS |
| Did not change docs/project, CURRENT, Final Activation | PASS |
| Did not delete Legacy v3.1 | PASS |
| Did not cut over authority / did not enter RP2 | PASS |
| Did not change the nine frozen directory names | PASS |
| Did not adopt an unapproved equivalent | PASS |
| Did not decide UNKNOWNs unilaterally | PASS |
| Did not redesign R1 / did not fabricate IDs | PASS |
| 43/43 listed | PASS |
| State Domains unmerged | PASS |
| Capability not promoted to Skill | PASS |
| Source Role not treated as Collaboration/Banyan Role | PASS |
| Role/Permission/Git Identity/Auth not mixed | PASS |
| Shadow vs Canonical distinguished | PASS |
| Token principle not used to skip checks | PASS |
| Cleanup zero delete | PASS |
| Old R0→R2 route not revived | PASS |

Review terminal state at the time: `READY_FOR_HUMAN_REVIEW`.

After Human Decisions: `HUMAN_DECISIONS_APPROVED`.

This pack materialization does not start RP1 Implementation.

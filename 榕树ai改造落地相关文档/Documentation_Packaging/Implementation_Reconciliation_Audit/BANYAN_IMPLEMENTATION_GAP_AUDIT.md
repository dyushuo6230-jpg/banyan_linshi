# Banyan D1.5 Implementation Gap Audit

## Audit disposition

- Audit date: 2026-09-21
- Mode: `READ_ONLY`
- Result: `PASS_D1_5_AUDIT_WITH_GAPS_IDENTIFIED`
- Framework release finding: `FRAMEWORK_RELEASE_NOT_SELF_CONTAINED`
- Project Instance finding: `PROJECT_INSTANCE_SHADOW_PILOT_PARTIALLY_BOUND`
- D2 finding: `UNACCEPTED_DOCUMENTATION_OUTPUT`
- Legacy v3.1 source: available and inspected at `docs/governance/common_prd_v3.1/通用文档提示词v3.1.md` and `docs/governance/common_prd_v3.1/通用文档提示词v3.1完整使用说明.md`.

This report separates four different facts: a Legacy behavior was discovered, a contract was frozen, an implementation exists, and a project binding is active. One does not prove the next. Stage 07's `35/35` capability and `1026/1026` asset accounting proves design-time no-loss coverage only. Its own result keeps `real_apply_readiness: MIGRATION_BLOCKED` and `activation: OFF`.

## Evidence baseline

The audit read the current `banyan-framework/**` and `.banyan/**`, D0/D1 facts, targeted Stage 01–20 evidence, and the original v3.1 prompt and usage guide. The decisive evidence includes:

- Stage 03: 35 contracts are frozen; every entry says `implementation_frozen: false` and `provider_selected: false`.
- Stage 05: workflow, decision, and semantic-commit policy was designed; the workflow ends at `READY_FOR_EXECUTOR_OR_BLOCKED`.
- Stage 06: Change and Canonical Apply contracts were designed; no provider implementation was created.
- Stage 07: all Legacy items were accounted for and preserved in place; real apply remained blocked.
- Stages 09–10: Design Intelligence and Knowledge Publishing were contract-only.
- Stage 11: a shadow, rebuildable SQLite index was validated as `NOT_FINAL_RUNTIME_DB`.
- Stages 12–13: context, memory, freshness, evidence, impact, event, and learning contracts were accepted without Framework runtime implementations.
- Stage 15: the bounded Python Runtime was implemented.
- Stages 18/18.5: editor adapters, Go/Gin Control Plane, and 12-view WebUI were implemented.
- Stage 20: `v1.10-additive.1` was released as an additive supplement; `.banyan` remained a Shadow Pilot and Final Activation remained unauthorized.

## Current implementation boundary

The current executable Framework contains:

- strict default policy compilation and fail-closed permission evaluation;
- action and Pilot preflight;
- project Git inspection;
- semantic commit planning;
- fixture-scoped commit execution and current-project dry-run;
- append-only trace emission and paged trace reads;
- declarative provider-binding loading;
- Cursor, Codex, Generic Editor, and Pilot Cursor adapters;
- Python and Go control planes;
- 12 WebUI views, with no `/help` route;
- tests for these bounded paths.

The current Runtime API does not expose source intake, PRD lifecycle, informed-decision sessions, adaptive workflow execution, Change workspace, Canonical Apply, context recovery, memory, freshness, knowledge publishing, Design Intelligence execution, collaboration-role binding, or Help Center execution paths.

## AI Artifact migration findings

The full nine-category result is in `V3_1_ARTIFACT_MIGRATION_MATRIX.yaml`.

- `POLICY` has a real generalized runtime subset through `default-policy.yaml`, `PolicyCompiler`, and `PermissionEvaluator`.
- `STATE`, `DECISION_PROTOCOL`, and `COMPATIBILITY` are partial: bounded runtime states, permission decisions, and editor transports exist, but they do not cover the complete v3.1 semantics.
- `WORKFLOW` and `CONTEXT_RECOVERY` are frozen-contract-only.
- `ROLE` and `TEMPLATE` have no Framework-native migration target that is both shipped and consumable.
- `SKILL` remains split between preserved Legacy assets and documentation. No Framework-native Skill catalog or AnyDesign Runtime binding exists.
- No category has evidence supporting wholesale `SUPERSEDED_WITH_EVIDENCE` for the original v3.1 behavior set.

## Capability implementation findings

The required 35-row result is in `CAPABILITY_IMPLEMENTATION_MATRIX.yaml`.

Two bounded capabilities have complete current paths for their stated current scope:

- `CAP-EDITOR`: Cursor, Codex, and Generic Editor requests pass through a shared adapter gateway into the Control Plane and Runtime.
- `CAP-COMMIT`: semantic planning, fail-closed execution controls, fixture execution, current-project dry-run, rollback protection, and tests exist.

Several capabilities have useful implementation fragments but are not complete against their frozen contracts:

- `CAP-AUTH` implements fail-closed action authorization, but the complete contract registry and project-authority overlay are absent.
- `CAP-TRACE` implements append-only audit trace, but not the full canonical evidence/reference graph.
- The nine Design/AnyDesign capabilities still have Legacy scripts, but lack Stage 09 Provider Port bindings, Runtime consumers, and Framework integration tests.
- `CAP-PROFILE`, `CAP-PORT`, and `CAP-SQL` have Shadow or project-overlay data without complete runtime consumers.

The remaining governance, document, workflow, context, publishing, and UI-governance capabilities are frozen contracts or preserved compatibility references rather than executable Framework capabilities.

## Framework self-containment gap

`banyan-framework/` does not ship the authoritative Capability Contract Registry, Artifact Registry schema, Source Role Registry, workflow contracts, comprehensive state definitions, collaboration-role schema, Skill catalog/provider references, Provider Port schemas, Project Overlay schema, v3.1 compatibility mapping, or complete version/status/provenance rules.

The D0 Source of Truth directly points outside the Framework to `.banyan-refactor/stages/**` for these definitions. Stage 20 classifies `.banyan-refactor` as temporary and ready for later archival. A release that requires that temporary construction tree to explain its contracts cannot independently preserve its own semantics. The detailed verdict is in `FRAMEWORK_SELF_CONTAINMENT_AUDIT.md`.

## Project Instance audit

The 13-file `.banyan/` tree is internally consistent with the accepted Stage 17 Pilot scope, but it is intentionally narrow:

- Core contracts: no contract-registry pointer or packaged definitions.
- Source Roles: reference-only mappings exist, but no Source Role Registry binding.
- Workflows: no workflow binding.
- Skills/Providers: two Pilot bindings exist (`cursor-pilot-adapter` and `runtime-permission`); no Design provider binding.
- Policies: the Runtime policy hash is recorded; there is no general policy catalog binding.
- Profiles: project and contributor profiles exist; most Stage 04 variables remain `UNKNOWN` or `BLOCKED`.
- Roles: contributor permission metadata exists; no complete collaboration-role schema.
- Runtime state: bound for the Shadow Pilot.
- Index: an allowlist manifest exists; it is not the Stage 11 SQLite/query runtime.
- Trace: Pilot events exist and do not grant authorization.
- Migration: rollback metadata exists; Canonical Apply and Final Activation remain disabled.

The absence of final activation is an accepted Shadow Pilot constraint. Missing contract/source-role/workflow/role/provider bindings are implementation gaps if `.banyan` is expected to become a self-describing active Project Instance.

## Deferred design versus missing implementation

Stage-specific design acceptance is preserved: this audit does not call Stage 09–13 failures for doing contract work only. It records the present release consequence. The detailed classifications are in `DEFERRED_VS_MISSING_IMPLEMENTATION.md`.

The capabilities that block the intended end-to-end experience are Adaptive Workflow execution, natural-language orchestration, informed decisions, Change/Canonical Apply, and collaboration-role binding. Index, context, memory, freshness, evidence, impact, event, learning, publishing, and Design provider execution are accepted designs that remain outside the current Runtime. `/help` is a missing UX surface already identified by D0/D1.

## D0/D1/D2 consistency

D0 and D1 correctly distinguish frozen contracts from executable implementation and preserve nine `DOC-GAP-CANDIDATE` items. Their Framework version facts remain consistent: release `v1.10-additive.1`, governance CURRENT `v1.9.1`, Runtime package `0.1.0`, Project Instance Shadow Pilot, Final Activation false.

The current tree also contains 16 files under `banyan-framework/docs/user-guide/`, and `docs/README.md` plus `DOCUMENTATION_MAP.md` describe D2 as complete. No `D2_USER_GUIDE_ACCEPTANCE_REPORT.md` exists. Under the D1.5 rule, these files are retained but classified `UNACCEPTED_DOCUMENTATION_OUTPUT`. This audit neither validates nor continues D2, and it does not refresh the D0 Source of Truth.

## Gap register

### IR-AUDIT-GAP-001 — Release semantics depend on the temporary construction tree

- Priority: P0
- Evidence: authoritative registries/contracts live under `.banyan-refactor/stages/**`; D0 cites them directly; Stage 20 plans later bootstrap retirement.
- Consequence: the release cannot fully explain or validate its own declared capability model after construction evidence is archived.
- Classification: `FRAMEWORK_RELEASE_NOT_SELF_CONTAINED`.

### IR-AUDIT-GAP-002 — v3.1 artifact behavior is accounted but not fully migrated

- Priority: P0
- Evidence: Stage 07 is shadow design with activation off; ROLE and TEMPLATE lack shipped Framework targets; SKILL and compatibility assets remain external.
- Consequence: preserving source files does not provide stable Framework registry, loader, consumer, runtime, or tests.

### IR-AUDIT-GAP-003 — Main natural-language delivery loop has no executor

- Priority: P1
- Evidence: no Framework path performs natural language -> adaptive workflow -> informed decision -> Change/Canonical Apply -> validation.
- Consequence: the target developer experience must be manually orchestrated outside the Framework.

### IR-AUDIT-GAP-004 — Project Instance cannot bind the full contract model

- Priority: P1
- Evidence: `.banyan/overlays/bindings.yaml` has no bindings; no contract/source-role/workflow/role registry reference exists; provider bindings are Pilot-only.
- Consequence: Final Activation cannot rely on a self-describing, complete Project Instance binding graph.

### IR-AUDIT-GAP-005 — Knowledge, context, and evidence runtimes remain outside Framework

- Priority: P2
- Evidence: Stage 11 shadow SQLite is not a final runtime DB; Stages 12–13 accepted contracts without runtime execution; Stage 10 ran no publisher.
- Consequence: freshness-aware recovery, memory, impact, events, learning, and Project Guide publishing are unavailable as Framework services.

### IR-AUDIT-GAP-006 — Design provider capabilities have no Framework binding

- Priority: P2
- Evidence: Legacy AnyDesign scripts exist; Stage 09 states no adapter/runtime was produced; `.banyan/providers/bindings.yaml` contains no Design provider.
- Consequence: nine design capabilities cannot be invoked through Runtime/Control Plane with contract enforcement.

### IR-AUDIT-GAP-007 — Collaboration role model is documentation-only

- Priority: P1
- Evidence: no Runtime role enum/binding schema exists for Implementation Owner, Draft Contributor, Reviewer, and Project Authority.
- Consequence: workflow and authorization cannot consistently resolve collaboration responsibility.

### IR-AUDIT-GAP-008 — Help Center is absent

- Priority: P3
- Evidence: the implemented routes contain 12 views and no `/help` endpoint or page.
- Consequence: in-product guidance is unavailable.

### IR-AUDIT-GAP-009 — D2 output has no acceptance record

- Priority: P3
- Evidence: 16 User Guide files and updated navigation exist; `D2_USER_GUIDE_ACCEPTANCE_REPORT.md` does not.
- Consequence: documentation claims D2 completion without the required formal acceptance artifact.
- Classification: `UNACCEPTED_DOCUMENTATION_OUTPUT`.

## Non-actions

No gap was repaired. No file under `banyan-framework/**`, `.banyan/**`, or `docs/project/**` was modified. No Git operation, migration, D2/D3 continuation, or Final Activation was performed.

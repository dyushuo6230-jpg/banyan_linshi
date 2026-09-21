# Stage 06 Acceptance Report

## Status

`COMPLETED / PASS_CHANGE_WORKSPACE_AND_CANONICAL_APPLY_CONTRACT_FREEZE / NOT_IMPLEMENTED`

## Low-Token Verification

No repository rediscovery, Stage 01–05 rerun, asset rebuild, Git-history analysis, or full capability reload occurred. A targeted metadata query found no verified Legacy OpenSpec instance.

## Change Workspace Generic Contract

The Core contract defines stable change identity, lifecycle, artifacts, relationships, decisions, evidence, apply state, and provider binding without provider-specific filenames or fields. A workspace is never canonical truth.

## Provider Port

Nine operations define request, response, failure, timeout/cancel, evidence, and side effects. No provider implementation was created.

## OpenSpec Binding

OpenSpec is represented by a separate `DESIGN_ONLY_INACTIVE` binding. Provider paths, artifact names, and lifecycle mappings do not leak into Generic Core. Activation requires later provider validation.

## Change Lifecycle / Identity

Banyan stable identity remains authoritative and cannot be replaced by provider identity. Lifecycle transitions require explicit evidence and gates.

## Parallel Draft / Promotion

Multiple candidates are supported. Selection, merge, preservation, rejection, or blocking requires explicit resolution through the Stage 05 Decision Gate. Timestamp-, provider-, and AI-selected winners are forbidden.

## Canonical Apply

Apply is an explicit controlled transaction requiring preview, impact, reference and freshness checks, decision, authorization, checkpoint, validation, evidence, and reconciliation. Stage 06 performs no apply.

## Apply Preview / Impact

Preview binds provider and canonical revisions and enumerates creates, updates, supersessions, preserved artifacts, reference/derived impacts, conflicts, warnings, protected targets, rollback point, decision level, and authorization.

## Reference Integrity / Reconciliation

Stable IDs, references, supersession, authority, provenance, canonical/workspace state, derived projections, and trace lineage must all pass. Partial or inconsistent results become `RECONCILIATION_BLOCKED`.

## Authorization / Rollback

Authorization consumes Stage 05 decision and confirmation contracts. Rollback requires a verified snapshot, affected artifacts, reverse and reference-restoration plans, validation, result, and evidence.

## Archive / History

Archive is a semantic state transition only. It does not imply delete, move, compression, or Git commit.

## CON-002 Carry-over

CON-002 remains `OPEN` with Stage 12 ownership. Stage 06 models divergence but does not adjudicate project freshness.

## Open Risks

R03-PURITY, R03-SOURCE, CON-002, R03-COST, R03-SECRET, and R03-LOCAL remain open. Secret recovery remains `PARTIAL_APPROVED`.

## V06-01..V06-20

All 20 validations pass.

## Hard Metrics

All seven hard metrics are `0`.

## Actual Writes / Protected Areas

Writes are limited to this run and the two Bootstrap files. No canonical project document, business code, Legacy/OpenSpec workspace, Secret body, Git state, or `.banyan` instance was changed.

## Bootstrap Register / Trace

Both Bootstrap records mark Stage 06 contract design complete with provider activation and real apply off.

## NEXT_STAGE_HANDOFF

The handoff carries provider-neutral workspace, inactive OpenSpec binding, apply/reconciliation contracts, and inherited blockers.

## Stage 07 Entry Gate

`PASS_FOR_STAGE07_REFERENCE_MIGRATION_DESIGN_WITH_INHERITED_BLOCKERS`; execution is not authorized and Stage 07 was not started.

# F1 Core Object Model — Reconciliation v1.0

> Stage: F1 — Core Object Model  
> Status: HUMAN_APPROVED / ARCHITECTURE_FREEZE_READY

## 1. Reconciled sources

F1 is based on four source classes:
- historical communication and user-approved decisions
- Legacy v3.1 governance semantics
- accepted Refactor / Stage contracts
- current Framework / R1 / RP1 reality

## 2. Preserved boundaries

The following must not be silently changed:
- Capability != Skill
- Source Role != Collaboration Role != future executable AI Functional Role
- Role != Permission != Git Identity != Authentication
- State domains remain separate
- Project Instance / Binding / Runtime / Context / Evidence / Infrastructure are not automatically Artifacts
- RP1 classifications remain valid as migration/shadow evidence
- TOKEN_EFFICIENCY_MUST_NOT_REDUCE_GOVERNANCE_FIDELITY

## 3. F1 problem

Before F1, “Artifact” was being used for several different concepts:
- reusable Framework definitions
- formal Project engineering outputs
- runtime/operational records
- project bindings
- index/infrastructure records

F1 freezes top-level object families so later taxonomy, storage, runtime and WebUI design do not mix unrelated meanings.

## 4. Mandatory carried scenarios

- `SCENARIO-DELIVERY-01`: multiple Batches are complete but overall delivery is not closed when a new requirement arrives.
- `SCENARIO-DELIVERY-02`: some Batches are complete, some in progress, some not started when a requirement changes.
- `SCENARIO-PROGRESS-01`: code + tests are complete while Governance Closeout is incomplete; development progress must not remain 0.
- `SCENARIO-INTEGRATION-01`: development is complete but intentionally not merged to `main`; this must not block development completion or Batch closeout.

These do not alter F1. They are mandatory later inputs for F7/F10.

## 5. Result

F1 is an additive semantic clarification layer. It does not invalidate R0, R1 or RP1 and does not authorize RP2 cutover or `.banyan` mutation.

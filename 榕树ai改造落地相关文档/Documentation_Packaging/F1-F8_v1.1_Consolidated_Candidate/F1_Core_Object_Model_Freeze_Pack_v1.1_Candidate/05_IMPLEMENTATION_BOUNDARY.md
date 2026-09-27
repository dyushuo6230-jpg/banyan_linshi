# F1 Core Object Model — Implementation Boundary v1.0

> **Candidate status:** `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW`. v1.0 approval/freeze statements below are retained as historical source-contract evidence; this v1.1 text is not a new freeze or implementation authorization.


> Status: ARCHITECTURE FREEZE ONLY

## Allowed

F1 authorizes later stages to consume the frozen top-level object model.

## Not authorized by F1

- RP2 authority cutover
- `.banyan` mutation
- current Loader/Registry authority changes
- RP1 directory rename/delete
- 35 Capability -> 35 Skill promotion
- final AI Functional Role list
- final DefinitionArtifact subtype list
- SQLite DDL / physical DB layout
- Batch lifecycle implementation
- progress metric implementation
- `main` merge policy implementation
- Change/Canonical Apply runtime
- Evidence runtime schema
- WebUI implementation
- Legacy deletion

## Cursor decision

Immediate Cursor code execution is NOT automatically authorized by F1.

F1 is an Architecture Freeze Pack. Any code/schema implementation must later receive an Implementation Freeze with exact file scope, schema changes, migration, rollback and acceptance tests.

## Mandatory future carryover

These scenarios must remain active inputs:
- SCENARIO-DELIVERY-01
- SCENARIO-DELIVERY-02
- SCENARIO-PROGRESS-01
- SCENARIO-INTEGRATION-01

## Candidate deferred-obligation boundary

Material deferred items retain subject, question, rationale, declaring owner, explicit or deterministically derivable future owner, trigger, preconditions, must-happen-before, forbidden-before-resolution guard, expected resolution, authority requirement, dependencies, status, provenance and closure/supersession history. Implementation Detail Deferred, Required Future Decision, Future Capability Reserved, and Migration/Cutover Deferred are distinct. DEFERRED is intentional postponement, unlike UNKNOWN evidence or UNRESOLVED required judgment; it is not undefined, forgotten, unowned or authorized work. A planning/governance dependency is not a runtime resolution dependency; implicit deferred cycles require architecture/planning resolution. Trigger reached requires a resolution attempt, not authorization; if prerequisites are absent the result is NOT_READY/UNKNOWN, and a protected action reaching its must-before boundary is BLOCKED. RESOLVED is neither IMPLEMENTED nor ACTIVATED. Supersession or NOT_APPLICABLE retains history. FUTURE is not an owner or miscellaneous unowned bucket; a future capability without a present implementation owner retains an explicit Owner Resolution Gate. Canonical mutation belongs to F7, project binding/reconciliation to F8, index/retrieval/freshness/impact to F9, runtime permission/execution to F10, UX/control plane to F11, and migration/retirement to F12. A later stage is not higher authority; future ownership grants no current authorization. Future Capability Reserved, including AI_AUTONOMOUS_LEARNING, is neither a roadmap commitment, current capability nor current authorization; activation requires a separate future proposal and applicable review. Exact schema/enum/API/UI/lock/CAS/index/migration mechanics remain deferred. Implementation, RP2, authority cutover, canonical replacement, final activation and legacy retirement remain NOT_AUTHORIZED; SQLite Physical Schema remains NOT_FROZEN.

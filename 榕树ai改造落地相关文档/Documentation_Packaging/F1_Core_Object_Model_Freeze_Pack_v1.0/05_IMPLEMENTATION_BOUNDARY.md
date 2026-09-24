# F1 Core Object Model — Implementation Boundary v1.0

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

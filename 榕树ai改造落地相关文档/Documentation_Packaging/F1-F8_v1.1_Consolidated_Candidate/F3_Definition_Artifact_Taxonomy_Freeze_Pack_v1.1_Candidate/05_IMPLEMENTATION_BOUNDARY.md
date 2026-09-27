# 05_IMPLEMENTATION_BOUNDARY.md

> **Candidate status:** `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW`. v1.0 approval/freeze statements below are retained as historical source-contract evidence; this v1.1 text is not a new freeze or implementation authorization.


# F3 Implementation Boundary

F3 authorizes downstream architecture work to consume the frozen taxonomy.

It does **not** authorize:

```text
RP2 implementation
Loader/Resolver changes
Registry changes
Manifest changes
Schema changes
new physical directories
movement of RP1 43 shadow artifacts
artifact deletion
artifact reclassification
authority cutover
.banyan activation
Final Activation
```

Current R1/RP1 migration categories remain protected.

Exact Context Recovery mapping is deferred to F9.

Before any physical taxonomy migration, an Implementation Freeze must define:
- source category,
- target type,
- Stable ID strategy,
- lineage,
- reference migration,
- schema validation,
- compatibility impact,
- authority cutover,
- rollback/recovery,
- acceptance tests,
- `PLAN_CONFORMANCE_CHECK`.

No implementer may infer these silently.

## Candidate deferred-obligation boundary

Material deferred items retain subject, question, rationale, declaring owner, explicit or deterministically derivable future owner, trigger, preconditions, must-happen-before, forbidden-before-resolution guard, expected resolution, authority requirement, dependencies, status, provenance and closure/supersession history. Implementation Detail Deferred, Required Future Decision, Future Capability Reserved, and Migration/Cutover Deferred are distinct. DEFERRED is intentional postponement, unlike UNKNOWN evidence or UNRESOLVED required judgment; it is not undefined, forgotten, unowned or authorized work. A planning/governance dependency is not a runtime resolution dependency; implicit deferred cycles require architecture/planning resolution. Trigger reached requires a resolution attempt, not authorization; if prerequisites are absent the result is NOT_READY/UNKNOWN, and a protected action reaching its must-before boundary is BLOCKED. RESOLVED is neither IMPLEMENTED nor ACTIVATED. Supersession or NOT_APPLICABLE retains history. FUTURE is not an owner or miscellaneous unowned bucket; a future capability without a present implementation owner retains an explicit Owner Resolution Gate. Canonical mutation belongs to F7, project binding/reconciliation to F8, index/retrieval/freshness/impact to F9, runtime permission/execution to F10, UX/control plane to F11, and migration/retirement to F12. A later stage is not higher authority; future ownership grants no current authorization. Future Capability Reserved, including AI_AUTONOMOUS_LEARNING, is neither a roadmap commitment, current capability nor current authorization; activation requires a separate future proposal and applicable review. Exact schema/enum/API/UI/lock/CAS/index/migration mechanics remain deferred. Implementation, RP2, authority cutover, canonical replacement, final activation and legacy retirement remain NOT_AUTHORIZED; SQLite Physical Schema remains NOT_FROZEN.

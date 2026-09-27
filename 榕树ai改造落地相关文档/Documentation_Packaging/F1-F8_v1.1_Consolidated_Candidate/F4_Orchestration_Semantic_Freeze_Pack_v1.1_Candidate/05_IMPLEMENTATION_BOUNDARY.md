# 05_IMPLEMENTATION_BOUNDARY.md

> **Candidate status:** `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW`. v1.0 approval/freeze statements below are retained as historical source-contract evidence; this v1.1 text is not a new freeze or implementation authorization.


Status: `ARCHITECTURE_FROZEN`
Implementation Authorized: `NO`

## Allowed semantic use
Later stages may treat F4 Role / Capability / Skill / Workflow / Resolver / Handoff / Validation / Standards-boundary / Atom-closure semantics as frozen input.

## Not authorized
F4 does not authorize Cursor implementation, RP2 implementation, Authority Cutover, artifact-directory redesign, schema/registry authority changes, `.banyan` rewrite/re-init, Full Legacy Semantic Migration, Canonical project writes, Legacy retirement/deletion, provider execution, Permission engine changes or Final Activation.

## Owner stages
- F5: PRD / Requirement governance, related Policy/State/Decision/Template boundaries.
- F6: UI_SPEC / Design Truth / AnyDesign / Visual Validation / Visual Repair domain semantics.
- F7: Change Workspace / Draft / Human Decision application / Canonical Apply / Rollback / Reference Integrity.
- F8: ProjectInstance / init-adopt-migrate-reconcile / Binding / Provider Selection / Standard applicability.
- F9: Context / Index / Memory / Freshness / Evidence / Trace / Impact / Learning.
- F10: Runtime / Provider / MCP / Permission / Adapter / Git / Semantic Commit execution.
- F11: WebUI / Help / Guided Setup / Control Plane.
- F12: Compatibility / Reference Project reconcile / zero-runtime-dependency / retirement.

## Deferred physical design
Exact directories, filenames, schemas, SQLite DDL, enum names, API routes, CLI commands, registry layout and Execution Plan persistence are not frozen by F4.

## Migration sequencing
`CROSS-STAGE-GATE-01` must pass before Full Legacy Semantic Migration. Before then only inventory, discovery, semantic classification, owner mapping, transformation planning, shadow materialization, compatibility analysis and dry-run are allowed.

If migration discovers an unexpected semantic value: block only the affected unit where safe; classify it; route it to an existing owner; if current architecture cannot express it, open an owner-stage Change Proposal; never invent a type or silently coerce it.

Principle: **Design precedes migration. Migration may discover new facts, but migration must not invent architecture to absorb them.**

## Candidate deferred-obligation boundary

Material deferred items retain subject, question, rationale, declaring owner, explicit or deterministically derivable future owner, trigger, preconditions, must-happen-before, forbidden-before-resolution guard, expected resolution, authority requirement, dependencies, status, provenance and closure/supersession history. Implementation Detail Deferred, Required Future Decision, Future Capability Reserved, and Migration/Cutover Deferred are distinct. DEFERRED is intentional postponement, unlike UNKNOWN evidence or UNRESOLVED required judgment; it is not undefined, forgotten, unowned or authorized work. A planning/governance dependency is not a runtime resolution dependency; implicit deferred cycles require architecture/planning resolution. Trigger reached requires a resolution attempt, not authorization; if prerequisites are absent the result is NOT_READY/UNKNOWN, and a protected action reaching its must-before boundary is BLOCKED. RESOLVED is neither IMPLEMENTED nor ACTIVATED. Supersession or NOT_APPLICABLE retains history. FUTURE is not an owner or miscellaneous unowned bucket; a future capability without a present implementation owner retains an explicit Owner Resolution Gate. Canonical mutation belongs to F7, project binding/reconciliation to F8, index/retrieval/freshness/impact to F9, runtime permission/execution to F10, UX/control plane to F11, and migration/retirement to F12. A later stage is not higher authority; future ownership grants no current authorization. Future Capability Reserved, including AI_AUTONOMOUS_LEARNING, is neither a roadmap commitment, current capability nor current authorization; activation requires a separate future proposal and applicable review. Exact schema/enum/API/UI/lock/CAS/index/migration mechanics remain deferred. Implementation, RP2, authority cutover, canonical replacement, final activation and legacy retirement remain NOT_AUTHORIZED; SQLite Physical Schema remains NOT_FROZEN.

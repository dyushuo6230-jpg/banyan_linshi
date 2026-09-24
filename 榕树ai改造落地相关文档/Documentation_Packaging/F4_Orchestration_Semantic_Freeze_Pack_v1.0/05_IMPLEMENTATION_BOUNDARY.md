# 05_IMPLEMENTATION_BOUNDARY.md

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

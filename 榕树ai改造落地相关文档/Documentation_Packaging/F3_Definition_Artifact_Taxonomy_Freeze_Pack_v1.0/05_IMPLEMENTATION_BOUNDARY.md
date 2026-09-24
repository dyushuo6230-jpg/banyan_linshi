# 05_IMPLEMENTATION_BOUNDARY.md

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

# Stage 19 — Full Technical Acceptance / RC

Stage19 verifies the final implementation after Stage18.5.

No new feature work should be introduced.

Acceptance model:

```text
Evidence
→ Claim
→ Independent Verification
→ PASS / BLOCKED / FAIL
```

A historical PASS is usable evidence, but Stage19 must verify critical cross-stage invariants where later changes could have invalidated them.

Priority revalidation:

```text
Stage18.5 changed WebUI/transport
→ revalidate Runtime boundary / adapters / provenance / Git safety

Stage17 activated Pilot .banyan
→ revalidate Pilot integrity / project-instance boundary

Stage15 introduced Runtime
→ revalidate compiler / policy / commit safety
```

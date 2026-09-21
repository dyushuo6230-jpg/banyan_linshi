# Upgrade and Migration Guide

Normal Banyan upgrades do not recreate `.banyan-refactor/`. Use the installed Banyan mechanisms:

```text
Change Proposal
→ Evidence and Impact
→ Migration Plan
→ Shadow / Preview
→ Validation
→ Explicit Apply Authorization
→ Rollback Readiness
→ Acceptance
```

Record eligible project migrations under `.banyan/migrations/` or a governed change workspace. Every proposal must identify current/candidate versions, changed contracts, affected artifacts, authority and freshness, compatibility, data transformations, rollback, validation and acceptance criteria.

Run policy and schema checks before preview. Preview must not become authorization. Apply only after target-scoped authorization and a checkpoint. Validate references, provenance, trace, Project Instance integrity, Git state and no-loss coverage. A failed validation follows the documented rollback path and remains visible in history.

Framework software upgrades and Project Instance activation are separate decisions. Updating reusable binaries or source packages cannot promote a Pilot, replace canonical documents, resolve authority conflicts or change the current version pointer by itself.

# 20-G Upgrade / Migration Guide

Future Banyan upgrades must NOT recreate `.banyan-refactor/` as normal behavior.

Mature upgrade lifecycle:

```text
Change Proposal
→ Impact
→ Migration Plan
→ Shadow / Preview
→ Validation
→ Apply
→ Rollback readiness
→ Acceptance
```

Use Banyan's own migration/change mechanism, including `.banyan/migrations/` where appropriate.

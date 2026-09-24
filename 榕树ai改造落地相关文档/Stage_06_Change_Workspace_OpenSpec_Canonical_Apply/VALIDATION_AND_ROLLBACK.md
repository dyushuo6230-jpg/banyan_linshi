# Stage 06 Validation

| ID | Check | PASS |
|---|---|---|
| V06-01 | Upstream | Stage05 and relevant frozen inputs valid |
| V06-02 | Low Token | no repo rediscovery |
| V06-03 | Workspace Core | provider-neutral |
| V06-04 | Provider Port | complete operations/failures |
| V06-05 | OpenSpec Binding | separate from Core |
| V06-06 | Change Identity | stable Banyan ID distinct |
| V06-07 | Lifecycle | controlled transitions |
| V06-08 | Artifact Relations | typed relationships |
| V06-09 | Parallel Draft | multi-candidate supported |
| V06-10 | Promotion | no silent winner |
| V06-11 | Apply Preview | mandatory |
| V06-12 | Reference Check | mandatory |
| V06-13 | Canonical Authority | workspace not truth |
| V06-14 | Authorization | Stage05 gate consumed |
| V06-15 | Reconciliation | explicit post-apply validation |
| V06-16 | Rollback | contract complete |
| V06-17 | Archive | semantic, not implicit delete |
| V06-18 | Secret Safety | 13 bodies untouched |
| V06-19 | Write Scope | no legacy/canonical mutation |
| V06-20 | Handoff | Stage07 handoff complete, Stage07 not started |

Hard metrics:

```text
CHANGE_WORKSPACE_WITHOUT_PROVIDER_PORT = 0
PROVIDER_SPECIFIC_FIELD_IN_CORE_CHANGE_SCHEMA = 0
CANONICAL_APPLY_WITHOUT_PREVIEW = 0
CANONICAL_APPLY_WITHOUT_REFERENCE_CHECK = 0
PARALLEL_DRAFT_WITHOUT_RECONCILIATION_PATH = 0
SILENT_CONFLICT_WINNER_PATH = 0
APPLY_PATH_WITHOUT_AUTHORIZATION_GATE = 0
```

# Stage 11 Validation

| ID | Check | PASS |
|---|---|---|
| V11-01 | Upstream | Stage10 seal / requirements valid |
| V11-02 | Low Token | no repo/Git rediscovery |
| V11-03 | SQLite Schema | schema parses and initializes |
| V11-04 | Index Authority | index marked non-canonical |
| V11-05 | Stable ID | all indexed entities have stable ID |
| V11-06 | Locator | path separated from identity |
| V11-07 | Source Role | classification available |
| V11-08 | References | imported without silent loss |
| V11-09 | Unresolved | missing target remains unresolved |
| V11-10 | Regex Literal | NOT_A_REFERENCE preserved |
| V11-11 | Provenance | indexed or UNKNOWN |
| V11-12 | Trace | lineage fields complete |
| V11-13 | Trace Auth | trace grants no authorization |
| V11-14 | History | non-success states preserved |
| V11-15 | Projection | source links preserved |
| V11-16 | Progress | current/history distinguished |
| V11-17 | Handover | canonical/operational refs queryable |
| V11-18 | ProviderBinding | activation state preserved |
| V11-19 | Secret | body/hash absent |
| V11-20 | Query Suite | required queries pass |
| V11-21 | Rebuild | isolated rebuild proof passes |
| V11-22 | Determinism | count/hash invariants explainable |
| V11-23 | Write Scope | shadow/run/bootstrap only |
| V11-24 | Handoff | Stage12 handoff complete; not started |

Hard metrics:

```text
INDEX_RECORD_WITHOUT_STABLE_ID = 0
INDEX_RECORD_WITHOUT_SOURCE_ROLE_OR_CLASSIFICATION = 0
INDEX_AS_CANONICAL_TRUTH_PATH = 0
REFERENCE_EDGE_LOST_DURING_IMPORT = 0
UNRESOLVED_REFERENCE_WITH_INVENTED_TARGET = 0
HISTORY_NON_SUCCESS_STATE_NORMALIZED_TO_SUCCESS = 0
TRACE_EVENT_WITHOUT_LINEAGE = 0
SECRET_BODY_OR_HASH_INDEXED = 0
SHADOW_DB_NOT_REBUILDABLE_FROM_STRUCTURED_INPUTS = 0
```

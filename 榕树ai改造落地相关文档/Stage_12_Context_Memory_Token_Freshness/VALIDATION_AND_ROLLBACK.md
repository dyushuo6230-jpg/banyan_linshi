# Stage 12 Validation

| ID | Check | PASS |
|---|---|---|
| V12-01 | Upstream | Stage11 seal/query surface valid |
| V12-02 | Low Token | query-first, no rediscovery |
| V12-03 | Context Types | layered context explicit |
| V12-04 | Selection | authority/freshness precede cost |
| V12-05 | Freshness | no mtime-only winner |
| V12-06 | CON-002 | resolved or typed blocked with evidence |
| V12-07 | Conflict | no silent winner |
| V12-08 | Memory | never canonical truth |
| V12-09 | Memory Source | source refs mandatory |
| V12-10 | Memory Freshness | as_of/freshness mandatory |
| V12-11 | Recovery | current/historical differentiated |
| V12-12 | Handover | latest valid, not latest-file only |
| V12-13 | Token Budget | mandatory context cannot be dropped |
| V12-14 | Compaction | blockers preserved |
| V12-15 | Compaction | authority/provenance preserved |
| V12-16 | Cache | version/freshness keyed |
| V12-17 | On Demand | bounded and logged |
| V12-18 | Historical Refs | typed disposition without invention |
| V12-19 | Regex Literal | remains NOT_A_REFERENCE |
| V12-20 | Secret | body excluded |
| V12-21 | Cost Policy | no vendor/model/fixed percentage |
| V12-22 | Stage13 Surface | evidence/impact context complete |
| V12-23 | Write Scope | run/bootstrap only |
| V12-24 | Handoff | Stage13 not started |

Hard metrics:

```text
FRESHNESS_DECISION_BY_MTIME_ONLY = 0
FRESHNESS_CONFLICT_WITH_SILENT_WINNER = 0
CONTEXT_SUMMARY_WITHOUT_SOURCE_REFS = 0
CONTEXT_SUMMARY_WITHOUT_AS_OF_OR_FRESHNESS = 0
CONTEXT_COMPACTION_DROPPED_BLOCKER = 0
MEMORY_PROMOTED_TO_CANONICAL_TRUTH = 0
TOKEN_BUDGET_BYPASSED_REQUIRED_CONTEXT = 0
HISTORICAL_REFERENCE_WITH_INVENTED_TARGET = 0
SECRET_BODY_INCLUDED_IN_CONTEXT_INDEX = 0
```

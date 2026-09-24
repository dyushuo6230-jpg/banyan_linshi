# Stage 13 Validation

| ID | Check | PASS |
|---|---|---|
| V13-01 | Upstream | Stage12 seal/query handoff valid |
| V13-02 | Low Token | query-first, no rediscovery |
| V13-03 | Evidence | source refs mandatory |
| V13-04 | Evidence | provenance/classification mandatory |
| V13-05 | Evidence Chain | every derived step traceable |
| V13-06 | Impact | typed direct/transitive/potential/unknown |
| V13-07 | Impact Basis | no unsupported direct edge |
| V13-08 | Decision Evidence | human decision preserved distinctly |
| V13-09 | Event | observed/derived/correlated separated |
| V13-10 | Causality | correlation not auto causality |
| V13-11 | Prompt Version | observation version-bound |
| V13-12 | Outcome Attribution | multi-factor by default |
| V13-13 | Learning Candidate | proposal only |
| V13-14 | Evaluation | baseline/counterexample required |
| V13-15 | Promotion | approval/change gate mandatory |
| V13-16 | Project/Core | no auto project→core promotion |
| V13-17 | Secret | no secret learning |
| V13-18 | CON-002 | remains typed blocked |
| V13-19 | Historical Refs | dispositions unchanged |
| V13-20 | Cost Telemetry | abstract, provider-neutral |
| V13-21 | False Pos/Neg | typed register supported |
| V13-22 | Stage14 Handoff | authorization requirements complete |
| V13-23 | Write Scope | run/bootstrap only |
| V13-24 | Handoff | Stage14 not started |

Hard metrics:

```text
EVIDENCE_RECORD_WITHOUT_SOURCE_REF = 0
EVIDENCE_RECORD_WITHOUT_PROVENANCE_OR_CLASSIFICATION = 0
CORRELATION_PROMOTED_TO_CAUSALITY_WITHOUT_EVIDENCE = 0
IMPACT_EDGE_WITHOUT_BASIS = 0
PROMPT_OUTCOME_WITH_SINGLE_FACTOR_ATTRIBUTION_BY_DEFAULT = 0
LEARNING_CANDIDATE_AUTO_APPLIED = 0
PROJECT_SPECIFIC_LEARNING_AUTO_PROMOTED_TO_CORE = 0
SECRET_OR_SECRET_DERIVED_LEARNING_RECORD = 0
CON002_RESOLVED_BY_LEARNING_OR_EVENT_FREQUENCY = 0
```

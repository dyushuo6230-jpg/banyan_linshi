# Stage 08 Validation

| ID | Check | PASS |
|---|---|---|
| V08-01 | Upstream | Stage07 seal / blockers preserved |
| V08-02 | Low Token | no rediscovery |
| V08-03 | PRD Authority | business truth explicit |
| V08-04 | UI_SPEC Authority | no second business truth |
| V08-05 | Scope | every UI_SPEC application-scoped |
| V08-06 | Enablement | explicit state |
| V08-07 | Partial | partial coverage explicit |
| V08-08 | Design Evidence | evidence authority defined |
| V08-09 | Static Guessing | unsupported behavior not promoted |
| V08-10 | Lifecycle | states controlled |
| V08-11 | Approval | gate mandatory |
| V08-12 | PRD Trace | mandatory for approved UI_SPEC |
| V08-13 | Design Trace | mandatory |
| V08-14 | Version | independent versions tracked |
| V08-15 | Freshness | PRD relevant changes affect UI status |
| V08-16 | Change Integration | Canonical flow consumed |
| V08-17 | Readiness | approval required |
| V08-18 | v3.1 Compatibility | key UI semantics mapped |
| V08-19 | Write Scope | no canonical/legacy mutation |
| V08-20 | Handoff | Stage09 handoff, Stage09 not started |

Hard metrics:

```text
UI_SPEC_BUSINESS_TRUTH_DUPLICATION_PATH = 0
UI_SPEC_WITHOUT_APPLICATION_SCOPE = 0
UI_SPEC_WITHOUT_EXPLICIT_ENABLEMENT_STATE = 0
APPROVED_UI_SPEC_WITHOUT_PRD_TRACE = 0
APPROVED_UI_SPEC_WITHOUT_DESIGN_EVIDENCE = 0
IMPLEMENTATION_READY_WITHOUT_APPROVAL_GATE = 0
PRD_RELEVANT_CHANGE_WITHOUT_UI_FRESHNESS_EFFECT = 0
```

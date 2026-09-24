# Stage 09 Validation

| ID | Check | PASS |
|---|---|---|
| V09-01 | Upstream | Stage08 seal valid |
| V09-02 | Low Token | no rediscovery/full corpus load |
| V09-03 | Source Intake | design source authority = EVIDENCE_ONLY |
| V09-04 | Provider Port | provider-neutral + failure semantics |
| V09-05 | Scene | normalized fields provider-neutral |
| V09-06 | Geometry | observed != fixed implementation |
| V09-07 | Semantic | confidence/evidence mandatory |
| V09-08 | Truth | only supported/approved content |
| V09-09 | Tokens | source/derived/recommended separated |
| V09-10 | Behavior | unsupported interactions UNKNOWN |
| V09-11 | Data | demo content not business truth |
| V09-12 | FACT | direct evidence only |
| V09-13 | INFERENCE | explicitly marked |
| V09-14 | RECOMMENDATION | explicitly marked |
| V09-15 | IR Input | framework-neutral |
| V09-16 | UI Governance | no auto promotion to UI_SPEC |
| V09-17 | Validation | versioned evidence inputs |
| V09-18 | Drift | typed drift categories |
| V09-19 | Compatibility | legacy UI design semantics mapped |
| V09-20 | Secret | protected bodies untouched |
| V09-21 | Write Scope | no canonical/code/provider implementation |
| V09-22 | Handoff | Stage10 handoff complete; Stage10 not started |

Hard metrics:

```text
PROVIDER_SPECIFIC_FIELD_IN_NORMALIZED_SCENE = 0
UNMARKED_INFERENCE_AS_FACT = 0
UNMARKED_RECOMMENDATION_AS_FACT = 0
STATIC_IMAGE_INTERACTION_ASSUMPTION = 0
OBSERVED_GEOMETRY_FORCED_TO_FIXED_LAYOUT = 0
DESIGN_OUTPUT_AUTO_PROMOTED_TO_UI_SPEC = 0
DESIGN_ARTIFACT_WITHOUT_PROVENANCE = 0
DESIGN_PROVIDER_PORT_WITHOUT_FAILURE_SEMANTICS = 0
```

# Acceptance Criteria and Expected Outputs

## Phase 1 — One-Pass Batch Repair

Expected new files:

```text
F1-F8_v1.1_Consolidated_Candidate/
00_CONSOLIDATION_CONTROL/
├── FINAL_EXHAUSTIVE_DISCOVERY_BEFORE_REPAIR.md
├── FINAL_NORMATIVE_CLAUSE_COVERAGE_MATRIX.md
└── FCFR_EXHAUSTIVE_BATCH_CORRECTION.md
```

Existing control docs may be factually updated only when necessary.

### Phase 1 acceptance

If there is no unresolved Human Decision:

```text
Post-repair PARTIAL = 0
Post-repair MISSING = 0
Post-repair CONTRADICTED = 0
Deterministic Blocking Finding = 0
Unauthorized New Semantic = 0
Cross-file Contradiction = 0
Implementation Leakage = 0
Candidate Freeze Leakage = 0
```

Candidate remains:

```text
AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW
```

This phase does not produce `PASS_PENDING_HUMAN_APPROVAL`.

## Phase 2 — Independent Final Review

Expected new file:

```text
F1-F8_v1.1_Consolidated_Candidate/
00_CONSOLIDATION_CONTROL/
FINAL_CONSOLIDATED_FREEZE_REVIEW_RERUN_03.md
```

### PASS requirements

```text
Approved Patch Mapping = 18/18
Approved Semantic Coverage = COMPLETE 18/18
Clause PARTIAL = 0
Clause MISSING = 0
Clause CONTRADICTED = 0
Silent Semantic Drop = 0
Unauthorized Supersession = 0
Authority Drift = 0
Owner Drift = 0
Competing Canonical Truth = 0
State-domain Collapse = 0
Current-effective Ambiguity = 0
Binding Winner Ambiguity = 0
Handoff Qualifier Loss = 0
Patch 016 Full Semantic Coverage = COMPLETE
Blocking Deferred Architecture Gap = 0
Unauthorized New Semantic = 0
Cross-file Contradiction = 0
Correction Regression = 0
Implementation Leakage = 0
Candidate Freeze Leakage = 0
Blocking Finding = 0
Human Decision Required = 0
```

Then and only then:

```text
FINAL_CONSOLIDATED_FREEZE_REVIEW_RERUN_03
= PASS_PENDING_HUMAN_APPROVAL

READY_FOR_HUMAN_FINAL_APPROVAL
= YES
```

Still prohibited:

```text
HUMAN_APPROVED
architecture_freeze_granted=true
freeze_baseline_established=true
new Freeze Baseline
merge main
F9
Implementation
```

## Git expectations

All work stays on:

```text
f1-f8-v1.1-consolidation
```

Do not merge main until Final Review PASS + explicit Human Final Freeze Approval + formal v1.1 Freeze Baseline packaging.

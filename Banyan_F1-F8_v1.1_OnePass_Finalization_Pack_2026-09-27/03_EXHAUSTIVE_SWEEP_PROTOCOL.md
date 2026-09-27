# Exhaustive Clause-Level Sweep Protocol

## Purpose

This protocol replaces:

```text
Patch title mapped = PASS
```

with clause-level evidence.

The sweep must be exhaustive before any repair begins.

## Phase A — Inventory all formal normative clauses

Read:

```text
F1～F8 v1.0
AUDIT-PATCH-001～017
AUDIT-PATCH-002-SUP-01
```

For each source, extract every normative clause, including:

- `must`
- `must not`
- `forbidden`
- explicit `!=`
- explicit `=`
- owner assignments
- authority boundaries
- state requirements
- lifecycle requirements
- applicability rules
- resolution rules
- supersession rules
- handoff qualifiers
- deferred obligations
- current-effective rules
- machine-readable invariants
- mandatory gates
- closure/history requirements

Do not count explanatory examples as normative unless the source makes them binding.

## Phase B — Build one row per normative clause

Use `06_CLAUSE_MATRIX_TEMPLATE.md`.

Each row must contain:

```text
Source ID
Source section
Normative clause
Owner/domain
Expected Candidate landing
Actual Candidate landing
Prose coverage
Machine-readable coverage if required
Supersession status
Coverage result
Finding ID if incomplete
```

Coverage result:

```text
COMPLETE
PARTIAL
MISSING
CONTRADICTED
SUPERSEDED_AS_APPROVED
NOT_APPLICABLE_WITH_REASON
```

## Phase C — Exhaustive discovery before edits

Before modifying Candidate:

1. Complete the matrix for all formal inputs.
2. Continue even after first blocker.
3. Collect all findings.
4. Deduplicate by root cause.
5. Classify each finding:

```text
DETERMINISTIC_REPAIR
HUMAN_DECISION_REQUIRED
NON_BLOCKING_OPTIMIZATION
```

6. Save:

```text
00_CONSOLIDATION_CONTROL/
FINAL_EXHAUSTIVE_DISCOVERY_BEFORE_REPAIR.md
```

This file must not later be rewritten into PASS.

## Phase D — Batch repair

After discovery is complete:

- repair all `DETERMINISTIC_REPAIR` findings in one batch;
- do not guess `HUMAN_DECISION_REQUIRED`;
- do not perform unrelated refactors;
- do not redesign approved architecture;
- do not modify v1.0 or Audit Patch history.

After repairs, rerun the entire matrix from the beginning.

## Phase E — Cross-stage invariants

Independently verify:

### Authority

```text
Intent
Decision
Approval
Development Entry
Authority
Apply Authorization
Runtime Permission
```

remain distinct.

### Canonical truth

One semantic fact must not gain multiple canonical write targets.

### Owner

F5/F6/F7/F8 and future F9/F10/F11/F12 boundaries must not drift.

### State

Same labels across different domains must not collapse.

### Binding / resolution

No latest/order/specificity/confidence accidental winner.

### Handoff

Required qualifiers cannot disappear.

### Deferred

All material deferred obligations remain owned, bounded, future-recoverable, non-authorizing.

### Candidate state

Historical source approval/freeze cannot become current Candidate approval/freeze.

## Phase F — Machine-readable checks

Parse all Candidate YAML.

At minimum verify:

```text
24/24 YAML parse successfully
candidate_metadata current state is unique
historical state stays under source_baseline
no current human_approved=true
no architecture_freeze_granted=true
no freeze_baseline_established=true
all authorization prohibitions preserved
F8 core_invariants parses as an actual list
```

Do not rely only on grep.

## Phase G — Unauthorized new semantics sweep

Search Candidate for new semantics not traceable to v1.0 or approved Audit Patch.

Examples:

```text
new top-level object family
new authority source
new owner promotion
new global registry with governance authority
new mandatory workflow
new physical schema freeze
new runtime permission
new implementation authorization
new current capability inferred from future reservation
```

Every such item needs a formal source or becomes a finding.

## Required end-state for successful batch repair

```text
All normative clauses inventoried
All clause rows COMPLETE / approved supersession / justified N/A
PARTIAL = 0
MISSING = 0
CONTRADICTED = 0
Unauthorized New Semantics = 0
Blocking deterministic finding = 0
Unresolved Human Decision = 0
Cross-file contradiction = 0
Implementation leakage = 0
Candidate freeze leakage = 0
```

This still does not equal Human Approval.

# Formal Inputs and Authority Rules

## Formal consolidation authority

The only formal architecture inputs for F1～F8 v1.1 consolidation are:

```text
F1～F8 v1.0 Original Frozen Baseline
+
AUDIT-PATCH-001 ～ AUDIT-PATCH-017
+
AUDIT-PATCH-002-SUP-01
```

Approved Audit Patches:

```text
榕树ai改造落地相关文档/
Documentation_Packaging/
PreF9_Architecture_Integrity_Review/
10_HUMAN_APPROVED_PATCHES/
```

Also read:

```text
00_AUDIT_GOVERNANCE_AND_PACKAGING_PROTOCOL.md
19_FINAL_CROSS_STAGE_REVIEW_CLOSEOUT.md
20_FINAL_CROSS_STAGE_WORKING_HANDOVER_CHECKPOINT.md
```

## Candidate under review

```text
榕树ai改造落地相关文档/
Documentation_Packaging/
F1-F8_v1.1_Consolidated_Candidate/
```

## Historical review evidence

These are evidence, not architecture authority:

```text
FINAL_CONSOLIDATED_FREEZE_REVIEW.md
FCFR_CORRECTION_PASS_01.md
FINAL_CONSOLIDATED_FREEZE_REVIEW_RERUN_01.md
FCFR_CORRECTION_PASS_02.md
FINAL_CONSOLIDATED_FREEZE_REVIEW_RERUN_02.md
FCFR_CORRECTION_PASS_03.md
DEFERRED_OBLIGATION_RECONCILIATION.md
```

If evidence summary conflicts with a HUMAN_APPROVED Patch, the Patch wins.

## Historical immutability

Must remain unchanged:

```text
F1～F8 v1.0 Original Frozen Baseline
PreF9 approved Audit Patch history
all prior Final Review / Correction history
```

## Core invariants

```text
Assignment != Binding != Resolution != Runtime Execution
Stable ID != Revision != Version != Current Effective
Evidence != Authority
Index != Authority
Trace != Authority
Gate PASS != Authority
Current Effective != Canonical Truth
Later Stage != Higher Authority
State Consumer != State Owner
Projection != Canonical Truth
Automatic Re-resolution != Automatic Reauthorization
Operational Exception != Governed Exception
Technical Recovery != Semantic Rollback
Deferred != Authorized
Deferred Obligation != Backlog Task
Deferred Obligation != Implementation Task
Deferred Handoff != Authority Transfer
Deferred Handoff != Implementation Authorization
Missing Required Qualifier != PASS
```

## Human decision policy

Only mark `HUMAN_DECISION_REQUIRED` when:

```text
multiple legitimate materially different outcomes
+
material consequence
+
existing approved rules cannot determine a unique governed result
```

Do not use Human Decision as a safety fallback for deterministic gaps.

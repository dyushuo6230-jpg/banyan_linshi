# Banyan / 榕树 AI — Pre-F9 下一窗口从这里开始 v8.0

## 1. 当前正式状态

```text
F1～F8 v1.0 = Original Frozen Baseline / UNCHANGED
Phase 0 = COMPLETE

Audit Batch 1 = CLOSED
Audit Batch 2 = CLOSED
Audit Batch 3 = CLOSED
Audit Batch 4 = CLOSED
Audit Batch 5 = CLOSED
Audit Batch 6 = CLOSED

Final Cross-stage Review = CLOSED

Formal Audit Patch Range
= AUDIT-PATCH-001 ～ AUDIT-PATCH-017
```

## 2. 恢复顺序

新窗口依次读取：

1. GitHub F1～F8 v1.0 Freeze Packs；
2. `00_AUDIT_GOVERNANCE_AND_PACKAGING_PROTOCOL.md`；
3. Batch 1～6 Final Closeout；
4. `19_FINAL_CROSS_STAGE_REVIEW_CLOSEOUT.md`；
5. `10_HUMAN_APPROVED_PATCHES/` 全部正式 Patch，当前到 `AUDIT-PATCH-017`；
6. `20_FINAL_CROSS_STAGE_WORKING_HANDOVER_CHECKPOINT.md`；
7. 本文件。

不要重做或重新审批 Batch 1～6 / Final Cross-stage Review。

## 3. Final Cross-stage Review 已完成

```text
AUDIT-PATCH-017 = HUMAN_APPROVED
FCR-CHAIN-01 = ARCHITECTURALLY_RESOLVED
FCR-PATCH-02 = NOT REQUIRED
Final Cross-stage Whole-chain Sweep = PASS
Final Cross-stage Review = CLOSED
```

## 4. 下一阶段

正式进入：

```text
F1～F8 v1.1 Consolidation / No-Loss Reconciliation
```

不是继续增加 Audit Batch。

## 5. Consolidation Input

```text
F1～F8 v1.0 Original Frozen Baseline
+
AUDIT-PATCH-001～017 HUMAN_APPROVED
```

Repository Implementation Reality 可作为 Evidence，但不能自动成为 Consolidation Truth。

## 6. Consolidation Required Work

```text
Patch-to-Baseline Integration Mapping
Per-stage Merge Plan
Supersession / Compatibility Matrix
No-Loss Reconciliation
Duplicate / Contradiction Detection
Cross-stage Invariant Reconciliation
F1～F8 v1.1 Candidate Pack Generation
Final Consolidated Freeze Review
Explicit Human Approval
```

## 7. No Historical Rewrite

```text
F1～F8 v1.0
= immutable historical Original Frozen Baseline
```

不得原地修改 v1.0。

AUDIT-PATCH-001～017 继续独立保留。

## 8. Candidate Boundary

```text
F1～F8 v1.1 Candidate
!= New Freeze Baseline
```

只有 Final Consolidated Freeze Review + Explicit Human Approval 后才成为新 Freeze Baseline。

## 9. Human Decision Boundary

确定性 Mapping / Merge / Dedup / No-Loss Reconciliation 默认自动。

只有：

```text
real semantic conflict
authority conflict
material supersession ambiguity
multiple legitimate incompatible consolidation outcomes
```

才进入 Human Decision。

## 10. 下一步启动方式

先执行四源对账，然后从：

```text
Patch-to-Baseline Integration Mapping
```

开始。

不要直接生成 v1.1 Freeze Pack。

## 11. 固定禁止事项

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

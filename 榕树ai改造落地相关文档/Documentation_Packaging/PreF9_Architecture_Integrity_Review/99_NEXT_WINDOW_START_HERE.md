# Banyan / 榕树 AI — Pre-F9 下一窗口从这里开始 v4.0

## 1. 当前状态

```text
F1～F8 v1.0 = Original Frozen Baseline / UNCHANGED
Phase 0 = COMPLETE
Audit Batch 1 = CLOSED
Audit Batch 2 = CLOSED
Audit Batch 3 = CLOSED
Current Next = Resolve next Audit Batch from formal audit plan / repository evidence
```

禁止提前进入 Implementation / RP2 / Authority Cutover / Canonical Replacement / Final Activation / Legacy Retirement。

---

## 2. 恢复顺序

新窗口继续工作时按顺序读取：

1. GitHub F1～F8 v1.0 Freeze Packs；
2. `00_AUDIT_GOVERNANCE_AND_PACKAGING_PROTOCOL.md`；
3. `08_BATCH01_FINAL_CLOSEOUT.md`；
4. `09_BATCH02_FINAL_CLOSEOUT.md`；
5. `11_BATCH03_FINAL_CLOSEOUT.md`；
6. `10_HUMAN_APPROVED_PATCHES/` 中全部正式 Patch，当前到 `AUDIT-PATCH-011`；
7. `12_BATCH03_WORKING_HANDOVER_CHECKPOINT.md`；
8. 本文件 `99_NEXT_WINDOW_START_HERE.md`。

F1～F8 v1.0 原文件不能被 Audit Patch 直接覆盖；Patch 只作为后续 Consolidation（整合）的输入。

---

## 3. Batch 1 / Batch 2

```text
Audit Batch 1 = CLOSED
Audit Batch 2 = CLOSED
```

正式 Patch：

- AUDIT-PATCH-001 ～ AUDIT-PATCH-005；
- AUDIT-PATCH-002-SUP-01；
- AUDIT-PATCH-006 ～ AUDIT-PATCH-010。

`CON-002 = ARCHITECTURALLY_RESOLVED`（由 AUDIT-PATCH-009 收口）。

不要重做 B1 / B2。

---

## 4. Batch 3

主题：

```text
Product / Design / Change Chain
```

完成：

```text
Four-Source Reconciliation = COMPLETE
Main Chain Map = COMPLETE
Final Completeness Sweep = PASS
```

唯一新增 Finding：

```text
B3-CHAIN-01
Requirement / Product Semantic Anchor
× Design / UI Contract Typed Semantic Linkage
× Impact Applicability
GAP / P1
```

通过：

```text
B3-PATCH-01 HUMAN_APPROVED
```

正式归档为：

```text
AUDIT-PATCH-011_Product_Design_Typed_Semantic_Linkage_and_Impact_Applicability.md
```

结论：

```text
B3-CHAIN-01 = ARCHITECTURALLY_RESOLVED
B3-PATCH-02 = NOT REQUIRED
Audit Batch 3 = CLOSED
```

---

## 5. Batch 3 核心冻结

```text
Requirement Change != Automatic UI Change
UI Change != Automatic Product Change

Product Change Affecting UI → F6 Re-resolution
Design Change Crossing Product Boundary → F5 Resolution

Semantic Link != Authority
Trace Link != Duplicate Product Truth

SQLite != Canonical Truth
SQLite != Authority
Indexed Relation != Confirmed Material Impact

Automatic != Ungoverned
Governed != Manual Every Time
```

Product ↔ Design/UI 第一版核心关系：

```text
REALIZES（承载 / 实现）
REPRESENTS（呈现 / 表达）
INVOKES（触发）
CONSTRAINED_BY（受约束）
ACCEPTANCE_COVERS（覆盖验收意图）
```

---

## 6. Batch 3 Final Sweep

```text
Blocking Architecture Gap = 0
Blocking Conflict = 0
Competing Product Truth = 0
Competing UI / Design Truth = 0
Cross-stage Owner Leakage = 0
Canonical Apply Bypass Path = 0
Current Effective Silent Replacement Path = 0
Historical Trace Loss Path = 0
Index / SQLite Authority Promotion Path = 0
```

---

## 7. Explicit Deferred

以下不是 Batch 3 未完成项：

- SQLite DDL / Relation Physical Schema；
- Graph Physical Schema；
- F9 Relation / Freshness / Impact physical index design；
- F10 runtime authorization implementation；
- F11 governance UX；
- migration tooling；
- autonomous AI learning。

---

## 8. 下一步固定指令

不要自动发明 `Audit Batch 4` 的主题或 Finding ID。

先从仓库中的正式 Audit Plan / Review Scope / Handover 证据中解析下一 Batch；如果正式资料没有定义下一 Batch，则先做审计计划续接，而不是凭空编号。

确定下一 Batch 后继续固定流程：

```text
四源对账
→ 系统说明（白话 + 例子）
→ KEEP / GAP / DEFECT / OPTIMIZATION
→ 修正设计
→ 完整审批稿
→ 用户明确 <PATCH-ID> HUMAN_APPROVED
→ 正式独立 Markdown
→ Batch Closeout
```

不得把“好的 / 下一步 / 继续 / 按建议”自动解释成 HUMAN_APPROVED。

---

## 9. 固定禁止事项

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

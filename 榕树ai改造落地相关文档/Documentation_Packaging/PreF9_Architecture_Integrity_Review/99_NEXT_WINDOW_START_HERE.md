# Banyan / 榕树 AI — Pre-F9 下一窗口从这里开始 v5.0

## 1. 当前状态

```text
F1～F8 v1.0 = Original Frozen Baseline / UNCHANGED
Phase 0 = COMPLETE
Audit Batch 1 = CLOSED
Audit Batch 2 = CLOSED
Audit Batch 3 = CLOSED
Audit Batch 4 = CLOSED
Current Formal Patch Range = AUDIT-PATCH-001 ～ AUDIT-PATCH-013
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
6. `13_BATCH04_FINAL_CLOSEOUT.md`；
7. `10_HUMAN_APPROVED_PATCHES/` 中全部正式 Patch，当前到 `AUDIT-PATCH-013`；
8. `14_BATCH04_WORKING_HANDOVER_CHECKPOINT.md`；
9. 本文件 `99_NEXT_WINDOW_START_HERE.md`。

F1～F8 v1.0 原文件不能被 Audit Patch 直接覆盖；Patch 只作为后续 Consolidation 输入。

---

## 3. 已关闭批次

```text
Audit Batch 1 = CLOSED
Audit Batch 2 = CLOSED
Audit Batch 3 = CLOSED
Audit Batch 4 = CLOSED
```

不要重做或重新审批 B1～B4 已批准 Patch。

---

## 4. Batch 3

```text
AUDIT-PATCH-011 = HUMAN_APPROVED
B3-CHAIN-01 = ARCHITECTURALLY_RESOLVED
B3-PATCH-02 = NOT REQUIRED
```

---

## 5. Batch 4

### B4-CHAIN-01

```text
Project Binding Resolution Target
× Multi-Binding Composition / Conflict
× Current Effective Determinism

B4-PATCH-01 HUMAN_APPROVED
→ AUDIT-PATCH-012 HUMAN_APPROVED
→ ARCHITECTURALLY_RESOLVED
```

### B4-CHAIN-02

```text
Cross-Target Resolution Dependency
× Cycle Detection
× Deterministic Convergence
× Informed Decision Escalation Boundary

B4-PATCH-02 HUMAN_APPROVED
→ AUDIT-PATCH-013 HUMAN_APPROVED
→ ARCHITECTURALLY_RESOLVED
```

Final：

```text
Final Completeness Sweep = PASS
Additional Blocking Gap = 0
B4-PATCH-03 = NOT REQUIRED
Audit Batch 4 = CLOSED
```

---

## 6. Batch 4 核心冻结

```text
Multiple Applicable Bindings != Binding Conflict
One Current Effective Result != One Constituent Binding
Scope Match != Precedence
Project Local != Automatic Override
Runtime Fallback != Durable Rebinding

Workflow Loop != Resolution Dependency Cycle
Reference != Resolution Dependency
Dependency Order != Governance Precedence
Evaluation Order != Semantic Priority
Implicit Cyclic Resolution = FORBIDDEN
Local Resolution Cycle != Global Project Invalidation
Unbounded Resolution Oscillation = FORBIDDEN
Cached Result != Automatic Cycle Breaker
STALE Result cannot silently satisfy Current Dependency

Cycle Detected != Human Decision Required
UNRESOLVED != Human Decision Required
UNKNOWN != Human Decision Required
Missing Evidence != Human Decision Required
Deterministically Resolvable → must not escalate to human
Valid Informed Decision != Automatic Dependency Mutation
```

---

## 7. Owner Boundary

```text
Project Binding / Effective Project Resolution → F8
Durable Protected Mutation / Revision / Canonical Apply → F7
Index / Dependency Lookup / Freshness / Impact → F9
Runtime Permission / Execution → F10
Informed Decision Protocol → existing AUDIT-PATCH-005 governance
```

F8 不建立 Universal Resolver / Global Dependency Authority。

---

## 8. Explicit Deferred

以下不是 Batch 4 未完成项：

- Binding / Dependency physical schema；
- SQLite DDL；
- Graph DB；
- exact relation enum；
- cycle / SCC / topological-sort implementation；
- retry count；
- Fixed-Point Solver；
- runtime exact enum；
- F9 physical index；
- F10 implementation；
- F11 UX；
- migration tooling；
- autonomous AI learning。

---

## 9. 下一步固定规则

下一 Audit Batch 的主题必须从正式 Audit Plan / Review Scope / Repository Evidence 中解析。

如果正式资料没有定义下一 Batch，则先做审计计划续接，不凭空发明主题。

确定下一 Batch 后继续：

```text
四源对账
→ 系统说明（白话 + 例子）
→ KEEP / GAP / DEFECT / OPTIMIZATION
→ 完整修正设计
→ 完整审批稿
→ exact <PATCH-ID> HUMAN_APPROVED
→ 正式独立 Markdown
→ Final Completeness Sweep
→ Batch Closeout
```

普通“好的 / 下一步 / 继续 / 按建议”不得自动解释成 HUMAN_APPROVED。

---

## 10. 固定禁止事项

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

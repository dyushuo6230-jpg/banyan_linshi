# Banyan / 榕树 AI — F1～F8 v1.1 One-Pass Finalization Work Pack

## 目标

当前不再采用“发现一个问题 → 修一个问题 → 再审一次”的循环，而改成：

```text
一次性穷尽发现全部剩余问题
→ 一次性批量修复全部确定性问题
→ 独立再做一次最终审查
→ 若 PASS_PENDING_HUMAN_APPROVAL，再做最终 Human Approval
```

当前分支必须保持：

```text
f1-f8-v1.1-consolidation
```

不要 merge `main`。

## 解压后放哪里

把整个目录：

```text
Banyan_F1-F8_v1.1_OnePass_Finalization_Pack_2026-09-27/
```

放到仓库根目录，例如：

```text
banyan_linshi/
├── Banyan_F1-F8_v1.1_OnePass_Finalization_Pack_2026-09-27/
├── 榕树ai改造落地相关文档/
└── ...
```

可以把这个工作包一起提交到当前工作分支。

## 执行顺序

### 第 1 步：一次性发现 + 一次性批量修复

在 Cursor 中打开：

```text
04_CURSOR_ONE_PASS_BATCH_REPAIR_PROMPT.md
```

把全文交给 Cursor Agent / Composer。

要求 Cursor：

1. 完整读取正式输入；
2. 对 F1～F8 v1.0 + 18 个 Approved Audit Inputs 做 Clause-Level Exhaustive Sweep；
3. 不能发现第一个问题就停；
4. 必须把全部 Finding 一次性找全；
5. 冻结 Discovery Snapshot；
6. 一次性修复所有 deterministic findings；
7. 真正无法由正式合同确定的才标记 Human Decision Required；
8. 修复后全量回归；
9. commit + push 当前分支；
10. 不执行最终 Rerun 03。

### 第 2 步：独立最终审查

第 1 步完成并 push 后，再执行：

```text
05_CURSOR_FINAL_REVIEW_PROMPT.md
```

这一步：

```text
Review != Repair
```

不允许修 Candidate。

理想结果：

```text
FINAL_CONSOLIDATED_FREEZE_REVIEW_RERUN_03
= PASS_PENDING_HUMAN_APPROVAL

READY_FOR_HUMAN_FINAL_APPROVAL
= YES
```

即使 PASS，也必须继续保持：

```text
human_approved = false
architecture_freeze_granted = false
freeze_baseline_established = false
```

等待最终人工批准。

## 建议先读

```text
01_CURRENT_STATE_SNAPSHOT.md
02_FORMAL_INPUTS_AND_AUTHORITY.md
03_EXHAUSTIVE_SWEEP_PROTOCOL.md
06_CLAUSE_MATRIX_TEMPLATE.md
07_ACCEPTANCE_AND_EXPECTED_OUTPUTS.md
```

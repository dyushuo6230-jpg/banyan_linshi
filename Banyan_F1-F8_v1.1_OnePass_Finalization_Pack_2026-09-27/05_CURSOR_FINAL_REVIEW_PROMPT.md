# Cursor Prompt — Independent Final Consolidated Freeze Review Rerun 03

> 只有在 `04_CURSOR_ONE_PASS_BATCH_REPAIR_PROMPT.md` 完成、commit + push 后执行本文件。

这是 Banyan / 榕树 AI：

```text
F1～F8 v1.1
FINAL CONSOLIDATED FREEZE REVIEW — RERUN 03
```

本次：

```text
Review != Repair
```

禁止修改 Candidate 语义。

## 1. 前置条件

必须确认上一阶段已生成：

```text
00_CONSOLIDATION_CONTROL/
FINAL_EXHAUSTIVE_DISCOVERY_BEFORE_REPAIR.md

00_CONSOLIDATION_CONTROL/
FINAL_NORMATIVE_CLAUSE_COVERAGE_MATRIX.md

00_CONSOLIDATION_CONTROL/
FCFR_EXHAUSTIVE_BATCH_CORRECTION.md
```

并且上一阶段已经 commit + push。

## 2. 独立性要求

不要相信：

```text
Batch Correction Report says PASS
Matrix says COMPLETE
```

作为最终结论。

必须独立重新读取：

```text
F1～F8 v1.0
AUDIT-PATCH-001～017
AUDIT-PATCH-002-SUP-01
current Candidate
```

然后自己重建验证结果。

## 3. 不允许 Repair

发现任何问题：

```text
记录 Finding
→ Final Result = BLOCKED
```

不要修。

Finding ID：

```text
FCFR-R3-001
FCFR-R3-002
...
```

## 4. Historical Integrity

验证：

```text
F1～F8 v1.0 modified = 0
PreF9 approved patch modified = 0
historical review/correction modified = 0
```

## 5. Clause-Level Exhaustive Revalidation

重新枚举 formal normative clauses。

不得只复用上一阶段矩阵。

对每条验证：

```text
formal source
→ candidate landing
→ semantics
→ machine landing when required
```

最终输出：

```text
Total Normative Clause Count
COMPLETE
PARTIAL
MISSING
CONTRADICTED
Approved Superseded
N/A with reason
```

要求：

```text
PARTIAL = 0
MISSING = 0
CONTRADICTED = 0
```

## 6. 18 Approved Inputs

必须：

```text
Approved Patch Mapping = 18/18
Approved Semantic Coverage = COMPLETE 18/18
Incomplete Patch Integration = 0
Silent Semantic Drop = 0
```

## 7. Baseline No-Loss

确认所有未被正式 supersede 的 v1.0 contracts 都存在。

## 8. Supersession

确认 supersession 只发生在已批准范围。

## 9. Authority

确认：

```text
Authority Drift = 0
Authority Promotion Path = 0
```

## 10. Canonical Truth

确认：

```text
Competing Canonical Truth = 0
```

## 11. Owner

确认：

```text
Owner Drift = 0
Competing Owner = 0
```

## 12. State

确认：

```text
State-domain Collapse = 0
```

## 13. Current Effective

确认：

```text
Current-effective Ambiguity = 0
```

## 14. Binding

确认：

```text
Binding Winner Ambiguity = 0
```

## 15. Handoff

确认：

```text
Cross-stage Handoff Qualifier Loss = 0
```

## 16. Deferred

重新完整验证 Patch 016。

确认：

```text
Patch 016 Full Semantic Coverage = COMPLETE
Material Deferred = 14
Blocking Deferred Architecture Gap = 0
Deferred Backlog Collapse Path = 0
Deferred Implementation Task Collapse Path = 0
```

如 Material Deferred 数量变化，必须解释正式依据。

## 17. Machine-readable

真实 parse 全部 24 Candidate YAML。

确认：

```text
YAML Parse Failure = 0
Current/Historical State Competition = 0
```

F8：

```text
core_invariants
```

必须是真实 sequence。

记录 parsed count。

## 18. Candidate State

必须仍：

```text
AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW
human_approved = false
architecture_freeze_granted = false
freeze_baseline_established = false
```

## 19. Authorization

必须仍：

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

## 20. Unauthorized New Semantics

独立检查：

```text
Unauthorized New Semantic Count = 0
```

## 21. Cross-file Contradiction

要求：

```text
Cross-file Contradiction Count = 0
```

## 22. Correction Regression

重新验证历史所有修复：

```text
FCFR-001～005
FCFR-R1-001
FCFR-R2-001～005
Exhaustive Batch Correction findings
```

要求：

```text
Correction Regression Count = 0
```

## 23. 结果分类

仅允许：

### A. PASS_PENDING_HUMAN_APPROVAL

只有全部满足：

```text
All review domains PASS
Approved Semantic Coverage = 18/18 COMPLETE
Clause PARTIAL = 0
Clause MISSING = 0
Clause CONTRADICTED = 0
Silent Semantic Drop = 0
Unauthorized New Semantic = 0
Cross-file Contradiction = 0
Correction Regression = 0
Blocking Finding = 0
Human Decision Required = 0
Implementation Leakage = 0
Candidate Freeze Leakage = 0
```

此时：

```text
FINAL_CONSOLIDATED_FREEZE_REVIEW_RERUN_03
= PASS_PENDING_HUMAN_APPROVAL

READY_FOR_HUMAN_FINAL_APPROVAL
= YES
```

但：

```text
HUMAN_APPROVED = NO
NEW FREEZE BASELINE = NOT_ESTABLISHED
```

### B. BLOCKED

任何 blocker。

### C. HUMAN_DECISION_REQUIRED

只有现有规则无法唯一决定的多个合法 material outcomes。

## 24. 新增 Review 文件

新增：

```text
00_CONSOLIDATION_CONTROL/
FINAL_CONSOLIDATED_FREEZE_REVIEW_RERUN_03.md
```

不要覆盖任何旧 Review。

## 25. Existing Candidate = 0 修改

本次必须：

```text
Existing Candidate semantic files modified = 0
```

如果你认为需要修改 Candidate：

不要改。

记录 Finding。

## 26. Git

执行：

```text
git status
git diff --stat
git diff
```

理想新增只有：

```text
FINAL_CONSOLIDATED_FREEZE_REVIEW_RERUN_03.md
```

## 27. Commit / Push

PASS 建议 commit：

```text
docs(consolidation): add final freeze review rerun 03
```

BLOCKED 建议：

```text
docs(consolidation): record final freeze review rerun 03
```

push：

```text
origin/f1-f8-v1.1-consolidation
```

不要 merge main。

## 28. 最后报告

只报告：

1. Final Review Rerun 03 Result
2. Total Normative Clause Count
3. Clause COMPLETE / PARTIAL / MISSING / CONTRADICTED
4. 20 Review Domains PASS / FAIL
5. Blocking Finding Count
6. New Finding IDs
7. Human Decision Required Count
8. Approved Patch Mapping
9. Approved Semantic Coverage
10. Silent Semantic Drop
11. Baseline No-Loss
12. Unauthorized Supersession
13. Authority Drift
14. Owner Drift
15. Competing Canonical Truth
16. State-domain Collapse
17. Current-effective Ambiguity
18. Binding Winner Ambiguity
19. Cross-stage Handoff Qualifier Loss
20. Patch 016 Full Semantic Coverage
21. Material Deferred Count
22. Blocking Deferred Architecture Gap
23. Unauthorized New Semantic Count
24. Cross-file Contradiction Count
25. Correction Regression Count
26. 24 YAML parse result
27. F8 core_invariants parsed count
28. Implementation Leakage
29. Candidate Freeze Leakage
30. Existing Candidate modified count
31. v1.0 modified
32. PreF9 modified
33. historical review/correction modified
34. Candidate lifecycle
35. READY_FOR_HUMAN_FINAL_APPROVAL
36. New Review File
37. commit SHA
38. 是否 push

不要 Human Approve。
不要建立 v1.1 Freeze Baseline。
不要 merge main。
不要进入 F9。

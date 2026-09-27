# Cursor Prompt — One-Pass Exhaustive Discovery + Batch Repair

把本文件全文作为一个完整任务交给 Cursor。

这是 Banyan / 榕树 AI：

```text
F1～F8 v1.1
Exhaustive Clause-Level Discovery
+
One-Pass Batch Correction
```

当前分支必须是：

```text
f1-f8-v1.1-consolidation
```

当前已知 head：

```text
a3e426a9840e94e7c25c048afd97594b76e1d0f5
```

如果本地 branch/head 与远端当前状态不一致，先同步并说明，不要在错误分支施工。

## 0. 本次任务目标

不要继续：

```text
发现 1 个问题
→ 修
→ 再审
→ 再发现 1 个
```

本次必须：

```text
先完整穷尽所有 Formal Normative Clauses
→ 一次性找到所有剩余问题
→ 冻结 Discovery Snapshot
→ 一次性修复全部 deterministic findings
→ 全量重新验证
→ commit + push
→ 停止
```

本次不执行最终 Review Rerun 03。

## 1. 读取工作包

先读取：

```text
00_START_HERE.md
01_CURRENT_STATE_SNAPSHOT.md
02_FORMAL_INPUTS_AND_AUTHORITY.md
03_EXHAUSTIVE_SWEEP_PROTOCOL.md
06_CLAUSE_MATRIX_TEMPLATE.md
07_ACCEPTANCE_AND_EXPECTED_OUTPUTS.md
```

这些文件是执行说明，不是 Architecture Authority。

## 2. 正式 Authority

正式输入只能来自：

```text
F1～F8 v1.0 Original Frozen Baseline
+
AUDIT-PATCH-001～017 HUMAN_APPROVED
+
AUDIT-PATCH-002-SUP-01 HUMAN_APPROVED
```

必须实际读取仓库正式文件。

不要用聊天摘要替代。

Review / Correction 文件只作为 evidence。

如果 evidence 摘要与正式 HUMAN_APPROVED Patch 有差异：

```text
正式 Patch 为准
```

## 3. 严格禁止

不得：

- 修改 F1～F8 v1.0；
- 修改 PreF9 HUMAN_APPROVED Patch；
- 修改任何历史 Final Review / Correction verdict；
- merge main；
- Human Approve；
- 设置 architecture_freeze_granted=true；
- 设置 freeze_baseline_established=true；
- 创建正式 v1.1 Freeze Baseline；
- 进入 F9 implementation；
- 进入 Implementation；
- RP2；
- Authority Cutover；
- Canonical Replacement；
- Final Activation；
- Legacy Retirement；
- 冻结 SQLite Physical Schema；
- 为了“补齐”而新增未经批准的架构系统。

## 4. Phase A：完整 Normative Clause Inventory

必须完整读取：

F1～F8 v1.0 六文件 Pack

以及：

```text
AUDIT-PATCH-001
AUDIT-PATCH-002
AUDIT-PATCH-002-SUP-01
AUDIT-PATCH-003
AUDIT-PATCH-004
AUDIT-PATCH-005
AUDIT-PATCH-006
AUDIT-PATCH-007
AUDIT-PATCH-008
AUDIT-PATCH-009
AUDIT-PATCH-010
AUDIT-PATCH-011
AUDIT-PATCH-012
AUDIT-PATCH-013
AUDIT-PATCH-014
AUDIT-PATCH-015
AUDIT-PATCH-016
AUDIT-PATCH-017
```

从正式源中枚举所有 normative clauses。

不要只按 Patch 标题做一行。

必须达到：

```text
one normative clause / invariant / mandatory boundary
→ one matrix row
```

包括：

- MUST
- MUST NOT
- FORBIDDEN
- formal equality / inequality
- Owner
- Authority
- Canonical Truth
- Current Effective
- State
- Binding / Resolution
- Applicability
- Freshness
- Gate
- Handoff
- Deferred
- Supersession
- Closure
- History
- Machine-readable requirements

## 5. 生成 Clause Coverage Matrix

新增：

```text
F1-F8_v1.1_Consolidated_Candidate/
00_CONSOLIDATION_CONTROL/
FINAL_NORMATIVE_CLAUSE_COVERAGE_MATRIX.md
```

按照：

```text
06_CLAUSE_MATRIX_TEMPLATE.md
```

每一条正式 normative clause 都必须记录：

```text
Clause ID
Formal Source
Section
Normative Contract
Owner / Domain
Expected Candidate Landing
Actual Candidate Landing
Prose Coverage
Machine Coverage
Supersession / Compatibility
Result
Finding ID
```

Result 只能：

```text
COMPLETE
PARTIAL
MISSING
CONTRADICTED
SUPERSEDED_AS_APPROVED
NOT_APPLICABLE_WITH_REASON
```

## 6. 不允许见第一个问题就停

这是本次最重要的规则之一。

发现：

```text
PARTIAL
MISSING
CONTRADICTED
```

时：

记录 Finding，

但继续扫描剩余所有正式输入。

必须把：

```text
001～017
+
002-SUP-01
+
v1.0 non-superseded contracts
```

全部扫描完。

只有全部扫描完成，才允许进入 Repair。

## 7. Discovery Snapshot

在任何 Candidate Repair 发生之前，新增：

```text
00_CONSOLIDATION_CONTROL/
FINAL_EXHAUSTIVE_DISCOVERY_BEFORE_REPAIR.md
```

必须记录：

```text
Total Normative Clauses
COMPLETE Count
PARTIAL Count
MISSING Count
CONTRADICTED Count
Approved Supersession Count
N/A Count
Deterministic Repair Finding Count
Human Decision Required Count
Cross-file Contradiction Count
Unauthorized New Semantic Count
```

列出：

```text
EXH-FINDING-001
EXH-FINDING-002
...
```

不要只列 blocker；所有 materially relevant incomplete clauses 都要列完。

该文件写入后，不得在 Repair 后改成“发现 0 问题”。它是 before-repair evidence。

## 8. Finding 分类

每个 Finding 分类：

### A. DETERMINISTIC_REPAIR

正式批准合同已经唯一决定正确结果。

### B. HUMAN_DECISION_REQUIRED

只有满足：

```text
multiple legitimate materially different outcomes
+
material consequence
+
existing approved contracts cannot uniquely resolve
```

才可使用。

### C. NON_BLOCKING_OPTIMIZATION

不影响合同完整性。

不要把 deterministic gap 升级成人工决策。

## 9. Human Decision 的处理

如果存在 Human Decision Required：

- 继续完成所有其他 Clause 扫描；
- 继续修复所有与该决策独立的 deterministic findings；
- 不猜该 Human Decision；
- 在最终结果中单独列出；
- Candidate 不能进入 Ready for Final Review PASS。

## 10. Phase B：一次性 Batch Repair

Discovery 全部完成后：

一次性修复所有：

```text
DETERMINISTIC_REPAIR
```

禁止：

```text
修一个
→ 停止
→ 再让用户跑一次
```

本次目标是一个 Batch Correction。

## 11. Repair Authority

每一项 Repair 必须能追溯到：

```text
v1.0 retained contract
or
HUMAN_APPROVED Audit Patch
```

如果无法找到正式 Source：

不得修成新的架构语义。

## 12. Repair 范围原则

只修改：

```text
F1-F8_v1.1_Consolidated_Candidate/
```

内必要的：

```text
01_RECONCILIATION.md
02_TARGET_DESIGN.md
03_HUMAN_DECISIONS.yaml
04_FROZEN_CONTRACT.yaml
05_IMPLEMENTATION_BOUNDARY.md
06_ACCEPTANCE_GATES.yaml
00_CONSOLIDATION_CONTROL/*
```

不要为了统一格式机械改动无关文件。

## 13. Machine-readable 一致性

如果正式语义要求机器可恢复：

同步补齐 YAML。

不能出现：

```text
Prose says X
YAML silently says Y
```

修复后真实 parse 全部 24 份 Candidate YAML。

## 14. Candidate / Historical State

所有 Candidate YAML 必须仍：

```yaml
candidate_metadata:
  lifecycle_state: AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW
  human_approved: false
  architecture_freeze_granted: false
  freeze_baseline_established: false
```

历史 v1.0 HUMAN_APPROVED / Freeze PASS 只能存在于：

```text
source_baseline
```

不能成为 current Candidate state。

## 15. Global Authorization 必须保持

仍然：

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

## 16. Authority 全链检查

必须保持：

```text
User Intent
!= Human Decision
!= Approval Evidence
!= Development Readiness
!= Development Entry Authorization
!= Authority
!= Apply Authorization
!= Runtime Permission
```

以及：

```text
Role != Authority
Assignment != Authority
Binding != Authority
Resolution Result != Authority
Evidence != Authority
Index != Authority
Trace != Authority
Gate PASS != Authority
Runtime ALLOW != Semantic Authority
Later Stage != Higher Authority
```

## 17. Canonical Truth 检查

保持：

```text
One Semantic Fact
→ One Canonical Write Target
```

并：

```text
Projection != Canonical Truth
Index != Canonical Truth
Cache != Canonical Truth
Trace != Canonical Truth
Runtime Observation != Canonical Truth
Current Effective != Canonical Truth
```

## 18. Owner 检查

保持：

```text
F5 = Product Meaning / Governance
F6 = Design / UI Semantics
F7 = Governed Change / Canonical Apply
F8 = Project Instance / Binding / Resolution
F9 = future Index / Search / Freshness / Impact Evidence
F10 = future Runtime Permission / Execution
F11 = future UX / Control Plane
F12 = future Migration / Retirement
```

Consumer != Owner。

## 19. Patch 003 全扫

完整核对：

```text
Stable ID
Revision
Version
Version Scheme
Published Exact Version
Version Constraint
Current Effective
qualified Latest
```

确保无 forced SemVer、无 silent rebinding、无 Current Effective 混淆。

## 20. Patch 004 全扫

完整核对：

```text
Rule Entry
Rule Module
PolicyDefinition
Rule System
Engineering Standard
Engineering Standard Pack
Configuration Profile
```

确保：

```text
One Rule Entry
→ Exactly One Canonical Primary Module / write target
```

引用不得变成 ownership。

## 21. Patch 005 全扫

完整核对：

```text
Explicit ASK Intent
Explicit AUTO Intent
Task > Project > User preference
Preference != Authority Priority
Multiple Valid Materially Distinct + ASK
```

AUTO 不得绕过 governance。

## 22. Patch 016 全扫

即使 Correction Pass 03 已标 COMPLETE，也必须从正式 Patch 原文重新验证。

至少覆盖：

```text
Deferred identity
Architecture Hole Test
Task separation
Minimum Logical Contract
No Global Deferred Authority
Categories
Future Owner Resolution
Declaring/Future Owner boundary
Future Owner != Current Authorization
Trigger quality
Trigger != Authorization
Preconditions
Must-Happen-Before
Deferred Guard
Expected Resolution Output
Human Decision Boundary
Future Capability Reserved
State semantics
Deadline transition
Closure
Supersession
History
Deferred Handoff
F9/F11/F12 limits
Implementation-owned Deferred
Premature Activation
Owner conflict
Dependencies
Consolidation Reconciliation
Banyan-wide invariants
```

并重新核：

```text
14 Material Deferred
0 Blocking Architecture Gap
```

## 23. Patch 017 全扫

完整核对：

```text
Purpose
Source Owner
Target Consumer
Subject / Target
Scope
Context
Typed Payload
Authority Basis
Resolution Basis
Revision / Version Basis
Freshness
State / Gate qualifiers
UNKNOWN
BLOCKED
HOLD
Provenance
Deferred Guard
Invalidation / Re-resolution
Point-of-use revalidation
```

保持：

```text
Missing Required Qualifier != PASS
Handoff Accepted != Basis Valid Forever
Later Consumer != Higher Authority
Mismatch != Mutation Authority
```

## 24. Cross-file Contradiction Sweep

横向检查：

```text
duplicate incompatible definition
competing owner
competing authority
competing canonical truth
competing current-effective rule
competing binding winner rule
state-domain collapse
deferred owner conflict
handoff qualifier mismatch
future-stage authority promotion
```

所有 Finding 必须进入同一 Batch。

## 25. Unauthorized New Semantics Sweep

检查 Candidate 是否出现无法追溯到正式 Source 的：

```text
new object family
new F3 primary type
new authority source
new mandatory stage/workflow
new global registry authority
new current capability
new implementation permission
new physical schema freeze
new runtime permission
new cutover permission
```

如果有，记录 Finding 并处理。

## 26. Batch Correction Report

新增：

```text
00_CONSOLIDATION_CONTROL/
FCFR_EXHAUSTIVE_BATCH_CORRECTION.md
```

记录：

```text
Source Discovery Snapshot
Total Findings
Deterministic Findings
Human Decision Findings
Non-blocking Optimization
Files Changed
Per Finding Source Contract
Per Finding Exact Repair
Per Finding Verification
Remaining Deterministic Finding Count
Remaining Human Decision Count
```

## 27. 更新 Matrix

Repair 完成后，重新从头跑完整 Clause Matrix。

`FINAL_NORMATIVE_CLAUSE_COVERAGE_MATRIX.md` 应反映 repair 后结果。

不要只更新改过的 rows。

## 28. Repair 后必须达到

如果没有 Human Decision：

```text
PARTIAL = 0
MISSING = 0
CONTRADICTED = 0
Unauthorized New Semantics = 0
Deterministic Blocking Finding = 0
Human Decision Required = 0
Cross-file Contradiction = 0
Implementation Leakage = 0
Candidate Freeze Leakage = 0
```

如果不能达到，如实报告。

## 29. Control Documents

按事实需要更新：

```text
PATCH_TO_BASELINE_INTEGRATION_MAP.md
SUPERSESSION_COMPATIBILITY_MATRIX.md
NO_LOSS_RECONCILIATION_REPORT.md
CROSS_STAGE_INVARIANT_RECONCILIATION.md
CONSOLIDATION_MANIFEST.md
```

不要无意义全改。

## 30. 不得修改历史 Review

必须保持 0 修改：

```text
FINAL_CONSOLIDATED_FREEZE_REVIEW.md
FCFR_CORRECTION_PASS_01.md
FINAL_CONSOLIDATED_FREEZE_REVIEW_RERUN_01.md
FCFR_CORRECTION_PASS_02.md
FINAL_CONSOLIDATED_FREEZE_REVIEW_RERUN_02.md
FCFR_CORRECTION_PASS_03.md
```

`DEFERRED_OBLIGATION_RECONCILIATION.md` 只有发现正式事实需要修正时才允许更新，并必须记录原因。

## 31. Git 检查

执行：

```text
git status
git diff --stat
git diff
```

确认：

```text
v1.0 modified = 0
PreF9 modified = 0
historical review modified = 0
code modified = 0
F9 Pack created = 0
main merge = 0
```

## 32. Commit / Push

完成后建议 commit：

```text
fix(consolidation): exhaustively reconcile remaining v1.1 candidate gaps
```

push：

```text
origin/f1-f8-v1.1-consolidation
```

不要 merge main。

## 33. 本次结束点

本次完成后停止。

不要创建：

```text
FINAL_CONSOLIDATED_FREEZE_REVIEW_RERUN_03.md
```

因为下一步必须是独立 Review。

## 34. 最后向我报告

只报告：

1. Total Normative Clause Count
2. Pre-repair COMPLETE / PARTIAL / MISSING / CONTRADICTED
3. Total Findings
4. Deterministic Repair Findings
5. Human Decision Required Findings
6. Unauthorized New Semantic Findings
7. Cross-file Contradiction Findings
8. 全部 deterministic finding 是否一次性修完
9. Post-repair PARTIAL / MISSING / CONTRADICTED
10. Approved Patch Mapping
11. Approved Semantic Coverage
12. Baseline No-Loss
13. Patch 016 Full Semantic Coverage
14. 14 Material Deferred reconciliation 是否仍有效
15. F8 core_invariants parsed count
16. 24 Candidate YAML parse 是否全部成功
17. Authority Drift
18. Owner Drift
19. Implementation Leakage
20. Candidate Freeze Leakage
21. v1.0 modified
22. PreF9 modified
23. historical review/correction modified
24. Modified Candidate Files
25. Modified Control Files
26. Discovery Snapshot File
27. Clause Matrix File
28. Batch Correction Report File
29. Candidate lifecycle
30. commit SHA
31. 是否 push

不要执行 Final Review。

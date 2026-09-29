# F10-D07 — Cross-Action Orchestration × Dependency × Parallel Execution Boundary

**阶段：** F10 — Runtime Permission / Execution Governance Architecture  
**主题：** Cross-Action Orchestration（跨动作执行协调）× Dependency（依赖）× Parallel Execution（并行执行）边界  
**状态：** `HUMAN_APPROVED`

**上游依赖：**
- `F10-G01 HUMAN_APPROVED`
- `F10-D01 HUMAN_APPROVED`
- `F10-D02 HUMAN_APPROVED`
- `F10-D03 HUMAN_APPROVED`
- `F10-D04 HUMAN_APPROVED`
- `F10-D05 HUMAN_APPROVED`
- `F10-D06 HUMAN_APPROVED`

**Implementation Authorization：** `NO`

---

## 1. 决策目的

F10-D07 解决：

> 当一个 Task 内存在多个 Action 时，F10 如何依据既有 Workflow、Dependency、Atomicity、Scope、Runtime Permission 和当前运行状态，决定哪些 Action 现在可执行、哪些可以并行、哪些必须等待，以及局部 Failure / Pause / Cancel 应影响到哪里。

核心目标：

```text
Governed Workflow / Dependency
+
Current Runtime State
+
Per-Action Execution Preconditions
↓
Resolve Ready Actions
↓
Minimum Necessary Serialization
+
Safe Parallel Execution
↓
Localized Failure / Block Propagation
↓
Continue until applicable Workflow condition satisfied
```

---

## 2. Workflow Orchestration != Runtime Scheduling

```text
Workflow Orchestration != Runtime Scheduling
```

F4 Workflow 决定 what actions / nodes exist、semantic order、branch、merge、loop、retry、skip、replace、join、escalation。

F10-D07 只负责在当前 Runtime State 下执行这些已受治理的 Workflow 语义。

---

## 3. F4 继续拥有 Workflow Graph 语义

F4 继续负责：

```text
Workflow Definition
Workflow Graph
Node Dependency
Branch / Merge
Loop
Retry
Pause / Resume
Skip / Replace
Partial Blocking
Checkpoint
Reconcile
Escalation
```

F10 不创建第二套 Workflow Definition Authority。

---

## 4. Runtime Scheduler != Workflow Authority

```text
Runtime Scheduler != Workflow Authority
```

F10不能因为 parallel is faster 就改变 F4 已定义的语义依赖。

---

## 5. Workflow Order != Authority Priority

```text
Workflow Order != Authority Priority
Execution Order != Authority Priority
```

先执行的 Action 不自动拥有更高 Authority。

---

## 6. Dependency 不是单一 Owner

D07 正式区分：

```text
Workflow Dependency
Project Resolution Dependency
Dependency / Impact Discovery
Runtime Scheduling Dependency State
```

这些不是一个对象。

---

## 7. F4 Workflow Dependency

回答：Workflow 语义上哪个 Node / Action 依赖哪个 Node / Action。

---

## 8. F8 / Domain Resolution Dependency

Project Resolution Dependency 回答：为解析某个 Current Effective Project Result，哪些 Hard Resolution Dependency 必须先成立。

该语义继续由已有 F8 / Domain Resolution Contract 管理。F10不得修改。

---

## 9. F9 Dependency / Impact Boundary

F9继续负责：

```text
Dependency Index
Reverse Dependency
Candidate Retrieval
Dependency Discovery Evidence
Potential Impact
Freshness
Provenance
```

```text
F9 Index Edge != Canonical Dependency
F9 Impact Discovery != Scope Expansion Authorization
```

---

## 10. F10 Dependency Consumption Boundary

F10只消费当前 Action 需要的：

```text
Resolved Workflow Dependency
Applicable Project / Domain Dependency Result
F9 Dependency / Impact Evidence
```

用于当前运行调度。

```text
Runtime Dependency Evidence != Dependency Mutation Authority
```

---

## 11. F10 不得修改 Dependency Graph

如果运行中发现 new dependency evidence / unexpected cross-target relation / possible dependency conflict，F10只能：

```text
Pause affected execution
→ Capture evidence
→ Route F9 / F8 / applicable Domain Owner
→ Re-resolution
```

不得 silently add / delete / reverse dependency edge。

---

## 12. AI Guess != Dependency Contract

```text
AI Guess != Dependency Contract
```

模型认为“看起来有依赖”，只能形成候选证据。

---

## 13. Task / Action / Attempt 分层继续有效

```text
Task != Action != Execution Attempt
```

D07 对 Action 进行跨动作协调。Attempt 仍由 D04 管理。

---

## 14. Runtime Coordination 的对象是 Action

Runtime Scheduling 判断各 Action 是否 Ready / Waiting / Blocked / Executing / Completed。Exact Enum 不在 D07 冻结。

---

## 15. Ready 定义

Ready 表示当前 Action 所需上游 Workflow / Dependency 前置条件已经满足，可以进入自身的 Context / Permission / Route 运行流程。

```text
Action Ready != Runtime ALLOW
```

---

## 16. Waiting / Blocked / Failure 分离

```text
Waiting != Failed
Waiting != Blocked
Dependency Not Ready != Action Failure
Blocked != Failed
```

Waiting 表示依赖尚未准备好；Blocked 表示存在适用治理或执行条件阻止继续。

---

## 17. Parallel Execution

D07 正式允许 Parallel Execution，但必须满足当前所有适用：

```text
Workflow Dependency
Resolution Dependency
Scope
Authorization
Runtime Permission
Atomicity
Expected Base
Target relationship
Resource constraints
```

---

## 18. Parallelism 是执行优化，不是语义权限

```text
Parallelism != Authority
Parallelism != Scope Expansion
Parallelism != Workflow Rewrite
```

---

## 19. Minimum Necessary Serialization

D07 正式建立：

```text
Minimum Necessary Serialization
```

只有确实存在执行依赖、语义依赖、Atomicity、Expected Base、Target Conflict 或其他必须串行条件时才串行。

---

## 20. Independence / Dependency / Unknown 边界

```text
Known Independence → Parallel Allowed
Known Dependency → Serialize Where Necessary
Unknown Material Dependency != Safe Independence
Unknown Local Dependency != Serialize Entire Project
```

---

## 21. 文件与模块关系不能替代语义依赖

```text
Different Files != Semantically Independent
File Overlap != Semantic Conflict
Same Module != Must Serialize Entire Task
Same Repository != Same Project Scope
```

实际判断依据仍是 Dependency / Mutation / Atomicity / Expected Base。

---

## 22. Per-Action Runtime Permission

并行 Action 必须分别拥有自己的：

```text
Execution Context
Runtime Permission
Runtime Route
Attempt
Runtime Result
```

```text
Permission(Action A) != Permission(Action B)
Same Task != Shared Runtime Permission
```

---

## 23. Cross-Action Context Isolation

```text
Execution Context(A) != Execution Context(B)
```

可复用 Stable Task Basis，但 Target / Expected Base / Permission / Provider Route / Runtime State / Attempt State 等 Volatile Slice 保持 Action-specific。

```text
Shared Stable Basis != Shared Giant Execution Context
```

---

## 24. Cross-Action Result Handoff

若 B 依赖 A 的 Result：

```text
A Result
→ governed handoff
→ B Context
```

不得依赖 A Provider Session Memory、Temporary Process Memory 或 Hidden Model Context。

```text
Provider Session != Workflow State
```

---

## 25. Result Handoff 保留治理限定

跨 Action Handoff 继续遵循：

```text
Result without required qualifiers != Same Semantic Result
```

不得丢失适用 Scope / Freshness / HOLD / BLOCKED / UNKNOWN / Authority / Authorization Basis / Downstream Obligations。

---

## 26. Barrier / Join Contract

D07 承认 Barrier / Join Condition，用于表达多个上游 Action 达到指定条件后下游才可继续。

Barrier / Join 语义由 Workflow Contract 定义，F10 负责执行。

本 Decision 不冻结 ALL / ANY / QUORUM / N_OF_M 等精确 Join Syntax。

```text
Join Satisfied != Runtime ALLOW
```

下游 Ready 后仍需自身 D01 Permission。

---

## 27. Upstream Success 与 Downstream

```text
Downstream Cannot Proceed != Upstream Successful Result Invalid
```

如果某一个依赖失败，其他已合法完成结果不能被删除。

---

## 28. Failure Propagation

```text
Failure Propagation must follow applicable Dependency
Local Action Failure != Global Task Stop
```

支持 Partial Blocking：只阻塞受影响 Action + materially dependent downstream Actions。

---

## 29. Failure Propagation != Failure Copy

```text
Upstream FAILED != Downstream automatically FAILED
```

下游可根据 Contract 成为 WAITING / BLOCKED / UNAFFECTED / CANCELLED / SKIPPED 等适用状态。

---

## 30. Cancel / Pause / Resume / Retry 传播

```text
Cancel Action B != Cancel A + C automatically
Pause Action != Pause Entire Task automatically
Retry Action != Retry all upstream/sibling Actions
```

Task Cancel 只停止该 Task 后续相关执行，继续保持：

```text
Cancel != Rollback
```

Resume 后仅重新评估 materially dependent Actions，不重启整个 Workflow。

---

## 31. Parallel Started != Independence Proven Forever

```text
Parallel Started != Dependency Stable Forever
```

运行中发现新的 Material Evidence 时：

```text
Capture Evidence
→ Pause affected Action where necessary
→ Targeted Dependency / Impact Re-resolution
```

---

## 32. Runtime-discovered Dependency Evidence

```text
Runtime Dependency Evidence != Canonical Dependency
Effective Dependency Graph Change != Canonical Dependency Mutation
```

长期 Dependency Contract 变化仍走 Domain Owner → F7 Governed Change → Canonical Apply。

---

## 33. Dependency Re-plan

确定性可解时允许 Automatic Dependency Re-plan。

但：

```text
Automatic Dependency Re-plan != Automatic Reauthorization
Impact Discovery != Scope Expansion Authorization
```

---

## 34. Cycle Boundary

D07 不重建 Dependency Cycle Architecture，继续继承：

```text
Workflow Loop != Resolution Dependency Cycle
Cycle != Semantic Conflict
Cycle Detected != Human Decision Required
Local Resolution Cycle != Global Project Invalidation
```

---

## 35. Scheduler Order

```text
Scheduler Order must not change Semantic Result
First Finished != Semantic Winner
Last Finished != Semantic Winner
Race Winner != Authority Winner
Concurrent Change != Conflict
```

完成顺序不产生 Authority。

---

## 36. Expected Base × Parallel Execution

每个 Mutation Action 保持自己适用的 Expected Base。

若 A 修改导致 B 的 Expected Base Material Change：

```text
B must not blindly continue
→ Pause / Revalidate / Reconcile
```

```text
Expected Base Mismatch != Global Task Failure
```

---

## 37. Atomicity Boundary

```text
Parallel Execution must preserve Applicable Atomicity Contract
Parallel != Independent Acceptance
Atomic Group A/B != Serialize unrelated C/D/E
```

继续遵守 Minimum Necessary Serialization。

---

## 38. Runtime Lock != Semantic Authority

```text
Provider Lock
Git Lock
DB Lock
Runtime Lock
!= Semantic Authority
```

锁只做执行协调。

---

## 39. Resource Scheduling

Runtime可根据 Provider concurrency / CPU / memory / rate limit / queue capacity / environment capacity 做资源调度。

但：

```text
Resource Waiting != Semantic Dependency
Temporary Resource Constraint != Governance Block
```

---

## 40. Priority Scheduling

允许 Scheduling Priority，但：

```text
Higher Scheduling Priority != Higher Authority
High Priority != Permission Override
High Priority != Dependency Override
```

Exact Priority Formula 不冻结。

---

## 41. Batch Execution

未来允许 Batch of Actions，但：

```text
Batch != Shared Authority
Batch Result != Every Action Result
```

每个 Material Action 仍保留自身 Result / Evidence / Permission Basis。

---

## 42. Cross-Action Result Composition

```text
Result Composition != Authority Merge
```

多个 Action 成功不能组合出新的 Authority。

多个 Positive Result 也不能覆盖一个适用 Material BLOCK。

---

## 43. Required / Optional / Alternative / Skip

Workflow 可区分 Required Action / Optional Action / Alternative Action，具体语义归 F4。

F10按已解析结果执行。

```text
Runtime cannot invent Alternative Route
Runtime convenience != Skip Authority
```

---

## 44. Cross-Action Handoff

跨 Action Handoff 应遵循：

```text
Purpose-sensitive
Minimum Sufficient
Governance-preserving
```

```text
Handoff Order != Authority Priority
Source Action Owner != Consumer Action Owner
Cross-Action Handoff != Full Action Context Duplication
```

缺失关键限定时：

```text
→ UNKNOWN / UNRESOLVED
```

不得猜 PASS。

---

## 45. Cross-Action Recovery

如果 A Failure 已由 D05 Recovery 恢复：

```text
re-evaluate only materially dependent downstream actions
```

不要求全 Task 重算。

```text
Action A Result invalidated
→ invalidate only dependent material consumers
```

历史 Trace / Evidence 仍保留。

---

## 46. Runtime Scheduler 定位

D07 不建立：

```text
GlobalSchedulerAuthority
UniversalWorkflowAuthority
UniversalDependencyAuthority
```

Runtime Scheduler 只是：

```text
consumer of governed workflow/dependency
+
current runtime state coordinator
```

不是 Truth Owner。

---

## 47. No Fixed Universal Pipeline

D07 不冻结 frontend → backend → test → git 等全局固定顺序。

也不冻结：

```text
one action at a time globally
everything parallel by default
```

---

## 48. Smallest Valid Execution Graph

继续继承 F4：

```text
Runtime MUST prefer
the smallest valid execution graph
+
the smallest necessary resolution scope
```

速度来自：

```text
parallel independent actions
reuse stable context
targeted dependency resolution
localized failure recovery
minimum serialization
```

而不是跳过治理。

---

## 49. Reliable Automatic Routing

当 Dependency / Join / Permission / Runtime State 已知且唯一可解时：

```text
Automatic Scheduling
```

```text
Multiple Ready Actions != Human Scheduling Decision Required
Scheduling Choice != Semantic Choice
Parallel Action Failure != Human Decision Required
Dependency Re-resolution != Human Decision Required
```

---

## 50. Human Decision Boundary

只有出现：

```text
Material Semantic Choice
Authority Conflict
Material Scope Expansion
Multiple Legitimate Incompatible Workflow Choices
Multiple Legitimate Incompatible Dependency Interpretations
High-impact Governance Decision
```

且无已有规则唯一决定时才进入 Human Governance。

---

## 51. Scheduling Trace

Material 调度决策应可解释：

```text
why Action A was Ready
why Action B waited
why A/B ran in parallel
why C was blocked
which dependency / barrier applied
```

但：

```text
Scheduling Trace != Workflow Authority
```

---

## 52. F11 展示边界

未来 F11 可展示 Running / Waiting / Blocked Actions、Dependency Reason、Parallel Group、Recovery State。

但：

```text
F11 UI != Scheduling Authority
UI visual order != Workflow semantic order
```

---

## 53. Current Safety State

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

D07不改变这些状态。

---

## 54. Architecture / Implementation Separation

D07 不冻结：

```text
Exact scheduler algorithm
Exact ready-state enum
Exact waiting-state enum
Exact queue implementation
Exact worker pool
Exact parallelism number
Exact concurrency limit
Exact lock implementation
Exact join syntax
Exact DAG engine
Exact topological-sort algorithm
Exact dependency graph database
Exact cycle algorithm
Exact priority formula
Exact resource scheduler
Exact task runner
Exact distributed scheduler
Exact event bus
Exact persistence schema
```

---

## 55. AI Autonomous Boundary

F10可以自动：

```text
resolve ready actions
schedule independent actions
pause affected dependency chain
resume after deterministic recovery
re-evaluate barriers
request dependency re-resolution
```

但不代表 AI 可 invent Workflow / mutate Dependency Contract / expand Scope / create Authority / silently change Atomicity / invent semantic merge。

---

## 56. Core Invariants

```text
Workflow Orchestration != Runtime Scheduling
Runtime Scheduler != Workflow Authority
Execution Order != Authority Priority
Workflow Dependency != Project Resolution Dependency
Dependency Discovery != Dependency Authority
Runtime Dependency Evidence != Canonical Dependency
Action Ready != Runtime ALLOW
Waiting != Failed
Waiting != Blocked
Dependency Not Ready != Action Failure
Parallelism != Authority
Parallelism != Scope Expansion
Minimum Necessary Serialization
Unknown Material Dependency != Safe Independence
Unknown Local Dependency != Serialize Entire Project
Different Files != Semantically Independent
File Overlap != Semantic Conflict
Same Module != Must Serialize Entire Task
Same Task != Shared Runtime Permission
Permission(A) != Permission(B)
Execution Context(A) != Execution Context(B)
Provider Session != Workflow State
Join Satisfied != Runtime ALLOW
Downstream Cannot Proceed != Upstream Result Invalid
Local Action Failure != Global Task Stop
Failure Propagation must follow Dependency
Cancel Propagation must follow Dependency
Parallel Started != Independence Proven Forever
Effective Dependency Graph Change != Canonical Dependency Mutation
Automatic Dependency Re-plan != Automatic Reauthorization
Workflow Loop != Resolution Dependency Cycle
Cycle != Semantic Conflict
Cycle Detected != Human Decision Required
Local Dependency Cycle != Global Project Invalidation
Scheduler Order must not change Semantic Result
First Finished != Semantic Winner
Last Finished != Semantic Winner
Race Winner != Authority Winner
Concurrent Change != Conflict
Expected Base Mismatch != Global Task Failure
Parallelism must preserve Atomicity
Runtime Lock != Semantic Authority
Resource Waiting != Semantic Dependency
Higher Scheduling Priority != Higher Authority
High Priority != Permission Override
Batch != Shared Authority
Result Composition != Authority Merge
Handoff Order != Authority Priority
Runtime Scheduler != Global Dependency Authority
```

---

## 57. Forbidden Interpretations

明确禁止：

1. F10修改 F4 Workflow Dependency；
2. F10成为第二套 Workflow Authority；
3. F9 Index Edge 直接当 Canonical Dependency；
4. Runtime发现关系后自行增删长期 Dependency；
5. 不同文件默认可并行；
6. 同文件默认整个 Task 串行；
7. Unknown Dependency 默认独立；
8. 局部未知导致整个 Project 永久串行；
9. 同 Task 多 Action 共用 Runtime ALLOW；
10. A 的 Authorization 自动传 B；
11. 多 Action 共用 Giant Execution Context；
12. Provider Session Memory 作为正式 Handoff；
13. Join 满足后跳过 D01；
14. 一个 Action Failure 自动让整个 Task Failure；
15. Failure 不看 Dependency 全量传播；
16. Cancel / Pause / Retry 一个 Action 自动传播整个 Task；
17. 并行启动后忽略新发现 Dependency；
18. Runtime Evidence 自动写 Canonical Dependency；
19. Automatic Re-plan 自动扩大 Authorization；
20. Cycle 默认询问用户；
21. Local Cycle 导致 Global Project Invalid；
22. First / Last Finished 决定 Semantic Winner；
23. Runtime Lock 被解释成 Authority；
24. Atomic Group 导致所有无关 Action 串行；
25. Resource Waiting 写成 Semantic Dependency；
26. Priority 突破 Permission / Gate / Dependency；
27. Batch 共用 Authority；
28. 多数 SUCCESS 覆盖 Material BLOCK；
29. Runtime发明 Alternative / Skip；
30. Handoff 丢失 Scope / Freshness / Blocker；
31. Scheduling Trace 被解释成 Workflow Truth；
32. UI显示顺序修改 Workflow Semantics；
33. D07 Approval 自动授权 Implementation / Real Parallel Execution / Final Activation。

---

## 58. 与 F4 / F7 / F8 / F9 的关系

F4：继续拥有 Workflow Graph、Workflow Dependency、Branch / Merge、Loop / Retry、Pause / Resume、Skip / Replace、Partial Blocking、Join / Handoff、Escalation。

F7：继续拥有 Apply Scope、Expected Base、Write Set、Impact Set、Semantic Atomicity、Concurrent Change Reconciliation、Canonical Apply。

F8 / Domain Resolution：继续拥有 Project Resolution Dependency、Active Hard Dependency、Cycle / Convergence、Current Effective Resolution。

F9：继续拥有 Dependency Index、Reverse Dependency、Dependency / Impact Discovery、Candidate Retrieval、Freshness、Provenance。

F10-D07：仅协调多个已受治理 Action 的 Runtime 执行。

---

## 59. 与 D01～D06 的关系

D01：每个 Action 自己做 Runtime Permission。  
D02：每个 Action 自己拥有 minimum-sufficient Execution Context。  
D03：每个 Action自己解析 Provider / Adapter Route。  
D04：每个 Action / Attempt 有独立 Lifecycle。  
D05：Failure / Block 传播遵循真实 Dependency Blast Radius。  
D06：跨 Action Result / Evidence / Handoff 保持 Qualifier 与 Acceptance Boundary。  
D07：负责多个 Action 的安全、高效 Runtime Coordination。

---

## 60. 后续边界

D07 不提前冻结：

```text
F10 → F11 formal runtime handoff
Control Plane command boundary
Runtime user-intervention contract
F10 stage exit criteria
F10 final consistency review
F10 architecture freeze closure
```

---

## 61. Acceptance Meaning

用户已明确批准：

```text
F10-D07 HUMAN_APPROVED
```

因此正式成立：

```text
F4 Workflow Authority remains separate from F10 Runtime Scheduling
Dependency domains remain owner-separated
F10 cannot mutate dependency truth
Ready / Waiting / Blocked semantics remain distinct
safe parallel execution is allowed
Minimum Necessary Serialization is the default principle
each Action keeps its own Permission / Context / Route / Attempt
failure / pause / cancel propagation follows real dependencies
Barrier / Join conditions are enforced, not invented by F10
parallel execution must preserve Expected Base and Atomicity
runtime-discovered dependencies route for re-resolution
resource scheduling and priority remain operational, not Authority
cross-action results use governed explicit handoff
automatic scheduling is preferred whenever deterministic
human involvement remains limited to genuine unresolved semantic decisions
```

但不表示批准 Exact Scheduler / DAG / Queue / Worker / Parallelism / Join Syntax / Dependency Storage / Locking / Priority Formula、Implementation、Real Project Parallel Execution、RP2、Authority Cutover、Canonical Replacement、Final Activation 或 Legacy Retirement。

---

## 62. Approval Status

```text
F10-D07 = HUMAN_APPROVED
```

普通“好的 / 下一步 / 继续 / 按建议继续”均不代表后续 Decision 的批准。

---

**END**

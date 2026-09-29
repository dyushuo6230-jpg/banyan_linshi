# F10-D04 — Execution Lifecycle × Attempt × Pause / Resume / Retry / Cancel Boundary

**阶段：** F10 — Runtime Permission / Execution Governance Architecture  
**主题：** Execution Lifecycle（执行生命周期）× Execution Attempt（执行尝试）× Pause / Resume / Retry / Cancel 边界  
**状态：** `HUMAN_APPROVED`  
**上游依赖：**
- `F10-G01 HUMAN_APPROVED`
- `F10-D01 HUMAN_APPROVED`
- `F10-D02 HUMAN_APPROVED`
- `F10-D03 HUMAN_APPROVED`

**Implementation Authorization：** `NO`

---

## 1. 决策目的

F10-D04 解决：

> 当一个 Action 真正进入执行以后，如何表达它当前处于什么运行状态；发生技术失败、Provider/Adapter 故障、上下文变化、暂停、恢复、重试、取消、结果不确定等情况时，Banyan 如何安全地继续，而不会把一次技术故障错误解释成新的业务动作、盲目重复产生副作用，或者越过上游治理边界。

核心目标：

```text
Task
↓
Action
↓
Execution Attempt
↓
Result / Pause / Retry / Recovery
↓
Action Completion
```

同时保持：

```text
Runtime Recovery
!= Semantic Authority
```

---

## 2. Task / Action / Execution Attempt 三层分离

正式：

```text
Task
!= Action
!= Execution Attempt
```

### Task

表达用户或 Workflow（工作流）最终需要完成的目标。

例如：

```text
给商品管理增加批量上下架
```

### Action

表达完成 Task 所需的某一个逻辑执行动作。

例如：

```text
修改 tenant-admin 页面
修改 backend API
运行测试
检查 Git Diff
```

### Execution Attempt

表达某个 Action 的一次具体运行尝试。

例如：

```text
Action = 修改 backend API

Attempt 1
→ Provider timeout

Attempt 2
→ Provider fallback
→ success
```

---

## 3. Retry 默认不创建新的业务 Action

正式：

```text
Retry
!= New Task

Retry
!= New Business Action
```

对于仍属于同一逻辑目标、同一 Action 语义的重试：

```text
same Action
→ new Execution Attempt
```

---

## 4. Execution Attempt Identity

Execution Attempt 应能够在逻辑上区分不同运行尝试。

例如：

```text
Action-A
├── Attempt-1
├── Attempt-2
└── Attempt-3
```

但：

```text
Execution Attempt Identity
!= Domain Stable Identity
```

F10 不建立与 F7 Stable ID / Revision Governance 竞争的新长期身份体系。

---

## 5. F10 Execution Attempt != F7 Apply Attempt

F7 已经拥有：

```text
Apply Attempt
```

用于 Governed Change / Canonical Apply（受治理变更 / 规范应用）领域。

F10 的 Execution Attempt 表达：

> 一次具体技术运行尝试。

因此正式：

```text
F10 Execution Attempt
!= F7 Apply Attempt
```

---

## 6. 两类 Attempt 可以存在映射，但不得合并 Owner

一个 F7 Apply Attempt 底层可能通过一个或多个 F10 Execution Attempt 完成。

例如：

```text
F7 Apply Attempt A
↓
F10 Execution Attempt 1
→ transient failure

F10 Execution Attempt 2
→ technical recovery
→ succeeds
```

具体映射依据适用 Apply / Execution Contract。

F10 不重新定义 F7 Apply Attempt。

---

## 7. Execution Attempt != Apply Result

正式保持：

```text
Execution Attempt Result
!= F7 Apply Result

F7 Apply Result
!= Change Result
```

一次技术执行成功不能自动证明整个 Governed Apply 成功。

---

## 8. Execution Lifecycle 不只包含成功 / 失败

F10 生命周期必须能够在逻辑上表达至少以下类别：

```text
Not Started / Prepared
Executing
Paused
Completed
Failed
Cancelled
Outcome Unknown
```

本 D04 **不冻结精确 Enum 名称**。

---

## 9. State Semantics != Exact State Machine

D04 冻结的是状态意义和转换约束，而不是：

```text
Exact Enum
Exact State Diagram
Exact Database Status
Exact Transition API
```

这些延后到实现或更具体 Contract。

---

## 10. Prepared / Ready Boundary

Action 已完成：

```text
Execution Context assembly
Runtime route resolution
Applicable permission checks
```

可能进入可执行准备状态。

但：

```text
Prepared
!= Executed

Prepared
!= Completed
```

---

## 11. Executing Boundary

Executing 表达：

> 当前 Attempt 已开始进入实际执行过程，并可能产生 Runtime Side Effect（运行时副作用）。

一旦进入可能产生副作用的阶段，就不能再假设：

```text
failure
=
nothing happened
```

---

## 12. Provider / Adapter Success != Governed Action Success

Provider 或 Adapter 返回：

```text
SUCCESS
```

首先只是 Execution Evidence（执行证据）。

正式：

```text
Provider Success
!= Action Complete

Adapter Success
!= Action Complete
```

仍需满足当前 Execution Contract 要求的：

```text
target verification
post-execution validation
expected result
required evidence
applicable downstream checks
```

---

## 13. Mutation Completed != Canonical Apply Succeeded

正式继承 F7：

```text
Mutation Completed
!= Canonical Apply Succeeded
```

F10 不能把：

```text
file written
git command returned success
provider reports success
```

直接解释成 F7 Canonical Apply 成功。

---

## 14. Pause 定义

Pause（暂停）表示：

> 当前 Action 暂时停止继续产生新的执行副作用，但 Action 尚未结束，也不自动判定失败或取消。

正式：

```text
Pause
!= Failure

Pause
!= Cancel

Pause
!= Rollback
```

---

## 15. Pause 是可恢复运行状态

可能触发 Pause 的情况包括：

```text
Required Context temporarily unavailable
Expected Base needs revalidation
Provider temporary unavailable
Adapter temporary unavailable
Gate changed
Authorization applicability needs revalidation
Target mismatch
Runtime dependency became stale
Safe interruption requested
```

具体 Trigger（触发条件）由适用 Contract 决定。

---

## 16. Pause 不自动使整个 Task 失败

正式：

```text
Action Paused
!= Task Failed
```

Task 中其他不依赖该 Action 的合法工作，是否可以继续，由 Workflow / Dependency Contract 决定。

---

## 17. Pause 必须保留恢复所需的最小充分状态

逻辑上应能够保留当前 Action 相关的：

```text
Task Ref
Action Ref
Attempt lineage
Execution Context basis
Permission basis
Runtime route basis
Known progress
Known side effects
Applicable checkpoint where supported
Pause reason
Relevant evidence
```

不要求建立一个固定大对象。

---

## 18. Pause State != New Canonical Truth

暂停信息属于 Runtime State。

正式：

```text
Pause State
!= Canonical Truth

Pause Reason
!= Semantic Authority
```

---

## 19. Resume 定义

Resume（恢复）表示：

> 对一个尚未终结的 Paused Action，在确认相关恢复条件后继续完成该 Action。

正式：

```text
Resume
!= Blind Continue
```

---

## 20. Resume 前必须 Targeted Revalidation

恢复前只检查与 Pause 原因和当前 Action 合法性相关的 Material Basis。

例如：

```text
Authorization validity
Scope
Expected Base
Freshness
Provider / Adapter route
Gate
Target state
Deferred Guard
```

正式：

```text
Resume
→ Targeted Revalidation
```

而不是：

```text
Resume
→ Full Architecture Re-resolution
```

---

## 21. Automatic Resume

如果导致 Pause 的条件已经恢复，并且：

```text
Scope unchanged
Authorization still applicable
Required target basis still valid
No unresolved material conflict
```

则：

```text
Automatic Resume
```

不要求用户确认。

---

## 22. Resume Action != Continue Same Process

恢复一个 Action 不要求必须恢复相同 OS Process、Provider Session 或 Network Connection。

正式：

```text
Resume Action
!= Continue Same Technical Process
```

例如：

```text
Attempt 1 interrupted
↓
safe state confirmed
↓
Attempt 2 starts
↓
same Action resumes
```

这是合法的 Resume。

---

## 23. Resume 可以产生新的 Attempt

如果原 Attempt 无法技术恢复，但 Action 仍可安全继续：

```text
Paused Action
↓
new Execution Attempt
↓
Resume
```

因此：

```text
Resume
does not require
same Attempt identity
```

---

## 24. Retry 定义

Retry 表示：

> 对仍然有效的同一 Action 再次发起执行尝试。

通常：

```text
Retry
→ new Execution Attempt
```

---

## 25. Retry != Blind Repeat

正式：

```text
Retry
!= Blind Repeat
```

Retry 前必须确认当前动作仍具备适用执行基础。

可能包括：

```text
Action semantics still valid
Scope still valid
Authorization still applicable
Target / Expected Base still safe
Required Context still valid
Runtime route still applicable or safely re-resolved
Previous Attempt side-effect state understood
```

---

## 26. Retry × D03 Fallback

Retry 与 Provider / Adapter Fallback 是不同语义。

例如：

```text
Attempt 1
Provider A
→ timeout

Attempt 2
Provider A
```

是：

```text
Retry
```

而：

```text
Attempt 2
Provider B
```

可能同时是：

```text
Retry
+
Governed Fallback
```

因此：

```text
Retry
!= Fallback
```

但允许组合。

---

## 27. Retry 不要求重复全部前置治理

如果 Material Basis 没有变化：

```text
Retry
→ Targeted Revalidation
```

而不是重新进行整个 Task 的完整审批。

---

## 28. Side Effect Boundary

F10 执行生命周期必须明确区分：

```text
Known No Side Effect
Known Side Effect
Side Effect Unknown
```

具体 Enum 名称不在 D04 冻结。

---

## 29. Timeout != No Side Effect

正式：

```text
Timeout
!= No Side Effect

No Response
!= Action Not Executed

Connection Lost
!= No Mutation
```

因为 Provider / Adapter 可能已经执行，只是执行结果没有成功返回。

---

## 30. Known No Side Effect

如果能够确定前一次 Attempt：

```text
produced no relevant side effect
```

则在完成适用 Revalidation 后，可以安全进入：

```text
Retry
```

---

## 31. Known Side Effect

如果明确已经发生副作用：

```text
Known Side Effect
```

则不得简单重新重复同样 Mutation。

必须根据实际状态判断：

```text
continue
validate
recover
complete
or route
```

---

## 32. Side Effect Unknown

如果无法确定前一次 Attempt 是否已经产生副作用：

```text
Side Effect Unknown
```

则：

```text
Blind Retry = FORBIDDEN
```

---

## 33. Actual State Reconciliation

Side Effect Unknown 时应优先：

```text
Inspect Actual Target State
↓
Compare Expected State / Expected Base
↓
Determine Known Actual Effect
↓
Choose safe continuation
```

正式：

```text
Unknown Side Effect
→ Actual State Reconciliation
```

---

## 34. Reconciliation 结果

对账后可能得到：

```text
Not Applied
Already Applied
Partially Applied
Applied Differently
Still Unknown
```

具体 Enum 不在 D04 冻结。

---

## 35. Already Applied

如果当前 Action 的预期效果已经完整、合法成立：

```text
Already Applied
```

则不得为了“Retry”再次重复 Mutation。

后续应进入适用 Validation / Completion 判断。

---

## 36. Not Applied

如果确定：

```text
No relevant side effect occurred
```

且其他 Material Basis 仍合法，则可以创建新的 Attempt 重试。

---

## 37. Partial Effect

如果：

```text
Partially Applied
```

不能假装：

```text
nothing happened
```

也不能直接假装：

```text
completed
```

必须进入适用 Recovery / Reconciliation。

---

## 38. Idempotency Boundary

某个 Action 即使技术上看似可重复，也不能默认假设：

```text
Action is idempotent
```

正式：

```text
Retry-safe
must be established
by applicable execution contract / state reconciliation
```

而不是模型猜测。

---

## 39. Checkpoint 定义

Checkpoint（检查点）用于表达：

> 某个 Action 在当前执行合同允许的情况下，已经安全完成并可作为恢复基点的阶段性状态。

---

## 40. Checkpoint 不是所有 Action 的强制要求

正式：

```text
Checkpoint Support
= Contract-dependent
```

某些 Action 可以：

```text
checkpoint → resume
```

某些 Atomic Action（原子动作）则可能不允许中间 Checkpoint。

---

## 41. Checkpoint != Canonical Acceptance

正式：

```text
Checkpoint
!= Canonical Acceptance
```

Checkpoint 只是 Runtime Recovery Basis（运行时恢复依据）。

---

## 42. Atomicity Boundary

如果上游 Execution / Apply Contract 要求：

```text
Semantic Atomicity
```

F10 不得为了方便 Retry / Resume 把它静默拆成可独立接受的多个语义结果。

正式：

```text
Runtime Recovery
must preserve
applicable Atomicity Contract
```

---

## 43. F7 Atomicity 继续归 F7

F7 继续拥有：

```text
Apply Plan
Semantic Atomicity Boundary
Canonical Apply Governance
```

F10负责：

```text
concrete execution enforcement
```

而不是重新解释 Atomicity。

---

## 44. Cancel 定义

Cancel（取消）表示：

> 停止当前 Action / Task 尚未发生的未来执行。

正式：

```text
Cancel
!= Rollback
```

---

## 45. Cancel 不自动撤销已经发生的副作用

例如：

```text
Action A completed
Action B not started
↓
Cancel
```

不自动意味着：

```text
undo Action A
```

已经产生的效果如何处理，由对应 Recovery / Change / Rollback Contract 决定。

---

## 46. Cancel Requested != Safely Cancelled

对于正在执行的 Action：

```text
Cancel Requested
```

不一定能立刻安全中断。

正式：

```text
Cancel Requested
!= Safely Cancelled
```

---

## 47. Safe Interruption Boundary

如果某 Action 不能任意时刻中断，则 Cancel 应：

```text
request stop
↓
reach applicable safe interruption boundary
↓
stop future execution
```

具体机制不在 D04 冻结。

---

## 48. Cancel During Atomic Operation

如果适用 Atomicity Contract 不允许中间中断：

```text
Cancel Request
```

不得破坏原子性。

系统应按当前 Contract 到达安全边界后再终止未来执行。

---

## 49. Cancelled != Failed

正式：

```text
Cancelled
!= Failed
```

Cancelled 表示执行被主动终止。

Failed 表示执行未按计划成功完成。

两者结果语义不同。

---

## 50. Cancelled != Rolled Back

继续保持：

```text
Cancelled
!= Rolled Back
```

---

## 51. Technical Recovery 定义

Technical Recovery（技术恢复）处理：

> 在语义目标未改变的前提下，对失败、中断、部分副作用或技术执行问题进行安全恢复。

例如：

```text
restore technical consistency
retry safe action
resume from checkpoint
switch governed adapter/provider
reconcile actual target state
```

---

## 52. Technical Recovery != Semantic Rollback

正式继承 F7：

```text
Technical Recovery
!= Semantic Rollback

Technical Recovery
!= Compensating Change

Technical Recovery
!= Data Restoration
```

这些不能因为都叫“恢复”而混为一类。

---

## 53. Canonical Acceptance 前后的边界

对 F7 Canonical Apply 类 Action：

Canonical Acceptance 之前的失败，可进入：

```text
Technical Recovery
```

Canonical Acceptance 以后如果希望撤销已接受的语义结果：

```text
Semantic Rollback Intent
→ Governed Change / Apply Path
```

F10不能自行实施语义回滚。

---

## 54. Execution Failure 定义

Execution Failure 表示：

> 某次 Execution Attempt 未能满足本次尝试要求。

它首先属于 Runtime Result / Evidence。

---

## 55. Execution Failure != Action Failure Automatically

某次 Attempt 失败：

```text
Attempt Failed
```

不自动意味着：

```text
Action Failed Permanently
```

因为 Action 可能：

```text
Retry
Fallback
Recover
Resume
```

---

## 56. Action Failure Boundary

只有当当前 Action 根据适用 Lifecycle / Recovery Contract 已无法合法继续或被明确终止时，才形成 Action-level Failure。

---

## 57. Action Failure != Task Failure Automatically

正式：

```text
Action Failed
!= Task Failed
```

Task 是否失败，需要结合：

```text
Workflow dependency
Required vs optional action
Recovery path
Alternative route
Downstream obligations
```

判断。

---

## 58. Attempt Success != Action Complete

一次 Attempt 技术成功：

```text
Attempt Success
```

仍可能需要：

```text
post-execution validation
target verification
required evidence
downstream gate
```

所以：

```text
Attempt Success
!= Action Complete
```

---

## 59. Action Complete != Task Complete

正式：

```text
Action Complete
!= Task Complete
```

一个 Task 可以包含多个 Action、Validation、Obligation 和 Gate。

---

## 60. Outcome Unknown

F10-D04 正式承认：

```text
Outcome Unknown
```

作为必要的逻辑状态类别。

它表示：

> 当前系统尚不能可靠确认一次 Attempt 最终造成了什么结果或副作用。

---

## 61. Outcome Unknown != Failure

正式：

```text
Outcome Unknown
!= Failure

Outcome Unknown
!= Success

Outcome Unknown
!= No Side Effect
```

---

## 62. Outcome Unknown 优先自动对账

出现 Outcome Unknown 时：

```text
Automatic State Inspection
+
Targeted Reconciliation
```

应优先于询问用户。

---

## 63. Outcome Unknown 的人工边界

只有在：

```text
automatic inspection unavailable
+
material side effect cannot be safely determined
+
continuation requires a consequential choice
```

时才进入 Human Governance。

---

## 64. Permission × Lifecycle

D01 Runtime Permission 不是只在 Action 开始时检查一次然后永久有效。

如果生命周期中相关 Material Basis 发生变化：

```text
Authorization revoked
Scope materially changed
Gate changed
Expected Base conflict
Relevant provider route no longer valid
Deferred Guard changed
```

则受影响执行必须：

```text
Pause / stop at safe boundary
→ revalidate
```

---

## 65. Initial ALLOW != Execute Forever

正式：

```text
Initial Runtime ALLOW
!= Permanent Permission Until Action Ends
```

但也不要求每个技术步骤都重新完整算 Permission。

采用：

```text
dependency-sensitive targeted revalidation
```

---

## 66. Mid-execution Authorization Change

执行中如果发现 Authorization：

```text
Revoked
Superseded
No Longer Applicable
```

则未来受影响的执行不能继续。

正确：

```text
stop at applicable safe boundary
→ preserve state / evidence
→ route governance
```

---

## 67. 已经发生的副作用不自动回滚

即使 Authorization 中途失效：

```text
already produced side effects
```

也不能自动推导：

```text
rollback everything
```

如何处理已发生结果，由适用领域 Governance 决定。

---

## 68. D03 Provider Fallback × Lifecycle

如果当前 Provider / Adapter 出现可恢复运行故障：

```text
Attempt fails / pauses
↓
D03 resolves governed compatible route
↓
new Attempt
↓
continue same Action
```

可以自动完成。

---

## 69. Provider Change != New Action

在保持同一 Action 语义的情况下：

```text
Provider A
→ Provider B
```

不自动创建新的业务 Action。

它可以只是新的 Execution Attempt / Runtime Route。

---

## 70. Adapter Change != New Action

同样：

```text
Adapter A
→ Adapter B
```

如果执行合同保持：

```text
same Action
same semantics
```

不构成新业务 Action。

---

## 71. D02 Context × Lifecycle

Pause / Retry / Resume 不要求默认复制整个旧 Execution Context。

正确：

```text
reuse still-valid stable basis
+
refresh changed runtime slices
```

---

## 72. Context Changed During Pause

Pause 期间相关 Context 发生变化时，应按照 D02：

```text
selective invalidation
+
targeted rebuild
```

而不是默认整 Task 重放。

---

## 73. Recovery Context != New Truth

Recovery 过程中得到的实际状态、Diff、Provider Result 等属于：

```text
Runtime Evidence / Observation
```

不自动成为 Canonical Truth。

---

## 74. Trace / Evidence Requirement

每个 Material Execution Attempt 应能够在需要时追踪：

```text
Action Ref
Attempt Ref
Runtime route
Permission / Authorization basis
Start / End or relevant lifecycle markers
Result
Known side effects
Validation result
Failure / Pause reason
Recovery relation
```

本 D04 不冻结具体 Trace Schema。

---

## 75. Attempt Lineage

Retry / Resume / Recovery 产生新 Attempt 时，应能逻辑追踪：

```text
previous attempt
→ next attempt
```

从而避免多个执行尝试成为无法关联的孤立事件。

---

## 76. Attempt Lineage != Authority

正式：

```text
Attempt Lineage
!= Authority
```

它是 Trace / Recovery Basis，不是执行授权来源。

---

## 77. Failure Classification

D04 允许后续对 Failure 进行分类，例如：

```text
Provider failure
Adapter failure
Context failure
Permission failure
Target mismatch
Validation failure
Infrastructure failure
Outcome unknown
```

但不在本 D04 固定完整 Taxonomy。

---

## 78. Failure Classification 用于路由，不用于抢 Owner

例如：

```text
Provider failure
→ D03 runtime route resolution

Freshness problem
→ F9

Apply semantic conflict
→ F7

Product semantic conflict
→ Product Owner
```

F10负责检测和路由，不吞并对应领域 Authority。

---

## 79. Automatic Recovery First

对于：

```text
transient network error
temporary provider failure
compatible adapter fallback
machine-resolvable stale context
non-material expected-base change
safe retry
safe resume
```

应优先：

```text
Automatic Recovery
```

而不是 Human Decision。

---

## 80. Human Decision Boundary

以下情况才可能进入 Human Governance：

```text
Material Semantic Choice
Authority Conflict
Material Scope Expansion
Unknown Side Effect cannot be safely reconciled
Multiple legitimate incompatible recovery paths
New high-impact authorization required
Explicit human-only governance requirement
```

---

## 81. Multiple Recovery Paths != Human Decision Automatically

如果多个恢复路径存在，但已有规则能够唯一决定：

```text
Automatic Resolve
```

只有多个合法恢复路径产生重大不同后果且现有治理无法确定 Winner 时，才需要 Human Decision。

---

## 82. Failure != Human Decision Required

正式：

```text
Execution Failure
!= Human Decision Required
```

以及：

```text
Pause
!= Human Decision Required

Retry
!= Human Approval Required

Resume
!= Human Approval Required
```

---

## 83. No Infinite Retry

D04 不授权：

```text
retry forever
```

Retry 必须受适用 Recovery / Resource / Safety Contract 约束。

但本 D04 不冻结具体：

```text
Retry Count
Backoff
Timeout
```

---

## 84. Retry Exhaustion

达到适用 Retry / Recovery 边界后：

```text
Retry Exhausted
```

不自动等于 Human Decision。

可能进入：

```text
Fallback
Pause
Block
Route Owner
Fail Action
```

由适用 Contract 判断。

---

## 85. No Infinite Pause

同样：

```text
Pause
```

不是无限期隐藏问题的机制。

如果恢复条件长期无法满足，应根据适用治理：

```text
route
terminate
cancel
block
or require decision
```

具体策略后续冻结。

---

## 86. Execution Order Boundary

D04 不把 Action Lifecycle 定义成全系统唯一固定顺序。

正式：

```text
Lifecycle semantics
!= One universal Workflow
```

不同 Workflow 可以组合不同 Action，只要遵守本 D04 生命周期合同。

---

## 87. Parallel Execution Boundary

D04 不禁止未来多个独立 Action 并行执行。

但：

```text
Parallel
!= Ignore Dependency / Atomicity / Scope
```

具体并发控制不在 D04 冻结。

---

## 88. Concurrent Mutation Boundary

如果多个 Action 可能修改相同或相关 Target：

```text
Concurrency
```

必须遵循 F7 / F9 / Expected Base / Applicable Conflict Governance。

D04 不创建新的 Semantic Merge Authority。

---

## 89. No Runtime Semantic Merge

正式：

```text
Runtime detects conflict
!= Runtime may invent semantic merge
```

未解析语义冲突必须路由相应 Owner。

---

## 90. Current Project Safety State

当前继续保持：

```text
Current Project Execution = DRY_RUN_ONLY where governed
Canonical Write = BLOCKED where governed
Final Activation = NOT_AUTHORIZED
```

D04 只冻结生命周期语义，不解除任何执行限制。

---

## 91. Historical Runtime Compatibility

历史 Runtime / Semantic Commit Executor 已有：

```text
permission precheck
authorization validation
identity check
staging verification
trace
leftover validation
rollback test in isolated fixture
```

这些可作为 Compatibility Evidence。

但：

```text
Historical Executor Behavior
!= F10-D04 Architecture Authority
```

---

## 92. Architecture / Implementation Separation

D04 不冻结：

```text
Exact lifecycle enum
Exact state machine code
Exact Attempt ID format
Exact checkpoint format
Exact persistence layer
Exact retry count
Exact timeout
Exact backoff
Exact cancellation API
Exact process kill behavior
Exact queue semantics
Exact job scheduler
Exact transaction implementation
Exact compensation algorithm
Exact trace schema
Exact recovery storage
```

---

## 93. AI Autonomous Boundary

自动：

```text
Pause
Revalidate
Retry
Fallback
Resume
State Reconciliation
```

属于既有规则下的运行时确定性治理。

不代表：

```text
AI creates new Authority
AI changes Product semantics
AI performs unauthorized rollback
AI invents recovery policy
AI autonomously expands Scope
```

---

## 94. Core Invariants

F10-D04 正式建立：

```text
Task
!= Action
!= Execution Attempt

Retry
!= New Task

Retry
!= New Business Action

F10 Execution Attempt
!= F7 Apply Attempt

Execution Attempt Result
!= Apply Result
!= Change Result

Provider Success
!= Action Complete

Mutation Completed
!= Canonical Apply Succeeded

Pause
!= Failure

Pause
!= Cancel

Pause
!= Rollback

Resume
!= Blind Continue

Resume Action
!= Continue Same Technical Process

Retry
!= Blind Repeat

Retry
!= Fallback

Timeout
!= No Side Effect

No Response
!= Action Not Executed

Side Effect Unknown
→ Reconcile Before Retry

Checkpoint
!= Canonical Acceptance

Cancel
!= Rollback

Cancel Requested
!= Safely Cancelled

Cancelled
!= Failed

Technical Recovery
!= Semantic Rollback

Attempt Failed
!= Action Failed Permanently

Attempt Success
!= Action Complete

Action Complete
!= Task Complete

Outcome Unknown
!= Failure
!= Success

Initial Runtime ALLOW
!= Permanent Permission

Provider Change
!= New Business Action

Adapter Change
!= New Business Action

Failure
!= Human Decision Required

Runtime Conflict Detection
!= Semantic Merge Authority
```

---

## 95. Forbidden Interpretations

明确禁止：

1. Provider timeout 后直接假设没有副作用；
2. No Response 后直接重复 Mutation；
3. Retry 自动创建新的 Task；
4. 每次 Retry 都要求重新做完整人工审批；
5. 把 F10 Execution Attempt 当成 F7 Apply Attempt；
6. Provider Success 直接等于 Action Success；
7. File Write Success 直接等于 Canonical Apply Success；
8. Attempt Success 直接等于 Task Success；
9. Pause 自动等于 Failure；
10. Pause 自动等于 Cancel；
11. Resume 不校验变化直接继续；
12. Resume 必须恢复相同 OS Process；
13. Retry 和 Fallback 混为一个概念；
14. Partial Side Effect 当成 No Side Effect；
15. Side Effect Unknown 时盲目重试；
16. 默认所有 Action 都是 Idempotent；
17. 所有 Action 强制使用 Checkpoint；
18. Checkpoint 自动等于 Canonical Acceptance；
19. Cancel 自动撤销已完成副作用；
20. Cancel Request 立即硬切断所有 Atomic Action；
21. Technical Recovery 自动变成 Semantic Rollback；
22. F10 自行 Rollback 已 Canonically Accepted 的语义变化；
23. Initial ALLOW 后忽略 Authorization / Gate 的后续重大变化；
24. Provider/Adapter 切换自动创建新业务 Action；
25. 一个 Attempt 失败就立即询问用户；
26. 所有 Runtime Failure 都升级 Human Decision；
27. 无限 Retry；
28. 无限 Pause 隐藏未解决问题；
29. Runtime 发现并发冲突后自行语义合并；
30. D04 Approval 自动授权真实 Mutation / Implementation / Final Activation。

---

## 96. 与 F7 的关系

F7 继续拥有：

```text
Apply Plan
Apply Authorization
Apply Scope
Expected Base semantics
Semantic Atomicity
Apply Attempt
Canonical Acceptance
Apply Result
Semantic Rollback
Change Closeout
```

F10-D04 负责：

```text
concrete execution lifecycle
technical attempt
runtime pause / retry / resume / cancel
technical recovery coordination
```

不修改 F7 Owner。

---

## 97. 与 F10-D01 的关系

D01 决定：

```text
Can this Action execute now?
```

D04 规定：

```text
What happens after execution begins?
```

生命周期发生 Material Basis 变化时，调用 D01 的 Targeted Revalidation。

---

## 98. 与 F10-D02 的关系

D02 提供：

```text
Action-specific Execution Context
```

D04 在 Pause / Resume / Retry 时只刷新必要 Context Slice，不默认重新加载全部 Task Context。

---

## 99. 与 F10-D03 的关系

D03 提供：

```text
Runtime Provider / Adapter Route
```

D04 在 Provider / Adapter 故障时，可以通过 D03 解析合法 Fallback，再创建新的 Execution Attempt。

---

## 100. 后续 Decision 边界

D04 已覆盖总体生命周期语义，但不完整冻结：

```text
Detailed Failure / Recovery taxonomy
Result / Evidence / Trace contract
Execution acceptance criteria
Cross-action orchestration
Stage exit / F11 handoff
```

这些由后续 F10 Decision 继续收敛。

---

## 101. Acceptance Meaning

用户已明确批准：

```text
F10-D04 HUMAN_APPROVED
```

因此正式成立：

```text
Task / Action / Execution Attempt separation
Execution Attempt distinct from F7 Apply Attempt
Retry normally creates new Attempt under same Action
Pause / Resume / Retry / Cancel semantics
Outcome Unknown as a real runtime condition
No blind retry when side effects are unknown
Actual-state reconciliation before uncertain retry
Checkpoint is contract-dependent
Cancel does not imply rollback
Technical Recovery does not imply Semantic Rollback
Runtime ALLOW must remain validity-sensitive during execution
Ordinary recoverable failures auto-recover first
Human escalation remains exceptional
```

但不表示批准：

```text
Exact State Enum
Exact Retry Count
Exact Timeout
Exact Backoff
Exact Checkpoint Storage
Exact Recovery Algorithm
Implementation
Real Project Write
RP2
Authority Cutover
Canonical Replacement
Final Activation
Legacy Retirement
```

---

## 102. Approval Status

```text
F10-D04 = HUMAN_APPROVED
```

普通“好的 / 下一步 / 继续 / 按建议继续”均不代表后续 Decision 的批准。

---

**END**

# F11-D02 — Runtime Projection & State Presentation
## 运行状态投影与展示

**Stage：** F11 — Control Plane / Governance UX Architecture（控制面 / 治理交互架构）  
**Decision ID：** F11-D02  
**Upstream Gate：** F11-G01 = HUMAN_APPROVED / FROZEN  
**Upstream Decision：** F11-D01 = HUMAN_APPROVED / FROZEN  
**Status：** HUMAN_APPROVED / FROZEN  

**Implementation Authorization：** NO  
**RP2 Authorization：** NO  
**Authority Cutover Authorization：** NO  
**Canonical Replacement Authorization：** NO  
**Final Activation Authorization：** NO  
**Legacy Retirement Authorization：** NO  

---

# 1. 决策目标

F11-D02 用于冻结 Banyan Control Plane 对 Runtime State（运行状态）的投影与展示语义。

本 Decision 不重新设计 F10 Runtime State Machine（运行状态机），而是回答：

```text
F10 / Domain 已经知道系统现在处于什么状态后，

F11 如何：
准确展示当前状态；
解释 Task / Action / Attempt 层级；
区分 Current / Latest Known / Historical；
展示 Reason / Blocker / Recovery / Progress；
表达 Human Attention Requirement；
展示当前可见的 Control Hint；
处理 Stale Projection；
处理断线和重连；
展示多个 Domain Qualifier；
区分 Terminal State / Result / Acceptance / Apply；
并保证 UI 不创造第二份 Runtime Truth。
```

---

# 2. 上游冻结继承

F11-D02 必须继承 F11-G01 与 F11-D01。

继续保持：

```text
F11 != Runtime Authority

Presentation State
!= Runtime State Truth

RuntimeProjection
!= Runtime Truth

RuntimeProjection
!= Canonical Truth

Projection Contract Owner
!= Projected Fact Authority Owner

Task
!= Action
!= Execution Attempt

Control Hint
!= Runtime Permission

UI Enabled
!= Permission Granted
```

F10 已冻结：

```text
Waiting != Failed
Waiting != Blocked

Task != Action != Execution Attempt
```

---

# 3. F11 不重新建立 Runtime State Machine

F11 不维护一套与 F10 平行的权威运行状态机。

正式：

```text
Authoritative Runtime State
→ RuntimeProjection
→ Presentation Mapping
→ Human-readable Presentation
```

禁止：

```text
F10 State
→ F11 invents another authoritative State
→ F11 State drives Runtime
```

因此：

```text
Presentation Mapping
!= New Runtime State Machine
```

---

# 4. Presentation State 的定位

F11 可以为了人类理解，将 Runtime State 映射为：

```text
“执行中”
“等待中”
“被阻塞”
“正在恢复”
“已完成”
```

等展示语言。

但：

```text
Presentation State
!= Runtime State Truth

Presentation Label
!= Runtime Permission

Presentation Label
!= Domain Authority
```

Presentation State 只解决：

> 人应该怎样理解当前已知事实。

不得反向成为 Runtime Scheduler、Provider Resolution、Permission Resolution 或 Governance Resolution 的输入 Truth。

---

# 5. Runtime Presentation 采用正交维度模型

F11-D02 不通过不断增加复合 State Enum 来表达所有情况。

Runtime Presentation 逻辑上允许由以下独立维度组合：

```text
Authoritative State

Presentation Summary

Reason

Blocker

Recovery

Progress + Progress Basis

Expected Continuation

Human Attention Requirement

Available Control Hint

Observation / Freshness

Result / Evidence / Trace References
```

正式：

```text
Runtime Presentation
!= One Giant State Enum
```

---

# 6. State 与 Reason 分离

State 回答：

> 当前处于什么状态？

Reason 回答：

> 为什么处于这个状态？

例如：

```text
State:
WAITING

Reason:
DEPENDENCY_NOT_READY
```

或：

```text
State:
BLOCKED

Reason:
PROJECT_GATE_HOLD
```

正式：

```text
State
!= Reason
```

---

# 7. Reason 与 Blocker 分离

Blocker 回答：

> 哪个实际条件阻止系统继续？

例如：

```text
State:
BLOCKED

Reason:
当前执行前置治理条件未满足

Blocker:
Project Gate = HOLD
```

Reason 是对当前情况的解释语义。

Blocker 是需要被解除、改变或重新解析的约束条件。

正式：

```text
Reason
!= Blocker

Human-readable Explanation
!= Blocker Truth
```

Reason / Blocker 的完整模型留给 F11-D05。

---

# 8. State 与 Recovery 分离

Runtime 出现失败事件后，系统可能已经自动进入 Recovery（恢复）。

例如：

```text
Attempt EA-01:
FAILED

Action:
RECOVERING
```

或：

```text
Action:
RUNNING

Recovery:
RETRY / FALLBACK ACTIVE
```

因此：

```text
Failure Event
!= Current Failure

Recovery In Progress
!= Final Failure
```

F11 不得因为历史 Attempt 失败，就把当前 Action 直接展示成 FAILED。

---

# 9. Historical Failure 与 Current Failure 分离

例如：

```text
Attempt 1 = FAILED
Attempt 2 = FAILED
Attempt 3 = RUNNING
```

当前展示应保持：

```text
Action:
RUNNING

Current Attempt:
RUNNING

Previous Attempts:
2 FAILED
```

不得压成：

```text
Action = FAILED
```

正式：

```text
Historical Failure
!= Current Failure

Failed Attempt
!= Current Action Failure

Attempt History
!= Action Current State
```

---

# 10. WAITING 的展示语义

WAITING 表示当前工作尚未继续，但并不自动代表错误、失败、暂停或人工介入。

例如：

```text
State:
WAITING

Reason:
Waiting for Action B

Expected Continuation:
自动继续
```

推荐的人类表达：

> 正在等待上游步骤完成。条件满足后系统将自动继续。

正式：

```text
WAITING
!= BLOCKED

WAITING
!= PAUSED

WAITING
!= FAILED

WAITING
!= Human Decision Required
```

---

# 11. BLOCKED 的展示语义

BLOCKED 表示存在当前阻止继续的条件。

但：

```text
BLOCKED
!= FAILED

BLOCKED
!= Human Decision Required
```

例如：

```text
State:
BLOCKED

Blocker:
Project Gate HOLD

Human Attention:
NONE
```

可以表达为：

> 当前被阻塞。系统正在等待相关 Gate 条件变化，目前无需人工决策。

只有真正存在独立的：

```text
Human Decision Required
```

时，才进入治理决策交互。

---

# 12. PAUSED 的展示语义

PAUSED 表示 Runtime 当前处于暂停状态。

F11 应允许同时表达：

```text
Pause Reason

Pause Source

Expected Continuation

Available Control Hint
```

例如：

```text
State:
PAUSED

Reason:
Explicit runtime control

Control Hint:
RESUME
```

但：

```text
PAUSED
!= Runtime Permission to Resume
```

真正 Resume 仍须进入 F10 Point-of-use Revalidation。

---

# 13. RECOVERING 的展示语义

当 Runtime 正在自动恢复时，F11 应优先表达：

> 系统正在自动恢复。

而不是：

> 执行失败。

正式：

```text
RECOVERING
!= FAILED

Recovery Active
!= Human Action Required
```

除非上游进一步明确：

```text
Human Attention Required
```

否则恢复过程不应默认升级为人工处理。

---

# 14. Runtime State 与 Human Attention 分离

F11-D02 正式区分：

```text
Runtime State

Human Attention Requirement
```

例如：

```text
WAITING
+
Attention NONE
```

表示：

> 系统自己等待。

```text
BLOCKED
+
Attention NONE
```

表示：

> 当前有 Blocker，但不需要人工处理。

```text
BLOCKED
+
Human Decision Required
```

才表示：

> 需要人类治理判断。

正式：

```text
Runtime State
!= Human Attention Requirement

Runtime State
!= Human Action Requirement

Runtime State
!= Human Decision Requirement

State Severity
!= Human Attention Severity
```

---

# 15. Expected Continuation

F11 允许展示 Expected Continuation（预期后续行为）。

它回答：

> 按当前规则，系统下一步预计怎么处理？

例如：

```text
automatic continue when dependency becomes ready

automatic recovery in progress

waiting for external governed condition

human decision required
```

Exact Enum 不在 D02 冻结。

正式：

```text
Expected Continuation
!= Guaranteed Outcome
```

F11 可以表达：

> 系统将尝试自动恢复。

不得无依据表达：

> 系统一定会恢复成功。

---

# 16. Control Hint 的定位

RuntimeProjection 可以携带当前可见的控制提示，例如：

```text
RETRY
RESUME
PAUSE
CANCEL
```

F11 可以将其映射为 Control Surface 中的交互入口。

但：

```text
Displayed Control Availability
!= Runtime Permission

Control Hint
!= Pre-authorized Action

Button Enabled
!= Permission Granted
```

真正受保护动作仍由 F10 在使用点重新验证。

---

# 17. UI Button State 不构成安全边界

Implementation 可以拥有：

```text
retryButtonEnabled = true
```

等前端状态。

但架构语义必须理解为：

```text
Button Presentation
derived from current Projection
```

不得理解成：

```text
Button Enabled
= authoritative permission truth
```

因此：

```text
UI Disabled
!= Security Boundary

UI Enabled
!= Runtime Permission
```

---

# 18. Progress 与 State 分离

Progress（进度）不是 Runtime State。

例如：

```text
State:
RUNNING

Progress:
600 / 1000
```

正式：

```text
State
!= Progress
```

F11 不因为：

```text
RUNNING
```

就自动推导一个百分比。

---

# 19. Progress 必须保留 Basis

任何 Progress 表达必须能够解释其依据。

例如：

```text
processed_items = 600
total_items = 1000
```

可以支持：

```text
60%
```

但：

```text
completed_actions = 3
total_actions = 5
```

只能够可靠表达：

```text
3 / 5 actions completed
```

并不自动等于：

```text
60% of work completed
```

正式：

```text
Progress Display
must preserve Progress Basis

Progress Value
without Progress Basis
is insufficient for trustworthy presentation

Action Count Ratio
!= Work Completion Percentage
```

---

# 20. ETA 不得无依据生成

F11 不得为了 UX 看起来更完整而伪造预计剩余时间。

正式：

```text
No Reliable Estimate
→ Do Not Fabricate ETA
```

只有存在受支持的时间估算 Basis 时，才允许展示 ETA。

---

# 21. Task / Action / Execution Attempt 展示层级

F11 必须继续保持：

```text
Task
!= Action
!= Execution Attempt
```

Task 表示更高层工作。

Action 表示可治理 / 可控制的业务或运行步骤。

Execution Attempt 表示某次具体执行发生。

不得为了 UI 简化统一压成：

```text
Job
Run
Operation
```

并丢失层级语义。

---

# 22. Authoritative Parent State 优先

如果真正 Runtime Owner 已明确提供：

```text
Task State
```

则 F11 应优先展示该权威状态。

同时可以补充：

```text
Child State Summary
```

例如：

```text
Task:
RUNNING

Children:
5 COMPLETED
2 RUNNING
1 WAITING
1 BLOCKED
```

这里：

```text
Task State
```

与：

```text
Child Summary
```

分别承担不同职责。

---

# 23. 无 Authoritative Parent State 时不得自行创造

如果上游没有提供正式 Task State，F11 不得根据 Child State 自行创建新的权威父状态。

允许：

```text
Derived Presentation Summary
```

例如：

> 当前 5 个步骤中，2 个已完成、1 个执行中、1 个等待、1 个失败。

但不得将其保存或解释为新的：

```text
Task Runtime State
```

正式：

```text
Child State Aggregation
!= Authoritative Parent State

Derived Aggregate Summary
!= Domain State Truth
```

---

# 24. 不创造组合状态爆炸

F11-D02 禁止通过新增大量组合 State 来表达 Qualifier。

不推荐：

```text
RUNNING_WITH_BLOCKER

RUNNING_WITH_WAITING

RUNNING_WITH_RECOVERY

BLOCKED_WITH_RUNNING_CHILD

PARTIALLY_COMPLETED_WITH_WARNING
```

优先采用：

```text
State
+
Qualifiers
+
Summary
+
Attention
+
Recovery
```

正式：

```text
Do not encode every qualifier combination
into a new authoritative state.
```

---

# 25. “部分成功”不得无定义使用

如果：

```text
A1 = COMPLETED
A2 = COMPLETED
A3 = FAILED
```

F11 不默认创造：

```text
PARTIAL_SUCCESS
```

因为“部分成功”可能分别指：

```text
部分 Action 执行完成

部分业务结果被接受

部分 Canonical Apply 已完成
```

这些不是同一个概念。

因此：

```text
Descriptive Aggregation
preferred over invented evaluative aggregate state
```

优先表达：

> 3 个步骤中 2 个完成，1 个失败。

---

# 26. All Children Terminal 不等于 Parent Completed

即使所有 Child 都进入某种终态，也不能由 F11 自动推出：

```text
Parent = COMPLETED
```

例如：

```text
A1 COMPLETED
A2 COMPLETED
A3 CANCELLED
```

Task 的最终含义必须由真正 Owner / Workflow Contract 决定。

正式：

```text
All Children Terminal
!= Parent Completed
```

---

# 27. Attempt History 不替代 Action State

例如：

```text
Attempt 1 = FAILED
Attempt 2 = FAILED
Attempt 3 = COMPLETED
```

如果 Action 当前正式状态为：

```text
COMPLETED
```

F11 应表达：

```text
Action:
COMPLETED

Attempt History:
FAILED
FAILED
COMPLETED
```

而不是：

```text
Action:
PARTIAL_SUCCESS
```

正式：

```text
Attempt History
!= Action Current State
```

---

# 28. Attempt / Action / Task Terminality 分离

Terminal State（终态）必须限定到对应生命周期对象。

正式：

```text
Attempt Terminality
!= Action Terminality

Action Terminality
!= Task Terminality
```

失败的 Attempt 后仍可能 Retry。

Action 结束后 Task 仍可能有其他 Action。

Task 的终结语义也不能从某一个 Action 推导。

---

# 29. Terminal State 与 Result 分离

Terminal State 回答：

> 这个生命周期对象是否结束。

Result 回答：

> Runtime 产生了什么结果。

正式：

```text
Terminal State
!= Result
```

例如：

```text
Execution Attempt:
COMPLETED

Result:
DesignPackageCandidate v3
```

“完成”不等于“结果已被接受”。

---

# 30. Result 与 Acceptance 分离

正式：

```text
Result Produced
!= Result Accepted

Result
!= Acceptance
```

Runtime 产生结果后，后续可能仍存在：

```text
Validation

Human Decision

Approval

Apply Authorization

Canonical Apply
```

因此 F11 不得将：

```text
Result Generated
```

展示成：

```text
Business Fully Completed
```

---

# 31. Execution Completion 与业务接受分离

正式：

```text
Execution Completed
!= Business Accepted

Execution Completed
!= Governance Approved

Execution Completed
!= Canonical Applied
```

例如：

```text
Patch Candidate:
generated

Validation:
PASS

Human Decision:
APPROVED

Apply Authorization:
VALID

Canonical Apply:
PENDING
```

适合展示为：

> 修改方案已生成并通过验证，已经批准，但尚未正式应用。

不得直接简化为：

> 修改成功。

---

# 32. Outcome 必须 Domain-qualified

如果系统后续使用 Outcome 概念，必须明确其 Domain。

例如：

```text
Runtime Outcome

Validation Outcome

Governance Outcome

Apply Outcome
```

不得创建一个全局：

```text
Outcome = SUCCESS
```

覆盖全部含义。

正式：

```text
Outcome
must remain Domain-qualified
```

D02 不建立新的 Outcome Core Object。

更详细 Result / Outcome 模型留给 F11-D06。

---

# 33. COMPLETED 不自动等于“成功”

如果上游正式语义是：

```text
COMPLETED
```

F11 应根据实际含义表达：

> 执行完成。

不得无依据提升为：

> 全部成功。

正式：

```text
Completed
!= Business Success by default
```

---

# 34. CANCELLED / SKIPPED 与 FAILED 分离

合法 Workflow 可能存在：

```text
CANCELLED
SKIPPED
REPLACED
INVALIDATED
```

等状态或结果。

具体 Enum 由对应 Owner 决定。

F11 必须保持：

```text
Cancelled
!= Failed

Skipped
!= Failed

Not Completed
!= Failed
```

不能仅因某 Action 未执行至 COMPLETED 就显示为失败。

---

# 35. No Result 与 Failure 分离

正式：

```text
No Result
!= Failure

Result Exists
!= Success
```

RUNNING Action 尚未产生 Result 是正常情况。

CANCELLED Action 可能合法地没有业务 Result。

Result 的存在也不表示已经通过 Validation 或被接受。

---

# 36. No Active Action 不等于 Task Completed

如果：

```text
当前没有 Active Action
```

其原因可能是：

```text
尚未开始

等待 Workflow Resolution

等待外部条件

Not Applicable

Task 已结束
```

因此：

```text
No Active Action
!= Task Completed
```

F11 不自行推断。

---

# 37. Historical State 与 Current State 分离

F11 应明确区分：

```text
Current State

Historical State
```

例如历史：

```text
14:01 FAILED
14:02 RECOVERING
14:03 RUNNING
14:10 COMPLETED
```

当前：

```text
COMPLETED
```

正式：

```text
Historical State
!= Current State

Historical Failure
!= Current Failure
```

---

# 38. Latest Known 与 Current Confirmed 分离

如果当前 Source 暂时无法重新确认状态，但最近一次观察结果是：

```text
RUNNING
```

F11 应表达：

> 最近一次已知状态：执行中。当前状态正在重新确认。

不得无提示直接表达：

> 正在执行。

正式：

```text
Latest Known
!= Current Confirmed
```

---

# 39. Stale Projection 不等于 Runtime Failure

如果 Projection 已无法确认仍然有效：

```text
Projection = STALE
```

这说明：

> 当前投影可能已经过时。

不说明：

```text
Runtime = FAILED
```

正式：

```text
Stale Projection
!= Failed Runtime
```

---

# 40. Observation / Freshness Semantics

RuntimeProjection 在逻辑上必须能够表达：

```text
当前是否已确认

是否为 Latest Known

是否正在 Refresh

是否已经 Stale

Current Basis 是否暂不可用
```

Exact Enum 留待后续。

F11-D02 不采用无治理依据的：

```text
confidence = 83%
```

等 AI 概率表达。

优先使用确定性 Freshness / Observation 语义。

---

# 41. 不要求绝对实时同步

F11-D02 不要求 Control Plane 与 Runtime 达到绝对零延迟同步。

正式：

```text
Perfect Real-time Synchrony
is not required.

Truthful Freshness Semantics
is required.
```

即：

> 可以存在观察延迟，但不能把旧信息冒充成当前已确认事实。

---

# 42. Projection Snapshot

F11 可以把某次 RuntimeProjection 理解为：

```text
Projection Snapshot
```

但：

```text
Snapshot
!= Eternal Truth
```

F10→F11 已明确：

```text
UI State Snapshot != Eternal Runtime State
```

---

# 43. 断线后的 Current Projection Recovery

Control Surface 断线重连后，F11 应优先恢复：

```text
Current Projection
```

回答：

> 现在是什么状态？

不要求先重放断线期间的所有 Runtime Event。

正式：

```text
Current State Recovery
!= Complete Historical Replay
```

---

# 44. Current Recovery 与 History Recovery 分离

断线重连后的两个问题分别处理：

```text
现在是什么？
→ Current Projection Recovery

断线期间发生了什么？
→ Trace / History Recovery
```

因此：

```text
State Recovery
!= Mandatory Event Replay
```

这允许：

```text
Current Projection first
History on demand
```

符合 Purpose-sensitive Minimum Sufficient Context 原则。

---

# 45. Observed Projection Transition 不等于完整 Runtime History

例如页面观察到：

```text
Snapshot 1:
WAITING

Snapshot 2:
COMPLETED
```

不能自动推断 Runtime 真正直接发生：

```text
WAITING → COMPLETED
```

中间可能实际存在：

```text
RUNNING
RECOVERING
```

等状态，只是 F11 没观察到。

正式：

```text
Observed Projection Transition
!= Complete Runtime Transition History

Projection Delta
!= Trace
```

要回答完整历史，必须进入 Trace / History。

---

# 46. Pre-submit Refresh 与 Runtime Revalidation 分离

对于高影响 Control Interaction，F11 可以在提交前主动 Refresh 当前 Projection。

但：

```text
Pre-submit Refresh
!= Point-of-use Revalidation
```

即使 F11 刚刚刷新，Runtime 在真正使用 Control Intent 前仍可能发生变化。

因此最终保护仍由 F10 执行。

---

# 47. Freshness Expectation 可以按 Purpose 不同

不同 Projection Purpose 可以拥有不同 Freshness 要求。

例如：

```text
CONTROL
→ currentness requirement stronger

SUMMARY
→ moderate freshness

AUDIT
→ historical basis
```

但 D02 不冻结：

```text
Polling Interval

WebSocket Protocol

SSE

Refresh Timer
```

正式只冻结：

```text
Freshness Expectation
may vary by Purpose.
```

---

# 48. 多 Surface 一致性

Web / CLI / IDE / API / Mobile 可以拥有不同展示密度。

例如同一状态：

Web：

> 正在自动恢复，无需操作。

CLI：

```text
A17 RECOVERING
attention=none
```

IDE：

```text
Recovering
```

均可。

但必须保持：

```text
Presentation Density may differ.

Core State Semantics may not diverge.
```

不得出现同一已确认 Projection：

```text
Web = FAILED

CLI = RUNNING

IDE = HUMAN DECISION REQUIRED
```

却没有对应不同 Basis 的情况。

---

# 49. 信息展示优先级

F11 Runtime Presentation 应优先回答：

```text
现在发生什么？

是否需要我处理？

为什么？

系统下一步会做什么？

我现在能表达哪些控制意图？

依据是什么？
```

这是 Governance UX 的信息优先级。

不要求把所有底层字段一次性展示。

---

# 50. Progressive Disclosure

F11 推荐使用 Progressive Disclosure（渐进展开）。

第一层：

```text
当前状态
是否需要人
简要原因
```

第二层：

```text
Blocker
Recovery
Progress
Domain Qualifiers
Expected Continuation
```

第三层：

```text
Evidence
Trace
Provenance
Authority References
```

具体 UI Layout 留给 Implementation。

---

# 51. Less Detail 不得损失 Governing Meaning

允许：

```text
Less Detail
```

但禁止：

```text
Less Governing Meaning
```

例如真实情况：

```text
Runtime COMPLETED
Canonical Apply PENDING
```

可以简化成：

> 已生成，尚未正式应用。

不能简化成：

> 已完成。

如果这种表达会让用户理解成正式 Apply 已完成。

---

# 52. Multi-domain Qualifier Presentation

RuntimeProjection 可以展示多个 Domain 的相关限定信息，例如：

```text
Runtime:
BLOCKED

Apply Authorization:
VALID

Project Gate:
HOLD
```

F11 可以生成：

> 当前运行被项目 Gate HOLD 阻止，现有 Apply Authorization 仍然有效。

但：

```text
Multi-domain Presentation
!= Authority Merge
```

不得生成新的：

```text
GLOBAL_AUTHORIZED
GLOBAL_BLOCKED
GLOBAL_SAFE
```

作为权威状态。

---

# 53. Qualifier 必须 Basis-backed

F11 展示：

```text
degraded
warning
blocked
risk
```

等 Qualifier 时，必须存在受支持 Basis。

正式：

```text
Presentation Qualifier
must remain Basis-backed.
```

若上游没有定义 Provider 已经处于：

```text
DEGRADED
```

F11 不得自行因为“感觉慢”就创造该状态。

---

# 54. Presentation Derivation 为单向 UX 派生

F11 可以：

```text
Domain Facts
→ Presentation Summary
```

但不得：

```text
Presentation Summary
→ mutate Domain State
```

正式：

```text
Presentation Derivation
!= Domain State Mutation
```

任何 Runtime / Governance 状态变化必须通过对应正式 Interaction / Domain Contract 完成。

---

# 55. Badge / Color / Icon 不是 Authority

未来 UI 可以使用：

```text
颜色
图标
Badge
动画
排序
强调级别
```

但：

```text
Color
!= State Semantics

Badge
!= Runtime State

Visual Success
!= Governance Approval

Presentation Priority
!= Domain Priority
```

CLI 即使没有颜色，也必须能够保留核心语义。

---

# 56. AI Presentation Summary

F11 可以使用 AI 生成更自然的人类说明。

例如：

> 当前任务大部分步骤已完成，还有一个步骤等待依赖，暂时无需人工操作。

但必须有事实 Basis，例如：

```text
5 Completed
1 Waiting
Attention NONE
```

正式：

```text
AI Presentation Summary
must remain Fact-backed.
```

如果信息不足，应表达不确定性，而不是补猜。

---

# 57. D02 与 D03 的边界

D02 只定义：

```text
Control Hint 如何展示

Control Hint != Runtime Permission
```

以下内容由 F11-D03 负责：

```text
Control Intent lifecycle

Point-of-use Revalidation handoff

Duplicate delivery

NO_LONGER_APPLICABLE

Retry / Resume / Pause / Cancel routing
```

---

# 58. D02 与 D04 的边界

D02 只定义：

```text
Human Decision Requirement
must be independently presentable
```

以及：

```text
BLOCKED
!= Human Decision Required
```

具体：

```text
Decision Context
Alternative Presentation
Human Decision Input
Decision Evidence
```

由 F11-D04 负责。

---

# 59. D02 与 D05 的边界

D02 只冻结：

```text
State
!= Reason

Reason
!= Blocker

Reason / Blocker must remain independently representable
```

具体：

```text
Reason taxonomy

Primary / Secondary Reason

Root Cause

Immediate Cause

Multiple Blockers

Explanation hierarchy
```

由 F11-D05 负责。

---

# 60. D02 与 D06 的边界

D02 只冻结：

```text
Terminal State
!= Result

Result
!= Evidence

Evidence
!= Trace

Result
!= Acceptance
```

具体：

```text
Result Presentation

Evidence Navigation

Trace Timeline

Provenance Presentation

Attempt / Result History
```

由 F11-D06 负责。

---

# 61. D02 与 D07 的边界

D02 只冻结：

```text
Runtime State
!= Human Attention Requirement

Attention must be independently presentable.
```

具体：

```text
Notification severity

Human Attention policy

Deduplication

Notification merge

Inbox

Push

SLA
```

由 F11-D07 负责。

---

# 62. D02 与 D08 的边界

D02 冻结：

```text
Latest Known
!= Current Confirmed

Surface presentation semantics must remain consistent
```

而：

```text
Reconnect Protocol

Delivery Consistency

Cross-surface interaction continuity

Session recovery

Duplicate delivery transport behavior
```

留给 F11-D08。

---

# 63. F11-D02 核心不变量

正式冻结：

```text
Presentation State
!= Runtime State Truth

Presentation Mapping
!= New Runtime State Machine

State
!= Reason

Reason
!= Blocker

State
!= Recovery

State
!= Progress

State
!= Human Attention Requirement

State
!= Human Decision Requirement

State
!= Control Availability

WAITING
!= BLOCKED

WAITING
!= FAILED

WAITING
!= PAUSED

BLOCKED
!= FAILED

Recovery In Progress
!= Final Failure

Failure Event
!= Current Failure

Historical Failure
!= Current Failure

Failed Attempt
!= Current Action Failure

Control Hint
!= Runtime Permission

Button Enabled
!= Permission Granted

Progress Value
must remain Basis-interpretable

Action Count Ratio
!= Work Completion Percentage

No Reliable Estimate
→ No Fabricated ETA

Child State Aggregation
!= Authoritative Parent State

Derived Aggregate Summary
!= Domain State Truth

All Children Terminal
!= Parent Completed

Attempt History
!= Action Current State

Attempt Terminality
!= Action Terminality

Action Terminality
!= Task Terminality

Terminal State
!= Result

Result Produced
!= Result Accepted

Execution Completed
!= Business Accepted

Execution Completed
!= Governance Approved

Execution Completed
!= Canonical Applied

Completed
!= Business Success by default

Skipped
!= Failed

Cancelled
!= Failed

Not Completed
!= Failed

No Result
!= Failure

Result Exists
!= Success

No Active Action
!= Task Completed

Outcome
must remain Domain-qualified

Historical State
!= Current State

Latest Known
!= Current Confirmed

Stale Projection
!= Failed Runtime

Expected Continuation
!= Guaranteed Outcome

Current State Recovery
!= Complete Historical Replay

State Recovery
!= Mandatory Event Replay

Observed Projection Transition
!= Complete Runtime Transition History

Projection Delta
!= Trace

Pre-submit Refresh
!= Point-of-use Revalidation

Freshness Expectation
may vary by Purpose

Presentation Qualifier
must remain Basis-backed

Presentation Derivation
!= Domain State Mutation

Badge / Color / Summary
!= Authority

Presentation Priority
!= Domain Priority

Visual Success
!= Governance Approval

AI Presentation Summary
must remain Fact-backed

Less Detail
!= Less Governing Meaning

Presentation Density may vary by Surface

Core Presentation Semantics
may not diverge by Surface
```

---

# 64. Explicitly Forbidden Designs

F11-D02 明确禁止将以下方式提升为正式架构：

```text
F11-owned replacement Runtime State Machine

Universal UI State used as Runtime truth

WAITING displayed as FAILED by default

BLOCKED interpreted as Human Decision Required by default

Historical Attempt failure used as current Action failure

Every qualifier combination encoded as new state

Child-state aggregation used as parent authority state

Action-count ratio presented as work percentage without basis

Fabricated ETA

Stale snapshot presented as confirmed current truth

Projection delta treated as complete Runtime trace

UI refresh treated as Runtime revalidation

Button enabled state treated as permission

Runtime COMPLETED treated as Canonical Apply completed

Result existence treated as business success

Green visual state treated as governance approval

Cancelled / Skipped treated as failure by default

Cross-domain facts compressed into new F11 Global Authority State

AI-generated qualifier without supporting basis
```

---

# 65. Deferred

F11-D02 不冻结：

```text
Exact Runtime State Enum

Exact Presentation State Enum

Exact Reason Enum

Exact Blocker Enum

Exact Recovery Enum

Exact Attention Enum

Exact Control Hint Enum

Exact Freshness Enum

Exact Progress Schema

Exact ETA Algorithm

Exact Task Summary Formula

Exact Outcome Schema

Exact UI Colors

Exact Badge Styles

Exact Icons

Exact Component Layout

Exact Page Structure

Exact Refresh Interval

Polling

WebSocket

SSE

Push Protocol

Exact Cache Strategy

Exact API Contract

Exact DTO Schema

Exact Go Struct

Exact TypeScript Interface

Database

SQLite Physical Schema

Frontend Store Design
```

---

# 66. 与后续 F11 Decisions 的关系

F11-D02 建立状态展示基础。

后续：

```text
F11-D03
细化 Control Intent 与 Point-of-use Revalidation

F11-D04
细化 Human Decision UX

F11-D05
细化 Reason / Blocker / Explanation

F11-D06
细化 Result / Trace / Evidence / Provenance

F11-D07
细化 Notification / Human Attention

F11-D08
细化 Multi-Surface / Session / Delivery Consistency
```

后续 Decision 可以扩充 D02 的某个维度，但不得重新合并本稿已经拆开的 State、Reason、Result、Attention、Authority 等语义。

---

# 67. Approval Effect

本稿已经明确：

```text
F11-D02 HUMAN_APPROVED
```

因此正式冻结：

```text
Runtime state presentation boundary

Task / Action / Attempt presentation hierarchy

Authoritative State vs Derived Summary boundary

State / Reason / Blocker / Recovery separation

State / Progress separation

State / Human Attention separation

Control Hint / Runtime Permission separation

Progress Basis requirement

Current / Latest Known / Stale semantics

Projection Snapshot semantics

Reconnect current-state recovery boundary

Projection Delta / Trace boundary

Terminal State / Result / Acceptance separation

Execution / Governance / Canonical Apply separation

Multi-domain qualifier presentation boundary

Cross-surface semantic consistency

Presentation simplification governance
```

但不代表：

```text
Runtime State Enum Frozen

Reason Enum Frozen

UI Layout Frozen

Color System Frozen

API Frozen

Transport Frozen

Polling Strategy Frozen

WebSocket Strategy Frozen

Database Frozen

SQLite Schema Frozen

Implementation Authorized

RP2 Authorized

Authority Cutover Authorized

Canonical Replacement Authorized

Final Activation Authorized
```

---

# 68. Final Frozen Decision

```text
F11-D02
— Runtime Projection & State Presentation

STATUS:
HUMAN_APPROVED / FROZEN

F11 presents Runtime state
without becoming Runtime truth owner.

Authoritative State remains separate from
Presentation Summary.

Task / Action / Execution Attempt remain distinct.

State remains separate from:
Reason
Blocker
Recovery
Progress
Attention
Control Hint
Result
Acceptance.

WAITING is not BLOCKED or FAILED.

BLOCKED does not automatically require human action.

Recovery in progress is not final failure.

Historical Attempt failure does not override
current recovered Action state.

Task child aggregation may produce descriptive
presentation summaries,
but not new authoritative parent state.

Progress requires interpretable basis.

F11 does not fabricate percentages or ETA.

Latest Known is not Current Confirmed.

Stale Projection is not Runtime Failure.

Reconnect recovers current state first;
full history remains on-demand.

Observed Projection transitions are not
complete Runtime transition history.

Control-surface refresh never replaces
F10 Point-of-use Revalidation.

Terminal State is not Result.

Result Produced is not Result Accepted.

Runtime Completion is not Governance Approval
and is not Canonical Apply Completion.

Multi-domain facts may be composed for presentation,
but presentation does not merge authority.

Presentation may be simplified,
but governing meaning may not be lost.

Implementation remains NOT_AUTHORIZED.
```

---

**END OF F11-D02 HUMAN_APPROVED FREEZE**

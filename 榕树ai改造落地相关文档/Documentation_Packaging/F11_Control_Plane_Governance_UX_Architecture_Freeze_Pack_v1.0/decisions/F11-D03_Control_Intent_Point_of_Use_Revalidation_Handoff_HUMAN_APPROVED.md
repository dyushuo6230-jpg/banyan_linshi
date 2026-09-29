# F11-D03 — Control Intent & Point-of-use Revalidation Handoff
## 控制意图与使用点再验证交接

**Stage：** F11 — Control Plane / Governance UX Architecture（控制面 / 治理交互架构）  
**Decision ID：** F11-D03  
**Upstream Gate：** F11-G01 = HUMAN_APPROVED / FROZEN  
**Upstream Decision：** F11-D01 = HUMAN_APPROVED / FROZEN  
**Upstream Decision：** F11-D02 = HUMAN_APPROVED / FROZEN  
**Status：** HUMAN_APPROVED / FROZEN  

**Implementation Authorization：** NO  
**RP2 Authorization：** NO  
**Authority Cutover Authorization：** NO  
**Canonical Replacement Authorization：** NO  
**Final Activation Authorization：** NO  
**Legacy Retirement Authorization：** NO  

---

# 1. 决策目标

F11-D03 用于冻结：

```text
Control Hint 如何变成明确 RuntimeControlIntent；

F11 在该过程中负责什么；

F10 何时以及如何重新验证；

旧 Projection / 旧按钮 / 旧 Authorization
为什么不能直接成为当前 Runtime Permission；

Retry / Resume / Pause / Cancel
怎样保持各自语义；

Scope / Authority / Gate / Provider
发生变化时如何处理；

多 Surface、重复投递、网络超时、
F11/F10 重启时怎样避免重复 Runtime 后果；

Control Intent 什么时候应停止自动执行，
并转入治理解析 / Human Decision；

以及 Control Intent 的反馈怎样最终回归
Current RuntimeProjection。
```

---

# 2. 核心责任边界

F11-D03 正式采用：

```text
F11
= Express / Capture / Correlate / Route / Present

F10
= Revalidate / Resolve / Permit / Route Runtime /
  Create Execution Consequence
```

F11 不拥有：

```text
Runtime Permission
Runtime Provider Resolution
Adapter Routing
Execution Attempt Lifecycle
```

这些仍属于 F10。

---

# 3. 控制主链

正式逻辑责任链：

```text
RuntimeProjection
↓
Control Hint
↓
Origin expresses explicit RuntimeControlIntent
↓
F11 Capture
↓
F11 Routing / Correlation
↓
F10 Point-of-use Revalidation
↓
F10 Resolution
↓
if currently valid and execution is required
Runtime Consequence
↓
Execution Attempt / Result / Trace
↓
new RuntimeProjection
↓
F11 Presentation
```

该链描述的是：

```text
Responsibility Semantics
```

不是固定 Transport / API 调用顺序。

---

# 4. Control Hint 与 Control Intent 分离

F11-D02 已冻结 Control Hint 只是当前 Projection 下可展示的控制入口。

因此：

```text
Control Hint
!= Control Intent
```

例如：

```text
UI shows [Retry]
```

不表示 RuntimeControlIntent 已存在。

只有 Origin 明确表达：

```text
Retry A17
```

后才形成新的 Logical Intent。

---

# 5. Control Intent 与 Runtime Permission 分离

正式继承 F10：

```text
Control Request
!= Runtime Permission
```

因此：

```text
RuntimeControlIntent
!= Runtime Permission

RuntimeControlIntent
!= Authorization

RuntimeControlIntent
!= Execution Attempt
```

---

# 6. Control Intent 表达目标语义，不表达底层执行配方

RuntimeControlIntent 表达：

```text
PAUSE target
RESUME target
RETRY target
CANCEL target
```

等控制意义。

不得默认表达：

```text
Use Provider A
Use Adapter X
Call command Y
Restore old process directly
```

因此：

```text
Control Intent
= Desired Runtime Control Meaning

Control Intent
!= Provider Choice

Control Intent
!= Adapter Choice

Control Intent
!= Execution Recipe
```

Provider / Adapter / Runtime Execution Context 仍由 F10 根据当前规则解析。

---

# 7. Control Intent 的基本逻辑信息

F11-D03 不冻结 Exact Schema，但要求 Control Intent 逻辑上能够保持：

```text
Stable Logical Identity

Origin

Target / Subject

Intent Meaning

Observed Basis

Correlation

Relevant Scope / Context References
where needed
```

这些信息用于：

```text
interpretability
deduplication
routing
revalidation
recovery
correlation
```

而不是授权。

---

# 8. Observed Basis

Control Intent 应能够保持：

> Origin 是在什么观察上下文下表达该控制意图的。

例如：

```text
Intent:
RETRY A17

Observed:
A17 = FAILED
```

如果 F10 真正使用时：

```text
A17 = RUNNING
```

则 Retry 可能已经不再适用。

正式：

```text
Observed Basis
!= Runtime Permission
```

---

# 9. Point-of-use Revalidation

Point-of-use Revalidation（使用点再验证）定义为：

> 在受保护 Runtime 行为真正准备被消费 / 执行时，根据当前有效事实重新判断该 Intent 的适用性、权限和治理条件。

它不是：

```text
用户点击按钮时检查一次
```

也不是：

```text
前端刚 Refresh 过就永久有效
```

正式：

```text
Point-of-use Revalidation
occurs at protected use,
not merely at UI click time.
```

---

# 10. Pre-submit Refresh 不能替代 Revalidation

F11 可以在高影响 Control Intent 提交前刷新 Projection。

但：

```text
Pre-submit Refresh
!= Point-of-use Revalidation
```

因为 Refresh 与真正 Runtime Use 之间状态仍可能改变。

---

# 11. Revalidation 的最小语义范围

D03 不重新定义 F10 Permission Algorithm。

但 Current Revalidation 逻辑上可重新确认：

```text
Target 是否仍有效

Current Runtime State 是否仍适用

Scope 是否仍成立

Authorization / Authority Basis 是否仍有效

Gate 是否仍允许

是否已存在等价处理

是否为 Duplicate Delivery

是否已经被另一 Interaction 改变

是否需要重新进行 Provider / Adapter / Runtime resolution
```

---

# 12. 比例化 Revalidation

所有 Protected Control Intent 都必须重新验证。

但验证范围可以按照：

```text
Intent Meaning

Target State

Scope

Authority

Gate

Potential Runtime Consequence
```

决定。

正式：

```text
Every Protected Control Intent
requires Point-of-use Revalidation.

Revalidation Scope
may depend on Intent meaning
and governed consequence.
```

---

# 13. 更严格验证不等于全系统重算

正式：

```text
Stronger Revalidation
!= Full Architecture Recompute
```

高影响 Control 也应采用：

```text
Purpose-sensitive
Minimum Sufficient
Current Revalidation
```

而不是重新扫描或执行整个 F1-F10。

---

# 14. Retry 语义

Retry 表示：

> 对当前同一 Runtime Action 重新尝试完成其既有语义。

正式：

```text
Retry
!= New Business Action
```

Retry 允许产生：

```text
new Execution Attempt
```

但不自动创建新的 Business Action。

---

# 15. Retry Revalidation

Retry 可重点重新确认：

```text
Action 是否仍存在

当前是否仍处于可 Retry 状态

是否已经自动 Recovery

是否已经由其他 Surface Retry

Scope 是否仍适用

Authorization 是否仍有效

Gate 是否允许

Runtime Execution Context 是否需要重新解析
```

Current Applicability 是 Retry 的一等语义。

---

# 16. Resume 语义

Resume 表示：

> 希望当前被暂停的 Runtime 工作重新进入合法推进过程。

但：

```text
Resume
!= Blind Continue
```

Resume 必须基于 Current Context 重新解析。

---

# 17. Pause Snapshot 不等于 Resume Permission

暂停时记录的：

```text
Provider
Scope
Authorization
Gate
Execution Context
```

不能被当作未来 Resume 时永久有效。

正式：

```text
Pause Snapshot
!= Resume Permission
```

Resume 时必须以当前事实重新判断。

---

# 18. Pause 语义

Pause 表示：

> 希望当前可暂停 Runtime 工作停止继续推进。

是否可以实际暂停取决于 Use-time Runtime 状态。

因此：

```text
Displayed Pause Hint
!= Guaranteed Pause Capability
```

Target 可能已经：

```text
Completed
Already Paused
Entered non-interruptible phase
```

最终由 F10 判断。

---

# 19. Cancel 语义

Cancel 通常可能产生更高影响：

```text
terminate execution
affect downstream scheduling
trigger cleanup / compensation
```

因此允许：

```text
higher-impact control
→ proportionally stronger revalidation
```

但 D03 不冻结：

```text
Cancel 永远需要二次人工确认
```

是否需要确认由后续 UX / Domain Policy 决定。

---

# 20. UI Confirmation 与 Runtime Permission 分离

即使 UI 出现：

```text
“确定取消吗？”
```

并由用户确认，

也只表示：

```text
Interaction Confirmation
```

而不是：

```text
Runtime Permission
```

正式：

```text
UI Confirmation
!= Runtime Permission
```

---

# 21. Scope 变化

RuntimeControlIntent 只授权其原有治理语义下的控制请求。

正式：

```text
Control Intent
!= Scope Expansion Approval
```

例如：

```text
Retry tenant-admin Action
```

不得静默解释为：

```text
同时批准修改 shared component
和 platform-admin
```

---

# 22. Material Scope Expansion

若 Revalidation 发现：

```text
Material Scope Expansion
```

则原 Control Intent 不得自动跨越该边界。

正确方向：

```text
Runtime Control
↓
Material Scope Expansion detected
↓
protected execution stops
↓
Governance Resolution
↓
Human Decision if genuinely required
↓
new / updated valid basis
↓
current runtime re-resolution
```

正式：

```text
Control Intent
cannot absorb Material Scope Expansion.
```

---

# 23. Authority 的使用点语义

Intent 创建时有效的 Authority 不保证使用时仍有效。

正式：

```text
Intent Creation-time Authority
!= Use-time Authority
```

因此：

```text
old Authorization
```

不能因为曾经 VALID 就被永久复用。

---

# 24. Authority Changed 不自动等于 Human Decision

如果 Authority Basis 变化：

```text
Authority Changed
```

系统应优先：

```text
re-resolve
apply existing authority rules
recover automatically where deterministic
```

因此：

```text
Authority Changed
!= Human Decision Required
```

只有真正出现未解决 Governance Judgment Gap 时才升级。

---

# 25. Authority Conflict

若出现多个同时有效且互相冲突的 Authority，而既有规则无法唯一决定：

```text
Authority Conflict
```

普通 Control Intent 不得自行解决。

正式：

```text
Resume
!= Authority Conflict Resolution

Retry
!= Authority Conflict Resolution

Runtime Control Intent
must not resolve unresolved Authority Conflict.
```

---

# 26. Gate 边界

明确的用户 Runtime Control 不得突破已有 Gate。

正式：

```text
Explicit User Control
!= Gate Override

Explicit Control Intent
!= Governed Exception
```

例如：

```text
Safety Gate = HOLD
```

用户点击 Resume 不自动解除 HOLD。

---

# 27. Provider 变化

正常 Control Intent 表达：

```text
Retry A17
```

而不是：

```text
Retry A17 using Provider A
```

因此只要：

```text
Semantic Intent unchanged
Scope unchanged
Governance rules satisfied
```

F10 可以重新解析 Provider。

正式：

```text
Provider Change
!= New Control Intent by default

Provider Re-resolution
!= Human Decision by default
```

---

# 28. Runtime 变化与 Intent 失效分离

任何状态变化不自动导致 Intent 失效。

正式：

```text
Any State Change
!= Intent Invalidation
```

例如：

```text
Provider revision changed
Projection revision changed
internal node changed
```

在语义仍适用时，可以继续解析。

但：

```text
Material Applicability Change
```

可使 Intent：

```text
No Longer Applicable
Blocked
Re-routed
Governance Escalated
```

---

# 29. Resolution 不采用单一 ALLOW / DENY

D03 不冻结 Exact Resolution Enum。

但必须允许区分：

```text
Applicable / Accept for processing

Blocked / Rejected

No Longer Applicable

Duplicate / Already Handled

Re-resolution Required

Governance Resolution Required
```

不同 Resolution 不得全部压成：

```text
Permission Denied
```

---

# 30. NO_LONGER_APPLICABLE

例如：

```text
User observed:
A17 FAILED

User sends:
RETRY

Current:
A17 RUNNING
```

该 Retry 已不再适用。

正式：

```text
No Longer Applicable
!= Permission Denied

No Longer Applicable
!= Runtime Failure

No Longer Applicable
!= System Error
```

这是正常并发状态变化结果。

---

# 31. Duplicate Delivery

同一个 Stable Intent 被重复发送：

```text
CI-100
CI-100
```

属于：

```text
Duplicate Delivery
```

而不是：

```text
New Intent
```

正式继续继承：

```text
Duplicate Delivery
!= New Intent
```

---

# 32. New Explicit Intent

第一次 Retry 后再次失败，用户明确重新 Retry：

```text
CI-101
```

属于新 Intent。

正式：

```text
New Explicit Intent
!= Revision of Old Intent by default
```

---

# 33. Material Intent Change

例如：

```text
RETRY
```

改成：

```text
CANCEL
```

通常应理解为：

```text
New Intent
```

而不是旧 Intent Revision。

正式：

```text
Material Intent Change
→ New Intent by default
```

---

# 34. Stable Identity 与并发安全

Stable Interaction ID 可用于：

```text
deduplication
correlation
recovery
```

但不能单独解决并发。

正式：

```text
Stable Interaction Identity
!= Concurrency Safety by itself
```

真正并发安全仍依赖 Use-time Current Revalidation。

---

# 35. 多 Surface 独立 Intent

Web：

```text
CI-100 RETRY A17
```

IDE：

```text
CI-200 RETRY A17
```

是两个独立逻辑 Intent。

它们看起来都合理，并不代表：

```text
应该创建两个 Execution Attempt
```

正式：

```text
Two Valid-looking Intents
!= Two Authorized Runtime Consequences
```

---

# 36. Concurrent Control Processing

并发处理必须保持：

```text
Point-of-use State Validity
```

例如第一个 Retry 使 Action 进入 RUNNING 后，第二个 Retry 再验证时应基于 RUNNING 判断。

正式：

```text
Concurrent Control Processing
must preserve Point-of-use State Validity.
```

---

# 37. D03 不冻结并发实现技术

D03 不规定：

```text
mutex
database transaction
distributed lock
CAS
single writer
event sequencing
```

这些属于 Implementation。

架构只冻结最终语义要求。

---

# 38. Delivery 与 Runtime Consequence 分离

正式：

```text
Delivery Semantics
!= Runtime Consequence Semantics
```

D03 不冻结：

```text
exactly-once delivery
at-least-once delivery
at-most-once transport
```

但要求：

```text
Duplicate Delivery
must not silently become
Duplicate Authorized Runtime Consequence.
```

---

# 39. Delivery Count 与 Attempt Count 分离

同一 Intent 的多个 Transport Delivery 可以最终只关联一个 Runtime 后果。

因此：

```text
Delivery Count
!= Execution Attempt Count

Processing Invocation Count
!= Runtime Consequence Count
```

---

# 40. Transport Timeout

网络超时只说明：

> 当前发送方没有获得可靠确认。

不说明：

```text
Intent 未收到
Intent 已失败
Runtime 已失败
```

正式：

```text
Transport Timeout
!= Control Intent Failure

Transport Timeout
!= Runtime Failure
```

---

# 41. Transport Retry

如果只是同一逻辑 Submission 的传输重试：

```text
Transport Retry
```

应保留同一 Logical Intent Identity。

正式：

```text
Transport Retry
should preserve Logical Intent Identity
for the same submission.
```

不得因为网络超时自动制造：

```text
new explicit control intent
```

---

# 42. Unknown Submission Outcome

如果发送方当前不知道：

```text
Intent 是否已经被接收
```

应表达：

```text
Submission Outcome Unknown
```

而不是：

```text
Runtime Failed
```

正式：

```text
Unknown Submission Outcome
!= Runtime Failure
```

---

# 43. F11 重启

F11 重启不产生新的 RuntimeControlIntent。

正式：

```text
F11 Restart
!= New Control Intent
```

需要恢复的 Durable Intent / Correlation 可依据 D01 的 Durable-eligible 规则处理。

---

# 44. F10 重启与 Recovery Uncertainty

如果 F10 在：

```text
Intent received
```

与：

```text
Runtime consequence created
```

附近重启，

恢复时不得因为不确定就盲目再次执行。

正式：

```text
Recovery Uncertainty
must trigger State / Correlation Recovery
before protected re-execution.
```

以及：

```text
Recovery Uncertainty
!= Permission to Re-execute
```

---

# 45. Recovery Uncertainty 不等于 Human Decision

技术恢复不确定性首先进入：

```text
correlation recovery
state inspection
result inspection
trace inspection
deterministic re-resolution
```

正式：

```text
Recovery Uncertainty
!= Human Decision Required

Technical Uncertainty
!= Governance Judgment Gap
```

---

# 46. Control Plane 不确定性不得放大 Runtime 后果

正式：

```text
Control-plane Delivery Uncertainty
must not silently multiply
Protected Runtime Consequences.
```

F11/F10 重连、超时、重复处理不能因为 Control Plane 自己的不确定性静默产生额外受保护 Runtime 后果。

---

# 47. Automatic Runtime Recovery 不依赖 F11

F11 不是 Mandatory Runtime Hop。

因此：

```text
Automatic Runtime Recovery
does not require
synthetic Human Control Intent.
```

F10 自动：

```text
retry
fallback
recovery
```

可以依据自身已冻结 Runtime Contract 执行。

---

# 48. Automation-originated Intent

若外部 Automation 真实通过 F11 Control Surface 提交：

```text
PAUSE A17
```

可以形成：

```text
RuntimeControlIntent
origin = AUTOMATION
```

但：

```text
Automation-originated Intent
!= Human Intent

Automation-originated Intent
!= Human Governance Decision
```

---

# 49. Origin Surface 不拥有 Runtime Authority

Web / IDE / CLI / API 仅代表 Origin / Surface。

正式：

```text
Origin Surface
!= Runtime Control Authority
```

如果不同身份拥有不同控制能力，应来自：

```text
Identity
Scope
Authority
Governance rules
```

而不是因为：

```text
Web
IDE
CLI
```

本身拥有更高权限。

---

# 50. Interaction Lifecycle 与 Runtime Lifecycle 分离

F11 可以跟踪：

```text
Submission

Routing

Resolution visibility

Correlation
```

但这不是 Runtime Action State Machine。

正式：

```text
Interaction Lifecycle
!= Runtime Action Lifecycle

Control Interaction Tracking
!= Control Execution State Machine
```

---

# 51. Intent State 不使用 Runtime State 替代

例如：

```text
CI-100 RETRY
```

产生：

```text
EA-20 RUNNING
```

应表达：

```text
Intent:
resolved / correlated to EA-20

Attempt:
RUNNING
```

而不是：

```text
Intent = RUNNING
```

同样：

```text
EA-20 FAILED
```

不自动意味着：

```text
CI-100 FAILED
```

正式：

```text
Runtime Failure
!= Control Intent Failure
```

---

# 52. Intent Capture Failure 与 Resolution Block 分离

例如：

```text
malformed intent
missing target
cannot route
```

属于：

```text
Capture / Routing Failure
```

而：

```text
Gate HOLD
Authorization expired
No Longer Applicable
```

属于：

```text
Resolution outcome
```

正式：

```text
Intent Resolution
!= Interaction Capture Failure

Intent Resolution Block
!= Runtime Failure
```

---

# 53. F11 可以展示 F10 Resolution，但不拥有其 Truth

F11 可以记录或展示：

```text
Resolution:
NO_LONGER_APPLICABLE
```

但：

```text
F11 Interaction State
!= F10 Resolution Authority
```

F10 仍然是 Runtime Resolution Owner。

---

# 54. Accepted for Processing 的边界

如果使用：

```text
Accepted for Processing
```

只表示：

> 当前 Runtime Resolution 接受该 Intent 进入后续处理。

不得解释为：

```text
永久权限
最终执行成功
```

正式：

```text
Accepted for Processing
!= Runtime Permission Persisted

Accepted for Processing
!= Execution Succeeded
```

---

# 55. Submission / Resolution / Runtime Outcome 三层分离

Control Intent 的反馈至少在语义上区分：

```text
Submission Outcome

Resolution Outcome

Runtime Consequence / Outcome
```

正式：

```text
Submission Outcome
!= Resolution Outcome
!= Runtime Outcome
```

例如：

```text
Submission:
RECEIVED

Resolution:
ALLOW

Runtime:
EA-20 RUNNING
```

是三个不同事实。

---

# 56. Intent Submission Success 不等于 Runtime Success

正式：

```text
Intent Submission Success
!= Runtime Control Success

Intent Accepted
!= Runtime Execution Succeeded
```

页面不能在请求刚提交时直接显示：

```text
Retry succeeded
```

除非对应 Runtime 结果已确认。

---

# 57. Control Intent Rejected 不等于 Runtime Failure

如果：

```text
RETRY
```

因 Authorization / Gate / Applicability 被阻止，

说明：

```text
Runtime execution never occurred
```

因此：

```text
Control Intent Rejected
!= Runtime Execution Failure
```

---

# 58. Optimistic Interaction Feedback

Implementation 可以显示：

```text
正在提交暂停请求…
正在提交取消请求…
```

但：

```text
Optimistic Interaction Feedback
!= Confirmed Runtime State
```

不能在 Runtime 未确认前将 Action 状态改为：

```text
PAUSED
CANCELLED
RUNNING
```

---

# 59. Requested 与 Confirmed 分离

正式：

```text
Requested Pause
!= Confirmed Paused State

Requested Resume
!= Confirmed Running State

Requested Retry
!= Confirmed New Attempt

Requested Cancel
!= Confirmed Cancelled State
```

Confirmed State 必须回归 authoritative / current RuntimeProjection。

---

# 60. Control Feedback 最终回归 Current Projection

F11 不应长期依赖本地 optimistic state 判断 Runtime。

正式：

```text
Control Feedback
should converge back to
authoritative / current RuntimeProjection.
```

例如：

```text
Retry submitted
↓
Resolution allowed
↓
EA-20 created
↓
Current Projection:
A17 RUNNING
```

最终以新的 Current Projection 为主要 Runtime 展示依据。

---

# 61. Runtime Control 与 Human Governance Decision 的边界

普通 Runtime Control 可以继续自动解析，只要：

```text
Semantic Intent remains materially unchanged

Governed Scope remains valid

Authority can be deterministically resolved

Existing Gate is not bypassed

No new governed exception is required

No unresolved material governance choice remains
```

---

# 62. Governance Boundary Crossing

当普通 Control Intent 需要跨越：

```text
Material Scope Expansion

Unresolved Authority Conflict

Gate Override / Governed Exception

New High-impact Irreversible Governance Choice

Multiple materially distinct legitimate paths
that existing rules cannot uniquely resolve
```

时，普通 Runtime Control 不得继续自动执行。

---

# 63. 多方案不自动等于 Human Decision

即使存在多个 Candidate，系统仍应优先：

```text
collapse equivalent options

remove dominated options

apply existing policy

perform deterministic routing
```

只有仍剩：

```text
multiple materially distinct legitimate choices
```

且现有规则不能唯一解析时，才形成 Human Decision Requirement。

---

# 64. Operational Failure 不自动转 Human Decision

例如：

```text
network timeout
temporary bridge failure
provider transient error
```

优先进入：

```text
retry
fallback
re-query
re-route
technical recovery
```

正式：

```text
Operational Failure
!= Human Decision Required
```

---

# 65. Control Intent 不承担 Governance Decision

正式：

```text
Control Intent
cannot absorb Material Scope Expansion

Runtime Control Intent
must not resolve unresolved Authority Conflict

Explicit Control Intent
!= Governed Exception
```

---

# 66. Decision Input 与 Runtime Control Intent 分离

当真正需要 Human Decision 时：

```text
Human Decision Requirement
↓
F11-D04 GovernanceDecisionInteraction
```

用户随后提供的是：

```text
GovernanceDecisionInput
```

而不是：

```text
RuntimeControlIntent
```

正式：

```text
Decision Input
!= Runtime Control Intent
```

---

# 67. Governance Resolution 不自动复活旧 Intent

完成治理决策后：

```text
Governance Resolution
```

不得直接：

```text
blindly resume old Control Intent
```

正确：

```text
Governance Resolution
↓
Current runtime context re-resolved
↓
determine whether original Intent
is still applicable
```

正式：

```text
Governance Resolution
!= Automatic Revival of Old Control Intent
```

---

# 68. Materially Changed Control Meaning

如果 Governance Resolution 后：

```text
Scope
Intent Meaning
Target Meaning
Runtime Consequence
```

发生实质改变，

则原则上：

```text
Materially Changed Control Meaning
→ New Control Intent by default
```

除非 Runtime Contract 明确认为原 Intent 仍保持相同语义。

---

# 69. Intent Withdrawal 与 Runtime Cancellation 分离

如果尚未消费的 Intent 未来支持撤回：

```text
Intent Withdrawal
```

也不等于：

```text
Runtime Cancellation
```

一旦 Runtime 已经产生 Execution Attempt，再取消通常应形成新的 Runtime Control Intent。

正式：

```text
Intent Withdrawal
!= Runtime Cancellation
```

Exact Withdrawal Model 暂缓。

---

# 70. 一次 Intent 与 Runtime 后果不是固定 1:1

D03 不冻结：

```text
one Intent = one Attempt
```

正式允许：

```text
One Control Intent
may resolve to zero, one,
or multiple Runtime Consequences
according to owning Runtime Contract.
```

例如：

```text
NO_LONGER_APPLICABLE
→ zero

RETRY
→ one new Attempt

future Task-level Cancel
→ multiple governed consequences
```

---

# 71. Correlation Requirement

Control Intent 应能与：

```text
Resolution

Execution Attempt where applicable

Runtime Result

Current Projection
```

保持关联。

例如：

```text
CI-100
→ Resolution ALLOW
→ EA-20
→ Result R-20
```

但：

```text
Correlation
!= Authorization

Correlation
!= Ownership Merge
```

---

# 72. D03 与 D04 的边界

D03 负责：

```text
普通 Runtime Control
什么时候不能继续自动执行
```

D04 负责：

```text
Human Decision Context

Alternatives

Material Differences

Recommendation presentation

Decision Input collection
```

D03 不设计 Human Decision UX。

---

# 73. D03 与 D05 的边界

D03 要求：

```text
Control Resolution
must preserve Reason interpretability
```

但：

```text
Reason taxonomy
Root Cause
Immediate Cause
Multiple Blockers
Explanation hierarchy
```

由 D05 负责。

---

# 74. D03 与 D06 的边界

D03 负责：

```text
Intent → Resolution → Runtime Consequence
Correlation Requirement
```

D06 负责：

```text
Result Presentation

Trace Timeline

Evidence Navigation

Provenance
```

---

# 75. D03 与 D08 的边界

D03 冻结：

```text
Stable logical Intent identity

Duplicate Delivery != New Intent

Timeout / restart semantics

Cross-surface duplicate-consequence prevention
```

但 D08 再细化：

```text
Reconnect

Delivery consistency

Session recovery

Transport sequencing

Cross-surface continuation
```

---

# 76. D03 与 Implementation 的边界

D03 不冻结：

```text
REST

HTTP Status Code

WebSocket

SSE

gRPC

Message Broker

Database Transaction

Distributed Lock

Mutex

CAS

Outbox / Inbox implementation

Retry Count

Timeout Seconds

DB Schema

Redis Structure

Go Struct

TypeScript Interface
```

D03 只冻结：

```text
Semantic Handoff
```

---

# 77. Control Handoff 六阶段模型

F11-D03 正式采用：

```text
1. Observe
   F11 获得 RuntimeProjection / Control Hint

2. Express
   Origin 产生明确 RuntimeControlIntent

3. Capture
   F11 保留 Identity / Target / Basis /
   Origin / Correlation

4. Revalidate
   F10 使用当前事实进行
   Point-of-use Revalidation

5. Resolve
   F10 得出当前适用性 /
   permission / block / stale /
   duplicate / re-resolution /
   governance escalation 结果

6. Consequence & Reflect
   合法时形成 Runtime 后果；
   F11 通过 correlation +
   new Current Projection 展示结果
```

该模型是责任模型，不是固定技术流程。

---

# 78. 自动优先、人工最后

Control Intent 无法直接执行时，推荐解析顺序：

```text
1. Current State Revalidation

2. Deterministic Re-resolution

3. Existing Recovery / Fallback

4. Existing Scope / Authority / Gate Rule Resolution

5. Domain Governance Routing

6. Human Decision only when
   genuine unresolved judgment remains
```

该顺序不表示必须机械经过全部步骤。

如果规则已经明确必须 Human Decision，可以直接进入对应治理流程。

---

# 79. F11-D03 核心不变量

正式冻结：

```text
Control Hint
!= Control Intent

Control Intent
!= Runtime Permission

Control Intent
!= Authorization

Control Intent
!= Execution Attempt

Control Intent
!= Provider Choice

Control Intent
!= Adapter Choice

Control Intent
!= Execution Recipe

Observed Basis
!= Runtime Permission

Point-of-use Revalidation
occurs at protected use,
not merely at UI click time

Pre-submit Refresh
!= Point-of-use Revalidation

Every Protected Control Intent
requires Point-of-use Revalidation

Revalidation Scope
may depend on Intent meaning
and governed consequence

Stronger Revalidation
!= Full Architecture Recompute

Retry
!= New Business Action

Resume
!= Blind Continue

Pause Snapshot
!= Resume Permission

Displayed Pause Hint
!= Guaranteed Pause Capability

UI Confirmation
!= Runtime Permission

Control Intent
!= Scope Expansion Approval

Control Intent
cannot absorb Material Scope Expansion

Intent Creation-time Authority
!= Use-time Authority

Authority Changed
!= Human Decision Required

Runtime Control Intent
must not resolve unresolved Authority Conflict

Explicit User Control
!= Gate Override

Explicit Control Intent
!= Governed Exception

Provider Change
!= New Control Intent by default

Provider Re-resolution
!= Human Decision by default

Any State Change
!= Intent Invalidation

Material Applicability Change
may invalidate or re-route Intent

No Longer Applicable
!= Permission Denied

No Longer Applicable
!= Runtime Failure

No Longer Applicable
!= System Error

Duplicate Delivery
!= New Intent

New Explicit Intent
!= Revision of Old Intent by default

Material Intent Change
→ New Intent by default

Stable Interaction Identity
!= Concurrency Safety by itself

Two Valid-looking Intents
!= Two Authorized Runtime Consequences

Concurrent Control Processing
must preserve Point-of-use State Validity

Delivery Semantics
!= Runtime Consequence Semantics

Delivery Count
!= Execution Attempt Count

Processing Invocation Count
!= Runtime Consequence Count

Transport Timeout
!= Control Intent Failure

Transport Timeout
!= Runtime Failure

Transport Retry
should preserve Logical Intent Identity
for the same submission

Unknown Submission Outcome
!= Runtime Failure

F11 Restart
!= New Control Intent

Recovery Uncertainty
!= Permission to Re-execute

Recovery Uncertainty
!= Human Decision Required

Technical Uncertainty
!= Governance Judgment Gap

Control-plane Delivery Uncertainty
must not silently multiply
Protected Runtime Consequences

Automatic Runtime Recovery
does not require synthetic Human Control Intent

Automation-originated Intent
!= Human Governance Decision

Origin Surface
!= Runtime Control Authority

Interaction Lifecycle
!= Runtime Action Lifecycle

Control Interaction Tracking
!= Control Execution State Machine

Runtime Failure
!= Control Intent Failure

Intent Resolution
!= Interaction Capture Failure

Intent Resolution Block
!= Runtime Failure

F11 Interaction State
!= F10 Resolution Authority

Accepted for Processing
!= Runtime Permission Persisted

Accepted for Processing
!= Execution Succeeded

Submission Outcome
!= Resolution Outcome
!= Runtime Outcome

Intent Submission Success
!= Runtime Execution Success

Control Intent Rejected
!= Runtime Execution Failure

Optimistic Interaction Feedback
!= Confirmed Runtime State

Requested Pause
!= Confirmed Paused State

Requested Resume
!= Confirmed Running State

Requested Retry
!= Confirmed New Attempt

Requested Cancel
!= Confirmed Cancelled State

Control Feedback
should converge back to Current RuntimeProjection

Decision Input
!= Runtime Control Intent

Governance Resolution
!= Automatic Revival of Old Control Intent

Materially Changed Control Meaning
→ New Control Intent by default

Intent Withdrawal
!= Runtime Cancellation
```

---

# 80. Explicitly Forbidden Designs

F11-D03 明确禁止将以下方式提升为正式架构：

```text
Button Click = Runtime Permission

UI Confirmation = Runtime Permission

Old Projection = Current Permission

Old Authorization = Permanent Permission

Control Intent = Provider instruction

Retry = New Business Action

Resume = Blind restoration of old runtime state

Control Intent = Scope Expansion approval

User Control = Gate override

Runtime Control = Authority conflict resolution

Same Intent redelivery = New runtime action

Transport timeout = Runtime failure

F11 restart = Resubmit all controls

F10 uncertainty = Blindly execute again

ControlIntent.status = Runtime RUNNING / FAILED
as authoritative runtime truth

Accepted = permanent permission

Interaction success = runtime success

Human Decision Input = Runtime Control Intent

Governance approval = Blind revival of old intent

Optimistic UI state = Confirmed Runtime state
```

---

# 81. Deferred

F11-D03 明确暂缓：

```text
Exact Control Intent Enum

Exact Resolution Enum

Exact Intent Lifecycle Enum

Exact Revalidation Algorithm

Exact Retry Policy

Exact Retry Limit

Exact Timeout

Exact Concurrency Algorithm

Exact Idempotency Algorithm

Exact Locking Mechanism

Transaction Design

CAS

Distributed Lock

Exactly-once Transport

At-least-once Transport

REST Routes

HTTP Status Codes

WebSocket ACK

SSE

gRPC

Message Broker

Outbox / Inbox implementation

Control Intent DB Schema

Redis Design

Go Struct

TypeScript Interface

UI Confirmation Dialog

Exact Intent Withdrawal Mechanism
```

---

# 82. Approval Effect

本稿已经明确：

```text
F11-D03 HUMAN_APPROVED
```

因此正式冻结：

```text
Control Hint → Control Intent boundary

RuntimeControlIntent semantic meaning

Intent Identity / Origin / Target / Basis model

Point-of-use Revalidation responsibility

Proportional Revalidation principle

Retry / Resume / Pause / Cancel semantic boundaries

Scope / Authority / Gate / Provider change handling

No Longer Applicable semantics

Duplicate Delivery / New Intent distinction

Concurrency safety semantic requirement

Timeout / restart / recovery uncertainty boundary

Submission / Resolution / Runtime Outcome separation

Interaction Lifecycle / Runtime Lifecycle separation

Governance escalation boundary

Control Intent / Human Decision separation

Intent / Runtime consequence correlation

Feedback convergence to Current RuntimeProjection
```

但不代表：

```text
API Frozen

Transport Frozen

Intent Enum Frozen

Resolution Enum Frozen

Database Frozen

SQLite Schema Frozen

Concurrency Implementation Frozen

Exactly-once Delivery Frozen

UI Frozen

Implementation Authorized

RP2 Authorized

Authority Cutover Authorized

Canonical Replacement Authorized

Final Activation Authorized

Legacy Retirement Authorized
```

---

# 83. Final Frozen Decision

```text
F11-D03
— Control Intent & Point-of-use Revalidation Handoff

STATUS:
HUMAN_APPROVED / FROZEN

F11 expresses and tracks Control Intent
without becoming Runtime Permission Authority.

A Control Hint is not a Control Intent.

A Control Intent is not Runtime Permission,
Provider Selection, Adapter Instruction,
or Execution Attempt.

Every protected Control Intent is revalidated
at the actual point of protected Runtime use.

Observed UI state and pre-submit refresh
do not replace F10 revalidation.

Retry remains the same Business Action
and may create a new Execution Attempt.

Resume never means blind continuation
from an old pause snapshot.

Material Scope Expansion,
unresolved Authority Conflict,
Gate override requirements,
governed exceptions,
and unresolved materially different choices
cannot be silently absorbed by Runtime Control.

Duplicate delivery is not a new Intent.

Transport timeout is not Runtime failure.

Control-plane uncertainty must not silently
multiply protected Runtime consequences.

Submission Outcome,
Resolution Outcome,
and Runtime Outcome remain distinct.

F11 interaction tracking is not
a second Runtime Control State Machine.

Human Governance Decision Input
is not Runtime Control Intent.

Governance Resolution does not automatically
revive an old Control Intent.

Runtime Control feedback ultimately converges
back to authoritative/current RuntimeProjection.

Implementation remains NOT_AUTHORIZED.
```

---

**END OF F11-D03 HUMAN_APPROVED FREEZE**

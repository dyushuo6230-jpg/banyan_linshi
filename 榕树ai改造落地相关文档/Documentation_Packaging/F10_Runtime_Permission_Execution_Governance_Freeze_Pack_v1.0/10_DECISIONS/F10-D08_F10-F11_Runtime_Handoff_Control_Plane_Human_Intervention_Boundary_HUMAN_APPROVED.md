# F10-D08 — F10→F11 Runtime Handoff × Control Plane × Human Intervention Boundary

**阶段：** F10 — Runtime Permission / Execution Governance Architecture  
**主题：** F10→F11 Runtime Handoff（运行时交接）× Control Plane（控制面）× Human Intervention（人工介入）边界  
**状态：** `HUMAN_APPROVED`

**上游依赖：**
- `F10-G01 HUMAN_APPROVED`
- `F10-D01 HUMAN_APPROVED`
- `F10-D02 HUMAN_APPROVED`
- `F10-D03 HUMAN_APPROVED`
- `F10-D04 HUMAN_APPROVED`
- `F10-D05 HUMAN_APPROVED`
- `F10-D06 HUMAN_APPROVED`
- `F10-D07 HUMAN_APPROVED`

**Implementation Authorization：** `NO`

---

## 1. 决策目的

F10-D08 解决：

> Runtime 已经能够完成 Permission、Context、Provider / Adapter、Lifecycle、Failure Recovery、Result / Trace 和 Cross-Action Coordination 以后，应该如何把“当前运行状态”安全、准确、最小充分地交给未来 F11 Control Plane；F11 可以展示什么、用户可以提交什么控制意图、什么情况下才真正需要 Human Decision，以及所有 UI 操作如何继续受到 F10 Runtime Governance 约束。

总体关系：

```text
F10 Runtime Governance
↓
Purpose-sensitive Runtime Projection
↓
F11 Control Plane
↓
Display / Observe / Submit Control Intent
↓
F10 Point-of-use Revalidation
↓
Runtime Execution / Block / Recovery / Governance Route
```

---

## 2. F10 Runtime Governance != F11 Control Plane UX

```text
F10 Runtime Governance
!= F11 Control Plane UX
```

F10负责：

```text
Runtime Permission
Execution Context consumption
Provider / Adapter route
Execution Attempt
Lifecycle
Failure / Recovery
Runtime Result
Runtime Scheduling
```

F11未来负责：

```text
presentation
inspection
human interaction surface
control intent submission
governed decision presentation
```

---

## 3. F11 不是第二个 Runtime

```text
F11 Control Plane
!= Second Runtime Engine
```

F11 不重新实现：

```text
Permission Resolver
Provider Resolver
Adapter Router
Retry Engine
Lifecycle Engine
Dependency Scheduler
```

---

## 4. F11 不是 Authority Center

```text
F11
!= Global Authority
!= Runtime Permission Authority
!= Product Authority
!= Design Authority
!= Apply Authorization Authority
```

---

## 5. UI Action != Authority

继续继承既有合同：

```text
UI Action
!= Authority
```

一个按钮、菜单、API 调用入口本身不产生治理权力。

---

## 6. Control Request != Runtime Permission

用户通过 F11 发出：

```text
Retry
Resume
Cancel
Pause
Inspect
```

等请求，只形成：

```text
Control Intent
```

正式：

```text
Control Request
!= Runtime Permission
```

---

## 7. Control Intent 定义

Control Intent 表达：

> 用户或控制面希望 Runtime 尝试执行哪一种受支持的控制动作。

例如：

```text
Retry Action X
Resume Action Y
Cancel Task Z
Inspect Failure A
```

它不是技术实现指令。

---

## 8. Control Intent != Execution Implementation Instruction

```text
Control Intent
!= Provider Instruction
!= Adapter Instruction
!= Attempt Instruction
```

F11 不应指定：

```text
use Provider B
call MCP Adapter
create Attempt 17
```

除非未来存在专门受治理的高级诊断能力。

---

## 9. Provider / Adapter 继续由 F10 解析

收到 Control Intent 后：

```text
F10
→ resolve current context
→ resolve permission
→ resolve provider / adapter
→ execute lifecycle transition
```

F11 不越过 D03。

---

## 10. User controls intent; Runtime owns Attempt

```text
User controls Action / Task intent
Runtime owns Execution Attempt lifecycle
```

普通用户不需要理解 Attempt ID 才能 Retry / Resume。

---

## 11. Retry Click != Retry Authorization

用户点击 Retry 后：

```text
Retry Requested
↓
F10 receives intent
↓
D04 / D05 reconciliation
↓
D01 point-of-use validation
↓
D03 route resolution
↓
safe?
├─ YES → new Attempt
└─ NO  → remain blocked / route owner
```

---

## 12. Resume Click != Blind Resume

```text
User Resume Intent
!= Resume Allowed
```

继续遵循：

```text
Resume
→ Targeted Revalidation
```

---

## 13. Cancel Click != Immediate Hard Kill

```text
Cancel Intent
!= Safely Cancelled
```

若当前 Action 存在 Atomicity / Safe Interruption Boundary，F10仍按 D04安全终止。

---

## 14. UI Enabled != Permission Granted

```text
UI Enabled
!= Runtime Permission Granted
```

UI 显示错误、缓存错误或被绕过，也不能突破 F10。

---

## 15. UI Disabled != Security Boundary

```text
UI Disabled
!= Security Boundary
```

真正的 Permission Enforcement 必须存在于 Runtime / Server-side governed boundary。

---

## 16. Button Visible != Action Authorized

```text
Button Visible
!= Action Authorized
```

---

## 17. Control Plane API 不得绕过 Runtime

继续继承历史 Stage 16：

```text
Control Plane API
must compose Runtime API / Runtime Contract
```

而不是建立独立执行后门。

---

## 18. No Direct Mutating Adapter Endpoint

F11 不应直接暴露类似：

```text
git commit now
write file directly
invoke provider raw mutation
```

这类绕开 Runtime Governance 的 mutating endpoint。

```text
Control Plane
→ Runtime Intent / Governed Action
→ Runtime Enforcement
```

---

## 19. One UI Click != Combined Authority

```text
One UI Click
!=
Product Decision
+
Design Decision
+
Apply Authorization
+
Runtime Permission
+
Execution
```

这些语义继续分层。

---

## 20. User Runtime Control != Human Governance Decision

```text
User Runtime Control
!= Human Governance Decision
```

Pause / Cancel / Inspect 通常只是 Runtime Control；选择重大语义差异方案才可能构成 Governance Decision。

---

## 21. Human Governance Decision 定义边界

真正 Human Decision 继续复用：

```text
Informed Decision
DecisionProtocolDefinition
Applicable Domain Authority
```

F11 不创建新的 Decision Protocol。

---

## 22. F11 只是 Human Decision Surface

```text
F11
= Human Decision Presentation / Input Surface
```

但：

```text
F11
!= Decision Authority Owner
```

---

## 23. Decision Evidence != Runtime Permission

用户完成合法 Informed Decision 后形成 Decision Evidence，但继续保持：

```text
Decision Evidence
!= Apply Authorization
!= Runtime Permission
```

---

## 24. Human Decision != Immediate Canonical Mutation

```text
Human Decision
!= Immediate Canonical Mutation
```

例如：

```text
Human selects Option B
↓
Applicable Domain Resolution
↓
F7 Governed Change where required
↓
Apply Authorization where required
↓
F10 Runtime Permission
↓
Execution
```

---

## 25. Explicit Choice 才能成为 Choice Intent

继续继承：

```text
Silence
Cancellation
AI Recommendation
Inference
Ambiguous Preference
!= Human Confirmation
```

---

## 26. “继续”不自动产生 Authorization

用户普通表达“继续”时，如果当前 Action 因 Authorization expired / Scope unauthorized / Governed HOLD 而 BLOCKED：

```text
Continue Intent
!= New Authorization
```

---

## 27. Runtime State != User Action Required

```text
Runtime State
!= User Action Required
```

例如 PAUSED 可能正在自动恢复，不代表需要用户点击 Resume。

---

## 28. Operational Recovery != Human Interaction

对于：

```text
Provider temporary failure
Adapter transient failure
Refreshable freshness
Deterministic reconciliation
Governed fallback
Safe retry
```

继续采用：

```text
Automatic Recovery First
```

---

## 29. UNKNOWN != Human Decision Required

```text
UNKNOWN
!= Human Decision Required
```

UNKNOWN 首先触发 retrieve / revalidate / reconcile / re-resolve。

---

## 30. NEEDS_INPUT 语义必须拆分

历史 Runtime 中的 `NEEDS_INPUT` 不得混指“机器缺资料”和“真正需要人做治理决策”。

至少逻辑上应区分：

```text
Machine-resolvable Missing Input
Human Governance Input Required
```

---

## 31. Missing Context != Human Input Required

```text
Missing Context
!= Human Input Required
```

能由 F8 / F9 / 项目事实自动取得的，不应推给用户。

---

## 32. Human Decision Required 的触发边界

只有类似：

```text
Material Semantic Choice
Authority Conflict
Material Scope Expansion
Governed Exception Request
High-impact Irreversible Governance Choice
Multiple Legitimate Incompatible Outcomes
```

且已有确定性规则无法唯一解析时，才进入 Human Decision。

---

## 33. Multiple Options != Automatic Human Decision

```text
Multiple Options
!= Automatic Human Decision
```

继续复用：

```text
Validity Filtering
Equivalent-path Collapse
Dominance Elimination
Material Difference Detection
Preference Resolution
```

之后再判断。

---

## 34. Operational Difference != Human Choice

如果候选仅存在 provider latency / adapter implementation / retry timing / resource scheduling 等内部执行差异，且最终语义相同：

```text
Automatic
```

不打扰用户。

---

## 35. Information-only State

允许一种逻辑交互：

```text
INFORMATION_ONLY
```

表示只向用户说明发生了什么，但不要求用户行动。

Exact Enum 不冻结。

---

## 36. Optional Control State

允许：

```text
OPTIONAL_CONTROL
```

表示用户可 Pause / Cancel / Inspect，但系统不依赖用户才能正常继续。

---

## 37. Human Decision Required State

允许：

```text
HUMAN_DECISION_REQUIRED
```

表示 Runtime / Domain Governance 已确认必须由合法 Human Authority 作出决定。

Exact Enum 不冻结。

---

## 38. Information != Decision Request

```text
Information Notification
!= Human Decision Request
```

---

## 39. Optional Control != Governance Decision

```text
Optional Runtime Control
!= Governance Decision
```

---

## 40. Human Decision Required 必须来自治理解析

F11不得自行根据 error exists / unknown exists / multiple buttons exist 推断 Human Decision Required。

---

## 41. F10→F11 Handoff 定义

F10→F11 Handoff 是：

> 面向 Runtime Observation / Control / Human Interaction Purpose 的最小充分状态投影。

---

## 42. F10→F11 Handoff != Full Execution Context Dump

```text
F10 Internal Runtime Context
!= F11 Runtime Control View
```

F11 不需要默认拿完整 PRD / Design Package / Entire Source Context / Full Provider Context / All Evidence Body。

---

## 43. Purpose-sensitive Minimum Sufficient Projection

继续遵循：

```text
Purpose-sensitive
Minimum Sufficient
Governance-preserving
```

---

## 44. F11 Current Runtime View

逻辑上可包含：

```text
Subject / Task Ref
Current Action / relevant Actions
Current Runtime State
Progress basis where reliable
Reason
Blocker / Hold
Failure / Recovery State
Relevant Current Result
Available governed control intents
Human Decision requirement
Evidence / Trace refs
Relevant Scope
Relevant downstream obligation
```

Exact Schema 不冻结。

---

## 45. F11 View != Runtime Truth Store

```text
F11 Runtime View
!= Runtime Truth Store
```

它是 F10 Runtime State 的 Projection。

---

## 46. F11 不自己计算 Current Runtime State

```text
UI Projection
!= Runtime Resolution
```

---

## 47. Current Runtime View != Historical Trace

```text
Current Runtime View
!= Historical Trace
```

历史 Attempt 保留在 Trace，当前主状态由 F10 投影。

---

## 48. History != Current Effective Runtime State

```text
History
!= Current Effective Runtime State
```

---

## 49. Available Controls 应由 Runtime Capability 投影

```text
Current Runtime State
+
Applicable Control Capability
+
Governance State
↓
Available Control Intents
↓
F11 UI
```

而不是前端硬编码。

---

## 50. UI Button State 必须来自 Runtime / Stage Capability

继续继承历史 Stage16：

```text
UI Action State
must come from
Runtime / Stage Capability
```

---

## 51. UI 不得放宽 BLOCKED

```text
Runtime = BLOCKED
→ UI cannot infer AVAILABLE
```

---

## 52. UI 不得丢失 HOLD / UNKNOWN

HOLD / UNKNOWN / BLOCKED / STALE 如对用户判断重要，不得在 UI Projection 中静默消失。

---

## 53. Handoff Compression != Governance Compression

```text
Context Compression != Governance Compression
Handoff Projection != Semantic Downgrade
```

---

## 54. Required Handoff Qualifier Missing != PASS

```text
Missing Required Handoff Qualifier
!= PASS
```

如果不能安全解释当前控制能力：

```text
→ UNKNOWN / unavailable control
```

而不是猜测开放按钮。

---

## 55. Authority Reference != Authority Transfer

F11可显示 Authority / Decision Basis，但：

```text
Authority Reference
!= Authority Transfer
```

---

## 56. Trace rendered in UI != Authorization

```text
Trace rendered in UI
!= Authorization
```

---

## 57. Provenance rendered in UI != Authority

```text
Provenance Display
!= Authority
```

---

## 58. Progress 必须基于可靠证据

```text
Unknown Progress
!= Estimated Progress Presented as Fact
```

没有可靠结构化依据时不能猜百分比。

---

## 59. Structured Progress 可以展示

只有存在可靠 step count / completed units / checkpoint / provider progress 等证据时，才展示相应进度。

---

## 60. Progress != Acceptance

```text
100% Progress
!= Runtime Acceptance
```

---

## 61. Notification != Material Trace

```text
Material Trace Event
!= User Notification Event
```

Trace 可详细，通知应按 UX / Attention Policy 聚合。

---

## 62. 自动恢复不应形成通知风暴

例如多次 Attempt / Retry / Fallback 后自动恢复成功，普通 UI 可汇总为：

```text
Automatic recovery completed
No user action required
```

详细过程放入 Trace。

---

## 63. Failure occurred != User must be interrupted

```text
Failure occurred
!= User must be interrupted
```

---

## 64. Human Attention 是稀缺治理资源

继续采用：

```text
Reliable Automatic Routing
×
Minimum Human Decision Governance
```

---

## 65. Informed Decision 展示要求

真正需要用户判断时，F11 应展示 Minimum Sufficient Decision Context，至少包括适用：

```text
What happened
Why automatic resolution stopped
Current Scope
Relevant Authority / Governance basis
Option A
Option B
Material differences
Main impact
Validation impact
Risk
Downstream impact
What happens if no decision is made
```

---

## 66. AI Recommendation != Human Decision

```text
AI Recommendation
!= Human Decision
```

---

## 67. F11 不成为 Decision Protocol Owner

```text
F11 Decision UI
!= DecisionProtocolDefinition Owner
```

---

## 68. Explicit User Decision 形成 Decision Evidence

合法 Human Authority 明确选择后：

```text
Explicit Choice
→ Governed Decision Evidence
```

但是否形成 Product Decision / Design Decision / Apply Authorization，仍由对应 Domain Contract 判断。

---

## 69. User Identity != Authority Automatically

```text
Authenticated User
!= Applicable Authority Automatically
```

---

## 70. Admin UI != Universal Authority

```text
Admin UI
!= Universal Authority
```

---

## 71. Control Intent 应声明 Subject

Material Control Intent 至少逻辑上识别：

```text
Subject / Task / Action
Requested Control
Relevant Scope
Current observed state reference where required
```

Exact Schema 不冻结。

---

## 72. Stale UI Control Request

如果 UI 显示 PAUSED，但用户点击 Resume 前 Runtime 已恢复，则旧请求必须基于 current state 重新评估，不能按旧页面状态盲执行。

---

## 73. UI State Snapshot != Eternal State

```text
UI State Snapshot
!= Eternal Runtime State
```

---

## 74. Point-of-use Revalidation 仍由 F10 执行

任何可能产生 Material Side Effect 的 Control Intent：

```text
→ F10 point-of-use revalidation
```

---

## 75. Handoff Accepted != Eternal Validity

```text
F11 received runtime view
!= runtime basis remains valid forever
```

---

## 76. Duplicate Control Delivery != Duplicate Execution

网络重试、双击、重复消息不能被解释为重复执行同一 Mutation。

```text
Duplicate Control Delivery
!= Duplicate Authorized Action
```

Exact Idempotency Key / Request ID 机制不在 D08 冻结。

---

## 77. Multiple Control Surfaces

未来可以存在：

```text
Web UI
CLI
IDE
API
Other Control Surface
```

因此：

```text
F11 Web UI
!= Only Runtime Control Surface
```

---

## 78. Control Surface != Runtime State Owner

```text
Control Surface
!= Runtime State Owner
```

---

## 79. UI Disconnect != Runtime Failure

```text
Control Plane Disconnect
!= Runtime Failure
```

---

## 80. UI Disconnect != Runtime Cancel

```text
UI Disconnect
!= Cancel
```

---

## 81. Runtime Lifetime != UI Session Lifetime

```text
Runtime State Lifetime
!= UI Session Lifetime
```

---

## 82. UI Reconnect

重新连接时：

```text
F11
→ fetch current F10 runtime view
```

不依赖本地旧页面恢复 Runtime Truth。

---

## 83. Multiple Control Clients

多个合法 Control Surface 同时观察 / 控制同一 Task 时：

```text
last click wins
```

不得作为默认治理规则。

---

## 84. Last Control Request != Higher Authority

```text
Latest Control Request
!= Higher Authority
```

---

## 85. Conflicting Control Intents

例如：

```text
Client A → Resume
Client B → Cancel
```

需依据 Current Runtime State、Applicable Control Contract、Authority / Ownership where applicable、Ordering / Concurrency Rules 解析。

Exact Algorithm 不冻结。

---

## 86. Control Conflict != Semantic Conflict Automatically

```text
Control Request Conflict
!= Product / Design Semantic Conflict Automatically
```

---

## 87. F11 状态更新不是 Mutation Authorization

```text
State Display Update
!= Mutation Authorization
```

---

## 88. F11 Read Surface 与 Mutation Surface 分离

Control Plane 可以大量 read / inspect / trace / provenance / status，但真实 Mutation Intent 必须走 Runtime Governed Contract。

---

## 89. Read-only UX 不自动需要高强度门禁

```text
Same Control Plane
!= Same Governance Cost for every action
```

---

## 90. Protected Control Intent

Apply / Commit / Protected Write / Cutover / Activation 等高影响 Intent 必须继续走其完整治理链。

---

## 91. Current Hard Prohibitions 必须映射到 F11

当前：

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
```

F11 不得将这些显示为已授权可执行能力。

---

## 92. UI Capability Projection 不能创造未来权限

```text
Future Feature Exists in UI Design
!= Feature Authorized Now
```

---

## 93. Current Stage Safety State 继续有效

历史 Stage16 的：

```text
AVAILABLE_READ_ONLY
AVAILABLE_DRY_RUN
BLOCKED
NEEDS_INPUT
NOT_APPLICABLE
NOT_AUTHORIZED_IN_STAGE16
```

仅作为历史实现 / 兼容证据。

D08 不冻结这些 Exact Enum。

---

## 94. Historical Stage16 != F11 Architecture Authority

```text
Historical Stage16 Implementation
!= F11 Final Architecture Authority
```

---

## 95. F10→F11 Runtime Handoff != Authority Transfer

```text
F10→F11 Handoff
!= Authority Transfer
```

---

## 96. F10→F11 Runtime Handoff != Runtime Ownership Transfer

```text
Handoff to F11
!= Runtime Ownership Transfer
```

F10仍拥有 Runtime Enforcement。

---

## 97. Handoff Direction != Authority Direction

```text
Handoff Direction
!= Authority Direction
```

---

## 98. Later Stage != Higher Authority

```text
F11 being later than F10
!= Higher Authority
```

---

## 99. F11 Response 返回 F10 的仍是 Input

F11提交 Control Intent / Governed Decision Input，这些都是 Input；F10 / Domain Owner 再按 Contract 解析。

---

## 100. Decision Input 与 Control Intent 必须可区分

```text
Runtime Control Intent
!= Governance Decision Input
```

---

## 101. Decision Input 与 Authorization 必须可区分

```text
Governance Decision Input
!= Apply Authorization automatically
```

---

## 102. Available Action Projection

F10可向 F11 投影：

```text
Allowed Control Intent
Unavailable Control Intent
Blocked Control Intent
Human Decision Requirement
```

但这是当前 Runtime Derived State，不是永久 Permission。

---

## 103. Available Control Cache != Eternal Capability

```text
Cached Available Control
!= Eternal Available Control
```

---

## 104. Control View 可以缓存，但必须可失效

Authorization changed / Gate changed / Action completed / Task cancelled 等变化都应使相关 UI Capability Projection 失效。

Exact push / polling 机制不冻结。

---

## 105. Control Plane UX 可以聚合复杂 Runtime 状态

例如：

```text
3 Actions running
1 automatically recovering
2 waiting
```

可以聚合展示。

但：

```text
UX Aggregation
!= Runtime State Merge
```

---

## 106. Aggregated Success != Every Action Accepted

```text
Task looks healthy
!= Every Action Accepted
```

---

## 107. User-facing Simplicity != Governance Loss

```text
Simple UX
!= Drop Material Governance Meaning
```

---

## 108. Runtime Reason 应可转成用户可理解说明

例如 `AUTHORITY_EXPIRED` 可展示为：

> 当前授权已失效，需要重新完成相应治理步骤。

---

## 109. Friendly Message != Semantic Rewrite

```text
User-friendly Explanation
!= Change underlying Runtime Semantics
```

---

## 110. User Notification Policy 不在 D08 详细冻结

D08 只冻结：

```text
not every trace event becomes notification
```

Exact Toast / Inbox / Badge / Push 策略留给 F11。

---

## 111. Runtime Command Contract 与 UI 技术解耦

F10 Control Contract 不硬编码 React / Vue / Ant Design / WebSocket / HTTP only。

---

## 112. F11 不应知道 Provider 细节才能发 Control Intent

例如：

```text
Retry Action
```

而不是：

```text
Retry Codex HTTP Adapter request
```

---

## 113. Control Intent 可扩展

未来新增 Pause / Resume / Cancel / Retry / Inspect / Acknowledge / Request governed decision 等能力，不应推翻 Core Contract。

Exact Control Catalog 不冻结。

---

## 114. Human Intervention 可局部化

如果只有 Action B需要 Human Decision，而 A/C 无真实 Dependency，可以继续。

```text
Human Decision Required for one Action
!= Whole Task Must Freeze
```

---

## 115. Human Decision Blast Radius

人工决策影响范围也必须遵循 Scope / Dependency / Atomicity。

---

## 116. Human Decision Return 后定向恢复

```text
Re-resolve affected Domain
↓
revalidate affected Actions
↓
resume only materially affected execution
```

不默认重跑全部 Task。

---

## 117. Informed Decision Context 应最小充分

```text
Informed Decision Context
!= Full Runtime Context Dump
```

---

## 118. 用户不负责帮系统查技术事实

如果 file location / provider health / freshness / dependency lookup / current target state 可由系统确定性取得：

```text
System must resolve first
```

---

## 119. Human Decision 不是系统偷懒出口

```text
Human Decision
!= Escape Hatch for Missing Automation
```

---

## 120. F11 只显示真正待人处理事项

“Needs Your Decision”不得混入 auto-retry in progress / stale context being refreshed / provider fallback being resolved。

---

## 121. Explainability

F11应能在需要时展示：

```text
why this Action is blocked
why a control is unavailable
why automatic recovery occurred
why human decision is required
```

依据来自 D06 Trace / Evidence / Governance Basis。

---

## 122. Explainability != Runtime Authority

```text
F11 Explanation
!= Runtime Authority
```

---

## 123. F11 可展示历史，但历史不能改当前状态

```text
History display
!= Current Runtime Resolution
```

---

## 124. Control Plane Audit

Material Control Intent / Human Decision Input 应可形成 Trace / Provenance Evidence。

但：

```text
Audit Record
!= Authorization
```

---

## 125. Control Intent Trace

在需要时应能回答：

```text
who / what submitted the intent
what subject
what requested control
what current basis was observed
what F10 decided
what result followed
```

Exact Schema 不冻结。

---

## 126. Runtime Refusal 应可解释

如果用户点击 Resume，而 F10返回 BLOCKED，F11应能展示为什么不能恢复、当前阻塞条件、系统是否正在自动处理、是否真的需要人工治理。

---

## 127. Refused Control != Task Failure

```text
Control Intent Rejected
!= Task Failure
```

---

## 128. Invalid Control Intent

若当前 Action 已 Completed，旧页面仍发 Retry，Control Intent 可被 reject / no-op / reinterpreted，具体行为后续实现决定。

但不得产生不符合当前状态的新副作用。

---

## 129. F11 Stage / Implementation 不因 D08 自动启动

D08 只冻结：

```text
F10 outgoing handoff
+
future F11 consumption boundary
```

不表示：

```text
F11 Implementation Authorized
F11 Final Activation Authorized
```

---

## 130. Architecture / Implementation Separation

D08 不冻结：

```text
Exact Control Plane API
Exact Runtime View Schema
Exact UI State Enum
Exact Control Intent Enum
Exact WebSocket / SSE / Polling mechanism
Exact frontend framework
Exact auth/session implementation
Exact request idempotency implementation
Exact notification strategy
Exact progress UI
Exact retry button behavior
Exact command conflict algorithm
Exact persistence
Exact F11 component structure
```

---

## 131. AI Autonomous Boundary

F10 / F11可以自动：

```text
project runtime state
refresh view
display explainable reason
route operational recovery automatically
submit structured control intent
```

但不代表 AI 可以：

```text
invent Authority
UI create Permission
turn recommendation into human approval
change governance policy
silently expand Scope
convert missing facts into user decisions
```

---

## 132. Core Invariants

```text
F10 Runtime Governance != F11 Control Plane UX
F11 Control Plane != Second Runtime Engine
UI Action != Authority
Control Request != Runtime Permission
Control Intent != Execution Implementation Instruction
User Runtime Control != Human Governance Decision
One UI Click != Combined Authority
Decision Evidence != Apply Authorization != Runtime Permission
Human Decision != Immediate Canonical Mutation
Runtime State != User Action Required
Operational Recovery != Human Interaction
UNKNOWN != Human Decision Required
Missing Context != Human Input Required
Multiple Options != Automatic Human Decision
Information Notification != Human Decision Request
Optional Runtime Control != Governance Decision
F11 Runtime View != Runtime Truth Store
UI Projection != Runtime Resolution
Current Runtime View != Historical Trace
History != Current Effective Runtime State
UI Enabled != Permission Granted
UI Disabled != Security Boundary
Button Visible != Action Authorized
Trace rendered in UI != Authorization
Provenance Display != Authority
Unknown Progress != Estimated Progress Presented as Fact
Material Trace Event != User Notification Event
Failure Occurred != User Must Be Interrupted
AI Recommendation != Human Decision
Authenticated User != Applicable Authority Automatically
Admin UI != Universal Authority
UI State Snapshot != Eternal Runtime State
Duplicate Control Delivery != Duplicate Authorized Action
Control Plane Disconnect != Runtime Failure
UI Disconnect != Cancel
Runtime State Lifetime != UI Session Lifetime
F11 Web UI != Only Runtime Control Surface
Control Surface != Runtime State Owner
Latest Control Request != Higher Authority
F10→F11 Handoff != Authority Transfer
F10→F11 Handoff != Runtime Ownership Transfer
Handoff Direction != Authority Direction
Later Stage != Higher Authority
Runtime Control Intent != Governance Decision Input
Governance Decision Input != Apply Authorization Automatically
Cached Available Control != Eternal Available Control
UX Aggregation != Runtime State Merge
Simple UX != Governance Semantic Loss
Human Decision != Escape Hatch for Missing Automation
```

---

## 133. Forbidden Interpretations

明确禁止：

1. F11自己重新实现 Runtime Permission；
2. UI按钮存在就代表可执行；
3. UI Disabled 被当成真正安全边界；
4. F11直接调用 Git / Filesystem / Provider Mutation 绕过 F10；
5. 用户点击 Retry 就无条件再次执行；
6. 用户点击 Resume 就盲目继续；
7. Cancel 按钮立即硬切断 Atomic Action；
8. F11指定 Provider / Adapter / Attempt；
9. 一个 UI Click 同时完成 Decision / Authorization / Permission / Execution；
10. 普通 Continue 被解释成新 Authorization；
11. UNKNOWN直接显示“需要用户决定”；
12. Missing Context直接问用户；
13. Provider timeout弹窗让用户决定是否 Fallback；
14. Adapter unavailable弹窗让用户挑 Adapter；
15. F11根据 Error 自己决定 Human Decision Required；
16. Multiple Options 一律询问用户；
17. AI推荐自动等于用户选择；
18. Silence /取消 /模糊表达被当成人工批准；
19. F11把完整 Execution Context Dump 给 UI；
20. F11根据历史 Trace 自己计算 Current Runtime State；
21. History 中最后一条状态覆盖 Current Runtime Projection；
22. UI丢掉 HOLD / BLOCKED / UNKNOWN；
23. Progress 无证据却展示精确百分比；
24. 每个 Runtime Trace Event 都弹通知；
25. 自动 Recovery 过程反复打扰用户；
26. F11自己生成 Informed Decision Protocol；
27. 用户选择后直接修改 Canonical Truth；
28. Admin UI身份自动获得 Universal Authority；
29. UI页面旧状态直接驱动新 Mutation；
30. 重复点击导致重复 Mutation；
31. 浏览器关闭自动 Cancel Task；
32. 浏览器断线导致 Runtime Truth 丢失；
33. 最后一个客户端请求自动成为 Winner；
34. F11 Web UI 成为唯一 Runtime Control Surface；
35. F11 Handoff 被理解成 Runtime Ownership Transfer；
36. F11阶段更晚就认为 Authority 更高；
37. UI Capability Cache 永久有效；
38. UX 聚合吞掉 Material BLOCK；
39. Human Decision 成为系统缺自动化时的默认兜底；
40. D08 Approval 自动授权 F11 Implementation / Final Activation。

---

## 134. 与 F4 / Informed Decision 的关系

F4继续拥有：

```text
Workflow Control Semantics
Decision / Governance Interrupt Node
Workflow Choice
Escalation
```

既有 DecisionProtocolDefinition 继续提供 Informed Decision 语义。

F11仅提供交互界面。

---

## 135. 与 D01 的关系

D01继续拥有 Runtime Permission / Authorization Validation / Point-of-use Revalidation。

所有 F11 Control Intent 最终仍由 D01适用校验。

---

## 136. 与 D04 的关系

D04继续拥有 Pause / Resume / Retry / Cancel / Attempt / Safe Interruption。

F11只提交对应 Intent。

---

## 137. 与 D05 的关系

D05决定 Failure classification / Recovery owner / Automatic Recovery / Human Escalation Requirement。

F11不自己把 Failure 升级人工。

---

## 138. 与 D06 的关系

D06提供 Current Result / Evidence / Trace / Reason / Provenance / Runtime Acceptance，供 F11展示和解释。

F11不能重新解释这些 Result。

---

## 139. 与 D07 的关系

F11可以展示 Running / Waiting / Blocked / Parallel Actions / Dependency Reason，但跨 Action Scheduling 仍由 D07 / F4 Contract 处理。

---

## 140. 与历史 Stage16 的关系

历史 Stage16 已证明以下边界合理：

```text
Control Plane API only composes Runtime API
No direct mutating Git endpoint
UI Action State comes from Runtime / Stage capability
Trace cannot be rendered as Authorization
```

这些作为 Compatibility Evidence。

历史具体 Endpoint / Enum 不成为 D08 的 Architecture Authority。

---

## 141. 与 F11 的未来关系

D08 只提前冻结：

```text
what F10 may hand off
what F11 may consume
what F11 may request
what F11 may not decide
```

F11 自身更完整 Architecture 仍在未来 F11 Stage 冻结。

---

## 142. 后续 F10 Decision 边界

D08 后仍需继续收敛：

```text
F10 Stage Exit Contract
F10 completeness / consistency review
F10 → F11 formal stage handoff package
F10 final architecture freeze closure
```

不预设 D08 一定是 F10 最后一项。

---

## 143. Acceptance Meaning

用户已明确批准：

```text
F10-D08 HUMAN_APPROVED
```

因此正式成立：

```text
F10 Runtime Governance and F11 UX remain separated
F11 cannot create Runtime Permission or Authority
Control Plane submits intent rather than direct mutation
all mutating control intents return through F10 point-of-use validation
Runtime state does not automatically mean user action is required
automatic operational recovery remains default
UNKNOWN / missing context do not automatically escalate to humans
runtime control and governance decision remain distinct
Informed Decision remains governed by existing Decision Protocol
F10→F11 handoff is minimum-sufficient and governance-preserving
F11 consumes Current Runtime View rather than recomputing runtime truth
available UI controls derive from governed runtime capability
UI enablement is never the security boundary
Trace / Provenance may be presented but grant no authorization
duplicate / stale / concurrent control requests cannot bypass current runtime state
UI session lifetime remains separate from runtime state lifetime
future multiple control surfaces remain possible
human intervention stays limited to genuine unresolved judgment
```

但不表示批准：

```text
Exact Control Plane API
Exact F11 UI State Enum
Exact Runtime View Schema
Exact Control Intent Schema
Exact Request Idempotency mechanism
Exact Notification UX
Exact Progress UI
Exact WebSocket / SSE design
F11 Implementation
Real Project Write
RP2
Authority Cutover
Canonical Replacement
Final Activation
Legacy Retirement
```

---

## 144. Approval Status

```text
F10-D08 = HUMAN_APPROVED
```

普通“好的 / 下一步 / 继续 / 按建议继续”均不代表后续 Decision 的批准。

---

**END**

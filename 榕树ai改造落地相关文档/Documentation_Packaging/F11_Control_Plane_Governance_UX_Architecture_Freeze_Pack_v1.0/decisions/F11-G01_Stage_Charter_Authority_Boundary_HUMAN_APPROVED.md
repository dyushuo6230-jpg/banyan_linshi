# F11-G01 — Stage Charter / Authority Boundary
## F11 阶段章程与权威边界

**Stage：** F11 — Control Plane / Governance UX Architecture（控制面 / 治理交互架构）  
**Decision ID：** F11-G01  
**Status：** HUMAN_APPROVED / FROZEN  
**Implementation Authorization：** NO  
**RP2 Authorization：** NO  
**Authority Cutover Authorization：** NO  
**Canonical Replacement Authorization：** NO  
**Final Activation Authorization：** NO  
**Legacy Retirement Authorization：** NO  

---

# 1. 决策目的

F11-G01 用于冻结 F11 整个阶段的顶层职责、Authority（权威）边界、与 F4 / F7 / F8 / F9 / F10 的接口关系，以及后续 F11-D01～D10 必须共同遵守的总原则。

F11-G01 不设计具体 Web 页面，不冻结具体 API URL，不冻结数据库结构，不冻结 Vue / React / Ant Design 等技术实现，不重新设计 F10 Runtime（运行时），也不新增 Runtime Permission Authority（运行时许可权威）。

F11-G01 首先解决以下根问题：

```text
用户怎样看见 Banyan 正在做什么？
用户怎样理解为什么系统在等待、阻塞、暂停或恢复？
用户怎样安全地向系统表达 Retry / Pause / Resume / Cancel 等控制意图？
真正需要 Human Decision（人工决策）时，用户怎样获得充分信息并提交明确选择？
这些交互怎样不破坏 F1～F10 已冻结的 Authority 边界？
```

---

# 2. F11 的正式定位

F11 正式定义为：

> F11 是 Banyan 面向人和外部 Control Surface（控制入口）的 Control Plane（控制面）与 Governance UX（治理交互层）。F11 负责将既有 Authority Domain（权威域）和 Runtime 产生的当前状态、原因、结果、证据、可用控制能力和真正的治理决策需求，以 Purpose-sensitive Minimum Sufficient（按用途最小充分）的方式呈现给人或外部控制端，并将明确的控制意图、治理输入和交互输入安全路由回对应 Owner。

F11 自身不因“展示”“按钮”“输入”“通知”“推荐”“确认”“交互”而获得新的 Semantic Authority（语义权威）、Runtime Permission（运行时许可）或 Canonical Mutation Authority（规范事实修改权）。

正式：

```text
F11 = Control Plane + Governance UX

F11 != Runtime Authority
F11 != Product Authority
F11 != Design Authority
F11 != Apply Authorization Authority
F11 != Canonical Mutation Authority
F11 != Provider Binding Authority
F11 != Runtime Provider Resolver
F11 != Adapter Router
F11 != DecisionProtocolDefinition Owner
```

---

# 3. F11 与 F10 的正式边界

F10 在 F11 阶段进入后继续有效。

F10 继续拥有：

```text
Runtime Permission
Point-of-use Revalidation
Execution Context consumption
Runtime Provider Resolution
Adapter Routing
Execution Attempt / Lifecycle
Pause / Resume / Retry / Cancel enforcement
Runtime Failure / Recovery Coordination
Runtime Result / Evidence / Trace
Cross-Action Runtime Scheduling
```

这些职责不会因为出现 Control Plane、Web UI、CLI、IDE、API 或 Mobile Surface 而转移到 F11。

正式保持：

```text
F11 Stage Entry != F10 Retirement

F11 UI != Runtime Authority

Control Request != Runtime Permission

UI Enabled != Permission Granted

UI Disabled != Security Boundary

UI Action != Authority

Button Visible != Action Authorized

User Runtime Control != Human Governance Decision
```

---

# 4. F11 不是 Runtime 必经中枢

F11 不成为所有 Runtime 行为的 Mandatory Hop（强制必经节点）。

正式：

```text
F11
!= Mandatory Runtime Hop
```

确定性的合法 Runtime 工作可以在不经过用户界面、不等待 Control Plane、不等待 Human Input 的情况下继续。

例如：

```text
Retry
Fallback
Technical Recovery
Context Refresh
Dependency Re-resolution
Runtime Continue
```

若已经由既有 Runtime / Governance Rule 唯一确定，并且：

```text
Scope 未扩大
Authority 未改变
Semantic Intent 未改变
Gate 未突破
Governance Constraint 未绕过
```

则系统可自动继续。

正式：

```text
Deterministic Runtime Work
may continue
without F11 interaction
```

同时：

```text
F11 Availability
!= Runtime Availability

F11 Offline
!= Runtime Pause

Control Plane Reachability
!= Runtime Permission Prerequisite
```

因此关闭浏览器、IDE 断线、CLI 退出或 Mobile 离线，不自动导致 Runtime Task 被 Pause 或 Cancel。

---

# 5. F11 的核心职责

F11 的 Ownership（责任归属）限定为 Control Plane 与 Governance Interaction Semantic（控制面与治理交互语义）。

F11 可以拥有以下逻辑职责：

```text
Control Surface Interaction Semantics

Runtime Projection Presentation

Control Intent Capture

Governance Decision Interaction

Reason / Blocker / Explanation Presentation

Result / Evidence / Trace / Provenance Navigation

Human Attention Governance

Multi-Control-Surface Interaction Contract

Control Session / Delivery Interaction Semantics

Interaction Correlation
```

这里的 Owner 含义是：

> F11 可以决定“某类状态、原因、控制入口和治理交互应该怎样被安全表达和传递”。

但不代表：

> F11 成为这些被展示内容的 Semantic Authority Owner。

例如：

```text
F11 may own:
How BLOCKED is presented

F11 does not own:
Whether the Action is semantically BLOCKED
```

---

# 6. Runtime Projection 是 F11 的观察入口

F11 不复制完整 Runtime Truth，也不重建 Runtime State。

正式：

```text
Runtime / Domain Truth
→ Current Purpose-sensitive Projection
→ F11 Presentation
```

F11 可以消费的内容包括：

```text
Subject / Task / Action references
Current Runtime State
Current Result
Failure / Recovery State
Progress basis where reliable
Reason / Blocker / HOLD
Available governed Control Intents
Human Decision Requirement
Trace / Evidence / Provenance references
Relevant Scope
Downstream Obligations
```

F11 不得长期维护另一套独立的“UI Truth”。

正式：

```text
Presentation State
!= Runtime State Truth

UI Snapshot
!= Eternal Runtime State

Cached Available Control
!= Eternal Available Control
```

---

# 7. Presentation 不创造新的事实

F11 可以把机器可理解的状态转换为人可理解的表达。

例如：

```text
AUTHORITY_EXPIRED
```

可以被展示为：

```text
“当前操作已暂停，因为原执行授权已经失效。”
```

但正式保持：

```text
Explanation Projection
!= New Runtime Fact

Explanation
!= Authority
```

AI-generated Explanation（AI 生成解释）必须能够追溯到已有：

```text
Reason
State
Evidence
Provenance
Resolution Basis
```

F11 不得为了“更容易理解”而重新猜测一个未被 Domain Owner 或 Runtime 解析出的原因。

---

# 8. Control Intent 的正式定位

F11 可以接收和提交 Control Intent（控制意图）。

Control Intent 表达：

> 某个 Origin（来源）希望 Banyan 对某个 Subject / Task / Action 采取某种控制行为。

例如：

```text
PAUSE
RESUME
RETRY
CANCEL
```

但 Control Intent 不等于：

```text
Runtime Permission
Execution Attempt
Provider Command
Adapter Command
Authorization
Canonical Mutation
```

正式：

```text
Control Intent
!= Runtime Permission

Control Intent
!= Execution Attempt

Control Intent
!= Execution Implementation Instruction
```

---

# 9. Control Intent 的逻辑生命周期

Control Intent 的逻辑流程为：

```text
Origin / Control Surface
↓
Control Intent
↓
F11 Capture / Correlation / Routing
↓
Relevant Runtime / Domain Owner
↓
F10 Point-of-use Revalidation
↓
Current Validity Resolution
↓
ALLOW / BLOCK / NO_LONGER_APPLICABLE / RE-RESOLVE
↓
if allowed:
Runtime Execution
↓
Result / Evidence / Trace
↓
F11 Projection / Presentation
```

Control Intent Lifecycle 与 Runtime Action Lifecycle 必须分离。

正式：

```text
Control Intent Lifecycle
!= Runtime Action Lifecycle
```

例如用户请求：

```text
RETRY Action A17
```

新的 Retry 通常形成新的 Execution Attempt，但不自动创建一个新的 Business Action。

正式：

```text
Task != Action != Execution Attempt

Retry != New Business Action
```

---

# 10. Point-of-use Revalidation 仍属于 F10

F11 展示某个 Control 为可用，只表示：

> 在当前投影时刻，该 Control 根据已有信息是可提供的用户入口。

这不代表真正执行时一定获得许可。

因此：

```text
Control Shown
!= Control Guaranteed Executable
```

用户提交 Control Intent 后，受保护动作必须回到 F10 根据当前事实重新验证。

如果：

```text
State 已变化
Authorization 已失效
Scope 已变化
Gate 已变化
Action 已由其他 Surface 处理
Control 已不再适用
```

F10 可以返回：

```text
BLOCK
NO_LONGER_APPLICABLE
RE-RESOLUTION_REQUIRED
```

F11 负责把结果正确展示，而不是强制执行旧 Snapshot 中显示的操作。

---

# 11. 多 Control Surface 下的重复控制边界

F11 Core 不绑定 Web UI。

正式：

```text
F11 Core
!= Web UI Core
```

F11 应允许：

```text
Web
CLI
IDE
API
Mobile
Future Control Surface
```

不同 Surface 可以使用完全不同的视觉与交互形式，但共享同一套：

```text
Runtime Projection semantics
Control Intent semantics
Governance Decision semantics
Authority boundaries
Correlation semantics
```

如果 Web 与 IDE 同时向同一个 Action 提交 Retry，重复 Control Delivery 不得自动形成两次合法 Runtime Action。

正式保持：

```text
Duplicate Control Delivery
!= Duplicate Authorized Action
```

因此 F11 后续应支持稳定的 Interaction / Intent Correlation，但 Correlation ID 本身不授予 Authority。

正式：

```text
Correlation
!= Authorization
```

---

# 12. F11 输入不得设计成万能 UserAction

F11 不采用一个无语义区分的 Universal UserAction（万能用户操作）来承载全部交互。

逻辑上至少区分：

```text
Query / Inspect Interaction

Runtime Control Intent

Governance Decision Input

Attention Acknowledgement

Presentation Interaction
```

具体完整 Enum 与 Schema 暂缓到后续 Decision 或 Implementation。

正式：

```text
Interaction Mechanism
!= Interaction Meaning
```

“用户点击了按钮”本身不能决定该行为属于：

```text
查看
控制
决策
确认
批准
授权
```

必须由 Typed Interaction Semantic（分型交互语义）明确解释。

---

# 13. Governance Decision Input 与 Runtime Control Intent 必须分离

正式：

```text
Governance Decision Input
!= Runtime Control Intent

Human Decision
!= Runtime Control
```

例如：

```text
RETRY Action A17
```

属于 Runtime Control Intent。

而：

```text
“选择方案 B，并接受相应 Scope Expansion”
```

可能属于 Governance Decision Input。

这两种输入可以共享：

```text
Session
Origin
Correlation
Subject Reference
Timestamp
Provenance
```

等外层交互信息，但其：

```text
Authority
Owner
Validation
Routing
Outcome
```

必须分别解析。

---

# 14. F11 与 F4 Informed Decision 的边界

F11 不负责重新判断“什么时候必须找人”。

F4 及既有 Informed Decision Contract 继续负责：

```text
Workflow Candidate Validity
Material Difference Resolution
Automatic Selection Eligibility
Decision Required Resolution
Informed Decision trigger
```

正式保持：

```text
Multiple Candidates
!= Automatic Human Decision

UNKNOWN
!= Human Decision Required

Missing Context
!= Human Input Required

Operational Failure
!= Human Decision Required
```

F11 只有在既有 Governance / Domain Resolution 已经得到真正的 Human Decision Requirement 时，才负责向用户呈现 Minimum Sufficient Decision Context（最小充分决策上下文）并接收明确输入。

F11 不因为看到多个选项就自行决定弹出治理决策。

---

# 15. Human Decision UX 的责任

当真正需要 Human Decision 时，F11 负责展示足够支持判断的信息。

逻辑上可能包括：

```text
Decision Subject
Alternatives
Scope
Material Differences
Major Impact
Risk
Validation Scope
Long-term Maintenance Impact
Evidence / Reason Basis
```

F11 可以提供 AI Recommendation（AI 建议），但：

```text
AI Recommendation
!= Human Decision
```

用户明确选择产生的 Governance Decision Input 仍必须交给对应 Decision / Domain Owner 处理。

正式：

```text
Governance Decision Input
!= Apply Authorization

Human Decision
!= Runtime Permission

Decision Evidence
!= Apply Authorization
!= Runtime Permission
```

---

# 16. Acknowledge 不得提升成治理批准

F11 必须严格区分：

```text
Acknowledge
Approval
Decision
Authorization
Runtime Control
```

例如用户点击：

```text
“我知道了”
```

只能形成：

```text
Attention Acknowledged
```

不得静默升级为：

```text
Human Decision
Approval
Apply Authorization
Runtime Permission
```

正式：

```text
Acknowledge
!= Approval

Acknowledge
!= Human Decision

Acknowledge
!= Control Authorization
```

---

# 17. Presentation Interaction 不进入 Runtime Authority

以下行为默认属于 Presentation Interaction（展示交互）：

```text
展开 Trace
切换 Evidence Tab
搜索日志
展开更多原因
查看 Provenance
分页
过滤
排序
```

这些行为不因为经过 F11 就成为 Runtime Control 或 Governance Decision。

正式禁止将所有 UI 行为写入一个：

```text
UniversalControlAction
```

否则会混淆：

```text
Presentation
Control
Governance
Authority
```

---

# 18. Origin 必须保持可区分

F11 后续交互语义应能区分输入来源。

逻辑来源可能包括：

```text
HUMAN
SYSTEM
CONTROL_SURFACE
AUTOMATION
```

具体枚举后续冻结。

正式：

```text
Machine-originated Request
!= Human Decision
```

系统自动提交 Inspect、Projection Refresh 或其他技术交互，不得冒充明确的 Human Governance Decision。

---

# 19. Human Attention Governance 顶层原则

F11 不把用户作为默认 Error Handler（错误处理者）。

系统首先自动完成：

```text
State Query
Context Refresh
Trace Lookup
Dependency Re-resolution
Retry Eligibility Resolution
Fallback
Technical Recovery
Freshness Refresh
Owner Routing
```

只有在既有规则无法唯一解析，并最终存在真正治理判断缺口时，才占用用户注意力。

典型判断缺口包括：

```text
Material Semantic Choice
Authority Conflict
Material Scope Expansion
Governed Exception
High-impact Irreversible Governance Choice
Multiple Legitimate Incompatible Outcomes
```

正式：

```text
Failure
!= Human Judgment

Operational Failure
!= Human Decision Required

Recovery Failure
!= Immediate Human Decision
```

---

# 20. Notification 不创造新的状态与 Authority

F11 Notification / Attention 只负责帮助人发现真正需要关注的事情。

正式：

```text
Notification
!= Runtime State

Notification Dismissed
!= Blocker Resolved

Notification Read
!= Human Decision

Notification Acknowledged
!= Approval
```

自动恢复成功、普通 Waiting、可确定性重试等场景默认不应被提升成高干扰 Human Attention。

F11 的目标是：

```text
Automatic resolution where deterministic
+
Human attention only for genuine judgment
```

---

# 21. F11 与 F7 的边界

F7 继续拥有：

```text
Governed Change
Decision / Approval distinction
Apply Authorization
Canonical Apply Governance
Rollback Governance
Reference-safe Mutation
```

F11 可以展示这些状态并承接相应用户输入，但不得将一次 UI 操作合并成：

```text
Decision
+
Approval
+
Apply Authorization
+
Runtime Permission
+
Execution
```

正式保持：

```text
Decision
!= Approval
!= Apply Authorization
!= Runtime Permission
```

F11 不重新定义 F7 Canonical Apply Authority。

---

# 22. F11 与 F8 的边界

F8 继续拥有：

```text
Project Instance
Binding
Profile Instance
Provider Binding
Version Pin
Feature Activation
Project Reconciliation
```

F11 可以展示这些 Current Effective Result（当前有效结果），也可以接收用户希望修改相关配置的输入。

但 F11 必须首先路由 Owner，而不是直接完成 Durable Binding（持久绑定）。

例如：

```text
“本次 Runtime 换 Provider B”
```

可能属于 F10 Runtime Provider Resolution。

而：

```text
“以后这个项目默认使用 Provider B”
```

可能属于 F8 Project Binding Governance。

正式：

```text
Interaction Surface
does not decide Domain Ownership
```

---

# 23. F11 与 F9 的边界

F9 继续负责：

```text
Index
Query
Context Selection
Dependency / Impact Discovery
Freshness Evidence
Deferred Obligation Discovery
Targeted Retrieval
```

F11 不全量加载所有历史信息。

正式采用：

```text
Current Purpose
→ Minimum Sufficient Projection
→ User expands / requests more
→ Targeted Trace / Evidence / Dependency lookup
```

而不是：

```text
Every UI View
→ Full Repository Scan
→ Full Architecture Reload
→ Full Trace Reload
```

F11 必须继续遵守：

```text
Purpose-sensitive Minimum Sufficient Context
```

同时：

```text
Less Context = allowed

Less Governing Meaning = forbidden
```

---

# 24. Trace / Evidence / Provenance 边界

F11 可以查询、展示、过滤和关联：

```text
Result
Evidence
Trace
Provenance
```

但这些概念不得合并。

正式保持：

```text
Runtime Result
!= Evidence
!= Trace
!= Acceptance

Evidence
!= Authority

Trace
!= Authorization

Trace
!= Runtime Permission

Provenance
!= Authority
```

F11 后续应优先采用 Progressive Disclosure（渐进展示）：

```text
先显示用户可理解原因
↓
再显示依据摘要
↓
需要时展开 Evidence / Trace / Provenance
```

但具体 UI Layout 留给 Implementation。

---

# 25. Control Session 与 Runtime Lifetime 分离

正式：

```text
Control Session
!= Runtime Execution Lifetime
```

已有 F10 Core 明确：

```text
UI Session Lifetime
!= Runtime State Lifetime
```

因此：

```text
浏览器关闭
IDE 退出
CLI 结束
网络断开
页面刷新
```

均不得被静默解释成：

```text
Pause
Cancel
Retry
Resume
```

F11 后续需要支持：

```text
Reconnect
Projection Refresh
Correlation
Duplicate Delivery Protection
```

但具体协议留待后续 Decision 与 Implementation。

---

# 26. Control Intent 不翻译成底层执行指令

F11 只表达用户希望达成的控制语义。

例如：

```text
RETRY Action A17
```

F11 不得自行解析：

```text
Provider X
Adapter Y
具体执行命令
具体进程
具体 API 调用顺序
```

正确：

```text
F11 Control Intent
↓
F10 Revalidation
↓
Runtime Provider Resolution
↓
Adapter Resolution
↓
Execution Attempt
```

正式：

```text
Control Intent
!= Provider Instruction

Control Intent
!= Adapter Instruction

Control Intent
!= Execution Implementation Instruction
```

---

# 27. 推荐与 Authority 分离

F11 可以为了提升体验而提供：

```text
Recommended Action
Suggested Next Step
AI Recommendation
```

例如：

```text
“当前建议 Resume”
```

但：

```text
Recommendation
!= Permission

Recommended Control
!= Guaranteed Executable Control
```

用户提交后仍回到 Current State Revalidation（当前状态重新验证）。

---

# 28. F11 顶层运行原则

F11 采用以下顶层原则：

```text
Observe automatically
Explain progressively
Act by explicit intent
Decide only when genuinely required
Revalidate before protected execution
```

中文正式含义：

```text
能够自动观察的状态由系统自动获取；

解释采用按需展开，避免一次加载无关信息；

控制动作必须具备明确意图，不从普通展示行为猜测；

只有真正需要人的治理判断时才要求 Human Decision；

真正执行受保护动作前必须按当前事实重新验证。
```

---

# 29. F11 Core 与具体 Surface 解耦

F11 Architecture 不锁定 Web。

正式：

```text
F11 Semantic Core
supports:
Web / CLI / IDE / API / Mobile / Future Surface
```

不同 Control Surface 可以拥有不同：

```text
Layout
Component Model
Interaction Density
Navigation
Presentation Style
```

但不能形成不同：

```text
Authority Semantics
Runtime Permission Semantics
Control Intent Meaning
Human Decision Meaning
Runtime State Meaning
```

---

# 30. F11 Architecture 与 Implementation 的边界

F11 Architecture Freeze 只冻结：

```text
职责
Owner
Authority Boundary
Interaction Semantics
Runtime Projection Boundary
Control Intent Boundary
Human Decision Interaction Boundary
Attention Governance Boundary
Cross-stage Handoff Boundary
Multi-Surface Semantic Contract
```

当前不冻结：

```text
Vue / React / Ant Design 页面实现

具体按钮布局

REST API URL

WebSocket / SSE / Polling

数据库表

SQLite Physical Schema

完整 RuntimeState Enum

完整 ControlIntent Enum

具体 Go Struct

具体 TypeScript Interface

具体消息格式

Trace Physical Storage

Notification Channel

页面组件树

Design Package

Implementation Code
```

进入 F11 Architecture Stage 不代表 F11 Implementation Entry。

当前继续：

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

---

# 31. Explicit Non-Ownership

F11 明确不拥有：

```text
Runtime Permission Authority

Runtime State Truth Ownership

Provider Binding Authority

Runtime Provider Resolution

Adapter Routing

Execution Attempt Lifecycle

Product Authority

Design Authority

Apply Authorization

Canonical Mutation Authority

Project Binding Authority

DecisionProtocolDefinition Ownership

Index Truth Authority

Freshness Authority

Canonical Acceptance Authority
```

这些 Owner 继续由既有阶段合同决定。

---

# 32. Cross-stage Owner Preservation

正式保持：

```text
F4
→ Workflow / Orchestration / Informed Decision semantics

F5
→ Product / Requirement Authority

F6
→ Design / UI Truth Authority

F7
→ Change / Apply / Canonical Apply Governance

F8
→ Project Instance / Binding / Profile / Provider Binding

F9
→ Index / Context / Dependency / Impact / Freshness lookup

F10
→ Runtime Permission / Provider Runtime / Adapter / Execution Governance

F11
→ Control Plane / Governance UX
```

后阶段不会因为更接近用户界面而获得更高 Authority。

正式：

```text
Later Stage
!= Higher Authority
```

---

# 33. F11 Stage Entry 条件

F11 当前 Stage Entry 建立在：

```text
F1～F8 Frozen
F9 FINAL ARCHITECTURE FREEZE = HUMAN_APPROVED
F10 FINAL ARCHITECTURE FREEZE = HUMAN_APPROVED
F10 Blocking Architecture Gap = 0
F10 Additional Architecture Patch Required = NO
```

F11 Entry 不重新打开 F10。

只有未来发现：

```text
real frozen-baseline contradiction
new HUMAN_APPROVED upstream change
invalidated cross-stage contract
```

才可能形成新的 Reconciliation / Patch Need。

---

# 34. Packaging Obligation 与 Architecture Boundary

当前 Git Repository 中 F9 / F10 Freeze Pack 的可发现性问题属于 Packaging / Repository Discoverability Obligation。

正式：

```text
Packaging Discoverability Gap
!= Architecture Gap

Packaging Obligation
!= Freeze Revocation
```

因此不阻塞 F11 Architecture。

在未来建立 F1～F10 Consolidated Repository Baseline 时，应补齐对应正式归档路径。

---

# 35. F11-G01 核心不变量

F11-G01 正式冻结以下核心不变量：

```text
F11 != Runtime Authority

F11 != Mandatory Runtime Hop

F11 Stage Entry != F10 Retirement

F11 Architecture Entry != Implementation Entry

Presentation State != Runtime State Truth

Explanation != New Runtime Fact

UI Action != Authority

Button Visible != Action Authorized

UI Enabled != Permission Granted

UI Disabled != Security Boundary

Control Intent != Runtime Permission

Control Intent != Execution Attempt

Control Intent != Execution Implementation Instruction

Control Intent Lifecycle != Runtime Action Lifecycle

Governance Decision Input != Runtime Control Intent

Human Decision != Runtime Control

Acknowledge != Approval

Acknowledge != Human Decision

Interaction Mechanism != Interaction Meaning

Machine-originated Request != Human Decision

Recommendation != Permission

Runtime Result != Evidence != Trace != Acceptance

Evidence != Authority

Trace != Authorization

Provenance != Authority

Control Session != Runtime Execution Lifetime

Duplicate Control Delivery != Duplicate Authorized Action

Correlation != Authorization

UNKNOWN != Human Decision Required

Missing Context != Human Input Required

Operational Failure != Human Decision Required

Notification != Runtime State

Notification Read != Human Decision

Later Stage != Higher Authority
```

---

# 36. 后续 F11 Decision 的约束

F11-D01～D10 后续设计不得违反 F11-G01。

任何后续设计如果试图：

```text
让 UI 自己授予 Runtime Permission

让 Control Plane 自己选择 Provider

让 Human Decision 直接完成 Canonical Mutation

让按钮 Enabled 成为安全边界

让 Trace 作为 Authorization

让 F11 成为所有 Runtime 的必经点

让 UNKNOWN 自动要求用户决定

让系统错误默认转成人工确认

把 Web UI 结构提升成 F11 Core

让旧 Control Plane Implementation 覆盖新的 Freeze Contract
```

均视为违反 F11-G01，应在对应 Decision 内修正，而不是静默解释。

---

# 37. Deferred（明确暂缓）

F11-G01 不冻结以下事项：

```text
Exact ControlIntent Catalog

Exact Interaction Enum

Exact RuntimeProjection Schema

Exact HumanDecisionInput Schema

Exact Correlation ID Format

Exact Session Protocol

Exact Notification Severity Model

Exact API Contract

Exact Web / CLI / IDE Adapter Contract

Exact Transport

Exact Storage

Exact UI Component Model

Exact Design System Mapping
```

原则：

```text
Do not over-design now.

Do not leave Authority ambiguity unresolved.
```

---

# 38. Approval Effect

本条目已明确：

```text
F11-G01 HUMAN_APPROVED
```

因此正式生效：

```text
F11 Stage Charter
= FROZEN

F11 Authority Boundary
= FROZEN

F11 / F10 Runtime Boundary
= FROZEN

F11 / F4 Human Decision Boundary
= FROZEN

F11 Control Intent Top-level Boundary
= FROZEN

F11 Multi-surface Top-level Direction
= FROZEN
```

但不代表：

```text
Implementation Authorized

API Frozen

Schema Frozen

Web UI Frozen

SQLite Schema Frozen

Authority Cutover Authorized

Canonical Replacement Authorized

Final Activation Authorized
```

---

# 39. Final Frozen Decision

```text
F11-G01 — Stage Charter / Authority Boundary

STATUS:
HUMAN_APPROVED / FROZEN

F11 = Control Plane / Governance UX

F11 != Runtime Authority

F11 != Mandatory Runtime Hop

Control Intent != Permission

Governance Decision Input != Runtime Control Intent

Presentation != Truth

Explanation != New Fact

Human Attention only for genuine judgment gap

Protected execution returns to F10 point-of-use revalidation

F11 Core remains Control-Surface-neutral

Implementation remains NOT_AUTHORIZED
```

---

**END OF F11-G01 HUMAN_APPROVED FREEZE**

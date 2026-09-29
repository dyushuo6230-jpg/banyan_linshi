# F11-D01 — Control Plane Core Object & Responsibility Model
## 控制面核心对象与职责模型

**Stage：** F11 — Control Plane / Governance UX Architecture（控制面 / 治理交互架构）  
**Decision ID：** F11-D01  
**Upstream Gate：** F11-G01 = HUMAN_APPROVED / FROZEN  
**Status：** HUMAN_APPROVED / FROZEN  
**Implementation Authorization：** NO  
**RP2 Authorization：** NO  
**Authority Cutover Authorization：** NO  
**Canonical Replacement Authorization：** NO  
**Final Activation Authorization：** NO  
**Legacy Retirement Authorization：** NO  

---

# 1. 决策目标

F11-D01 用于冻结 F11 Control Plane（控制面）内部的核心逻辑对象、辅助逻辑对象、对象之间的责任关系、Truth Owner（事实权威归属）、Interaction（交互）边界、Projection（投影）边界以及持久化原则。

本 Decision 重点解决：

```text
F11 需要哪些稳定逻辑对象？

哪些对象属于 F11 自己的交互语义？

哪些只是对 F7 / F8 / F9 / F10 等上游事实的投影？

Task / Action / Execution Attempt 如何保持语义区分？

RuntimeProjection 如何组合多个 Domain 的状态而不制造新的 Authority？

用户交互如何区分 Query / Control / Decision / Acknowledge / Presentation？

Interaction 如何拥有稳定 Identity、Basis、Correlation 和重复投递边界？

哪些内容可以持久化？

哪些内容原则上应保持 Derived / Rebuildable？

如何避免 F11 变成新的 Runtime Truth Store 或影子数据库？
```

---

# 2. 设计基本原则

F11-D01 不通过“多造对象”解决架构问题。

正式采用：

```text
Minimum Sufficient Logical Object Model
```

即：

> 只建立稳定表达 Control Plane 职责所必需的逻辑对象；不为了未来可能实现的数据库、API、页面、消息队列或缓存提前制造持久化业务对象。

正式：

```text
Logical Object
!= New Canonical Truth

Logical Object
!= New DefinitionArtifact by default

Logical Object
!= New Authority Domain

Architecture Object
!= Database Table

Semantic Contract
!= Physical Schema
```

---

# 3. F11 对象的四层职责结构

F11 Core 采用以下逻辑分层：

```text
1. Surface / Session Layer
   控制入口与交互上下文

2. Projection / Understanding Layer
   状态、原因、证据和注意力的面向用途投影

3. Interaction / Submission Layer
   查询、Runtime 控制、治理决策和其他分型交互

4. Correlation / Continuity Layer
   跨 Surface、Interaction、Runtime Attempt、Result 的关联与连续性
```

该分层是：

```text
Responsibility Model
```

不是固定：

```text
Runtime Call Order
```

---

# 4. F11 Core Semantic Contracts

以下逻辑语义属于 F11 Core Semantic Contract（核心语义合同）：

```text
ControlSurface

RuntimeProjection

Typed Interaction Boundary

RuntimeControlIntent

GovernanceDecisionInteraction
```

Core Semantic Contract 的含义是：

> 如果这些核心语义缺失，F11 无法稳定承担 Control Plane / Governance UX 职责。

但：

```text
Core Semantic Contract
!= Must Persist
```

核心不等于必须落库。

---

# 5. Supporting Semantic Contracts

以下逻辑概念属于 Supporting Semantic Contract（辅助语义合同）：

```text
ControlSession

InteractionSubmission Envelope

ExplanationProjection

EvidenceView

AttentionSignal

InteractionCorrelation
```

它们需要明确职责边界，但：

```text
Supporting Contract
!= Dedicated Persistent Object Required
```

Implementation 可根据实际需要：

```text
inline
compose
embed
materialize
cache
split
merge physically
```

但不得破坏已冻结语义。

---

# 6. Referenced Upstream Subjects

F11 不重新创建以下 Domain Object：

```text
Task
Action
Execution Attempt

Change
Decision
Approval
Apply Authorization

Project Instance
Binding
Provider Binding
Version Pin

Result
Evidence
Trace
Provenance

Deferred Obligation
Dependency
Impact
```

F11 对这些对象采用：

```text
Reference / Projection
```

而不是：

```text
Ownership Copy
```

正式：

```text
F11 Reference
!= Subject Ownership
```

---

# 7. ControlSurface

## 7.1 定义

ControlSurface（控制入口）表示：

> 人、系统或外部 Consumer 与 Banyan Control Plane 进行观察、查询、控制或治理交互的入口上下文。

允许包括：

```text
Web
CLI
IDE
API
Mobile
Future Control Surface
```

具体完整目录暂不冻结。

---

## 7.2 责任

ControlSurface 可以决定：

```text
presentation style
interaction mechanism
navigation
interaction density
surface-specific UX
```

但不得决定：

```text
Runtime Permission
Semantic Authority
Provider Binding
Runtime Provider Resolution
Canonical Mutation
```

正式：

```text
ControlSurface
!= Authority

Surface Capability
!= Runtime Permission

Different Surface
!= Different Authority Semantics
```

---

# 8. ControlSession

## 8.1 定义

ControlSession（控制会话）表示：

> 某个 Consumer 通过某个 ControlSurface 进行的一段可关联交互上下文。

可辅助承载：

```text
current viewed subject
pagination
subscription context
temporary presentation preference
reconnect context
```

---

## 8.2 可选性

ControlSession 不作为所有 F11 Interaction 的强制前置条件。

正式：

```text
No ControlSession
!= Invalid F11 Interaction
```

API、CLI 或其他 Stateless Consumer（无状态消费者）可在没有长期 Session 的情况下合法使用 F11。

---

## 8.3 生命周期

正式：

```text
ControlSession
!= Runtime Execution Lifetime

ControlSession Identity
!= Interaction Identity
```

Session 结束、浏览器关闭、IDE 断开或 CLI 退出不自动产生：

```text
Pause
Resume
Retry
Cancel
```

---

# 9. RuntimeProjection

## 9.1 定义

RuntimeProjection（运行时投影）是：

> 针对特定 Purpose（用途）、Consumer、Subject、Scope 和当前 Resolution Basis（解析依据）生成的最小充分可观察状态。

逻辑关系：

```text
Domain / Runtime Truth
↓
Purpose-sensitive Composition
↓
RuntimeProjection
↓
F11 Presentation
```

---

# 10. Projection Subject Model

RuntimeProjection 应保持 Subject-interpretable（主体可解释）。

逻辑上区分：

```text
Primary Subject

Related Subjects

Parent / Child references where applicable
```

例如：

```text
Primary Subject = Task T100
Related Subjects = Action A1 / A2 / A3
```

或：

```text
Primary Subject = Action A3
Parent = Task T100
Current Attempt = EA-04
```

正式：

```text
Primary Projection Subject
!= Subject Ownership
```

---

# 11. Task / Action / Execution Attempt 不得压平

F11 必须保留：

```text
Task != Action != Execution Attempt
```

不得为了 UI 简单将其全部压成：

```text
Job
Run
Operation
```

并丢失治理差异。

例如：

```text
Action A3
Attempt 1 = FAILED
Attempt 2 = FAILED
Attempt 3 = RUNNING
```

不能错误展示成：

```text
Task failed three times
```

应保持：

```text
Task
Action
Current Attempt
Prior Attempt History
```

的语义区别。

---

# 12. RuntimeProjection 允许 Multi-domain Composition

RuntimeProjection 可以根据 Consumer Purpose 组合多个 Domain 已解析结果。

例如：

```text
F10 Runtime State = BLOCKED

F7 Apply Authorization = VALID

F8 Project Gate = HOLD

F9 Freshness Evidence = CURRENT
```

F11 可以组合展示：

```text
Runtime = BLOCKED
Apply Authorization = VALID
Project Gate = HOLD
Freshness = CURRENT

Reason:
Execution currently blocked by Project Gate HOLD.
```

---

# 13. Projection Composition 不产生 Authority Merge

正式：

```text
Projection Composition
!= State-domain Merge

Projection Composition
!= Authority Merge

Multiple Authority References
!= New Combined Authority
```

F11 不得把：

```text
F7 Authorization
+
F8 Gate
+
F10 Runtime Permission
```

压成一个新的：

```text
F11 Global Authorization
```

---

# 14. F11 不创建跨 Domain Global Truth

F11 可以生成：

```text
Presentation Summary
```

例如：

```text
“当前存在 1 个运行阻塞项。”
```

但不得创建并反向驱动执行的：

```text
GLOBAL_SAFE
GLOBAL_BLOCKED
GLOBAL_AUTHORIZED
GLOBAL_APPROVED
```

正式：

```text
Presentation Summary
!= Cross-domain Authoritative State
```

---

# 15. Purpose-sensitive Projection

RuntimeProjection 必须允许按照不同 Purpose 生成不同最小充分内容。

示例：

```text
SUMMARY
→ state
→ short reason
→ attention summary
```

```text
INSPECT
→ current state
→ current attempt
→ reason
→ scope
→ related controls
```

```text
CONTROL
→ current observed basis
→ applicable control hints
→ relevant qualifiers
```

```text
AUDIT
→ result refs
→ trace refs
→ evidence refs
→ provenance refs
```

以上只表示 Purpose 类型示例。

Exact Purpose Enum 暂不冻结。

正式：

```text
Same Subject
+
Different Purpose
may produce different valid Projections
```

---

# 16. RuntimeProjection 不是固定大 DTO

F11-D01 不冻结一份包含全部字段的“大而全 RuntimeProjection Schema”。

正式只要求：

```text
Projection must be purpose-sensitive

Projection must remain subject-interpretable

Projection must preserve required governance qualifiers

Projection must retain source / owner interpretability
```

具体字段、Schema、Transport 留待后续 Decision / Implementation。

---

# 17. RuntimeProjection 与 Truth 的边界

正式：

```text
RuntimeProjection
!= Runtime Truth

RuntimeProjection
!= Canonical Truth

RuntimeProjection
!= Authorization
```

Projection 中包含某个事实，不会把 Truth Ownership 转移给 F11。

例如：

```text
Runtime State Truth Owner = F10
Project Binding Truth Owner = F8
Apply Authorization Owner = F7
```

正式：

```text
Projection Contract Owner
!= Projected Fact Authority Owner
```

---

# 18. Projection Basis

RuntimeProjection 必须逻辑上能够解释：

> 这份投影基于什么 Subject、Scope、状态依据、版本 / Revision Basis、Freshness / Current Applicability Basis 生成。

这里不要求单一：

```text
GlobalBasisObject
```

而是要求：

```text
Basis Preservation
```

正式：

```text
Basis must preserve qualifiers
required for safe interpretation.
```

---

# 19. Projection Freshness

Projection Freshness 不采用简单时间戳等价模型。

正式：

```text
Freshness Basis
!= Elapsed Time

Projection Timestamp
!= Still Valid
```

保护动作仍回到 F10 Point-of-use Revalidation。

---

# 20. Projection Revision

F11 允许逻辑上存在：

```text
Projection Identity
Projection Revision
```

用于表达同一逻辑 Projection 的更新。

但：

```text
Projection Revision
!= Subject Revision

Projection Revision
!= Canonical Revision

Projection Revision
!= Runtime Attempt Revision
```

Projection Revision 只描述 Projection 自身的更新身份。

---

# 21. ExplanationProjection

## 21.1 定义

ExplanationProjection（解释投影）表示：

> 将已有 State、Reason、Evidence Basis 和 Resolution Basis 转换为当前 Consumer 可理解表达的派生投影。

它回答：

```text
Why is this happening?
```

而 RuntimeProjection 主要回答：

```text
What is happening?
```

---

## 21.2 Authority Boundary

正式：

```text
ExplanationProjection
!= New Runtime Fact

ExplanationProjection
!= Reason Authority

Explanation
!= Authority
```

若底层不存在可支持的原因，F11 不得通过 AI 猜测新的 Reason。

---

# 22. EvidenceView

EvidenceView 表示：

> 对已有 Result / Evidence / Trace / Provenance 的查询、摘要、导航与渐进展示。

正式：

```text
EvidenceView
!= Evidence

EvidenceView
!= Evidence Store

EvidenceView
!= Authority
```

F11 不复制另一套 Evidence Truth。

---

# 23. AttentionSignal

## 23.1 定义

AttentionSignal 表示：

> 基于当前 Governed State 派生出的“是否真正需要人类注意”的交互投影。

它与 Notification（通知投递）分离。

正式：

```text
AttentionSignal
!= Notification Delivery
```

---

## 23.2 状态边界

正式：

```text
AttentionSignal
!= Runtime State

Attention Acknowledged
!= Domain State Changed

Attention Cleared
must follow underlying condition resolution
or valid attention re-resolution
```

---

# 24. InteractionSubmission Envelope

F11 允许一个轻量统一交互外壳：

```text
InteractionSubmission
```

其作用仅是帮助承载：

```text
origin
surface context
subject reference
interaction type
basis reference
correlation
```

Exact Schema 暂不冻结。

正式：

```text
InteractionSubmission
!= Universal UserAction

InteractionSubmission
!= Permission
```

---

# 25. Typed Interaction Boundary

F11 必须区分不同交互语义。

逻辑上至少包括：

```text
Query / Inspect Interaction

Runtime Control Intent

Governance Decision Interaction / Input

Attention Acknowledgement

Presentation Interaction
```

具体完整 Enum 暂缓。

正式：

```text
Interaction Mechanism
!= Interaction Meaning
```

“点击按钮”不能自动推导该操作属于：

```text
查看
控制
决策
批准
授权
```

---

# 26. Query / Inspect Interaction

以下类型通常属于查询 / 查看：

```text
Inspect
Read
Expand
Load more detail
Query trace
Query evidence
```

这些行为本身：

```text
!= Runtime Control
!= Human Decision
!= Apply Authorization
```

---

# 27. Presentation Interaction

例如：

```text
分页
过滤
排序
切换 Tab
展开详情
折叠区域
```

默认属于 Presentation Interaction。

F11 不把所有 UI 行为写入：

```text
UniversalControlAction
```

避免 Presentation 与 Governance / Runtime Control 混淆。

---

# 28. RuntimeControlIntent

## 28.1 定义

RuntimeControlIntent 表示：

> Origin 希望对某个 Runtime Subject / Task / Action 采取某种运行控制行为的明确请求。

典型例子：

```text
PAUSE
RESUME
RETRY
CANCEL
```

Exact Intent Catalog 暂不冻结。

---

## 28.2 边界

正式：

```text
RuntimeControlIntent
!= Runtime Permission

RuntimeControlIntent
!= Execution Attempt

RuntimeControlIntent
!= Provider Instruction

RuntimeControlIntent
!= Adapter Instruction

RuntimeControlIntent
!= Execution Implementation Instruction
```

---

# 29. RuntimeControlIntent Basis

RuntimeControlIntent 必须能够保持其 relevant observed basis（相关观察依据）可解释。

例如：

```text
RETRY Action A17
```

应能表达其输入基于：

```text
Observed:
A17 = FAILED
```

若真正处理时：

```text
A17 = RUNNING
```

F10 可判定：

```text
NO_LONGER_APPLICABLE
```

而不是盲目执行。

---

# 30. GovernanceDecisionInteraction

## 30.1 定义

GovernanceDecisionInteraction 表示：

> 当既有 Domain / Decision Protocol 已经判定 Human Decision Required 后，由 F11 用于展示 Decision Context、Alternative 差异并接收明确 Human Input 的治理交互。

F11 不负责创造 Human Decision Requirement。

---

## 30.2 Authority Boundary

正式：

```text
GovernanceDecisionInteraction
!= Decision Authority

GovernanceDecisionInput
!= Governed Decision Record

GovernanceDecisionInput
!= Apply Authorization

Human Decision
!= Runtime Permission
```

---

# 31. Decision Basis Preservation

Governance Decision Input 必须能够针对其 Decision Basis 被解释。

至少逻辑上可恢复：

```text
Decision Subject
Alternatives
Material Differences
Scope
Applicable Context
Relevant Authority / Governance basis
```

例如用户选择：

```text
B
```

不能脱离：

```text
B 当时到底代表什么
```

而永久解释。

正式：

```text
Governance Decision Input
must remain interpretable
against its Decision Basis.
```

---

# 32. Material Decision Basis Change

如果 Decision Interaction 创建后出现：

```text
Material Scope Change
Alternative Meaning Change
New Material Impact
Authority Basis Change
```

不得静默使用旧 Human Input 覆盖新语义。

正确：

```text
Material Decision Basis Changed
→ route Decision Owner
→ determine whether new Human Decision is required
```

F11 本身不拥有该判断的最终 Authority。

---

# 33. Shared Interaction Envelope 不共享 Authority

RuntimeControlIntent 与 GovernanceDecisionInteraction 可以共享：

```text
Stable Identity
Origin
Subject reference
Basis reference
Correlation
Timing / sequence metadata
```

但：

```text
Shared Interaction Envelope
!= Shared Authority Semantics
```

它们的：

```text
Owner
Validation
Routing
Applicability
Outcome
```

仍分别解析。

---

# 34. Stable Interaction Identity

F11 Interaction 必须允许稳定逻辑 Identity。

目的包括：

```text
duplicate delivery handling
cross-session continuity
cross-surface correlation
reconnect
auditability
delivery recovery
```

正式：

```text
Stable Interaction ID
!= Authorization
```

Interaction Identity 不依附单一：

```text
ControlSession
ControlSurface
```

因此：

```text
Interaction Identity
!= ControlSession Identity

Interaction Identity
!= ControlSurface Identity
```

---

# 35. Duplicate Delivery 与 New Intent

必须区分：

```text
same logical intent redelivery
```

与：

```text
new explicit intent
```

例如：

```text
CI-100 RETRY A17
```

网络失败后重发同一 CI-100：

```text
= duplicate delivery
```

若第一次 Retry 已失败，用户再次明确点击 Retry：

```text
= new logical intent
```

正式：

```text
Duplicate Delivery
!= New Intent

New Explicit Intent
!= Revision of Old Intent by default
```

---

# 36. Interaction Revision

允许 Interaction 自身存在 Revision 概念，用于处理同一逻辑交互的非实质更新。

但：

```text
Interaction Revision
!= New Human Intent by default

Interaction Revision
!= New Authority
```

涉及实质 Intent、Scope、Decision Basis 或 Authority 变化时，应按相应 Domain 重新判断，不得通过普通 Revision 静默覆盖。

---

# 37. Interaction Freshness / Applicability

F11 不定义统一 Fixed TTL（固定有效时间）。

不同 Interaction 的有效性依赖：

```text
Interaction Type
Subject State
Observed Basis
Decision Basis
Authority / Governance conditions
```

正式：

```text
Interaction Freshness
= applicability relative to relevant basis
```

而不是：

```text
all interactions valid for N seconds
```

---

# 38. Interaction Status 与 Runtime Outcome 分离

Interaction 逻辑上可以存在处理状态，例如：

```text
Received
Routed
Resolved
No Longer Applicable
Rejected
Accepted for Processing
```

Exact Enum 暂缓。

但正式保持：

```text
Interaction Outcome
!= Runtime Outcome
```

例如：

```text
Retry Intent accepted
```

不表示：

```text
Retry execution succeeded
```

---

# 39. Decision Interaction Capture 与 Decision Acceptance 分离

正式：

```text
Interaction Capture Success
!= Domain Decision Acceptance

Domain Decision Acceptance
!= Apply Authorization

Apply Authorization
!= Runtime Permission
```

F11 成功收到了用户选择，不代表该输入已经完成所有后续治理与执行授权。

---

# 40. InteractionCorrelation

InteractionCorrelation 表示：

> 跨 Interaction、Runtime Resolution、Execution Attempt、Result 或 Decision Resolution 的关联语义。

可用于：

```text
InteractionSubmission
→ RuntimeControlIntent
→ F10 Resolution
→ Execution Attempt
→ Result
```

或：

```text
Decision Requirement
→ GovernanceDecisionInteraction
→ Human Input
→ Domain Decision Resolution
→ downstream consequence
```

---

# 41. Correlation Boundary

正式：

```text
Correlation
!= Authorization

Correlation Chain
!= Lifecycle Ownership Merge
```

关联只回答：

```text
这些事件 / 对象之间是什么关系？
```

不回答：

```text
谁有 Authority？
```

---

# 42. 多 Control Surface 连续性

Stable Interaction Identity 与 Correlation 应允许：

```text
Web submit
↓
Web disconnected
↓
IDE reconnect / inspect
↓
recover current interaction / runtime relationship
```

而不是因为 Surface 改变就重新创建重复 Runtime 操作。

因此：

```text
Surface Change
!= New Intent
```

除非 Consumer 实际产生了新的明确 Intent。

---

# 43. Semantic Nature Classification

F11-D01 正式区分对象的 Semantic Nature（语义性质）：

```text
Truth Reference

Projection

Interaction

Supporting Context

Supporting Relation
```

推荐映射：

| 概念 | Semantic Nature |
|---|---|
| ControlSurface | Supporting / Surface Context |
| ControlSession | Supporting Context |
| RuntimeProjection | Projection |
| ExplanationProjection | Projection |
| EvidenceView | Projection |
| AttentionSignal | Projection |
| InteractionSubmission | Interaction Envelope |
| RuntimeControlIntent | Interaction |
| GovernanceDecisionInteraction | Interaction |
| InteractionCorrelation | Supporting Relation |
| Task / Action / Attempt 等 | Truth Reference |

该分类用于防止 Implementation 把 Projection 误当 Truth。

---

# 44. Core 与 Persistence 分离

正式：

```text
Core Semantic Contract
!= Must Persist

Supporting Contract
!= Semantically Disposable

Persisted Record
!= Canonical Truth
```

对象是否持久化必须根据独立语义需求判断。

---

# 45. Persistence Principle

正式采用：

```text
Persist only when persistence serves
a distinct semantic requirement.
```

即：

> 只有持久化本身解决明确问题时才持久化。

合理 Persistence Reason（持久化理由）包括但不限于：

```text
Deduplication

Cross-session Continuity

Cross-surface Continuity

Auditability

Human Decision Evidence

Delivery Reliability

Process Restart Recovery

Required History
```

以下不是充分理由：

```text
“这个对象存在于架构图中”
```

---

# 46. RuntimeProjection Persistence

RuntimeProjection 默认：

```text
Derived
Freshness-sensitive
Rebuildable
```

正式：

```text
RuntimeProjection
= Rebuildable by default
```

Projection 不因为被生成过就成为永久历史事实。

正式：

```text
Projection Persistence
requires independent retention reason.
```

---

# 47. Projection 与 History 分离

Runtime 历史应优先通过真正的：

```text
Result
Trace
Evidence
Attempt History
```

保存。

不应使用：

```text
Every UI Projection Snapshot
```

作为新的历史 Truth Store。

---

# 48. Materialized Projection

未来为了性能，可以存在：

```text
Materialized Projection
```

即被缓存或物化的 Projection。

但：

```text
Materialized Projection
!= Canonical Truth

Materialized Projection
!= Authority Promotion

Cache Hit
!= Permission Valid
```

保护动作仍须依据当前规则重新验证。

---

# 49. Derived Projection Rebuildability

对于：

```text
RuntimeProjection
ExplanationProjection
EvidenceView
AttentionSignal
```

默认要求具备：

```text
Rebuildable from authoritative / current sources
```

正式：

```text
Loss of Derived Projection
!= Loss of Domain Truth
```

---

# 50. RuntimeControlIntent Persistence

RuntimeControlIntent 属于：

```text
Durable-eligible Interaction
```

在需要：

```text
deduplication
audit
cross-session continuity
restart recovery
delivery reliability
```

时可以持久化。

但：

```text
Durable Intent Record
!= Durable Runtime Permission
```

系统重启后发现旧 Intent Record，不得因为记录存在就绕过 Current Revalidation。

---

# 51. Governance Decision Persistence

GovernanceDecisionInteraction 的展示本身默认可以：

```text
Derived / Rebuildable
```

但 Human explicit input（人的明确输入）在需要治理证据时应支持：

```text
Durable / Auditable Capture
```

F11 可以捕获并可靠传递。

但：

```text
Captured Decision Input
!= Governed Decision Record
```

真正 Governed Decision Record 仍由对应 Domain / Decision Owner 管理。

---

# 52. Explanation Persistence

ExplanationProjection 默认：

```text
Rebuildable
```

不要求所有自然语言解释长期保存。

只有存在独立治理理由，例如：

```text
需要证明某次 Human Decision 当时向用户展示了什么 Minimum Sufficient Decision Context
```

时，才可能持久化相应 Decision Context Snapshot。

正式：

```text
Persistence Reason
must come from semantic need,
not object existence.
```

---

# 53. EvidenceView Persistence

正式：

```text
EvidenceView
= Derived / Read-oriented by default
```

F11 不通过保存 EvidenceView 创建新的 Evidence Store。

---

# 54. AttentionSignal Persistence

AttentionSignal 默认：

```text
Derived
Recomputable
```

当前不冻结：

```text
Durable Inbox
Notification History
SLA Queue
Attention Database
```

正式：

```text
AttentionSignal
!= Durable Inbox Item by default
```

该部分留给 F11-D07 进一步讨论。

---

# 55. ControlSession Persistence

ControlSession 默认：

```text
Ephemeral / Short-lived
```

未来可持久化：

```text
UI preference
last viewed subject
filter preference
layout preference
```

但：

```text
Session Persistence
!= Runtime Persistence

UX Preference
!= Governance Truth
```

---

# 56. InteractionCorrelation Persistence

InteractionCorrelation 是：

```text
Durable-eligible Supporting Relation
```

可通过：

```text
references
trace fields
relation records
```

等不同实现方式表达。

正式：

```text
Correlation Semantic
must exist

Dedicated Correlation Storage Object
is implementation-deferred
```

---

# 57. F11 不建立 Shadow Truth Store

F11 不得因为“查询方便”默认复制：

```text
Runtime State

Project Binding State

Apply Authorization

Evidence

Trace

Decision Truth
```

形成自己的长期 authoritative copy。

正式：

```text
F11 Control Plane Store
!= Shadow Authority Store
```

如果 Implementation 使用：

```text
cache
projection store
search index
frontend state
Redis
materialized view
```

其语义仍必须保持：

```text
Projection / Cache / Index
!= Canonical Truth
!= Authority
```

---

# 58. Owner Boundary Matrix

| 语义 | Owner |
|---|---|
| ControlSurface Interaction Semantics | F11 |
| RuntimeProjection Contract | F11 |
| Explanation Presentation Contract | F11 |
| Evidence Navigation / View Contract | F11 |
| Attention Interaction Semantics | F11 |
| RuntimeControlIntent Capture / Routing Contract | F11 |
| GovernanceDecisionInteraction UX Contract | F11 |
| Runtime State Truth | F10 |
| Runtime Permission | F10 |
| Runtime Provider Resolution | F10 |
| Execution Attempt Lifecycle | F10 |
| Product / Requirement Authority | F5 |
| Design / UI Truth Authority | F6 |
| Change / Apply Authorization / Canonical Apply | F7 |
| Project Instance / Binding / Provider Binding | F8 |
| Index / Context / Dependency / Impact / Freshness lookup | F9 |
| Informed Decision trigger / orchestration semantics | F4 + applicable Domain Governance |
| Governed Decision Record | applicable Domain Owner |

---

# 59. Owner 与 Projection Owner 分离

正式：

```text
Projection Contract Owner
!= Projected Fact Authority Owner

GovernanceDecisionInteraction Owner
!= Decision Authority Owner

EvidenceView Owner
!= Evidence Authority Owner

ExplanationProjection Owner
!= Reason Truth Owner

AttentionSignal Owner
!= Underlying Blocker Owner
```

---

# 60. Authority 分离不等于碎片化查询

虽然 Truth Owner 不同，但 F11 不要求每次页面展示都分别实时调用所有 Domain。

允许：

```text
Purpose-sensitive Composed Projection
```

其中包含必要：

```text
state
owner refs
authority refs
freshness basis
reason refs
control hints
```

因此：

```text
Authority Separation
!= Query Fragmentation
```

F9 / F10 等现有 Index、Context、Handoff 和 Runtime Projection 能力应被复用。

---

# 61. F11-D01 核心不变量

正式冻结：

```text
Logical Object
!= New Canonical Truth

Logical Object
!= New DefinitionArtifact by default

Core Semantic Contract
!= Must Persist

Supporting Contract
!= Semantically Disposable

Persisted Record
!= Canonical Truth

Projection Contract Owner
!= Projected Fact Authority Owner

Primary Projection Subject
!= Subject Ownership

Task
!= Action
!= Execution Attempt

RuntimeProjection
!= Runtime Truth

RuntimeProjection
!= Canonical Truth

RuntimeProjection
!= Authorization

Projection Composition
!= State-domain Merge

Projection Composition
!= Authority Merge

Multiple Authority References
!= New Combined Authority

Projection Revision
!= Subject Revision

Projection Revision
!= Canonical Revision

Presentation Summary
!= Cross-domain Authoritative State

ExplanationProjection
!= New Runtime Fact

EvidenceView
!= Evidence Store

AttentionSignal
!= Runtime State

AttentionSignal
!= Durable Inbox Item by default

InteractionSubmission
!= Universal UserAction

InteractionSubmission
!= Permission

Interaction Mechanism
!= Interaction Meaning

RuntimeControlIntent
!= Runtime Permission

RuntimeControlIntent
!= Execution Attempt

RuntimeControlIntent
!= Execution Implementation Instruction

GovernanceDecisionInteraction
!= Decision Authority

GovernanceDecisionInput
!= Governed Decision Record

GovernanceDecisionInput
!= Apply Authorization

Interaction Identity
!= ControlSession Identity

Interaction Identity
!= ControlSurface Identity

Stable Interaction ID
!= Authorization

Duplicate Delivery
!= New Intent

New Explicit Intent
!= Revision of Old Intent by default

Interaction Outcome
!= Runtime Outcome

Interaction Capture
!= Domain Decision Acceptance

Shared Interaction Envelope
!= Shared Authority Semantics

User Input
must remain basis-interpretable

F11 Basis Preservation
!= Freshness Authority

Correlation
!= Authorization

Correlation Chain
!= Lifecycle Ownership Merge

Projection Persistence
requires independent retention reason

RuntimeProjection
= Rebuildable by default

Durable Intent Record
!= Durable Runtime Permission

Captured Decision Input
!= Governed Decision Record

Loss of Derived Projection
!= Loss of Domain Truth

Materialized Projection
!= Authority Promotion

Cache Hit
!= Permission Valid
```

---

# 62. Explicitly Forbidden Designs

F11-D01 明确禁止将以下方式提升为正式架构：

```text
Universal ControlPlaneState as authoritative truth

Universal UserAction

F11Task / F11Action / F11Attempt copies

F11 Evidence Store copied from source Evidence

F11 GlobalAuthorization

F11 GlobalSafeState

F11 Decision Truth copied from Domain Owner

ControlSession as Runtime lifecycle owner

ControlSurface-specific Authority

Every Projection permanently persisted by default

Every AttentionSignal permanently persisted by default

Interaction ID used as permission grant

Cached UI state used as protected-action permission
```

---

# 63. Deferred

F11-D01 明确暂缓：

```text
Exact Object Schema

Exact Field Names

Exact Stable ID Format

Exact Revision Format

Exact Interaction Enum

Exact Projection Purpose Enum

Exact Interaction Status Enum

Exact RuntimeControlIntent Catalog

Exact GovernanceDecisionInput Schema

Exact Projection Freshness Algorithm

Exact Interaction Expiry Rules

Exact Storage Technology

Exact Database Tables

SQLite Physical Schema

Redis Design

Exact Cache Strategy

Exact Materialized View Strategy

Exact API Contract

Exact Transport

WebSocket / SSE / Polling

Exact Go Struct

Exact TypeScript Interface

Exact UI Store Model

Exact Durable Inbox Model
```

这些事项只有在后续主题确实需要时再冻结。

---

# 64. 与 F11 后续 Decision 的关系

F11-D01 提供 F11 后续主题的对象与责任基础。

后续建议：

```text
F11-D02
→ Runtime Projection & State Presentation

F11-D03
→ Control Intent & Point-of-use Revalidation Handoff

F11-D04
→ Human Decision UX & Informed Decision Interaction

F11-D05
→ Reason / Blocker / Explanation Model

F11-D06
→ Result / Trace / Evidence / Provenance Presentation

F11-D07
→ Notification & Human Attention Governance

F11-D08
→ Multi-Surface / Session / Delivery Consistency
```

后续 Decision 可以细化本稿对象，但不得违反本稿 Owner / Authority / Truth / Persistence 边界。

---

# 65. Approval Effect

本稿已经明确：

```text
F11-D01 HUMAN_APPROVED
```

因此正式冻结：

```text
F11 Control Plane logical object model

Core vs Supporting semantic contract boundary

Referenced upstream subject boundary

RuntimeProjection responsibility model

Projection Subject / Purpose / Basis model

Multi-domain projection composition boundary

Typed Interaction boundary

RuntimeControlIntent logical identity

GovernanceDecisionInteraction logical boundary

Interaction Identity / Revision / Basis / Correlation principles

Derived vs Durable persistence principles

F11 shadow-truth-store prohibition

Cross-stage Owner preservation
```

但不代表：

```text
Physical Schema Frozen

Database Frozen

SQLite Schema Frozen

API Frozen

Enum Frozen

Transport Frozen

Web UI Frozen

Implementation Authorized

RP2 Authorized

Authority Cutover Authorized

Canonical Replacement Authorized

Final Activation Authorized
```

---

# 66. Final Frozen Decision

```text
F11-D01
— Control Plane Core Object & Responsibility Model

STATUS:
HUMAN_APPROVED / FROZEN

F11 uses a minimum sufficient logical object model.

ControlSurface / RuntimeProjection /
Typed Interaction / RuntimeControlIntent /
GovernanceDecisionInteraction
form the Core Semantic Contracts.

ControlSession / InteractionSubmission /
ExplanationProjection / EvidenceView /
AttentionSignal / InteractionCorrelation
remain Supporting Semantic Contracts.

F11 references Task / Action / Attempt and other
upstream governed subjects without copying ownership.

RuntimeProjection may compose multi-domain facts,
but composition does not merge truth or authority.

Task != Action != Execution Attempt.

Projection != Truth.

Interaction != Permission.

Governance Decision Interaction != Decision Authority.

Stable Interaction Identity supports continuity,
deduplication and correlation,
but never grants authorization.

Derived projections are rebuildable by default.

Persistence requires an independent semantic reason.

Durable interaction records do not become
durable runtime permission.

Captured Human Decision Input does not become
the governed Decision Record merely because
F11 persisted or received it.

F11 must not become a shadow Runtime /
Evidence / Decision / Authority store.

Implementation remains NOT_AUTHORIZED.
```

---

**END OF F11-D01 HUMAN_APPROVED FREEZE**

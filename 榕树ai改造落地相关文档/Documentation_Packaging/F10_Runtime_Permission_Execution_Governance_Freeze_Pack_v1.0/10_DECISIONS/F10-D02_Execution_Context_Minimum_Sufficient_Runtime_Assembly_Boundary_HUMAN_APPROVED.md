# F10-D02 — Execution Context × Minimum Sufficient Runtime Assembly Boundary

**阶段：** F10 — Runtime Permission / Execution Governance Architecture  
**主题：** Execution Context（执行上下文）× Minimum Sufficient Runtime Assembly（最小充分运行时组装）边界  
**状态：** `HUMAN_APPROVED`  
**上游依赖：**
- `F10-G01 HUMAN_APPROVED`
- `F10-D01 HUMAN_APPROVED`

**Implementation Authorization：** `NO`

---

## 1. 决策目的

F10-D02 解决：

> 当某个具体 Action（动作）已经准备进入 Runtime Permission（运行时许可）判断和实际执行链时，F10 到底应该拿着哪些信息执行，以及这些信息如何做到既足够可靠，又不退化成全仓扫描、全量上下文加载和重复治理。

核心目标：

```text
Current Action
↓
Resolve what this action actually needs
↓
Reuse stable governed basis
+
Load action-specific context
+
Attach current runtime state
↓
Minimum Sufficient Execution Context
↓
Permission / Execution
```

F10-D02 不建立第二套 Project Truth、第二套 F9 Context System 或第二套 Authority System。

---

## 2. Execution Context 定义

Execution Context（执行上下文）定义为：

> 针对当前一个 Task / Action，从已有 Project Context、Task Context、F9 当前有效上下文、Authorization / Gate 等治理依据以及当前 Runtime State 中，按用途组合出来的最小充分运行时工作包。

正式：

```text
Execution Context
=
Inherited Governed Basis
+
Action-specific Projection
+
Current Runtime State
```

---

## 3. Execution Context 的基本性质

Execution Context 必须保持：

```text
Task / Action Scoped
Purpose-specific
Minimum Sufficient
Derived
Rebuildable
Context-aware
Governance-preserving
```

因此：

```text
Execution Context
!= Canonical Truth

Execution Context
!= Global Project Truth

Execution Context
!= New Authority
```

---

## 4. 三层逻辑 Context

F10-D02 正式区分三个逻辑层次：

```text
Project Context
↓
Task Context
↓
Action Execution Context
```

这是逻辑责任划分，不要求实现成三个固定物理对象。

---

## 5. Project Context

Project Context 回答：

> 当前任务属于哪个 Project / Project Instance，这个 Project 当前如何使用 Banyan。

主要由 F8 领域提供或解析。

可能包括：

```text
Project Reference
Project Instance
Source / Location Binding
Applicable Profile
Provider Binding
Version
Feature / Gate
Boundary References
Project-level Effective State
```

F10 不重新成为 Project Context Authority。

---

## 6. Task Context

Task Context 回答：

> 当前这一次任务是什么、解决什么问题、涉及哪些语义范围以及哪些治理依据。

可能组合来自：

```text
Requirement
Design
Task Scope
Applicable Rules
Change / Apply references
Dependency / Impact
Current Effective Context
Authorization references
```

Task Context 不要求每个 Action 全量加载。

---

## 7. Action Execution Context

Action Execution Context 回答：

> 当前这一个具体动作真正执行时，需要哪些最小充分信息。

例如：

```text
Action Reference
Action Type
Target
Current Effective Scope
Relevant Requirement Slice
Relevant Design Slice
Relevant Code / Data Slice
Applicable Rule Slice
Applicable Authorization
Required Gate / Preconditions
Expected Base
Provider Runtime Context
Adapter Runtime Context
Runtime Permission Basis
Relevant Freshness / State
```

---

## 8. Project Context != Task Context != Action Context

正式：

```text
Project Context
!= Task Context

Task Context
!= Action Execution Context

Action Execution Context
!= Entire Task Context Copy
```

后一级可以引用和投影前一级，但不要求复制全部内容。

---

## 9. F8 Runtime Handoff × D02

F8 已经拥有：

```text
Task / Action Scoped
Minimum Sufficient
Derived
Rebuildable
Project Instance Runtime Handoff
```

因此 D02 不创建第二套 Project Instance Runtime Handoff。

正式：

```text
F8 Runtime Handoff
→ Input to F10 Execution Context

F10 Execution Context
!= Replacement for F8 Runtime Handoff
```

---

## 10. F8 Runtime Handoff 的作用

F8 可向 F10 提供当前动作相关的：

```text
Project Ref
Scope
Effective Bindings
Applicable Profile
Effective Provider
Effective Version
Feature / Gate State
Boundary Refs
Authority / Evidence Refs
UNKNOWN / BLOCKED
```

F10 使用这些结果，但不得把它们复制成第二份 Project Truth。

---

## 11. F9 Context Assembly × D02

F9 继续拥有：

```text
Index
Search / Retrieval
Context Selection
Context Assembly
Freshness
Dependency / Impact Lookup
Targeted Recovery
Projection / Cache support
```

F10-D02 不建立竞争的：

```text
Runtime Index
Second Search Engine
Second Repository-wide Context Resolver
```

---

## 12. F10 对 F9 的使用方式

当当前 Action 缺少必要 Context 时：

```text
F10 identifies required missing context
↓
F9 targeted retrieval / assembly
↓
Applicable validation
↓
Attach required slice
↓
Continue
```

正式：

```text
F10 Context Need
!= F10 owns repository-wide retrieval
```

---

## 13. Execution Context × Runtime Permission

D01 已冻结 Runtime Permission 所需逻辑输入。

D02 的责任是：

> 为当前 Action 提供这些输入需要的最小充分 Context Envelope（上下文包络）。

因此：

```text
Execution Context
→ Runtime Permission Input
```

但：

```text
Execution Context Ready
!= Runtime ALLOW
```

---

## 14. Context Ready != Authorized

正式：

```text
Context Ready
!= Authorization Valid

Context Ready
!= Runtime Permission

Context Ready
!= Execution Authorized
```

上下文准备完成只是运行时判断的输入条件之一。

---

## 15. Minimum Sufficient 原则

Execution Context 必须遵循：

```text
Minimum Sufficient
!= Minimum Possible
```

“最小充分”不是越少越好。

正确含义：

> 不携带与当前动作无关的内容，但不能删除会改变 Scope、Authority、Validity、Freshness、Gate 或合法性的治理关键信息。

---

## 16. Context Compression != Governance Compression

正式：

```text
Context Compression
!= Governance Compression
```

允许压缩：

```text
irrelevant details
duplicate evidence body
unrelated module content
unneeded history
```

禁止压缩掉：

```text
Scope
Authority Basis
Authorization Envelope
Applicability
Expected Base
Freshness Basis
Gate Result
HOLD
BLOCKED
UNKNOWN
STALE
Deferred Guard
Material Downstream Obligation
```

如果这些内容与当前 Action 的合法性有关。

---

## 17. Purpose-sensitive Context

不同 Action 可以拥有不同 Execution Context。

例如同一个商品任务：

```text
Action A = Frontend Edit
Action B = Backend Edit
Action C = Test
Action D = Git Diff Validation
```

每个动作只加载自己需要的内容。

正式：

```text
Same Task
!= Same Execution Context for Every Action
```

---

## 18. Frontend Action 示例

例如：

```text
Action = Edit tenant-admin goods page
```

可能需要：

```text
Relevant Product Requirement
Relevant Design Constraint
Frontend Component
API Client Contract
Frontend Engineering Rules
Current Target State
Authorization
Expected Base
Provider / Adapter Runtime Context
```

不要求默认加载全部 backend / miniapp / platform-admin。

---

## 19. Backend Action 示例

同一任务下：

```text
Action = Edit backend goods API
```

可能需要：

```text
Relevant Business Requirement
Handler / Service / Model
API Contract
Backend Engineering Rules
Dependency Slice
Authorization
Expected Base
Provider / Adapter Runtime Context
```

不要求继续携带与后端动作无关的 UI 视觉细节。

---

## 20. Discoverable != Loaded

正式：

```text
Discoverable
!= Loaded
```

某个信息未来可能有用，不等于当前 Action 必须立即加载。

正确：

```text
Known Required
→ Load

Potentially Relevant
→ Keep discoverable reference

Actually Required Later
→ Resolve when needed
```

---

## 21. Potential Impact != Immediate Context Expansion

F9 发现：

```text
Potential Impact
```

不自动意味着：

```text
Load all impacted targets into current Execution Context
```

只有当前 Action 实际需要的内容才进入当前工作包。

---

## 22. Stable Basis × Volatile Runtime Slice

Execution Context 逻辑上区分：

```text
Stable Governed Basis
+
Volatile Runtime Slice
```

以同时满足速度和可靠性。

---

## 23. Stable Governed Basis

相对稳定、可复用的依据可能包括：

```text
Project Identity Ref
Task Identity
Approved Requirement Ref
Applicable Design Ref
Authorization Basis
Stable Rule Ref
Pinned Revision / Version Basis
```

只要其相关性和有效性没有发生 Material Change（实质变化），就不要求反复重新解析。

---

## 24. Volatile Runtime Slice

容易发生变化的运行时内容可能包括：

```text
Target Current State
Expected Base observation
Git / Workspace state
Provider Health
Current Gate Result
Freshness State
Runtime Permission Result
Current Environment State
```

这些应根据当前 Action 的需要进行 Point-of-use Validation（使用点校验）。

---

## 25. Stable Basis != Eternal Basis

即使某内容相对稳定：

```text
Stable
!= Eternal
```

如果其：

```text
Revision
Applicability
Authority
Scope
Supersession
Validity
```

发生 Material Change，则仍应重新解析。

---

## 26. Context Inheritance

允许 Action Context 逻辑继承：

```text
Project-level basis
+
Task-level basis
```

然后只附加：

```text
Action-specific projection
+
Current runtime slice
```

正式：

```text
Context Inheritance
!= Full Context Duplication
```

---

## 27. Context Overlay / Local Override Boundary

允许针对当前 Action 增加局部运行时信息。

但：

```text
Action-local Runtime Override
```

不得静默覆盖：

```text
Canonical Truth
Authority
Authorization Envelope
Project Binding
Governed Scope
```

因此：

```text
Runtime Overlay
!= Governance Override
```

---

## 28. Dynamic Context Expansion

Action 执行过程中发现确实缺少必要信息时，允许 Execution Context 动态扩展。

正式：

```text
Execution Context Expansion
must be

Need-driven
+
Scope-bounded
+
Authorization-bounded
+
Governance-preserving
```

---

## 29. Context Expansion != Scope Expansion

正式区分：

```text
Load More Relevant Context
!= Material Scope Expansion
```

例如原任务已经授权：

```text
tenant-admin.goods
+
backend.goods
```

前端 Action 后续需要读取 backend API contract：

```text
Context Expansion
→ allowed
```

因为仍在既有任务与授权包络内。

---

## 30. Context Expansion 不得绕过 D01

如果为继续执行而需要进入：

```text
new business domain
new protected target
new authority domain
outside authorization envelope
```

则：

```text
Context Need
does not authorize
Scope Expansion
```

必须回到 D01 已冻结的治理路径。

---

## 31. More Context != More Authority

正式：

```text
More Loaded Context
!= Wider Authorization

More Evidence
!= Higher Authority

More Repository Visibility
!= More Execution Permission
```

Context 只影响“知道什么”，不自动扩大“允许做什么”。

---

## 32. Provider Context Boundary

Provider 可以消费当前 Action 所需的 Execution Context。

但：

```text
Provider
!= Context Authority
```

Provider 不得因为自身方便：

```text
silently expand scope
load unrestricted project context
reinterpret authorization
replace canonical context
```

---

## 33. Provider Missing-input Request

如果 Provider 发现缺少必要信息，可以返回：

```text
Required Context Need
```

F10 根据需要路由：

```text
F9 retrieval
F8 project resolution
Applicable owner
```

然后重新组装相关 Execution Context。

Provider 不自行把 UNKNOWN 猜成事实。

---

## 34. Adapter Context Boundary

Adapter 只消费执行通道真正需要的信息。

例如：

```text
Target
Operation
Expected Base
Required Runtime Permission
Relevant Execution Parameters
```

Adapter 不需要默认获得完整 PRD、完整设计包或整个 Project Context。

---

## 35. Adapter != Context Resolver

正式：

```text
Adapter
!= Project Context Resolver

Adapter
!= Task Context Authority

Adapter
!= Authorization Resolver
```

Adapter 的核心责任仍然是执行技术动作，而非重新解释治理语义。

---

## 36. Context Slice 组合能力

D02 允许 Execution Context 由多个可组合的 Purpose-specific Slice（用途切片）组成，例如：

```text
Requirement Slice
Design Slice
Code Slice
Rule Slice
Data Slice
Git Slice
Provider Slice
Test Slice
Authorization Slice
Runtime State Slice
```

具体类型集合不在 D02 冻结。

---

## 37. No Giant Fixed ExecutionContext Object

D02 不要求建立：

```text
ExecutionContext {
    every_possible_field...
}
```

禁止为了方便形成 Runtime God Object（运行时万能对象）。

推荐逻辑：

```text
Common Governed Envelope
+
Purpose-specific Context Slices
```

---

## 38. Common Governed Envelope

Execution Context 的公共治理包络逻辑上至少应能保持当前动作所需的：

```text
Project Ref
Task Ref
Action Ref / Purpose
Scope
Target
Applicable Governance References
Authorization / Authority References where required
Material State Qualifiers
Resolution / Freshness Basis where required
Provenance
```

不是所有字段对所有 Action 都必须存在。

---

## 39. Optional / Purpose-specific Parts

根据 Action 需要再附加：

```text
Code Context
Design Context
Requirement Context
Test Context
Provider Context
Adapter Context
Git Context
Data Context
Other Future Context
```

保持可扩展。

---

## 40. Context Identity Boundary

Execution Context 可以有临时 Identity / Reference 便于 Trace 或复用。

但：

```text
Execution Context Identity
!= Domain Stable Identity
```

不得因此建立与 F7 Stable ID / Revision Governance 竞争的第二套长期身份体系。

---

## 41. Execution Context 生命周期

Execution Context 默认是：

```text
Action-scoped
or
Short-lived Task-scoped derived state
```

不自动成为永久 Project Artifact。

---

## 42. Rebuildable

正式：

```text
Execution Context
must be logically rebuildable
from governed sources and derived state
```

因此不能让一个不可追溯的临时 Context 成为唯一 Truth。

---

## 43. Context Cache / Reuse

为了速度，可以：

```text
Cache
Reuse
Project
Share stable slices
```

但必须遵循：

```text
Cached Context
!= Eternal Context
```

---

## 44. Reuse Boundary

只有相关 Material Basis（重要依据）仍有效时，才能复用 Context Slice。

例如：

```text
same target basis
same relevant scope
same required revision/version basis
same applicable rule basis
same freshness requirement satisfied
```

才可安全复用。

---

## 45. F9 Freshness 复用

F10 不建立第二套通用 Freshness System。

正式：

```text
Execution Context Freshness
→ reuse F9 Freshness / Basis mechanisms where applicable
```

不是：

```text
F10 invents separate freshness truth
```

---

## 46. Cached Context Miss

正式：

```text
Context Cache Miss
!= Context Invalid

Context Cache Miss
!= Permission Denied
```

Cache Miss 时：

```text
Targeted Rebuild
```

即可。

---

## 47. Cached Context Stale

如果相关 Slice 被判定 stale：

```text
Stale Slice
→ targeted refresh / re-resolution
```

不要求重新创建整个 Task Context。

---

## 48. Selective Invalidation

某个 Context Slice 发生变化，不自动使全部 Execution Context 无效。

例如：

```text
Provider Health changed
```

可能只需刷新：

```text
Provider Runtime Slice
```

而不是重载全部 Requirement / Design / Code Context。

正式：

```text
Localized Change
→ Localized Revalidation where sufficient
```

---

## 49. Dependency-aware Invalidation

若某个变化会影响多个 Slice，则按真实 Dependency（依赖）进行定向失效。

禁止：

```text
Any Change
→ Invalidate Everything
```

也禁止：

```text
Any Change
→ Ignore Everything
```

---

## 50. Point-of-use Context Check

在受保护动作真正执行前：

```text
Action Execution Context
+
D01 Point-of-use Validation
```

共同确认关键运行依据仍成立。

正式：

```text
Context Assembled Earlier
!= Context Automatically Valid Forever
```

---

## 51. Context Missing Boundary

如果当前 Action 缺少必要 Material Context：

```text
Missing Material Context
!= Assume Default
```

应优先：

```text
Determine Source / Owner
→ Targeted Resolve
→ Attach
→ Re-evaluate
```

---

## 52. Missing Context != Human Input

正式：

```text
Missing Context
!= Human Input Required
```

如果可以通过：

```text
F8
F9
F7
Other governed owner
Current project source
```

自动取得，就不得默认询问用户。

---

## 53. Context Conflict

如果不同来源提供的内容形成真实 Material Conflict（实质冲突）：

```text
Execution Context Assembly
must not pick arbitrary winner
```

正确：

```text
Preserve conflict
→ Route applicable owner / resolver
```

---

## 54. Evidence Boundary

Execution Context 可以携带：

```text
Evidence Ref
Relevant Claim
Provenance
```

不要求复制整个 Evidence Body。

正式：

```text
Evidence Projection
!= Full Evidence Duplication
```

---

## 55. Provenance Boundary

重要 Context Slice 应在需要时能够回答：

```text
Where did this come from?
For what purpose?
For what scope?
Based on what revision/version/current state?
```

但：

```text
Provenance
!= Authority
```

---

## 56. Requirement / Design Context Boundary

F10 可以消费相关 Requirement / Design Slice。

但：

```text
Execution Context Projection
!= Product Interpretation Authority

Execution Context Projection
!= Design Interpretation Authority
```

发现语义不一致时应回对应 Owner。

---

## 57. Code Reality Boundary

当前代码可以作为：

```text
Current Implementation Reality
Runtime Evidence
Target Context
```

但：

```text
Current Code
!= Product Truth

Current Code
!= Design Truth

Current Code
!= Architecture Authority
```

---

## 58. Runtime State Boundary

F10 可以向 Execution Context 附加当前运行态，例如：

```text
Permission Basis
Provider Availability
Adapter Readiness
Pause / Block State
Current Attempt Ref
Current Environment State
```

这些是 Runtime State，不自动进入上游 Canonical Truth。

---

## 59. Action Result 不自动写回 Context Truth

一次 Action 完成后产生的：

```text
Result
Observation
Trace
```

可以成为后续 Context 输入证据。

但：

```text
Execution Result
!= Automatic Canonical Context Update
```

是否成为新的 Current Effective 状态由对应 Owner 决定。

---

## 60. Task 内 Context Continuity

同一个 Task 的多个 Action 可以共享：

```text
stable governed basis
valid cached slices
resolved references
```

避免重复加载。

但每个 Action 仍必须根据自己需要形成适用的 Execution Context。

---

## 61. Cross-action Leakage Boundary

Action A 加载的所有临时信息，不自动进入 Action B。

正式：

```text
Previous Action Context
!= Next Action Required Context
```

只共享仍相关且仍有效的部分。

---

## 62. Cross-module Development

同一 Project 内一个任务可以自然跨：

```text
tenant-admin
backend
shared
miniapp
other governed modules
```

只要仍在 Task / Authorization Envelope 内。

D02 不把跨模块 Context 加载解释成跨 Project。

---

## 63. Cross-project Boundary

如果当前动作真正需要另一个独立 Project Identity 的信息或执行目标，则必须依据适用跨 Project Governance 解析。

不能因为仓库物理上在一起就默认属于当前 Project。

---

## 64. Git Repository Boundary

正式保持：

```text
Repository Visibility
!= Project Scope

Repository Path
!= Semantic Scope
```

因此 Execution Context Assembly 不能简单使用：

```text
same Git repo
→ load / authorize everything
```

---

## 65. Context Loading × Security Boundary

D02 采用最小必要暴露原则：

```text
Current Action
receives only context materially needed
for its governed purpose
```

D02 不要求把：

```text
credentials
secrets
unrelated protected data
```

复制进通用 Execution Context。

具体 Credential / Secret Handling（凭据/密钥处理）机制不在 D02 冻结。

---

## 66. Capability Reference != Secret Copy

未来如 Provider / Adapter 执行需要 Credential 或 Capability：

```text
Context may carry governed reference / capability handle
```

不因此要求：

```text
copy raw credential into every context
```

具体实现延后。

---

## 67. Performance Boundary

D02 明确禁止：

```text
Every Action
→ Full Repo Scan

Every Action
→ Full Rule Load

Every Action
→ Full Task Replay

Every Action
→ Full Evidence Duplication

Every Action
→ Re-ask User
```

---

## 68. Targeted Loading Principle

正确路径：

```text
Action
↓
Scope / Purpose
↓
Relevant Basis
↓
Required Context Slices
↓
Targeted Retrieval / Validation
↓
Execution Context Ready
```

---

## 69. Speed != Governance Loss

正式：

```text
Fast Context Assembly
!= Drop Governance Qualifiers
```

性能优化不得依赖：

```text
ignore Authority
ignore Scope
ignore Freshness
ignore BLOCK / HOLD
ignore Expected Base
```

---

## 70. Context Size 不作为唯一优化目标

D02 不冻结：

```text
Fixed token limit
Fixed file count
Fixed context byte size
```

因为不同 Action 的最小充分量不同。

正确目标：

```text
Relevance
+
Sufficiency
+
Governance Completeness
+
Efficiency
```

---

## 71. Future Provider / Technology Extensibility

Execution Context 不应硬编码：

```text
Cursor only
Codex only
OpenAI only
Vue only
Go only
Git only
```

应允许未来不同：

```text
Provider
Editor
Language
Framework
Adapter
Execution Environment
```

消费适用 Context Slice。

---

## 72. Context Contract 与技术栈解耦

例如：

```text
Relevant Requirement
Applicable Scope
Expected Base
Authorization Basis
```

这些治理语义不应因为执行技术栈从 Vue 改 React、从 Go 改其他语言而改变。

---

## 73. No Context God Object

明确禁止把 F10 演化成：

```text
one giant context object
containing every project fact
every rule
every file
every authorization
every evidence
every runtime state
```

这会破坏：

```text
flexibility
performance
owner boundaries
freshness control
```

---

## 74. No Second Truth Store

D02 不授权建立：

```text
Execution Context Canonical Store
Second Project Truth Database
Second Requirement Truth
Second Design Truth
Second Binding Truth
```

Execution Context 是派生运行态。

---

## 75. No Second Context Governance Domain

F10-D02 不吞并：

```text
F8 Project Context Governance
F9 Retrieval / Context Assembly Governance
F7 Change / Apply Governance
F5 Product Governance
F6 Design Governance
```

它只负责当前执行用途的组合和消费。

---

## 76. Deferred / Blocked State Preservation

如果上游当前有效交接中存在：

```text
UNKNOWN
BLOCKED
HOLD
STALE
Deferred Guard
```

且与当前 Action 相关，则不能在 Execution Context 组装时静默丢失。

---

## 77. Negative State Preservation

正式：

```text
UNKNOWN
cannot become PASS by projection

BLOCKED
cannot disappear by context compression

HOLD
cannot become ALLOW by omission
```

---

## 78. Context Expansion × Human Decision

Context 动态补齐本身通常是确定性工作。

因此：

```text
Need More Context
!= Human Decision
```

只有补齐过程中发现：

```text
Material Semantic Conflict
Authority Conflict
Material Scope Expansion
Multiple Legitimate Incompatible Choices
```

才进入 Human Governance。

---

## 79. Normal Developer Experience

正常开发应表现为：

```text
用户提出任务
↓
Banyan 自动解析 Project / Task
↓
按当前 Action 自动准备最小上下文
↓
缺资料自动定向补齐
↓
运行时校验
↓
继续执行
```

而不是：

```text
请用户选择加载哪些文件
请用户告诉 API 在哪里
请用户每次确认跨目录
请用户每次确认上下文扩展
```

---

## 80. Architecture / Implementation Separation

D02 不冻结：

```text
Exact ExecutionContext Struct
Exact JSON / YAML Schema
Exact Token Budget
Exact Cache Backend
Exact Storage Backend
Exact Vector Store
Exact SQLite Schema
Exact Context Window Strategy
Exact Chunk Size
Exact Retrieval Algorithm
Exact Embedding Model
Exact Provider Message Format
Exact Adapter Payload
Exact Credential Mechanism
Exact Serialization Format
Exact Directory
Exact API
```

这些属于后续 Implementation 或更具体 Contract。

---

## 81. Current Hard Prohibitions

继续保持：

```text
Implementation = NOT_AUTHORIZED

RP2 = NOT_AUTHORIZED

Authority Cutover = NOT_AUTHORIZED

Canonical Replacement = NOT_AUTHORIZED

Final Activation = NOT_AUTHORIZED

Legacy Retirement = NOT_AUTHORIZED

SQLite Physical Schema = NOT_FROZEN
```

D02 Approval 不改变以上状态。

---

## 82. AI Autonomous Boundary

Execution Context 自动组装可以：

```text
automatically select relevant context
automatically retrieve missing deterministic context
automatically refresh stale slices
automatically reuse valid slices
```

但：

```text
Automatic Context Assembly
!= AI Autonomous Authority
!= AI Autonomous Policy Mutation
!= AI Autonomous Canonical Promotion
```

---

## 83. Core Invariants

F10-D02 正式建立：

```text
Project Context
!= Task Context
!= Action Execution Context

Execution Context
!= Canonical Truth

Execution Context
!= Authority

Execution Context Ready
!= Runtime ALLOW

F8 Runtime Handoff
!= F10 Execution Context Replacement

F10 Context Need
!= F10 Retrieval Authority

Minimum Sufficient
!= Governance-incomplete

Context Compression
!= Governance Compression

Discoverable
!= Loaded

Potential Impact
!= Immediate Context Expansion

Stable Basis
!= Eternal Basis

Context Inheritance
!= Full Context Duplication

Runtime Overlay
!= Governance Override

Context Expansion
!= Material Scope Expansion

More Context
!= More Authority

Provider
!= Context Authority

Adapter
!= Context Resolver

Cached Context
!= Eternal Context

Context Cache Miss
!= Permission Denied

Missing Context
!= Human Input Required

Evidence Projection
!= Full Evidence Duplication

Provenance
!= Authority

Current Code
!= Canonical Semantic Truth

Execution Result
!= Automatic Canonical Context Update

Repository Visibility
!= Project Scope

Fast
!= Governance Loss
```

---

## 84. Forbidden Interpretations

明确禁止：

1. 把 Execution Context 当成新的 Canonical Truth；
2. 把 F8 Runtime Handoff 复制成 F10 第二套 Project Truth；
3. 让 F10 建第二套全仓 Index / Search / Context System；
4. 每个 Action 加载完整 Task Context；
5. 每个 Action 扫描完整 Git Repository；
6. 因为 Context 越多就认为 Authority 越大；
7. 因为同 Git Repo 就默认全部属于当前 Project；
8. 把 Potential Impact 全量塞入当前 Context；
9. Provider 自己静默扩大 Scope；
10. Provider 自己重新解释 Authorization；
11. Adapter 自己成为 Context Authority；
12. Adapter 默认获得整个 Project Context；
13. Context Compression 丢掉 Scope / Authority / Freshness / BLOCK；
14. UNKNOWN 在投影时自动变成 PASS；
15. HOLD 因为没有复制进 Context 而失效；
16. 动态补 Context 绕过 Authorization Envelope；
17. Action A 的全部临时 Context 自动污染 Action B；
18. 一个 Slice stale 就无条件重建整个 Task；
19. Cache 命中就永久不做 Freshness 检查；
20. Cache Miss 就解释成 Permission Denied；
21. 为了少 Token 丢掉治理关键限定；
22. 建立 Giant ExecutionContext God Object；
23. 建立新的 Execution Context Canonical Store；
24. 把 Current Code 自动升级成 Product / Design Truth；
25. D02 Approval 自动授权 Implementation 或真实写入。

---

## 85. 与 F10-D01 的关系

D01 已冻结：

```text
Runtime Permission
Authorization Validation
Point-of-use Validation
Scope / Authorization Boundary
Fail-closed + Auto-resolve-first
```

D02 为 D01 提供：

```text
Minimum Sufficient Runtime Inputs
```

因此：

```text
D02 supplies context
D01 determines permission semantics
```

D02 不修改 D01。

---

## 86. 与 F8 的关系

F8 继续拥有：

```text
Project Identity
Project Instance
Bindings
Profile
Provider Binding
Version
Feature / Gate Project State
Task-scoped Project Runtime Handoff
```

D02 只消费和投影。

---

## 87. 与 F9 的关系

F9 继续拥有：

```text
Index
Retrieval
Context Selection / Assembly
Freshness
Dependency / Impact
Targeted Recovery
Projection / Cache support
```

F10-D02：

```text
declares execution-purpose context need
+
assembles runtime working envelope
```

而不是取代 F9。

---

## 88. 后续 Decision 边界

D02 不提前冻结：

```text
Provider Runtime Resolution detailed rules
Adapter Contract
Execution Lifecycle
Pause / Resume / Retry / Cancel
Failure / Recovery
Execution Result / Evidence / Trace
Stage Exit / F11 Handoff
```

这些继续作为后续 F10 Decision。

---

## 89. Acceptance Meaning

用户已明确批准：

```text
F10-D02 HUMAN_APPROVED
```

因此正式成立：

```text
Project / Task / Action Context logical layering
Execution Context is derived / scoped / rebuildable
Action-specific minimum-sufficient assembly
Stable Basis + Volatile Runtime Slice separation
Purpose-sensitive context loading
Discoverable != Loaded
Dynamic context expansion within existing governance envelope
Provider / Adapter consume context but do not own context authority
F9 remains retrieval / freshness owner
Context reuse / selective invalidation
Governance-critical qualifiers must survive compression
```

但不表示批准：

```text
Exact ExecutionContext Schema
Exact Context Store
Exact Retrieval Algorithm
Exact Cache Technology
Exact Token Budget
Implementation
Real Project Write
RP2
Authority Cutover
Canonical Replacement
Final Activation
Legacy Retirement
```

---

## 90. Approval Status

```text
F10-D02 = HUMAN_APPROVED
```

普通：

```text
好的
下一步
继续
按建议
```

均不代表后续 Decision 的批准。

---

**END**

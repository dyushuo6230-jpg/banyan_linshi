# F9-D04 — Context Selection & Assembly

**中文名称：上下文选择与组装**

---

## 0. 文档身份

| 项目 | 内容 |
|---|---|
| Stage | F9 — Index / Projection / Cache Architecture |
| Decision | F9-D04 |
| 名称 | Context Selection & Assembly |
| 中文名称 | 上下文选择与组装 |
| 当前状态 | `HUMAN_APPROVED` |
| 精确批准语句 | `F9-D04 HUMAN_APPROVED` |
| 前置批准 | `F9-G01 HUMAN_APPROVED` |
| 前置批准 | `F9-D01 HUMAN_APPROVED` |
| 前置批准 | `F9-D02 HUMAN_APPROVED` |
| 前置批准 | `F9-D03 HUMAN_APPROVED` |
| 上游正式架构基线 | F1～F8 v1.1 Architecture Freeze Baseline |
| Implementation | `NOT_AUTHORIZED` |
| RP2 | `NOT_AUTHORIZED` |
| Authority Cutover | `NOT_AUTHORIZED` |
| Canonical Replacement | `NOT_AUTHORIZED` |
| Final Activation | `NOT_AUTHORIZED` |
| Legacy Retirement | `NOT_AUTHORIZED` |
| SQLite Physical Schema | `NOT_FROZEN` |

本决策只冻结 F9 的 Context Selection（上下文选择）、Context Assembly（上下文组装）、Materiality（实质相关性）、Context Coverage（上下文覆盖）、Subject-aware Deduplication（基于主体身份的去重）、Conflict Preservation（冲突保留）、Progressive Loading（渐进式加载）、Context Budget Boundary（上下文预算边界）、Context Lifecycle（上下文生命周期）、Context Reuse / Projection（上下文复用与投影）、Consumer Handoff（消费者交接）等架构语义。

本决策不冻结 Prompt 具体格式、Token 数值、Context Window 数值、JSON / YAML / XML Schema、数据库表、缓存 Provider、TTL、Watcher、锁、并发算法、Embedding、Reranker、Context Compression 具体模型、具体摘要算法、具体刷新算法、Runtime 执行机制或 Implementation。

---

## 1. 决策目标

F9-D04 解决：

> D03 已经确定“去哪找、找什么、按什么 Scope / Profile / Temporal / Domain Role 找”以后，F9 如何从合法 Retrieval Result（检索结果）中选择真正需要进入当前任务 Context（上下文）的信息，并在有限上下文预算下保留正式语义、冲突、约束、来源、覆盖状态和适用边界。

D04 的核心目标不是把找到的东西尽量全部塞进 AI Context，而是只加载当前任务真正需要的最小充分上下文，同时不能因为压缩、去重、预算或交接破坏 Truth / Authority / Scope / Temporal / Provenance。

---

## 2. 总体核心原则

F9-D04 正式采用：

## Minimum Sufficient Context
**最小充分上下文**

即：

> 只加载完成当前 Query / Task 所必需的最小信息集合，但不得为了节省 Token、加快速度或减少内容而删除会实质改变结论、合法边界、冲突、未知状态或治理约束的信息。

```text
Retrieved Candidate != Context-loaded Item
More Context != Better Context
Minimum Context != Minimum Sufficient Context
```

---

## 3. D03 与 D04 的责任边界

F9-D03 负责去哪找、找什么、找哪个 Scope、使用哪个 Profile、找 Current 还是 Historical、哪些 Domain / Source Role 可参与、允许扩大到哪里。

F9-D04 负责找到以后哪些真正进入 Context、哪些只保留 Reference、哪些 Deferred、如何去重、如何保护冲突、如何压缩、如何控制上下文预算、什么时候继续展开、什么时候停止、如何形成 Consumer View。

```text
D03 = Query Resolution
D04 = Context Selection & Assembly
```

D04 不得自行重新定义 D03 已解析的 Query Boundary。

---

## 4. Context Package

F9-D04 引入逻辑概念：

## Context Package
**上下文包**

Context Package 表示：

> 面向当前 Task / Query，从已解析 Search Space 和 Retrieval Result 中形成的、结构化的、带适用语义与来源信息的派生上下文集合。

Context Package 是：

```text
Task-scoped
Derived
Rebuildable
```

它不是：

```text
Canonical Truth
Canonical Memory
Permanent Knowledge
Authority Artifact
Profile Binding
Runtime Permission
Domain Truth Store
```

```text
Context Package != Canonical Truth
Assembly != Canonicalization
```

---

## 5. Context Package 必须保留语义角色

Context Package 不能把异质来源扁平化为普通文本数组。

逻辑上必须能够保留 Normative Context、Observed Context、Supporting Evidence、Historical Context、Exploratory Reference、Constraints / Guards、Coverage、Unknown / Unresolved / Blocked / Stale、Provenance、Source Role、Domain Role、Scope、Temporal、Freshness、Authority Basis。

具体字段和物理 Schema 不在 D04 冻结。

```text
Context Assembly must preserve semantic role
```

---

## 6. Normative Context

Normative Context 用于表达“应该是什么”，例如 Current Effective Requirement、Approved Design Meaning、Applicable Rule、Effective Profile Result、Effective Binding Result。

Normative Context 不因其他 Evidence 更详细、更相似或更新更近而失去正式语义地位。

---

## 7. Observed Context

Observed Context 用于表达“当前实际是什么”，例如 Current Code、Current Config、Current File State、Observed Runtime Evidence。

```text
Normative Truth != Observed State
```

Observed Context 可以揭示 Divergence（偏差），但不得自动覆盖 Normative Context。

---

## 8. Supporting Evidence

Supporting Evidence 用于解释为什么相信某结论、某正式结果如何产生、某 Subject 的来源和批准链，以及 Trace / Decision / Test / Occurrence 等辅助依据。

Supporting Evidence 不要求全部全文进入 Context，可根据当前任务采用 Material Extract、Semantic Summary、Reference Only 等更轻量表达。

---

## 9. Historical Context

Historical Context 只有在当前 Query Purpose 需要历史、演化、对比、变化原因时才成为 Material Context。

```text
Historical Exists != Historical Must Load
```

Current Query 不得因为历史资料更丰富而默认加载所有历史版本。

---

## 10. Exploratory Reference

Exploratory Context 用于其他 Project、其他 Scope、类似实现、参考模式、Legacy、Candidate Discovery。

```text
Exploratory Context != Applicable Context
```

进入 Context Package 后仍必须保留其 Exploratory 身份。

---

## 11. Constraints / Guards 是一等上下文

Constraints / Guards 不得被视为附属备注。

例如：

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

以及 Scope Guard、Approval Gate、Permission Constraint、Material UNKNOWN、BLOCKED、Required Validation，都属于可能直接改变后续行为的 Material Context。

```text
Guard / Constraint must not be dropped as background noise
```

---

## 12. Context Selection 顺序

D04 不采用 Search Score → Top K 作为上下文选择主逻辑。

正式采用：

```text
Applicability / Role / Authority
↓
Materiality
↓
Relevance
↓
Budget
```

```text
Context Selection Priority != Search Ranking
```

---

## 13. Search Rank 不能重排 Authority

Search Similarity、Latest File、Largest Revision、Most Occurrences、Longest Content、Most Detailed Evidence 均不得直接决定 Context Truth Priority。

```text
Search Relevance != Semantic Authority
Newer File != Higher Context Priority
More Detailed Evidence != Higher Semantic Authority
```

---

## 14. Materiality

D04 采用 Materiality（实质相关性）。

判断一个 Context Item 是否必须进入当前 Context，核心问题是：

> 如果不加载该内容，是否会实质改变当前 Query 的结论、约束、合法边界、冲突判断、Coverage 或后续允许动作？

若会，则属于 Material Context；若只是重复背景、补充例子、非必要历史、低价值参考或可延迟 Supporting Evidence，则可以 Reference 或 Deferred。

---

## 15. Protected Material Context

以下信息属于受保护的 Material Context：

- Material Truth；
- Material Guard；
- Material Conflict；
- Material Unknown；
- Material Unresolved；
- Material Blocked；
- Material Coverage；
- 会改变当前 Scope / Profile / Temporal / Applicability 的事实；
- 会改变当前结论的关键 Provenance；
- 会改变当前任务合法性的 Authorization / Gate。

```text
Budget Pressure != Permission To Drop Material Truth
Budget Pressure != Permission To Drop Material Conflict
Budget Pressure != Permission To Drop Guard
```

---

## 16. Loaded / Referenced / Deferred

D04 必须支持不同逻辑加载状态：

### Loaded
正文或 Material Extract 真正进入当前 Context。

### Referenced
保留 Subject Identity、Role、摘要、Locator、Provenance 等必要信息，需要时再展开。

### Deferred
知道该内容存在，但当前任务暂无 Material Need，因此暂不加载。

具体 enum 不冻结。

---

## 17. Progressive Context Loading

D04 采用 Progressive Context Loading（渐进式上下文加载）。

逻辑上可从：

```text
Identity / Metadata
↓
Material Summary
↓
Material Extract
↓
Full Source Detail
```

逐步深入。

```text
Load on material need
not load on mere existence
```

---

## 18. Loading Depth 不等于 Authority

```text
Loading Depth != Authority Level
```

一个 Summary 即使加载得更完整，也不因此获得比 Canonical Source 更高 Authority。

---

## 19. Context Expansion Trigger

Reference 只有在出现 Material Need 时才应进一步展开。

Material Expansion Trigger 可包括：

- 当前结论依赖该内容；
- 出现 Material Conflict；
- 出现 Material UNKNOWN / UNRESOLVED；
- 存在 Coverage Gap；
- Provenance 不足以支撑当前结论；
- 必须确认 Scope / Applicability；
- 必须确认正式约束或 Gate。

```text
Reference Existence != Expansion Trigger
```

---

## 20. Context Expansion 不得绕过 D03

```text
Context Expansion != Search Scope Expansion Authorization
```

D04 可以在 D03 已允许 Search Boundary 内继续展开 Context；若需要扩大 Project / Scope、改变 Profile / Temporal Mode 或新增 Exploratory Boundary，则必须返回 D03重新 Query Resolution。

---

## 21. Context Item

D04 引入逻辑 Context Item（上下文项）。

Context Item 不只是 Plain Text Chunk，至少必须能够关联：

```text
Subject
Context Role
Selected Content
Scope
Temporal
Source Role
Provenance
Freshness / Coverage
```

```text
Context Item != Plain Text Chunk
```

---

## 22. Context Fragment

一个 Subject 可以只加载当前任务相关 Fragment，但：

```text
Context Fragment != New Subject
```

Fragment 只是 Derived Context Projection，不能因为被截取而产生新的 Governed Identity。

---

## 23. Subject-aware Deduplication

D04 正式采用 Subject-aware Deduplication（基于 Subject Identity 的去重）。

```text
Same Subject != Multiple Independent Truths
```

---

## 24. 去重必须保留 Provenance

```text
Content Deduplicated
+
Evidence Lineage Preserved
```

不得为了去重把 Canonical Source、Supporting Occurrence、Revision、Scope、Provenance 全部抹掉。

---

## 25. Semantic Similarity 不等于去重身份

```text
Semantic Similarity != Dedup Identity
```

Embedding / Text Similarity 不得作为合并 Governed Subjects 的充分依据。

---

## 26. 同一 Subject 不同 Revision 不得错误合并

去重至少必须尊重：

```text
Subject Identity
+
Temporal / Revision Context
+
Scope
+
Query Role
```

```text
Same Subject Identity != Same Context Fact Across Revisions
```

---

## 27. Same Text 不等于 Same Scoped Fact

```text
Same Text != Same Scoped Fact
```

---

## 28. Occurrence Count 不等于 Authority Strength

```text
Occurrence Count != Authority Strength
```

---

## 29. 独立 Evidence Role 不得错误去重

即使多个来源得出相同数值，只要分别承担 Normative / Validation / Observed 等不同 Evidence Role，就不得因文本重复而删除其独立身份。

---

## 30. Conflict Preservation

D04 负责 Detect / Preserve / Structure Context 中存在的 Material Conflict，不负责 Arbitrate / Choose Winner / Create New Authority。

```text
Conflict Preservation != Conflict Arbitration
```

---

## 31. Contrast Group

D04 允许逻辑上形成 Contrast Group（对照组 / 冲突组）。

Contrast Group 是 Derived Context Structure，不是新的 Domain Truth。

---

## 32. 冲突不得被平均或合并

```text
Conflicting Context must remain distinguishable
```

---

## 33. 同 Domain Governance Conflict 也必须保留

同一 Scope / Domain 中存在多个正式候选且上游没有 winner 时，D04 必须保留其 Identity、Scope、Effective Basis、Provenance、Conflict State，不得通过 Search Score、Recency、Occurrence Count 或 AI Guess 自行解决。

---

## 34. Material Semantic Atoms

Material Context Compression 必须保留会改变任务结论的关键语义，包括数值、阈值、否定、必须 / 禁止 / 允许、Scope、Temporal、Owner、Authority Basis、Lifecycle、Identity、Relation Type、Conflict、Unknown、Blocked、Required Gate。

---

## 35. Compression 必须保持治理强度

```text
Compression must preserve modality
```

`NOT_AUTHORIZED` 不得压缩成“不建议”，`MUST` 不得弱化成“最好”，`UNKNOWN` 不得压缩成“可能没有”。

---

## 36. Compression 不得改变 Material Semantics

```text
Compression must not weaken material semantics
Compression must preserve traceability
```

---

## 37. AI Summary 的边界

AI Summary 只属于 Derived Projection。

```text
AI Summary != Source Truth
```

重要 Summary 必须保留 Derived From、Subject、Source Role、Scope、Temporal、Provenance。

---

## 38. Representation Depth

D04 允许同一 Context Item 使用不同表达深度：

```text
Full Content
Material Extract
Semantic Summary
Reference Only
```

```text
Representation Depth != Semantic Role
```

---

## 39. Material Unknown 必须保留

```text
Material Unknown must not be omitted
```

---

## 40. Missing Context 不等于 Negative Evidence

```text
Missing Context != Negative Evidence
```

---

## 41. Context Coverage

Context Package 必须能够表达 Context Coverage。

```text
Partial Context != Complete Context
```

---

## 42. Material Coverage Map

D04 引入 Material Coverage Map（实质覆盖图）。

Coverage Requirement 来自：

```text
Query Purpose
+
D03 Domain Roles
+
Material Constraints
```

而不是固定 Domain Checklist。

---

## 43. Coverage 是任务相对的

```text
Coverage Requirement is task-relative
```

---

## 44. Context Sufficient 不等于全部资料已加载

```text
Context Sufficient != All Available Information Loaded
More Available Evidence != More Required Context
```

---

## 45. Stop When Materially Sufficient

D04 正式采用 Stop When Materially Sufficient（实质充分即停止）。

当所有 Material Obligations 已充分覆盖、Material Conflict 已保留、Material Unknown / Unresolved 已显式、Guards / Scope / Protection 已保留、所需 Freshness 满足或限制已明确、剩余 Frontier Item 无已知 Material Effect 时，应停止继续加载。

---

## 46. Unexpanded Reference 不等于不完整

```text
Unexpanded Reference != Incomplete Context
```

---

## 47. 每次扩展后必须重新判断 Sufficiency

```text
Every material expansion must re-evaluate context sufficiency
```

---

## 48. Context Frontier

D04 允许逻辑上维护 Context Frontier（上下文前沿）。

Context Frontier 是 Derived / Task-scoped。

```text
Frontier Reference != Mandatory Future Load
```

---

## 49. Budget Allocation

D04 的上下文预算必须 Role-aware / Materiality-aware。

```text
Budget Allocation must be role-aware and materiality-aware
```

---

## 50. Protected Material Budget 与 Flexible Budget

逻辑上应区分 Protected Material Budget 与 Flexible Supporting Budget。

```text
Supporting Volume must not evict protected material context
```

具体物理 Token Pool 不冻结。

---

## 51. Material Domain Minimum

```text
Material Domain must receive minimum sufficient coverage
```

---

## 52. Breadth Before Unnecessary Depth

```text
Material Breadth before unnecessary depth
Material Breadth != Universal Breadth
```

---

## 53. Budget Exhaustion

```text
Budget Exhaustion != Silent Truncation
```

必须显式表达 Partial / Insufficient Coverage / Resource-limited 等语义。

---

## 54. Answer Strength 不得超过 Coverage

```text
Answer Conclusion Strength <= Available Material Coverage
```

---

## 55. Coverage 不采用单一百分比 Truth Score

```text
Coverage is obligation-based
not raw percentage completeness

No single universal context quality score
```

---

## 56. Context Readiness

Context Readiness 是 Purpose-relative。

```text
Context Ready is purpose-relative
```

---

## 57. Context Ready 不等于 Runtime Authorized

```text
Context Ready != Runtime Authorized
```

---

## 58. Context Package Lifecycle

```text
Context Package != Permanent Knowledge
Context Package != Canonical Memory
Context Package != Eternal Current State
```

---

## 59. Context Package Identity 与 Snapshot Revision 分离

```text
Context Snapshot Revision != Domain Revision != Domain Version
```

---

## 60. Context Reuse

Context Reuse 必须检查 Query Purpose、Material Obligations、Scope、Profile、Temporal、Domain Roles、Protection、Freshness Requirement、Relevant Source Basis。

```text
Same Query Text != Same Context Applicability
```

---

## 61. Same Project 不等于 Same Context Need

```text
Same Project != Same Context Need
```

---

## 62. Consumer / Task Projection

兼容旧 Context 时，可以形成更窄 Consumer Projection。

```text
Context Projection may narrow
Context Projection must not silently expand
```

---

## 63. D04 不得自行扩大 Resolution Boundary

若发生 Material Resolution Input 变化，则必须返回 D03重新解析。

```text
Context Reuse != Scope Expansion Authorization
```

---

## 64. Local Refresh

如果 Query Resolution Basis 不变、只有局部 Source / Context Item 变化，应优先 Local Refresh。

---

## 65. Local Refresh 后必须重新评估

```text
Local Refresh must trigger affected-context re-evaluation
```

---

## 66. Context-local Dependency 与 Global Impact 分离

```text
Context-local dependency != Global Impact Discovery
```

---

## 67. Protection 更新后必须重新限制 Context

```text
Previously Loaded != Permanently Authorized
Context Cache must not bypass updated protection
```

---

## 68. Stale Context Item

若 D06/D07 判定某 Context Item stale：

```text
Stale Context Item
→ affect coverage/readiness
→ refresh if material
→ re-evaluate sufficiency
```

```text
Stale Context != Invalid Domain Subject
```

---

## 69. Snapshot Coherence

Context Snapshot 应保持足够的 Snapshot Coherence（快照一致性），不得无标识地把会改变结论的新旧 Applicability State 混成一个完整当前状态。

---

## 70. Mid-task Refresh

```text
Mid-task Refresh
must preserve snapshot coherence
or explicitly establish a new snapshot
```

---

## 71. Context Snapshot Freshness Basis

Context Snapshot 必须保留足够的 Source Basis、Resolution Basis、Temporal Basis、Freshness Basis 供后续 D06/D07 评估。

D04 不冻结 TTL、Fingerprint、Watcher、Polling、Git Hook、Invalidation Algorithm。

---

## 72. Consumer Boundary

多个 Role / Agent 可以复用同一 Governed Evidence，但不默认共享同一个全量 Context View。

```text
Shared Governed Evidence
↓
Consumer-specific Context Projection
```

---

## 73. Consumer Projection 必须保留 Material Semantics

```text
Consumer Projection != Semantic Rewrite Authority
```

---

## 74. Consumer Projection 不得自行扩大 Scope

```text
Consumer Projection may narrow
but may not silently expand
```

---

## 75. Context Semantic Envelope

D04 正式要求 Context Handoff 保留 Context Semantic Envelope（上下文语义外壳）。

逻辑上至少包含：

```text
Task / Query Basis
Scope
Profile Context
Temporal Mode
Domain Roles
Source Roles
Protection
Freshness
Coverage
Conflicts
Unknown / Unresolved
Guards
Provenance
Stop Basis
```

具体物理结构不冻结。

---

## 76. Handoff 不能只传正文

```text
Context Content
without applicability metadata
is unsafe for handoff
```

---

## 77. Handoff 不产生 Authority

```text
Context Handoff != Authority Delegation
```

---

## 78. Handoff 不产生 Permission

```text
Context Handoff != Permission Grant
```

---

## 79. Package Availability 不等于 Consumer Eligibility

```text
Package Availability != Consumer Eligibility
```

---

## 80. Summary-of-Summary 必须保留 Lineage

多级 Context Projection / Summary / Handoff 必须保持可追踪：

```text
Consumer
→ Handoff Projection
→ Context Item
→ Subject
→ Original Governed / Evidence Source
```

禁止形成不可追溯“传话真相”。

---

## 81. Lineage 不要求每次加载全部原文

```text
Traceability != Full Source Reload
```

---

## 82. Consumer Inference 必须保持身份

```text
Consumer Derived Output != Upstream Canonical Truth
```

---

## 83. Context Package 可安全删除

```text
Delete Context Package != Delete Domain Truth
```

---

## 84. Context Cache 不等于 AI 自主学习

```text
AI Autonomous Learning = NOT_CURRENT_CAPABILITY
Context Cache Retention != Autonomous Learning
```

---

## 85. Context Readiness 状态

D04 必须能够表达 Context 是否足够、Partial、Refresh Required、Blocked、Superseded、Expired / Evicted 等生命周期语义。

具体 enum 不冻结。

---

## 86. Purpose 变化必须重新评估 Coverage

```text
Purpose Change → Re-evaluate Material Coverage
```

---

## 87. Context Ready At Assembly Time 不是永久执行资格

```text
Context Ready At Assembly Time != Permanent Execution Readiness
```

---

## 88. Stop Basis

Context Assembly 必须能够记录 Stop Basis（停止依据）。

---

## 89. Sufficiency Stop 与 Resource Stop 分离

```text
Stopped Because Sufficient
!=
Stopped Because Resource Exhausted / Blocked
```

---

## 90. Query / Context Snapshot 可复用，但需检查 Compatibility

```text
Context Reuse requires compatibility evaluation
```

且：

```text
Same Query Text
!= Same Query Resolution
!= Same Context Applicability
```

---

## 91. Context Package 不成为永久 Current State

Source / Scope / Profile / Protection / Freshness Basis 变化后，旧 Context Package 不得永久作为当前状态继续使用。

具体失效算法交给 D06 / D07 / D09。

---

## 92. D04 与 D06 的边界

D04 负责 Freshness Requirement 在 Context 中的保留、stale 后对 Coverage / Readiness 的影响、Material stale item 需要 refresh。

D06 负责 Freshness Evaluation、Revalidation、stale 判定算法。

```text
D04 != Freshness Algorithm
```

---

## 93. D04 与 D07 的边界

D07 负责 Fingerprint、Change Detection、Invalidation Trigger。

```text
D04 != Change Detection Engine
```

---

## 94. D04 与 D08 的边界

```text
Context-local dependency != Global Impact Discovery
```

---

## 95. D04 与 D09 的边界

D04 定义 Context Package 可缓存、可复用、可局部刷新、可重建、可删除。

D09 定义 Cache Provider、Rebuild Mechanism、Cache Lifecycle、Retry Implementation、Storage Strategy。

---

## 96. D04 不冻结具体技术实现

本决策明确不冻结：

```text
Prompt XML / JSON format
Token number
Context window size
Chunk size
Compression model
Summary model
Vector DB
Cache DB
SQLite schema
Redis layout
TTL
Watcher
Lock
Concurrency
Provider
API
CLI
Runtime adapter
```

---

## 97. 自动化边界

F9 / AI 可以自动：

- 计算 Material Context Need；
- 选择 Loaded / Referenced / Deferred；
- 对同 Subject Occurrence 做确定性去重；
- 保留 Provenance；
- 识别 Material Conflict；
- 形成 Contrast Group；
- 压缩 Supporting Evidence；
- 生成可追溯 Summary；
- 维护 Coverage；
- 渐进展开 Reference；
- 在 Materially Sufficient 时停止；
- 分配 Role-aware Budget；
- 形成 Consumer Projection；
- 局部 Refresh；
- 重新评估 Coverage / Sufficiency；
- 裁剪不适用于 Consumer 的 Context；
- 生成 Context Semantic Envelope；
- 保留 Stop Basis / Selection Basis / Provenance。

F9 / AI 不得自动：

- 把不同 Governed Subject 因相似而合并；
- 把不同 Scope Fact 合并；
- 把冲突平均掉；
- 通过 Search Rank 选择 Governance Winner；
- 把 `NOT_AUTHORIZED` 压缩成“不建议”；
- 把 Unknown 删掉；
- 把 Supporting Evidence 升级为 Truth；
- 因预算改变 Authority；
- 因 Context Expansion 扩大 Search Scope；
- 因 Handoff 赋予 Authority；
- 因 Handoff 赋予 Permission；
- 把 Consumer Inference 升级为 Canonical Truth；
- 把 Cache 当自主学习；
- 把 Context Ready 当 Runtime Authorized。

---

## 98. 核心不变量

```text
Retrieved Candidate != Context-loaded Item
More Context != Better Context
Context Package != Canonical Truth
Assembly != Canonicalization
Context Item != Plain Text Chunk
Context Fragment != New Subject
Search Relevance != Semantic Authority
Newer File != Higher Context Priority
More Detailed Evidence != Higher Semantic Authority
Budget Pressure != Permission To Drop Material Truth
Budget Pressure != Permission To Drop Material Conflict
Budget Pressure != Permission To Drop Guard
Semantic Similarity != Dedup Identity
Same Text != Same Scoped Fact
Occurrence Count != Authority Strength
Conflict Preservation != Conflict Arbitration
Compression != Semantic Rewrite Authority
AI Summary != Source Truth
Representation Depth != Semantic Role
Material Unknown must not be omitted
Missing Context != Negative Evidence
Partial Context != Complete Context
Context Sufficient != All Available Information Loaded
Unexpanded Reference != Incomplete Context
Reference Existence != Expansion Trigger
Loading Depth != Authority Level
Budget Exhaustion != Silent Truncation
Context Ready != Runtime Authorized
Context Snapshot Revision != Domain Revision
Same Query Text != Same Context Applicability
Same Project != Same Context Need
Context Projection may narrow but may not silently expand
Context Reuse != Scope Expansion Authorization
Previously Loaded != Permanently Authorized
Stale Context != Invalid Domain Subject
Context Handoff != Authority Delegation
Context Handoff != Permission Grant
Package Availability != Consumer Eligibility
Consumer Derived Output != Upstream Canonical Truth
Delete Context Package != Delete Domain Truth
Context Cache Retention != Autonomous Learning
Context Ready At Assembly Time != Permanent Execution Readiness
```

---

## 99. Acceptance Gates

- D04-AF-01 Retrieved Candidate 与 Context-loaded Item 明确分离。
- D04-AF-02 Minimum Sufficient Context 成立。
- D04-AF-03 Context Package 保留 Normative / Observed / Supporting / Historical / Exploratory / Guard 等角色。
- D04-AF-04 Context Package 为 Task-scoped / Derived / Rebuildable，不成为 Canonical Truth。
- D04-AF-05 Selection 顺序遵循 Applicability / Role / Authority → Materiality → Relevance → Budget。
- D04-AF-06 Search Score / Latest / Largest Revision 不直接决定 Context Truth Priority。
- D04-AF-07 Material Truth / Guard / Conflict / Unknown / Coverage 受到预算保护。
- D04-AF-08 Loaded / Referenced / Deferred 逻辑能力存在。
- D04-AF-09 Progressive Loading 由 Material Need 驱动。
- D04-AF-10 Context Expansion 不绕过 D03 Query Boundary。
- D04-AF-11 Context Item 保留 Subject / Scope / Temporal / Source Role / Provenance 等身份。
- D04-AF-12 Context Fragment 不产生新 Subject Identity。
- D04-AF-13 Subject-aware Deduplication 成立。
- D04-AF-14 去重保留 Provenance。
- D04-AF-15 Semantic Similarity 不作为 Governed Identity Merge 依据。
- D04-AF-16 不同 Revision / Scope / Query Role 不被错误去重。
- D04-AF-17 Occurrence Count 不产生 Authority。
- D04-AF-18 独立 Evidence Role 不被重复文本误删。
- D04-AF-19 Conflict 被保留而非平均。
- D04-AF-20 D04 不承担未决 Conflict Arbitration。
- D04-AF-21 Compression 保留 Material Semantic Atoms。
- D04-AF-22 Compression 保留 MUST / MUST NOT / MAY / UNKNOWN 等治理强度。
- D04-AF-23 AI Summary 保留 Traceability。
- D04-AF-24 Material Unknown / Unresolved / Blocked / Stale / Partial 不被静默删除。
- D04-AF-25 Context Coverage 明确。
- D04-AF-26 Material Coverage Map 为任务动态形成，不使用万能固定 Checklist。
- D04-AF-27 Stop When Materially Sufficient 成立。
- D04-AF-28 Unexpanded Reference 不被视为必然不完整。
- D04-AF-29 每次 Material Expansion 后重新评估 Sufficiency。
- D04-AF-30 Context Frontier 不形成无限自动展开。
- D04-AF-31 Budget Role-aware / Materiality-aware。
- D04-AF-32 Supporting / Historical / Exploratory 不挤掉 Protected Material Context。
- D04-AF-33 每个 Material Domain 获得 Minimum Sufficient Coverage。
- D04-AF-34 Budget Exhaustion 显式产生 Partial / Insufficient，而非 Silent Truncation。
- D04-AF-35 Answer Strength 不超过 Context Coverage。
- D04-AF-36 Coverage 不压缩成单一 Universal Quality Score。
- D04-AF-37 Context Ready 与 Runtime Authorized 分离。
- D04-AF-38 Context Package Lifecycle 非永久。
- D04-AF-39 Context Snapshot Revision 与 Domain Revision 分离。
- D04-AF-40 Context Reuse 检查 Purpose / Scope / Profile / Temporal / Protection / Freshness / Source Basis 兼容性。
- D04-AF-41 Purpose / Material Obligation 变化后重新评估 Coverage。
- D04-AF-42 Consumer Projection 可缩窄但不得静默扩大。
- D04-AF-43 Material Resolution Input 变化返回 D03，而非由 D04自行重解释。
- D04-AF-44 局部 Source 变化支持 Local Refresh。
- D04-AF-45 Local Refresh 后重新评估 Conflict / Coverage / Sufficiency。
- D04-AF-46 Protection 更新后 Previously Loaded Context 不保留永久访问资格。
- D04-AF-47 Stale Context 影响 Readiness / Coverage，但不宣布 Domain Subject 无效。
- D04-AF-48 Context Snapshot 保持足够的 Temporal / Freshness Coherence。
- D04-AF-49 跨 Consumer 默认采用 Consumer-specific Projection。
- D04-AF-50 Consumer Projection 保留 Material Semantics。
- D04-AF-51 Context Semantic Envelope 在 Handoff 中保留。
- D04-AF-52 Context Handoff 不产生 Authority Delegation。
- D04-AF-53 Context Handoff 不产生 Permission Grant。
- D04-AF-54 Consumer Eligibility 重新应用 Protection Boundary。
- D04-AF-55 Summary-of-Summary 保留到原 Governed / Evidence Source 的 Lineage。
- D04-AF-56 Consumer Inference 不升级为 Upstream Canonical Truth。
- D04-AF-57 Context Package 可安全删除和重建。
- D04-AF-58 Context Cache 不构成 AI Autonomous Learning。
- D04-AF-59 Mid-task Refresh 保持 Snapshot Coherence。
- D04-AF-60 D04 未冻结 D06 Freshness Algorithm。
- D04-AF-61 D04 未冻结 D07 Fingerprint / Change Detection。
- D04-AF-62 D04 未冻结 D08 Global Impact Discovery。
- D04-AF-63 D04 未冻结 D09 Cache / Storage / Rebuild 技术实现。
- D04-AF-64 Implementation、RP2、Authority Cutover、Canonical Replacement、Final Activation、Legacy Retirement 仍未授权。
- D04-AF-65 SQLite Physical Schema 仍为 `NOT_FROZEN`。

---

## 100. Final Owner Boundary

```text
Upstream Domain Owner
→ owns semantic truth

F8
→ owns Project / Binding /
   Effective Profile / Project context semantics

F9-D03
→ owns Query Resolution /
   Search-space planning /
   bounded recovery decision

F9-D04
→ owns Context Selection /
   Assembly /
   Coverage /
   Dedup /
   Progressive Loading /
   Context Lifecycle /
   Consumer Projection /
   Handoff semantic preservation

F9-D06
→ owns Freshness Evaluation / Revalidation

F9-D07
→ owns Fingerprint /
   Change Detection /
   Invalidation Trigger

F9-D08
→ owns Global Dependency /
   Impact Discovery

F9-D09
→ owns Cache /
   Projection /
   Rebuild implementation behavior
```

---

## 101. Architecture Closure

```text
D03 Query Resolution Plan
↓
Eligible Retrieval Results
↓
Materiality Evaluation
↓
Role-aware Selection
↓
Subject-aware Deduplication
↓
Conflict / Unknown / Guard Preservation
↓
Loaded / Referenced / Deferred
↓
Material Coverage Map
↓
Role-aware Budget Allocation
↓
Progressive Context Loading
↓
Material Sufficiency Evaluation
↓
Stop When Materially Sufficient
↓
Context Snapshot
↓
Consumer-specific Projection
↓
Context Semantic Envelope
↓
Consumer Use
↓
Local Refresh / Re-resolution as needed
```

并始终保持：

```text
Truth stays upstream.
Authority stays upstream.
Scope stays governed.
Profile Truth stays upstream.
Protection stays enforced.
Conflict stays visible.
Unknown stays explicit.
Coverage stays explicit.
Compression stays traceable.
Context stays task-scoped.
Handoff does not create authority.
Context Ready does not authorize runtime action.
```

---

## 102. Final Decision

F9-D04 最终确定：

> Banyan F9 不将 Retrieval Result 直接等同于 AI Context，而是在 D03 已解析的 Query Boundary 内，通过 Materiality、Domain Role、Source Role、Scope、Temporal、Authority Basis、Protection、Freshness 和 Coverage 选择最小充分上下文。

> Context Package 是 Task-scoped、Derived、Rebuildable 的任务视图，不是 Canonical Truth、Canonical Memory、Permanent Knowledge 或 Authority Artifact。Context Assembly 必须保持 Normative、Observed、Supporting、Historical、Exploratory、Guard、Unknown、Conflict 和 Coverage 等不同语义角色，不得扁平化为普通文本集合。

> D04 采用 Subject-aware Deduplication。同一 Subject 的多个 Occurrence 可去重正文，但必须保留 Provenance；不同 Governed Subject、不同 Revision、不同 Scope、不同 Query Role 不得因文本或 Embedding 相似而错误合并。Occurrence 数量不形成 Authority。

> Material Conflict 必须被保留，而不能在 Summary / Compression 中被平均、合并或静默消失。D04 可以形成 Contrast Group 等派生对照结构，但不得自行完成 Governance Conflict Arbitration。

> Context Compression 必须保护 Material Semantic Atoms，包括数值、否定、Scope、Temporal、Owner、Authority、Lifecycle、Identity、Relation、Conflict、Unknown 和 MUST / MUST NOT / MAY 等治理强度。AI Summary 只是 Derived Projection，必须保留 Traceability。

> D04 采用 Progressive Context Loading。Context Item 可以 Loaded、Referenced 或 Deferred，并根据 Material Need 从 Metadata / Summary / Extract 逐步展开。Reference 的存在本身不构成继续加载理由；Context Expansion 不得绕过 D03 的 Scope / Profile / Temporal / Protection Boundary。

> Context Coverage 由当前 Query Purpose、Domain Role 和 Material Obligation 动态决定。Context Sufficient 不等于全部资料已加载；达到 Material Sufficiency 后应停止。Context Frontier 只表示可继续展开的入口，不是自动待办清单。

> Context Budget 必须 Role-aware、Materiality-aware。Material Truth、Guard、Conflict、Unknown 和 Coverage 不得被 Supporting / Historical / Exploratory 内容挤掉。Material Context 无法全部容纳时，必须显式产生 Partial / Insufficient Coverage，而不是 Silent Truncation。下游回答强度不得超过当前 Material Coverage。

> Context Package 具有生命周期。可兼容复用、Consumer-specific Projection 和 Local Refresh，但 Scope / Profile / Temporal / Domain Role / Protection / Query Purpose 等 Material Resolution Input 发生变化时必须返回 D03重新解析。Local Refresh 后必须重新评估受影响的 Conflict、Coverage 和 Sufficiency。

> 多个 Role / Agent 可以复用相同 Governed Evidence，但默认通过 Consumer-specific Context Projection，而不是共享一个无边界全量 Context。Handoff 必须保留 Context Semantic Envelope 和原 Source Lineage；Context Handoff 不等于 Authority Delegation，也不等于 Permission Grant。

> Context Package / Cache 可安全删除与重建，不能成为 Domain Truth Store，也不能成为当前阶段 AI Autonomous Learning 的隐性永久知识库。

---

## 103. HUMAN_APPROVED Effect

本文件已经获得：

```text
F9-D04 HUMAN_APPROVED
```

因此：

```text
Context Selection Boundary
= ARCHITECTURALLY_FROZEN

Context Package Model
= ARCHITECTURALLY_FROZEN

Materiality / Coverage Boundary
= ARCHITECTURALLY_FROZEN

Subject-aware Dedup Boundary
= ARCHITECTURALLY_FROZEN

Conflict Preservation Boundary
= ARCHITECTURALLY_FROZEN

Progressive Loading Boundary
= ARCHITECTURALLY_FROZEN

Context Budget Governance Boundary
= ARCHITECTURALLY_FROZEN

Context Lifecycle / Reuse Boundary
= ARCHITECTURALLY_FROZEN

Consumer Projection / Handoff Boundary
= ARCHITECTURALLY_FROZEN
```

但仍然：

```text
F9 Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

`F9-D04 HUMAN_APPROVED` 只表示本决策的架构语义冻结，不代表 Prompt、Token 配置、Context Engine、Cache、数据库、向量系统、Summary Model、Runtime、Consumer Agent 或任何代码施工授权。

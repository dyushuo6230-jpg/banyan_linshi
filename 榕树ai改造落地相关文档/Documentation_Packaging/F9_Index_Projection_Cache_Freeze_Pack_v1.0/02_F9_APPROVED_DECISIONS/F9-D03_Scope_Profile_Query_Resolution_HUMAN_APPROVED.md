# F9-D03 — Scope / Profile / Query Resolution

**中文名称：范围 / 配置档案 / 查询解析**

## 0. 文档身份与冻结状态

| 项目 | 内容 |
|---|---|
| Stage | F9 — Index / Projection / Cache Architecture |
| Decision | F9-D03 |
| 名称 | Scope / Profile / Query Resolution |
| 中文名称 | 范围 / 配置档案 / 查询解析 |
| Approval Status | `HUMAN_APPROVED` |
| Exact Approval | `F9-D03 HUMAN_APPROVED` |
| 前置批准 | `F9-G01 HUMAN_APPROVED` |
| 前置批准 | `F9-D01 HUMAN_APPROVED` |
| 前置批准 | `F9-D02 HUMAN_APPROVED` |
| 上游正式架构基线 | F1～F8 v1.1 Architecture Freeze Baseline |
| Implementation | `NOT_AUTHORIZED` |
| RP2 | `NOT_AUTHORIZED` |
| Authority Cutover | `NOT_AUTHORIZED` |
| Canonical Replacement | `NOT_AUTHORIZED` |
| Final Activation | `NOT_AUTHORIZED` |
| Legacy Retirement | `NOT_AUTHORIZED` |
| SQLite Physical Schema | `NOT_FROZEN` |

本决策只冻结 F9 的 Query Resolution（查询解析）、Scope Resolution（范围解析）、Profile Applicability Resolution（配置档案适用性解析）、Temporal Resolution（时间语义解析）、Domain Role Resolution（领域角色解析）、Search Space Boundary（搜索空间边界）以及查询恢复边界。

本决策不冻结任何数据库结构、搜索算法、向量算法、评分算法、缓存实现、具体 enum、API、Prompt 模板、具体 Context Assembly（上下文组装）算法或物理实现。

---

## 1. 决策目标

F9-D03 解决：

> 当一个 Query（查询）进入 F9 后，系统如何在不进行全库乱搜、不跨项目串线、不误用错误 Profile、不混淆 Current 与 Historical、不让 Code Evidence 抢走 Product / Design Truth 的前提下，解析出本次查询真正应该访问的范围、配置档案、时间语义、领域角色和受保护搜索空间。

D03 的核心目标不是“怎样搜得最像”，而是“这次到底应该去哪一片合法索引里找”。

---

## 2. 核心总原则

F9-D03 正式采用：

```text
Resolve Before Retrieve
先解析，再检索
```

禁止默认：

```text
Global Search
→ Similarity Ranking
→ Guess Scope / Profile / Authority
```

正确链路是：

```text
Query
↓
Purpose Resolution
↓
Material Constraint Selection
↓
Project / Context Anchor
↓
Scope Resolution
↓
Profile Applicability Resolution
↓
Temporal / Effective Resolution
↓
Domain Role Resolution
↓
Protection Boundary
↓
Freshness Requirement
↓
Primary Search Space
↓
Retrieval
↓
Bounded Recovery
↓
Optional Exploratory Search
↓
Result Classification
↓
F9-D04 Context Selection & Assembly
```

---

## 3. Query Resolution Plan

F9-D03 引入逻辑：

**Query Resolution Plan — 查询解析计划**

它表示：

> 针对当前 Task / Query，解析出的“应该去哪里找、按什么适用条件找、允许扩大到哪里、哪些领域负责回答”的派生计划。

Query Resolution Plan 是：

```text
Derived
Task-scoped
Rebuildable
```

它不是：

```text
Canonical Scope
Profile Binding
Authority
Runtime Permission
Canonical Truth
```

因此：

```text
Query Resolution Plan
!= Canonical Truth
```

---

## 4. Query Resolution Plan 的逻辑组成

Query Resolution Plan 至少应具备表达以下逻辑信息的能力：

```text
Query Purpose
Project / Context Anchor
Scope Constraints
Profile Context Reference
Temporal / Effective Mode
Domain Roles
Subject Kind Constraints
Source Role Constraints
Primary Search Space
Exploratory Search Space
Allowed Expansion Boundary
Protection / Visibility Constraints
Freshness Requirement
Resolution Basis
Provenance
Resolution Outcome
Coverage
```

本决策只冻结逻辑含义，不冻结具体字段名称或数据结构。

---

## 5. Query Purpose

每个正式 Query Resolution 必须解析 Query Purpose，即当前用户 / 系统究竟想知道什么。

例如：
- 当前正式规则是什么；
- 历史规则是什么；
- 当前代码怎么实现；
- Requirement 对应哪个 UI；
- 某 Subject 改动可能影响什么；
- 两个版本有什么变化；
- 产品与实现是否一致。

具体 Purpose Enum 不在 D03 冻结。

```text
Query Purpose = Mandatory
Exact Purpose Enum = NOT_FROZEN
```

---

## 6. Scope 不采用单一字符串

D03 不采用扁平 `scope = "refund"` 模型。

正式采用：

**Scope Constraint Set — 范围约束集合**

Query Scope 由若干适用 Scope Dimension 的 Constraint 组成。

例如：

```text
Project = x_shop_server
Application = tenant-admin
ProductArea = refund
Tenant = current tenant
Environment = production
```

并非所有 Query 都必须包含全部维度。

---

## 7. Scope Dimension 开放扩展

F9 Core 不硬编码固定万能 Scope Schema。

未来可扩展 Project / Application / Module / Feature / Tenant / Region / Environment / Audience / Business Type / Domain 等 Scope Dimension。

新增 Scope Dimension 不应要求重写 F9 Core。

```text
F9 Scope Resolution
!= Scope Definition Authority
```

Scope Dimension 的正式语义仍由适用上游 Domain / Project Model 定义。

---

## 8. Scope Constraint 必须保留来源

每个 Scope Constraint 必须能够保留：

```text
Value
Source / Basis
Applicability
Resolution Context
```

必要时可保留发现置信证据，但：

```text
Confidence
!= Scope Authority
```

D03 必须能够回答：为什么这次 Query 被解析到这个 Scope？

---

## 9. Explicit Constraint 与 Inherited Constraint

D03 必须区分：

```text
Explicit Query Constraint
```

与：

```text
Inherited Context Constraint
```

Explicit Query Constraint 来自当前 Query 的明确表达。

Inherited Context Constraint 可以来自 Current Task Context、Current Project Context、已解析 Project Facts、适用 Profile / Scope Context。

---

## 10. Query Override 不修改 Canonical Scope

同一 Scope Dimension 中，当前 Query 的明确约束可替换该 Query Plan 中继承的值，但：

```text
Query Override
!= Canonical Scope Mutation
```

它只影响当前 Query。

---

## 11. Context Inheritance 条件

只有当前 Task 已可靠绑定到某个 Project / Scope 时，才允许自动继承。

```text
Known Current Task Context
can be inherited

Historical Mention
!= Current Scope
```

不能因为某个 Project 在前文被多次提及，就自动认为它是当前 Query Scope。

---

## 12. Conversation Context 边界

Conversation Context 可以作为 Query Resolution Evidence，但：

```text
Conversation Context
!= Canonical Scope Truth
```

用户当前明确的新 Query Constraint 必须能够替换上一任务中继承的 Query Scope，而不修改正式项目事实。

---

## 13. Scope 采用组合而不是全局优先级覆盖

Scope 来源之间默认采用：

```text
Constraint Composition
```

而不是固定全局优先级。

不同来源若描述不同 Scope Dimension，应组合，而不是互相覆盖。

---

## 14. 同维度冲突才进入覆盖 / 冲突判断

只有两个 Constraint 指向同一 Scope Dimension 时，才判断：
- 当前 Query 的 Explicit Override；
- Inherited Context 是否应被替换；
- 是否存在正式 Scope Relation；
- 是否形成 Multi-Scope；
- 是否产生真正 Ambiguity / Conflict。

---

## 15. Narrowing

若新增 Constraint 只是进一步缩小 Search Space，则属于 Narrowing，可自动继续。

```text
Narrower Scope
!= Higher Authority
```

---

## 16. More Specific 不等于 Override

```text
More Specific Scope
!= Automatic Override

More Specific Scope
!= Higher Authority
```

真正 Override 必须来自适用 Governance / Relation / Authority。

---

## 17. Scope Resolution 的正常结果类型

至少支持以下逻辑结果：
- Compatible Intersection；
- Narrowing；
- Bounded Multi-Scope；
- Ambiguity / Conflict。

具体物理 enum 不在 D03 冻结。

---

## 18. Multiple Applicable Scopes 不等于 Conflict

用户明确要求比较多个 Scope 时，属于合法 Bounded Multi-Scope，无需人工确认。

```text
Multiple Applicable Scopes
!= Scope Conflict
```

---

## 19. Scope Ambiguity 与 Semantic Conflict 分离

```text
Scope Ambiguity
!= Semantic Conflict
```

Scope Ambiguity 表示不知道该选哪个合法范围；Semantic Conflict 表示相同适用 Scope 中正式语义冲突。

---

## 20. Narrow by Default

正式采用：

**Narrow by Default — 默认定向缩小**

禁止：

```text
No Match
↓
silently remove scope
↓
global search
```

```text
No Result
!= Scope Expansion Authorization
```

---

## 21. No Silent Expansion

Search Scope 扩大必须具有：
- Explicit Query Intent；
- 或正式 Bounded Query Policy。

并保留 Scope Provenance。

---

## 22. Primary Search Space

Primary Search Space 表示当前 Query 真正要求的正式适用搜索范围。

只有其中的结果可以成为当前 Query 的直接适用候选。

---

## 23. Exploratory Search Space

Exploratory Search Space 用于类似参考、其他 Project / Scope、Shared Profile、Historical、Legacy、Candidate Discovery。

```text
Exploratory Result
!= Primary Applicable Result
```

---

## 24. Automatic Expansion

自动进入 Exploratory Search 必须：
1. 用户明确要求扩大；
2. 或存在正式 Bounded Governance Policy。

且必须保持 Primary Scope、标记 exploratory identity、保留 scope provenance。

---

## 25. Expansion Boundary

任何 Search Expansion 必须具有明确有限边界。

```text
Search Expansion
must be bounded
```

禁止无限 fallback 直到“总能找到东西”。

---

## 26. Global Query

真正 Global Query 必须来自 Explicit Global Query Intent 或正式 Governed Root Boundary。

```text
Missing Scope != Global
Global Query != Global Subject Applicability
```

---

## 27. “All” 必须有 Root Boundary

```text
ALL
must have explicit Root Boundary
```

如 `All under current project` 与 `All accessible projects` 是不同 Query。

---

## 28. Discovery Expansion 不扩大 Mutation Scope

```text
Discovery Scope Expansion
!= Mutation Scope Expansion
```

---

## 29. Protection Boundary 先于 Search Expansion

Search Expansion 不得绕过 Protection Boundary。

```text
Explicit Query Scope
!= Access Authorization
```

---

## 30. Query Search Space 必须 Protection-bounded

Query Search Space 在形成阶段就应受到适用 Protection Constraint 限制。

```text
Query Search Space
must be protection-bounded
```

---

## 31. Profile 与 Query Scope 分离

```text
Profile Scope
!= Query Scope
```

Profile 主要表达哪些 Profile-dependent Subject / Rule / Standard 对当前 Query 具备 Applicability。

---

## 32. Profile 实质相关原则

采用：

**Material Profile Principle — Profile 实质相关原则**

只有 Profile 会实质改变 Subject Applicability、Rule Applicability、Implementation Guidance、Provider / Config Applicability、Engineering Standard 时，Profile 才成为当前 Query 必需约束。

```text
Profile Exists
!= Profile Required For Every Query
```

---

## 33. F9 消费 Profile Result，不重建 Profile Truth

F9 使用上游正式 Profile Binding / Effective Profile Result / Project Profile Context。

```text
Profile Evidence != Effective Profile
Profile Match != Profile Binding
Profile Similarity != Profile Applicability
```

---

## 34. Multiple Profiles 不等于 Conflict

```text
Multiple Profiles
!= Profile Conflict
```

只有同一 Profile Role 下出现互斥、同时有效且无法按治理规则解析的候选时，才构成 Profile Resolution Conflict。

---

## 35. Profile 不作为 Search Ranking Authority

Profile 参与 Applicability Filtering，不成为 Authority Ranking 或单纯 Search Score Bonus。

```text
Profile Match
!= Authority Winner
```

---

## 36. Missing Profile

若 Profile 是 Material Constraint 而无法解析：

```text
Profile Context = UNKNOWN / UNRESOLVED
```

```text
Missing Profile
!= Default Profile
```

除非上游存在明确合法默认规则。

---

## 37. 非实质 Profile 缺失不阻塞 Query

```text
Non-material Missing Constraint
!= Query Block
```

---

## 38. Temporal Intent

每个 Query 必须能解析适用 Temporal Intent。

逻辑上支持 Current Applicable / Historical / Exact Revision / Exact Version / As-Of / Evolution / Comparison 等扩展。

具体物理 enum 不在 D03 冻结。

---

## 39. Current 默认

普通无明确历史语义的现时 Query 可以默认 Current Applicable。

```text
Current
!= Latest
```

Current 必须依据正式 Applicable Effective Result，而非最大 Revision / Version、最新修改文件或最新 Commit。

---

## 40. Explicit Temporal Constraint 优先

```text
Explicit Historical / Exact Constraint
> Implicit Current Default
```

但不修改上游 Current Effective Truth。

---

## 41. Temporal Applicability 优先于 Search Relevance

```text
Temporal Applicability
> Search Relevance
```

Historical Result 不得因相似度更高而冒充 Current Result。

---

## 42. Historical Result 保持历史身份

```text
Historical Retrieval
!= Current Applicability
```

---

## 43. Temporal Context Consistency

Historical / As-Of Query 的 Scope、Profile、Effective Result、Subject State、Source Evidence 应尽可能解析到一致时间语义。

```text
Historical Query
must not silently mix
current applicability
with historical subject state
```

---

## 44. Current Profile 不阻断合法 Historical Query

```text
Current Profile
!= Historical Search Ban
```

Historical Query 应使用对应 Historical Profile Context；无法解析时应标记缺失，而不是自动填 Current Profile。

---

## 45. Minimum Sufficient Query Context

采用：

**Minimum Sufficient Query Context — 最小充分查询上下文**

只解析对当前 Query Purpose 真正有实质影响的 Constraint，不要求每次 Query 都解析整个 Project 世界模型。

---

## 46. Domain Resolution

每个 Query 必须能表达相关 Domain 在当前 Query 中的角色。

至少支持逻辑能力：
- Primary；
- Normative；
- Observed；
- Supporting；
- Comparison；
- Historical。

具体 enum 不在 D03 冻结。

---

## 47. Primary Domain

Primary Domain 表示当前 Query 主要询问哪个责任领域的事实。

---

## 48. Primary Domain 不等于全局 Authority

```text
Primary Domain
!= Global Authority Priority
```

---

## 49. Normative 与 Observed 分离

```text
Normative Truth
!= Observed State
```

---

## 50. Code Domain 边界

Code 可以成为 Current Code Fact Query 的 Primary Domain，但：

```text
Code Primary for Code Fact
!= Code becomes Product Truth

Current Code
!= Automatic Product Truth
!= Automatic Design Truth
!= Automatic Architecture Truth
```

---

## 51. Cross-Domain Query

```text
Cross-Domain Query
!= Cross-Domain Winner Selection
```

每个 Domain 只回答自己拥有的事实，再进行 Comparison / Consistency Analysis。

---

## 52. Primary Miss 不提升 Supporting Domain

```text
Primary Domain Miss
!= Supporting Domain Promotion
```

---

## 53. Missing Normative Truth 不由 Observed State 静默补齐

```text
Observed Implementation
cannot silently fill missing Normative Truth
```

---

## 54. Normative Truth 不等于当前已实现

```text
Normative Truth
!= Observed Implementation State
```

---

## 55. Bounded Multi-Domain

多个 Domain 的不同语义结果可以安全并列回答时：

```text
Multi-Domain Answerable
!= Needs Disambiguation
```

---

## 56. Source Role 参与 Query Eligibility

```text
Source Role Eligibility
!= Search Rank
```

Source Role 决定某 Source 是否有资格回答当前 Query。

---

## 57. Supporting Source 不因内容更丰富获得 Authority

```text
More Detailed Evidence
!= Higher Semantic Authority
```

---

## 58. Query Evidence Role

Query Result 应能够保留 Normative / Observed / Supporting / Historical / Exploratory 等用途。

Evidence Role 是：

```text
Derived query-use classification
based on governed metadata
```

不是 F9 自行创造 Authority。

---

## 59. Freshness Requirement

Query Resolution Plan 必须能表达 Freshness Requirement。

D03 不冻结 Freshness 计算算法；Freshness Evaluation / Revalidation 属于 F9-D06。

---

## 60. Query Resolution Success 与 Search Hit 分离

```text
Query Resolution Success
!= Search Result Found

Resolution Failure
!= Retrieval Miss
```

---

## 61. Resolution Outcome

至少支持以下语义能力：
- RESOLVED；
- BOUNDED_MULTI_RESOLVED；
- PARTIALLY_RESOLVED；
- NEEDS_DISAMBIGUATION；
- UNRESOLVED；
- BLOCKED。

具体物理 enum 不冻结。

---

## 62. Outcome 语义必须分离

```text
NEEDS_DISAMBIGUATION != UNRESOLVED
UNRESOLVED != BLOCKED
BLOCKED != NO_MATCH
NO_MATCH != Semantic Absence
```

---

## 63. Localized Failure

```text
Branch Failure
!= Global Query Failure
```

只有失败 Branch 是 Query Purpose 的 Material Requirement 时才影响整体结果。

---

## 64. Partial Result

Partial Result 必须明确 Coverage。

```text
Partial Success
must not masquerade as complete success
```

---

## 65. No Match 原因必须区分

Primary Search No Match 后，逻辑上至少能够区分：

```text
TRUE_NO_MATCH
INDEX_MISS
INDEX_STALE
SOURCE_NOT_INDEXED
SOURCE_UNAVAILABLE
METADATA_INCOMPLETE
PROTECTION_FILTERED
```

具体物理 enum 不冻结。

---

## 66. No Match 先分析原因，再恢复

```text
Primary Search
↓
No Match
↓
Cause Analysis
↓
Bounded Recovery
↓
Retry Primary Search
↓
Optional Exploration
```

禁止 No Match 后立即 Scope Expansion。

---

## 67. Source Recovery

在 Resolved Query Boundary + Known Source Role + Known Source Mapping 已明确时，可在原 Primary Scope 内回源：

```text
recover
rebuild local derived index
retry
```

---

## 68. Source Recovery 与 Scope Expansion 分离

```text
Source Recovery
!= Scope Expansion
```

---

## 69. Source Recovery 必须 Scope-bounded

禁止 Index Miss 后扫描整个仓库 / 所有项目 / 全部历史。

---

## 70. Recovery 推荐顺序

逻辑顺序：

```text
1. Validate Query Resolution
2. Check Index Coverage
3. Check Index Freshness
4. Check Source Mapping / Availability
5. Attempt bounded source recovery
6. Rebuild affected derived layer
7. Retry Primary Search
8. Only then consider bounded exploration
```

具体执行机制不冻结。

---

## 71. Recovery 保持 Domain Role

```text
Recovery
must preserve Domain Role
```

---

## 72. Recovery 保持 Temporal Role

```text
Recovery
must preserve Temporal Role
```

---

## 73. Recovery 保持 Profile Applicability

```text
Recovery
must preserve Profile Applicability
```

---

## 74. Recovery 保持 Protection Boundary

自动 Recovery 不得绕过适用 Protection / Visibility / Access Constraint。

---

## 75. Exploratory Search 不等于 Resolution Recovery

```text
Exploration
!= Primary Resolution Recovery
```

---

## 76. Automatic Recovery 有边界

```text
Auto Recovery
!= Unbounded Retry
```

---

## 77. Derived-layer Failure 与 Governance-layer Failure 分离

```text
Derived-layer failure
→ automatic recovery preferred

Governance-layer ambiguity / conflict
→ no silent recovery
```

---

## 78. Human Clarification 最小化

只有同时满足：
- Multiple legitimate choices；
- Materially different results；
- No deterministic winner；
- Bounded multi-answer not sufficient / safe；

才进入 Human Clarification。

```text
AI uncertainty alone
!= Human clarification requirement
```

---

## 79. Bounded Multi-Scope / Multi-Domain 优先

可安全同时检索并明确区分结果时，优先 Bounded Multi-Scope / Bounded Multi-Domain，而不是强制用户选择。

---

## 80. Sufficient Resolution

采用：

**Sufficient Resolution — 充分解析**

Query Resolution Success 表示当前 Query Purpose 的 Material Constraints 已解析到足以构建合法、受保护、有限、可执行的 Search Plan。

```text
Resolution Completeness
is purpose-relative
```

---

## 81. Material Missing Constraint

```text
Material Missing Constraint
!= Safe Default
```

不得用 Guess / Latest / Default Profile / Global / Most Similar Result 静默继续。

---

## 82. Local Unresolved 不等于 Global Block

```text
Local Unresolved
!= Global Query Block
```

---

## 83. Resolution Basis

Query Resolution Plan 必须保留 Resolution Basis，使 Project / Application / Profile / Temporal / Domain Role 等选择可解释、可审计。

---

## 84. Query Plan Provenance

```text
Resolved Query Plan
must retain provenance
```

至少可追踪 Query Input、Inherited Context、Governed References、Applied Policies、Scope/Profile/Temporal Decision Basis、Expansion Rules、Branch Decisions、Recovery Path。

---

## 85. Query Plan Cache

Query Resolution Plan 可以缓存，但：

```text
Cached Query Plan
= Derived Cache
```

---

## 86. Same Query Text 不等于 Same Query Resolution

```text
Same Query Text
!= Same Query Resolution
```

---

## 87. Context Compatibility

Query Plan Cache 复用必须检查 Relevant Context Compatibility，包括适用的 Project / Scope / Profile / Temporal / Protection / Query Purpose 等重要输入。

---

## 88. Query Plan Freshness

Query Plan 有效性依赖 Resolution Inputs。Scope Fact / Profile Effective Result / Protection Constraint / Source Mapping 等发生变化时，旧 Query Plan 不得永久继续有效。

具体 Freshness / Invalidation 算法属于 F9-D06 / D07 / D09。

---

## 89. No Match 保留 Coverage Boundary

```text
No Match Within Bounded Search Space
!= Global Nonexistence

Index Miss
!= Semantic Absence
```

---

## 90. Protection-aware Explainability

```text
Explainability
must remain protection-aware
```

Protection Policy 可以限制结果内容、Source 甚至 Subject 存在性披露。

---

## 91. BLOCKED 不等于可公开全部原因

```text
Audit Explainability
!= Unrestricted User Disclosure
```

---

## 92. Query Recovery Trace

Recovery Trace 可用于审计、调试、解释和后续 Freshness / Cache 分析。

```text
Recovery Trace
!= Canonical Semantic Truth
```

---

## 93. 与 F9-D02 的边界

```text
D02 = what is indexed
D03 = where / under what conditions to search
```

---

## 94. 与 F9-D04 的边界

```text
D03 = Query Resolution
D04 = Context Selection & Assembly
```

D03 不负责结果进入 Context 后的去重、压缩、Token 控制和组装。

---

## 95. 与 F9-D06 的边界

D03定义 Freshness Requirement 和 Recovery Intent。

```text
D03
!= Freshness Algorithm
```

---

## 96. 与 F9-D07 的边界

具体 Fingerprint / Change Detection / Invalidation Trigger 属于 F9-D07。

---

## 97. 与 F9-D08 的边界

```text
D03
!= Impact Engine
```

---

## 98. 与 F9-D09 的边界

具体 Cache Storage / Projection Rebuild / Retry Implementation / Cache Lifecycle 属于 F9-D09。

---

## 99. Query Core 架构

禁止建立：

```text
UniversalQueryAuthority
UniversalScopeAuthority
UniversalProfileAuthority
UniversalDomainAuthority
```

正式采用：

```text
Thin Query Core
+
Domain-aware Adapter
+
Scope-aware Resolver
+
Profile-aware Adapter
+
Governed Metadata Inputs
```

---

## 100. 自动化边界

F9 / AI 可以自动：
- 解析明显 Query Purpose；
- 继承可靠 Current Task Context；
- 组合兼容 Scope Constraints；
- 执行 Narrowing；
- 使用正式 Effective Profile Context；
- 解析 Current / Historical / Exact 等 Temporal Intent；
- 确定 Query Domain Roles；
- 生成 Bounded Multi-Scope / Multi-Domain；
- 执行 Primary Search；
- 检测 No Match 类型；
- 执行受限 Source Recovery；
- 重建自己的 Derived Index；
- 进行有界 Retry；
- 在规则授权下执行 Exploratory Search；
- 生成 Resolution Basis / Provenance；
- 局部降级未解析 Branch；
- 输出 Coverage。

F9 / AI 不得自动：
- 把 Missing Scope 当 Global；
- 把 Missing Profile 当 Default；
- 把 Current 当 Latest；
- 把 Historical 当 Current；
- 把 Supporting Domain 升级成 Primary Truth；
- 让 Code 替代 Product / Design Truth；
- 让搜索相似度决定 Authority；
- 让更具体 Scope 自动产生 Override；
- 扩大 Discovery Scope 后扩大 Mutation Scope；
- 绕过 Protection；
- 把 Cross-Project Reference 当 Current Project Truth；
- 通过无限 Scope Expansion 强行找到答案；
- 通过 AI Confidence 解决 Governance Conflict。

---

## 101. 核心不变量

```text
Resolve Before Retrieve

Query Resolution Plan != Canonical Truth
Query Scope != Canonical Scope
Profile Scope != Query Scope
Query Override != Canonical Scope Mutation
Historical Mention != Current Scope
Conversation Context != Canonical Scope Truth
Narrower Scope != Higher Authority
More Specific != Automatic Override
Multiple Applicable Scopes != Scope Conflict
Scope Ambiguity != Semantic Conflict
No Result != Scope Expansion Authorization
Primary Search Space != Exploratory Search Space
Exploratory Result != Primary Applicable Result
Global Query != Global Subject Applicability
Missing Scope != Global
Discovery Scope Expansion != Mutation Scope Expansion
Explicit Query Scope != Access Authorization
Profile Match != Authority Winner
Missing Profile != Default Profile
Current != Latest
Historical Retrieval != Current Applicability
Temporal Applicability > Search Relevance
Primary Domain != Global Authority Priority
Normative Truth != Observed State
Code Primary for Code Fact != Code becomes Product Truth
Cross-Domain Query != Cross-Domain Winner Selection
Primary Domain Miss != Supporting Domain Promotion
Observed Implementation != Missing Normative Truth
Normative Truth != Observed Implementation State
Source Role Eligibility != Search Rank
Query Resolution Success != Search Hit
Resolution Failure != Retrieval Miss
NEEDS_DISAMBIGUATION != UNRESOLVED != BLOCKED != NO_MATCH
Branch Failure != Global Query Failure
Source Recovery != Scope Expansion
Exploration != Primary Resolution Recovery
Auto Recovery != Unbounded Retry
Derived-layer failure != Governance-layer ambiguity
Same Query Text != Same Query Resolution
Partial Success != Complete Success
No Match != Semantic Absence
Protection-aware Explainability != Unrestricted Disclosure
```

---

## 102. Acceptance Gates

- D03-AF-01 所有正式 Retrieval 前具备 Query Resolution Plan。
- D03-AF-02 Query Purpose、Scope、Profile、Temporal、Domain、Protection、Freshness 等责任边界明确。
- D03-AF-03 Scope 使用开放 Constraint Set，而非单一字符串或万能固定 Schema。
- D03-AF-04 Explicit Constraint 与 Inherited Context 能区分并保留来源。
- D03-AF-05 Query Override 不修改 Canonical Scope。
- D03-AF-06 Scope 采用 Composition / Compatibility / Intersection，不采用简单全局优先级覆盖。
- D03-AF-07 Narrower Scope 不产生 Higher Authority 或 Automatic Override。
- D03-AF-08 Bounded Multi-Scope 与真实 Scope Ambiguity 能区分。
- D03-AF-09 No Silent Expansion 成立。
- D03-AF-10 Primary Search Space 与 Exploratory Search Space 隔离。
- D03-AF-11 Expansion Boundary 有限且保留 Scope Provenance。
- D03-AF-12 Global Query 与 Global Subject Applicability 分离。
- D03-AF-13 Discovery Scope Expansion 不扩大 Mutation Scope。
- D03-AF-14 Protection Boundary 在 Search Space 形成阶段生效。
- D03-AF-15 Profile 仅在实质相关时参与 Query。
- D03-AF-16 F9消费 Effective Profile Result，不重建第二套 Profile Truth。
- D03-AF-17 Multiple Profiles 与 Profile Conflict 能区分。
- D03-AF-18 Missing Profile 不存在静默 Default。
- D03-AF-19 Temporal Intent 可区分 Current / Historical / Exact / As-Of / Comparison 等逻辑语义。
- D03-AF-20 Current 与 Latest 严格分离。
- D03-AF-21 Historical Result 不得冒充 Current Result。
- D03-AF-22 Historical Query 保持 Temporal Context Consistency。
- D03-AF-23 Normative 与 Observed Domain Role 分离。
- D03-AF-24 Code 可以回答 Code Fact，但不获得 Product / Design / Architecture Truth。
- D03-AF-25 Cross-Domain Query 不通过搜索排名选 Winner。
- D03-AF-26 Primary Domain Miss 不自动提升 Supporting Domain。
- D03-AF-27 Source Role 参与 Eligibility，而不是只有 Search Rank。
- D03-AF-28 Resolution Outcome 与 Retrieval Outcome 分离。
- D03-AF-29 Resolved / Multi-Resolved / Partial / Disambiguation / Unresolved / Blocked 等结果语义能区分。
- D03-AF-30 Branch Failure 支持局部化，不默认 Global Block。
- D03-AF-31 No Match 先分析原因，再执行 Recovery。
- D03-AF-32 Source Recovery 与 Scope Expansion 严格分离。
- D03-AF-33 Recovery 保持 Domain / Temporal / Profile / Protection Boundary。
- D03-AF-34 Exploratory Search 不冒充 Primary Recovery。
- D03-AF-35 Automatic Recovery 有界。
- D03-AF-36 Derived-layer Failure 可自动恢复，Governance Conflict 不可静默修复。
- D03-AF-37 Human Clarification 只在真正 Material Multiple-choice 场景出现。
- D03-AF-38 Sufficient Resolution 成立，不要求 Complete World Resolution。
- D03-AF-39 Material Missing Constraint 不使用 Silent Default。
- D03-AF-40 Query Resolution Basis 与 Provenance 可审计。
- D03-AF-41 Query Plan Cache 是 Derived Cache，且复用依赖 Context Compatibility。
- D03-AF-42 Partial Result 保留 Coverage。
- D03-AF-43 No Match 只针对 Bounded Search Space，不代表 Global Absence。
- D03-AF-44 Explainability 保持 Protection-aware。
- D03-AF-45 D03 未提前冻结 D04 Context Assembly。
- D03-AF-46 D03 未提前冻结 D06 Freshness Algorithm。
- D03-AF-47 D03 未提前冻结 D07 Fingerprint / Invalidation Algorithm。
- D03-AF-48 D03 未提前冻结 D08 Impact Engine。
- D03-AF-49 D03 未提前冻结 D09 Cache / Rebuild Implementation。
- D03-AF-50 Implementation、RP2、Authority Cutover、Canonical Replacement、Final Activation、Legacy Retirement 仍未授权。
- D03-AF-51 SQLite Physical Schema 仍为 `NOT_FROZEN`。

---

## 103. Final Owner Boundary

```text
Upstream Domain Owner
→ owns semantic truth

F8
→ owns Project Identity /
   Binding /
   Effective Project/Profile Resolution semantics

F9-D03
→ owns task-scoped query resolution /
   search-space planning /
   bounded recovery decision

F9-D04
→ owns context selection & assembly

F9-D06
→ owns freshness evaluation & revalidation

F9-D07
→ owns fingerprint / change detection / invalidation

F9-D08
→ owns dependency / impact discovery

F9-D09
→ owns cache / projection / rebuild behavior
```

---

## 104. Architecture Closure

```text
Query
↓
Purpose
↓
Material Constraints
↓
Project / Context Anchor
↓
Scope Constraint Composition
↓
Profile Applicability
↓
Temporal Resolution
↓
Domain Roles
↓
Source Role Eligibility
↓
Protection Boundary
↓
Freshness Requirement
↓
Primary Search Space
↓
Retrieval
↓
Bounded Recovery
↓
Optional Exploratory Search
↓
Resolution / Retrieval Outcome
↓
Coverage
↓
F9-D04 Context Assembly
```

并保持：

```text
Search Space is task-scoped.
Truth stays upstream.
Authority stays upstream.
Profile Truth stays upstream.
Protection stays enforced.
Recovery stays bounded.
Exploration never becomes applicability by itself.
```

---

## 105. Final Decision

Banyan F9 在任何正式检索前，先生成 Task-scoped、Derived、Rebuildable 的 Query Resolution Plan，通过 Query Purpose、Project / Context、Scope Constraint、Profile Applicability、Temporal Intent、Domain Role、Source Role、Protection Boundary 和 Freshness Requirement 形成最小充分 Search Space，而不是先执行全局搜索再通过相似度猜测适用范围。

Scope 采用开放 Constraint Set 和可解释的 Constraint Composition；当前 Query 的明确约束可以替换继承的 Query Context，但不得修改 Canonical Scope。更具体 Scope 只缩小搜索空间，不产生更高 Authority 或自动 Override。

F9 使用正式 Effective Profile Result 作为 Query Applicability Input，不重新构建 Profile Truth。Profile 只在对当前 Query Purpose 有实质影响时参与解析，Missing Profile 不自动等于 Default Profile。

Current、Historical、Exact Revision / Version、As-Of、Evolution 和 Comparison 等时间语义必须被区分。普通现时 Query 可以采用 Current Applicable，但 Current 严格不等于 Latest；Historical Result 不得因为搜索相关度更高而冒充 Current Result。

Query Domain Resolution 必须区分 Normative、Observed、Supporting、Comparison 等角色。Code 可以作为 Current Code Fact 的 Primary Domain，但不得因此成为 Product / Design / Architecture Truth。Cross-Domain Query 不通过搜索相关度选 Winner，而由各 Domain 回答自己拥有的事实后再进行比较。

Query Resolution Success 与 Search Hit 严格分离。Primary Search No Match 后，F9 必须先分析 Index Coverage、Freshness、Source Availability、Metadata 和 Protection，再在原 Scope 内执行有界 Source Recovery；Source Recovery 不等于 Scope Expansion，Exploratory Search 也不等于 Primary Resolution Recovery。

F9 优先自动解决可确定问题。派生层故障由 F9 自动恢复；只有多个合法、实质不同、没有确定性 Winner 且无法安全并行处理的情况才请求 Human Clarification。局部未解析只阻塞依赖该分支的查询，不默认阻塞整个 Query。

Query Plan、Query Scope Snapshot、Recovery Trace 和 Query Cache 均属于派生、任务上下文敏感、可重建信息，不获得 Canonical Truth、Authority、Profile Binding、Runtime Permission 或 Mutation Scope。

---

## 106. HUMAN_APPROVED Effect

本文件已经获得：

```text
F9-D03 HUMAN_APPROVED
```

因此：

```text
Query Resolution Plan Architecture
= ARCHITECTURALLY_FROZEN

Scope Resolution Boundary
= ARCHITECTURALLY_FROZEN

Profile Applicability Query Boundary
= ARCHITECTURALLY_FROZEN

Temporal Query Resolution Boundary
= ARCHITECTURALLY_FROZEN

Domain Role Resolution Boundary
= ARCHITECTURALLY_FROZEN

Search Space Expansion Boundary
= ARCHITECTURALLY_FROZEN

Query Failure / Recovery Boundary
= ARCHITECTURALLY_FROZEN
```

但仍然：

```text
F9 Implementation
= NOT_AUTHORIZED

RP2
= NOT_AUTHORIZED

Authority Cutover
= NOT_AUTHORIZED

Canonical Replacement
= NOT_AUTHORIZED

Final Activation
= NOT_AUTHORIZED

Legacy Retirement
= NOT_AUTHORIZED

SQLite Physical Schema
= NOT_FROZEN
```

`F9-D03 HUMAN_APPROVED` 只表示本决策的架构语义冻结，不代表任何 Query Engine、数据库、向量检索、缓存、权限系统、Context Builder、运行时搜索或代码施工授权。

# F9-D02 — Indexed Subject & Metadata Model

**中文名称：被索引主体与元数据模型**

## 0. 冻结状态

| 项目 | 内容 |
|---|---|
| Stage | F9 — Index / Projection / Cache Architecture |
| Decision | F9-D02 |
| 名称 | Indexed Subject & Metadata Model |
| 中文名称 | 被索引主体与元数据模型 |
| Approval Status | `HUMAN_APPROVED` |
| Exact Approval | `F9-D02 HUMAN_APPROVED` |
| 前置批准 | `F9-G01 HUMAN_APPROVED` |
| 前置批准 | `F9-D01 HUMAN_APPROVED` |
| 上游正式架构基线 | F1～F8 v1.1 Architecture Freeze Baseline |
| Implementation | `NOT_AUTHORIZED` |
| RP2 | `NOT_AUTHORIZED` |
| Authority Cutover | `NOT_AUTHORIZED` |
| Canonical Replacement | `NOT_AUTHORIZED` |
| Final Activation | `NOT_AUTHORIZED` |
| Legacy Retirement | `NOT_AUTHORIZED` |
| SQLite Physical Schema | `NOT_FROZEN` |

本决策只冻结 F9 的 Indexed Subject（被索引主体）与逻辑 Metadata（元数据）架构边界。

本决策不冻结任何具体数据库、物理 Schema、字段名称、API、文件格式、搜索引擎、向量数据库、图数据库、Embedding 模型或实现技术。

---

## 1. 决策目标

F9-D02 解决：

> F9 到底对“什么东西”建立可发现索引，以及一个被索引主体至少需要携带哪些逻辑信息，才能支持后续搜索、上下文加载、新鲜度判断、反向发现、影响分析和可追溯性，同时不把 F9 变成新的 Canonical Truth（正式真相）、Authority（权威）或万能 Core。

核心目标：

```text
找到正确对象
+
知道这个对象是谁
+
知道它属于哪个范围
+
知道它由谁负责
+
知道它从哪里来
+
知道它当前依据什么状态存在
+
知道索引结果是否仍可信
+
能够回到真正的上游权威来源
```

同时必须保证：

```text
Index Convenience
!= New Semantic Authority
```

---

## 2. 总体架构结论

F9 采用：

```text
Upstream Domain Truth
        ↓
Governed Subject Identity
        ↓
Indexed Subject
        ↓
Core Metadata
+ Typed Facets
        ↓
Discovery Projection / Search Unit
        ↓
Occurrence / Locator
```

上游 Domain Truth 仍由 F1～F8 及未来适用 Domain Owner 拥有。

F9 只建立：
- 可发现性；
- 定向导航；
- 可重建派生信息；
- 索引元数据；
- 搜索投影；
- 关系索引；
- 来源与血缘索引；
- 新鲜度证据引用；
- 后续查询、影响发现和上下文加载所需的派生结构。

F9 不建立第二套 Product Truth、Design Truth、Rule Truth、Binding Truth、Authority Truth、Current Effective Truth 或 Canonical Relation Truth。

---

## 3. Indexed Subject 定义

`Indexed Subject` 是：

> 具有稳定发现、导航、上下文加载、关系发现、新鲜度判断或影响分析价值，并能够稳定指向、确定边界和追溯来源的逻辑主体。

Indexed Subject 是 F9 的索引对象身份视图，不是新的 F1 Top-level Object。

```text
Indexed Subject
!= New F1 Object Family
!= Canonical Truth Copy
!= Search Chunk
!= Physical File
!= Database Row
```

---

## 4. Indexed Subject / Discovery Unit / Occurrence 分离

### 4.1 Indexed Subject
表达“这是哪个逻辑主体”。

### 4.2 Discovery Unit
为了全文搜索、向量搜索、Embedding、摘要、分词、排名、局部加载而生成的可重建搜索单位。

### 4.3 Occurrence / Locator
表达某个 Subject 在什么 Source、什么位置出现。

正式冻结：

```text
Indexed Subject != Discovery Unit
Indexed Subject != Search Chunk
Indexed Subject != Embedding Unit
Indexed Subject != Occurrence
Indexed Subject != Locator
```

---

## 5. Subject 资格模型

F9 不建立封闭 Subject 类型白名单。

一个正式 Indexed Subject 必须同时满足：

### Addressable — 可稳定指向
能够明确回答“到底是哪一个主体”。

### Independently Useful — 有独立发现价值
具有独立查询、导航、上下文加载、关系发现、影响分析或新鲜度跟踪价值。

### Bounded — 边界可独立解释
具有适用的独立 Scope、Owner、Revision、Version、Lifecycle、Relation、Current Effective 或影响范围边界。

### Traceable — 可追溯
能够最终追溯到 Source Role、Source/Occurrence、适用 Revision/Basis、Provenance、Applicable Owner。

无法可靠追溯的派生搜索内容不得提升为可信治理信息。

---

## 6. Subject 粒度原则

采用：

**Minimum Stable Independent Subject — 最小稳定独立主体原则**

若一个 Subject 内部包含多个彼此独立的 Stable Identity / Scope / Owner / Revision / Lifecycle / Relation / Current Effective / Impact Boundary，则可能过粗。

若拆出的单位没有独立身份、Scope、Owner、变化或关系/导航价值，则过细，应保留为 Discovery Unit / Occurrence。

安全默认：

```text
Prefer Discovery Unit
over premature Subject promotion
```

---

## 7. File 与 Subject 分离

```text
File != Subject
```

一个 File 可包含 `0..N` Indexed Subjects。

一个 Subject 可存在于 `1..N` Occurrences。

文件数量不得解释为 Subject 数量。

---

## 8. Subject Hierarchy

允许父子 Subject：

```text
PRD Document
  ↓ contains
Product Area
  ↓ contains
Requirement
```

但：

```text
Containment != Authority
Parent != Higher Authority
Child != Lower Authority
```

层级只服务导航、搜索展开、定向加载和组织结构。

---

## 9. Subject Kind 开放扩展

F9 Core 不硬编码所有领域类型。

Subject Kind 由上游 Domain Contract / Adapter 扩展。

```text
New Domain Type
!= F9 Core Rewrite
```

---

## 10. Core Metadata + Typed Facets

正式采用：

```text
Core Metadata Envelope
+
Typed Facets
```

禁止所有 Subject 强制填写大型万能 Metadata Record。

---

## 11. Metadata 强度

### Mandatory
正式 Indexed Subject 必须存在。

### Conditional Mandatory
对应语义存在时必须存在。

### Optional
服务搜索、排名、摘要、导航、体验、性能；丢失不得改变正式语义。

---

## 12. Core Metadata — Identity

正式 Indexed Subject 至少可表达：

```text
Subject Reference
Identity Kind
Subject Kind
Domain Reference
```

```text
Governed Subject Identity
!= F9 Discovery Identity
```

---

## 13. Scope / Applicability

Scope / Applicability 属于 Core Metadata 能力。

```text
Missing Scope
!= Global Scope
```

D02 只冻结 Scope Metadata 承载能力。

```text
Scope Metadata
!= Scope Resolution
```

Scope / Profile / Query Resolution 属于 F9-D03。

---

## 14. Owner Metadata

正式 Subject 必须能够表达：

```text
Explicit Owner Reference
```

或：

```text
Deterministic Owner Resolution Reference
```

```text
Indexed Owner Reference
!= F9 Ownership Decision
```

无法确定 Owner 时进入明确 UNKNOWN / UNRESOLVED 或适用治理状态，不得默认 `owner = F9`。

---

## 15. Authority Metadata

Authority 为 Conditional Mandatory。

涉及 Decision、Approval、Canonical Mutation、Protected Action、Runtime Permission、Binding Resolution、Governed Exception 时，必须能够携带 Authority Reference / Basis / Scope / Constraints。

```text
Authority Reference != Authority Transfer
Index Match != Effective Authority
Search Ranking != Authority Ranking
```

---

## 16. Source Role 与 Source Locator

```text
Source Role != Source Locator
Path Change != Source Role Change
Path Change != Subject Identity Change
```

---

## 17. Occurrence Model

一个 Subject 可拥有多个 Occurrence。

Occurrence 可表达 Source Reference、Source Role、Locator、Revision/Fingerprint、Provenance、Observation Basis。

```text
Occurrence != Subject
Multiple Occurrences != Multiple Subjects
```

---

## 18. Provenance 与 Lineage

Provenance / Lineage 属于正式 Subject 核心能力。

重要 Derived Projection 同样必须保留 Provenance。

```text
Derived Metadata
must retain provenance
```

---

## 19. Lifecycle / State Metadata

F9 不建立万能 `status` 替代领域状态。

状态应能够保留：

```text
State Domain
State Reference
State Owner
State Basis
```

```text
Same State Label
!= Same State Domain
```

---

## 20. Freshness Metadata

Freshness 表达能力属于 Core Metadata。

可表达：
- Freshness Applicability；
- Freshness Evidence Reference；
- Observed Revision / Fingerprint；
- Freshness State。

但：

```text
Freshness Metadata
!= Freshness Resolution Algorithm
```

Freshness Evaluation / Revalidation 属于 F9-D06。

---

## 21. Revision / Version / Effective Facet

若 Subject 存在对应语义，则必须独立表达。

```text
Stable ID != Revision
Revision != Version
Latest != Current Effective
Lifecycle != Freshness
```

不得压成模糊 `current_version`。

---

## 22. Binding / Resolution Facet

可携带 Binding Target Reference、Binding Purpose、Candidate References、Resolution Result Reference、Resolution Basis。

必须保持：

```text
Index Match != Candidate Eligibility
Candidate Eligibility != Effective Binding
Similarity != Binding Winner
Latest != Binding Winner
File Order != Binding Winner
AI Confidence != Binding Winner
```

---

## 23. Governed Relation 与 Derived Discovery Edge

正式 Governed Relation 的语义由上游 Domain Owner 定义。

F9 可生成 Similarity / Co-occurrence / Possible Relation / Embedding Near / Impact Candidate 等 Derived Discovery Edge。

必须明确：

```text
Derived Discovery Edge != Governed Relation
Search Match != Canonical Relation
Similarity != Semantic Equivalence
Index Edge != Canonical Dependency
```

---

## 24. Discovery Facet

可包含 Alias、Keyword、Summary、Embedding、Search Token、Language Hint、Ranking Hint。

```text
Alias != Stable Identity
Summary != Canonical Content
Embedding != Semantic Truth
Search Ranking != Governance Priority
```

这些可以删除、重建、换模型而不改变正式 Subject Identity。

---

## 25. Protection / Visibility

F9 必须能够保存适用 Protection / Visibility / Access Constraint Reference。

```text
Index Visibility
must not expand Source Visibility

Protection Reference
!= Runtime Permission
```

---

## 26. Metadata 不得复制完整 Canonical Truth

F9 Core Metadata 不直接拥有完整 Product Rule Body、PRD Truth、UI_SPEC Truth、Workflow Definition、Policy Definition、Binding Logic、Authority Logic、Runtime State 或第二份 Canonical Business Content。

可保存 Reference、Search Projection、Summary、Excerpt、Fingerprint、Derived Representation。

```text
Metadata != Canonical Content Copy
```

---

## 27. Missing Metadata 规则

禁止：

```text
Missing Scope → Global
Missing Owner → F9
Missing Version → Latest
Missing Authority → Allowed
Missing Gate → PASS
Missing Relation → No Dependency
```

```text
Missing Required Metadata
!= Default PASS
```

---

## 28. Metadata Completeness 不等于有效性

```text
Metadata Complete != Subject Valid
Metadata Complete != Current Effective
Metadata Complete != Authority Valid
Metadata Complete != Fresh
```

---

## 29. Facet 不得互相夺权

```text
Facet contributes information
but does not redefine another domain's authority.
```

---

## 30. Subject Identity 连续性总原则

```text
Subject Identity
follows semantic identity
```

以下变化默认不创建新 Subject：

```text
File Rename
Directory Move
Path Change
Representation Format Change
Alias Change
Search Projection Change
Embedding Change
Index Rebuild
```

---

## 31. Fingerprint / Hash 边界

```text
Fingerprint
= Change Detection Evidence

Fingerprint
!= Stable Identity
```

---

## 32. Revision 与 Subject Identity

```text
New Revision != New Subject

Revision != Replacement
Revision != Split
Revision != Merge
```

---

## 33. 大幅内容变化不自动重建身份

F9 可发现 Major Semantic Delta Candidate，但不得根据文本差异、Embedding 差异、名称变化或 AI 判断自动宣布旧 Subject 结束、新 Subject 创建。

---

## 34. Identity Resolution 顺序

```text
Explicit Governed Identity
↓
Governed Evolution Record
↓
Deterministic Identity Mapping
↓
UNKNOWN / UNRESOLVED
```

AI Guess、Latest File、Index Order、Search Ranking、Similarity Score 不得作为正式 Identity Winner。

---

## 35. Split

```text
Old Subject
↓ SPLIT_INTO
New Subject A
New Subject B
```

```text
Split != Rename
Split does not erase predecessor history
```

---

## 36. Merge

```text
Subject A
Subject B
↓ MERGED_INTO
Subject C
```

```text
Merge != Rename
```

---

## 37. Replacement

```text
Old Subject
↓ REPLACED_BY
New Subject
```

```text
Revision != Replacement
```

---

## 38. Superseded / Retired

```text
Superseded != Deleted History
Retired != Reusable Identity
```

Stable Identity 不得分配给无关新 Subject。

---

## 39. Discovery Duplicate 自动修复

Discovery-only 重复记录在确定性证据下可由 F9 自动去重/合并。

属于 Derived Index Repair，不属于 Canonical Semantic Mutation。

---

## 40. Governed Identity 不得由 F9 自动合并

```text
Similarity != Identity Equivalence
Two Governed IDs != F9 Merge Authority
```

F9 可生成 Possible Duplicate Candidate 并路由 Domain Owner。

---

## 41. Identity Conflict

同一 Governed Stable ID 指向互不兼容语义主体时形成 Identity Conflict。

禁止 Latest File / Last Write / Index Order / Similarity / AI Confidence 作为 winner。

---

## 42. Discovery Identity → Governed Identity

可形成：

```text
Discovery Identity
↓ RESOLVED_TO
Governed Identity
```

历史 Discovery Identity 与 Provenance 保留。

```text
Identity Candidate Match
!= Identity Promotion
```

F9 无权自行升级为 Domain Governed Identity。

---

## 43. Identity Correction

历史错误身份映射通过可审计 Identity Correction / Supersession / Rebinding History 修正。

```text
Identity Correction
!= History Rewrite
```

---

## 44. Owner / Scope / Locator 变化与身份

```text
Owner Change != Automatic Identity Change
Scope Change != Automatic Identity Change
Locator Change != Automatic Identity Change
```

正式 Split / Merge / Replacement 由 Domain Governance 决定。

---

## 45. Index Entry Identity

必须区分：

```text
Governed Subject Identity
F9 Discovery Identity
Index Entry Identity
```

```text
Governed Subject ID
!= Discovery ID
!= Index Entry ID
```

---

## 46. Index Rebuild

```text
Index Rebuild
must preserve Subject Identity
when upstream identity is unchanged.
```

---

## 47. Historical 与 Current Resolution

```text
Historical Identity Resolution
!= Current Identity Resolution
```

D02 只保留身份和血缘能力；Query 如何选择当前/历史由后续 Query Resolution 设计处理。

---

## 48. Subject Candidate Discovery

F9 可发现：
- Potential Subject Candidate；
- Potential Duplicate；
- Potential Split；
- Potential Merge；
- Potential Relation；
- Potential Identity Correction。

但：

```text
Candidate Detection != Canonical Promotion
Candidate Detection != Semantic Mutation
```

---

## 49. Code / Evidence Subject 边界

```text
Indexed Code Evidence != Architecture Truth
Code Location != Semantic Owner
Code Dependency != Canonical Dependency
Current Code != Automatic Product Truth
```

---

## 50. F9 与上游 Owner 边界

F9 可：

```text
index
discover
reference
project
search
trace
surface
rebuild
```

F9 不可因此：

```text
decide
approve
canonically mutate
grant authority
grant runtime permission
```

---

## 51. 与 F9-D03 的边界

```text
D02 = Scope Metadata Capability
D03 = Scope / Profile / Query Resolution
```

---

## 52. 与 F9-D06 的边界

```text
D02 = Freshness Metadata Capability
D06 = Freshness Resolution & Revalidation
```

---

## 53. 与 F9-D08 的边界

```text
D02 = Subject / Reference / Relation Index Foundation
D08 = Dependency / Impact Discovery
```

D02 不是 Impact Engine。

---

## 54. AI 自动化边界

AI / F9 可以自动：
- 扫描可索引来源；
- 建立 Discovery Unit；
- 生成 Embedding / Summary / Keyword；
- 建立搜索 Projection；
- 检测可能重复、关系、身份冲突；
- 识别 Subject Candidate；
- 在确定性证据下合并 Discovery-only Records；
- 重建 Index；
- 更新派生 Metadata；
- 准备 Decision / Review Evidence Package。

AI / F9 不得自动：
- 创造新 Domain Authority；
- 将 Discovery Identity 升级为 Governed Identity；
- 合并两个 Governed Identities；
- 决定正式 Split / Merge / Replace；
- 创建正式 Product / Design / Rule 语义；
- 将 Search Similarity 升级为 Governed Relation；
- 将 Code Evidence 升级为 Architecture Truth；
- 将 Metadata Completeness 升级为 Current Effective；
- 将 Freshness Evidence 升级为 Authority；
- 将 Index Match 升级为 Binding Winner。

---

## 55. 明确禁止的万能结构

禁止建立：

```text
UniversalSubjectAuthority
UniversalSemanticOwner
UniversalRelationAuthority
UniversalIdentityResolver
UniversalBindingResolver
UniversalStateTruth
UniversalMetadataTruth
```

F9 应保持：

```text
Thin Core
+
Extensible Subject Kinds
+
Typed Facets
+
Domain-Owned Semantics
```

---

## 56. 本决策明确不冻结

不冻结：
- SQLite 表结构；
- DDL；
- JSON/YAML/protobuf Schema；
- Go struct；
- Stable ID 字符串格式；
- Index Entry ID 格式；
- 字段名称/长度；
- 数据库索引类型；
- FTS / Vector DB / Graph DB；
- Elasticsearch / OpenSearch；
- Embedding / Reranker；
- Chunk 大小和算法；
- Tokenization；
- Cache 结构；
- 序列化格式；
- 搜索评分公式；
- Freshness 算法；
- Watcher / Polling / Git Hook；
- API / CLI / WebUI；
- 权限实现；
- Migration；
- Legacy Retirement；
- Runtime 执行逻辑。

---

## 57. 核心不变量

```text
Index != Truth
Index != Authority

Indexed Subject != New F1 Top-level Object

Indexed Subject != Search Chunk
Indexed Subject != Occurrence
Indexed Subject != Index Entry

File != Subject

Governed Subject Identity
!= F9 Discovery Identity
!= Index Entry Identity

Stable Identity != Path
Stable Identity != File Name
Stable Identity != Hash
Stable Identity != Embedding
Stable Identity != Revision
Stable Identity != Version

Revision != Replacement
Revision != Split
Revision != Merge

Source Role != Source Locator

Alias != Identity

Search Match != Governed Relation
Similarity != Semantic Equivalence
Index Edge != Canonical Dependency

Authority Reference != Authority Transfer
Index Match != Effective Authority

Metadata != Canonical Truth Copy

Missing Scope != Global
Missing Owner != F9
Missing Version != Latest
Missing Authority != Allowed
Missing Required Metadata != PASS

Discovery Candidate != Canonical Promotion

Code Evidence != Architecture Truth

Index Rebuild != Identity Rebuild

Superseded != Deleted History
Retired Identity != Reusable Identity

Containment != Authority
Parent != Higher Authority

Freshness Evidence != Authority

Metadata Complete != Current Effective

Index Visibility must not expand Source Visibility
```

---

## 58. Acceptance Gates

- D02-AF-01 Indexed Subject 与 Search Chunk / Discovery Unit / Occurrence 明确分离。
- D02-AF-02 Subject 资格采用开放资格模型，而不是封闭白名单。
- D02-AF-03 Subject 粒度采用 Minimum Stable Independent Subject。
- D02-AF-04 File 与 Subject 非一一关系。
- D02-AF-05 Core Metadata 与 Typed Facets 分离，无万能 Record。
- D02-AF-06 Mandatory / Conditional Mandatory / Optional 明确。
- D02-AF-07 Identity / Scope / Owner / Source / Provenance / State / Freshness 公共边界明确。
- D02-AF-08 Revision / Version / Current Effective 不压缩成一个概念。
- D02-AF-09 Governed Relation 与 Derived Discovery Edge 隔离。
- D02-AF-10 Discovery Projection 不获得 Canonical Semantic Authority。
- D02-AF-11 Protection / Visibility 不因索引扩大。
- D02-AF-12 Missing Metadata 不存在静默安全默认。
- D02-AF-13 Rename / Move / Format Change / Rebuild 不自动产生新 Subject。
- D02-AF-14 Split / Merge / Replace / Supersession 历史可追踪。
- D02-AF-15 Discovery Identity 与 Governed Identity 升级边界明确。
- D02-AF-16 Duplicate Discovery Record 可自动修复，Governed Identity 合并不得由 F9 擅自执行。
- D02-AF-17 Identity Conflict 不使用 Latest / File Order / Search Ranking / AI Confidence 解决。
- D02-AF-18 Index Rebuild 不改变未变化 Governed Subject Identity。
- D02-AF-19 F9 不获得 F5/F6/F7/F8 语义 Owner 或 Authority。
- D02-AF-20 D02 未提前冻结 D03 / D06 / D08 Resolver / Algorithm / Impact Engine。
- D02-AF-21 Implementation、RP2、Authority Cutover、Canonical Replacement、Final Activation、Legacy Retirement 仍未授权。
- D02-AF-22 SQLite Physical Schema 仍为 `NOT_FROZEN`。

---

## 59. Final Owner Boundary

```text
Upstream Domain Owner
→ owns semantic truth

F7
→ owns protected canonical mutation path

F8
→ owns applicable project binding /
   effective project resolution semantics

F9
→ owns derived discovery /
   index / projection metadata architecture

F10
→ future runtime permission / execution

F11
→ future UX / Control Plane

F12
→ future migration / retirement
```

F9 的 Owner 范围仅限派生索引、搜索发现、投影元数据以及这些派生结构的完整性。

---

## 60. Architecture Closure

```text
Governed Subject
        ↓
Indexed Subject Reference
        ↓
Core Metadata
        │
        ├─ Identity
        ├─ Scope / Applicability
        ├─ Owner Reference
        ├─ Source / Occurrence
        ├─ Provenance / Lineage
        ├─ State Reference
        └─ Freshness Capability
        │
        ├─ Revision / Version Facet
        ├─ Authority Facet
        ├─ Binding Facet
        ├─ Relation Facet
        ├─ Protection Facet
        └─ Other Typed Facets
        ↓
Discovery Projection
        ├─ Alias
        ├─ Keyword
        ├─ Summary
        ├─ Search Tokens
        └─ Embedding
```

```text
Truth stays upstream.
Authority stays upstream.
Canonical mutation stays governed.
F9 remains rebuildable.
```

---

## 61. Final Decision

Banyan F9 采用以稳定逻辑 Subject 为中心的索引模型，而不是以文件、Chunk、数据库行或搜索向量为中心的身份模型。

Indexed Subject 必须满足可指向、独立有用、边界明确、来源可追溯四项基本资格，并采用最小稳定独立主体粒度。

所有 Indexed Subject 共享最小 Core Metadata Contract，并通过 Typed Facets 承载领域特有信息；不得建立万能巨大 Schema，也不得将 F9 Metadata 复制层升级为第二套 Canonical Truth。

Governed Identity、Discovery Identity 和 Index Entry Identity 严格分离；文件移动、改名、Revision、Projection 或 Index Rebuild 不自动改变正式主体身份。Split、Merge、Replacement、Supersession 和 Identity Correction 必须保留完整 Lineage，不得覆盖历史。

F9 可以自动维护派生索引、搜索投影和 Discovery Identity，也可以发现关系、重复、冲突和 Subject Candidate，但不得自行创造或合并上游 Governed Identity，不得将相似度、搜索排名、文件顺序、Latest 或 AI Confidence 升级为正式语义、关系、Authority 或 Current Effective 结论。

F9-D02 只冻结逻辑 Indexed Subject 与 Metadata Architecture；Scope / Profile / Query Resolution 留给 F9-D03，Freshness Evaluation / Revalidation 留给 F9-D06，Dependency / Impact Discovery 留给 F9-D08。所有物理 Schema、数据库、索引引擎、Embedding、字段名称和实现机制继续 Deferred，等待未来 Implementation Plan 与 Implementation Freeze。

---

## 62. HUMAN_APPROVED Effect

本文件已经获得：

```text
F9-D02 HUMAN_APPROVED
```

因此：

```text
Indexed Subject Model
= ARCHITECTURALLY_FROZEN

Subject Eligibility / Granularity
= ARCHITECTURALLY_FROZEN

Core Metadata + Typed Facets
= ARCHITECTURALLY_FROZEN

Identity Continuity / Evolution Boundary
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

`F9-D02 HUMAN_APPROVED` 只表示本决策的架构语义冻结，不代表任何代码施工、数据库建立、迁移、运行时启用或正式切换授权。

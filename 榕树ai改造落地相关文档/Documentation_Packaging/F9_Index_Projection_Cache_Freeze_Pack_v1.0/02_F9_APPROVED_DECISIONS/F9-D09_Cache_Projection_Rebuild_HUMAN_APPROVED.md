# F9-D09 — Cache / Projection / Rebuild

**中文名称：缓存、派生投影与重建**

---

## 0. 文档身份

| 项目 | 内容 |
|---|---|
| Stage | F9 — Index / Projection / Cache Architecture |
| Decision | F9-D09 |
| 名称 | Cache / Projection / Rebuild |
| 中文名称 | 缓存、派生投影与重建 |
| 当前状态 | `HUMAN_APPROVED` |
| 精确批准语句 | `F9-D09 HUMAN_APPROVED` |
| 前置批准 | `F9-G01 HUMAN_APPROVED` |
| 前置批准 | `F9-D01 HUMAN_APPROVED` |
| 前置批准 | `F9-D02 HUMAN_APPROVED` |
| 前置批准 | `F9-D03 HUMAN_APPROVED` |
| 前置批准 | `F9-D04 HUMAN_APPROVED` |
| 前置批准 | `F9-D05 HUMAN_APPROVED` |
| 前置批准 | `F9-D06 HUMAN_APPROVED` |
| 前置批准 | `F9-D07 HUMAN_APPROVED` |
| 前置批准 | `F9-D08 HUMAN_APPROVED` |
| Implementation | `NOT_AUTHORIZED` |
| RP2 | `NOT_AUTHORIZED` |
| Authority Cutover | `NOT_AUTHORIZED` |
| Canonical Replacement | `NOT_AUTHORIZED` |
| Final Activation | `NOT_AUTHORIZED` |
| Legacy Retirement | `NOT_AUTHORIZED` |
| SQLite Physical Schema | `NOT_FROZEN` |

本决策只冻结 Cache、Projection、Derived Artifact、Derived Generation、Rebuild、Refresh、Invalidate、Publication、Retention、Recovery 与相关 Owner Boundary 的架构语义。

不冻结具体 Redis / SQLite / Database Table、Hash Algorithm、Queue、Worker、Scheduler、Transaction、Pointer Swap、GC 实现、重试次数、并发数、Go Struct、API、UI 或其他物理实现。

---

## 1. 核心定位

F9-D09负责：

> 对 F9 派生层中的 Cache、Projection、Index、Context Snapshot、Dependency / Impact Projection 等对象执行安全的失效、刷新、重建、发布、保留和清理。

D09负责的是：

```text
Derived State Maintenance
```

不是：

```text
Canonical Truth Maintenance
```

正式冻结：

```text
Rebuild != Canonical Mutation
Cache Repair != Source Repair
```

---

## 2. Derived Artifact

## Derived Artifact
**派生产物**

表示：

> 根据一个或多个 Source / Effective Basis 计算、索引、摘要、转换、投影或缓存出的结果。

可包括：

- Index Entry；
- Search Projection；
- Context Snapshot；
- Dependency Projection；
- Impact Projection；
- Freshness Projection；
- Consumer Projection；
- Derived Summary；
- Cache Entry。

正式冻结：

```text
Derived Artifact != Canonical Source
```

---

## 3. Cache / Projection / Index 分离

Cache、Projection、Index 可以共享物理存储，但逻辑职责不同。

```text
Cache != Projection
Projection != Index
```

Cache 主要服务复用。

Projection 主要服务特定用途的语义视图。

Index 主要服务发现、导航与检索。

---

## 4. Physical Storage 与 Semantic Identity 分离

正式冻结：

```text
Physical Storage Similarity
!= Semantic Identity

Logical Contract
!= Physical Schema
```

因此当前仍保持：

```text
SQLite Physical Schema = NOT_FROZEN
```

---

## 5. Cache 的语义

Cache 表示：

> 某个已计算 Derived Result 在满足兼容条件时可被再次复用。

Cache 必须能追溯：

- Cached What；
- Derived From What；
- Purpose；
- Scope；
- Temporal；
- Profile / Applicability；
- Protection；
- Rebuild Basis；
- Provenance。

不得只剩裸 `key → value` 语义。

---

## 6. Cache Semantic Identity

正式冻结：

```text
Cache Key
!= Cache Semantic Identity

Same Query Text
!= Same Cache Semantics
```

Cache Semantic Identity 必须考虑会影响结果语义的 Purpose、Scope、Profile、Temporal、Protection、Source Basis 等因素。

具体物理 Cache Key 格式不冻结。

---

## 7. Cache Hit 的边界

正式冻结：

```text
Cache Hit
!= Freshness Confirmation

Cache Hit
!= Applicability Confirmation

Cache Hit
!= Runtime Authorization
```

Cache Hit 只说明存在可候选复用的结果。

---

## 8. Projection 的语义

## Projection
**派生投影**

表示：

> 按特定用途，从 Source / Effective Basis 中抽取、转换或重组出的 Derived View。

正式冻结：

```text
Projection is purpose-specific
```

同一个 Source 可以拥有：

- Search Projection；
- Context Projection；
- Dependency Projection；
- Impact Projection；
- Consumer Projection。

---

## 9. Projection 不取得 Source Authority

Projection 可以复制 Authority Metadata，但不能因此成为 Authority Owner。

```text
Projected Authority Metadata
!= Projection Authority
```

---

## 10. Projection Contract

每类重要 Projection 应具有：

## Projection Contract
**投影契约**

逻辑上定义：

- Input Kind；
- Output Semantic Fields；
- Purpose；
- Coverage；
- Normalization；
- Protection；
- Dependency Expectation；
- Input Obligation；
- Coherence Boundary；
- Publication Boundary。

正式冻结：

```text
Projection Contract
!= Implementation Schema

Logical Projection Contract
!= Physical Database Schema
```

---

## 11. Projection Definition 与 Result 分离

```text
Projection Definition
!= Projection Result
```

同一个 Projection Definition 可基于不同 Source Basis 生成多个 Result / Generation。

---

## 12. Projection Definition Evolution

正式冻结：

```text
Projection Definition Change
!= Source Change
```

Projection Definition 改变时，需要 Rebuild Compatibility Evaluation，但：

```text
Projection Definition Change
!= Full Rebuild Automatically
```

---

## 13. Projection Contract Version

Projection Contract 可独立演进。

但：

```text
Projection Contract Version
!= Domain Version
```

Contract Evolution 应保留兼容关系、Rebuild Requirement 与 Provenance。

---

## 14. Rebuild

## Rebuild
**重建**

表示：

> 根据当前可接受的 Authoritative Source 或 Applicable Governed Effective Result，重新生成 Derived Artifact。

正式冻结：

```text
Rebuild
!= Canonical Mutation
```

---

## 15. Rebuild 与 Re-resolution 分离

正式冻结：

```text
Rebuild
!= Re-resolution
```

如果 Scope、Profile、Temporal、Query Resolution Basis 发生实质变化：

```text
→ D03 Re-resolution
```

D09不能拿旧 Resolution Basis 强行重建。

---

## 16. Rebuild 与 Revalidation 分离

正式冻结：

```text
Rebuild Complete
!= Freshness Satisfied
```

重建完成后，必要时回 D06判断当前任务 Freshness Requirement 是否满足。

---

## 17. Rebuild 与 Authority Resolution 分离

正式冻结：

```text
Rebuild Selection
!= Authority Resolution
```

D09不能因为：

- Latest；
- Highest Version；
- Search Rank；
- Most Recent File；

而自行选 Effective Winner。

---

## 18. Rebuild Basis

重要 Rebuild 必须具有可追踪：

## Rebuild Basis
**重建依据**

逻辑上包括：

- Target Derived Artifact；
- Source / Effective Basis；
- Scope；
- Temporal；
- Profile / Applicability；
- Protection；
- Dependency Basis；
- Projection Contract；
- Rebuild Reason；
- Trigger Evidence；
- Provenance。

---

## 19. Rebuild Result Provenance

不得只记录：

```text
status = SUCCESS
```

应能解释：

```text
What rebuilt?
From what?
Which basis?
Which coverage?
Which contract?
Which trigger?
Which unresolved input?
```

正式冻结：

```text
Rebuild Success
without Basis
is insufficient provenance
```

---

## 20. Invalidate / Evict / Refresh / Rebuild 分离

## Logical Invalidate
不能再无条件复用。

## Physical Evict
物理删除或驱逐。

## Refresh
轻量更新。

## Rebuild
按 Basis 重新生成。

正式冻结：

```text
Invalidate != Evict
Invalidate != Rebuild
Refresh != Full Rebuild
```

---

## 21. Current Stale 与 Historical Value 分离

正式冻结：

```text
Stale For Current
!= Useless For History
```

旧 Derived Artifact 即使不适用于 Current，也可能继续用于：

- Historical；
- Audit；
- Recovery；
- Comparison；
- Debugging。

---

## 22. Invalidation 不自动立即 Rebuild

正式冻结：

```text
Invalidated
!= Must Rebuild Immediately
```

允许不同策略：

- Eager；
- Lazy；
- On-demand；
- Batch。

具体策略与调度算法不冻结。

---

## 23. Rebuild Policy

Rebuild Policy 应根据：

- Artifact Kind；
- Purpose；
- Consumer Demand；
- Materiality；
- Risk；
- Freshness Requirement；
- Protection；
- Dependency Breadth；
- Cost；
- Blocking Status。

正式冻结：

```text
Rebuild Policy
is artifact- and purpose-aware
```

---

## 24. TTL 边界

TTL 可以触发：

- Revalidation；
- Refresh；
- Rebuild Candidate。

但：

```text
TTL Expired
!= Semantic Invalidity
```

TTL 不定义 Truth。

---

## 25. Rebuild Trigger 来源

D09可消费：

- D06 Freshness Result；
- D07 Invalidation Trigger；
- D08 Impact Result；
- Consumer Demand；
- Recovery Result；
- Missing Derived Artifact；
- Governed Policy / Time Trigger。

正式冻结：

```text
D09 consumes rebuild triggers
```

D09不成为第二套 Change Detection Engine。

---

## 26. Safety Check

D09可以检查：

- Source 是否存在；
- Basis 是否可用；
- Contract 是否兼容；
- Protection 是否满足；
- Publication 是否仍有资格。

但不得猜测缺失的：

- Source；
- Scope；
- Profile；
- Effective Result；
- Owner。

---

## 27. D09 与 D05 / D03 / D06 / D08 边界

```text
Missing Source / Basis
→ D05

Resolution Basis changed
→ D03

Freshness Sufficiency
→ D06

Global Impact Boundary unclear
→ D08
```

正式冻结：

```text
Rebuild != Recovery
Rebuild Scope Discovery != Global Impact Discovery
```

---

## 28. Partial Rebuild

D09允许：

## Partial Rebuild
**局部重建**

但只有在 Projection Contract 允许且可证明 Coherence 的前提下成立。

---

## 29. Projection Coherence Boundary

## Projection Coherence Boundary
**投影一致性边界**

表示：

> 哪些 Projection Part 必须在兼容 Basis 下作为整体成立。

正式冻结：

```text
Projection Coherence Boundary
is projection-contract-specific
```

Core 不写死万能字段组。

---

## 30. Partial Rebuild 与 Coherence

正式冻结：

```text
Partial Rebuild
must respect coherence boundary

Local Rebuild Success
!= Whole Projection Coherence
```

---

## 31. Projection Coherence 与时间戳分离

```text
Projection Coherence
!= Same Build Timestamp
```

只要 Source / Applicability / Dependency Basis 仍兼容，不要求所有字段同一时间生成。

---

## 32. Unknown Coherence

正式冻结：

```text
Unknown Coherence
must not be treated as coherent
```

如果无法可靠证明局部兼容，可扩大 Partial Rebuild 或升级 Full Rebuild。

---

## 33. Multi-source Rebuild Basis

一个 Derived Artifact 可以依赖多个 Source。

D09必须支持：

## Rebuild Basis Set
**重建依据集合**

例如：

```text
Requirement R6
Profile P3
Protection S2
Binding B5
Projection Contract V4
```

---

## 34. Multi-source Coherence

正式冻结：

```text
Multi-source Rebuild
must preserve basis coherence

Rebuild Basis Coherence
!= Same Observation Timestamp
```

---

## 35. Individually Current 不等于可组合

正式冻结：

```text
Individually Current Inputs
!= Coherent Rebuild Basis Set
```

不能把几个“各自最新”的输入强行拼接。

---

## 36. Compatible Basis 优先于 Latest

D09应选择：

> 当前治理上可组合、可适用的 Basis Set。

而不是简单使用每个 Source 最新版本。

---

## 37. Projection Input Obligation

Projection Contract 应逻辑区分：

- Required Material Input；
- Conditional Material Input；
- Optional Supporting Input。

具体 Schema 不冻结。

---

## 38. Missing Input Consequence

缺少 Input 后果由 Projection Contract + Materiality 决定。

可能：

```text
REBUILD_BLOCKED
```

或：

```text
DEGRADED
```

正式冻结：

```text
Missing Input Consequence
is materiality- and contract-relative
```

不采用全局统一 Fail Open / Fail Closed。

---

## 39. Partial / Degraded Projection

正式冻结：

```text
Partial Rebuild
!= Full Rebuild Success

Degraded Projection
!= Complete Projection
```

Degraded Result 必须显式暴露：

- Missing Basis；
- Coverage Gap；
- Degraded Reason；
- Consumer Limitation。

---

## 40. Degraded Usability

正式冻结：

```text
Degraded Usability
is purpose-relative
```

最终是否足以支撑 Context / Freshness Requirement，由 D04 / D06 判断。

---

## 41. Artifact Identity 与 Generation 分离

正式冻结：

```text
Cache Identity
!= Cache Generation

Projection Identity
!= Projection Generation

Derived Generation
!= Domain Revision
```

---

## 42. Derived Generation

## Derived Generation
**派生代次**

表示同一逻辑 Derived Artifact 的一次可追踪生成状态。

Material Source / Contract / Dependency / Protection Basis 改变时，可以形成新 Generation。

物理使用 INSERT 或 UPDATE 不冻结。

---

## 43. Derived Generation Lineage

重要 Generation 应保留：

- Generated From；
- Basis Set；
- Projection Contract；
- Rebuild Trigger；
- Supersedes / Replaces；
- Previous Generation Relation。

正式冻结：

```text
Derived Generation Lineage
!= Canonical Domain History
```

---

## 44. Refresh 与 Generation

Refresh 是否产生新 Generation，取决于是否改变：

- Material Content；
- Basis；
- Coverage；
- Protection Semantics。

非实质 Metadata Refresh 不必强制新 Generation。

---

## 45. Rebuild Job / Artifact / Generation 分离

正式冻结：

```text
Rebuild Job Identity
!= Derived Artifact Identity

Rebuild Job Identity
!= Derived Generation Identity
```

Job 是一次执行尝试。

Generation 是派生状态。

Artifact 是逻辑对象。

---

## 46. Retry 与 Basis

正式冻结：

```text
Retry With Different Basis
!= Same Rebuild Attempt Semantically
```

重试不能静默换 Source / Basis。

---

## 47. Rebuild Deduplication

正式冻结：

```text
Same Rebuild Target
!= Same Rebuild Work
```

Semantic Rebuild Dedup 至少应考虑：

- Target；
- Basis Set；
- Projection Contract；
- Cause；
- Coverage；
- Material Consumer Requirement。

---

## 48. Dedup 与 Coalescing 分离

Dedup：

> 相同工作执行一次。

Coalescing：

> 兼容的连续变化合并处理。

正式冻结：

```text
Rebuild Coalescing
requires compatible purpose and basis
```

---

## 49. Operational Coalescing

```text
R5 → R6 → R7
```

若只需要 Current Projection，可以直接针对 R7重建。

但：

```text
Operational Rebuild Coalescing
!= Historical Generation Erasure
```

---

## 50. Derived Current Pointer

允许存在逻辑：

## Derived Current Pointer
**派生当前指针**

表示某 Purpose / Scope / Temporal / Consumer 下当前可复用的 Generation。

但：

```text
Derived Current Pointer
!= Canonical Effective Pointer
```

---

## 51. Latest Built 不等于 Current Applicable

正式冻结：

```text
Latest Built Generation
!= Current Applicable Generation

Build Recency
!= Projection Applicability
```

Current Applicable 由 Applicability + Basis 决定，而不是创建时间。

---

## 52. Single Global Current 不总是充分

不同 Consumer 可能合法使用不同 Generation：

- Current Applicable；
- Historical Exact Revision；
- Protected Admin View；
- Tenant-safe View。

正式冻结：

```text
Single Global Current Generation
is not always sufficient
```

---

## 53. Shared Generation 与 Consumer Compatibility

正式冻结：

```text
Shared Derived Generation
requires consumer compatibility
```

Consumer-specific Projection 可以收窄：

- Content；
- Visibility；
- Coverage。

但：

```text
Consumer Projection
may narrow
but must not expand authority or protection eligibility
```

---

## 54. Projection Chain

重要 Derived Artifact 应保留：

## Projection Chain / Derivation Lineage
**投影链 / 派生血缘**

例如：

```text
Canonical Source
↓
Normalized Projection
↓
Search Projection
↓
Consumer Projection
```

但：

```text
Projection Chain
!= Authority Chain
```

---

## 55. Derived Projection 不得反向升级 Authority

正式冻结：

```text
Derived Projection
must not be used as authority-upgrading reconstruction source
```

Source 不可用时，Derived Artifact 只能按 D05 / Governed Recovery Boundary 作为有限 Recovery Evidence。

---

## 56. Build 与 Publish 分离

## Build
构建 Candidate Generation。

## Publish
使 Eligible Consumer 可以看到该 Generation。

正式冻结：

```text
Build Complete
!= Published
```

---

## 57. Publish Eligibility

一个 Generation 是否可发布，至少检查：

- Build Completed；
- Required Input；
- Coherence；
- Protection；
- Required Validation；
- Basis Applicability；
- Supersession；
- Consumer Eligibility。

正式冻结：

```text
Build Success
!= Publish Eligibility
```

---

## 58. Atomic Publication

Consumer-visible Publication 必须保证 Generation-level Coherence。

正式冻结：

```text
Consumer-visible Publication
must preserve generation-level coherence
```

---

## 59. Atomic Publication 与实现机制分离

正式冻结：

```text
Atomic Publication Contract
!= Specific Transaction Mechanism
```

未来可使用：

- Transaction；
- Pointer Swap；
- Versioned Key；
- Copy-on-write；
- Manifest Swap。

当前不冻结。

---

## 60. Building New Generation 不自动失效 Old Generation

正式冻结：

```text
New Generation Building
!= Old Generation Immediately Unusable
```

旧 Generation 是否还可使用，由 Purpose + D04 / D06判断。

---

## 61. Concurrent Rebuild

例如：

```text
J1 @ R6
J2 @ R7
```

正式冻结：

```text
Later Job Completion
!= Newer Applicable Result

Last Write Wins
!= Rebuild Applicability Rule
```

---

## 62. Publish 前重新检查 Basis

Publish 前必须重新确认：

- Rebuild Basis；
- Projection Contract；
- Scope；
- Temporal；
- Profile；
- Protection；
- Consumer Eligibility；
- Supersession。

Successful Build 可能在 Publish 前被 Superseded。

---

## 63. Current Pointer 回退保护

没有明确合法 Rollback Evidence 时：

```text
old late build
```

不得覆盖更新、更适用的 Generation。

但：

```text
Lower Revision
!= Automatically Old
```

合法 Rollback 仍然允许。

---

## 64. Semantic Rebuild Deduplication

同一 Target + Basis + Contract + Cause + Coverage 的语义工作，应允许共享执行。

并发 Consumer Demand 不应产生重复 Semantic Rebuild Work。

---

## 65. Rebuild Storm 防护

D09必须支持逻辑能力：

- Priority；
- Batching；
- Coalescing；
- Dedup；
- Lazy；
- Demand-driven；
- Bounded Concurrency。

具体算法、Worker 数、Batch Size 不冻结。

---

## 66. Rebuild Priority

正式冻结：

```text
Rebuild Priority
!= Authority Priority

Rebuild Priority
!= Impact Severity
```

Priority 可参考：

- Current Demand；
- Materiality；
- Risk；
- Freshness Requirement；
- Protection；
- Dependency Breadth；
- Cost；
- Blocking Status；
- Task Purpose。

---

## 67. Build Failure 与 Publication Rejection

正式冻结：

```text
Build Failure
!= Publication Rejection
```

例如 Build 成功但已被新 Generation Supersede，不属于 Build Failure。

---

## 68. Publication Supersession

正式冻结：

```text
Publication Rejected Due To Supersession
!= System Failure
```

这是并发情况下的合法 Outcome。

---

## 69. Rebuild Failure Model

失败至少应能区分：

- Input unavailable；
- Basis incompatible；
- Contract error；
- Build computation failure；
- Validation failure；
- Publication conflict；
- Superseded；
- Protection failure；
- Unknown。

具体 enum 不冻结。

---

## 70. Retry

正式冻结：

```text
Retry
must be cause-aware

Retry without new evidence/progress
must be bounded
```

Basis / Contract 类错误不得盲目无限重试。

---

## 71. Cross-owner Loop Control

D09 ↔ D03 / D05 / D06 / D08 的循环必须每次带来：

- New Evidence；
- New Basis；
- New Availability；
- New Resolution。

否则停止并显式进入：

```text
BLOCKED
UNKNOWN
NEEDS_OWNER
```

正式冻结：

```text
Cross-owner retry loop
must be progress-bounded
```

---

## 72. Rebuild Failure 后 Old Generation

正式冻结：

```text
Rebuild Failure
!= Mandatory Old Cache Deletion
```

也不代表旧 Generation 一定还能 Current Serve。

其可用性由：

- Freshness；
- Purpose；
- Materiality；
- Protection；
- Applicability；

共同决定。

---

## 73. Multiple Retained Generations

一个 Artifact 可以同时保留多个 Generation。

```text
One Artifact Identity
may have multiple retained generations
```

正式冻结：

```text
Retained Generation
!= Current Applicable Generation
```

---

## 74. Publication 与 Historical Retention

正式冻结：

```text
Publish New Generation
!= Retire Historical Generation
```

发布新 Current 不自动删除历史 Generation。

---

## 75. Partial Consumer-visible Publication

默认不假设 Partial Publication 安全。

只有 Projection Contract 明确定义：

## Independent Publication Boundary
**独立发布边界**

时才允许分区独立发布。

正式冻结：

```text
Publication Boundary
must be defined by projection contract
```

---

## 76. Multi-shard Projection

即使多个 Shard 都存在：

```text
All Shards Exist
!= Whole Projection Ready
```

整体状态仍需 Coverage / Coherence / Purpose-aware 判断。

---

## 77. Publication 与 Freshness 分离

正式冻结：

```text
Publication Success
!= Freshness Satisfaction
```

Publish 只是派生层可见性状态，不代表所有任务都 Fresh。

---

## 78. Publication 与 Protection

正式冻结：

```text
Published For Consumer A
!= Eligible For Consumer B
```

Temporary Publication State 也不得放松 Protection Boundary。

---

## 79. Cache Stampede 防护

并发大量请求命中失效 Cache 时，D09应支持语义上的共享重建、有限等待、Fallback / Degraded 路径。

具体 single-flight 等实现不冻结。

---

## 80. Consumer Waiting / Fallback / Fail

不采用统一：

```text
always wait
always serve stale
always fail
```

策略。

行为应根据：

- Purpose；
- Materiality；
- Freshness；
- Protection；

决定。

---

## 81. Rebuild Outcome

D09逻辑 Outcome 应能区分：

- BUILT_NOT_PUBLISHED；
- PUBLISHED；
- SUPERSEDED；
- DEGRADED_PUBLISHED；
- BLOCKED；
- FAILED；
- PARTIAL；
- RETRYABLE；
- NON_RETRYABLE。

具体 enum 不冻结。

---

## 82. Job / Generation / Basis 三层分离

正式冻结：

```text
Job Success
!= Generation Currentness

Generation Exists
!= Generation Published

Generation Published
!= Generation Fresh For All Consumers
```

---

## 83. Operational Metrics 与 Governance 分离

D09可以记录：

- Duration；
- Retry Count；
- Queue Delay；
- Build Cost；
- Failure Cause。

但：

```text
Operational Metrics
!= Governance Evidence
```

除非已有 Governance Rule 明确引用。

---

## 84. Derived Generation Lifecycle

一个 Generation 可以逻辑经历：

- Building；
- Built；
- Validated；
- Published；
- Current Applicable；
- Superseded；
- Historical；
- Degraded；
- Blocked；
- Failed；
- Retained；
- Cleanup Candidate。

具体 enum 不冻结。

正式冻结：

```text
Derived Generation Lifecycle
!= Domain Subject Lifecycle
```

---

## 85. Superseded 与 Delete 分离

正式冻结：

```text
Superseded For Current
!= Eligible For Immediate Deletion
```

---

## 86. Garbage Collection

## Derived Garbage Collection
**派生垃圾清理**

只管理 Derived State。

正式冻结：

```text
Derived Garbage Collection
!= Domain Object Retirement
```

---

## 87. Cleanup Eligibility

清理前至少检查：

- Current Use；
- Historical Requirement；
- Audit Reference；
- Recovery Reference；
- Outstanding Rebuild；
- Required Lineage；
- Retention Policy；
- Protection；
- Downstream Reference；
- Outstanding Obligation。

---

## 88. Cleanup Candidate

正式冻结：

```text
Cleanup Candidate
!= Immediate Physical Deletion
```

物理删除时机 / 批次 / Storage Mechanism 不冻结。

---

## 89. Retention Policy

Retention 应：

```text
artifact-aware
purpose-aware
```

具体保存 7 / 30 / 90 天等参数不冻结。

---

## 90. TTL 与 Retention 分离

正式冻结：

```text
TTL Expired
!= Retention Expired

Not Reusable For Current
!= Must Be Deleted
```

---

## 91. Historical Generation Addressability

重要历史 Generation 必须可以通过：

- Artifact Identity；
- Generation Identity；
- Basis；
- Temporal / Revision；
- Lineage；

重新寻址。

---

## 92. Orphan Generation

## Orphan Generation
**孤立派生代次**

指没有 Current Pointer 指向的 Generation。

正式冻结：

```text
Orphan Generation
!= Invalid Generation
```

它可能继续用于 Audit / Historical / Debug / Cleanup Candidate。

---

## 93. Build Intermediate

Build Workspace / Partial Chunk / Temporary Record 与正式 Generation 分离。

```text
Build Intermediate
!= Published Generation
```

默认：

```text
Incomplete Build Workspace
must not become consumer-visible result
```

---

## 94. Ephemeral Cleanup

没有 Reference、Audit、Recovery Requirement 的 Intermediate Artifact 可确定性自动清理，不需要 Human。

---

## 95. Missing Derived Current Pointer

正式冻结：

```text
Missing Derived Current Pointer
!= Permission To Choose Latest Generation
```

不能直接选择 Latest Created / Latest Built。

---

## 96. Pointer Recovery

Derived Current Pointer Recovery 必须根据：

- Purpose；
- Scope；
- Temporal；
- Profile；
- Protection；
- Applicable Effective Basis；
- Generation Basis；
- Publication State。

无法确定时：

```text
CURRENT_POINTER_UNRESOLVED
```

---

## 97. Pointer Missing 与 Source Missing 分离

正式冻结：

```text
Derived Pointer Missing
!= Source Missing
```

Pointer 丢失通常可以重建派生状态，不自动升级为 Domain Recovery。

---

## 98. D05 Recovery Boundary

只有当：

- Required Source unavailable；
- Required Historical Basis missing；
- Locator unresolved；
- Continuation State missing；

才进入 D05。

正式冻结：

```text
Derived Pointer Recovery
!= Domain Recovery automatically
```

---

## 99. Cross-session Rebuild Recovery

D09复用 D05 Continuation State，恢复最小充分状态：

- Target Artifact；
- Current Applicable Generation；
- Pending / Building Generation；
- Rebuild Basis；
- Projection Contract；
- Trigger Cause；
- Publication State；
- Pending Retry；
- Failure；
- Next Owner Route。

---

## 100. Recovered State 与 Current State 分离

正式冻结：

```text
Recovered Rebuild State
!= Current Reconfirmed Rebuild State
```

恢复后必须重新对账当前派生状态。

---

## 101. Session Change 不触发重建

正式冻结：

```text
Session Change
!= Rebuild Trigger
```

换窗口 / 恢复 Session 不意味着重新生成所有 Projection。

---

## 102. Rebuild Completion

## Rebuild Completion
**重建完成**

至少应明确：

- Build Outcome；
- Coherence；
- Publication Outcome；
- Applicable Pointer Outcome；
- Material Failure / Unknown；
- Provenance；
- Next Freshness Action。

---

## 103. Build Complete 与 Rebuild Complete

正式冻结：

```text
Build Complete
!= Rebuild Complete
```

---

## 104. Publication Complete 与 Workflow Complete

正式冻结：

```text
Publication Complete
!= Rebuild Workflow Complete
```

发布后仍可能需要记录 Lineage、Supersession、Old Generation State 与 D06 Handoff。

---

## 105. D09 Completion 是 Target / Purpose-relative

正式冻结：

```text
D09 Completion
is target- and purpose-relative
```

不要求所有项目 Cache / Projection 全局同步重建。

---

## 106. Workflow Complete 与 Success 分离

正式冻结：

```text
Rebuild Workflow Complete
!= Rebuild Success
```

以下也可以是完整 Workflow Outcome：

- BLOCKED；
- DEGRADED；
- SUPERSEDED；
- FAILED_NON_RETRYABLE。

---

## 107. Completion 必须暴露未解决 Material State

正式冻结：

```text
Rebuild Completion
requires explicit unresolved-material-state reporting
```

不得静默隐藏：

- Unknown；
- Blocked；
- Degraded；
- Missing Material Basis；
- Publication Rejection。

---

## 108. Successful Rebuild 条件

成功重建至少要求：

- Required Inputs Satisfied；
- Coherence Satisfied；
- Build Success；
- Publish Eligibility；
- Applicable Publication Success；
- Protection Satisfied；
- Provenance Recorded。

随后：

```text
→ D06 Freshness Revalidation
```

---

## 109. D09 → D06 Handoff

至少携带：

- Artifact Identity；
- Generation Identity；
- Rebuild Basis Set；
- Projection Contract；
- Coverage；
- Build Outcome；
- Publication Outcome；
- Degraded / Missing Input；
- Protection State；
- Supersession State；
- Provenance。

---

## 110. D09 → D10 Handoff

D09向 D10提供：

- Rebuild Failure Mode；
- Fallback Generation Availability；
- Degraded Generation State；
- Blocked Cause；
- Retryability；
- Unavailable Source / Provider；
- Consumer Limitation。

但：

```text
D09 Failure Evidence
!= D10 Failure Policy
```

---

## 111. D09 不提前定义全局 Fallback

D09不自行规定：

```text
always serve stale
always fail closed
always fallback
```

Global Fallback / Degraded Policy 由 D10继续治理。

---

## 112. D09 → D12 Handoff

D09可向未来 F9-D12提供：

- Current Applicable Derived References；
- Outstanding Rebuilds；
- Blocked Artifacts；
- Degraded Projections；
- Known Fallbacks；
- Rebuild Basis / Provenance；
- Unresolved Material Maintenance State。

但：

```text
D09 Handoff
!= F10 Activation
```

---

## 113. D09 → D11 Boundary

长期无法解决的 Derived Maintenance 问题可形成：

```text
Deferred Obligation Candidate
```

但：

```text
D09 Blocked Item
!= Automatically Approved Deferred Obligation
```

正式 Deferred Governance 属于 D11 / Applicable Governance Owner。

---

## 114. GC 与 Deferred Evidence

Cleanup 前必须检查 Outstanding Obligation Reference，不能误删尚待治理的问题证据。

---

## 115. Storage Pressure Boundary

正式冻结：

```text
Storage Pressure
!= Authority To Delete Governed Retention Evidence
```

存储压力不能静默删除治理要求保留的审计 / 历史证据。

---

## 116. Protection-aware Garbage Collection

Garbage Collection 必须保持 Protection Boundary。

不得为了归档或删除把 Protected Data 复制到更低保护级别的区域。

---

## 117. Lineage Preservation

正式冻结：

```text
Cleanup
must not silently destroy required lineage
```

可以保留 Lineage Metadata 或做 History Compaction。

---

## 118. History Compaction

正式冻结：

```text
History Compaction
!= History Rewriting
```

压缩历史表示不能改写真正发生过的 Generation / Provenance。

---

## 119. Automated Cleanup 与 AI Optimization 分离

正式冻结：

```text
Automated Derived Cleanup
!= AI Autonomous Optimization
```

继续保持：

```text
AI Autonomous Optimization
= NOT_CURRENT_CAPABILITY
```

---

## 120. Storage Governance Boundary

D09管理 Derived Lifecycle。

但：

```text
Derived Lifecycle Ownership
!= Global Storage Governance Authority
```

Storage Quota、Legal Retention、Backup Policy、Archive Tier 等可由其他 Owner治理。

---

## 121. 核心不变量

```text
Cache != Canonical Truth
Projection != Canonical Truth
Derived Artifact != Canonical Source

Cache != Projection
Projection != Index

Physical Storage Similarity != Semantic Identity

Cache Key != Cache Semantic Identity
Same Query Text != Same Cache Semantics

Cache Hit != Freshness Confirmation
Cache Hit != Applicability Confirmation
Cache Hit != Runtime Authorization

Projection Contract != Implementation Schema
Projection Definition != Projection Result
Projection Definition Change != Source Change
Projection Contract Version != Domain Version

Rebuild != Canonical Mutation
Cache Repair != Source Repair
Rebuild != Re-resolution
Rebuild Complete != Freshness Satisfied
Rebuild Selection != Authority Resolution

Invalidate != Evict
Invalidate != Rebuild
Refresh != Full Rebuild

Stale For Current != Useless For History
Invalidated != Must Rebuild Immediately
Rebuild != Recovery

Partial Rebuild must respect coherence boundary
Local Rebuild Success != Whole Projection Coherence
Projection Coherence != Same Build Timestamp
Unknown Coherence != Coherent

Individually Current Inputs != Coherent Rebuild Basis Set

Partial Rebuild != Full Rebuild Success
Degraded Projection != Complete Projection

Cache Identity != Cache Generation
Projection Identity != Projection Generation
Derived Generation != Domain Revision
Derived Generation Lineage != Canonical Domain History

Rebuild Job Identity != Derived Artifact Identity
Rebuild Job Identity != Derived Generation Identity

Retry With Different Basis != Same Rebuild Attempt Semantically
Same Rebuild Target != Same Rebuild Work

Operational Rebuild Coalescing != Historical Generation Erasure

Derived Current Pointer != Canonical Effective Pointer
Latest Built Generation != Current Applicable Generation
Build Recency != Projection Applicability

Projection Chain != Authority Chain

Build Complete != Published
Build Success != Publish Eligibility

Later Job Completion != Newer Applicable Result
Last Write Wins != Rebuild Applicability Rule

Rebuild Priority != Authority Priority
Rebuild Priority != Impact Severity

Build Failure != Publication Rejection
Publication Rejected Due To Supersession != System Failure

Rebuild Failure != Mandatory Old Cache Deletion

Retained Generation != Current Applicable Generation
Publish New Generation != Retire Historical Generation

All Shards Exist != Whole Projection Ready
Publication Success != Freshness Satisfaction
Published For Consumer A != Eligible For Consumer B

Operational Metrics != Governance Evidence

Derived Generation Lifecycle != Domain Subject Lifecycle
Superseded For Current != Eligible For Immediate Deletion

Derived Garbage Collection != Domain Object Retirement
Cleanup Candidate != Immediate Physical Deletion

TTL Expired != Retention Expired
Not Reusable For Current != Must Be Deleted

Orphan Generation != Invalid Generation
Build Intermediate != Published Generation

Missing Derived Current Pointer != Permission To Choose Latest Generation
Derived Pointer Missing != Source Missing

Recovered Rebuild State != Current Reconfirmed Rebuild State
Session Change != Rebuild Trigger

Build Complete != Rebuild Complete
Publication Complete != Rebuild Workflow Complete
Rebuild Workflow Complete != Rebuild Success
Rebuild Completion != Freshness Confirmation

D09 Failure Evidence != D10 Failure Policy
D09 Handoff != F10 Activation
D09 Blocked Item != Automatically Approved Deferred Obligation

Storage Pressure != Authority To Delete Governed Retention Evidence
History Compaction != History Rewriting

Automated Derived Cleanup != AI Autonomous Optimization
```

---

## 122. Acceptance Gates

F9-D09 Architecture Freeze 只有在以下全部成立时才可 PASS：

1. Cache / Projection / Index 与 Canonical Truth 分离。
2. Derived Artifact 定位明确。
3. Cache / Projection / Index 逻辑职责分离。
4. Physical Storage 与 Semantic Contract 分离。
5. Cache Semantic Identity 不依赖裸 Key / Query Text。
6. Cache Hit 不自动等于 Fresh / Applicable / Authorized。
7. Projection Contract 与 Implementation Schema 分离。
8. Projection Definition / Result 分离。
9. Projection Definition Change 不伪装 Source Change。
10. Projection Contract Evolution 可追踪。
11. Rebuild 只消费 Authoritative / Applicable Governed Basis。
12. Rebuild 与 Re-resolution 分离。
13. Rebuild 与 Revalidation 分离。
14. Rebuild 不承担 Authority Winner Resolution。
15. Rebuild Basis / Provenance 可追踪。
16. Invalidate / Evict / Refresh / Rebuild 分离。
17. Stale Current Result 可保留 Historical Value。
18. Invalidated 不强制立即 Rebuild。
19. Rebuild Policy Purpose-aware。
20. TTL 不定义 Truth。
21. D09消费 D06 / D07 / D08 Trigger，不成为第二套 Detection Engine。
22. Missing Source 返回 D05。
23. Resolution Basis Change 返回 D03。
24. Freshness Sufficiency 返回 D06。
25. Global Impact Unknown 返回 D08。
26. Partial Rebuild 支持且受 Coherence Boundary 约束。
27. Multi-source Basis Coherence 明确。
28. Individually Current Inputs 不被误当为 Coherent Set。
29. Missing Input 按 Materiality / Contract 处理。
30. Partial / Degraded 状态显式。
31. Artifact Identity / Generation / Domain Revision 分离。
32. Generation Lineage 可追踪。
33. Rebuild Job / Generation / Artifact 分离。
34. Retry 不静默切换 Basis。
35. Semantic Dedup Basis-aware。
36. Coalescing 不删除 Historical Generation。
37. Derived Current Pointer 与 Canonical Effective Pointer 分离。
38. Latest Built 不自动成为 Current Applicable。
39. Consumer Compatibility / Protection 可限制 Generation 共享。
40. Projection Chain 不成为 Authority Chain。
41. Derived Projection 不反向升级 Authority。
42. Build 与 Publish 分离。
43. Publish Eligibility 独立存在。
44. Consumer-visible Publication 保持 Generation Coherence。
45. Atomic Publication 不绑定特定物理机制。
46. 并发旧 Job 不得覆盖更适用结果。
47. Last Write Wins 不成为派生层适用规则。
48. Rebuild Storm 有 Dedup / Coalescing / Priority / Bounded Concurrency 等架构防护。
49. Priority 与 Authority / Severity 分离。
50. Build Failure 与 Publication Rejection 分离。
51. Retry Cause-aware / Progress-aware。
52. 跨 Owner 循环 Progress-bounded。
53. Rebuild Failure 不自动删除旧 Generation。
54. 多 Generation 保留合法。
55. Current Applicable 是 Purpose / Scope / Temporal / Consumer-relative。
56. Publish New 不自动 Retire Historical。
57. Partial Publication 由 Contract 决定。
58. Publication Success 不等于 Freshness Satisfaction。
59. Publication Protection-aware。
60. Rebuild Outcome 不压缩成简单 SUCCESS / FAIL。
61. Job / Generation / Publication / Freshness 状态分离。
62. Operational Metrics 不形成 Governance Authority。
63. Derived Generation Lifecycle 与 Domain Lifecycle 分离。
64. Superseded 不自动物理删除。
65. GC 不成为 Domain Retirement。
66. Cleanup Eligibility 考虑历史、审计、恢复、血缘与 Obligation。
67. TTL 与 Retention 分离。
68. Historical Generation 可寻址。
69. Orphan 不自动 Invalid。
70. Build Intermediate 不自动 Consumer-visible。
71. Missing Pointer 不选择 Latest Generation。
72. Pointer Recovery 基于 Applicability / Basis。
73. Cross-session Recovery 复用 D05。
74. Session Change 不触发 Rebuild。
75. Build Complete / Publication Complete / Workflow Complete / Success 分离。
76. D09 Completion Target / Purpose-relative。
77. Material Unknown / Blocked / Degraded 显式。
78. Successful Rebuild 后仍返回 D06。
79. D09 → D10只提供 Failure Evidence，不提前定义 Fallback Policy。
80. D09 → D12 不提前 F10 Activation。
81. Blocked Item 不自动升级 Approved Deferred Obligation。
82. Storage Pressure 不得删除受治理 Retention Evidence。
83. GC 必须 Protection-aware。
84. History Compaction 不改写历史。
85. Automated Cleanup 不构成 AI Autonomous Optimization。
86. Global Storage Governance 不归 D09独占。
87. Implementation、RP2、Authority Cutover、Canonical Replacement、Final Activation、Legacy Retirement 仍未授权。
88. SQLite Physical Schema 仍为 `NOT_FROZEN`。

---

## 123. Final Owner Boundary

```text
Upstream Domain Owner
→ owns canonical truth /
   semantic validity /
   effective governance state

F9-D03
→ owns Scope / Profile / Query Resolution

F9-D04
→ owns Context Selection /
   Assembly /
   Context Sufficiency

F9-D05
→ owns Recovery /
   Continuation Recovery

F9-D06
→ owns Freshness Evaluation /
   Revalidation

F9-D07
→ owns Fingerprint /
   Change Detection /
   Invalidation Trigger

F9-D08
→ owns Dependency /
   Potential Impact Discovery

F9-D09
→ owns Derived Artifact Lifecycle /
   Cache /
   Projection /
   Logical Invalidation /
   Refresh /
   Rebuild /
   Publication /
   Retention /
   Derived Garbage Collection

F9-D10
→ will own Failure /
   Fallback /
   Degraded Mode policy
```

---

## 124. Architecture Closure

主链：

```text
D06 / D07 / D08 Trigger
↓
Resolve Derived Artifact
↓
Resolve Cache / Projection Semantic Identity
↓
Projection Contract
↓
Capture Rebuild Basis Set
↓
Dedup / Coalesce / Schedule
↓
Build Candidate Generation
↓
Check Projection Coherence
↓
Build Validation
↓
Publish Eligibility
↓
Atomic Publication
↓
Select Current Applicable Derived Generation
↓
D06 Freshness Revalidation
↓
Generation Lifecycle
↓
Retention / Cleanup
```

异常路由：

```text
Missing Source / Basis
→ D05

Resolution Basis changed
→ D03

Freshness unresolved
→ D06

Global Impact unclear
→ D08

Failure / Fallback / Degraded policy
→ D10

Long-lived unresolved obligation
→ D11

Stage Handoff
→ D12
```

---

## 125. Final Decision

F9-D09 最终确定：

> Banyan F9 将 Cache、Projection、Index、Context Snapshot、Dependency / Impact Projection 等统一视为 Derived State（派生状态），它们可以被刷新、重建、替换和清理，但均不成为 Canonical Truth。

> Cache Semantic Identity 必须依据真正影响结果语义的 Purpose、Scope、Profile、Temporal、Protection、Source Basis 等条件确定，而不能只依赖 Query Text 或裸 Cache Key。Cache Hit 只代表存在候选复用结果，不代表 Fresh、Applicable 或 Authorized。

> Projection 必须由 Projection Contract 定义用途、输入、输出语义、Coverage、Normalization、Protection、Input Obligation、Coherence Boundary 与 Publication Boundary。Projection Contract 与具体数据库 Schema、Go Struct 或实现代码保持分离。

> Derived Artifact 的逻辑 Identity、Generation、Rebuild Job、Domain Revision 必须分离。Derived Generation 只表示派生层生成代次，不成为 Domain Version；Generation Lineage 只记录派生历史，不成为 Canonical Domain History。

> Rebuild 必须基于 Authoritative Source 或 Applicable Governed Effective Basis。Rebuild 不重新执行 Authority Resolution，不替代 D03 Re-resolution，也不替代 D06 Freshness Revalidation。

> Multi-source Rebuild 必须保持 Rebuild Basis Set 的兼容性。多个输入“各自最新”不代表它们可以组合。Partial Rebuild 必须尊重 Projection Coherence Boundary，无法证明 Coherence 时必须扩大重建范围或显式保持 Unknown / Blocked。

> Logical Invalidate、Physical Evict、Refresh、Rebuild 必须分离。Invalidated 不自动意味着删除或立即重建；Current Stale Result 仍可合法保留为 Historical / Audit / Recovery Evidence。

> D09允许 Eager、Lazy、On-demand、Batch、Partial、Full、Degraded 等不同派生维护策略，但具体调度器、队列、Worker、Retry Count、Database Transaction 与 Physical Storage Schema 不在 F9-D09 冻结。

> Build 与 Publish 必须分离。Build Success 不自动意味着 Publish Eligible。Consumer-visible Publication 必须保持 Generation-level Coherence，并在发布前重新验证 Basis、Applicability、Protection、Supersession 与 Consumer Eligibility。

> 并发 Rebuild 不采用 Last Write Wins。旧 Job 晚完成不得覆盖更适用的新 Generation。Dedup、Coalescing、Priority 与 Rebuild Storm 防护必须 Basis-aware、Purpose-aware、Cause-aware。

> Publication Success 不等于 Freshness Satisfaction；Successful Rebuild 最终仍需 D06根据当前任务重新判断 Freshness。

> Derived Generation 的 Superseded、Historical、Orphan、Failed、Retained、Cleanup Candidate 等状态必须与 Domain Subject Lifecycle 分离。Superseded 不自动删除，TTL Expired 不等于 Retention Expired，Garbage Collection 不能成为 Domain Retirement。

> Cross-session Rebuild Recovery 复用 D05。Recovered Rebuild State 必须重新对账，Session Change 本身不构成 Rebuild Trigger。

> D09 Completion 是 Target / Purpose-relative。Build Complete、Publication Complete、Rebuild Workflow Complete 与 Rebuild Success 必须分离；Blocked / Degraded / Superseded 也可以是显式完成的 Workflow Outcome，但不得伪装成成功。

> D09向 D10提供 Failure / Fallback / Degraded Evidence，但不提前定义全局 Fallback Policy；向 D12提供 Derived Maintenance State，但不提前激活 F10；长期 Blocked Work 只能形成 Deferred Obligation Candidate，不自动成为 Approved Deferred Obligation。

> Derived Garbage Collection 必须遵守 Protection、Retention、Audit、Recovery、Lineage 与 Outstanding Obligation。Storage Pressure 不授权静默删除治理要求保留的历史证据，History Compaction 不得改写历史。

---

## 126. HUMAN_APPROVED Effect

本文件已经获得：

```text
F9-D09 HUMAN_APPROVED
```

因此：

```text
Derived Artifact Semantic Boundary
= ARCHITECTURALLY_FROZEN

Cache Semantic Identity Boundary
= ARCHITECTURALLY_FROZEN

Projection Contract Boundary
= ARCHITECTURALLY_FROZEN

Derived Generation / Lineage Boundary
= ARCHITECTURALLY_FROZEN

Rebuild Basis / Multi-source Coherence Boundary
= ARCHITECTURALLY_FROZEN

Partial / Full / Degraded Rebuild Boundary
= ARCHITECTURALLY_FROZEN

Invalidate / Evict / Refresh / Rebuild Boundary
= ARCHITECTURALLY_FROZEN

Build / Publish Boundary
= ARCHITECTURALLY_FROZEN

Publication Eligibility / Atomic Visibility Boundary
= ARCHITECTURALLY_FROZEN

Concurrency / Dedup / Coalescing Boundary
= ARCHITECTURALLY_FROZEN

Rebuild Failure / Retry Boundary
= ARCHITECTURALLY_FROZEN

Derived Lifecycle / Retention / Garbage Collection Boundary
= ARCHITECTURALLY_FROZEN

Rebuild Recovery Boundary
= ARCHITECTURALLY_FROZEN

Rebuild Completion / Handoff Boundary
= ARCHITECTURALLY_FROZEN
```

继续保持：

```text
F9 Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

`F9-D09 HUMAN_APPROVED` 只表示 Cache / Projection / Rebuild 架构语义冻结，不代表 Redis、SQLite、Queue、Worker、Scheduler、Cache Engine、Projection Engine、Rebuild Engine、Garbage Collector、Runtime、Agent 或任何实现施工获得授权。

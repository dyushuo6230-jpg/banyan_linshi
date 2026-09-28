# F9-D06 — Freshness Evidence & Revalidation

**中文名称：新鲜度证据与重新验证**

---

## 0. 文档身份

| 项目 | 内容 |
|---|---|
| Stage | F9 — Index / Projection / Cache Architecture |
| Decision | F9-D06 |
| 名称 | Freshness Evidence & Revalidation |
| 中文名称 | 新鲜度证据与重新验证 |
| 当前状态 | `HUMAN_APPROVED` |
| 精确批准语句 | `F9-D06 HUMAN_APPROVED` |
| 前置批准 | `F9-G01 HUMAN_APPROVED` |
| 前置批准 | `F9-D01 HUMAN_APPROVED` |
| 前置批准 | `F9-D02 HUMAN_APPROVED` |
| 前置批准 | `F9-D03 HUMAN_APPROVED` |
| 前置批准 | `F9-D04 HUMAN_APPROVED` |
| 前置批准 | `F9-D05 HUMAN_APPROVED` |
| Implementation | `NOT_AUTHORIZED` |
| RP2 | `NOT_AUTHORIZED` |
| Authority Cutover | `NOT_AUTHORIZED` |
| Canonical Replacement | `NOT_AUTHORIZED` |
| Final Activation | `NOT_AUTHORIZED` |
| Legacy Retirement | `NOT_AUTHORIZED` |
| SQLite Physical Schema | `NOT_FROZEN` |

本决策只冻结 Freshness（新鲜度）、Freshness Evidence（新鲜度证据）、Freshness Requirement（新鲜度要求）、Revalidation（重新验证）、Freshness Coverage（新鲜度覆盖）、Freshness Lifecycle（新鲜度生命周期）、Freshness Handoff（新鲜度交接）及相关 Owner Boundary（责任边界）的架构语义。

本决策不冻结 TTL 数值、Watcher、Polling、Git Hook、Fingerprint 算法、数据库结构、缓存实现、队列、锁、并发策略、具体 Provider、物理状态机、API 或代码实现。

---

## 1. 核心定位

D06负责回答：

> 当前 Index、Projection、Context Snapshot、Recovery Result 或其他 Derived Result，是否仍有足够证据支撑当前任务继续使用，以及何时必须重新验证。

D06不负责重新定义 Domain Truth。

正式冻结：

```text
Freshness
!= Authority

Freshness
!= Semantic Validity

Freshness
!= Current Effective Status
```

---

## 2. Freshness Evidence

## Freshness Evidence
**新鲜度证据**

用于说明：

> 当前派生对象与其 Source / Resolution Basis 是否仍具有足够一致性证据。

Freshness Evidence 可包含：

- Source / Subject Basis；
- Revision / Version；
- Effective Reference；
- Observation Basis；
- Fingerprint / Change Evidence；
- Dependency Coverage；
- Revalidation Result；
- Provenance；
- Unknown / Degraded 部分。

正式冻结：

```text
Freshness Evidence
!= Canonical Truth
```

其可以重新计算、失效、替换或重建。

---

## 3. Freshness 是对象相对、任务相对的

不得采用全局：

```text
fresh = true
```

Freshness 至少是：

```text
Subject-relative
Purpose-relative
```

同一份 Evidence 对历史分析可能足够，对 Current Runtime 判断可能不足。

正式冻结：

```text
Evidence Freshness
!= Task Freshness Sufficiency
```

---

## 4. Freshness Requirement

## Freshness Requirement
**新鲜度要求**

表示：

> 当前 Task 对某个 Material Subject 需要达到怎样的时效确认程度。

Freshness Requirement 属于：

```text
Task × Subject Usage
```

不是 Subject 永久固定属性。

形成依据可包括：

- Query Purpose；
- Subject Kind；
- Domain Role；
- Source Role；
- Temporal Intent；
- Risk；
- Governance Consequence；
- Mutation / Execution Consequence；
- Explicit User Requirement；
- Governed Policy；
- Known Change Characteristics。

---

## 5. Historical 与 Current 的 Freshness Requirement 分离

Historical / Exact Revision / As-of 查询重点是：

```text
Temporal Fidelity
```

不是“最新”。

正式冻结：

```text
Historical Freshness Requirement
!= Current Freshness Requirement
```

Current Query 关注：

```text
Current Applicable / Effective Basis
```

而不是：

```text
Latest File
```

继续保持：

```text
Current != Latest
```

---

## 6. 不冻结 Universal TTL

D06不冻结：

```text
所有对象统一 1 小时 / 24 小时过期
```

正式冻结：

```text
No universal TTL
```

时间可以成为 Revalidation Trigger，但：

```text
Age
!= Staleness

TTL Expired
!= Semantic Invalidity
```

同样：

```text
Recently Generated
!= Fresh
```

---

## 7. Freshness Requirement Set

Freshness Requirement 应支持组合约束，而不是强制统一 HIGH / MEDIUM / LOW。

逻辑上可表达：

- Temporal Requirement；
- Authority Confirmation Requirement；
- Material Dependency Requirement；
- Maximum Unverified Exposure；
- Source Availability Requirement；
- Supporting Evidence Requirement。

具体字段不冻结。

---

## 8. Freshness Evidence 能力来源

Freshness Evidence 可消费：

- Revision / Version Evidence；
- Effective Reference Evidence；
- Fingerprint / Change Evidence；
- Material Dependency Evidence；
- Observation Time；
- Explicit Invalidation Evidence；
- Source Availability Evidence；
- Recovery / Revalidation Evidence。

但任何单一信号均不得自动升级为 Truth。

---

## 9. Direct 与 Indirect Freshness Evidence

逻辑上区分：

### Direct Evidence

直接针对 Source Basis，例如：

```text
Revision unchanged
Effective Reference unchanged
Fingerprint unchanged
```

### Indirect Evidence

例如：

```text
Cache recently rebuilt
Summary recently generated
Index recently queried
```

正式冻结：

```text
Recent Derived Activity
!= Direct Source Freshness Evidence
```

并且：

```text
More Recent Observation
!= Stronger Freshness Evidence
```

---

## 10. Freshness Coverage

Freshness Evidence 必须表达自己验证到了什么。

例如：

```text
Revision ✓
Effective Status ✓
Profile ?
Protection ✓
```

不得只保存裸：

```text
fresh = true
```

正式冻结：

```text
Freshness Evidence
must expose coverage
```

---

## 11. Material Freshness Dependency

D06采用：

## Material Freshness Dependency
**实质新鲜度依赖**

即：

> 当前 Context Item / Claim 的 Freshness，真正依赖哪些上游 Material Basis。

Revalidation 优先围绕 Material Dependency 展开，不要求非 Material Historical / Supporting Evidence 全部重新验证。

---

## 12. Source Change 与 Material Change 分离

正式冻结：

```text
Source Changed
!= Material Semantic Change

Fingerprint Changed
!= Semantic Meaning Changed
```

D07负责检测变化。

D06负责判断：

> 变化是否影响当前 Freshness Requirement。

---

## 13. D06 与 D07 的核心边界

```text
D07
→ Change / Fingerprint / Invalidation Evidence

D06
→ Freshness Evaluation / Revalidation
```

正式冻结：

```text
Freshness Evaluation
!= Change Detection

D06
!= Change Detection Engine
```

---

## 14. Revalidation

## Revalidation
**重新验证**

用于重新确认：

> 某 Derived Result / Context / Projection 是否仍然可以基于当前 Source Basis 用于当前 Task。

正式冻结：

```text
Revalidation
!= Re-approval

Revalidation
!= Query Re-resolution

Revalidation
!= Physical Rebuild

Revalidation
!= Full Source Reload
```

---

## 15. Minimum Sufficient Revalidation

D06采用：

## Minimum Sufficient Revalidation
**最小充分重新验证**

逻辑上优先：

```text
Identity / Resolution Basis Check
↓
Revision / Effective Reference Check
↓
Relevant Change Evidence
↓
Material Dependency Check
↓
Material Extract Re-check
↓
Full Source Re-read
```

只有证据不足时才逐步深入。

---

## 16. Progressive Revalidation

Revalidation 应：

```text
Need-driven
Evidence-driven
Risk-aware
Materiality-aware
```

不得机械地：

```text
每次访问
→ 全部重读
→ 全量重建
```

正式冻结：

```text
Revalidation Depth
must follow material dependency
```

---

## 17. Revalidation Plan

允许逻辑：

## Revalidation Plan
**重新验证计划**

可表达：

- Target；
- Purpose；
- Freshness Requirement；
- Material Dependencies；
- Existing Evidence；
- Missing Evidence；
- Validation Order；
- Allowed Depth；
- Stop Condition；
- Protection Boundary。

但：

```text
Revalidation Plan
!= Canonical Truth
```

且：

```text
D03 Query Plan
!= D06 Revalidation Plan
```

D06不得借 Revalidation Plan 改变 Query Boundary。

---

## 18. Revalidation Trigger

Revalidation Trigger 可来自：

- 当前 Task 需要更强 Freshness；
- D07 Relevant Change Evidence；
- Material Dependency Change；
- Effective Reference Change；
- Profile / Binding Change Evidence；
- Recovery Degraded State；
- Source 恢复可访问；
- Consumer 要求 Current Confirmation；
- Existing Freshness Coverage 不足；
- Protection / Applicability Evidence Change；
- Time / Policy Trigger。

正式冻结：

```text
Trigger
!= Proven Stale
```

---

## 19. Hybrid Freshness Trigger

D06采用：

## Hybrid Freshness Trigger
**混合新鲜度触发**

支持：

```text
Change-driven
Time-driven
Task-driven
Risk-driven
Policy-driven
Recovery-driven
```

具体 Watcher / Polling / Scheduler 不冻结。

---

## 20. Freshness Evidence Reuse

已有 Freshness Evidence 可以复用，但必须检查：

- Subject；
- Scope；
- Temporal；
- Freshness Requirement；
- Protection；
- Coverage；
- Relevant Change Evidence。

正式冻结：

```text
Freshness Evidence Reuse
requires requirement compatibility

Same Subject
!= Same Freshness Coverage
```

---

## 21. Local Revalidation

若 Freshness Gap 局部且 Resolution Basis 稳定，应优先：

## Local Revalidation
**局部重新验证**

正式冻结：

```text
Local Freshness Gap
!= Full Context Revalidation
```

Local Revalidation 后必须重新评估：

- affected derived dependents；
- Freshness Coverage；
- Context Coverage；
- Snapshot Coherence。

---

## 22. Context-level Revalidation

若出现：

- 多个 Material Dependency Freshness UNKNOWN；
- Freshness Lineage 大面积不可信；
- Snapshot 新旧 Basis 混杂；
- Material Dependency 无法隔离；

则可升级：

```text
Context-level Revalidation
```

但仍不等于 D03 Re-resolution。

---

## 23. Revalidation 与 D05 Recovery 边界

若需要验证的 Material Source / Context Input：

```text
missing
evicted
locator lost
```

则进入：

```text
D05 Recovery
```

正式冻结：

```text
Freshness Revalidation
!= Context Recovery
```

逻辑链：

```text
D06
→ Recovery Needed
→ D05
→ Return to D06
```

---

## 24. Revalidation 与 D03 边界

若 Material Resolution Basis 变化：

- Project；
- Scope；
- Profile；
- Temporal；
- Protection；
- Query Purpose；
- Domain Role；

则：

```text
D03 Re-resolution
```

不能继续用旧 Revalidation Plan 修补。

---

## 25. Revalidation 与 D09 边界

D06可以判断：

```text
Derived Result stale / refresh required
```

但实际：

```text
invalidate
rebuild
cache refresh
storage update
retry
```

属于 D09。

正式冻结：

```text
Revalidation Decision
!= Physical Rebuild
```

---

## 26. D06 与 D08 边界

D06只处理：

```text
Freshness-local dependency
Context-local dependent
```

整个项目的 Dependency / Impact Discovery 由 D08负责。

正式冻结：

```text
Freshness-local Dependency
!= Global Impact Discovery
```

---

## 27. Partial Revalidation

允许：

## Partial Revalidation
**部分重新验证**

正式冻结：

```text
Partial Revalidation
!= Total Failure

Partial Freshness
!= Fully Fresh
```

Freshness Branch Failure 优先局部化。

---

## 28. Degraded Freshness

## Degraded Freshness
**降级新鲜度**

表示：

> 存在可用 Freshness Evidence，但 Current Confirmation 不完整。

正式冻结：

```text
Degraded Recovery
!= Degraded Freshness
```

以及：

```text
Source Unavailable
!= Source Changed

Cannot Revalidate
!= Proven Stale
```

---

## 29. Freshness UNKNOWN

正式冻结：

```text
Unknown Freshness
!= Fresh

Unknown Freshness
!= Stale

Freshness Unknown
!= Human Decision Required
```

UNKNOWN 只有覆盖当前 Material Freshness Obligation 时才阻塞对应 Claim。

系统应优先自动 Recovery / Re-fetch / Revalidation，再决定是否需要 Owner / Human。

---

## 30. Material Guard Freshness

Material Guard 是一等 Freshness Obligation。

例如：

```text
Implementation = NOT_AUTHORIZED
```

不得因为只关注业务内容而忽略其 Freshness / Applicability。

---

## 31. Package Freshness 不是最旧 Item 决定

正式冻结：

```text
Oldest Item
!= Package Freshness Result
```

Historical / Supporting Item 即使很旧，也不一定影响 Current Task。

反之：

```text
Material Freshness Gap
→ affects Context Readiness
```

---

## 32. Freshness Result 必须约束 Claim Strength

如果只能确认：

```text
Last Validated As Of T1
```

下游不得表述为：

```text
Current Confirmed
```

正式冻结：

```text
Freshness Result
must constrain claim strength
```

---

## 33. Freshness State 不冻结二元模型

逻辑上至少应能表达：

- Revalidated；
- Needs Revalidation；
- Stale；
- Unknown；
- Source Unavailable；
- Partially Revalidated；
- Degraded；
- Superseded Basis。

具体 enum 不冻结。

---

## 34. Revalidation Process 与 Freshness Result 分离

至少区分：

```text
Revalidation Process State

Freshness Evaluation State

Task Freshness Sufficiency
```

正式冻结：

```text
Revalidation Complete
!= Freshness Satisfied
```

---

## 35. Freshness Sufficiency 与 Context Sufficiency 分离

正式冻结：

```text
Freshness Sufficiency
!= Context Sufficiency

Freshness Ready
!= Context Ready
```

D06输出 Freshness Coverage。

D04综合 Content Coverage + Freshness Coverage 决定 Context Readiness。

---

## 36. Revalidation Stop Rule

D06采用：

## Stop When Freshness Is Sufficient
**新鲜度充分即停止**

当所有当前 Task 的 Material Freshness Obligations 已：

- Satisfied；
- Explicitly Degraded；
- Explicitly Unknown；
- Explicitly Blocked；

且没有未处理、会影响当前 Claim 的 Material Freshness Branch 时，停止继续验证。

正式冻结：

```text
Revalidation Complete
!= All Sources Rechecked

Revalidation Complete
!= Complete World Verification
```

---

## 37. Freshness Evidence Identity / Revision

Freshness Evidence 可以有独立派生 Identity / Revision，用于识别不同 Revalidation Result。

但：

```text
Freshness Evidence Identity
!= Governed Subject Identity

Freshness Evidence Revision
!= Domain Revision
```

---

## 38. Freshness Evidence Lifecycle

Freshness Evidence 具有生命周期。

正式冻结：

```text
Revalidated Once
!= Fresh Forever
```

逻辑上应能表达：

- Created；
- Applicable；
- Needs Revalidation；
- Partially Invalidated；
- Superseded；
- Degraded；
- Historical；
- No Longer Reusable。

具体 State Machine 不冻结。

---

## 39. Basis Compatibility

Freshness Evidence 复用主要依据：

```text
Basis Compatibility
```

不是：

```text
Age Alone
```

正式冻结：

```text
Freshness Reuse
depends on basis compatibility
not age alone
```

---

## 40. Freshness Evidence Supersession

新的 Revalidation Result 不因时间更晚就自动覆盖旧 Evidence。

正式冻结：

```text
Newer Revalidation Result
!= Automatic Supersession
```

只有 Applicability / Coverage 可比较且新的 Evidence 真正覆盖原 Basis 时，才能对当前 Purpose 取代旧 Evidence。

---

## 41. Freshness Evidence Expired

正式冻结：

```text
Freshness Evidence Expired
!= Evidence Proven False
```

过期通常意味着：

```text
Needs Revalidation
```

而不是：

```text
Semantically Invalid
```

---

## 42. Shared Freshness Evidence

多个 Consumer 可以共享兼容的 Freshness Evidence。

但：

```text
Shared Freshness Evidence
!= Universal Consumer Eligibility
```

同一 Evidence 可能满足 Consumer A，不满足 Consumer B。

---

## 43. Freshness Handoff

跨 Consumer / Session Handoff 应保留：

- Freshness Requirement Basis；
- Revalidation Basis；
- Freshness Coverage；
- Observation Basis；
- Unknown / Degraded；
- Claim Limitation；
- Unverified Material Dependencies；
- Relevant Change Evidence。

正式冻结：

```text
Freshness Handoff
must preserve freshness semantics
```

---

## 44. Freshness Handoff 不产生 Authority

正式冻结：

```text
Freshness Handoff
!= Authority Delegation

Freshness Handoff
!= Permission Grant
```

---

## 45. Protection-aware Freshness Reuse

Freshness Evidence 的存在不意味着所有 Consumer 都能看到。

正式冻结：

```text
Freshness Evidence Availability
!= Consumer Eligibility
```

必要时允许生成：

```text
Protection-safe Freshness Projection
```

但 Projection 不得改变 Freshness State、Coverage 或 Claim Limitation。

---

## 46. Mid-task Change

如果任务执行中出现 Material Source Change：

```text
previous freshness evidence
→ re-evaluate
```

正式冻结：

```text
Material Source Change
may invalidate previously sufficient freshness evidence
```

但：

```text
Detected Change
!= Full Freshness Invalidation
```

只重新验证受影响的 Material Dependency。

---

## 47. Coverage-scoped Invalidation

Freshness Evidence 的失效应尽量按 Coverage 局部化。

正式冻结：

```text
Freshness Evidence Invalidation
should be coverage-scoped
```

---

## 48. Freshness Snapshot

允许形成：

## Freshness Snapshot
**新鲜度快照**

用于：

- Material Revalidation；
- Context Handoff；
- Consumer Handoff；
- Recovery；
- Major Refresh；
- 高后果 Current Claim 前的确认。

Freshness Snapshot 是：

```text
Derived
Scoped
Purpose-aware
Rebuildable
```

正式冻结：

```text
Freshness Snapshot
!= Canonical Truth
```

---

## 49. Freshness Snapshot Coherence

Freshness Snapshot 必须保持 Material Coherence。

但：

```text
Freshness Coherence
!= Identical Observation Timestamp
```

不同 Source 可以在不同时间观察，只要时间差没有造成当前 Task 的 Material Ambiguity，或相关差异已显式表达。

---

## 50. Revalidation Result Cache

Revalidation Result 可以缓存复用。

但：

```text
Cached Revalidation Result
!= Eternal Freshness Truth
```

再次使用时仍检查：

- Requirement Compatibility；
- Coverage；
- Scope；
- Temporal；
- Protection；
- Relevant Change Evidence。

---

## 51. No Universal Freshness Score

D06不采用万能评分作为治理依据。

正式冻结：

```text
No universal freshness score
```

Authority、Freshness、Coverage、Protection、Conflict 必须保持多维表达。

---

## 52. Revalidation Basis

重要 Revalidation Result 必须能够说明：

- Revalidation Target；
- Freshness Requirement；
- Source / Revision Basis；
- Observation Basis；
- Evidence Used；
- Covered Dependencies；
- Unverified Dependencies；
- Result；
- Provenance；
- Claim Limitation；
- Next Trigger Basis。

正式冻结：

```text
Revalidation Basis
!= Canonical Truth
```

---

## 53. Freshness Completion

D06采用：

## Freshness Evaluation Completion
**新鲜度评估完成**

当当前 Task 的全部 Material Freshness Obligations 都已被：

```text
Satisfied
or
Explicitly Degraded
or
Explicitly Unknown
or
Explicitly Blocked
```

且无未处理 Material Freshness Branch 时：

```text
Freshness Evaluation = COMPLETE
```

但：

```text
Freshness Evaluation Complete
!= Freshness Requirement Satisfied
```

---

## 54. Freshness Failure Handling

不得冻结全局 Fail Open 或 Fail Closed。

Freshness Failure Handling 必须是：

```text
Purpose-relative
Materiality-aware
Risk-aware
Authority-aware
```

---

## 55. D06 输出给 D04

D06向 D04提供：

- Freshness Requirement Basis；
- Evaluated Material Subjects；
- Freshness Coverage；
- Revalidation Basis；
- Satisfied Obligations；
- Unknown Obligations；
- Degraded Obligations；
- Blocked Obligations；
- Claim Limitation；
- Relevant Change Evidence。

D04结合 Context Content Coverage 决定 Context Readiness。

---

## 56. D06 输出给 D05

若因 missing source、missing context、lost locator、eviction 无法继续 Revalidate：

```text
D06
→ Recovery Needed
→ D05
```

D05负责恢复可用输入。

D06负责恢复 Freshness Confidence。

---

## 57. D06 输出给 D07

当需要正式确认：

```text
what changed
which fingerprint changed
which invalidation trigger fired
```

交给 D07。

D06不得创建第二套 Change Detection。

---

## 58. D06 输出给 D08

当问题变成：

> 这个变化在整个项目 / Subject Graph 中影响谁？

交给 D08。

---

## 59. D06 输出给 D09

当确定：

```text
Derived Result stale
```

且需要物理：

```text
invalidate / rebuild / refresh
```

交给 D09。

逻辑：

```text
D06
→ stale derived result
→ D09 rebuild
→ D06 revalidation
```

---

## 60. 防止 D06 ↔ D09 无限循环

如果重复 Rebuild 仍无法解决不一致，必须判断：

```text
Derived Problem?
or
Upstream Governance Conflict?
```

正式冻结：

```text
Retry
must be cause-aware
```

若问题属于上游 Governance Conflict，停止重复 Rebuild，并路由适用 Owner / Resolver。

---

## 61. 自动化边界

F9 / AI 可以自动：

- Revision comparison；
- Fingerprint Evidence consumption；
- Effective Reference check；
- Material Dependency check；
- Local Revalidation；
- Freshness Coverage calculation；
- Partial / Degraded labeling；
- Freshness Evidence reuse compatibility check；
- Protection-safe Freshness Projection；
- bounded retry；
- Freshness Snapshot regeneration；
- Revalidation Basis generation。

F9 / AI 不得自动：

- Choose Authority Winner；
- Promote Latest to Current Effective；
- Expand Scope；
- Override Protection；
- Resolve Profile / Binding Governance Conflict；
- Upgrade Derived Evidence to Canonical Truth；
- Treat UNKNOWN as Fresh；
- Treat Source Unavailable as Changed；
- Treat Freshness Satisfied as Runtime Permission。

---

## 62. AI Autonomous Learning Boundary

Freshness Evidence / Snapshot 可以保留用于 cache、reuse、audit、recovery。

但：

```text
Freshness Evidence Retention
!= Autonomous Learning
```

当前继续保持：

```text
AI Autonomous Learning
= NOT_CURRENT_CAPABILITY
```

---

## 63. 核心不变量

```text
Freshness != Authority
Freshness != Semantic Validity
Freshness != Current Effective Status
Freshness Evidence != Canonical Truth
Evidence Freshness != Task Freshness Sufficiency
Age != Staleness
Recently Generated != Fresh
Current != Latest
More Recent Observation != Stronger Freshness Evidence
Recent Derived Activity != Direct Source Freshness Evidence
Source Changed != Material Semantic Change
Fingerprint Changed != Semantic Meaning Changed
Freshness Evaluation != Change Detection
Revalidation != Re-approval
Revalidation != Query Re-resolution
Revalidation != Physical Rebuild
Revalidation != Full Source Reload
Trigger != Proven Stale
TTL Expired != Semantic Invalidity
Same Subject != Same Freshness Coverage
Partial Freshness != Fully Fresh
Unknown Freshness != Fresh
Unknown Freshness != Stale
Freshness Unknown != Human Decision Required
Source Unavailable != Source Changed
Cannot Revalidate != Proven Stale
Revalidated Derived Evidence != Canonical Truth
Latest != Current Effective
Local Freshness Gap != Full Context Revalidation
Freshness-local Dependency != Global Impact Discovery
Partial Revalidation != Total Failure
Degraded Recovery != Degraded Freshness
Freshness Branch Failure != Global Freshness Failure
Revalidation Complete != Freshness Satisfied
Freshness Sufficiency != Context Sufficiency
Freshness Ready != Context Ready
Revalidated Once != Fresh Forever
Freshness Evidence Revision != Domain Revision
Newer Revalidation Result != Automatic Supersession
Shared Freshness Evidence != Universal Consumer Eligibility
Freshness Handoff != Authority Delegation
Freshness Handoff != Permission Grant
Detected Change != Full Freshness Invalidation
Freshness Evidence Expired != Evidence Proven False
Freshness Snapshot != Canonical Truth
Cached Revalidation Result != Eternal Freshness Truth
Freshness Evidence Retention != Autonomous Learning
Freshness Satisfied != Runtime Authorized
```

---

## 64. Acceptance Gates

F9-D06 Architecture Freeze 只有在以下全部成立时才可 PASS：

1. Freshness 与 Authority / Semantic Validity / Current Effective 分离。
2. Freshness Evidence 不成为 Canonical Truth。
3. Freshness Requirement 为 Task × Subject Usage 相对。
4. Historical 与 Current Freshness Requirement 分离。
5. 不采用 Universal TTL。
6. Age 与 Staleness 分离。
7. Direct / Indirect Freshness Evidence 可区分。
8. Freshness Evidence 暴露 Coverage。
9. Material Freshness Dependency 明确。
10. Source Change 不自动等于 Material Semantic Change。
11. D06 与 D07 Change Detection 分离。
12. Revalidation 与 Re-approval 分离。
13. Revalidation 与 D03 Re-resolution 分离。
14. Revalidation 与 D09 Rebuild 分离。
15. Revalidation 与 D05 Recovery 分离。
16. Minimum Sufficient Revalidation 成立。
17. Progressive Revalidation 成立。
18. Revalidation Plan 不改变 Query Boundary。
19. Hybrid Freshness Trigger 成立。
20. Trigger 不等于 Proven Stale。
21. Freshness Evidence Reuse 检查 Compatibility。
22. Same Subject 不等于 Same Freshness Coverage。
23. Local Revalidation 优先处理局部 Gap。
24. Partial Revalidation 不成为 Total Failure。
25. Degraded Recovery 与 Degraded Freshness 分离。
26. UNKNOWN 不被自动视为 Fresh / Stale。
27. Source Unavailable 不被自动视为 Changed。
28. Material Guard Freshness 被保护。
29. Freshness Result 约束 Claim Strength。
30. Revalidation Process / Freshness State / Task Sufficiency 分离。
31. Stop When Freshness Is Sufficient 成立。
32. Revalidation Complete 不要求 Full World Verification。
33. Freshness Evidence 具有独立生命周期但不获得 Domain Revision。
34. Basis Compatibility 优先于 Age Alone。
35. Newer Revalidation Result 不自动 Supersede。
36. Shared Freshness Evidence 保持 Consumer Eligibility。
37. Freshness Handoff 保留 Semantic Envelope。
38. Freshness Handoff 不产生 Authority / Permission。
39. Freshness Invalidation 支持 Coverage-scoped 局部失效。
40. Freshness Snapshot 不成为 Canonical Truth。
41. Freshness Snapshot 保持 Material Coherence。
42. Cached Revalidation Result 不成为 Eternal Freshness Truth。
43. 不采用 Universal Freshness Score。
44. Revalidation Basis 可解释。
45. Freshness Evaluation Complete 与 Freshness Requirement Satisfied 分离。
46. Freshness Failure Handling 为 Purpose-relative。
47. D04 / D05 / D07 / D08 / D09 Owner Boundary 明确。
48. Retry Cause-aware，不形成 D06 ↔ D09 无限循环。
49. Freshness Evidence Retention 不构成 Autonomous Learning。
50. Freshness Satisfied 不产生 Runtime Permission。
51. Implementation、RP2、Authority Cutover、Canonical Replacement、Final Activation、Legacy Retirement 仍未授权。
52. SQLite Physical Schema 仍为 `NOT_FROZEN`。

---

## 65. Final Owner Boundary

```text
Upstream Domain Owner
→ owns semantic truth /
   effective semantic status

F8
→ owns Project / Binding /
   Effective Profile semantics

F9-D03
→ owns Query Resolution /
   Search-space boundary

F9-D04
→ owns Context Selection /
   Assembly /
   Coverage /
   Context Sufficiency

F9-D05
→ owns Context Recovery /
   Continuation Recovery

F9-D06
→ owns Freshness Requirement /
   Freshness Evidence /
   Revalidation /
   Freshness Coverage /
   Freshness Handoff

F9-D07
→ owns Fingerprint /
   Change Detection /
   Invalidation Trigger Evidence

F9-D08
→ owns Global Dependency /
   Impact Discovery

F9-D09
→ owns Cache /
   Projection /
   Physical Rebuild behavior
```

---

## 66. Architecture Closure

```text
Task / Context
↓
Freshness Requirement
↓
Existing Freshness Evidence
↓
Compatibility / Coverage Check
↓
Relevant Change Evidence
↓
Need Revalidation?
↓
Progressive Revalidation
↓
Material Freshness Dependency Validation
↓
Partial / Degraded / Unknown Handling
↓
Freshness Coverage
↓
Freshness Snapshot / Reuse
↓
Consumer-safe Freshness Handoff
↓
Freshness Evaluation Completion
↓
D04 Context Sufficiency
```

必要时：

```text
Missing Input
→ D05

Resolution Basis Changed
→ D03

Need Change Evidence
→ D07

Need Global Impact
→ D08

Need Derived Rebuild
→ D09
```

---

## 67. Final Decision

F9-D06 最终确定：

> Banyan F9 将 Freshness 定位为派生信息与其 Source / Resolution Basis 在当前任务下是否仍具有足够一致性证据的问题，而不是 Truth、Authority 或 Current Effective Status 本身。

> Freshness Requirement 是 Task × Subject Usage 相对的，不采用单一永久 TTL、全局 Freshness Level 或万能 Freshness Score。Historical Query 关注 Temporal Fidelity；Current Query 关注 Current Applicable / Effective Basis，而不是最新文件。

> Freshness Evidence 必须保留 Observation Basis、Compared Basis、Coverage、Material Dependencies、Unknown / Degraded 部分与 Provenance。仅有时间戳、最近生成、缓存命中或最近查询不能单独证明 Source Freshness。

> D06采用 Minimum Sufficient Revalidation 与 Progressive Revalidation。能够通过稳定 Identity、Revision、Effective Reference、Fingerprint / Change Evidence 和 Material Dependency 确认时，不要求全文重读。

> Source Change、Fingerprint Change 只是 Revalidation Evidence，不自动等于 Material Semantic Change 或 Freshness 全局失效。D07检测变化，D06判断该变化是否影响当前 Task 的 Material Freshness Requirement。

> Revalidation 与 Re-approval、Query Re-resolution、Context Recovery、Physical Rebuild 严格分离。Material Resolution Basis 改变返回 D03；缺失恢复输入交 D05；Change Detection 交 D07；Global Impact 交 D08；Derived Rebuild 交 D09。

> Freshness 可以 Partial、Degraded、Unknown 或 Blocked。Source Unavailable 不等于 Source Changed，Cannot Revalidate 不等于 Proven Stale。UNKNOWN 只在覆盖 Material Freshness Obligation 时阻塞当前 Claim。

> Freshness Evidence 可以跨 Consumer 复用，但必须重新检查 Scope、Temporal、Requirement、Protection、Coverage 与 Relevant Change Evidence。共享 Evidence 不意味着所有 Consumer 自动具备可见性或满足相同 Freshness Requirement。

> Freshness Evidence、Revalidation Result 和 Freshness Snapshot 均为 Derived、Scoped、Rebuildable 对象，不成为 Canonical Truth，不升级 Authority，也不产生 Permission。

> Freshness Evaluation Complete 只表示当前 Material Freshness Obligations 均已明确处理，不等于所有 Requirement 已满足；Freshness Ready 不等于 Context Ready，更不等于 Runtime Authorized。

---

## 68. HUMAN_APPROVED Effect

本文件已经获得：

```text
F9-D06 HUMAN_APPROVED
```

因此：

```text
Freshness Semantic Boundary
= ARCHITECTURALLY_FROZEN

Freshness Requirement Boundary
= ARCHITECTURALLY_FROZEN

Freshness Evidence Model
= ARCHITECTURALLY_FROZEN

Material Freshness Dependency Boundary
= ARCHITECTURALLY_FROZEN

Revalidation Boundary
= ARCHITECTURALLY_FROZEN

Progressive / Minimum Revalidation Boundary
= ARCHITECTURALLY_FROZEN

Partial / Degraded / Unknown Freshness Boundary
= ARCHITECTURALLY_FROZEN

Freshness Evidence Lifecycle / Reuse Boundary
= ARCHITECTURALLY_FROZEN

Freshness Handoff Boundary
= ARCHITECTURALLY_FROZEN

Freshness Completion Boundary
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

`F9-D06 HUMAN_APPROVED` 只表示 Freshness Evidence & Revalidation 架构语义冻结，不代表任何 Watcher、Polling、Fingerprint Engine、Cache、数据库、Provider、Runtime、Agent 或代码施工获得授权。

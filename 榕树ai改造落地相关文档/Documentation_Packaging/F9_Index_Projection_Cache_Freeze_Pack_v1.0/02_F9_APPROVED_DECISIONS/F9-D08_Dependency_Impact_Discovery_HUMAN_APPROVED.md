# F9-D08 — Dependency / Impact Discovery

**中文名称：依赖与影响发现**

---

## 0. 文档身份

| 项目 | 内容 |
|---|---|
| Stage | F9 — Index / Projection / Cache Architecture |
| Decision | F9-D08 |
| 名称 | Dependency / Impact Discovery |
| 中文名称 | 依赖与影响发现 |
| 当前状态 | `HUMAN_APPROVED` |
| 精确批准语句 | `F9-D08 HUMAN_APPROVED` |
| 前置批准 | `F9-G01 HUMAN_APPROVED` |
| 前置批准 | `F9-D01 HUMAN_APPROVED` |
| 前置批准 | `F9-D02 HUMAN_APPROVED` |
| 前置批准 | `F9-D03 HUMAN_APPROVED` |
| 前置批准 | `F9-D04 HUMAN_APPROVED` |
| 前置批准 | `F9-D05 HUMAN_APPROVED` |
| 前置批准 | `F9-D06 HUMAN_APPROVED` |
| 前置批准 | `F9-D07 HUMAN_APPROVED` |
| Implementation | `NOT_AUTHORIZED` |
| RP2 | `NOT_AUTHORIZED` |
| Authority Cutover | `NOT_AUTHORIZED` |
| Canonical Replacement | `NOT_AUTHORIZED` |
| Final Activation | `NOT_AUTHORIZED` |
| Legacy Retirement | `NOT_AUTHORIZED` |
| SQLite Physical Schema | `NOT_FROZEN` |

本决策只冻结 Dependency Discovery（依赖发现）、Dependency Evidence（依赖证据）、Potential Impact Discovery（潜在影响发现）、Impact Propagation（影响传播）、Impact Classification（影响分类）、Owner Routing（责任路由）、Impact Evidence Lifecycle（影响证据生命周期）、Reconciliation（对账）及相关 Owner Boundary（责任边界）的架构语义。

本决策不冻结具体 Graph Database、Search Engine、Vector Database、Code Parser、AST Engine、Watcher、Queue、Scheduler、Storage Schema、评分算法、API、UI 或具体实现代码。

---

## 1. 核心定位

D08负责回答：

> 某个 Material Change（实质变化）发生后，哪些 Subject、Derived Result、Context、Consumer 或 Domain 可能受到影响，需要进一步验证、重建、恢复、重新解析或交给真正 Owner 处理。

D08负责：
- Dependency Discovery；
- Relation Evidence；
- Potential Impact Discovery；
- Impact Path / Lineage；
- Impact Classification；
- Bounded Propagation；
- Owner Resolution / Routing；
- Impact Coverage；
- Impact Handoff。

D08不负责：
- 决定最终 Domain Truth；
- 宣布 Domain Object 已无效；
- 决定 Semantic Winner；
- 修改 Requirement / Design / Code；
- 执行 Implementation；
- 替 Domain Owner 做最终治理决策。

正式冻结：

```text
Potential Impact != Effective Invalidity
Impact Discovery != Semantic Validation
Impact Discovery != Mutation Authorization
Impact Discovery != Implementation Authorization
```

---

## 2. Dependency 的定义

Dependency（依赖）表示：

> 一个 Subject 的语义、派生结果、适用性、验证结果或执行判断，需要另一个 Subject / Basis 的某部分才能成立。

但：

```text
Reference != Dependency
Mention != Dependency
Search Similarity != Dependency
Search Match != Governed Relation
```

---

## 3. Dependency 与 Authority 分离

```text
Dependency Direction != Authority Direction
```

---

## 4. Dependency Evidence 分层

D08支持多种 Dependency Evidence：

### Governed Relation
由正式治理合同 / 冻结条文 / Catalog 明确声明。

### Structured Deterministic Relation
由结构化字段、Binding、Profile、Source Reference、Projection Definition 等确定性推导。

### Derived Discovery Relation
由代码 Import、API Call、Symbol Reference、Config Reference、Document Reference 等发现。

### Inferred Candidate
由 AI、Semantic Search、Similarity、名称 / 内容分析产生的候选。

正式冻结：

```text
Dependency Evidence Strength != Dependency Authority
Dependency Candidate != Governed Dependency
AI Inferred Dependency != Governed Dependency
```

---

## 5. Relation Semantics

Dependency Edge 不应只有无语义的 `A → B`，而应能表达例如：

- depends-on；
- derived-from；
- implements；
- validates-against；
- configured-by；
- profiled-by；
- protected-by；
- reads-from；
- references；
- contains。

具体 Relation Type 不冻结。

```text
Relation Discovery != Relation Semantics Authority
```

正式关系语义仍来自适用 Domain Contract / Governed Relation Catalog / Adapter Contract。

---

## 6. Same Endpoints 不等于 Same Relation

```text
Same Endpoints != Same Dependency Relation
```

Relation Identity 应至少考虑 Source Subject、Target Subject、Relation Type、Scope、Temporal、Coverage、Applicability。

---

## 7. Technical / Semantic / Governance Dependency 分离

```text
Technical Dependency != Semantic Dependency
Technical Relation != Governance Relation
```

Code Import、API Call 等技术边不得自动升级为业务语义或治理依赖。

---

## 8. Explicit Structured Reference

Config、Binding、Profile、Projection Source 等明确结构化引用可以成为 Deterministic Dependency Evidence。

但：

```text
Explicit Dependency != Whole-subject Material Impact
```

仍需 Dependency Coverage 判断具体影响范围。

---

## 9. Document Link / Mention / Name Similarity

```text
Document Link != Material Dependency
Mention != Dependency
Name Similarity != Dependency
```

---

## 10. AI Dependency Candidate

AI可以辅助发现可能存在但未显式声明的 Dependency。

AI Candidate 必须保留 Candidate Source、Candidate Target、Supporting Basis、Reason、Coverage Guess、Uncertainty、Provenance。

```text
AI Inferred Dependency != Confirmed Governed Dependency
```

---

## 11. No Universal Dependency Confidence Score

不采用万能 Dependency Score 作为治理依据。应多维表达 Evidence Type、Determinism、Relation Semantics Known、Coverage、Scope、Temporal、Lineage、Unknown。

```text
No universal dependency confidence score
```

---

## 12. Dependency Coverage

Dependency Coverage 表示：

> 下游 Subject 具体依赖上游 Subject 的哪一部分。

---

## 13. Dependency Coverage Granularity

允许 Field-level、Section-level、Subject-level、Whole-source、Unknown / Broad。

```text
Dependency Coverage Granularity
must follow actual dependency semantics
```

---

## 14. Unknown / Partial Dependency Coverage

Coverage 可以逻辑表达 COMPLETE_FOR_PURPOSE、PARTIAL、UNKNOWN；具体 enum 不冻结。

```text
Coverage Unknown != No Dependency
Incomplete Dependency Coverage != No Impact
```

---

## 15. Dependency 的 Scope / Profile / Temporal

```text
Dependency Exists != Currently Applicable Dependency
Current Dependency != Historical Dependency
```

历史 Dependency 不应因为 Current State 变化而被抹掉。

---

## 16. Change Evidence 是 D08 的主要入口

D08优先消费 D07提供的 Changed Subject、Changed Coverage、Change Classification、Observation Basis、Relevant Invalidation Trigger。

```text
D08 Impact Discovery
should preserve Changed Coverage
```

---

## 17. Subject Changed 不等于所有 Dependent 都受影响

应尽量结合：

```text
Changed Coverage
×
Dependency Coverage
```

```text
Subject Changed != Every Dependent Materially Impacted
```

---

## 18. Direct / Transitive Potential Impact

至少区分 Direct Potential Impact 与 Transitive Potential Impact。

---

## 19. Transitive Reachability 不等于 Confirmed Impact

```text
Transitive Reachability != Confirmed Transitive Impact
Graph Reachability != Effective Impact
```

---

## 20. Potential Impact Set

Potential Impact Set 是 D08形成的派生结果，可包含 Candidate Subject、Relation Basis、Impact Path、Changed Coverage、Dependency Coverage、Scope、Temporal、Evidence、Uncertainty、Owner Route。

```text
Potential Impact Set != Invalid Subject Set
Potential Impact Set != Canonical Truth
```

---

## 21. Impact Path

Impact Path 用于解释某个 Subject 为什么进入 Potential Impact Set。

```text
Impact Path != Authority Chain
```

---

## 22. Impact Path Count 不代表 Severity

```text
Impact Path Count != Impact Severity
Path Count != Authority Count
```

---

## 23. No Universal Impact Score

```text
No universal impact score
```

Impact 应保持 Direct / Transitive、Governed / Derived / Candidate、Coverage、Materiality、Scope、Temporal、Uncertainty 多维表达。

---

## 24. Dependency Discovery Outcome

逻辑上应能表达 FOUND、NO_EVIDENCE_FOUND、COVERAGE_INCOMPLETE、SOURCE_UNAVAILABLE、PROTECTION_LIMITED、UNSUPPORTED、UNKNOWN。

```text
No Dependency Result != Dependency Absence
```

---

## 25. No Result 不授权 Scope Expansion

```text
No Dependency Found != Scope Expansion Authorization
```

Dependency Search Boundary 必须遵循 D03 Query Resolution。

---

## 26. Primary / Exploratory Dependency Search

允许 Primary Dependency Search 与 Exploratory Dependency Search，但：

```text
Exploratory Relation != Applicable Dependency automatically
```

---

## 27. Bounded Discovery

Exploratory Discovery 必须依据 Domain、Subject Kind、Scope、Relation Type、Changed Coverage、Current Purpose 有界扩展。

---

## 28. Discovery Priority 与 Authority 分离

可以为了效率优先 Governed、Structured、Deterministic、Derived、Search / AI Candidate。

```text
Discovery Priority != Authority Priority
```

---

## 29. Stop When Impact Boundary Is Sufficient

当 Material Relation Obligation 已覆盖、Known Gap 已显式、当前 Purpose 已满足、Remaining Unknown 非 Material 或已路由时，可以停止 Discovery。

```text
Dependency Discovery Complete != Complete World Dependency Graph
```

---

## 30. Discovery Completion 必须暴露 Coverage

应说明 Searched Domains、Searched Relation Classes、Known Gaps、Unavailable Providers、Protection Limits、Unresolved Candidate Edges。

---

## 31. Governed Relation 与 Observed Evidence 不一致

应形成 Relation Discrepancy。

```text
Observed Relation Mismatch != Governed Relation Cancellation
```

---

## 32. Derived Relation Discovery 不自动提升 Canonical

```text
Derived Relation Discovery != Canonical Relation Promotion
```

---

## 33. D08 不拥有 Relation Lifecycle Authority

```text
Relation Discovery != Relation Lifecycle Authority
```

---

## 34. Relation Provenance / Lineage

Dependency Edge 必须保留来源、Producer、Observation Time、Source / Revision、Discovery Method、Lineage。

---

## 35. Dependency Evidence Age 与 Validity 分离

```text
Dependency Evidence Age != Dependency Validity
```

关系是否仍 Fresh 由 D06语义处理。

---

## 36. D08 与 D07 边界

```text
D08 Dependency Discovery != D07 Dependency Change Detection
```

---

## 37. D08 与 D09 边界

```text
Dependency Discovery != Dependency Cache Ownership
```

缓存、保存、重建、删除属于 D09。

---

## 38. Protection-aware Dependency Discovery

Dependency / Impact Discovery 必须遵守 Protection，并允许 Protection-safe Impact Projection。

---

## 39. Protection Filter 不等于 No Dependency

```text
Protection-filtered Result != Dependency Absence
```

---

## 40. Cross-domain Discovery

```text
Cross-domain Discovery != Cross-domain Authority Arbitration
```

---

## 41. Impact Classification

Potential Impact 被发现后，应进行面向后续动作的分类，可逻辑表达 Freshness Revalidation、Resolution Re-check、Recovery、Derived Rebuild、Domain Semantic Review、Protection / Eligibility Review、Further Impact Discovery、Unknown / Blocked。

```text
Impact Classification != Domain Semantic Judgment
```

---

## 42. Impact Classification 可组合

```text
Impact Classification is composable
```

同一 Impact Candidate 可拥有多个分类。

---

## 43. Direct Impact 优先于更深扩展

```text
Direct Potential Impact
should normally be evaluated
before deeper transitive expansion
```

---

## 44. Impact Propagation Frontier

Impact Propagation Frontier 表示当前任务已经查到哪里、哪些分支待继续、哪些分支已停止。

它是 Derived、Task-scoped、Rebuildable，不是 Canonical Dependency Graph。

---

## 45. Frontier 是 Purpose-relative

```text
Impact Frontier is purpose-relative
```

---

## 46. Impact Propagation Stop

采用 Stop When Material Impact Boundary Is Sufficient。

```text
Impact Propagation Stop must be evidence-based
```

---

## 47. Cross-domain Propagation 与 Ownership 分离

```text
Cross-domain Propagation != Cross-domain Semantic Ownership
```

跨 Domain 后进入对应 Owner Handoff。

---

## 48. Owner Routing 自动化

```text
Resolvable Owner Routing should be automatic
```

符合“可靠自动路由 × 最小人工决策”。

---

## 49. Human Escalation 边界

只有 Multiple Legitimate Owners、Owner Metadata Conflict、No Deterministic Mapping、Governance Conflict、Material Ambiguity 等情况下进入 Human / Governed Resolver。

```text
AI Uncertainty Alone != Human Escalation
```

---

## 50. Changed Subject Owner 与 Impact Owner 分离

```text
Changed Subject Owner != Impacted Subject Owner
Relation Owner != Impact Resolution Owner
```

---

## 51. Owner Resolution 顺序

建议：

```text
Explicit Governed Owner
↓
Governed Subject / Domain Mapping
↓
Deterministic Adapter / Responsibility Mapping
↓
Known Responsibility Contract
↓
UNRESOLVED
```

不得以 Folder Name、Latest Editor、File Author、AI Guess 作为最终 Owner Authority。

---

## 52. Multiple Impact Owners

```text
One Change may route to multiple independent owners
Multiple Impact Owners != Authority Conflict
```

---

## 53. Different Domain Outcomes

```text
Different Domain Outcomes != Contradiction automatically
```

---

## 54. Review 与 Modification 分离

```text
Review Required != Modification Required
```

D08不能把 Candidate 自动升级为“必须修改”。

---

## 55. Impact Assessment Result

允许表达 Candidate Subject、Impact Classification、Impact Basis、Relation Basis、Changed Coverage、Dependency Coverage、Scope、Temporal、Owner Route、Current Outcome、Uncertainty、Next Action。

```text
Impact Assessment Result != Canonical Domain Truth
```

---

## 56. Potential Impact Set 可收缩

```text
Impact Set Narrowing != Discovery History Deletion
```

---

## 57. Potential Impact Set 可有界扩展

扩展必须有明确原因，例如 New Relation、Coverage Gap、Cross-domain Dependency、Current Purpose、Owner-requested Deepening。

---

## 58. Branch-local Impact State

```text
Branch Impact Failure != Global Impact Failure
```

---

## 59. Material Unknown

Unknown 的后果按 Materiality / Purpose 判断；非 Material Unknown 可不阻塞 Completion，Material Guard / Protection / Current Authority 等 Unknown 可能阻塞。

---

## 60. Impact Coverage

Impact Coverage 表示当前 Purpose 下应检查的 Material Impact Boundary 已覆盖到哪里。

```text
Impact Coverage != Domain Validation
```

---

## 61. Impact Lineage

跨 Domain Handoff 必须保留 Root Change Evidence、Changed Coverage、Impact Path、Relation Basis、每一跳 Dependency Evidence。

```text
Impact Lineage != Canonical Domain Dependency History
```

---

## 62. Owner Result Provenance

Owner 回传结果必须能说明 Candidate、Root Change、Review Basis、Revision / Scope、Resolver 来源。

---

## 63. Previous Impact Resolution 不是永久结论

```text
Previous Impact Resolution != Eternal Impact Resolution
```

---

## 64. Protection-aware Owner Routing

```text
Protection-safe Impact Projection
must preserve actionable semantics
```

---

## 65. Protected Evidence 不自动升级 Human

```text
Protected Evidence != Human Escalation Automatically
```

---

## 66. Impact Severity / Breadth / Priority 分离

```text
Impact Breadth != Impact Severity
Impact Severity != Processing Priority
```

---

## 67. Impact Discovery Completion

当前 Purpose 下，当以下条件满足时可 COMPLETE：

1. Material Root Change 已明确；
2. Required Dependency Discovery 达到充分边界；
3. Material Potential Impact 已分类；
4. 可确定 Owner 的已路由；
5. Unknown / Blocked 显式记录；
6. 无未处理 Material Frontier；
7. Coverage / Gap / Protection Limit 已显式；
8. 下游 Handoff 已形成。

```text
Impact Discovery Complete != Entire Graph Traversed
```

---

## 68. Discovery Complete 与 Resolution Complete 分离

```text
Impact Discovery Complete != Impact Resolution Complete
Impact Discovery Complete != No Impact
```

---

## 69. Impact Evidence Lifecycle

Impact Evidence / Potential Impact Set / Impact Assessment Result 均具有生命周期。

```text
Previous Impact Result != Eternal Current Impact Result
```

---

## 70. Impact Result Basis

重要 Impact Result 必须保留 Root Change Basis、Changed Coverage、Dependency Basis、Scope、Temporal、Profile / Applicability、Owner Resolution Basis、Discovery Observation Point、Provenance。

```text
Impact Result without Basis is insufficient for reuse
```

---

## 71. Impact Evidence Identity / Revision

```text
Impact Evidence Identity != Governed Subject Identity
Impact Result Revision != Domain Revision
```

---

## 72. Impact Result Reuse

复用前必须检查 Root Subject、Root Change Basis、Changed Coverage、Dependency Basis、Scope、Temporal、Profile、Protection、Impact Purpose、Later Contradictory Evidence。

```text
Impact Result Reuse requires basis compatibility
```

---

## 73. Same Subject / Same Change 不代表 Same Boundary

```text
Same Changed Subject != Same Impact Boundary
Same Change Evidence != Same Impact Discovery Purpose
```

---

## 74. Owner Resolution Reuse

```text
Owner Resolution Reuse requires review-basis compatibility
```

---

## 75. Impact Result Supersession

```text
Newer Impact Result != Automatic Supersession
```

---

## 76. Historical Impact Evidence

```text
Superseded Impact Result != Invalid Historical Evidence
```

---

## 77. Multiple Impact Result Reconciliation

多个 Result 对账前必须先验证 Identity、Scope、Temporal、Changed Coverage、Relation Coverage、Protection、Purpose。

```text
Different Impact Sets != Impact Conflict automatically
```

---

## 78. Impact Discrepancy

```text
Impact Discrepancy != Domain Conflict automatically
```

---

## 79. Impact Evidence 不采用多数票

```text
Impact Evidence Count != Impact Truth
```

---

## 80. Impact Reconciliation 顺序

```text
Identity
↓
Scope
↓
Temporal
↓
Changed Coverage
↓
Relation Basis
↓
Dependency Coverage
↓
Protection
↓
Owner / Applicability
↓
Outcome
```

---

## 81. Different Owner Outcomes

```text
Different Owner Outcomes != Conflict automatically
```

只有同一 Governed Question、同一 Authority Scope 下产生不可兼容结论，才进入真正 Conflict Resolution。

---

## 82. Impact Reconciliation 不裁决 Authority

```text
Impact Reconciliation != Authority Arbitration
```

---

## 83. Progressive Impact Resolution

Owner 回传后，D08可以逐步收敛 Derived Impact State。

```text
Progressive Impact Resolution != Domain Truth Mutation
```

---

## 84. Incremental Impact Re-evaluation

优先 Reuse Compatible Dependency Evidence + Re-evaluate Affected Branches。

```text
New Change != Full Impact Rediscovery Automatically
```

---

## 85. Incremental Boundary 的安全条件

```text
Previous Impact Miss != Future No-impact Proof
Incomplete Historical Coverage != Safe Incremental Boundary
```

---

## 86. Broader Rediscovery Trigger

以下情况应扩大 Discovery：
- Root Changed Coverage materially expanded；
- Dependency Definition changed；
- Relation Coverage unreliable；
- Scope / Profile / Temporal materially changed；
- New Domain entered；
- Protection changed；
- Previous Coverage incomplete；
- Impact Discrepancy cannot be localized。

---

## 87. Impact Frontier Lifecycle

```text
Previous Impact Frontier != Eternal Expansion Boundary
```

---

## 88. Narrower Coverage 不满足 Broader Requirement

```text
Narrower Impact Coverage
cannot silently satisfy broader impact requirement
```

---

## 89. Consumer-specific Impact Projection

允许从完整 Impact Result 生成面向 Consumer 的投影。

```text
Impact Projection != New Impact Truth
```

Consumer Projection 必须保留 Root Change、Relevant Coverage、Affected Subject、Relation Basis、Current Classification、Unknown / Blocked、Required Next Action。

---

## 90. Cross-session Recovery

D08不建立独立 Recovery Engine。

跨 Session 复用 D05，恢复最小充分 Impact State。

```text
Recovered Impact State != Current Reconfirmed Impact State
```

---

## 91. Impact Completion 的 Materiality

Impact Discovery Completion 是 Purpose-relative / Materiality-relative。

---

## 92. Impact Discovery 与 Context Ready 分离

```text
Impact Discovery Complete != Context Ready
```

---

## 93. Impact Discovery 与 Runtime Authorization 分离

```text
Impact Discovery Complete != Runtime Authorized
```

---

## 94. D08 → D06

D08向 D06提供 Affected Subject、Impact Basis、Changed Coverage、Dependency Coverage、Relation Basis、Unknown / Gap，由 D06判断 Freshness Consequence。

---

## 95. D08 → D09

若 Projection / Cache / Index 确认需要 Rebuild，D08向 D09提供 Affected Derived Set、Impact Path、Trigger Basis、Coverage、Current Task Priority Context。

D09执行物理 invalidate / rebuild / refresh。

---

## 96. Rebuild 后仍需 D06

```text
Rebuild Completion != Freshness Confirmation
```

典型链：

```text
D07
→ D08
→ D06
→ D09
→ D06
```

---

## 97. D08 与 F9-D12 / F10 边界

D08结果可以被未来 F9-D12 纳入 Stage Handoff。

```text
D08 Impact Output != F10 Activation
Impact Handoff != Implementation Plan
```

---

## 98. Deferred Obligation 边界

Unresolved Material Impact 可以成为 Deferred Obligation Candidate。

```text
Unresolved Impact != Automatically Approved Deferred Obligation
```

---

## 99. Impact Semantic Envelope

最终 Impact Handoff 应逻辑包含：

- Root Change；
- Changed Coverage；
- Discovery Purpose；
- Dependency Evidence Basis；
- Potential Impact Set；
- Impact Classification；
- Impact Coverage；
- Impact Frontier；
- Resolved Branches；
- Pending Routes；
- Unknown / Blocked；
- Protection Constraints；
- Owner Resolution Basis；
- Provenance；
- Next Owner / Next Action。

具体物理 Schema 不冻结。

---

## 100. Impact Evidence 删除 / 重建边界

```text
Impact Evidence Deletion != Dependency Deletion
Impact Projection Rebuild != Domain Relation Mutation
```

---

## 101. Autonomous Learning Boundary

Impact Results、Impact Paths、Owner Responses 可以保留用于 Audit、Recovery、Reuse、Incremental Rediscovery。

```text
Impact Evidence Retention != Autonomous Learning
AI Autonomous Learning = NOT_CURRENT_CAPABILITY
```

---

## 102. 核心不变量

```text
Reference != Dependency
Mention != Dependency
Search Similarity != Dependency
Search Match != Governed Relation
Index Edge != Canonical Dependency

Dependency Direction != Authority Direction
Dependency Candidate != Governed Dependency
AI Inferred Dependency != Governed Dependency

Dependency Exists != Currently Applicable Dependency
Current Dependency != Historical Dependency

Coverage Unknown != No Dependency
Incomplete Dependency Coverage != No Impact
No Dependency Result != Dependency Absence
No Dependency Found != Scope Expansion Authorization
Protection-filtered Result != Dependency Absence

Subject Changed != Every Dependent Materially Impacted
Transitive Reachability != Confirmed Transitive Impact
Graph Reachability != Effective Impact

Potential Impact != Effective Invalidity
Potential Impact != Confirmed Failure
Potential Impact Set != Invalid Subject Set
Potential Impact Set != Canonical Truth

Impact Path != Authority Chain
Impact Path Count != Impact Severity
Path Count != Authority Count

Impact Classification != Domain Semantic Judgment
Review Required != Modification Required

Impact Discovery != Semantic Validation
Impact Discovery != Mutation Authorization
Impact Discovery != Implementation Authorization

Cross-domain Propagation != Cross-domain Semantic Ownership
Cross-domain Discovery != Cross-domain Authority Arbitration

Changed Subject Owner != Impacted Subject Owner
Relation Owner != Impact Resolution Owner
Multiple Impact Owners != Authority Conflict
Different Domain Outcomes != Contradiction automatically

Branch Impact Failure != Global Impact Failure
Impact Coverage != Domain Validation

Impact Lineage != Canonical Domain Dependency History
Previous Impact Resolution != Eternal Impact Resolution

Different Impact Sets != Impact Conflict automatically
Impact Discrepancy != Domain Conflict automatically
Impact Evidence Count != Impact Truth
Impact Reconciliation != Authority Arbitration

Newer Impact Result != Automatic Supersession
Superseded Impact Result != Invalid Historical Evidence
Same Changed Subject != Same Impact Boundary
Same Change Evidence != Same Impact Discovery Purpose

Previous Impact Miss != Future No-impact Proof
Incomplete Historical Coverage != Safe Incremental Boundary
New Change != Full Impact Rediscovery Automatically
Previous Impact Frontier != Eternal Expansion Boundary

Impact Projection != New Impact Truth
Recovered Impact State != Current Reconfirmed Impact State

Impact Discovery Complete != Entire Graph Traversed
Impact Discovery Complete != Impact Resolution Complete
Impact Discovery Complete != No Impact
Impact Discovery Complete != Context Ready
Impact Discovery Complete != Runtime Authorized

D08 Impact Output != F10 Activation
Impact Handoff != Implementation Plan
Unresolved Impact != Automatically Approved Deferred Obligation

Impact Evidence Deletion != Dependency Deletion
Impact Projection Rebuild != Domain Relation Mutation
Impact Evidence Retention != Autonomous Learning
```

---

## 103. Acceptance Gates

F9-D08 Architecture Freeze 只有在以下全部成立时才可 PASS：

1. Reference / Mention / Similarity 与 Dependency 分离。
2. Dependency 与 Authority 分离。
3. Governed / Deterministic / Derived / Inferred Evidence 分层明确。
4. Relation Type 有语义，不使用无语义 Graph Edge 代替治理关系。
5. Same Endpoints 不自动合并不同 Relation。
6. Technical Dependency 不自动升级 Semantic / Governance Dependency。
7. AI Dependency 只形成 Candidate。
8. 不采用 Universal Dependency Confidence Score。
9. Dependency Coverage 可表达 Partial / Unknown。
10. Dependency Scope / Profile / Temporal / Applicability 可追踪。
11. D08保留 D07 Changed Coverage。
12. Subject Change 不自动影响所有 Dependent。
13. Direct / Transitive Potential Impact 分离。
14. Reachability 不自动升级 Effective Impact。
15. Potential Impact Set 是 Derived Result，不是 Invalid Set。
16. Impact Path 保留 Explainability。
17. 不采用 Universal Impact Score。
18. No Dependency Result 不自动解释为 Dependency Absence。
19. Discovery Boundary 服从 D03。
20. Primary / Exploratory Discovery 分离。
21. Discovery 有停止规则。
22. Discovery Completion 暴露 Coverage / Gap / Protection Limit。
23. Governed Relation 与 Observed Evidence 不一致时保留 Discrepancy。
24. Derived Relation 不自动写回 Canonical。
25. D08不成为 Relation Lifecycle Authority。
26. Dependency Provenance / Lineage 可追踪。
27. D07 Change Detection 与 D08 Dependency Discovery 分离。
28. D09持有 Dependency Cache / Rebuild 实现责任。
29. Protection Filter 不被解释为 No Dependency。
30. Cross-domain Discovery 不进行 Authority Arbitration。
31. Impact Classification 面向后续动作。
32. 同一 Candidate 可多分类。
33. Direct Impact 优先于深层 Transitive Expansion。
34. Impact Frontier 为 Task-relative Derived State。
35. Propagation Stop Evidence-based。
36. Cross-domain Propagation 进入 Owner Handoff。
37. Owner 可解析时自动路由。
38. AI不确定本身不触发 Human。
39. Impact 按 Impacted Subject Owner 路由。
40. Relation Owner 与 Impact Resolution Owner 分离。
41. 多 Owner 不自动形成 Authority Conflict。
42. Review Required 与 Modification Required 分离。
43. D08不产生 Implementation Authorization。
44. Impact Assessment Result 不成为 Canonical Truth。
45. Potential Impact Set 支持收缩 / 有界扩展。
46. Branch 状态局部化。
47. Material Unknown 可阻塞，非 Material Unknown 可显式保留。
48. Impact Coverage 与 Domain Validation 分离。
49. Impact Lineage 可解释。
50. Previous Impact Resolution 不成为永久结果。
51. Protection-safe Projection 保留 Actionable Semantics。
52. Impact Severity / Breadth / Processing Priority 分离。
53. Impact Discovery Completion Purpose-relative。
54. Impact Evidence 生命周期明确。
55. Impact Result 复用基于 Basis Compatibility。
56. Impact Result Supersession 不按时间自动决定。
57. Impact Result 对账先验证可比性。
58. Impact Discrepancy 不自动升级 Domain Conflict。
59. Impact Reconciliation 不裁决 Authority。
60. Incremental Impact Re-evaluation 不依赖虚假的完整 Coverage。
61. Broader Rediscovery Trigger 明确。
62. Narrower Coverage 不满足 Broader Requirement。
63. Cross-session Recovery 复用 D05。
64. Recovered Impact State 不自动当 Current Reconfirmed。
65. D08 → D06 / D09 交接边界明确。
66. Rebuild Completion 不成为 Freshness Confirmation。
67. D08不提前激活 F10。
68. Impact Handoff 不成为 Implementation Plan。
69. Unresolved Impact 不自动成为 Approved Deferred Obligation。
70. Impact Evidence 删除 / 重建不修改 Domain Relation。
71. Impact Evidence Retention 不构成 Autonomous Learning。
72. Implementation、RP2、Authority Cutover、Canonical Replacement、Final Activation、Legacy Retirement 仍未授权。
73. SQLite Physical Schema 仍为 `NOT_FROZEN`。

---

## 104. Final Owner Boundary

```text
Upstream Domain Owner
→ owns semantic truth /
   domain relation semantics /
   domain validity /
   final domain resolution

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
   Change Evidence /
   Invalidation Trigger

F9-D08
→ owns Dependency Discovery /
   Potential Impact Discovery /
   Impact Propagation /
   Impact Classification /
   Owner Routing /
   Impact Coverage

F9-D09
→ owns Cache /
   Projection /
   Physical Invalidate /
   Rebuild behavior
```

---

## 105. Architecture Closure

主链：

```text
D07 Change Evidence
↓
Changed Subject + Changed Coverage
↓
Dependency Discovery
↓
Governed / Structured / Derived / Candidate Relations
↓
Dependency Coverage
↓
Direct Potential Impact
↓
Impact Propagation Frontier
↓
Conditional Transitive Discovery
↓
Potential Impact Set
↓
Impact Classification
↓
Owner Resolution
↓
Owner Handoff
↓
Progressive Impact Resolution
↓
Impact Coverage
↓
Impact Discovery Completion
```

Source 再变化：

```text
New D07 Change Evidence
↓
Compatibility Check
↓
Incremental Impact Re-evaluation
or
Broader Rediscovery
```

跨 Session：

```text
D05 Recovery
↓
Restore Minimum Sufficient Impact State
↓
D08 Reconcile / Re-evaluate
```

必要路由：

```text
Freshness consequence → D06
Missing source/context → D05
Resolution basis changed → D03
Physical derived rebuild → D09
Deferred material obligation candidate → D11 / applicable governance owner
```

---

## 106. Final Decision

F9-D08 最终确定：

> Banyan F9 将 Dependency Discovery 定位为“发现 Subject 之间可能影响当前任务成立条件的关系”，而不是创建第二套 Canonical Dependency Truth。Reference、Mention、Similarity、Index Edge 与 Governed Dependency 必须保持分离。

> Dependency Evidence 支持 Governed、Structured Deterministic、Derived Discovery 与 AI / Semantic Candidate 多种来源，但任何 Evidence Strength 都不自动提升 Authority。AI只能产生 Candidate 与解释证据，不能把推断关系升级为治理事实。

> Dependency 必须携带 Relation Meaning、Coverage、Scope、Temporal、Applicability 与 Provenance。Dependency Coverage 应尽量精确，但其粒度服从真实关系语义；Coverage 不完整时必须显式保留 Unknown，而不是假装无依赖。

> D08优先消费 D07的 Changed Subject 与 Changed Coverage，并结合 Dependency Coverage 形成 Direct / Transitive Potential Impact。Graph Reachability 只代表可达，不代表 Effective Impact。

> Potential Impact Set、Impact Path、Impact Frontier、Impact Coverage 与 Impact Assessment Result 均为 Derived / Task-scoped / Rebuildable Evidence，不是 Invalid Subject Set、Canonical Truth 或 Domain Validation Result。

> Impact Propagation 采用 Materiality-aware、Coverage-aware、Scope-aware、Temporal-aware 的条件传播，并在 Material Impact Boundary 足够时停止，而不是无条件遍历整个 Dependency Graph。

> 跨 Domain 传播只负责发现与路由，不取得跨 Domain Semantic Ownership。可解析 Owner 应自动路由；只有真正 Owner Conflict、Governance Ambiguity 或 Material Choice 才进入 Human / Governed Resolver。

> D08严格区分 Review Required 与 Modification Required。发现潜在影响不授权修改代码、设计、需求，也不进入 Implementation。

> Impact Evidence、Owner Result 与 Potential Impact Set 均具有生命周期。复用、Supersession、Incremental Re-evaluation 必须基于 Root Change、Coverage、Scope、Temporal、Dependency Basis、Protection 与 Purpose Compatibility，而不是依赖“最新时间”或“上次结果”。

> 多个 Impact Result 不一致时先做 Identity / Scope / Temporal / Coverage / Relation / Protection 对账。Impact Discrepancy 不自动等于 Domain Conflict；D08不得使用多数票或时间顺序裁决 Authority。

> Impact Discovery Completion 只表示当前 Purpose 的 Material Impact Obligations 已经被发现、分类、路由或明确标记 Unknown / Blocked，且无未处理 Material Frontier。它不等于 Impact Resolution Complete、Context Ready、Runtime Authorized 或 Implementation Activation。

> D08的结果可以被后续 F9-D12 纳入 Stage Handoff，但不提前定义 F10，也不形成 Implementation Plan、Authority Cutover 或 Final Activation。

---

## 107. HUMAN_APPROVED Effect

本文件已经获得：

```text
F9-D08 HUMAN_APPROVED
```

因此：

```text
Dependency Semantic Boundary
= ARCHITECTURALLY_FROZEN

Dependency Evidence / Relation Model Boundary
= ARCHITECTURALLY_FROZEN

Dependency Coverage Boundary
= ARCHITECTURALLY_FROZEN

Dependency Discovery Strategy Boundary
= ARCHITECTURALLY_FROZEN

Potential Impact Model Boundary
= ARCHITECTURALLY_FROZEN

Impact Propagation / Frontier Boundary
= ARCHITECTURALLY_FROZEN

Impact Classification Boundary
= ARCHITECTURALLY_FROZEN

Cross-domain / Owner Routing Boundary
= ARCHITECTURALLY_FROZEN

Impact Evidence Lifecycle / Reuse Boundary
= ARCHITECTURALLY_FROZEN

Impact Reconciliation Boundary
= ARCHITECTURALLY_FROZEN

Impact Coverage / Completion Boundary
= ARCHITECTURALLY_FROZEN

Impact Handoff Boundary
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

`F9-D08 HUMAN_APPROVED` 只表示 Dependency / Impact Discovery 架构语义冻结，不代表 Graph Engine、Code Analyzer、Dependency Scanner、Impact Engine、Database、Provider、Runtime、Agent 或任何实现施工获得授权。

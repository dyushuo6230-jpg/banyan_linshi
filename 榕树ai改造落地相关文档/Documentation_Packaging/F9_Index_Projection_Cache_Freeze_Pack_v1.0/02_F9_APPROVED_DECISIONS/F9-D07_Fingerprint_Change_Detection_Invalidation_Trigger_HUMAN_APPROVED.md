# F9-D07 — Fingerprint / Change Detection / Invalidation Trigger

**中文名称：指纹、变化检测与失效触发**

---

## 0. 文档身份

| 项目 | 内容 |
|---|---|
| Stage | F9 — Index / Projection / Cache Architecture |
| Decision | F9-D07 |
| 名称 | Fingerprint / Change Detection / Invalidation Trigger |
| 中文名称 | 指纹、变化检测与失效触发 |
| 当前状态 | `HUMAN_APPROVED` |
| 精确批准语句 | `F9-D07 HUMAN_APPROVED` |
| 前置批准 | `F9-G01 HUMAN_APPROVED` |
| 前置批准 | `F9-D01 HUMAN_APPROVED` |
| 前置批准 | `F9-D02 HUMAN_APPROVED` |
| 前置批准 | `F9-D03 HUMAN_APPROVED` |
| 前置批准 | `F9-D04 HUMAN_APPROVED` |
| 前置批准 | `F9-D05 HUMAN_APPROVED` |
| 前置批准 | `F9-D06 HUMAN_APPROVED` |
| Implementation | `NOT_AUTHORIZED` |
| RP2 | `NOT_AUTHORIZED` |
| Authority Cutover | `NOT_AUTHORIZED` |
| Canonical Replacement | `NOT_AUTHORIZED` |
| Final Activation | `NOT_AUTHORIZED` |
| Legacy Retirement | `NOT_AUTHORIZED` |
| SQLite Physical Schema | `NOT_FROZEN` |

本决策只冻结 Fingerprint（指纹）、Change Evidence（变化证据）、Change Detection（变化检测）、Invalidation Trigger（失效触发）、Invalidation Scope（失效范围）、Propagation（传播）、Baseline（基线）、Event Ordering（事件顺序）与相关 Owner Boundary（责任边界）的架构语义。

本决策不冻结具体 Hash 算法、Watcher、Polling、Hook、数据库、消息队列、锁、调度器、Provider、物理事件存储、具体状态机、API 或代码实现。

---

## 1. 核心定位

D07负责可靠发现某个 Subject / Source / Derived Basis 相比可比较基线是否发生变化，并生成可追溯的 Change Evidence 与有界 Invalidation Trigger，供 D06、D08、D09 等后续 Owner 使用。

D07不负责判断该变化是否已经改变最终 Domain Truth。

```text
Change Detected != Semantic Meaning Changed
Fingerprint Changed != Semantic Meaning Changed
Observed Change != Effective Semantic Change
```

## 2. Fingerprint 定位

Fingerprint 是用于变化检测的可比较状态特征，可来自 File Hash、Revision ID、Version、ETag、Commit、Normalized Content、Structured Fields、Material Projection、Dependency Set 或 Provider-specific Observation。

```text
Fingerprint != Canonical Truth
Fingerprint != Only File Hash
```

## 3. Fingerprint Capability 与 Semantic Owner 分离

D07可以拥有 Fingerprint Strategy、Comparison、Change Observation、Change Evidence、Invalidation Trigger Evidence，但不获得 Requirement / Design / Product / Binding 等 Domain Authority。

```text
Fingerprint Capability Owner != Semantic Owner
```

## 4. 多层 Fingerprint

D07允许组合 Physical Fingerprint、Structural Fingerprint、Material Scoped Fingerprint、Dependency Fingerprint；不要求所有 Subject 使用一个万能指纹。

```text
One Subject may have multiple fingerprints
```

## 5. Whole-object Fingerprint

Whole-object Fingerprint 适合确认完整物理表示是否发生任何变化，但不得单独承担 Semantic Change 判断。

```text
Whole-object Fingerprint != Semantic Change Detector
```

## 6. Scoped Fingerprint

允许针对 Material Fields / Material Projection 生成局部 Fingerprint，以降低无关变化噪音，但必须显式声明 Coverage。

```text
Scoped Fingerprint must declare coverage
No Change Within Scoped Coverage != No Change Outside Coverage
```

## 7. Fingerprint Coverage

每个重要 Fingerprint 必须知道 Observed Subject、Coverage、Fingerprint Basis、Normalization Basis、Method / Provider、Observation Context 与 Provenance。

```text
Fingerprint Value without Basis is insufficient change evidence
```

## 8. Fingerprint Identity 与 Subject Identity 分离

```text
Fingerprint Identity != Governed Subject Identity
Same Fingerprint != Same Governed Identity
```

Fingerprint 不承担 Governed Identity Resolution。

## 9. Normalization

Normalization 可用于减少 whitespace、line-ending、formatting、key-order、approved non-semantic representation noise，但必须保护 Material Semantic Atoms，包括数值、阈值、MUST / MUST NOT / MAY、Scope、Temporal、Owner、Authority、Protection、Effective State、Guard。

```text
Normalization must preserve material semantic atoms
```

## 10. Normalization 必须 Subject / Domain-aware

```text
Normalization Rule must be subject/domain-aware
```

不得全局假设所有数组顺序无意义、所有空格都可忽略、所有 Metadata 都非实质。

## 11. Normalization / Algorithm Evolution

```text
Normalization Strategy Change != Source Change
Fingerprint Algorithm Change != Subject Change
Coverage Model Change != Subject Change
```

Fingerprint Definition Evolution 必须可追踪。

## 12. Fingerprint Compatibility

两个 Fingerprint 只有在 Subject Identity、Coverage、Normalization、Method / Algorithm、Observation Context、Temporal / Revision Basis 可比较时才能直接比较。

```text
Non-comparable Fingerprints != Changed
```

不兼容时进入 `NOT_COMPARABLE` 或 `Needs Rebaseline`，不得强行判断 Changed / Unchanged。

## 13. Fingerprint Baseline

Fingerprint Baseline 是后续变化比较使用的上一个可比较 Observation Reference，属于 Derived Comparison Reference，不是 Canonical Truth。

```text
Fingerprint Baseline != Canonical Truth
```

## 14. Applicable Baseline

Baseline 必须匹配 Subject、Scope、Temporal、Coverage、Comparison Purpose、Fingerprint Basis。

```text
Latest Fingerprint != Applicable Baseline
```

## 15. Baseline Advancement

Observed New State 不自动成为新 Baseline；Baseline Advancement 必须建立在可接受的 Comparison / Observation Basis 上。

```text
Observed New State != Automatically Accepted Baseline
Fingerprint Baseline Advancement != Semantic Current Promotion
```

## 16. Rebaseline

当 Fingerprint Definition、Normalizer、Coverage 或算法发生不兼容变化时，可执行 Rebaseline（重新建立指纹基线）。

```text
Rebaseline != Observed Subject Change
```

Rebaseline 应保留 Old Basis、New Basis、Reason、Observation Point、Comparability、Provenance。

## 17. Observed Change

Observed Change 表示当前可比较 Basis 与上一 Baseline 存在差异。

```text
Observed Change != Effective Semantic Change
```

## 18. Change Evidence

Change Evidence 至少应保留 Observed Subject、Previous Basis、Current Basis、Observation Method、Observation Context、Difference Type、Coverage、Provenance、Lineage、Determinism / Evidence Type。

```text
Change Evidence != Canonical Truth
```

## 19. Change Evidence Coverage

```text
No Detected Change within covered basis != Entire Subject Unchanged
```

Change Detection 的“不变”结论只能覆盖被实际观察的 Basis。

## 20. Changed / Unknown / Unavailable 分离

必须区分 `CHANGED`、`UNKNOWN`、`SOURCE_UNAVAILABLE`、`NOT_COMPARABLE`。

```text
Unknown Change State != Changed
Source Unavailable != Changed
```

## 21. First Observation

没有 Previous Baseline 时，First Observation 只建立 Baseline，不能宣称 Change Detected。

```text
First Observation != Change Detected
```

## 22. First Observed 与 Newly Created 分离

```text
First Observed != Newly Created
Not Observed != Deleted
```

## 23. Path / Locator Change

```text
Path Changed != Subject Changed
Locator Change != Subject Replacement
```

只要 Governed Subject Identity 未变，移动 / 重命名不能自动创建新 Subject。

## 24. Deletion / Retirement 分离

必须区分 Physical Deletion、Locator Removal、Access Loss、Governed Retirement、Supersession。

```text
Physical Deletion != Governed Retirement
Index Miss != Source Deletion
```

## 25. Revision / Version Change

```text
Revision Changed != Material Semantic Change
Version Changed != Effective Winner Changed
```

## 26. Effective Reference Change

D07可以可靠检测 Current Effective Ref 的变化，但不负责选择 Winner。

```text
Effective Reference Change Detection != Effective Authority Resolution
```

## 27. Dependency Fingerprint

D07支持 Dependency Fingerprint，用于检测派生结果依赖的 Material Basis 是否变化。

```text
Dependency Fingerprint != Global Dependency Graph
```

全局依赖 / 影响发现属于 D08。

## 28. Change Classification

逻辑上至少允许：No Detected Change、Physical-only Change、Structural Change、Material Change Candidate、Dependency Change、Revision Change、Version Change、Effective Reference Change、Locator Change、Protection Change、Availability Change、Unknown Difference、Incomparable Basis。具体 enum 不冻结。

## 29. Material Change Candidate

```text
Material Change Candidate != Confirmed Domain Semantic Change
```

最终业务语义是否变化仍归真正 Domain Owner / Governed Rule。

## 30. Deterministic 与 AI-assisted 分离

优先使用 Revision compare、Hash compare、ETag compare、Stable ID mapping、Effective Ref compare、Structured Field diff、Dependency-set compare 等确定性方法。

AI可辅助 Semantic Diff、Material Change Candidate、Change Explanation、Candidate Classification，但：

```text
AI Semantic Diff != Domain Semantic Resolution
AI confidence != Deterministic Fingerprint
```

## 31. AI Semantic Diff 不得擦除已确认物理变化

如果 Physical Change 已确认，而 AI 判断“语义大概率未变”，两类证据都必须保留。

```text
Semantic Diff Assessment must not erase observed physical change
```

## 32. False Positive / False Negative

D07必须同时治理误报和漏报。误报会导致不必要 Revalidation / Rebuild；漏报可能导致旧 Context 被错误复用。

```text
False-positive / false-negative tolerance must be materiality-aware and risk-aware
```

不采用全局统一“宁可错杀”或“宁可漏掉”。

## 33. 高后果变化需要更强 Coverage

Material Guard、Authority、Protection、Scope、Effective State 等需要更强检测覆盖。

```text
Material Guard / Authority / Protection change detection requires stronger coverage
```

## 34. Metadata Change

重要 Subject 的 Change Basis 可以包括 Content、Identity Metadata、Scope、Authority、Protection、Effective Status、Dependency Basis。

```text
Metadata Change != Automatically Material Change
```

Materiality 应由适用 Domain / Subject Rule 决定。

## 35. Multi-provider Evidence

不同 Provider 可能观察不同层：Git 观察 Source Revision，Filesystem 观察物理表示，Index 观察派生投影，Cache 观察缓存结果。

```text
Provider Disagreement != Change Conflict automatically
Cross-layer Difference != Observation Conflict
```

只有可比较的同层 Basis 不一致时才形成真正 Observation Discrepancy。

## 36. Provider Count 不决定 Truth

```text
Provider Count != Change Truth
Evidence Count != Authority Count
```

多条派生 Evidence 可能来源于同一 Observation。

## 37. Change Evidence Lineage

重复 Evidence 必须保留 Lineage。

```text
Repeated Change Evidence != Independent Change Evidence
```

## 38. No Universal Change Confidence Score

D07不采用统一 `Change Confidence = 87%` 作为治理依据，而应分别表达 Determinism、Coverage、Comparability、Evidence Type、Unknown、Lineage。

```text
No universal change confidence score
```

## 39. Invalidation Trigger

Invalidation Trigger（失效触发信号）表示某个 Observed Change 使相关 Derived Result 需要重新评估是否仍可直接复用。

```text
Invalidation Trigger != Semantic Invalidity
Invalidation Trigger != Immediate Physical Deletion
```

## 40. Invalidation 的语义

D07中的 Invalidation 主要指 Derived Usability Invalidation（派生可用性失效）：direct reuse no longer guaranteed。

```text
Invalidated For Reuse != Semantically False
```

## 41. Derived Invalidation 与 Domain Invalidation 分离

```text
Derived Invalidation != Domain Semantic Invalidation
```

D07只能触发 / 标识 Index、Projection、Cache、Context Snapshot、Derived Summary、Consumer Projection 重新评估，不得宣布上游 Domain Subject 无效。

## 42. Invalidation Scope

Invalidation Scope 至少应考虑 Changed Subject、Changed Coverage、Material Dependency、Scope、Temporal、Profile、Consumer、Projection Type、Protection、Effective Reference。

## 43. Minimum Necessary Invalidation

D07采用 Minimum Necessary Invalidation（最小必要失效）。

```text
Invalidate Only Affected Derived Boundary
```

不采用 `Invalidate Everything Downstream By Default`。

## 44. Dependency Coverage 不完整

```text
Incomplete Dependency Coverage != No Dependency
Incomplete Dependency Coverage != Complete Impact Boundary
```

Coverage 不完整时不得得出“零影响”结论。

## 45. Parent / Child Propagation

```text
Parent Container Changed != Every Child Materially Changed
Child Change != Parent Projection Invalid
```

具体影响必须看 Material Dependency / Coverage。

## 46. Conditional Propagation

D07采用 Conditional Propagation（条件传播）：

```text
Upstream Change
↓
Direct Material Dependent enters evaluation
↓
Material Basis changed?
    No → may stop
    Yes → propagate further
```

不做无条件 Transitive Invalidation。

## 47. Propagation Stop Condition

传播停止必须 Evidence-based，可基于 Material Projection unchanged、Dependency Basis equivalent、Affected Coverage no longer propagates、Consumer Projection unaffected、Historical branch outside current scope。

```text
Propagation Stop must be evidence-based
```

## 48. Propagation Direction 与 Authority 分离

```text
Invalidation Propagation Direction != Authority Direction
```

变化传播沿 Dependency / Derivation 方向，不代表 Authority 高低。

## 49. Graph Descendant 不等于受影响对象

```text
Graph Descendant != Materially Affected Dependent
```

只有明确 Material Dependency / Impact Evidence 才能确认受影响。

## 50. Derived Edge 与 Governed Relation 分离

```text
Index Edge != Canonical Dependency
```

Derived Discovery Edge 只能形成 Potential Impact Candidate，不能自动升级为 Confirmed Dependency。

## 51. Invalidation Candidate 与 Confirmed Stale 分离

```text
Invalidation Candidate != Confirmed Derived Stale
```

D07识别候选影响；D06判断 Freshness Consequence。

## 52. Action Hint

Invalidation Trigger 可附带 Revalidate、Rebuild、Recover、Impact Discovery、Re-resolution、Owner Review 等 Action Hint。

```text
Action Hint != Action Authority
```

## 53. Change-to-Action Routing

核心路由：

```text
Observed Change
↓
Affected Derived Candidate
↓
Can deterministically classify?
    Yes → applicable action
    No  → D06 Revalidation
```

必要时：

```text
Missing Context → D05
Resolution Basis Changed → D03
Need Global Impact → D08
Need Derived Rebuild → D09
Governance Ambiguity → Applicable Owner / Resolver
```

## 54. D07 不成为 Global Orchestrator Authority

```text
Change Routing != Governance Ownership
```

D07只按已冻结责任边界路由。

## 55. Scope / Temporal-aware Invalidation

```text
Scope A Change != Scope B Invalidation
Current Change != Historical Snapshot Invalidity
```

Exact Revision / Historical Context 不应因 Current Effective 变化自动失效。

## 56. Current Effective Change 的传播

当 Current Effective Reference 变化时：依赖 Current Effective 的 Derived Result 进入重新评估；依赖 Exact Revision / Historical 状态的 Derived Result 不自动失效。Temporal Intent 必须参与传播判断。

## 57. Protection Change

即使 Content 不变，Protection Change 也可使 Consumer Projection、Search Projection、Context Package、Cached Visibility Result 需要重新评估。

```text
Protection Change can invalidate consumer-visible projections
```

## 58. Applicability / Authority Metadata Change

```text
Content Unchanged != Derived Applicability Unchanged
```

Scope、Profile、Authority、Binding、Protection 等变化都可能影响 Derived Applicability。

## 59. Scope / Profile Material Change

Material Resolution Basis 变化必须路由 D03 Re-resolution；D07不得自己 Patch 旧 Context。

## 60. Local Freshness 与 Global Impact 分离

```text
Local Freshness Question != Global Impact Question
```

局部 Freshness → D06；项目级 / 跨 Domain Impact → D08。

## 61. Logical Invalidation 与 Physical Eviction 分离

```text
Logical Invalidation != Physical Eviction
```

旧 Derived Result 可以因 Audit、Historical、Recovery、Debugging 而继续保留。

## 62. Invalidation 与 Rebuild 分离

```text
Invalidated != Must Rebuild Immediately
```

Eager / Lazy / On-demand / Batch Rebuild 属于 D09 / Implementation。

## 63. Invalidation Storm 防护原则

为了避免全系统失效风暴，D07冻结：Coverage-scoped Invalidation、Branch-local Propagation、Evidence-based Stop、Trigger Deduplication、Cause-aware Retry、Materiality-aware Propagation。具体队列 / 调度算法不冻结。

## 64. Trigger Deduplication

重复 Trigger 可去重，但必须保留 Subject、Cause、Coverage、Previous / Current Basis、Lineage。

```text
Same Subject != Same Invalidation Cause
```

## 65. Operational Coalescing

短时间连续变化 `R5 → R6 → R7` 允许 Current Operational Work 合并处理，但：

```text
Operational Coalescing != Historical Evidence Deletion
```

Historical Change Chain 必须保留。

## 66. Rebuild During New Change

若 Rebuild 基于 R5 进行时 Source 已变化到 R6，则：

```text
Rebuild Completion != Currentness Confirmation
```

重建后必须回 D06 验证 Freshness / Currentness。

## 67. Change Evidence Lifecycle

```text
Change Evidence has lifecycle
Previously Current Change Evidence != Eternally Current Evidence
```

旧 Evidence 可继续用于历史 / 审计，但不自动代表 Current Change State。

## 68. Change Evidence Identity / Revision

```text
Change Evidence Identity != Governed Subject Identity
Change Evidence Revision != Domain Revision
```

## 69. Multiple Baselines

同一 Subject 可以同时维护 Physical Baseline、Material Baseline、Dependency Baseline、Provider-specific Baseline，不要求单一 Universal Baseline。

## 70. Historical Change Chain

连续变化应保留 `R5 → R6`、`R6 → R7` 作为 Historical Change Evidence。

```text
Historical Change Chain != Operational Rebuild Sequence
```

## 71. Event Deduplication

同一个 Root Change 被多个 Provider 观察时可去重，但：

```text
Same Subject + Same Time != Same Change Cause
```

Content Change、Protection Change 等不同 Cause 不得误合并。

## 72. Event Ordering

```text
Event Arrival Order != Source Evolution Order
Later Received Event != Later Source State
```

事件顺序应优先依据 Revision、Version、Commit Ancestry、Source Sequence、Governed Evolution Evidence。无法可靠排序时保持 `ORDER_UNKNOWN`，不得猜测。

## 73. Late Event 与 Actual Rollback

必须区分 Late Observation 与 Actual Source Rollback。

```text
Lower Revision Observation != Automatic Late Event
```

Rollback 需要正式 Source Evolution Evidence。

## 74. Event Sequence 与 Authority 分离

```text
Event Sequence != Authority Priority
```

版本晚不代表 Governance Authority 更高。

## 75. Observation Gap

允许表达 Observation Gap（观测缺口）。例如系统知道 R5，下一次只观察到 R8，而 R6 / R7 未被观察。

```text
Observed Transition != Complete Evolution History
```

Gap 的影响按当前 Detection Purpose 判断。

## 76. Change Evidence Supersession

```text
Newer Change Evidence != Automatic Supersession
```

Supersession 需要比较 Subject、Basis、Coverage、Cause、Layer、Temporal、Applicability。

## 77. Change Evidence Reuse

旧 Evidence 只有在 Subject、Basis、Coverage、Temporal、Protection、No later contradictory observation 等兼容时才能复用。

```text
Change Evidence Reuse requires basis compatibility
```

## 78. Cross-session Recovery

D07不另建 Recovery Engine。跨 Session Change Evidence 恢复使用 D05 的 Recovery Anchor、Continuation State、Evidence Reference。

```text
Change Evidence Recovery uses D05 recovery semantics
```

## 79. Handoff 使用 Minimum Sufficient Change Context

换 Session / Consumer 时，不需要复制全部 Change History。只需按当前 Purpose 保留 Current Applicable Baseline、Recent Material Change Evidence、Outstanding Invalidation、Ordering / Gap State、Unresolved Unknown、Historical Evidence References。

## 80. Change Detection Completion

Change Detection Completion（变化检测完成）表示当前 Detection Purpose 所要求的 Material Observation Obligations 已得到明确处理。

```text
Change Detection Complete != Full Repository Scan
```

## 81. Detection Completion Coverage

Completion 必须表达 Observed、Changed、No Detected Change Within Coverage、Unknown、Unavailable、Not Comparable、Observation Gap，不能只输出 `done = true`。

## 82. Detection Complete 与结果分离

```text
Change Detection Complete != No Change
Change Detection Complete != Downstream Remediation Complete
```

## 83. D07 Final Output

D07逻辑输出至少应能表达 Detection Target、Comparison Basis、Fingerprint Basis、Coverage、Previous Observation、Current Observation、Change Classification、Change Evidence、Invalidation Candidate / Trigger、Ordering State、Observation Gap、Unknown / Unavailable、Protection-safe Explanation、Recommended Owner Route。具体 Schema 不冻结。

## 84. D07 → D06

D07向 D06提供 Relevant Change Evidence、Changed Freshness Basis、Coverage、Change Type、Observation Gap / Unknown、Invalidation Trigger。D06判断当前 Freshness Requirement 是否仍满足。

```text
D07 detects
D06 evaluates freshness consequence
```

## 85. D07 → D08

需要 Project-wide / Cross-domain Impact 时，D07向 D08提供 Changed Subject、Changed Coverage、Known Relations、Potential Affected Boundary、Change Evidence。

```text
D07 Change Evidence != D08 Impact Result
```

## 86. D07 → D09

当 Derived Result 已确定需要重建时，D07提供 Trigger Basis、Affected Derived Reference、Change Coverage、Previous / Current Basis，D09执行 invalidate / rebuild / refresh。

## 87. D09 完成后返回 D06

正式链路：

```text
D07 → D06 → D09 → D06
```

不得视为：

```text
D09 Rebuild Success → Automatically Fresh
```

## 88. Invalidation Evidence

Invalidation Evidence（失效证据）用于说明 What changed、Why affected、Which dependency、Which coverage、Which action、What remained unaffected。

```text
Invalidation Evidence != Canonical Truth
```

## 89. Invalidation Outcome

逻辑上至少允许 Unaffected、Needs Revalidation、Partially Affected、Stale For Current Use、Rebuild Required、Recovery Required、Re-resolution Required、Impact Discovery Required、Unknown。具体 enum 不冻结。

```text
Unknown Impact != No Impact
```

## 90. Protection-aware Change / Invalidation Evidence

Change Evidence、Invalidation Trigger、Explanation 都必须遵守 Protection。必要时 Consumer 只能得到 `Material revalidation required`，而不能知道受保护 Source 的存在或细节。

## 91. Provider Extensibility

D07未来可以支持 Git、Filesystem、Database、API、Object Storage、Graph、Search Index、External Provider。

```text
Provider Change != Semantic Change
Logical Change Contract != Physical Watcher Implementation
```

## 92. Observed Change History

D07可以长期保留 Fingerprint、Baseline、Change Evidence、Event History，但：

```text
Observed Change History != Canonical Domain History
```

若两者冲突，应保留 Discrepancy，并路由适用 Owner。

## 93. Missing Baseline

```text
Missing Baseline != Permission To Invent Previous State
```

优先通过 D05恢复兼容 Baseline。无法恢复时可以 Rebaseline，但必须显式记录：

```text
Historical Comparison Continuity = INCOMPLETE
```

## 94. Autonomous Learning Boundary

Fingerprint / Change Evidence / History 的保留用于 Detection、Audit、Recovery、Revalidation、Impact Analysis。

```text
Change Evidence Retention != Autonomous Learning
AI Autonomous Learning = NOT_CURRENT_CAPABILITY
```

## 95. Runtime Permission Boundary

```text
Change Detection Complete != Runtime Authorized
```

D07完成变化检测不赋予 Mutation Permission、Deployment Permission、Cutover Permission、Implementation Authorization。

## 96. 核心不变量

```text
Fingerprint != Truth
Fingerprint Changed != Semantic Meaning Changed
Small Physical Change != Small Semantic Change
Fingerprint Identity != Governed Subject Identity
Same Fingerprint != Same Governed Identity
Observed Change != Effective Semantic Change
Change Evidence != Canonical Truth
Source Unavailable != Changed
Path Changed != Subject Changed
Revision Changed != Material Semantic Change
Version Changed != Effective Winner Changed
Effective Reference Change Detection != Effective Authority Resolution
Dependency Fingerprint != Global Dependency Graph
Material Change Candidate != Confirmed Domain Semantic Change
AI Semantic Diff != Domain Semantic Resolution
Provider Count != Change Truth
Repeated Change Evidence != Independent Change Evidence
Invalidation Trigger != Semantic Invalidity
Invalidated For Reuse != Semantically False
Derived Invalidation != Domain Semantic Invalidation
Observed Change != Global Invalidation
Incomplete Dependency Coverage != No Dependency
Propagation Direction != Authority Direction
Parent Container Changed != Every Child Materially Changed
Child Change != Parent Projection Invalid
Invalidation Candidate != Confirmed Derived Stale
Action Hint != Action Authority
Scope A Change != Scope B Invalidation
Current Change != Historical Snapshot Invalidity
Graph Descendant != Materially Affected Dependent
Index Edge != Canonical Dependency
Logical Invalidation != Physical Eviction
Invalidated != Must Rebuild Immediately
Operational Coalescing != Historical Evidence Deletion
Rebuild Completion != Currentness Confirmation
Event Arrival Order != Source Evolution Order
Later Received Event != Later Source State
Event Sequence != Authority Priority
Observed Transition != Complete Evolution History
Newer Change Evidence != Automatic Supersession
Change Detection Complete != Full Repository Scan
Change Detection Complete != No Change
Change Detection Complete != Downstream Remediation Complete
Observed Change History != Canonical Domain History
Missing Baseline != Permission To Invent Previous State
First Observation != Change Detected
First Observed != Newly Created
Not Observed != Deleted
Change Detection Complete != Runtime Authorized
```

## 97. Acceptance Gates

F9-D07 Architecture Freeze 只有在以下全部成立时才可 PASS：

1. Fingerprint 与 Canonical Truth 分离。
2. Fingerprint Change 与 Semantic Change 分离。
3. 多层 Fingerprint 能力成立。
4. Fingerprint Coverage 明确。
5. Scoped Fingerprint 不产生 Coverage 外“不变”结论。
6. Normalization 保护 Material Semantic Atoms。
7. Fingerprint Definition / Algorithm / Coverage Evolution 可追踪。
8. Non-comparable Fingerprint 不强行判 Changed。
9. Baseline 是 Derived Reference，不是 Canonical Truth。
10. Latest Fingerprint 不自动成为 Applicable Baseline。
11. Baseline Advancement 不提升 Semantic Current。
12. Rebaseline 与 Source Change 分离。
13. Change Evidence 保留 Basis / Coverage / Provenance / Lineage。
14. Changed / Unknown / Unavailable / Not Comparable 分离。
15. First Observation 不被当成 Change。
16. First Observed 不被当成 Newly Created。
17. Path Change 不改变 Governed Identity。
18. Physical Deletion 与 Governed Retirement 分离。
19. Revision / Version Change 不自动确认 Material Change。
20. Effective Reference Change 不产生 Authority Resolution。
21. Dependency Fingerprint 不吞并 D08。
22. Change Classification 支持多维语义。
23. Material Change Candidate 不成为 Domain Semantic Truth。
24. Deterministic Detection 优先。
25. AI-assisted Diff 不获得 Semantic Authority。
26. False Positive / False Negative Control 风险感知。
27. Material Guard / Authority / Protection 具备更强 Coverage。
28. Multi-provider Evidence 先做 Basis / Layer 对账。
29. Provider Count 不形成多数票 Truth。
30. Repeated Evidence 通过 Lineage 去重。
31. 不采用 Universal Change Confidence Score。
32. Invalidation Trigger 与 Semantic Invalidity 分离。
33. Derived Invalidation 与 Domain Invalidation 分离。
34. Minimum Necessary Invalidation 成立。
35. Dependency Coverage 不完整时不宣称零影响。
36. Conditional Propagation 成立。
37. Propagation Stop Evidence-based。
38. Branch-local Invalidation 优先。
39. Graph Descendant 不自动成为受影响对象。
40. Derived Edge 只产生 Potential Impact Candidate。
41. D07 / D06 / D08 / D09 Owner Boundary 清楚。
42. Logical Invalidation 与 Physical Eviction 分离。
43. Invalidated 与 Immediate Rebuild 分离。
44. Invalidation Storm 具备架构级防护原则。
45. Trigger Dedup 保留 Cause / Coverage / Lineage。
46. Operational Coalescing 不删除 Historical Evidence。
47. Mid-rebuild Change 可重新验证 Basis。
48. Change Evidence Lifecycle 明确。
49. Event Arrival Order 与 Source Evolution Order 分离。
50. Late Event 与 Actual Rollback 可区分。
51. Observation Gap 可以显式表达。
52. Change Evidence Supersession 不按时间自动决定。
53. Cross-session Recovery 复用 D05。
54. Change Detection Completion Purpose-relative。
55. Detection Completion 具有 Coverage。
56. Detection Complete 与 No Change 分离。
57. Detection Complete 与 Remediation Complete 分离。
58. Observed Change History 不替代 Canonical Domain History。
59. Missing Baseline 不允许发明历史状态。
60. Change Evidence Retention 不构成 Autonomous Learning。
61. Change Detection Complete 不产生 Runtime Permission。
62. Implementation、RP2、Authority Cutover、Canonical Replacement、Final Activation、Legacy Retirement 仍未授权。
63. SQLite Physical Schema 仍为 `NOT_FROZEN`。

## 98. Final Owner Boundary

```text
Upstream Domain Owner
→ owns semantic truth /
   domain validity /
   effective governance state

F9-D03
→ owns Query Resolution /
   Resolution Basis

F9-D04
→ owns Context Assembly /
   Context Sufficiency

F9-D05
→ owns Context Recovery

F9-D06
→ owns Freshness Evaluation /
   Revalidation

F9-D07
→ owns Fingerprint /
   Change Observation /
   Change Evidence /
   Invalidation Trigger /
   Bounded Propagation Evidence

F9-D08
→ owns Global Dependency /
   Potential Impact Discovery

F9-D09
→ owns Physical Cache /
   Projection /
   Invalidate / Rebuild behavior
```

## 99. Architecture Closure

完整链路：

```text
Observed Subject
↓
Fingerprint Definition
↓
Normalization / Coverage
↓
Compatible Baseline
↓
Fingerprint Comparison
↓
Change Evidence
↓
Change Classification
↓
Invalidation Scope
↓
Affected Derived Candidate
↓
Conditional Propagation
↓
Propagation Stop / Continue
↓
Action Routing
```

必要时：

```text
Freshness consequence → D06
Missing context → D05
Resolution basis changed → D03
Global impact → D08
Derived rebuild → D09
Governance ambiguity → Applicable Owner / Resolver
```

生命周期：

```text
Baseline
↓
Observation
↓
Change Evidence
↓
Baseline Advancement / Rebaseline
↓
Historical Evidence Preservation
↓
Next Observation
```

## 100. Final Decision

F9-D07 最终确定：

> Banyan F9 将 Fingerprint 定位为变化检测工具，而不是 Truth、Identity 或 Authority。Fingerprint Changed 只证明可比较 Basis 出现差异，不自动证明 Domain Semantic Meaning 已变化。

> Fingerprint 必须保留 Basis、Coverage、Normalization、Method 与 Provenance。D07支持 Physical、Structural、Material Scoped 与 Dependency 等多层 Fingerprint，不采用单一万能 Hash。

> Fingerprint Comparison 只有在 Basis 可比较时才有效。Algorithm、Normalizer、Coverage 或 Fingerprint Definition 变化必须能够 Rebaseline，而不得伪装成 Source Change。

> Change Evidence 是 Derived Evidence，必须保留 Previous / Current Basis、Observation Context、Coverage、Lineage 与 Evidence Type。Changed、Unknown、Unavailable、Not Comparable 必须分离。

> D07允许检测 Physical、Structural、Material Candidate、Dependency、Effective Reference、Protection 等变化，但 Material Change Candidate 不成为 Confirmed Domain Semantic Change。AI 可以辅助解释差异，但不得成为 Domain Semantic Resolution Authority。

> D07中的 Invalidation 表示 Derived Result 不再保证可直接复用，而不是 Domain Truth 被判无效。采用 Minimum Necessary Invalidation、Coverage-scoped、Branch-local、Conditional Propagation 与 Evidence-based Stop，避免局部变化造成全系统失效风暴。

> Invalidation Trigger 与实际 Physical Eviction、Rebuild、Recovery、Re-resolution 分离。Freshness 交 D06，Missing Context 交 D05，Resolution Basis Change 交 D03，Global Impact 交 D08，Derived Rebuild 交 D09。

> Change Event 可以去重、合并 Current Operational Work，但必须保存 Historical Change Evidence。Event Arrival Order 不等于 Source Evolution Order，Late Event、Actual Rollback 与 Observation Gap 必须保持语义分离。

> Change Detection Completion 是 Purpose-relative、Coverage-aware 的检测完成，不等于全仓扫描、无变化、下游修复完成或 Runtime Authorized。

> Fingerprint Baseline、Change Evidence、Observed Change History 均属于 Derived / Rebuildable / Audit Evidence，不成为 Canonical Domain History，也不构成 AI Autonomous Learning。

## 101. HUMAN_APPROVED Effect

本文件已经获得：

```text
F9-D07 HUMAN_APPROVED
```

因此：

```text
Fingerprint Semantic Boundary
= ARCHITECTURALLY_FROZEN

Fingerprint Basis / Coverage Boundary
= ARCHITECTURALLY_FROZEN

Normalization / Compatibility Boundary
= ARCHITECTURALLY_FROZEN

Change Evidence Boundary
= ARCHITECTURALLY_FROZEN

Change Classification Boundary
= ARCHITECTURALLY_FROZEN

Invalidation Trigger Boundary
= ARCHITECTURALLY_FROZEN

Invalidation Scope / Propagation Boundary
= ARCHITECTURALLY_FROZEN

Baseline / Rebaseline Boundary
= ARCHITECTURALLY_FROZEN

Event Ordering / Observation Gap Boundary
= ARCHITECTURALLY_FROZEN

Change Detection Completion / Handoff Boundary
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

`F9-D07 HUMAN_APPROVED` 只表示 Fingerprint / Change Detection / Invalidation Trigger 架构语义冻结，不代表任何 Watcher、Hash Engine、Event Bus、Cache Invalidation Engine、Database、Provider、Runtime、Agent 或代码施工获得授权。

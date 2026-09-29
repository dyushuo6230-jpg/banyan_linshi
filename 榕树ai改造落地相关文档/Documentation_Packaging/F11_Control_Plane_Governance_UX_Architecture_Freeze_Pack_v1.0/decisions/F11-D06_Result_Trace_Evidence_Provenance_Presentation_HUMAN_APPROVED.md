# F11-D06 — Result / Trace / Evidence / Provenance Presentation
## 结果、追踪、证据与来源呈现

**Stage：** F11 — Control Plane / Governance UX Architecture（控制面 / 治理交互架构）  
**Decision ID：** F11-D06  
**Status：** HUMAN_APPROVED / FROZEN  
**Approval：** `F11-D06 HUMAN_APPROVED`

**Upstream：**
- F11-G01 = HUMAN_APPROVED / FROZEN
- F11-D01 = HUMAN_APPROVED / FROZEN
- F11-D02 = HUMAN_APPROVED / FROZEN
- F11-D03 = HUMAN_APPROVED / FROZEN
- F11-D04 = HUMAN_APPROVED / FROZEN
- F11-D05 = HUMAN_APPROVED / FROZEN

**Implementation Authorization：** NO  
**RP2 Authorization：** NO  
**Authority Cutover Authorization：** NO  
**Canonical Replacement Authorization：** NO  
**Final Activation Authorization：** NO  
**Legacy Retirement Authorization：** NO

---

# 1. 决策目标

F11-D06 冻结 F11 Control Plane 中 `Result / Trace / Evidence / Provenance` 的呈现语义、适用性、关联、可见性与边界。

核心定义：

```text
Result
= 产生了什么结果

Trace
= 事情怎样发生

Evidence
= 什么依据支持某个 Claim / Result / Decision / Validation / Explanation

Provenance
= 这些信息来自哪里、谁产生、基于哪个 Subject / Revision / Context
```

四者必须保持语义独立，不得互相替代。

---

# 2. Result 语义边界

Result 必须保持 Subject-bound，可属于 Task、Action、Execution Attempt、Validation、Decision、Apply / Change 或其他 governed Subject。

```text
Task != Action != Execution Attempt
Task Result != Action Result != Attempt Result
Attempt Result != Action Result
Latest Attempt Result != Action Result by default
```

Result 产生与 Result 被接受严格分离：

```text
Result != Acceptance
Result Produced != Result Accepted
Result Exists != Business Success
Runtime Success != Governance Acceptance
Validation PASS != Approval
Validation PASS != Apply Authorization
Decision Accepted != Runtime Permission
Decision Accepted != Apply Authorization
Decision Accepted != Canonical Mutation
```

Result Status 必须保持 Domain-qualified。F11 可以形成跨 Domain 的摘要，例如“执行已完成，验证未通过，尚未进入 Apply”，但：

```text
Multi-domain Result != Global Result Truth
Result Summary != New Global Outcome
Cross-domain Result Summary != Cross-domain Result Authority
```

不得因为 F11 为了 UX 聚合信息，就创建新的 `GLOBAL_SUCCESS / PARTIAL_SUCCESS / GLOBAL_FAILED` 等跨 Authority Domain 真值，除非上游 Domain Contract 已正式定义。

---

# 3. Result 的历史性、当前适用性与替代关系

历史 Result 保留其历史真实性：

```text
Historical Result != Current Effective Result
Later Success != Historical Failure Erasure
Newest Result != Current Effective Result by timestamp alone
Historical Truth != Current Applicability
```

Current Effective Result 需要结合 Subject、Purpose、Result Type、Revision、Attempt 与 Owning Contract 判断。

Superseded 与 Stale 必须区分：

```text
Superseded Result != False Result
Superseded Result != Deleted Result
Stale != Superseded
No Longer Applicable != Invalid History
```

- **Stale**：Basis 已变化，旧 Result 对当前问题的适用性需要重新确认。
- **Superseded**：已经存在正式后继 Result，在相同 Purpose / Subject Basis 上取代旧 Result 的当前适用位置。
- **No Longer Applicable**：仍是有效历史事实，但已不属于当前路径、Subject 或 Purpose。

Timestamp 不建立 Current Applicability：

```text
Timestamp != Applicability
```

---

# 4. Trace 语义边界

Trace 回答“事情怎样发生”，可关联 Interaction、Decision、Runtime、Attempt、Validation、Apply / Change 等过程。

```text
Trace != Result
Trace != Complete Domain Truth
Trace != Authorization
Trace != Runtime Permission
Trace Sequence != Cause Relation
Temporal Precedence != Causal Proof
```

Trace 记录过程，但不替代 Runtime State、Decision、Gate、Binding、Canonical 等实际 Authority Domain Truth。

AI / F11 可以总结已有 Trace，但不能补造缺失事件：

```text
Trace Summary must not invent missing events
Trace Gap != Explanation Permission to Guess
Incomplete Trace must remain explicitly representable
Incomplete Trace != Runtime Failure
```

后续 Source 补齐缺失事件属于 Trace Enrichment：

```text
Trace Enrichment != Historical Trace Invalidity
```

若多个 Trace Source 对 Material Event 表达冲突，应保留 Trace Conflict：

```text
Trace Conflict != Last-write-wins Resolution
Trace Conflict != Runtime Conflict by default
```

Trace Conflict 首先需要解析“记录冲突”还是“Runtime 真正冲突”，F11 不得按时间戳擅自覆盖。

---

# 5. Trace 的 Purpose-sensitive Presentation 与导航

Trace Presentation 应按 Purpose 加载，而不是全量日志轰炸：

```text
Trace Presentation should be Purpose-sensitive
Trace Relevance should be Purpose-sensitive
Audit Depth != Unbounded Full-system Scan
```

Trace 应支持至少两类逻辑导航：

```text
Subject path
Task → Action → Attempt

Correlation path
Control Intent → Resolution → Attempt → Result
```

并继续保持：

```text
Correlation != Authorization
Correlation != Ownership Merge
```

Decision、Runtime、Validation 等虽然可被关联，但仍由各自 Owner 管理。

---

# 6. Evidence 语义边界

Evidence 回答“有什么依据支持某个 Claim、Result、Decision、Validation 或 Explanation”。

```text
Result != Evidence
Evidence != Trace
Evidence != Authority
Evidence Available != Human Decision Required
Evidence Strong != Automatic Governance Decision
```

Evidence 可以独立存在；当它被用于支持某个 Claim 时，支持关系必须可解释：

```text
Evidence should remain Claim-relative where used as support
One Evidence may support multiple Claims
One Claim may require multiple supporting Evidence items
```

Evidence 本身不因支持某 Claim 就获得 Product / Design / Decision / Apply / Runtime Authority。

---

# 7. Supporting / Contradictory Evidence 与 Evidence Conflict

D06 必须允许区分：

```text
Supporting Evidence
Contradictory Evidence
Unresolved Evidence Conflict
```

Exact Enum 不在 D06 冻结。

关键反向证据不得被聚合隐藏：

```text
Material Contradictory Evidence must not be hidden by aggregation
Material Contradictory Evidence must be surfaced before a conclusion is treated as settled
```

Evidence Conflict 不归 F11 仲裁：

```text
Evidence Conflict != F11 Authority Resolution
Evidence Conflict != Human Decision Required by default
Evidence Conflict should first trigger deterministic verification where possible
```

应优先按既有 Authority precedence、Source verification、Evidence refresh、deterministic validation、Stale Evidence elimination 等规则确定性解析；只有仍存在真实 Material Governance Choice 时才进入 D04。

Evidence 数量与信息体量不能替代 Authority：

```text
Evidence Count != Authority Weight
Information Volume != Governing Weight
Evidence Strength should be Basis-defined, not arbitrarily scored
```

D06 不冻结通用 AI `evidence_score`。

---

# 8. Evidence 的历史真实性与当前适用性

```text
Evidence Truthfulness != Current Applicability
Superseded Evidence != False Evidence
Newer Evidence != Automatic Evidence Supersession
Stale Evidence must not be presented as Current Confirmation
```

Evidence 是否适用于当前 Claim，需要结合 Claim、Subject、Purpose、Revision、Build、Scope、Environment、RuleSet、Artifact Revision 等 Basis 判断。

真实历史 Evidence 可以证明过去，但不自动证明当前：

```text
Historical Truth != Current Applicability
```

若 Evidence 缺少足够 Provenance：

```text
Evidence without usable Provenance may be insufficient for some Claims
```

是否足够由具体 Purpose 和 Governance Rule 决定。

---

# 9. Provenance 语义边界

Provenance 回答：某条 Result / Evidence / Trace / Claim 来自哪里、谁产生、基于什么 Subject、Revision / Build / Attempt / Context。

```text
Provenance != Authority
Source Identity != Authority Priority
Same Claim Text != Same Claim Authority
Producer != Source Basis
Presentation Producer != Underlying Authority
```

例如 AI 可以是 Summary Producer，但其 Basis 可以来自 PRD、Runtime Result、Gate、Trace 或 Evidence；Presentation Producer 不因此获得 Underlying Authority。

Source Provenance 与 Current Effectiveness 分离：

```text
Source Provenance != Source CurrentEffectiveness
```

Provenance 应保留与 Applicability 有关的 Revision / Version Basis；当当前适用性依赖版本演进时，应保留必要的 Revision / Version lineage，但不要求无界展开完整版本树。

```text
Provenance should preserve relevant Revision / Version basis
Provenance should preserve relevant Revision / Version lineage where applicability depends on it
```

---

# 10. Applicability 与 Currentness

Applicability Basis 是 Purpose- 和 Subject-sensitive 的：

```text
Applicability Basis is Purpose- and Subject-sensitive
Timestamp != Applicability
F11 Applicability Presentation != Applicability Authority
Currentness Claim must remain Basis-backed
```

F11 可以呈现 Current / Historical / Stale / Superseded / No Longer Applicable，但不得凭 UI 本地逻辑创建 Currentness Truth。

F9 Freshness Evidence 可作为 Applicability Resolution 的输入，但不成为 Applicability Authority。

---

# 11. Purpose-sensitive Presentation

D06 允许针对不同 Purpose 形成不同投影，至少逻辑上覆盖：

```text
Operational Summary
Governance Decision
Audit / Diagnosis
Implementation Validation
```

Exact Enum 不冻结。

但：

```text
Purpose-specific Projection != Purpose-specific Truth
```

### Operational Summary

优先呈现 Current Material Result、当前 Failure / Blocker、相关 Attempt、Material Recovery、相关 Evidence / Trace 链接。

```text
Operational View should favor Current Material State over Exhaustive History
Operational Compression must preserve Current Material Outcome
```

### Governance Decision View

优先呈现 Decision Basis、Material Result、Material Evidence、Contradictory Evidence、Relevant Provenance 和 Material Impact references。

```text
Governance Decision View should prioritize Decision-relevant Evidence, not raw technical volume
```

### Audit / Diagnosis

可以下钻 Subject Chain、Attempt History、Control Intent、Decision Resolution、Provider Resolution、Trace Gaps、Evidence Conflicts、Provenance、Revision lineage，但：

```text
Audit Depth != Unbounded Full-system Scan
```

### Implementation Validation

未来可组合 Expected Behavior、Actual Result、Diff、Validation Evidence、Relevant Trace、Build / Revision Provenance，但：

```text
Implementation Validation View does not authorize Implementation
```

---

# 12. Progressive Disclosure

Result、Trace、Evidence、Provenance 均应支持渐进下钻：

```text
Result Presentation:
Summary → Domain Detail → Supporting Detail

Evidence Presentation:
Summary → Claim Support → Detailed Evidence → Provenance

Trace Detail:
Purpose-sensitive progressive expansion

Provenance:
Purpose-sensitive and bounded drill-down
```

并保持：

```text
Evidence Presentation Priority != Evidence Authority
Less Detail != Different Outcome Meaning
Aggregation may compress volume but must not erase Material Conflict
```

Evidence Navigation 应支持 Claim-centric drill-down；Trace Navigation 应支持 Subject / Correlation paths。

---

# 13. Existence / Visibility / Authority 分离

```text
Existence != Visibility
Visibility != Authority
More Visibility != More Authority by default
Decision Authority != Universal Data Visibility
```

拥有 Governance Decision Authority，不代表可读取所有 Secret / Provider / Debug 数据；能看到更多数据，也不自动拥有更多治理权。

---

# 14. Restricted / Redacted / Unavailable / Unknown / Incomplete

这些语义必须分离：

```text
Restricted Evidence != Missing Evidence
Restricted Trace != No Trace
Restricted Provenance != Unknown Provenance
Redacted != Restricted
Data Unavailable != Event Did Not Occur
Incomplete != Unavailable
```

- **Restricted**：对象已知存在，但当前身份无权查看相应 Detail。
- **Redacted**：允许展示安全裁剪后的部分语义。
- **Unavailable**：对象已知存在，但当前暂时无法读取。
- **Unknown**：当前无法确定对象 / 内容是否存在或是什么。
- **Incomplete**：已读取的 Trace / Evidence 结构存在已知缺口。

Redaction 可以减少 Detail，但不得改变 Result / Evidence / Provenance 的真实语义。

```text
Visibility Filtering must preserve Material Result Meaning
Restricted Contradiction must not silently become No Contradiction
```

具体哪些受限信息可以向用户透露，由 D09 决定。

---

# 15. Restricted / Unavailable / Unknown 不自动进入人工决策

```text
Restricted Data != Human Decision Required
Unavailable Data != Human Decision Required
Unknown Data != Human Decision Required
```

应优先进入 recovery、refresh、alternative source、verification、governance routing；只有真正剩余 Material Governance Choice 时才进入 D04。

---

# 16. View / Export / Download / Share / Persist Copy 分离

D06 正式区分这些语义，但不冻结具体 Permission Enum：

```text
View Permission != Export Permission
Derived Export != Raw Source Download
Download Permission != Share Permission
Share Presentation Artifact != Source Access Control Mutation
```

F11 能展示某 Evidence，不代表用户可以导出、下载原始材料、分享或修改 Source ACL。

---

# 17. Derived Report / Export 边界

F11 可以生成派生报告，但：

```text
Derived Report != Underlying Evidence Authority
Derived Export should preserve sufficient Provenance for its material claims
Export Visibility must not silently exceed authorized Presentation Scope
Export Scope must not exceed authorized Subject / Governance Scope
```

导出摘要必须保留 Material Applicability Qualifiers，例如 Historical / Stale / Superseded / Restricted / Incomplete / Conflicting。

```text
Export Compression must preserve Material Applicability Qualifiers
Exported Snapshot != Eternal Current Truth
Exported / Captured Evidence retains Historical Truth but not Eternal Current Applicability
```

Presentation Artifact Revision 与 Source Revision 分离：

```text
Presentation Artifact Revision != Source Revision
Presentation Revision must not collapse underlying Source Revisions
```

---

# 18. Presentation Convenience 不允许复制 Truth

```text
Presentation Convenience != Justification for Truth Duplication
Materialized Copy != Canonical Source
```

若因 performance、offline UX、audit continuity 需要 Materialize，应保留 Source Basis、Revision、Applicability，并继续明确其不是 Canonical Source。

---

# 19. F11 Ownership Boundary

F11 负责 presentation / correlation / summarization / navigation，不拥有上游真相：

```text
F11 Evidence Presentation != Evidence Ownership
F11 Result View != Result Ownership
F11 Trace View != Trace Ownership
Provenance Presentation != Provenance Authority
Unified Presentation != Unified Trace Authority
Unified Audit Presentation != Universal Audit Truth Object
Presentation Object != Mandatory Durable Record
```

F11 不得创建 shadow Result / Trace / Evidence / Provenance Truth Store。

---

# 20. F9 边界

F9 继续负责：

```text
Index
Search
Context Recovery
Dependency
Impact
Fingerprint
Cache
Freshness Evidence
Rebuild
```

D06 负责 Result / Trace / Evidence / Provenance 的 Presentation Semantics。

```text
Index Discovery != Evidence Meaning
Cache Hit != Current Result Truth
Cache Hit != Current Evidence Applicability
Freshness Evidence supports Applicability Resolution but does not become Applicability Authority
```

---

# 21. F10 边界

F10 继续拥有：

```text
Runtime Result Authority
Execution Attempt Authority
Runtime Trace Authority
Runtime Failure / Recovery Truth
```

F11-D06 只负责：

```text
present
correlate
summarize
navigate
```

不得根据 Trace 自行重建 Runtime Truth：

```text
Trace-derived Guess != Runtime State Truth
Result Exists != Runtime Completed
```

Partial / Streaming / Intermediate Result 可在 Runtime 未完成时存在。

---

# 22. D07 Attention 边界

D06 负责说明有什么 Material Result / Evidence / Trace / Conflict 值得查看；D07 决定是否提醒、何时提醒、提醒几次、哪个 Surface、是否去重 / 聚合 / 升级。

```text
Material Result != Immediate Notification
Evidence Conflict != Immediate Notification
Trace Gap != Immediate Notification
Attention-relevant Evidence != Notification Decision
```

---

# 23. D08 Multi-Surface 边界

D06 冻结跨 Surface 的语义一致性；D08 负责 session continuity、delivery、reconnect、duplicate delivery、cross-surface continuity。

```text
Same underlying Evidence may be rendered differently across Surfaces, but its semantics must remain identical
Cross-surface Compression must preserve Material Qualifiers
```

Stale / Historical / Superseded / Incomplete / Conflicting / Restricted 等关键限定不能因 Surface 简化而丢失。

---

# 24. D09 Visibility / Sensitive Data 边界

D06 冻结 Presentation Semantics、Applicability、Trace / Evidence / Provenance meaning；D09 冻结 Visibility、Sensitive Data、Redaction、Scope-based Presentation Safety。

```text
D06 Presentation Semantics != D09 Visibility Policy
Audit Purpose != Universal Visibility Authorization
Diagnostic Purpose != Sensitive-data Override
```

D09 可以减少 Detail，但不能改变底层 Material Result Meaning。

---

# 25. F11-D06 Responsibility Flow

```text
1. Resolve Subject / Purpose

2. Retrieve relevant Result / Trace / Evidence / Provenance from actual owners

3. Resolve applicability
   Current
   Historical
   Stale
   Superseded
   No Longer Applicable

4. Preserve quality semantics
   Complete
   Incomplete
   Conflicting
   Restricted
   Redacted
   Unavailable
   Unknown

5. Build Purpose-sensitive Projection

6. Preserve Domain-qualified Result / Failure / Acceptance semantics

7. Preserve support relations
   Claim ↔ Evidence
   Result ↔ Trace
   Item ↔ Provenance
   Correlation paths

8. Apply Visibility / Presentation Safety without changing underlying meaning

9. Present progressively
   Summary → Domain Detail → Evidence / Trace / Provenance Drill-down

10. Export / Share only through separately authorized semantics

11. Refresh against current Basis when Current Applicability matters
```

该模型是 Responsibility Flow，不是固定 API、Storage 或 UI 流程。

---

# 26. Core Invariants

F11-D06 正式冻结以下核心不变量：

```text
Result != Acceptance
Result Produced != Result Accepted
Result Exists != Business Success
Result must remain Subject-bound
Task Result != Action Result != Attempt Result
Attempt Result != Action Result
Latest Attempt Result != Action Result by default
Runtime Success != Governance Acceptance
Validation PASS != Approval
Validation PASS != Apply Authorization
Result Status should remain Domain-qualified
Multi-domain Result != Global Result Truth
Result Summary != New Global Outcome
Historical Result != Current Effective Result
Later Success != Historical Failure Erasure
Newest Result != Current Effective Result by timestamp alone
Superseded Result != False Result
Superseded Result != Deleted Result
Stale != Superseded
No Longer Applicable != Invalid History
Historical Truth != Current Applicability

Trace != Result
Trace != Complete Domain Truth
Trace != Authorization
Trace != Runtime Permission
Trace Sequence != Cause Relation
Temporal Precedence != Causal Proof
Trace Summary must not invent missing events
Trace Gap != Explanation Permission to Guess
Incomplete Trace must remain explicitly representable
Incomplete Trace != Runtime Failure
Trace Enrichment != Historical Trace Invalidity
Trace Conflict != Last-write-wins Resolution
Trace Conflict != Runtime Conflict by default
Trace Presentation should be Purpose-sensitive
Correlation != Authorization
Correlation != Ownership Merge

Result != Evidence
Evidence != Trace
Evidence != Authority
Evidence Available != Human Decision Required
Evidence Strong != Automatic Governance Decision
Evidence should remain Claim-relative where used as support
One Evidence may support multiple Claims
One Claim may require multiple supporting Evidence items
Evidence Conflict != F11 Authority Resolution
Evidence Conflict != Human Decision Required by default
Evidence Conflict should first trigger deterministic verification where possible
Evidence Count != Authority Weight
Information Volume != Governing Weight
Evidence Truthfulness != Current Applicability
Superseded Evidence != False Evidence
Newer Evidence != Automatic Evidence Supersession
Stale Evidence must not be presented as Current Confirmation
Material Contradictory Evidence must not be hidden by aggregation
Material Contradictory Evidence must be surfaced before a conclusion is treated as settled
Evidence Strength should be Basis-defined, not arbitrarily scored
Evidence without usable Provenance may be insufficient for some Claims

Provenance != Authority
Source Identity != Authority Priority
Same Claim Text != Same Claim Authority
Producer != Source Basis
Presentation Producer != Underlying Authority
Source Provenance != Source CurrentEffectiveness
Provenance should preserve relevant Revision / Version Basis
Applicability Basis is Purpose- and Subject-sensitive
Timestamp != Applicability
F11 Applicability Presentation != Applicability Authority
Currentness Claim must remain Basis-backed

Purpose-specific Projection != Purpose-specific Truth
Operational Compression must preserve Current Material Outcome
Governance Decision View should prioritize Decision-relevant Evidence
Audit Depth != Unbounded Full-system Scan
Implementation Validation View does not authorize Implementation
Evidence Presentation Priority != Evidence Authority
Less Detail != Different Outcome Meaning
Aggregation may compress volume but must not erase Material Conflict
Evidence Navigation should support Claim-centric drill-down
Trace Navigation should support Subject / Correlation paths
Provenance Depth should be Purpose-sensitive and bounded

Existence != Visibility
Visibility != Authority
Visibility != Export Permission
Visibility != Share Permission
Presentation != Ownership
Restricted Evidence != Missing Evidence
Restricted Trace != No Trace
Restricted Provenance != Unknown Provenance
Redacted != Restricted
Data Unavailable != Event Did Not Occur
Incomplete != Unavailable
Restricted Data != Human Decision Required
Unavailable Data != Human Decision Required
Unknown Data != Human Decision Required
More Visibility != More Authority by default
Decision Authority != Universal Data Visibility

View Permission != Export Permission
Derived Export != Raw Source Download
Download Permission != Share Permission
Share Presentation Artifact != Source Access Control Mutation
Derived Report != Underlying Evidence Authority
Derived Export should preserve sufficient Provenance
Export Visibility must not silently exceed authorized Presentation Scope
Export Compression must preserve Material Applicability Qualifiers
Export Scope must not exceed authorized Subject / Governance Scope
Exported Snapshot != Eternal Current Truth
Exported / Captured Evidence retains Historical Truth but not Eternal Current Applicability
Presentation Artifact Revision != Source Revision
Presentation Revision must not collapse underlying Source Revisions
Presentation Convenience != Justification for Truth Duplication
Materialized Copy != Canonical Source

Index Discovery != Evidence Meaning
Cache Hit != Current Result Truth
Cache Hit != Current Evidence Applicability
Freshness Evidence supports Applicability Resolution but does not become Applicability Authority
Trace-derived Guess != Runtime State Truth
Result Exists != Runtime Completed
Material Result != Immediate Notification
Evidence Conflict != Immediate Notification
Trace Gap != Immediate Notification
Attention-relevant Evidence != Notification Decision
Cross-surface Compression must preserve Material Qualifiers
D06 Presentation Semantics != D09 Visibility Policy
Visibility Filtering must preserve Material Result Meaning
Restricted Contradiction must not silently become No Contradiction
Audit Purpose != Universal Visibility Authorization
Diagnostic Purpose != Sensitive-data Override

F11 Evidence Presentation != Evidence Ownership
F11 Result View != Result Ownership
F11 Trace View != Trace Ownership
Provenance Presentation != Provenance Authority
Unified Audit Presentation != Universal Audit Truth Object
Presentation Object != Mandatory Durable Record
```

---

# 27. Explicitly Forbidden Designs

F11-D06 明确禁止：

```text
Result = Acceptance
Result exists = Success
Execution completed = Governance approved
Validation PASS = Human approval
Validation PASS = Apply Authorization
Latest Attempt = Action Result by default
Newest Result = Current Result only because timestamp is newer
Retry success = delete old failed Attempt
Result summary = New Global Truth
Trace = Complete Domain Truth
Trace = Authorization
Trace = Runtime Permission
Trace order = Cause
Missing Trace event = AI may invent it
Trace conflict = latest record wins
Evidence = Authority
More Evidence = Higher Authority
Evidence count = Governance weight
Evidence conflict = Ask human immediately
Evidence conflict = AI chooses preferred source
New Evidence = Old Evidence false
Newer Evidence = Automatically Current
Historical Evidence = Current Evidence
Timestamp = Applicability
Provenance = Authority
Source name = Authority priority
AI-produced summary = AI Authority
View = Export permission
View = Download permission
Download = Share permission
Audit mode = See everything
Debug mode = Sensitive-data bypass
Restricted item = Does not exist
Unavailable trace = Event did not occur
Redacted content = Replace actual meaning
F11 display = F11 owns source
F11 cache = Current Truth
F11 trace page = Runtime Trace Authority
F11 evidence page = Evidence Authority
Universal AuditEvent = Result + Trace + Evidence + Authority + State + Truth
Export report = New Canonical Source
Report revision = Underlying source revision
Presentation convenience = Copy all upstream truth
Materialized cache = Canonical Source
Cross-surface shorter output = Remove material qualifiers
```

---

# 28. Deferred

F11-D06 不冻结：

```text
Exact Result Enum
Exact Result Status Enum
Exact Evidence Enum
Exact Evidence Strength Model
Exact Trace Event Enum
Exact Trace Gap Enum
Exact Conflict Enum
Exact Provenance Schema
Exact Current / Historical / Stale / Superseded Enum
Exact Applicability Algorithm
Exact Evidence Conflict Algorithm
Exact Trace Conflict Algorithm
Exact Evidence Storage
Exact Trace Storage
Exact Provenance Storage
Exact Retention Policy
Exact Trace Sampling
Exact Search / Index implementation
Exact Export Format
Exact Download Permission Model
Exact Share Permission Model
Exact Report Schema
Exact Audit Report Format
Exact Redaction Rules
Exact Sensitive Data Classification
Exact Access Control Implementation
Exact UI Layout
Database Tables
SQLite Physical Schema
Redis Structure
REST API
HTTP Status
WebSocket
SSE
Go Struct
TypeScript Interface
```

---

# 29. Approval Effect

本稿已经明确：

```text
F11-D06 HUMAN_APPROVED
```

因此正式冻结：

```text
Result / Trace / Evidence / Provenance separation
Subject-bound Result semantics
Task / Action / Attempt Result separation
Produced / Accepted separation
Domain-qualified Result semantics
Historical / Current / Stale / Superseded / No Longer Applicable semantics
Trace Gap / Incomplete / Conflict semantics
Claim-relative Evidence semantics
Supporting / Contradictory Evidence
Evidence conflict preservation
Evidence / Authority separation
Provenance / Producer / Source / Revision separation
Applicability Basis semantics
Purpose-sensitive Presentation
Operational / Governance / Audit / Validation presentation boundaries
Claim-centric Evidence drill-down
Subject / Correlation Trace navigation
Progressive Disclosure
Restricted / Redacted / Unavailable / Unknown distinction
Existence / Visibility / Authority separation
View / Export / Download / Share separation
Derived Report provenance requirement
Cross-surface semantic consistency
F9 Index / Cache boundary
F10 Runtime Result / Trace Authority boundary
D07 Attention boundary
D08 Multi-surface boundary
D09 Visibility / Sensitive Data boundary
No F11 shadow Result / Trace / Evidence / Provenance truth store
```

但不代表：

```text
Evidence Store transferred to F11
Trace Store transferred to F11
Runtime Result Authority transferred to F11
Provenance Authority transferred to F11
Exact enums frozen
Exact evidence taxonomy frozen
Exact trace schema frozen
Exact export implementation frozen
Exact access-control model frozen
Exact retention policy frozen
Database frozen
SQLite schema frozen
API frozen
UI frozen
Implementation authorized
RP2 authorized
Authority Cutover authorized
Canonical Replacement authorized
Final Activation authorized
Legacy Retirement authorized
```

---

# 30. Final Frozen Decision

```text
F11-D06
— Result / Trace / Evidence / Provenance Presentation

STATUS:
HUMAN_APPROVED / FROZEN

Banyan keeps Result, Trace, Evidence, and Provenance semantically separate.

Result explains what was produced or resolved.
Trace explains how events occurred.
Evidence supports specific Claims, Results, Decisions, Validations, or Explanations.
Provenance explains where those materials came from, who produced them, and against which Subject / Revision / Context.

Result does not equal Acceptance.
Runtime success does not equal Governance acceptance.
Validation PASS does not equal Approval or Apply Authorization.
Results remain Subject- and Domain-qualified.
Historical Results remain true without automatically remaining currently applicable.
Later success does not erase earlier failure history.

Trace records process, not Permission, Authorization, or complete Domain Truth.
Trace gaps and conflicts remain explicit.
Missing Trace events must not be invented.

Evidence does not equal Authority.
Evidence quantity does not determine Governance weight.
Contradictory Evidence must not be silently hidden.
Evidence conflicts are resolved through existing Authority / verification rules before Human Decision is considered.
Evidence may remain historically true while no longer applying to the current Revision, Build, Scope, or Purpose.

Provenance does not equal Authority.
Producer, Source Basis, Revision, and Current Effectiveness remain distinct.
Timestamp does not establish Current Applicability.
Currentness remains Basis-backed.

F11 uses Purpose-sensitive Presentation rather than exposing all Result / Trace / Evidence for every interaction.
Operational, Governance, Audit, and future Implementation Validation may use different projections of the same underlying truth.
Less detail may not create different semantic meaning.

Existence, Visibility, Authority, Export Permission, and Share Permission remain distinct.
Restricted, Redacted, Unavailable, Incomplete, and Unknown remain semantically distinct.
View does not imply Export.
Download does not imply Share.
Derived Reports preserve sufficient Provenance but do not become new underlying Authority.
Exported snapshots retain Historical Truth, not Eternal Current Applicability.

F9 may discover, index, cache, and supply Freshness Evidence, but does not redefine Result / Evidence meaning.
F10 remains owner of Runtime Result and Runtime Trace truth.
F11 presents, correlates, summarizes, and navigates those facts without becoming their owner.

D07 governs Attention.
D08 governs multi-surface continuity.
D09 governs Visibility and Sensitive Data.

F11 does not create a shadow Result / Trace / Evidence / Provenance truth store.
Implementation remains NOT_AUTHORIZED.
```

---

**END OF F11-D06 HUMAN_APPROVED FREEZE**

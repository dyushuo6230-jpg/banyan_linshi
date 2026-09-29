# F11-D09 — Visibility / Sensitive Data / Presentation Safety
## 可见性 / 敏感数据 / 呈现安全

**Stage：** F11 — Control Plane / Governance UX Architecture  
**Decision ID：** F11-D09  
**Status：** HUMAN_APPROVED / FROZEN

**Upstream：**
- F11-G01 = HUMAN_APPROVED / FROZEN
- F11-D01 = HUMAN_APPROVED / FROZEN
- F11-D02 = HUMAN_APPROVED / FROZEN
- F11-D03 = HUMAN_APPROVED / FROZEN
- F11-D04 = HUMAN_APPROVED / FROZEN
- F11-D05 = HUMAN_APPROVED / FROZEN
- F11-D06 = HUMAN_APPROVED / FROZEN
- F11-D07 = HUMAN_APPROVED / FROZEN
- F11-D08 = HUMAN_APPROVED / FROZEN

**Implementation Authorization：** NO  
**RP2 Authorization：** NO  
**Authority Cutover Authorization：** NO  
**Canonical Replacement Authorization：** NO  
**Final Activation Authorization：** NO  
**Legacy Retirement Authorization：** NO

---

# 1. 决策目标

F11-D09 冻结 Banyan Control Plane 中 Visibility、Sensitive Data、Presentation Safety、Redaction、Abstraction、Safe Projection、Viewer、Scope、Purpose、Surface、Evidence / Provenance Visibility、Action Visibility、Export / Download / Share Visibility、Visibility Applicability、Safe Degradation 的语义与责任边界。

核心目标：

> 在不泄露敏感信息的前提下，仍然准确表达当前真实的运行、治理、决策、结果和注意力语义。

D09 必须同时满足：

```text
Truthful
Minimum-sufficient
Non-leaking
Purpose-appropriate
Authority-preserving
```

即：说的是真的；给的信息足够当前任务；不泄露；符合当前 Scope / Purpose / Surface；且“看见”本身不能创造 Authority 或 Permission。

---

# 2. Visibility 与 Authority 分离

正式冻结：

```text
Visibility != Authority
Can See != Can Decide
More Visibility != More Authority by default
Decision Authority != Universal Data Visibility
```

能够看到对象、Evidence、Result，不代表拥有 Decision / Runtime / Apply / Canonical Authority。

反过来，拥有 Decision Authority，也不代表可以查看所有原始敏感材料。

---

# 3. Visibility 不是单一布尔值

逻辑上至少区分：

```text
Existence Visibility
Summary Visibility
Detail Visibility
Evidence Visibility
Provenance Visibility
Action Visibility
Export / Download / Share Visibility
```

正式冻结：

```text
Object Existence Visibility != Object Detail Visibility
Subject Visibility != Action Visibility
Evidence Visibility != Full Provenance Visibility
View Visibility != Export Visibility
Export Visibility != Share Visibility
```

对象“是否存在”本身也可能属于敏感信息：

```text
Existence Metadata may itself be sensitive
```

---

# 4. Restricted / Unknown / Missing / Unavailable / Redacted 分离

正式冻结：

```text
Restricted != Unknown
Restricted != Missing
Restricted != Unavailable
Redacted != Unknown
```

语义：

```text
Unknown = 系统不知道
Unavailable = 当前无法取得
Restricted = 系统知道，但当前 Viewer / Context 不允许展示
Redacted = 允许展示结构或意义，但敏感 Detail 被隐藏
No Longer Applicable = 历史真实，但当前不再适用
```

不得全部压缩成 `N/A`。

```text
Presentation must preserve material absence semantics
```

---

# 5. Hide Detail, Preserve Meaning

D09 正式采用：

```text
Hide Detail,
Preserve Meaning
```

正式冻结：

```text
Redaction must not change governing meaning
Presentation Safety != Semantic Distortion
Safe Presentation must remain truthful
Restricted Supporting Detail must not erase Required Human Participation
Presentation Visibility must preserve Recipient Responsibility semantics
```

安全处理不得修改 State、Reason、Blocker、Decision Requirement、Result、Acceptance、Conflict existence、Human participation meaning。

Restricted Cause 不是 Unknown Cause：

```text
Restricted Cause != Unknown Cause
```

---

# 6. Action Visibility 与 Permission 分离

正式冻结：

```text
Button Visible != Action Authorized
Visible Action != Pre-authorized Action
UI Enabled != Permission Granted
UI Hidden != Security Boundary
```

D09 只负责当前 Viewer / Surface 是否应该看到某个 Action 入口；真正能否执行仍由 D03 / F10 / 对应 Authority Owner 决定。

```text
Can View Runtime Control != Can Execute Runtime Control
Hidden Control != Denied Runtime Permission
Visible Control != Granted Runtime Permission
```

---

# 7. Surface / Scope / Purpose / Role / Authority

正式冻结：

```text
Action Visibility may be Surface-sensitive
Same User != Same Presentation Detail across every Surface
Surface Capability != Visibility Authority
Surface Security Capability may enable safer presentation,
but must not create new visibility authority
```

Visibility Resolution 必须是 Context-composed，而不是单因素决定：

```text
Viewer
Subject
Scope
Purpose
Surface
Sensitivity
Relationship
Authority / Responsibility
Current Policy
Requested Presentation Action
```

正式冻结：

```text
Visibility Resolution must be context-composed, not single-factor
User Identity alone is insufficient for Visibility Resolution
Role != Universal Visibility
Role is an input to Visibility Resolution, not Visibility Truth
Administrative Capability != Universal Sensitive-data Visibility
Authority may justify required visibility, but does not imply unrestricted visibility
Required Participation != Right to raw secret disclosure
Visibility must remain Scope-bound
Role Scope must remain bounded by applicable Subject Scope
Visibility may be Purpose-sensitive
Purpose may shape visibility, but must not silently expand Scope
Audit Purpose != Universal Visibility Authorization
Diagnostic Purpose != Sensitive-data Override
Debug Mode != Visibility Bypass
```

---

# 8. Visibility Rule Composition / Override / Conflict

D09 采用限制保持原则：

```text
Visibility Composition should be restriction-preserving by default
```

但 Core 不建立全局固定优先级梯子：

```text
D09 Core must not invent a universal visibility precedence ladder
```

更具体、已治理的覆盖规则可以覆盖 General Rule，但必须显式声明优先关系：

```text
Specific Governed Override
may override General Visibility Rule
only when precedence is explicitly defined
```

正式冻结：

```text
Visibility Conflict must be resolved by governed precedence, not AI preference
Unresolved Visibility Conflict != Permission to disclose
Unresolved Visibility Conflict should fail safe in disclosure without falsifying domain meaning
Fail-safe Disclosure != Semantic Erasure
Mandatory Restriction cannot be bypassed by ordinary presentation convenience
User Presentation Preference != Sensitive-data Policy Override
```

Policy Conflict 应收窄披露，而不是扩大披露：

```text
Policy Conflict should narrow disclosure until governed resolution, not widen it
```

---

# 9. Subject / Field / Relationship / Evidence / Provenance 分离

正式冻结：

```text
Subject Visible != All Fields Visible
Visible Endpoints != Visible Relationship
Object Visibility != Relationship Visibility
Relationship Sensitivity must be independently governable
Evidence Visibility may be representation-sensitive
Provenance Visibility may be progressively disclosed
Provenance Visibility and Evidence Detail Visibility must remain separable
```

Evidence 可按 Summary / Structured Finding / Raw Artifact 等 Representation 形成不同 Visibility。

---

# 10. Evidence Conflict 与 Informed Decision

正式冻结：

```text
Restricted Contradictory Evidence must not become “No Contradiction”
Presentation Safety must not erase Material Decision Difference
Restricted Detail must not invalidate Informed Decision semantics
```

Raw Secret 不一定需要直接展示：

```text
Material Decision Context
may be satisfied by safe derived semantics
without raw secret disclosure
```

Presentation Capability 必须足以支撑其暴露的交互：

```text
Presentation Capability must be sufficient for the semantic interaction exposed
Cannot Safely Present Decision != No Decision Authority
```

如果当前 Surface 无法安全提供最低充分 Decision Context，应迁移交互，而不是降低语义质量：

```text
Presentation Relocation != Authority Transfer
Presentation Relocation != New Decision Requirement
```

Authority / Visibility 不兼容时：

```text
Authority / Visibility Incompatibility != Automatic Visibility Expansion
Authority / Visibility Incompatibility != Automatic Authority Revocation
Authority / Visibility Incompatibility != Human Decision Required by default
```

优先尝试 alternate safe Surface、safe derived semantics、authorized abstraction、existing exception rule、existing role / binding resolution。

---

# 11. Redaction / Abstraction / Material Semantic Preservation

正式冻结：

```text
Redaction != Abstraction
Abstraction must remain source-faithful
Safe Abstraction should preserve material actionability when policy permits
Actionability does not require full actor identity disclosure
Safe Projection must preserve all Material Semantics required for its Presentation Purpose
```

D09 正式采用：

```text
Material Semantic Preservation
```

Redaction 过度的判定：

```text
Redaction is excessive
when it removes
material operational or governance meaning
```

---

# 12. Aggregation Leakage

正式冻结：

```text
Aggregation != Automatic Safe Anonymization
Aggregation must not leak out-of-scope existence
Restricted Item Count may itself be sensitive
Hidden-item Metadata must obey Visibility Policy
```

同时：

```text
Aggregation must preserve
material hidden-class distinctions
when the viewer is entitled to know them

Preserve Material Meaning
within the viewer’s allowed disclosure envelope
```

---

# 13. AI Summary / Derived Information

正式冻结：

```text
AI Summary must obey the viewer’s Visibility Boundary
AI-derived Presentation must not reveal hidden source detail
Allowed Inputs to AI != Allowed Outputs to Viewer
Model Context Access != Viewer Disclosure Authorization
Backend Context Availability != Frontend Disclosure Permission
Inference must not bypass Visibility Policy
Derived Sensitive Information must be governed, not only Raw Sensitive Fields
Derived Disclosure must be governed as strictly as direct disclosure when it reveals protected meaning
Safe Summary must preserve Fact / Inference distinction
Permissible Inference must satisfy both evidentiary support and visibility policy
Derived Safe Summary must remain Basis-backed
Summary Basis Visibility may itself be safely abstracted
Safe Summary != Source Authority
```

AI 不是 Visibility / Redaction Authority：

```text
AI Presentation Generator != Visibility Authority
AI Presentation Generator != Redaction Authority
AI Sensitivity Inference may trigger safer handling but does not become Universal Classification Authority
```

---

# 14. Safe Projection 不建立第二 Truth Store

正式冻结：

```text
Safe Presentation Projection != New Domain Truth
Safe Presentation != Shadow Sanitized Truth Store
Materialized Safe Artifact != Canonical Sanitized Truth
Presentation Safety Owner != Universal Data Classification Authority
```

推荐逻辑：

```text
Authoritative Truth
+
Visibility Policy
→
Purpose-sensitive Safe Projection
```

而不是维护另一套永久“安全真相”。

---

# 15. Visibility Granularity

正式冻结：

```text
Visibility Granularity should be fit-for-purpose, not universally field-level
Coarse Visibility Rule must allow finer restriction where material sensitivity requires it
Fine-grained Visibility should be introduced only where semantic or sensitivity boundaries justify it
Visibility Default must be governed within an explicit scope
Unknown Sensitivity != Permission to Disclose
Protective Restriction may be temporary and classification-dependent
```

允许按需要采用 Subject-level、Section-level、Field-level、Relationship-level、Artifact-level、Representation-level 等粒度，但不机械要求每个字段都独立 ACL。

---

# 16. View / Export / Download / Share

继续继承 D06：

```text
View != Export
Export != Download
Download != Share
View Permission != Export Permission
Export Permission != Share Permission
```

并正式冻结：

```text
Usable by System != Presentable to Human
Presentable to Human != Exportable
Viewability != Automatic Exfiltration Permission
Auditability != Secret Disclosure
Audit Detail != Raw Secret Access
Export Risk may justify stricter visibility requirements than View Risk
Share != Authority Delegation
```

---

# 17. Error Presentation / Visibility Explanation

正式冻结：

```text
Error Presentation must obey the same Visibility Policy
Raw Error != Safe User Explanation
Safety != Meaningless Error Message
Visibility Resolution should be explainable at a safe level
Visibility Explanation must itself obey Visibility Policy
Access-denial Explanation must not disclose the protected fact it is denying
```

同一 Fact 可以针对不同 Viewer 形成不同 Safe Representation，但底层 Fact 不变：

```text
Same Fact may have different safe representations for different viewers
```

---

# 18. Visibility Current Applicability / Lifecycle

正式冻结：

```text
Past Visibility != Current Visibility
Cached Visibility Decision != Eternal Visibility Authorization
Visibility Change != Domain Fact Change
Visibility Revocation != Historical Truth Deletion
Cached Visibility != Current Visibility
```

Visibility Revalidation 应按 Purpose / Risk 发生，而不是机械连续重算：

```text
Visibility Revalidation should be purpose- and risk-sensitive, not mechanically continuous
```

典型 Material Boundary 可包括：Open sensitive detail、Decision interaction、Export、Download、Share、Cross-scope navigation、Reconnect、Sensitive cache reuse。Exact Trigger Deferred。

```text
Open Presentation must converge toward current Visibility applicability
Domain Snapshot != Visibility Snapshot
```

现实边界：

```text
Visibility Revocation
can stop future platform disclosure,
but cannot guarantee retroactive erasure
from human memory or external captures
```

---

# 19. Material Visibility Basis Change

正式冻结：

```text
Cached Sensitive Payload
must not be reused
solely because it was previously visible

Material Visibility Basis Change
must trigger applicability reevaluation
```

可能包括 Role、Scope、Project Binding、Authority assignment、Policy revision、Sensitivity classification、Surface security context、Purpose 的 Material Change。

```text
Any Policy Revision != Universal Visibility Invalidation
Sensitivity Classification Change != Automatic Disclosure Expansion
```

---

# 20. Draft / Notification / Export Current Visibility

正式冻结：

```text
Draft Visibility must be resolved independently from Draft Existence
Draft Exists != Draft Fully Visible
Cross-surface Draft Continuity != Cross-surface Detail Disclosure
Historical Notification Content != Current Safe Notification Content
Historical Notification View != Current Subject Visibility
Exported Snapshot != Current Visibility Authorization
Past Safe Projection != Current Safe Projection
Cached Safe Projection must not bypass current visibility applicability
```

同时：

```text
Visibility Revocation
!= Guaranteed Revocation
of previously exported external copies
```

---

# 21. Presentation Safety Failure / Safe Degradation

绝对禁止 Raw Fallback：

```text
Presentation Safety Failure != Permission to disclose raw data
Safety Uncertainty must not broaden disclosure
```

D09 采用 Safe Degradation 思想：

```text
Full Safe Detail
↓
Reduced Safe Detail
↓
Abstracted Meaning
↓
Restricted Placeholder
↓
No Disclosure
```

正式冻结：

```text
Safe Degradation should preserve the highest safely supportable semantic level
Safety Failure should degrade detail before erasing safe high-level meaning, where safely possible
Presentation Safety Failure must not create a substitute domain explanation
Redaction Failure != Unknown Domain Cause
Visibility Resolution Failure != Confirmed Denial
Visibility Resolution Failure != Confirmed Allow
Visibility Uncertainty != Domain Uncertainty
Visibility UNKNOWN != Human Decision Required
Safety Conflict Explanation must itself be safely presented
```

---

# 22. AI-generated Presentation Safety

正式冻结：

```text
AI-generated Safe Projection
must be safety-validatable
before viewer disclosure

Unverifiable AI Presentation
!= Permission to display it
```

必要时降级为 deterministic template、structured safe fields 或 restricted placeholder。

```text
User Request != Visibility Grant
Presentation Request != Visibility Authorization
```

---

# 23. Urgency / Blocker / Decision / Failure 不得覆盖 Sensitive Policy

正式冻结：

```text
Urgency != Sensitive-data Override
Blocker != Visibility Override
Human Decision Required != Visibility Override
Runtime Failure != Visibility Override
```

---

# 24. No Safe Decision Presentation Path

若 Decision Authority 存在、Material Decision Context 存在，但当前没有任何安全 Presentation Path 能提供最低充分信息，则：

```text
No Safe Decision Presentation Path
may become a governance blocking condition
```

但：

```text
Presentation Governance Blocker != Runtime Failure
Presentation Governance Blocker != Authority Conflict by default
Presentation Safety Blocker != Permission to weaken policy
```

---

# 25. D09 与 D04 边界

D04 拥有 Human Decision Requirement、Decision Question、Alternatives、Material Difference、Decision Basis、GovernanceDecisionInput。

D09 负责这些内容在当前 Viewer / Scope / Purpose / Surface 下如何安全呈现。

```text
D09 Presentation Filtering must not redefine D04 Decision Meaning
Presentation Block != Decision Requirement Resolution
```

---

# 26. D09 与 D05 边界

D05 拥有 Reason、Blocker、Cause、Explanation Semantics。

D09 负责 Detail Visibility、Safe Abstraction、Redaction。

```text
D09 may reduce Explanation Detail
but must not rewrite Reason / Cause Truth
Restricted Cause != Unknown Cause
```

---

# 27. D09 与 D06 边界

D06 拥有 Result、Trace、Evidence、Provenance、Applicability、Export Semantics。

D09 拥有 View / Detail / Representation / Export / Share Visibility Safety。

```text
D09 Visibility Policy != Evidence Authority
D09 Redaction != Result Mutation
D09 Export Safety != Export Truth Ownership
```

---

# 28. D09 与 D07 边界

D07 决定是否需要提醒、提醒谁、什么时候提醒。

D09 决定提醒中能够安全展示多少。

```text
Notification Eligibility != Notification Detail Visibility
Attention Requirement does not imply full notification disclosure
```

---

# 29. D09 与 D08 边界

D08 负责 Surface / Session / Delivery / Draft Continuity。

D09 负责同步与恢复时哪些内容可以安全展示。

```text
Cross-surface Continuity != Cross-surface Sensitive Payload Replication
Logical Continuity may cross Surfaces
Sensitive Detail must remain Surface- and Policy-eligible
```

---

# 30. D09 与 F10 边界

F10 继续拥有 Runtime State、Runtime Permission、Execution、Attempt、Result、Failure / Recovery。

```text
Can View Runtime Control != Can Execute Runtime Control
Hidden Control != Denied Runtime Permission
Visible Control != Granted Runtime Permission
Presentation Safety must not mutate Runtime Result semantics
```

D09 不得把真实 FAILED 改成 UNKNOWN，仅因为 Failure Detail 受限。

---

# 31. Responsibility Flow

D09 正式采用：

```text
1. Resolve Viewer
2. Resolve Subject / Scope
3. Resolve Presentation Purpose
4. Resolve Surface Context
5. Resolve Sensitivity / Visibility Policy
6. Resolve Representation:
   Full / Reduced / Redacted / Abstracted / Restricted / No Disclosure
7. Preserve Material Semantics
8. Validate Derived / AI-generated Presentation
9. Apply Action / Export / Download / Share boundaries
10. Present
11. Re-evaluate when Material Visibility Basis changes
```

这是 Responsibility Model，不是固定 API / ACL Workflow。

---

# 32. Safe Failure Flow

当 Visibility / Redaction / AI Presentation Safety 无法可靠解析时：

```text
Attempt current safe resolution
↓
Use safer deterministic representation
↓
Reduce Detail
↓
Abstract Material Meaning
↓
Restricted Placeholder
↓
No Disclosure
↓
Governance / Policy Resolution when genuinely required
```

禁止：

```text
Safety failure → raw fallback
```

---

# 33. Explicitly Forbidden Designs

F11-D09 明确禁止：

```text
Can View = Can Decide
Decision Authority = See Everything
Admin = Universal Visibility
Audit = Raw Secret Access
Debug Mode = Visibility Bypass
Secure Surface = New Authority
Role = Visibility Truth
User Identity = Complete Visibility Decision
Subject visible = all fields visible
Objects visible = relationship visible
Evidence visible = raw evidence visible
Evidence visible = all provenance visible
Button hidden = Security Boundary
Button visible = Permission Granted
User asks for hidden data = Visibility Grant
include_sensitive=true = Visibility Authorization
Urgent = show secret
Blocked = show secret
Decision Required = show secret
Failure = show secret
Restricted = Unknown
Restricted = Missing
Restricted = Unavailable
Redacted = Unknown
Redaction = change Reason
Redaction = erase blocker
Redaction = erase Human Decision Requirement
Restricted contradiction = no contradiction
Safe summary = invent new explanation
AI sees data = viewer may see data
AI inference = visibility bypass
Aggregation = anonymization
Count of hidden items = always safe
Audit mode = see everything
View = Export
Export = Share
Viewable = Copyable
System can use secret = Human may see secret
Visibility service failure = show raw data
Visibility service failure = confirmed deny
Visibility service failure = confirmed allow
Redaction failure = unknown domain reason
Policy conflict = choose permissive rule
Unknown sensitivity = safe to disclose
Old session permission = current visibility
Old cached detail = current visibility
Old export = current export authorization
Old notification = current safe detail
Draft sync = sensitive-data bypass
Cross-surface sync = raw sensitive replication
Presentation blocker = runtime failure
Presentation blocker = authority conflict automatically
D09 = Decision Authority
D09 = Evidence Authority
D09 = Runtime Permission Authority
Safe Presentation = second sanitized truth store
```

---

# 34. Deferred

F11-D09 明确暂缓：

```text
Exact Sensitivity Enum
Exact Clearance Enum
Exact Visibility Rule DSL
Exact Visibility Policy Schema
Exact Role / Scope precedence
Exact Policy inheritance syntax
Exact Governed Override syntax
Exact Redaction algorithm
Exact Abstraction algorithm
Exact masking format
Exact Secret Classification Catalog
Exact PII taxonomy
Exact field-level ACL implementation
Exact row-level ACL implementation
Exact relation ACL implementation
Exact artifact-level ACL implementation
Exact export permission model
Exact copy restriction mechanism
Exact secure Surface catalog
Exact Visibility Service design
Exact Policy Resolver implementation
Exact Visibility cache invalidation
Exact AI output filter
Exact content-safety validator
Exact Sensitive-data scanner
Exact Classification engine
Exact encryption mechanism
Exact key management
Exact retention policy
Database tables
SQLite Physical Schema
Redis Structure
REST API Authorization
WebSocket Visibility Filter
SSE Visibility Filter
Go Struct
TypeScript Interface
Frontend Route Guard
Frontend Field Guard
UI Layout
```

---

# 35. Final Freeze Effect

`F11-D09 HUMAN_APPROVED` 正式冻结：

```text
Visibility / Authority separation
Existence / Summary / Detail / Evidence / Provenance / Action / Export / Share visibility separation
Restricted / Unknown / Missing / Unavailable / Redacted semantics
Material Semantic Preservation
Context-composed Visibility Resolution
Scope-bound Visibility
Purpose-sensitive Visibility
Surface-sensitive Presentation
Governed Override / Visibility Conflict boundary
Subject / Field / Relationship sensitivity separation
Representation-sensitive Evidence visibility
Progressive Provenance disclosure
Action Visibility / Runtime Permission separation
View / Export / Download / Share separation
AI input / Viewer output boundary
Derived sensitive information governance
Aggregation leakage boundary
Safe Redaction / Abstraction / AI Summary semantics
Informed Decision preservation
Presentation Relocation
Authority / Visibility incompatibility handling
Visibility lifecycle / Current applicability
Cache / Draft / Notification / Export visibility boundary
Safe Degradation
Visibility / Redaction / AI Presentation failure semantics
D04 Decision boundary
D05 Explanation boundary
D06 Result / Evidence / Provenance / Export boundary
D07 Notification boundary
D08 Multi-Surface boundary
F10 Runtime Permission boundary
No Shadow Sanitized Truth Store
```

仍然不代表：

```text
Exact ACL model frozen
Exact RBAC / ABAC model frozen
Exact sensitivity taxonomy frozen
Exact redaction implementation frozen
Exact database model frozen
Exact permission cache frozen
Exact API security model frozen
Exact frontend guard frozen
Exact encryption implementation frozen
Implementation authorized
RP2 authorized
Authority Cutover authorized
Canonical Replacement authorized
Final Activation authorized
Legacy Retirement authorized
```

---

# 36. Final Decision

```text
F11-D09
— Visibility /
  Sensitive Data /
  Presentation Safety

DECISION:
HUMAN_APPROVED / FROZEN
```

最终冻结方向：

```text
Banyan separates Visibility from Authority.

Seeing information does not create Decision Authority,
Runtime Permission, or Apply Authority.

Decision Authority does not automatically grant unrestricted access
to all supporting data.

Visibility is context-composed and remains Scope-bound,
Purpose-sensitive, Surface-sensitive, and Policy-governed.

Restricted does not mean Unknown.
Redacted does not mean Missing.

Safe presentation may hide detail,
but must preserve material governing meaning.

Redaction, abstraction, aggregation, and AI summary
must not invent, erase, or distort Material Semantics.

AI access to backend context does not create viewer disclosure permission.

Unresolved visibility conflicts narrow disclosure rather than expand it.

If a Surface cannot safely provide minimum sufficient Decision Context,
the interaction is relocated rather than semantically degraded.

Visibility is current-applicable.
Past visibility, cached visibility, old Session state,
old Notification detail, or old Export does not establish current visibility.

Safety subsystem failure never permits raw fallback.

D04 keeps Decision meaning.
D05 keeps Reason / Blocker / Cause truth.
D06 keeps Result / Evidence / Trace / Provenance truth.
D07 keeps Attention policy.
D08 keeps multi-surface continuity.
F10 keeps Runtime Permission and Runtime Truth.

F11-D09 governs safe presentation without becoming
a second Authority domain,
a second Data Classification authority,
or a Shadow Sanitized Truth Store.

Implementation remains NOT_AUTHORIZED.
```

---

**END OF F11-D09 HUMAN_APPROVED FREEZE**

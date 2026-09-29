# F11-D05 — Reason / Blocker / Explanation Model
## 原因、阻塞与解释模型

**Stage：** F11 — Control Plane / Governance UX Architecture（控制面 / 治理交互架构）  
**Decision ID：** F11-D05

**Upstream：**
- F11-G01 = HUMAN_APPROVED / FROZEN
- F11-D01 = HUMAN_APPROVED / FROZEN
- F11-D02 = HUMAN_APPROVED / FROZEN
- F11-D03 = HUMAN_APPROVED / FROZEN
- F11-D04 = HUMAN_APPROVED / FROZEN

**Status：** HUMAN_APPROVED / FROZEN

**Implementation Authorization：** NO  
**RP2 Authorization：** NO  
**Authority Cutover Authorization：** NO  
**Canonical Replacement Authorization：** NO  
**Final Activation Authorization：** NO  
**Legacy Retirement Authorization：** NO

---

# 1. 决策目标

F11-D05 用于冻结 F11 Control Plane 中：

```text
State
Reason
Blocker
Cause
Explanation
```

之间的职责边界。

本 Decision 回答：

```text
当前状态为什么是这样？
什么条件正在真正阻止继续？
Reason 与 Error / Failure 有什么区别？
Reason 与 Blocker 有什么区别？
Immediate Cause / Contributing Cause / Root Cause 如何区分？
多个 Reason / Blocker 怎样共同表达？
Primary / Secondary Reason 如何选择？
Explanation 如何把机器事实转换成人可以理解的表达？
AI 可以解释到什么程度？
什么时候必须明确写“原因尚未确定”？
Reason / Blocker / Explanation 如何处理 Freshness？
如何区分 Current / Historical / Superseded / No Longer Applicable？
Explanation 怎样引用 Evidence / Trace / Provenance？
“为什么这样”和“接下来怎么办”分别由谁负责？
以及 F11 如何避免形成第二套 Runtime Truth / Cause Truth / Reason Truth。
```

---

# 2. 五层基本语义

F11-D05 正式采用：

```text
State
↓
Reason
↓
Blocker where applicable
↓
Cause relation where useful
↓
Explanation Projection
```

其中：

```text
State
= 当前发生什么

Reason
= 为什么当前这样

Blocker
= 当前什么条件阻止继续

Cause
= Reason / Failure / Blocker 为什么发生

Explanation
= 如何把已有事实和关系组织成人类可理解表达
```

---

# 3. State 与 Reason 分离

正式：

```text
State
!= Reason
```

例如：

```text
State:
WAITING

Reason:
DEPENDENCY_NOT_READY
```

State 表示当前处于什么状态；Reason 表示为什么处于这个状态。F11 不得使用 State Label 代替 Cause / Reason。

---

# 4. Reason 的定义

Reason 用于解释当前 Subject 为什么处于某个 State、Resolution 或 Result。

Reason 应来自：

```text
Runtime Owner
Domain Owner
Governance Owner
Gate / Decision / Dependency / Validation / other authoritative source
```

而不是由 F11 自己创造事实。

正式：

```text
Reason Presentation
!= Reason Authority
```

---

# 5. Reason 不等于 Error / Failure

正式：

```text
Reason
!= Error

Reason
!= Failure
```

例如：

```text
State:
WAITING

Reason:
Dependency B not completed
```

不是错误，也不是失败。

---

# 6. Blocker 的定义

Blocker 表示当前存在的、真正阻止 Subject 继续推进的条件。

例如：

```text
Gate G4 = HOLD
```

或：

```text
Human Decision D17 unresolved
```

Blocker 不是普通描述性原因，而是：

```text
Continuation-preventing condition
```

---

# 7. Reason 与 Blocker 分离

正式：

```text
Reason
!= Blocker
```

一个 Reason 可以存在而没有 Blocker。

---

# 8. Reason exists 不等于 Blocker exists

正式：

```text
Reason exists
!= Blocker exists
```

所有状态都可以拥有解释 Reason，但并非所有 Reason 都意味着 blocked、failed 或 user intervention。

---

# 9. Blocker 不等于 Human Action

正式：

```text
Blocker
!= Human Action Required

Blocker
!= Human Decision Required
```

例如 Dependency B incomplete 可以是 Active Blocker，但系统只需等待，不需要用户操作。

---

# 10. Human Action 与 Human Decision 分离

正式：

```text
Human Action Required
!= Human Decision Required
```

例如上传缺失证书可能是 Human Action，但没有 Material Governance Choice，因此不是 Governance Decision。

---

# 11. Immediate Reason 与 Root Cause 分离

正式：

```text
Immediate Reason
!= Root Cause
```

例如：

```text
Current State:
BLOCKED

Immediate Reason:
Gate G4 = HOLD
```

继续追问才可能发现：

```text
G4 HOLD
because Validation V8 incomplete
```

再往下：

```text
V8 required
because Scope Decision D12 expanded validation scope
```

这些属于 Cause Relation。

---

# 12. Immediate Cause

Immediate Cause 回答什么直接触发了当前 Reason、Failure 或 Blocker。

例如：

```text
Execution Attempt failed

Immediate Cause:
Provider timeout
```

Immediate Cause 不要求同时解释最底层根因。

---

# 13. Contributing Cause

当一个结果由多个因素共同促成时，允许 Contributing Cause。

例如：

```text
Immediate Cause:
Provider timeout

Contributing Cause:
Fallback binding stale
```

正式：

```text
Contributing Cause
!= Secondary Error Message
```

只有真正有因果贡献的事实才可称为 Contributing Cause。

---

# 14. Root Cause

Root Cause 只有在存在足够 Basis 时才可以声明。

正式：

```text
Root Cause Claim
requires supporting Basis.
```

不得因为 Provider timeout 就自动推断 network failure 为 Root Cause。

---

# 15. Root Cause 可以未知

正式：

```text
No Root Cause
!= No Explanation
```

允许：

```text
Known Immediate Cause
+
Unknown Root Cause
```

---

# 16. 多个 Cause 可以同时存在

正式：

```text
Multiple Contributing Causes
may coexist.
```

D05 不要求所有问题必须有 one and only one root cause。

---

# 17. Cause Relation 不强制单链

因果结构可以是 graph-shaped，而非 A → B → C。

正式：

```text
Causal Relationship
may be graph-shaped
while Presentation may be simplified.
```

---

# 18. Cause Graph 不要求全量构建

正式：

```text
Cause Graph
should be Purpose-sensitive,
not exhaustively universal.
```

只有对当前解释、恢复、治理判断、审计、诊断有实际价值的 Cause Relation 才需要保持。

---

# 19. Cause Relationship 与 Trace 分离

正式：

```text
Cause Relationship
!= Trace Sequence
```

Trace 回答实际发生过什么过程；Cause Relationship 回答哪些事实之间存在已支持的因果或贡献关系。

---

# 20. 时间先后不等于因果

正式：

```text
Temporal Precedence
!= Causal Proof
```

事件 A 先发生、B 后发生，不能仅凭时间顺序声明 A caused B。

---

# 21. Co-occurrence 不等于因果

正式：

```text
Co-occurrence
!= Causality
```

同时存在 Gate HOLD 与 Provider unavailable，不能自动解释成 Provider unavailable 导致 Gate HOLD。

---

# 22. 跨 Domain Cause 必须有来源支持

正式：

```text
Cross-domain Cause Link
must remain source-supported.
```

跨越 Decision、Scope、Validation、Gate、Runtime、Dependency 等 Domain 的因果解释，必须来自正式关系、规则、Evidence 或 Trace。

---

# 23. F11 组合 Explanation 不等于新的 Cause Authority

正式：

```text
Composed Explanation
!= Canonical Causal Truth

F11-composed Cause Graph
!= Canonical Cause Authority
```

---

# 24. Primary Reason

当同时存在多个 Reason 时，允许展示：

```text
Primary Reason
Secondary Reasons
```

Primary Reason 的作用是：对当前 Presentation Purpose，最直接解释当前状态 / Resolution / Block 的 Reason。

---

# 25. Primary Reason 是 Purpose-sensitive

正式：

```text
Primary Reason
should be Purpose-sensitive.
```

同一事实针对不同 Purpose，Primary Reason 可以不同。

---

# 26. Primary Reason 不是 Global Highest Reason

正式：

```text
Primary Reason
!= Globally Highest Reason
```

---

# 27. Primary Reason 不等于 Authority Priority

正式：

```text
Primary Presentation Reason
!= Authority Precedence
```

---

# 28. Primary Reason Selection 必须可解释

正式：

```text
Primary Reason Selection
must remain explainable and Basis-backed.
```

D05 不冻结具体评分算法。

---

# 29. Secondary Reason

正式：

```text
Secondary Reason
!= Every Observed Event
```

普通日志噪声不应被自动提升为 Secondary Reason。

---

# 30. Primary / Secondary 可以是 Presentation-derived

正式：

```text
Primary / Secondary Classification
may be Presentation-derived.
```

但 Reason Truth 仍然属于原 Domain Owner。

---

# 31. 多个 Active Blocker

一个 Subject 可以同时存在 Multiple Active Blockers。D05 不强制只保留一个 Blocker。

---

# 32. Blocker Composition

多个 Blocker 之间必须保持 Continuation Semantics。

正式：

```text
Multiple Blockers
must preserve Continuation Semantics.
```

---

# 33. Blocker Count 不等于 Continuation Logic

正式：

```text
Blocker Count
!= Continuation Logic
```

---

# 34. F11 不成为 Blocker Rule Engine

正式：

```text
Blocker Composition Presentation
!= Blocker Resolution Authority
```

实际组合逻辑应来自 Workflow、Gate、Runtime、Domain Contract。

---

# 35. Dependency 与 Blocker 分离

正式：

```text
Dependency
!= Blocker
```

Dependency 是关系事实；只有它当前真正阻止 Continuation 时，才成为 Active Blocker。

---

# 36. Governance Object 与 Active Blocker 分离

正式：

```text
Referenced Governance Object
!= Active Blocker by default.
```

---

# 37. Active Blocker 是 Contextual

正式：

```text
Active Blocker
is Contextual and Continuation-relative.
```

---

# 38. Historical Blocker

正式：

```text
Historical Blocker
!= Active Blocker
```

历史 Blocker 可进入 Trace / Audit，但不能继续作为 Current Blocker 展示。

---

# 39. 一个 Blocker 解除不等于 Subject Unblocked

正式：

```text
One Blocker Resolved
!= Subject Unblocked
```

---

# 40. Blocker Resolution Ratio 不等于 Work Progress

正式：

```text
Blocker Resolution Ratio
!= Work Completion Percentage.
```

---

# 41. Blocker Resolved 与 No Longer Applicable 分离

正式：

```text
Blocker Resolved
!= Blocker No Longer Applicable.
```

---

# 42. Reason / Blocker 不建立独立状态机

正式：

```text
Reason Lifecycle
!= Runtime Lifecycle

Blocker Lifecycle
!= Runtime Lifecycle

Explanation Lifecycle
!= Domain Lifecycle
```

---

# 43. Reason Resolution 不等于 Reason 对象状态机

正式：

```text
Reason Resolution
should not imply
a standalone Reason State Machine.
```

---

# 44. Current 与 Historical Reason

正式：

```text
Historical Reason
!= Current Reason

Historical Reason
!= Active Reason
```

---

# 45. Current 与 Historical Blocker

正式：

```text
Historical Blocker
!= Active Blocker
```

---

# 46. Superseded Explanation

正式：

```text
Superseded Explanation
!= Deleted Explanation.
```

---

# 47. Explanation Enrichment 与 Supersession 分离

正式：

```text
Explanation Enrichment
!= Reason Supersession.
```

---

# 48. Newer Evidence 不自动 Supersede

正式：

```text
Newer Evidence
!= Automatic Supersession.
```

---

# 49. Explanation No Longer Applicable

正式：

```text
Explanation No Longer Applicable
!= Human Action Completed.
```

---

# 50. Displayed Explanation 不等于 Current Truth

正式：

```text
Displayed Explanation
!= Current Explanation Truth.
```

---

# 51. Cached Explanation 不等于 Current Explanation

正式：

```text
Cached Explanation
!= Current Explanation.
```

---

# 52. Freshness 适用于 Reason / Blocker / Explanation

正式：

```text
Stale Reason Projection
!= Current Reason Truth.

Stale Explanation Basis
must not be presented
as Current Confirmed Cause.
```

---

# 53. Latest Known 与 Current Confirmed 分离

正式：

```text
Latest Known Reason
!= Current Confirmed Reason.
```

---

# 54. Mixed Freshness

正式：

```text
Explanation can contain Mixed Freshness,
but each Material Claim
must preserve its Basis semantics.
```

---

# 55. Explanation Freshness 可以 Claim-sensitive

正式：

```text
Explanation Freshness
may be Claim-sensitive.
```

---

# 56. Unknown Reason

正式：

```text
Unknown Reason
!= Runtime Failure

Unknown Reason
!= Human Decision Required.
```

---

# 57. Unknown 是合法 Explanation Outcome

正式：

```text
Unknown
is an acceptable Explanation Outcome.
```

---

# 58. Plausible Cause 与 Confirmed Cause 分离

正式：

```text
Plausible Cause
!= Confirmed Cause.
```

---

# 59. Known but Restricted 与 Unknown 分离

正式：

```text
Restricted Explanation Detail
!= Unknown Reason.
```

---

# 60. Explanation 的定义

ExplanationProjection 定义为：

> 将已有 State、Reason、Blocker、Cause、Recovery、Attention 和 supporting Basis 组织成人类可理解表达的派生 Projection。

正式：

```text
Explanation
!= New Runtime Fact

Explanation
!= New Governance Fact.
```

---

# 61. Explanation 不拥有 Authority

正式：

```text
Explanation
!= Authority.
```

---

# 62. Explanation 必须保持 Source Semantics

正式：

```text
Explanation
must preserve Source Semantics.
```

---

# 63. Human-readable Simplification 不得改变治理含义

正式：

```text
Human-readable Simplification
must preserve governing meaning.
```

---

# 64. Reason Code 与 Explanation 分离

正式：

```text
Reason Code
!= Human-readable Explanation.
```

---

# 65. Human-readable Message 不等于 Reason Identity

正式：

```text
Human-readable Message
!= Reason Identity.
```

---

# 66. AI Explanation 的允许范围

AI 可以压缩已确认事实、把 Reason Code 翻译成人话、组织多个 Domain 的已支持事实、生成不同 Surface 的表达版本、提取当前 Material Reason / Blocker。

---

# 67. AI Explanation 的禁止范围

正式：

```text
AI Explanation
may transform supported facts

but must not invent unsupported cause.
```

---

# 68. AI 不得补齐缺失治理事实

正式：

```text
AI Explanation
may compress known semantics

but must not complete
missing governance facts.
```

---

# 69. Fact / Inference / Recommendation 分离

正式：

```text
Fact
!= Inference
!= Recommendation.
```

---

# 70. Explanation Certainty 使用语义限定

正式：

```text
Explanation Certainty
should be semantically qualified,
not arbitrarily scored.
```

D05 不默认使用 AI 百分比置信度。

---

# 71. Explanation Claim 保留 Provenance Category

正式：

```text
Explanation Claim
should preserve provenance category.
```

---

# 72. Explanation 必须 Basis-backed

正式：

```text
Explanation
must remain Basis-backed.
```

---

# 73. Explanation Basis 最小充分

正式：

```text
Explanation Basis
should be Minimum Sufficient,
not Exhaustive by default.
```

---

# 74. Material Explanation Claim 必须可追踪

正式：

```text
Material Explanation Claim
should remain traceable
to supporting Basis.
```

---

# 75. Evidence / Trace / Provenance 分离

正式：

```text
Evidence
!= Trace
!= Provenance.
```

---

# 76. Explanation 不等于 Evidence

正式：

```text
Explanation
!= Evidence.
```

---

# 77. Explanation 应能链接 Evidence

正式：

```text
Explanation
should be traceable
to supporting Evidence
where such Evidence exists.
```

---

# 78. Explanation Timeline 不等于 Runtime Trace

正式：

```text
Explanation Timeline
!= Runtime Trace.
```

---

# 79. Explanation Evidence Requirement 不等于 Evidence Taxonomy Ownership

正式：

```text
Explanation Evidence Requirement
!= Evidence Taxonomy Ownership.
```

---

# 80. Multi-domain Explanation 不等于 Authority Merge

正式：

```text
Multi-domain Explanation
!= Authority Merge.
```

不得创建 GLOBAL_REASON / GLOBAL_BLOCKER 反向成为各 Domain Truth。

---

# 81. Explanation 的 Presentation Priority 不等于 Domain Priority

正式：

```text
Reason Presentation Priority
!= Domain Authority Priority.
```

---

# 82. Explanation 支持 Progressive Disclosure

正式：

```text
Explanation Detail
may expand progressively.
```

---

# 83. Explanation Depth 必须 Purpose-sensitive

正式：

```text
Explanation Depth
should be Purpose-sensitive and bounded.
```

---

# 84. Causal Completeness 不是每个界面的目标

正式：

```text
Causal Completeness
is not required
for every Presentation.
```

---

# 85. Operational Explanation 与完整 Root Cause Analysis 分离

正式：

```text
Operational Explanation
!= Full Root Cause Analysis.
```

---

# 86. State Label 不得反向生成 Cause

正式：

```text
State Label
must not be recycled
as unsupported Cause.
```

---

# 87. UI Control State 不等于 Blocker Truth

正式：

```text
UI Control State
!= Blocker Truth.
```

---

# 88. Reason 与 Next Action 分离

正式：

```text
Reason
!= Next Action.
```

---

# 89. Recovery 负责系统正在做什么

正式：

```text
Reason
!= Recovery.
```

---

# 90. Control Hint 负责用户可以发起什么 Runtime Control

正式：

```text
Explanation
cannot create Control Hint.
```

---

# 91. Human Decision Requirement 负责用户必须判断什么

正式：

```text
Explanation
may reference Human Decision Requirement

but must not become
Human Decision Interaction.
```

---

# 92. Expected Continuation

正式：

```text
Expected Continuation
!= Guaranteed Outcome.
```

---

# 93. User Action Guidance 必须有来源

正式：

```text
User Action Guidance
must be source-backed.
```

---

# 94. Control Available 不等于 User Action Required

正式：

```text
Control Available
!= User Action Required.
```

---

# 95. User Action Required 不等于 Immediate Notification

正式：

```text
User Action Required
!= Immediate Notification.
```

---

# 96. Action Guidance 信息架构

Explanation 可以组织：

```text
Current Situation
Why
Current Blocker
System Recovery
User Attention / Action Requirement
Expected Continuation
```

但这是逻辑信息结构，不是固定 DTO 或 UI Layout。

---

# 97. Current / Historical / Superseded / No Longer Applicable

D05 正式支持：

```text
Current
Historical
Superseded
No Longer Applicable
```

但不冻结 Exact Enum，也不得被误解为建立独立 Reason / Explanation 状态机。

---

# 98. Reason Lifecycle 与 Runtime Lifecycle 分离

正式：

```text
Reason Lifecycle
!= Runtime Lifecycle.
```

---

# 99. Blocker Lifecycle 与 Runtime Lifecycle 分离

正式：

```text
Blocker Lifecycle
!= Runtime Lifecycle.
```

---

# 100. Explanation Lifecycle 与 Domain Lifecycle 分离

正式：

```text
Explanation Lifecycle
!= Domain Lifecycle.
```

---

# 101. D05 不建立 Shadow Reason Store

正式：

```text
Reason Presentation Model
!= Shadow Reason Store.
```

---

# 102. Explanation Presentation 不要求全部永久持久化

正式：

```text
Explanation Presentation
!= Mandatory Durable Record.
```

---

# 103. 某些 Explanation 可以有审计价值

正式：

```text
Some Explanation Artifacts
may be audit-relevant

without making every Explanation
a canonical persistent object.
```

---

# 104. Explanation 与 Attention 分离

D05 负责为什么当前需要或不需要关注；D07 负责何时提醒、提醒到哪里、提醒多少次、是否去重、是否升级、是否聚合。

---

# 105. Reason Severity 不等于 Attention Urgency

正式：

```text
Reason Severity
!= Attention Urgency.
```

---

# 106. Technical Severity 不等于 Human Attention Priority

正式：

```text
Technical Severity
!= Human Attention Priority.
```

---

# 107. Blocker Exists 不等于 Notify Human

正式：

```text
Blocker Exists
!= Notify Human.
```

---

# 108. D05 与 D07 的责任边界

正式：

```text
Reason / Blocker semantics
!= Attention Governance.
```

---

# 109. Explanation 与 Presentation Safety

D05 要求 Explanation accurate / understandable / materially sufficient；D09 决定当前身份 / Scope / Surface 能看多少 Detail。

---

# 110. Explanation Truthfulness 不要求暴露原始敏感细节

正式：

```text
Explanation Truthfulness
!= Raw Sensitive Detail Exposure.
```

---

# 111. Safety Redaction 必须保留治理意义

正式：

```text
Presentation Safety Redaction
must preserve necessary governing meaning.
```

---

# 112. Redaction 不得替换成错误 Cause

正式：

```text
Redaction
must not substitute
a false explanation.
```

---

# 113. Visibility Difference 不等于 Reason Truth Difference

正式：

```text
Visibility Difference
!= Reason Truth Difference.
```

---

# 114. Safety-filtered Explanation 可不同密度

正式：

```text
Safety-filtered Explanation
may differ in detail

but not in governing meaning.
```

---

# 115. Restricted Reason 不等于 Unknown Reason

正式：

```text
Restricted Explanation Detail
!= Unknown Reason.
```

---

# 116. 跨 Surface Explanation

正式：

```text
Explanation Wording
may vary by Surface.

Explanation Density
may vary by Surface.

Explanation Meaning
may not diverge.
```

---

# 117. Human Explanation 可以抽象实现细节

正式：

```text
Human Explanation
may abstract implementation detail

but must not alter governing meaning.
```

---

# 118. Explanation Relevance

正式：

```text
Explanation Relevance
should follow
current user / governance purpose.
```

---

# 119. Reason / Blocker / Explanation Responsibility Flow

F11-D05 正式采用：

```text
1. Observe
   Obtain current Subject State / Resolution

2. Resolve
   Obtain owner-backed:
   Reason
   Blocker
   Cause
   Recovery semantics

3. Classify for Presentation
   Current / Historical
   Active / No Longer Applicable
   Primary / Secondary
   Fact / Inference
   Attention relevance

4. Compose
   Build Minimum Sufficient
   Human-readable Explanation

5. Qualify
   Preserve:
   Basis
   Freshness
   Certainty
   Provenance category
   visibility restrictions

6. Guide
   Reference only valid:
   Recovery
   Control Hint
   Human Decision Requirement
   Human Action Requirement
   Expected Continuation

7. Drill Down
   Link:
   Evidence
   Trace
   Provenance

8. Refresh
   Converge Explanation
   back to Current
   authoritative projections
```

该模型是责任模型，不是固定 API 或 Workflow。

---

# 120. F11-D05 核心不变量

正式冻结：

```text
State
!= Reason

Reason
!= Blocker

Reason
!= Error

Reason
!= Failure

Reason exists
!= Blocker exists

Blocker
!= Human Action Required

Blocker
!= Human Decision Required

Human Action Required
!= Human Decision Required

Immediate Reason
!= Root Cause

No Root Cause
!= No Explanation

Multiple Contributing Causes
may coexist

Primary Reason
should be Purpose-sensitive

Primary Reason
!= Globally Highest Reason

Primary Presentation Reason
!= Authority Precedence

Primary Reason Selection
must remain explainable
and Basis-backed

Secondary Reason
!= Every Observed Event

Primary / Secondary Classification
may be Presentation-derived

Multiple Blockers
must preserve Continuation Semantics

Blocker Count
!= Continuation Logic

Blocker Composition Presentation
!= Blocker Resolution Authority

Dependency
!= Blocker

Referenced Governance Object
!= Active Blocker by default

Active Blocker
is Contextual
and Continuation-relative

Historical Blocker
!= Active Blocker

One Blocker Resolved
!= Subject Unblocked

Blocker Resolution Ratio
!= Work Completion Percentage

Blocker Resolved
!= Blocker No Longer Applicable

Contributing Cause
!= Secondary Error Message

Root Cause Claim
requires supporting Basis

Known Immediate Cause
may coexist with Unknown Root Cause

Cause Graph
should be Purpose-sensitive,
not exhaustively universal

Cause Relationship
!= Trace Sequence

Temporal Precedence
!= Causal Proof

Co-occurrence
!= Causality

Cross-domain Cause Link
must remain source-supported

Composed Explanation
!= Canonical Causal Truth

Historical Reason
!= Current Reason

Historical Reason
!= Active Reason

Stale Reason Projection
!= Current Reason Truth

Latest Known Reason
!= Current Confirmed Reason

Unknown Reason
!= Runtime Failure

Unknown Reason
!= Human Decision Required

Unknown
is an acceptable Explanation Outcome

Plausible Cause
!= Confirmed Cause

Restricted Explanation Detail
!= Unknown Reason

Explanation
!= New Runtime Fact

Explanation
!= New Governance Fact

Explanation
!= Authority

AI Explanation
may transform supported facts
but must not invent unsupported cause

AI Explanation
may compress known semantics
but must not complete
missing governance facts

Fact
!= Inference
!= Recommendation

Explanation
must preserve Source Semantics

Human-readable Simplification
must preserve governing meaning

Explanation
must remain Basis-backed

Explanation Claim
should preserve provenance category

Explanation Basis
should be Minimum Sufficient,
not Exhaustive by default

Material Explanation Claim
should remain traceable
to supporting Basis

Evidence
!= Trace
!= Provenance

Explanation
!= Evidence

Explanation Timeline
!= Runtime Trace

Explanation Evidence Requirement
!= Evidence Taxonomy Ownership

Reason Code
!= Human-readable Explanation

Human-readable Message
!= Reason Identity

Explanation Certainty
should be semantically qualified,
not arbitrarily scored

Stale Explanation Basis
must not be presented
as Current Confirmed Cause

Explanation can contain Mixed Freshness,
but each Material Claim
must preserve its Basis semantics

Explanation Freshness
may be Claim-sensitive

Explanation Depth
should be Purpose-sensitive and bounded

Causal Completeness
is not required
for every Presentation

Operational Explanation
!= Full Root Cause Analysis

State Label
must not be recycled
as unsupported Cause

UI Control State
!= Blocker Truth

Reason
!= Next Action

Reason
!= Recovery

Explanation
cannot create Control Hint

Explanation
may reference Human Decision Requirement
but must not become
Human Decision Interaction

Expected Continuation
!= Guaranteed Outcome

User Action Guidance
must be source-backed

Control Available
!= User Action Required

User Action Required
!= Immediate Notification

Reason Lifecycle
!= Runtime Lifecycle

Blocker Lifecycle
!= Runtime Lifecycle

Explanation Lifecycle
!= Domain Lifecycle

Reason Resolution
should not imply
a standalone Reason State Machine

Superseded Explanation
!= Deleted Explanation

Explanation Enrichment
!= Reason Supersession

Newer Evidence
!= Automatic Supersession

Explanation No Longer Applicable
!= Human Action Completed

Displayed Explanation
!= Current Explanation Truth

Cached Explanation
!= Current Explanation

Multi-domain Explanation
!= Authority Merge

Reason Presentation Priority
!= Domain Authority Priority

Reason Severity
!= Attention Urgency

Technical Severity
!= Human Attention Priority

Blocker Exists
!= Notify Human

Explanation Truthfulness
!= Raw Sensitive Detail Exposure

Presentation Safety Redaction
must preserve necessary governing meaning

Redaction
must not substitute
a false explanation

Visibility Difference
!= Reason Truth Difference

Safety-filtered Explanation
may differ in detail
but not in governing meaning

Explanation Presentation
!= Mandatory Durable Record

Reason Presentation Model
!= Shadow Reason Store

Explanation Wording
may vary by Surface

Explanation Density
may vary by Surface

Explanation Meaning
may not diverge

Human Explanation
may abstract implementation detail
but must not alter governing meaning
```

---

# 121. Explicitly Forbidden Designs

F11-D05 明确禁止把以下方式提升为正式架构：

```text
State = Reason
Reason = Error
Reason = Failure
Reason = Blocker
Blocker = Human Decision Requirement
Blocker = User responsibility
Reason list first item = Primary Reason
Most severe-looking event = Primary Reason
Trace order = Causal proof
Earlier event = Root cause
Concurrent events = Causal relation
Any Provider failure = Root cause
Unknown cause = Ask user
Unknown reason = Runtime failure
UI Retry disabled = Permission denied blocker
Human-readable text = Reason identity
AI guess = Confirmed cause
AI summary = New runtime fact
AI explanation = Authority
Recommendation = Reason
Reason = User action
Provider timeout = Automatic Retry instruction
Explanation = Control Hint
Explanation = Human Decision Interaction
One blocker resolved = Subject unblocked
All blocker counts = Work progress
Historical blocker = Current blocker
Cached explanation = Current explanation
Old explanation = Current truth after reconnect
New evidence = Automatically supersede old reason
Every explanation = Persistent canonical object
F11 reason model = Shadow runtime truth store
Every cause relation = Full global cause graph
Raw sensitive data = Required explanation detail
Redaction = Replace actual cause with unrelated generic error
Notification = Blocker resolution
Reason severity = Notification priority
```

---

# 122. Deferred

F11-D05 明确暂缓：

```text
Exact Reason Enum
Exact Blocker Enum
Exact Cause Enum
Exact Primary / Secondary Enum
Exact Active / Historical Enum
Exact Superseded Enum
Exact Blocker Composition Enum
Exact Blocker Expression Language
Exact Cause Graph Schema
Exact Root Cause Algorithm
Exact Reason Priority Algorithm
Exact Explanation Certainty Enum
AI Confidence Percentage
Exact Explanation Text Template
Exact Localization Model
Exact Reason Stable ID Model
Exact Reason Persistence Model
Exact Explanation Persistence Model
Exact Evidence Taxonomy
Exact Trace Schema
Exact Provenance Schema
Exact Notification Priority
Exact Attention Policy
Exact Sensitive-data Redaction Rules
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

# 123. D05 与 D06 的边界

D05 负责：

```text
Reason semantics
Blocker semantics
Cause semantics
Explanation claims
Basis / Freshness requirements
Explanation-to-Evidence linkage requirement
```

D06 负责：

```text
Result Presentation
Evidence Presentation
Trace Presentation
Provenance Navigation
Timeline
Drill-down
Evidence / Trace / Provenance UX
```

正式：

```text
D05 requires Explanation supportability.

D06 owns rich Evidence / Trace /
Provenance Presentation.
```

---

# 124. D05 与 D07 的边界

D05 负责 why attention may be needed。

D07 负责：

```text
when to notify
how to notify
where to notify
priority
deduplication
reminder
escalation
inbox behavior
```

正式：

```text
Reason / Blocker semantics
!= Attention Governance.
```

---

# 125. D05 与 D09 的边界

D05 负责：

```text
Explanation accuracy
Explanation sufficiency
governing meaning preservation
```

D09 负责：

```text
Visibility
Sensitive Data
Scope-based Presentation Safety
Redaction rules
```

正式：

```text
D09 may reduce visible detail.

D09 may not alter
the underlying governing meaning.
```

---

# 126. Approval Effect

本稿已经明确：

```text
F11-D05 HUMAN_APPROVED
```

因此正式冻结：

```text
State / Reason / Blocker /
Cause / Explanation separation

Reason Authority boundary

Reason / Error / Failure separation

Active Blocker semantics

Human Action /
Human Decision separation

Immediate / Contributing /
Root Cause boundaries

Optional Purpose-sensitive Cause Graph

Primary / Secondary Reason semantics

Multiple Blocker composition preservation

Current / Historical semantics

Resolved /
No Longer Applicable separation

Superseded Explanation semantics

Unknown / Restricted Reason semantics

Basis / Freshness requirements

Fact / Inference /
Recommendation separation

AI Explanation boundary

Cross-domain Explanation boundary

Explanation Certainty semantics

Explanation-to-Evidence /
Trace / Provenance linkage requirement

Reason /
Recovery /
Control Hint /
Decision Requirement /
Human Action separation

Expected Continuation boundary

User Action Guidance source requirement

Attention boundary

Presentation Safety boundary

Cross-surface semantic consistency

No Shadow Reason / Cause Truth Store
```

但不代表：

```text
Exact Reason Enum frozen
Exact Cause Graph frozen
Root Cause Algorithm frozen
Risk / severity model frozen
Evidence taxonomy frozen
Trace schema frozen
Provenance schema frozen
Notification policy frozen
Sensitive data redaction implementation frozen
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

# 127. Final Frozen Decision

```text
F11-D05
— Reason / Blocker / Explanation Model

STATUS:
HUMAN_APPROVED / FROZEN

Banyan keeps State,
Reason,
Blocker,
Cause,
and Explanation
semantically separate.

State tells what is happening.

Reason explains why.

Blocker identifies a current
continuation-preventing condition.

Cause explains supported causal
or contributing relationships.

Explanation transforms supported
semantics into human-understandable form
without becoming a new source of truth.

Reason is not Error.

Reason is not Failure.

Reason is not automatically Blocker.

Blocker is not automatically
Human Action or Human Decision.

Multiple Reasons and Blockers
may coexist.

Primary Reason is purpose-sensitive,
Basis-backed,
and does not establish Authority precedence.

Multiple Blockers preserve
their real continuation semantics.

Cause may be graph-shaped,
but causal completeness is not required
for every interaction.

Temporal order and co-occurrence
do not prove causality.

Unknown Root Cause is legitimate.

AI may summarize supported facts,
but must not invent missing causes,
governance facts,
Control Hints,
Human Decisions,
or user responsibilities.

Fact,
Inference,
and Recommendation
remain distinct.

Material Explanation Claims
remain Basis-backed,
Freshness-aware,
and traceable.

Historical Reason
is not Current Reason.

Historical Blocker
is not Active Blocker.

Cached Explanation
is not Current Explanation.

Superseded Explanation
is preserved where audit matters
rather than silently rewritten.

Reason does not decide
what the user should do.

Recovery explains
what the system is doing.

Control Hint explains
what runtime control may be requested.

Human Decision Requirement explains
what governance judgment is required.

Human Action Requirement
is separate from Human Decision.

Expected Continuation
is not a guaranteed outcome.

F11 may compose explanations
across domains,
but does not merge their Authorities
or create new causal truth.

Explanation can vary in wording
and detail across Surfaces,
but not in governing meaning.

Presentation Safety may reduce detail,
but cannot replace the real explanation
with a false one.

F11 does not create
a shadow Reason / Cause truth store.

Implementation remains NOT_AUTHORIZED.
```

---

**END OF F11-D05 HUMAN_APPROVED FREEZE**

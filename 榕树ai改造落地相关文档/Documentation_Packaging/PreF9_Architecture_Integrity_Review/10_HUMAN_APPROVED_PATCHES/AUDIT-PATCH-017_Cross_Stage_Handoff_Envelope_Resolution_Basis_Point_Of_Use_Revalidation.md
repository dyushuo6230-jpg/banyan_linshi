# AUDIT-PATCH-017 — Cross-stage Handoff Envelope × Resolution Basis Continuity × Governance-critical Qualifier Preservation × Point-of-use Revalidation Boundary

> Formal Audit Patch ID: `AUDIT-PATCH-017`  
> Source Finding: `FCR-CHAIN-01`  
> Source Approval ID: `FCR-PATCH-01`  
> Status: `HUMAN_APPROVED`  
> Review: `Final Cross-stage Review`  
> Classification: `GAP / P1`  
> Primary Scope: `F4～F8 + Future F9/F10 Cross-stage Consumption`  
> Reuses: `AUDIT-PATCH-003 / 007 / 008 / 011 / 014 / 016`  
> Implementation Authorization: `NO`

---

## 1. Problem

Banyan 已存在多种合法 Cross-stage Handoff：

```text
Workflow Handoff
Development Entry Handoff
Product → Design Semantic Link
Change / Apply Handoff
State Projection
Project Runtime Handoff
Deferred Handoff
```

这些局部合同本身大体正确，但缺少一份 Banyan-wide 公共合同来保证：

> 跨阶段交接在压缩上下文时，不得丢失决定结果是否合法、适用于何 Scope、基于何 Authority、是否仍 Current/Fresh 的治理关键限定。

如果上游：

```text
Development Entry = AUTHORIZED
Scope = tenant-admin
Authority Basis = Human Decision X
Freshness = CURRENT
```

而下游只得到：

```text
AUTHORIZED
```

则 Scope / Authority Basis / Freshness 已丢失，可能形成：

```text
old authorization
+
new context
→ unsafe continuation
```

---

## 2. Existing Contract Preserved

本 Patch 不重建既有 Handoff 机制。

保留：

```text
F4 Typed Handoff
AUDIT-PATCH-007 Development Entry Handoff
AUDIT-PATCH-008 Freshness / Re-resolution
AUDIT-PATCH-011 Product / Design Typed Semantic Linkage
AUDIT-PATCH-014 Typed State Projection
AUDIT-PATCH-016 Deferred Handoff
F7 Final Pre-mutation Guard
F8 Task-scoped Minimum Sufficient Runtime Handoff
```

只补：

```text
Common Cross-stage Handoff Integrity Contract
```

---

## 3. Core Principle

正式：

```text
Cross-stage Handoff
must preserve
all governance-critical qualifiers
required to interpret the handed-off result safely.
```

---

## 4. Minimum Sufficient Boundary

正式：

```text
Minimum Sufficient
!= Governance-incomplete

Context Compression
!= Governance Compression

Handoff Projection
!= Semantic Downgrade
```

可以少传无关上下文，但不能少传会改变合法解释的治理含义。

---

## 5. Common Logical Handoff Envelope

逻辑上采用：

```text
CrossStageHandoffEnvelope
```

它不是新的 F1 Top-level Object、DefinitionArtifact、Canonical Truth 或 Global Authority。

Material Handoff 至少应能解释：

```text
What is being handed off?
Who produced it?
Who consumes it?
For what purpose?
For what Semantic Subject / Target?
For what Scope?
Under what Context?
Based on what governed facts?
Based on what Authority?
Based on what Revision / Version?
What is the Freshness / Current Effective basis?
Are UNKNOWN / HOLD / BLOCKED / STALE present?
What must downstream still validate?
What invalidates / re-resolves this handoff?
```

---

## 6. Logical Structure

```text
CrossStageHandoffEnvelope
=
Handoff Purpose
+ Source Owner
+ Target Consumer
+ Semantic Subject / Target
+ Scope
+ Context
+ Typed Payload
+ Authority / Governance References
+ Resolution Basis
+ Revision / Version Basis
+ Freshness / Applicability
+ State / Gate / Decision Qualifiers
+ Blockers / Unknowns / Holds
+ Provenance
+ Downstream Required Inputs
+ Downstream Obligations
+ Invalidation / Re-resolution Conditions
```

Exact schema deferred。

---

## 7. Purpose-sensitive Minimum Sufficient

正式：

```text
Handoff Envelope
= Purpose-sensitive Minimum Sufficient Contract
```

不要求 every handoff 携带所有字段。

字段按：

```text
Purpose
Scope
Applicability
Consumer Need
Governance Requirement
```

决定。

---

## 8. Governance-critical Qualifier

逻辑上定义：

```text
Governance-critical Qualifier
```

即：

> 一旦丢失，就可能导致 Consumer 错误解释合法范围、Authority、Freshness、状态或可执行性的限定。

典型包括：

```text
Scope
Authority Basis
Authorization Envelope
Applicability
Freshness
Revision / Version Basis
Current Effective Basis
Gate Result
HOLD
BLOCKED
UNKNOWN
STALE
Expiry / Validity Condition
Deferred Guard
Material Downstream Obligation
```

Exact taxonomy deferred。

---

## 9. Result / Qualifier Boundary

正式：

```text
Result without required qualifiers
!= Same Semantic Result
```

例如：

```text
AUTHORIZED
```

脱离：

```text
Scope = tenant-admin only
```

后，不再等价于原 Authorization。

---

## 10. Scope Preservation

正式：

```text
Scoped Result
must remain scope-interpretable downstream
```

禁止：

```text
tenant-admin AUTHORIZED
→ handoff compression
→ AUTHORIZED
→ platform-admin also executed
```

Scope Projection 可以收窄，但不能静默扩大。

继续：

```text
Impact Discovery
!= Scope Expansion Authorization
```

---

## 11. Authority Basis Preservation

如果 Result 的合法性依赖：

```text
Human Decision
Policy Grant
Apply Authorization
Governed Exception
```

则其 Authority Basis 必须可追踪。

正式：

```text
Authority Reference
!= Authority Transfer
```

且：

```text
Authority Reference Exists
!= Authority Still Applicable
```

仍需结合：

```text
Scope
Validity
Supersession
Revocation
Context
```

判断。

---

## 12. Decision Evidence Boundary

继续：

```text
Decision Evidence
!= Apply Authorization
!= Runtime Permission
```

Handoff 不得因为传递 Decision Evidence 就提升其治理层级。

---

## 13. Revision / Version / Current Effective Basis

如果 Result 基于：

```text
Revision R7
Version 3.1
```

生成，Consumer 必须能够恢复其 Material Resolution Basis。

正式：

```text
Current Effective Handoff
!= Eternal Effective Truth
```

Current Effective 仍然只是：

```text
Scope / Context-aware Derived Resolution Result
```

---

## 14. Freshness Preservation

若 Consumer 的合法执行依赖 Result 仍 Current，则 Freshness Basis 必须保持可验证。

正式：

```text
Freshness Evidence
!= Authority

Required Freshness Context Missing
→ Consumer may not assume CURRENT
```

---

## 15. State / Blocker Preservation

正式：

```text
Upstream STALE
cannot silently become CURRENT

UNKNOWN
cannot become ABSENT / FALSE / PASS by projection

BLOCKED
cannot disappear during handoff

HOLD
cannot disappear during handoff
```

若适用：

```text
Deferred Guard
must remain effective downstream
```

---

## 16. Compression Rule

正式：

```text
Compression may remove irrelevant data,
but may not remove a qualifier
whose absence can change legal interpretation.
```

---

## 17. Evidence Projection / Provenance

不要求复制整个 Evidence Body。

可以保留：

```text
Evidence Ref
Evidence Type
Relevant Claim
Provenance
```

正式：

```text
Handoff Integrity
!= Full Evidence Duplication

Provenance
!= Authority
```

但跨阶段必须能够回答：

```text
Why did this Consumer believe this Result?
```

---

## 18. Source Owner / Target Consumer / Purpose

Material Handoff 应能识别：

```text
Source Owner
Target Consumer
Handoff Purpose
```

正式：

```text
Source Owner != Consumer Owner
```

Handoff Purpose 示例：

```text
VALIDATION_INPUT
DEVELOPMENT_ENTRY
APPLY_INPUT
RUNTIME_EXECUTION
IMPACT_REEVALUATION
DEFERRED_OBLIGATION
```

Exact enum deferred。

正式：

```text
Same Payload
+
Different Handoff Purpose
!= Same Authorization
```

---

## 19. Handoff Accepted != Eternal Validity

正式：

```text
Handoff Accepted
!= Handoff Basis Remains Valid Forever
```

---

## 20. Point-of-use Revalidation Boundary

正式引入：

```text
Point-of-use Revalidation Boundary
```

含义：

> 在真正使用跨阶段 Derived / Authorized Result 执行受保护动作之前，如果其合法性依赖可能已变化的条件，应确认这些条件仍适用。

---

## 21. Point-of-use Revalidation != Full Re-resolution

正式：

```text
Point-of-use Revalidation
!= Recompute Entire Architecture Every Time
```

只验证相关 volatile prerequisites，例如：

```text
Authority validity
Authorization envelope
Scope
Expected Base
Freshness
Current Effective dependency
Gate state
Provider compatibility
Deferred Guard
```

按 Applicability 执行。

Immutable / revision-pinned / already-proven-stable basis 不需要重复全量解析。

---

## 22. F7 Existing Guard Reused

F7 已拥有：

```text
Exact Plan Revision
Authorization Ref
Observed Expected Base
Final Pre-mutation Guard
```

这是 Canonical Apply Domain 的高质量 Point-of-use Revalidation。

本 Patch：

```text
REUSE
```

不重建。

---

## 23. F10 Future Consumption

未来 F10 应消费：

```text
Task-scoped Runtime Handoff
+
Runtime Permission
+
Applicable Current Preconditions
```

受保护执行时这些条件必须仍合法。

但：

```text
F10 Revalidation
!= Product Authority
!= Design Authority
!= Binding Authority
!= Change Authority
```

---

## 24. Point-of-use Mismatch

若发现：

```text
STALE
MISMATCH
AUTHORITY_EXPIRED
SCOPE_CHANGED
GATE_CHANGED
```

正确：

```text
Pause affected action
→ Capture Evidence
→ Route Domain Owner
→ Re-resolution
```

正式：

```text
Point-of-use Mismatch
!= Canonical Mutation Authority
```

---

## 25. Automatic Revalidation / Re-resolution

若 deterministic check 得到：

```text
STILL_VALID
```

则：

```text
Automatic Continue
```

不需要人工。

若变化可在不扩大 Scope / Authority、不产生 Material Semantic Choice 的情况下确定性 re-resolve，则复用 `AUDIT-PATCH-008` 自动处理。

正式：

```text
Revalidation Failure
!= Human Decision Required
```

先分类：

```text
STALE
UNKNOWN
BLOCKED
CONFLICTED
```

只有真正的 Material Semantic Choice / Authority Conflict / Material Scope Expansion / Multiple Legitimate Incompatible Choices 才进入既有 Informed Decision。

---

## 26. Handoff Chain Continuity

一次任务可能经过：

```text
F5
→ F6
→ F7
→ F8
→ F10
```

不要求每跳复制全部历史。

但正式要求：

```text
Downstream Result
can trace the material basis
on which its legality depends.
```

---

## 27. Handoff Order / Authority Boundary

正式：

```text
Handoff Order
!= Authority Priority

Later Consumer
!= Higher Authority

Handoff Dependency
!= Fixed Runtime Call Order
```

后阶段离 Runtime 更近，不代表 Authority 更高。

---

## 28. Multi-source Handoff Composition

Consumer 可能同时消费：

```text
F5 Product State
F6 Design State
F7 Apply Authorization
F8 Binding / Gate
F9 Freshness Evidence
```

这些输入形成：

```text
Consumer-specific Effective Resolution Context
```

正式：

```text
Effective Resolution Context
!= Canonical Truth
```

---

## 29. Contradictory Inputs

例如：

```text
F7 Apply Authorization = VALID
F8 Gate = HOLD
```

不得因为早期 Authorization 存在就继续。

继续：

```text
One Positive Result
!= Override Another Blocking Gate / State
```

---

## 30. Composition Boundary

正式：

```text
Handoff Composition
!= State-domain Merge

Handoff Composition
!= Authority Merge

Multiple Authority References
!= New Combined Authority
```

---

## 31. Missing Required Input

如果 Consumer 所需的 Material Handoff Qualifier 缺失：

```text
→ UNKNOWN / UNRESOLVED
```

正式：

```text
Missing Required Handoff Qualifier
!= PASS
```

AI 不得补猜。

---

## 32. Legacy Compatibility

Legacy Handoff 可能只有：

```text
approved = true
```

必须进一步判断：

```text
approved for what?
scope?
authority?
freshness?
purpose?
```

无法唯一恢复时：

```text
UNKNOWN / UNRESOLVED MAPPING
```

不要求一次性全量迁移；允许 active-scope / change-triggered / runtime-triggered / risk-driven 治理。

---

## 33. No Global Handoff Authority

禁止：

```text
GlobalHandoffAuthority
UniversalHandoffResolver
```

正确架构：

```text
Common Handoff Integrity Contract
+
Domain-owned Payload Semantics
+
Consumer-specific Resolution
```

---

## 34. Owner Boundary

### F4

继续负责 Workflow-level Handoff Coordination，不拥有所有 Payload Semantic Authority。

### F5

继续负责 Product / Requirement / Approval / Readiness / Development Entry semantics。

### F6

继续负责 Design / UI / Validation / Repair semantics。

### F7

继续负责 Change / Apply / Apply Authorization / Canonical Mutation semantics。

### F8

继续负责 Project Instance / Binding / Provider / Version / Feature / Gate / Effective Project Context 与 Task-scoped Runtime Handoff。

### F9

未来提供 Handoff provenance / Basis refs / Freshness / Dependency / Impact lookup。

但：

```text
Index != Handoff Authority
```

### F10

未来负责 consume / applicable prerequisite validation / execute / mismatch evidence。

但：

```text
Runtime Executor != Semantic Decision Authority
```

---

## 35. Trace Boundary

Trace 可以记录：

```text
Handoff Chain
Resolution Basis
Consumer Result
```

但：

```text
Trace != Authority
```

---

## 36. Performance / Token Boundary

正确：

```text
Current Action
→ Required Handoff Qualifiers only
→ Targeted Revalidation
→ Execute / Re-resolve
```

不是：

```text
every action
→ full repository scan
→ full architecture reload
```

继续：

```text
TOKEN_EFFICIENCY_MUST_NOT_REDUCE_GOVERNANCE_FIDELITY
```

因此：

```text
Less Context = allowed
Less Governing Meaning = forbidden
```

---

## 37. Banyan-wide Invariants

```text
Cross-stage Handoff
must preserve governance-critical qualifiers

Minimum Sufficient
!= Governance-incomplete

Context Compression
!= Governance Compression

Handoff Projection
!= Semantic Downgrade

Result without required qualifiers
!= Same Semantic Result

Scoped Result
must remain scope-interpretable downstream

Authority Ref
!= Authority Transfer

Decision Evidence
!= Apply Authorization
!= Runtime Permission

Current Effective Handoff
!= Eternal Effective Truth

Upstream STALE
cannot silently become CURRENT

UNKNOWN
cannot become ABSENT / FALSE / PASS by projection

BLOCKED
cannot disappear during handoff

HOLD
cannot disappear during handoff

Deferred Guard
must remain effective when applicable

Handoff Accepted
!= Basis Valid Forever

Point-of-use Revalidation
!= Full Re-resolution Every Time

Point-of-use Mismatch
!= Mutation Authority

Revalidation Failure
!= Human Decision Required

Handoff Order
!= Authority Priority

Later Consumer
!= Higher Authority

Handoff Composition
!= State-domain Merge

Handoff Composition
!= Authority Merge

Missing Required Qualifier
!= PASS

Effective Resolution Context
!= Canonical Truth

Index
!= Handoff Authority

Trace
!= Handoff Authority
```

---

## 38. Forbidden Interpretations

禁止：

1. Minimum Sufficient Context = 可以删除 Scope；
2. Handoff 只传 Result、不传必要 Qualifier；
3. AUTHORIZED 可脱离 Authorization Envelope 使用；
4. Decision Evidence 自动升级为 Apply Authorization；
5. Authority Ref 自动转移 Authority；
6. Upstream STALE 在下游继续当 CURRENT；
7. UNKNOWN 因字段缺失自动变成 FALSE / PASS；
8. BLOCKED 因 Handoff 压缩消失；
9. HOLD 因 Stage 前进自动消失；
10. Deferred Guard 在 Handoff 后失效；
11. Current Effective Result 永久有效；
12. Runtime 无限复用旧 Handoff；
13. Point-of-use Revalidation = 每次全仓重算；
14. F10 Revalidation 获得 Product / Design / Binding Authority；
15. Mismatch 自动修改 Canonical Truth；
16. Revalidation Failure 自动要求人工；
17. 多个 Authority Ref 合成更高 Authority；
18. Later Stage 自动获得更高 Authority；
19. Handoff Order = Governance Priority；
20. Missing Qualifier = Default PASS；
21. Trace / Index 成为 Handoff Truth；
22. 建立 Global Handoff God Object；
23. 本 Patch 提前冻结 F10 Runtime API；
24. 本 Patch授权 Implementation / RP2 / Authority Cutover / Final Activation / Legacy Retirement。

---

## 39. Deferred

本 Patch 不冻结：

```text
Exact Handoff Schema
Envelope Physical Representation
Field Names
Serialization
Handoff ID Format
Correlation ID Format
Runtime Token Format
Cache Representation
Validity TTL
Fingerprint Algorithm
Revision Comparison Algorithm
F9 Index Schema
F10 Runtime API
Message Bus
Event Bus
RPC Transport
Database Tables
```

---

## 40. Integration / No-loss

本 Patch 不 Supersede：

```text
AUDIT-PATCH-007
AUDIT-PATCH-008
AUDIT-PATCH-011
AUDIT-PATCH-014
AUDIT-PATCH-016
```

而是 cross-stage normalize / compose with 它们。

F1～F8 v1.0 Original Frozen Baseline 保持不变。

未来在 F1～F8 v1.1 Consolidated Candidate 中作为：

```text
Cross-stage Handoff Integrity
```

公共治理合同吸收。

---

## 41. Human Decision

用户明确：

```text
FCR-PATCH-01 HUMAN_APPROVED
```

因此：

```text
FCR-PATCH-01 = HUMAN_APPROVED
FCR-CHAIN-01 = ARCHITECTURALLY_RESOLVED
AUDIT-PATCH-017 = HUMAN_APPROVED
```

---

## 42. Authorization Boundary

继续：

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

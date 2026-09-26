# AUDIT-PATCH-014 — Typed State Domain Identity × Cross-stage State Projection × Transition / Re-resolution Boundary

> Formal Audit Patch ID: `AUDIT-PATCH-014`  
> Source Finding: `B5-CHAIN-01`  
> Source Approval ID: `B5-PATCH-01`  
> Status: `HUMAN_APPROVED`  
> Audit Batch: `Audit Batch 5 — Cross-stage State / Exception Semantics`  
> Classification: `GAP / P1`  
> Primary Scope: `F1～F8 Cross-stage State Semantics`  
> Primary Owners: `Each State Domain Owner`  
> Cross-stage Coordination: `F4 / F7 / F8`  
> Reuses: `AUDIT-PATCH-003 / AUDIT-PATCH-007 / AUDIT-PATCH-008 / AUDIT-PATCH-013`  
> Implementation Authorization: `NO`

---

## 1. Problem

F1～F8 已分别冻结：

```text
State Domains Remain Separate
StateModelDefinition != RuntimeState
status_domains_typed = true
```

并形成了 Product / Approval / Readiness / Development Entry / UI / Validation / Change / Apply / Project / Gate / Runtime 等多个合法状态域。

缺口在于：Banyan 尚缺少一个跨阶段共同合同，明确不同 State Domain 如何被唯一识别、如何携带相同 State Label 而不混义、如何跨阶段投影、如何失效、如何重新解析，以及 State Consumer 与 State Owner 的边界。

若缺少该合同，未来实现可能退化成模糊的全局：

```text
status = READY
status = BLOCKED
status = CURRENT
```

从而破坏 `State Domains Remain Separate`。

---

## 2. Existing Contract Preserved

继续保留：

```text
F1: State Domains Remain Separate
F2: status_domains_typed = true
F3: StateModelDefinition != RuntimeState
F4: Handoff may carry decision state / blockers / unknowns / validation state
F5: Lifecycle != Approval != Development Readiness != Development Entry != Freshness
F6: Effective State != Authority Fact
F7: Attempt Result != Apply Result != Change Result
F7: Closed != Archived
F7: Stale != Invalid
F8: Gate Definition != Gate Result
F8: Gate PASS != Authority
F8: Drift != Conflict != Error != Change Case
```

本 Patch 不建立新的全局 State Machine，也不提前冻结完整 Exception / Error / Recovery taxonomy。

---

## 3. Typed State Result

重要 State Result 至少必须逻辑上可识别：

```text
Semantic Subject
+ State Domain
+ State Dimension
+ State Value
+ Scope / Context
+ State Basis / Provenance
+ Owner
```

即：

```text
TypedStateResult
=
Subject
+ StateDomain
+ StateDimension
+ StateValue
+ Scope
+ Context
+ ResolutionBasis
+ Provenance
+ Owner
```

本 Patch 不冻结 exact physical schema。

---

## 4. State Domain

State Domain 表示拥有共同语义、合法转换边界、解析依据与 Owner 的状态空间。

正式：

```text
State Domain != Stage
One Semantic Subject != One Global Status
State Domain != Mandatory Finite State Machine
```

同一 Subject 可以同时拥有多个彼此独立的 State Dimension。

例如：

```text
Lifecycle = APPROVED
Freshness = STALE
DevelopmentReadiness = READY
DevelopmentEntry = HOLD
CurrentEffective = YES
```

这些可以同时合法成立。

---

## 5. Same-label State Safety

正式：

```text
Same State Label
!= Same State Domain
!= Same Semantic Meaning
```

例如：

```text
Development Entry = BLOCKED
UI Repair = BLOCKED
Project Feature = BLOCKED
Runtime Execution = BLOCKED
```

其 Cause / Owner / Release Condition / Authority Requirement / Downstream Effect 均可不同。

State Value 必须在 State Domain 内解释。

---

## 6. Governed Fact / Derived State Boundary

正式：

```text
Governed State Fact
!= Derived Effective State

Derived State
!= Canonical Semantic Truth

Effective State
!= Authority Fact

State Derivation
!= Authority Creation
```

Resolver 只能根据已有合法事实、规则、Binding、Authority、Gate、Scope、Context、Version、Freshness、Evidence 等输入计算 Derived State。

---

## 7. State Transition Boundary

正式：

```text
State Transition
must be interpreted within State Domain
```

例如：

```text
Development Entry:
HOLD → AUTHORIZED
```

和：

```text
Change Lifecycle:
OPEN → CLOSED
```

是两个完全不同的 Transition Contract。

正式：

```text
Cross-domain State Change
!= State Transition
```

上游 Domain 状态改变不得被解释为下游 Domain 的直接状态转换。

---

## 8. Cross-stage State Projection

跨阶段允许：

```text
State Projection
```

其含义是：

> 上游 Typed State Result 作为下游 Resolution Input / Gate Input / Dependency Input 被消费。

正式：

```text
State Projection
!= State Copy

State Projection
!= Authority Transfer

Handoff-carried State
!= Receiving Domain State

State Consumer
!= State Owner
```

下游 Owner 仍负责解析自己的状态。

---

## 9. Cross-domain Propagation

统一采用：

```text
Upstream State / Fact Change
→ Impact / Dependency Detection
→ Downstream Freshness / Applicability Evaluation
→ affected State becomes STALE / UNKNOWN / BLOCKED / UNRESOLVED as applicable
→ Domain Owner Re-resolution
→ New Typed State Result
```

正式复用 `AUDIT-PATCH-008`。

```text
Cross-domain State Change
!= Direct Downstream State Mutation
```

---

## 10. Automatic Re-resolution Boundary

如果 Dependency / Rule / Scope 已能唯一判断：

```text
Deterministic State Invalidation
→ Automatic

Deterministic State Re-resolution
→ Automatic
```

但：

```text
Automatic State Re-resolution
!= Automatic Reauthorization
```

自动重新解析不得扩大 Scope、创造 Authority、绕过 Gate 或静默修改 Canonical Semantic Fact。

---

## 11. Shared Minimum Semantics

以下值允许拥有 Banyan-wide 最小共同抽象，但始终必须 Domain-scoped。

### STALE

```text
STALE
=
a previously valid result whose relevant resolution basis changed,
so it cannot be assumed current without re-resolution.
```

```text
STALE != INVALID
```

### UNKNOWN

```text
UNKNOWN
=
required state-relevant facts or evidence are insufficient
to determine a valid state value.
```

```text
UNKNOWN != FALSE
UNKNOWN != ABSENT
UNKNOWN != NOT_APPLICABLE
```

### BLOCKED

```text
BLOCKED
=
the domain knows that progress / transition / resolution
cannot legally continue under current applicable conditions.
```

```text
BLOCKED != UNKNOWN
```

BLOCKED 必须逻辑上可解释 Block Reason。

### CONFLICTED

```text
CONFLICTED
=
multiple valid applicable semantic requirements/results
are mutually incompatible and existing governance
cannot uniquely resolve them.
```

```text
Conflict != Divergence
Conflict != Drift
Conflict != Error
Conflict != Cycle
Conflict != Unknown
```

### REVIEW_REQUIRED

```text
REVIEW_REQUIRED
=
automatic resolution cannot complete
and applicable governance explicitly requires review.
```

不得将任何 uncertainty 自动转换为 REVIEW_REQUIRED。

### HOLD

继续：

```text
HOLD != REVIEW_REQUIRED
HOLD != BLOCKED
```

HOLD 是明确的 Governed Pause；它可以成为 Block Reason，但不等价于 BLOCKED。

### SUPERSEDED

```text
SUPERSEDED != DELETED
SUPERSEDED != INVALID
```

---

## 12. Current Effective Boundary

正式：

```text
Current Effective
!= Lifecycle State
!= Freshness
```

Current Effective 是 Scope / Context-aware Derived Resolution Relation，不建立全局 CurrentEffective State Machine。

Current Effective 变化必须可追踪其 Scope / Resolution Basis / Dependency / Owner / Provenance。

---

## 13. Gate / Approval / Validation / Runtime Boundaries

正式保持：

```text
Gate Result != Authority
Gate PASS != Authority Granted
Gate PASS != Change Closed
Gate PASS != Feature Activated
Gate PASS != Runtime Allowed

Development Readiness != Development Entry Authorization

Approval != Development Entry
Approval != Apply Authorization
Approval != Runtime Permission

Validation PASS != Product Approval
Validation PASS != Feature Activation
Validation PASS != Final Activation

Feature Activation != Runtime Permission

Attempt Result != Apply Result != Change Result

Execution Success != Semantic Acceptance

Runtime Result != Product State
Runtime Result != Project State
Runtime Result != Change State
Runtime Result != Authority
```

---

## 14. Event / Exception Minimum Boundary

本 Patch 只冻结：

```text
Event != State
Exception != State
Error != Conflict
```

Event / Exception 可以触发 State Transition、产生 Evidence、触发 Re-resolution 或 Governance，但不自动成为 State Value。

完整 Exception / Error / Failure / Recovery 模型留给 Batch 5 后续审核。

---

## 15. State History

应逻辑区分：

```text
Current State Result
State History
Transition History
Resolution History
```

正式：

```text
New Current State
!= Rewrite Previous State History

Historical State
!= Current State
```

State Snapshot 可用于 Task / Change / Validation / Audit reproducibility，但：

```text
State Snapshot != Canonical State Authority
```

Snapshot 也可能 STALE。

---

## 16. Scope / Locality

State Result 必须 Scope-aware。

正式：

```text
Local State Block
!= Global Project Block
```

跨阶段影响传播先经过：

```text
Scope Intersection
+ Dependency Applicability
```

不得因为局部 BLOCKED 而默认阻断整个 Project。

---

## 17. Dependency / Cycle Reuse

State Domain 可以依赖其他 Domain State Result，但：

```text
Dependency != State Merge
```

跨 State Domain Dependency Cycle 直接复用 `AUDIT-PATCH-013`：

```text
Cycle Detection
→ Automatic Structural Diagnosis
→ Deterministic Resolution if possible
→ explicit non-success state
→ Informed Decision only for genuine material semantic choice
```

不建立第二套 Cycle / Convergence 系统。

---

## 18. Owner Boundary

### F1
拥有 State Domain separation invariant、Definition / Runtime separation。

### F2
拥有 Storage Truth / typed status invariants，不在本 Patch 冻结 Physical State Schema。

### F3
拥有 StateModelDefinition taxonomy position；不自动增加新的顶级 StateDomainDefinition。

### F4
拥有 Workflow State Coordination、Typed Handoff、Pause / Resume / Retry / Skip / Partial Blocking；Workflow State != All Domain State。

### F5
拥有 Product / Requirement / Approval / Readiness / Development Entry 等 Product Governance State Domain。

### F6
拥有 UI / Design / Validation / Repair / Effective UI State Domain。

### F7
拥有 Change / Apply / Attempt / Result / Rollback / Closeout State Domain，以及 Durable Canonical Mutation Governance。

### F8
拥有 Project Instance / Binding / Feature / Gate / Effective Project State Domain。

### F9
未来负责 State lookup / Freshness Evidence / Dependency / Impact Query / Provenance Retrieval，不取得其他 Domain State Authority。

### F10
未来拥有 Runtime Permission / Runtime Execution State，不反向取得 Product / Design / Project / Change State Authority。

---

## 19. F9 / Index Boundary

未来 F9 可索引：

```text
State Subject
State Domain
State Value
Scope
Freshness
Owner
Dependency
Provenance
```

但：

```text
Index State != Canonical State Truth
Index Miss != State Absent
F9 != State Owner
F9 != State Transition Authority
F9 != State Resolution Authority
```

除 F9 自身拥有的 Freshness / Index Evidence Domain。

---

## 20. Performance

正常：

```text
Requested Action
→ Resolve required State Domains only
→ F9 candidate / freshness lookup
→ Targeted governed facts
→ Domain-owned State Resolver
→ Minimum Effective State Context
→ Action / Handoff
```

不默认加载整个 Project 全部状态和历史。

---

## 21. Legacy Compatibility

旧数据可能只有：

```text
status: active
status: blocked
status: done
```

不得直接提升成 Canonical Typed State。

正确：

```text
Legacy Status
→ identify Subject
→ identify probable State Domain
→ validate Scope / Owner / Context / Semantics
→ deterministic mapping if unique
```

无法唯一映射：

```text
→ UNKNOWN / UNRESOLVED MAPPING
```

```text
AI Guess != State Domain Resolution
```

不要求一次性全量迁移，可采用 active-scope / resolution-triggered / change-triggered / risk-driven 方式。

---

## 22. Banyan-wide Invariants

```text
State Domains Remain Separate
One Subject != One Global Status
State Domain != Stage
State Domain != Mandatory Finite State Machine
Same State Label != Same State Domain != Same Semantic Meaning
State Value must be interpreted within State Domain
Governed State Fact != Derived Effective State
Derived State != Canonical Truth
State Derivation != Authority Creation
State Projection != State Copy
State Projection != Authority Transfer
Handoff State != Receiving Domain State
Cross-domain State Change != Direct State Mutation
Cross-domain State Change → Impact / Dependency → Domain-owner Re-resolution
State Consumer != State Owner
Local State Block != Global Project Block
STALE != INVALID
UNKNOWN != FALSE != ABSENT != NOT_APPLICABLE
BLOCKED != UNKNOWN
HOLD != REVIEW_REQUIRED != BLOCKED
Conflict != Drift != Divergence != Error != Cycle != Unknown
Current Effective != Lifecycle State != Freshness
Gate Result != Authority
Approval != Development Entry != Apply Authorization != Runtime Permission
Validation PASS != Activation
Feature Activation != Runtime Permission
Attempt Result != Apply Result != Change Result
Execution Success != Semantic Acceptance
Event != State
Exception != State
Historical State != Current State
New Current State != Rewrite State History
State Re-resolution != Canonical Mutation
Automatic State Re-resolution != Automatic Reauthorization
Index State != Canonical State Truth
Index Miss != State Absent
AI Inference != State Authority
```

---

## 23. Forbidden Interpretation

禁止：

1. 创建 Banyan 全局 status；
2. 创建 Global State Machine / UniversalStateMachine / GlobalStatusResolver；
3. 同名 BLOCKED / CURRENT 自动同义；
4. F5 READY 自动等于 Development Entry AUTHORIZED；
5. Approved 自动等于 Apply Authorized；
6. Gate PASS 自动等于 Feature Activated；
7. Validation PASS 自动等于 Final Activation；
8. Change CLOSED 自动等于 Requirement CLOSED；
9. Repair CLOSED 自动等于 UI Contract CURRENT；
10. SHADOW_VALIDATED 自动等于 Final Activated；
11. Runtime ALLOW 自动等于 Product Approval；
12. Runtime Success 自动等于 Canonical Acceptance；
13. 上游状态直接写下游状态；
14. State Projection 转移 Authority；
15. State Consumer 获得 Owner 修改权；
16. UNKNOWN 自动变成 BLOCKED；
17. STALE 自动等于 INVALID；
18. BLOCKED 自动要求人工；
19. Local Block 自动全项目阻断；
20. Event 自动变成 State；
21. Exception 自动变成 State；
22. Error / Drift / Conflict 合并成统一 Failure State；
23. 新 Current State 覆盖历史；
24. F9 Index 成为 State Truth；
25. AI 猜测 Legacy Status Domain；
26. 本 Patch 提前冻结完整 Exception Model；
27. 本 Patch 授权 Implementation / RP2 / Final Activation。

---

## 24. Deferred

不冻结：

```text
Exact State Domain enum
Exact State Value enum
Exact State schema
State physical storage
SQLite State tables
Graph schema
State Domain Registry
State history layout
State transition API
Go interface
REST API
Runtime State Resolver implementation
FSM engine
Event Bus / Message Bus
Cache format
F9 State index schema
F10 Runtime state API
F11 State visualization UX
Migration tooling
Legacy status bulk migration
Exception taxonomy
Error taxonomy
Recovery taxonomy
Autonomous AI State Learning
```

---

## 25. No-Loss Mapping

本 Patch 保留并补充：

- F1 — State Domains Remain Separate；
- F2 — status_domains_typed；
- F3 — StateModelDefinition != RuntimeState；
- F4 — Typed Handoff；
- F5 — Lifecycle / Approval / Readiness / Entry / Current Effective / Freshness 分离；
- F6 — Effective State / CURRENT / STALE / REVIEW_REQUIRED 等；
- F7 — Attempt / Apply / Change Result、Closed / Archived、Stale / Invalid；
- F8 — Gate / Feature / Effective Project State、Drift / Conflict / Error 分离；
- AUDIT-PATCH-003 — Current Effective；
- AUDIT-PATCH-007 — Gate / Development Entry；
- AUDIT-PATCH-008 — Upstream Change → Re-resolution；
- AUDIT-PATCH-013 — Dependency / Cycle / Convergence。

---

## 26. Human Decision

用户明确：

```text
B5-PATCH-01 HUMAN_APPROVED
```

因此：

```text
AUDIT-PATCH-014 = HUMAN_APPROVED
B5-CHAIN-01 = ARCHITECTURALLY_RESOLVED
```

---

## 27. Authorization Boundary

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

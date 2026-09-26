# AUDIT-PATCH-012 — Project Binding Multi-Resolution × Conflict × Current Effective

> Formal Audit Patch ID: `AUDIT-PATCH-012`  
> Source Finding: `B4-CHAIN-01`  
> Source Approval ID: `B4-PATCH-01`  
> Status: `HUMAN_APPROVED`  
> Audit Batch: `Audit Batch 4 — Project Instance / Binding Chain`  
> Classification: `GAP / P1`  
> Primary Owner: `F8`  
> Cross-stage Owners: `F1 / F7 / F9 / F10`  
> Implementation Authorization: `NO`

---

## 1. Problem

F8 已冻结 `Binding != Effective Binding`，AUDIT-PATCH-001 已冻结：

```text
Assignment != Binding != Resolution != Execution
```

但原合同没有完整定义多个 Project Binding 同时适用时，如何区分共存、组合、候选替代、Primary/Fallback、Constraint、合法 Override 与真正 Conflict。若缺少该层，未来实现可能退化为 Last / Latest / File Order / Numeric Priority / AI Confidence 决定 Current Effective。

---

## 2. Existing Contract

继续保持：

```text
Binding != Effective Binding
Resolution != Binding
Resolution != Authority Creation
Latest != Current Effective
More Specific Scope != Higher Authority
Project Local != Automatic Override
Runtime Selection != Durable Rebinding
Index != Canonical Truth
Index != Authority
```

本 Patch 不重新定义 Assignment、Configuration Profile、Stable ID / Revision / Version、Authority、Reconciliation Precedence、Freshness / Re-resolution。

---

## 3. Target Contract — Binding Resolution Target

正式引入逻辑概念：

```text
Binding Resolution Target
```

用于回答多个 Binding 是否真的在决定同一个语义位置。逻辑上至少能识别：

```text
Project Instance
+ Binding Domain / Family
+ Relation Purpose
+ Semantic Target / Slot
+ Applicable Scope
+ Material Context
```

它不是 F1 新顶级对象、Canonical Artifact、Registry、数据库表或 Authority。

---

## 4. Candidate Binding Set

确定 Resolution Target 后形成：

```text
Candidate Binding Set
```

正式：

```text
Candidate Binding != Effective Binding
Index Match != Candidate Eligibility != Effective Binding
```

候选至少经过：

```text
Target Match
→ Scope Match
→ Applicability
→ Lifecycle Validity
→ Revision / Supersession
→ Version / Compatibility
→ Freshness
→ Policy / Boundary / Gate
```

---

## 5. Scope Boundary

```text
Scope Match != Precedence
More Specific Scope != Higher Authority
Project Local != Automatic Override
```

Scope 决定适用性，不自动决定 Winner。

---

## 6. Multi-Binding Relation Semantics

同一 Resolution Target 下至少支持以下语义类别：

```text
COMPOSE
ALTERNATIVE
FALLBACK
OVERRIDE
CONSTRAINT
MUTUALLY EXCLUSIVE
```

本 Patch 冻结语义能力，不冻结 exact physical enum。

### COMPOSE

多个 Binding 合法共同形成结果：

```text
Composition != Conflict
```

### ALTERNATIVE

多个候选合法但 Target 要求单选。已有合法 Selection Policy 时自动解析；没有合法唯一依据时进入 `UNRESOLVED`，不得使用 Last / Latest / AI Guess。

### FALLBACK

允许：

```text
Current Effective Primary
+ Approved Fallback Plan
```

但：

```text
Runtime Fallback != Durable Rebinding
```

### OVERRIDE

只有存在 Explicit Override Relation + Applicable Policy + Valid Authority + Valid Scope + Override Eligibility 时成立。

### CONSTRAINT

多个 Constraint 可共同求交集：

```text
Multiple Constraints != Conflict
```

交集为空且无其他治理规则可解时，进入 Conflict / Blocked。

### MUTUALLY EXCLUSIVE

多个有效候选不能同时成为同一 Target 的 Effective Result，且无 Selection / Fallback / Override / Supersession 等规则可解时，才构成真正 Conflict。

---

## 7. Lifecycle Relation Boundary

```text
SUPERSEDES / RETIRES / REPLACES
```

属于 Lifecycle / History Relation，不自动等价于 COMPOSE / FALLBACK / OVERRIDE。

继续保持：

```text
Revision Lineage != Supersession
Supersession != Runtime Precedence
```

---

## 8. Resolution Result Modes

逻辑上至少允许：

```text
Single Selection
Composite Set
Constraint Resolution
Primary + Fallback Plan
```

因此：

```text
One Current Effective Resolution Result
!= One Constituent Binding
```

---

## 9. Current Effective Uniqueness

正式：

```text
Same Resolution Target
+ Same Applicable Scope
+ Same Material Context
+ Same Resolution Basis
→ One Current Effective Resolution Result
```

Result 内部可包含多个合法组成 Binding，但不得有两个互相矛盾的 Current Effective Result 同时对同一 Target 生效。

---

## 10. Resolution Basis / Provenance

Current Effective Result 至少应可追踪：

```text
Binding Revisions
Scope
Applicability
Policy
Version / Compatibility
Authority refs
Override refs
Gate
Freshness Evidence
Relevant Context
Resolver Contract Version
```

Exact physical schema 延期。

---

## 11. Resolution / Policy / Authority Boundary

```text
Resolution != Authority Creation
Selection Policy != Semantic Authority
```

Provider Selection、Version Resolution、Profile Composition 等可以消费 Policy，但不会因此获得 Product / Design / Apply / Runtime Authority。

---

## 12. Forbidden Winner Algorithms

禁止把以下作为 Banyan 全局 Winner 规则：

```text
Numeric Priority without Governing Policy
File Order
Last Write
Latest Revision / Version
AI Recommendation
Model Confidence
```

继续：

```text
File Order != Governance Precedence
Latest != Current Effective
AI Confidence != Winner
```

---

## 13. Binding Conflict Definition

真正 Binding Conflict 至少要求：

```text
Same / Overlapping Resolution Target
+ Overlapping Applicable Scope
+ Multiple Valid Candidates
+ Mutually Incompatible Effective Outcomes
+ No valid Composition
+ No valid Selection Policy
+ No valid Fallback Relation
+ No valid Override
+ No valid Constraint Resolution
+ No valid Compatibility Resolution
+ No valid Supersession
+ No other deterministic governance rule
```

因此：

```text
Multiple Applicable Bindings != Binding Conflict
```

---

## 14. Locality

```text
Local Binding Conflict != Global Project Invalidation
```

默认只阻塞受影响 Resolution Target 及其真实依赖范围。

---

## 15. State Semantics

逻辑上至少能表达：

```text
RESOLVED
UNRESOLVED
UNKNOWN
STALE
CONFLICTED
BLOCKED
SUPERSEDED / NOT_APPLICABLE
```

Exact runtime enum 延期，并保持：

```text
UNRESOLVED != CONFLICTED
UNKNOWN != CONFLICTED
STALE != INVALID != DELETED
```

---

## 16. Automatic / Human Governance Boundary

```text
Multiple Candidates != Human Decision Required
```

当 Binding / Scope / Applicability / Policy / Compatibility / Version / Authority / Override / Fallback / Constraint / Gate / Freshness 已能唯一决定时：

```text
→ Automatic Resolution
```

只有真正 material judgment gap 才进入 Human Governance。

---

## 17. Resolution != Mutation

```text
Resolution Result != Durable Rebinding
Automatic Resolution != Automatic Mutation
Runtime Fallback != Durable Rebinding
```

需要永久修改受保护 Binding 时：

```text
Domain Owner
→ F7 Governed Change
→ Canonical Apply
```

---

## 18. Re-resolution

完整复用 AUDIT-PATCH-008：

```text
Authoritative Upstream Change
→ Affected Binding Target
→ Freshness Evaluation
→ Current Effective → STALE
→ F8 Re-resolution
→ New Effective Result
```

继续：

```text
Auto Re-resolution != Auto Reauthorization
Impact Discovery != Scope Expansion Authorization
```

---

## 19. Domain-specific Semantics

共同解析合同不取代领域语义：

- Source Resolver：Source Role / Mapping；
- Profile Resolver：Composition / Overlay；
- Provider Resolver：Capability / Health / Fallback；
- Version Resolver：Constraint / Compatibility；
- Feature Resolver：Activation / Dependency / Gate。

禁止 `UniversalBindingResolver` God Object。

---

## 20. Owner Boundary

### F1
负责 Assignment / Binding 一等对象家族共同边界，不拥有万能解析中心。

### F8
负责 Project Binding Resolution Target、Candidate Binding Resolution、Scope / Applicability、Source / Profile / Provider / Version / Feature Resolution、Effective Project Binding Result、Project Re-resolution。

### F7
负责 Durable Protected Binding Mutation、Revision、History、Supersession、Canonical Apply、Rollback。

### F9
未来负责 Binding Index、Reverse Reference、Candidate Discovery、Freshness / Impact Evidence、Provenance Retrieval。

```text
Index Match != Candidate Eligibility
Candidate Eligibility != Effective Binding
Index != Authority
```

### F10
消费 Task-scoped Minimum Sufficient Effective Project Context；不得由 Runtime Observation 反向创造 Canonical Binding。

---

## 21. Performance

正常路径：

```text
Task
→ Project Instance
→ Resolution Target
→ F9 Index Candidate Narrowing
→ Minimum Candidate Set
→ Targeted Canonical Read
→ Domain Resolver
→ Current Effective Result
```

```text
Index Miss != Semantic Absence
```

Coverage 不完整时回到 Canonical Source。

---

## 22. Legacy Compatibility

旧资料未显式表达 COMPOSE / FALLBACK / OVERRIDE 等关系时：

```text
Single Candidate → deterministic resolve
Existing explicit domain contract → derive relation semantics
Existing governed fallback / override evidence → preserve semantics
Multiple candidates + insufficient evidence → UNKNOWN / UNRESOLVED
```

禁止 AI 猜测补齐。

允许 active-project / change-triggered / resolution-triggered / risk-driven coverage，不要求全量迁移。

---

## 23. No-Loss Mapping

保留并兼容：

- AUDIT-PATCH-001 — Assignment / Binding / Resolution；
- AUDIT-PATCH-002 — Configuration Profile；
- AUDIT-PATCH-003 — Stable ID / Revision / Version / Current Effective；
- AUDIT-PATCH-008 — Upstream Change / Re-resolution；
- AUDIT-PATCH-009 — Authority Binding / Effective Authority；
- AUDIT-PATCH-010 — Reconciliation Precedence / Canonical Transition；
- F8-D02～D10。

本 Patch 只补齐 Multi-Binding Resolution。

---

## 24. Banyan-wide Invariants

```text
Multiple Bindings != Binding Conflict
Candidate Binding != Effective Binding
Index Match != Candidate Eligibility != Effective Binding
One Current Effective Result != One Constituent Binding
Scope Match != Precedence
More Specific Scope != Automatic Winner
Project Local != Automatic Override
Composition != Priority
Fallback != Retry
Runtime Fallback != Durable Rebinding
Alternative != Conflict
UNRESOLVED != CONFLICTED
UNKNOWN != CONFLICTED
STALE != INVALID != DELETED
Resolution != Authority Creation
Resolution Result != Canonical Truth
Automatic Resolution != Automatic Mutation
Automatic Re-resolution != Automatic Reauthorization
Impact Discovery != Scope Expansion Authorization
Latest != Current Effective
File Order != Governance Precedence
Last Write != Winner
AI Confidence != Winner
```

---

## 25. Forbidden Interpretation

禁止：

1. 多个 Binding 自动等于冲突；
2. Scope 更具体自动获胜；
3. Project Local 自动覆盖 Shared；
4. 数字 priority 自动决定 Winner；
5. 文件 / 加载顺序决定语义；
6. Latest 自动成为 Current Effective；
7. AI 推荐 / 置信度自动成为 Current Effective；
8. Resolution Result 自动写回 Canonical Binding；
9. Runtime Fallback 自动永久 Rebinding；
10. Effective Result 成为第二 Canonical Truth；
11. F9 / SQLite 获得 Binding Authority；
12. F10 Runtime 自主永久 Rebinding；
13. 建立 Universal Resolver God Object；
14. 每次多个 Candidate 都询问用户；
15. Local Conflict 自动全项目失效；
16. STALE 删除历史；
17. 本 Patch 授权 Implementation / RP2 / Final Activation。

---

## 26. Deferred

不冻结：

```text
BindingResolutionTarget physical schema
Binding Relation exact enum
SQLite Binding table
Relation / Graph physical schema
Resolver API / Go interface
YAML / JSON schema
SQL DDL
Index schema
Cache layout
Runtime exact enum
Provider scoring implementation
WebUI
Migration tooling
Autonomous AI learning
```

---

## 27. Downstream Impact / Integration Target

未来主要整合至：

```text
F8_Project_Instance_Governance_Freeze_Pack_v1.1 Candidate
```

并向 F1 / F7 / F9 / F10 补充消费边界，不改变既有 Owner。

---

## 28. Supersession / Compatibility

本 Patch 不删除 F8 v1.0 既有条文；它作为 Audit Patch Layer 补充解释和修复缺口。

F1～F8 v1.0 保持 Original Frozen Baseline，直到完整 Pre-F9 Audit 完成、生成 v1.1 Candidate、完成 No-Loss Reconciliation / Final Audit 并再次获得明确批准。

---

## 29. Human Decision

用户明确：

```text
B4-PATCH-01 HUMAN_APPROVED
```

因此：

```text
AUDIT-PATCH-012 = HUMAN_APPROVED
B4-CHAIN-01 = ARCHITECTURALLY_RESOLVED
```

---

## 30. Authorization Boundary

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

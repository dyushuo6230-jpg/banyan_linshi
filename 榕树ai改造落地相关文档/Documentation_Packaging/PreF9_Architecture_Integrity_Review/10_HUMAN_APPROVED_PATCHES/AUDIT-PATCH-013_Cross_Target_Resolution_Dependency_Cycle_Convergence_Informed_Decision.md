# AUDIT-PATCH-013 — Cross-Target Resolution Dependency × Cycle Detection × Deterministic Convergence × Informed Decision Escalation Boundary

> Formal Audit Patch ID: `AUDIT-PATCH-013`  
> Source Finding: `B4-CHAIN-02`  
> Source Approval ID: `B4-PATCH-02`  
> Status: `HUMAN_APPROVED`  
> Audit Batch: `Audit Batch 4 — Project Instance / Binding Chain`  
> Classification: `GAP / P1`  
> Primary Owner: `F8`  
> Cross-stage Owners: `F7 / F9 / F10`  
> Reuses: `AUDIT-PATCH-005 / AUDIT-PATCH-008 / AUDIT-PATCH-010 / AUDIT-PATCH-012`  
> Implementation Authorization: `NO`

---

## 1. Problem

AUDIT-PATCH-012 解决同一个 Resolution Target 内多个 Binding 的确定性解析，但不同 Resolution Target 之间仍可能互相依赖。

风险示例：

```text
Profile Resolution
→ requires Feature Resolution

Feature Resolution
→ requires Provider Resolution

Provider Resolution
→ requires Profile Resolution
```

若没有统一合同，可能形成隐藏循环、无限重算、靠调用顺序或缓存得到不确定结果。

---

## 2. Existing Contract

继续保持：

```text
Workflow may contain Loop / Retry / Reconcile
F8 stage diagram != fixed Runtime Call Order
Current Effective = Scope / Context-aware Derived Resolution Result
STALE != INVALID != DELETED
Runtime mismatch → Owner re-resolution
Reconciliation != Canonical Apply
Valid Human Decision != Immediate Canonical Mutation
```

本 Patch 不重做 Workflow Loop、Informed Decision、Freshness、Canonical Apply。

---

## 3. Target Contract

正式补齐：

```text
Cross-Target Resolution Dependency
+ Cycle Detection
+ Deterministic Convergence
+ Informed Decision Escalation Boundary
```

目标链：

```text
Requested Resolution Target
→ Resolve Active Hard Dependencies
→ Build Minimum Sufficient Dependency Graph
→ Cycle / Convergence Check
→ Deterministically Resolvable?
   ├─ YES → Automatic Resolution
   └─ NO  → Classify Unresolved Reason
            ├─ Missing Evidence → UNKNOWN
            ├─ Governance Block → BLOCKED
            ├─ Semantic Conflict → CONFLICTED / Owner Routing
            └─ Multiple Legitimate Material Semantic Choices
               → INFORMED_DECISION
```

---

## 4. Workflow Loop != Resolution Dependency Cycle

```text
Workflow Loop != Resolution Dependency Cycle
```

Workflow Loop 是受治理执行流程；Resolution Dependency Cycle 是为了得到 A 必须先知道 B，而 B 又依赖 A 的解析结构问题。

---

## 5. Resolution Dependency

正式引入逻辑关系：

```text
A --REQUIRES--> B
```

含义：

> Target A 的合法 Current Effective Resolution 必须先获得 Target B 的合法解析结果。

它首先是 Governed Logical Relation，不要求成为 F1 新顶级对象。

---

## 6. Relation Boundary

```text
Reference != Resolution Dependency
Evidence Relation != Hard Resolution Dependency
Helpful Evidence != Hard Dependency
```

只有：

```text
Without B
A cannot legally resolve
```

才属于 Hard Resolution Dependency。

---

## 7. Active Resolution Dependency Graph

当前 Project / Scope / Context 下真正适用的 Hard Dependency 形成：

```text
Active Resolution Dependency Graph
```

它表达计算先决条件，不表达 Authority：

```text
Dependency Order != Governance Precedence
Evaluation Order != Semantic Priority
```

---

## 8. Deterministic Resolution Requirement

```text
Active Hard Resolution Dependency Graph
must be deterministically resolvable
```

必须最终：

- 收敛到稳定 Current Effective Result；或
- 显式终止为 UNKNOWN / UNRESOLVED / BLOCKED / CONFLICTED 等非成功状态。

不得无限重算。

---

## 9. Runtime Call Order Boundary

禁止把 F8-D02 → D03 → D04 → D05 → D06 解释成固定 Runtime 调用顺序或语义优先级。

实际 Evaluation Order 来自 Active Dependency Graph。

无相互依赖节点可以并行，但：

```text
Scheduler Order must not change Semantic Result
First Resolved != Winner
Last Resolved != Winner
```

---

## 10. Scope / Context-aware Dependency

Dependency Applicability 必须 Scope / Context-aware。

允许 Conditional Dependency，但其条件必须由合法已知事实可靠解析。

禁止：

```text
Dependency Activation Condition
silently depends on
the unresolved result it is defining
```

除非未来存在显式受治理 Convergence Contract；当前未授权。

---

## 11. Minimum Sufficient Expansion

```text
Requested Target
→ expand only active required dependencies
→ stop at resolved / independent leaves
```

不要求每次构建全局完整图。

---

## 12. Cycle Detection

发现：

```text
A requires B
B requires C
C requires A
```

则：

```text
CYCLE_DETECTED
```

正常 Current Effective Resolution 不得继续宣称成功。

```text
Implicit Cyclic Resolution = FORBIDDEN
```

---

## 13. Cycle != Conflict

```text
Cycle != Semantic Conflict
```

Cycle 是依赖结构无法正常完成；Conflict 是有效语义要求彼此不兼容。

---

## 14. Locality

```text
Local Resolution Cycle != Global Project Invalidation
```

只阻塞 Cycle 成员及依赖该 Cycle 的下游 Target。

---

## 15. Automatic Structural Diagnosis

Cycle Detected 后先自动检查：

1. Dependency Direction 是否错误；
2. 普通 Reference 是否被误升为 Hard Dependency；
3. Evidence 是否被误当 Dependency；
4. Requirement / Input / Effective Result 是否混用；
5. Conditional Dependency 是否自引用；
6. Scope / Applicability 是否错误扩张；
7. Existing Rule / Policy 是否可以唯一修正。

若已有治理合同可唯一修正：

```text
Deterministically Resolvable
→ MUST NOT escalate to Human
```

---

## 16. Input / Result Separation

```text
Feature Requirement != Effective Feature
Provider Requirement != Effective Provider
Version Constraint != Effective Version
Resolution Input != Result Being Resolved
```

除非存在明确 Convergence Contract；当前未开放。

---

## 17. Cache Safety

```text
Cached Result != Automatic Cycle Breaker
```

只有缓存仍满足 Stable Subject / Scope / Context / Resolution Basis / Freshness 时，才能作为普通 Current Effective Snapshot 消费。

```text
STALE Result
cannot silently satisfy
a Current Resolution Dependency
```

Historical Reproduction 不得当作 Current Resolution 依据。

---

## 18. Dependency Topology Change

Effective Dependency Graph 可因 Scope / Context / Applicability 改变而变化：

```text
Effective Dependency Graph Change
!= Canonical Dependency Mutation
```

长期 Dependency Contract 持久变化时：

```text
Domain Owner
→ F7 Governed Change
→ Canonical Apply
```

Resolver 不得自行永久写回。

---

## 19. Automatic Re-plan Boundary

适用关系唯一可解时允许 Automatic Dependency Re-plan。

```text
Automatic Dependency Re-plan != Automatic Reauthorization
Impact Discovery != Scope Expansion Authorization
```

---

## 20. Oscillation Safety

同一 Resolution Basis 下不得出现无边界：

```text
State A → State B → State A → State B ...
```

正式：

```text
Unbounded Resolution Oscillation = FORBIDDEN
```

Resolution 必须收敛到稳定结果，或显式终止为非成功状态。Exact retry count / runtime algorithm 延期。

---

## 21. Fixed-Point Boundary

当前：

```text
General Fixed-Point Resolution Engine = NOT IMPLEMENTED
```

未来若某 Domain 真需要合法循环求解，至少必须有：

```text
Explicit Domain Contract
+ Declared Convergence Semantics
+ Bounded Resolution Rule
+ Deterministic Result Contract
```

```text
Future Extensibility != Current Authorization
```

---

## 22. Informed Decision Reuse

本 Patch 不创建第二套决策协议，正式复用：

```text
AUDIT-PATCH-005
Dynamic Workflow Choice × Informed Decision
```

冻结：

```text
Informed Decision != Cycle Resolution Algorithm
Cycle Detected != Human Decision Required
UNRESOLVED != Human Decision Required
UNKNOWN != Human Decision Required
Missing Evidence != Human Decision Required
Governance Block != Human Semantic Choice
```

---

## 23. Informed Decision Entry Condition

只有至少满足：

```text
Evidence materially sufficient
+ Applicable Rules known
+ Authority validly resolvable
+ Scope known
+ No deterministic governance rule uniquely resolves
+ Multiple legitimate semantic choices remain
+ Choices have materially different downstream meaning / effect
```

才进入：

```text
INFORMED_DECISION
```

---

## 24. Decision Package

Informed Decision 至少应提供：

- Current Problem；
- Cycle / Dependency Evidence；
- 为什么自动规则无法唯一决定；
- Option A / B 的语义含义；
- Owner Impact；
- Downstream Impact；
- Compatibility Impact；
- No-change consequence；
- Applicable Authority / Scope。

AI 可以解释、比较、组织证据，但不能替用户在多个合法 material semantic alternatives 中静默作决定。

---

## 25. Decision != Mutation

```text
Valid Informed Decision != Automatic Dependency Mutation
```

若要求 Durable Semantic Mutation：

```text
Informed Decision
→ Valid Decision Evidence
→ Applicable Authority / Scope
→ Target Semantic
→ F7 Governed Change
→ Canonical Apply
```

继续兼容 AUDIT-PATCH-010。

---

## 26. Resolution Escalation Ladder

```text
1. Deterministic Automatic Resolution
→ 2. Automatic Structural Diagnosis
→ 3. Evidence / Dependency Recovery
→ 4. Rule / Policy / Authority / Scope Resolution
→ 5. Explicit UNKNOWN / BLOCKED / CONFLICTED when applicable
→ 6. Informed Decision only for genuine material semantic choice
```

实现：

```text
Reliable Automatic Routing
× Minimum Human Decision Governance
```

---

## 27. Owner Boundary

### F8
负责 Project Resolution Dependency semantics、Active Dependency Graph semantics、Cycle Detection semantics、Convergence boundary、Decision Escalation Classification。

F8 不成为 Informed Decision Protocol Owner。

### F7
负责 Durable Dependency Mutation、Revision、History、Supersession、Canonical Apply、Rollback。

### F9
未来负责 Dependency Index、Reverse Dependency、Candidate Retrieval、Freshness、Impact、Provenance Retrieval。

```text
Index Edge != Canonical Dependency
F9 Cycle Evidence != Mutation Authority
```

### F10
只消费 Resolved Minimum Sufficient Project Context；遇到 STALE / UNKNOWN / BLOCKED / UNRESOLVED 或 Runtime mismatch 时路由回 F8 / Domain Owner，不得自行改 Dependency Graph。

---

## 28. No Global God Object

禁止：

```text
GlobalDependencyAuthority
GlobalResolutionGraphAuthority
UniversalDependencyResolver
```

正确结构：

```text
Common Resolution Dependency Contract
+ Domain-owned dependency semantics
+ F8 Project Resolution Coordination
```

---

## 29. Provenance

成功 Resolution 至少可解释：

```text
Requested Target
Active Dependencies
Dependency Applicability
Cycle Check Result
Dependency Results
Relevant Bindings
Relevant Versions
Relevant Policies
Authority / Gate
Freshness Basis
Final Effective Result
```

Cycle 诊断至少可解释 Members / Edges / Scope / Context / 每条 Dependency 的来源。

---

## 30. Historical Reproducibility

历史 Resolution 必须能够还原当时：

- 哪些 Dependency 生效；
- 为什么没有 Cycle；
- 使用哪些 Binding / Version；
- 为什么最终有效。

Current Contract 改变不得重写历史解释。

```text
Superseded != Deleted
```

---

## 31. Performance / Index Boundary

正常：

```text
Requested Target
→ F9 Candidate Dependency Lookup
→ Targeted Canonical Read
→ Minimum Active Hard Dependency Expansion
→ Cycle Check
→ Resolution
```

```text
Index Miss != No Dependency
```

Coverage 不完整时必须回到 Targeted Canonical Read。

---

## 32. Legacy Compatibility

旧资料没有显式 Dependency Relation 时，可从 Existing Governed Semantic Contract 确定性推导必要关系。

```text
AI Guess != Dependency Contract
```

不要求全量一次性迁移；允许 active-target / change-triggered / resolution-triggered / risk-driven coverage。

---

## 33. No-Loss Mapping

保留并兼容：

- AUDIT-PATCH-005 — Informed Decision Protocol；
- AUDIT-PATCH-008 — Upstream Change / Freshness / Re-resolution；
- AUDIT-PATCH-010 — Decision / Canonical Transition Boundary；
- AUDIT-PATCH-012 — Per-target Multi-Binding Resolution；
- F8-D08 — Drift / Reconciliation；
- F8-D09 — Current Effective Boundary；
- F8-D10 — Runtime Handoff。

本 Patch 只补齐 Cross-target Dependency / Cycle / Convergence / Decision Escalation。

---

## 34. Banyan-wide Invariants

```text
Workflow Loop != Resolution Dependency Cycle
Reference != Resolution Dependency
Evidence Relation != Hard Resolution Dependency
Dependency Order != Governance Precedence
Evaluation Order != Semantic Priority
First Resolved != Winner
Last Resolved != Winner
Scheduler Order must not change Semantic Result
Active Hard Dependency Graph must be deterministically resolvable
Implicit Cyclic Resolution = FORBIDDEN
Cycle != Semantic Conflict
Cycle Detected != Human Decision Required
Unresolved != Human Decision Required
Unknown != Human Decision Required
Missing Evidence != Human Decision Required
Governance Block != Human Semantic Choice
Informed Decision is only for genuine material semantic choice
Deterministically Resolvable → must not escalate to human
Cycle Detection != Mutation Authorization
Local Resolution Cycle != Global Project Invalidation
Cached Result != Automatic Cycle Breaker
STALE Result cannot silently satisfy Current Dependency
Resolution Input != Result Being Resolved unless explicit convergence contract exists
Effective Dependency Graph Change != Canonical Dependency Mutation
Automatic Dependency Re-plan != Automatic Reauthorization
Unbounded Resolution Oscillation = FORBIDDEN
Valid Informed Decision != Automatic Dependency Mutation
Future Extensibility != Current Authorization
```

---

## 35. Forbidden Interpretation

禁止：

1. Cycle Detected 默认问用户；
2. UNRESOLVED / UNKNOWN 默认升级人工；
3. Evidence 缺失让人猜；
4. Authority 缺失让人随意选择；
5. F8-D02～D06 固定 Runtime 顺序成为语义优先级；
6. First / Last Resolved 决定 Current Effective；
7. File / Scheduler 顺序打破 Cycle；
8. 多跑几轮直到“看起来稳定”；
9. STALE Cache 作为隐式破环器；
10. Resolver 自动删除 Dependency Edge；
11. Cycle 自动等于 Semantic Conflict；
12. Local Cycle 自动全项目 Invalid；
13. F9 Index 成为 Dependency Truth；
14. F10 Runtime 自主修改 Dependency；
15. AI Confidence 决定删除哪条依赖；
16. Informed Decision 绕过 Authority / Scope / Gate；
17. Human Decision 直接改 Canonical Dependency；
18. 当前阶段实现通用 Fixed-Point Solver；
19. Future Fixed-Point 授权今天接受隐式 Cycle；
20. 本 Patch 授权 Implementation / RP2 / Final Activation。

---

## 36. Deferred

不冻结：

```text
Dependency exact enum
Dependency physical schema
SQLite table
Graph DB
Cycle / SCC / topological-sort implementation
Retry count
Fixed-point algorithm
Resolver API
Go interface
Cache layout
Runtime exact enum
WebUI visualization
Migration tooling
Autonomous dependency learning
```

---

## 37. Integration Target / Downstream Impact

未来主要整合至：

```text
F8_Project_Instance_Governance_Freeze_Pack_v1.1 Candidate
```

并向 F7 / F9 / F10 增加明确消费边界。

AUDIT-PATCH-005 继续作为 Informed Decision Protocol Owner。

---

## 38. Supersession / Compatibility

本 Patch 不改写 F1～F8 v1.0 原冻结文件；作为 Audit Patch Layer 参与最终 v1.1 Consolidation。

---

## 39. Human Decision

用户明确：

```text
B4-PATCH-02 HUMAN_APPROVED
```

因此：

```text
AUDIT-PATCH-013 = HUMAN_APPROVED
B4-CHAIN-02 = ARCHITECTURALLY_RESOLVED
```

---

## 40. Authorization Boundary

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

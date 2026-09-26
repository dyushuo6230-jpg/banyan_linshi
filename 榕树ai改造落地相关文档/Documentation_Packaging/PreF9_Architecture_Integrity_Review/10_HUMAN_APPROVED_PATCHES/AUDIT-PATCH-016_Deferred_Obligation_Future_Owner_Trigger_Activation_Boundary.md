# AUDIT-PATCH-016 — Deferred Obligation Identity × Future Owner Resolution × Trigger / Activation Boundary × Closure / Supersession

> Formal Audit Patch ID: `AUDIT-PATCH-016`  
> Source Finding: `B6-CHAIN-01`  
> Source Approval ID: `B6-PATCH-01`  
> Status: `HUMAN_APPROVED`  
> Audit Batch: `Audit Batch 6 — Deferred / Future Owner / Boundary`  
> Classification: `GAP / P1`  
> Primary Scope: `F1～F8 Deferred / Future-stage Contracts`  
> Primary Owners: `Current Declaring Owner + Future Owning Stage`  
> Implementation Authorization: `NO`

---

## 1. Problem

Banyan 已大量正确使用：

```text
DEFERRED
NOT IMPLEMENTED
NOT FROZEN
FUTURE
OUT OF SCOPE
IMPLEMENTATION-OWNED
F9-OWNED
F10-OWNED
F11-OWNED
F12-OWNED
```

这些边界防止 Architecture 阶段过早冻结 SQLite DDL、Exact Schema、Runtime API、WebUI、Migration、Autonomous AI Learning 等实现细节。

缺口是：缺少一个 Banyan-wide Common Deferred Contract，确保某个事项今天被延期后，未来不会丢失 Owner、Trigger、Must-Happen-Before、Forbidden-before-resolution、Closure / Supersession 等治理信息。

---

## 2. Existing Good Pattern

F2 的：

```text
PHYSICAL_STORE_TOPOLOGY
```

已经提供高质量 Deferred 范例：

```text
Decision Owner Gate = STORAGE_IMPLEMENTATION_FREEZE

Prerequisites:
- F8_ARCHITECTURE_FREEZE_PASS
- F9_ARCHITECTURE_FREEZE_PASS
- F10_ARCHITECTURE_FREEZE_PASS

Must Happen Before:
- PERSISTENT_RUNTIME_DDL
- PERSISTENT_INDEX_DDL
- STORAGE_MIGRATIONS

Requires Human Decision = true
```

本 Patch 不修改该合同，而是将其治理能力推广为 Banyan-wide Common Deferred Contract。

---

## 3. Deferred Definition

正式：

```text
Deferred
=
the current architecture intentionally does not freeze
a later-owned decision / detail / capability,
while preserving enough boundary information
for safe downstream continuation
and deterministic future pickup.
```

因此：

```text
Deferred != Undefined
Deferred != Forgotten
Deferred != Unowned
Deferred != Authorized
```

---

## 4. Deferred != Architecture Gap

正式：

```text
Deferred != Architecture Gap
```

只要：

```text
Boundary Known
Owner Known / Deterministically Derivable
Trigger Known
Must-Happen-Before Known when applicable
Forbidden-before-resolution Known
Current Architecture does not require the answer
```

即可合法延期。

反之：

```text
Material Deferred
+ No Explicit Owner
+ No Deterministic Owner Resolution
= ARCHITECTURE GAP
```

---

## 5. Deferred Obligation

正式引入逻辑概念：

```text
Deferred Obligation
```

表示：

> 当前阶段明确保留给未来阶段 / Gate 解析的一项受治理义务。

它不是新的 F1 Top-level Object，也不是 Implementation Task。

正式：

```text
Deferred Obligation != Backlog Task
Deferred Obligation != Implementation Task
```

---

## 6. Minimum Logical Contract

Material Deferred 至少逻辑上应能回答：

```text
Subject / Topic
Deferred Question
Rationale
Declaring Owner
Future Owner
Trigger
Preconditions
Must-Happen-Before Boundary
Forbidden-Before-Resolution Boundary
Expected Resolution Output
Authority / Decision Requirement
Dependencies
Status
Provenance
Closure / Supersession
```

本 Patch 不冻结 physical schema，也不要求每个 Deferred 独立成文件。

---

## 7. No Global Deferred Authority

禁止：

```text
GlobalDeferredAuthority
UniversalFutureOwnerRegistry
```

正确结构：

```text
Common Deferred Contract
+
Domain-owned Deferred Declaration
+
Future Index / Discovery
```

---

## 8. Deferred Categories

逻辑上至少区分：

```text
Implementation Detail Deferred
Required Future Decision
Future Capability Reserved
Migration / Cutover Deferred
```

分类不等于 Priority。

普通 Exact Schema / Enum / API 等实现细节不应被过度治理；涉及 Authority、Canonical Truth、Owner、Compatibility、Storage Truth、Runtime Permission、Migration、Activation、Scope、Safety Boundary、Cross-stage Contract 的 Material Deferred 才需要强 Deferred Governance。

---

## 9. Future Owner Resolution

Future Owner 可以：

```text
Explicit
```

也可以：

```text
Deterministically Derived
```

例如：

```text
Index / Retrieval / Freshness / Impact → F9
Runtime Permission / Execution → F10
UX / Control Plane → F11
Migration / Retirement → F12
Canonical Mutation → F7
Project Binding / Reconciliation → F8
```

正式：

```text
Deterministically Derivable Owner
!= Unowned
```

无需为已能唯一解析的 Deferred 重复询问用户。

---

## 10. Declaring Owner / Future Owner Boundary

正式：

```text
Declaring Owner
!= Future Resolution Owner
```

当前阶段可以声明某未来问题为 Deferred，但不得因此预冻结 Future Owner 的 exact implementation。

反向也成立：

```text
Future implementation owner
cannot redefine upstream architecture semantics
```

---

## 11. Future Owner != Current Authorization

正式：

```text
Future Owner
!= Current Authorization

Assigned Future Stage
!= Activated Capability

Future Ownership
!= Current Implementation Permission
```

例如：

```text
F10 owns future Runtime implementation
```

不等于：

```text
F10 implementation is authorized now
```

---

## 12. Trigger

每个 Material Deferred 必须拥有明确：

```text
Resolution Trigger
```

推荐：

```text
Before F10 Runtime Implementation
Before Persistent DDL
When F9 Architecture Design Starts
Before Final Activation
When Legacy Migration Is Authorized
When a Future Capability Is Explicitly Proposed
```

正式：

```text
"When needed" alone
!= Sufficient Trigger
```

---

## 13. Trigger != Authorization

正式：

```text
Trigger Reached
!= Work Authorized
```

Trigger 到达只意味着：

```text
Deferred Obligation
→ Resolution Required
```

不自动意味着：

```text
Implementation Authorized
Migration Authorized
Canonical Mutation Authorized
Activation Authorized
```

---

## 14. Preconditions

正式区分：

```text
Trigger
!= Preconditions Satisfied
```

若 Trigger 已到但前置信息不足：

```text
Resolution Attempt
→ NOT_READY / UNKNOWN
```

不能为了清理 Deferred 提前拍板。

---

## 15. Must-Happen-Before

Material Deferred 在适用时必须明确：

```text
Must Be Resolved Before X
```

例如：

```text
Physical Store Topology
→ before Persistent DDL / Storage Migration

Runtime Permission concrete contract
→ before Real Runtime Activation

Legacy Migration / Retirement strategy
→ before Legacy Retirement
```

---

## 16. Forbidden-Before-Resolution / Deferred Guard

Material Deferred 还必须说明：

> 该义务被合法解决之前，哪些动作禁止。

逻辑上：

```text
Deferred Guard
=
a prohibition remaining active
until the Deferred Obligation is validly resolved
```

例如：

```text
Store Topology unresolved
→ no persistent DDL

Cutover unresolved
→ no canonical replacement

Retirement unresolved
→ no legacy retirement
```

正式：

```text
Deferred Guard != Authority
Convenience != Deferred Guard Override
```

---

## 17. Expected Resolution Output

Material Deferred 应描述未来结果类别，例如：

```text
Architecture Decision
Implementation Specification
Migration Plan
Runtime Contract
UX Contract
Physical Schema Freeze
Capability Approval
```

但：

```text
Expected Future Artifact Type
!= Need To Create Empty Artifact Now
```

---

## 18. Human Decision Boundary

正式：

```text
Deferred != Human Decision Required
```

只有：

```text
Multiple Legitimate Material Choices
+ Material Consequence
+ No Deterministic Governance Winner
```

才进入 existing Informed Decision / applicable Human Governance。

F2 `PHYSICAL_STORE_TOPOLOGY requires_human_decision = true` 保持不变。

---

## 19. Future Capability Reserved

例如：

```text
AI_AUTONOMOUS_LEARNING
```

当前应解释为：

```text
Future Capability Reserved
```

而不是：

```text
Required Future Implementation
```

正式：

```text
Future Extension Point != Roadmap Commitment
Future Capability Reserved != Current Capability
Future Extensibility != Current Authorization
```

未来真正提出启用时：

```text
Explicit Future Capability Proposal
→ Applicable Architecture / Governance Review
```

---

## 20. Deferred State Semantics

逻辑上至少允许：

```text
DEFERRED
READY_FOR_RESOLUTION
RESOLUTION_IN_PROGRESS
RESOLVED
SUPERSEDED
NOT_APPLICABLE
```

Exact enum deferred。

正式：

```text
DEFERRED != UNKNOWN
DEFERRED != UNRESOLVED
```

其中：

```text
DEFERRED
= current stage intentionally does not require resolution

UNKNOWN
= evidence insufficient

UNRESOLVED
= resolution is required now, but no valid result exists
```

---

## 21. Trigger / Deadline Transition

当 Trigger / Must-Happen-Before 到达：

```text
DEFERRED
→ RESOLUTION_REQUIRED / UNRESOLVED
```

若下游受保护动作试图继续：

```text
→ BLOCK
```

正式：

```text
Must-Happen-Before reached
→ cannot remain silently DEFERRED
```

---

## 22. Closure

Deferred Closure 表示：

> Future Owner 已依据合法 Contract 解决该义务。

但：

```text
Deferred Obligation Resolved
!= Implementation Completed

Implementation Completed
!= Activated

Deferred Resolution
!= Final Activation Authorization
```

---

## 23. Supersession / Not Applicable

未来新架构可能使 Deferred 不再适用。

正式：

```text
Deferred Superseded
!= Deferred Forgotten

SUPERSEDED
!= deleted history

NOT_APPLICABLE
!= Failure
```

必须保留为何关闭 / 被替代的 provenance。

---

## 24. Deferred History

逻辑上应能追踪：

```text
Who declared it?
Why was it deferred?
Original Trigger
Future Owner
Owner changes
Resolution
Supersession
Closure
```

不冻结 physical history storage。

---

## 25. Deferred Handoff

允许跨阶段：

```text
Deferred Handoff
```

传递：

```text
Deferred Topic
Frozen Boundary
Trigger
Dependencies
Forbidden Actions
Expected Future Resolution
```

但：

```text
Deferred Handoff
!= Current Authority Transfer

Deferred Handoff
!= Implementation Authorization
```

---

## 26. F9 / F11 / F12 Boundary

### F9

未来可以索引：

```text
Deferred Obligation
Future Owner
Trigger
Dependency
Must-Happen-Before
```

但：

```text
Index != Deferred Authority
Index Miss != Deferred Obligation Absent
```

### F11

未来可以展示 Pending Future Decisions / Upcoming Gates / Deferred Obligations。

但：

```text
UX Status != Resolution Authority
UX-owned != Governance Authority
```

### F12

未来负责 Legacy Reconciliation / Migration / Retirement Gates。

但：

```text
Migration-owned != Migration Authorized
Retirement Planning != Retirement Authorized
```

---

## 27. Implementation-owned Deferred

如果 Architecture Semantics 已充分冻结：

```text
Exact Go Interface
Exact Serialization
Exact Cache Representation
Exact Physical Enum
```

可以归 Implementation-owned。

正式：

```text
Implementation-owned Deferred
cannot silently redefine Architecture Contract
```

若 Implementation 发现 Architecture 语义需要变化：

```text
Implementation Evidence
→ Architecture Change Proposal
→ Applicable Owner
```

而不是让 Current Code 成为新 Architecture Truth。

---

## 28. Premature Deferred Activation

正式定义：

```text
Premature Deferred Activation
```

即：

> Deferred Gate 未满足 / 尚未合法解析时提前执行 Future Capability / Migration / Runtime / Canonical Change。

正式：

```text
Premature Deferred Activation
= FORBIDDEN
```

---

## 29. Existing High-risk Future Boundaries

### Physical Store Topology

继续由 F2 强 Gate 管理。

### Authority Cutover

现有 RP0 Rebaseline 已定义：

```text
RP2
= Artifact Authority Cutover / Discovery / Package Alignment
```

并保持：

```text
RP2 = NOT_AUTHORIZED
```

当前不得提前进入。

### Final Activation

现有 Stage16 / Stage17 Evidence 明确：

```text
Stage16
= Readiness only

Stage17
= PILOT / SHADOW only

PASS_PILOT_ONLY

final_activation = false
canonical_replacement = false
production_or_final_activation_authorized = false
```

因此 Final Activation 当前属于：

```text
High-impact Future Required Decision
```

Trigger 至少为：

```text
Explicit Future Final-Activation Proposal
+ applicable readiness / dependency gates
```

Resolution Authority：

```text
Applicable Human Governance
```

在获得新的明确授权前：

```text
Final Activation remains forbidden
```

### Legacy Retirement

现有 Owner Matrix 与 RP0：

```text
F12 / RP9
→ Legacy Reconciliation / Migration / Retirement
```

并已有：

```text
migration completeness
zero runtime dependency
rollback rehearsal
no valuable legacy capability unmapped
```

等 Exit Gate。

当前仍：

```text
Legacy Retirement = NOT_AUTHORIZED
```

---

## 30. FUTURE Bucket Boundary

正式：

```text
FUTURE != Owner
FUTURE != Miscellaneous Unowned Bucket
```

对于尚不存在的 Future Capability，Final implementation owner 可以延迟决定，但必须存在：

```text
Owner Resolution Gate
```

例如：

```text
Future Capability Proposal
→ resolve semantic owner
→ architecture / governance gate
```

因此 `AI_AUTONOMOUS_LEARNING` 可以继续合法处于 FUTURE / NOT_IMPLEMENTED，而不形成当前 Architecture Hole。

---

## 31. Deferred Dependency

Deferred 可以拥有 Planning / Governance Dependency，例如：

```text
F9 Physical Index
depends on
Storage Topology Decision
```

但：

```text
Deferred Planning Dependency
!= Runtime Resolution Dependency
```

若出现：

```text
A must resolve before B
B must resolve before A
```

则：

```text
Implicit Deferred Cycle = FORBIDDEN
```

必须在 Architecture / Planning 层处理。

---

## 32. Owner Conflict

如果多个 Stage 声称拥有同一 Future Decision：

```text
Owner Conflict
```

不得：

```text
Later Stage Wins
```

正式：

```text
Later Stage != Higher Authority
Implementation Detail != Architecture Authority
```

优先由 Existing Owner Matrix / Domain Semantics / Scope / Authority 确定性解析。

只有真正无法唯一解析时才进入 Human Governance。

---

## 33. Consolidation

F1～F8 v1.1 Consolidation 时应执行：

```text
Deferred Obligation Reconciliation
```

检查：

```text
Still Deferred
Resolved
Superseded
Not Applicable
Owner Changed
Boundary Changed
```

但：

```text
F1～F8 v1.1 Consolidation
!= Resolve All Deferred Implementation Details
```

只需要证明剩余 Deferred：

```text
safe
owned / owner-resolvable
bounded
future-recoverable
```

---

## 34. Architecture Hole Test

每个 Material Deferred 必须能够回答：

```text
If this is not decided now,
can currently authorized architecture
still remain correct and safe?
```

如果：

```text
YES
```

可以继续 Deferred。

如果：

```text
NO
```

则它其实是：

```text
Current Architecture Gap
```

正式：

```text
Needed for current semantic correctness
→ Architecture Gap

Not needed until future trigger
+ boundary known
→ Valid Deferred
```

---

## 35. Reliable Automatic Routing

继续：

```text
Reliable Automatic Routing
× Minimum Human Decision Governance
```

因此：

```text
Owner derivable → automatic
Trigger deterministic → automatic
Safe Deferred → no human interaction
```

仅 Owner genuinely ambiguous / Material Architecture Choice / Authority Conflict / High-risk Cutover-Migration 等真正判断缺口进入 Human Governance。

---

## 36. AI Boundary

AI 可以：

```text
Inventory Deferred Items
Classify Deferred Type
Resolve Deterministic Future Owner
Detect Missing Trigger
Detect Premature Activation
Detect Owner Conflict
Prepare Future Decision Package
```

AI 不得：

```text
Turn Deferred into Implemented
Invent Authority
Silently choose Material Future Architecture
Activate Future Capability
Treat Future Owner as Current Permission
Remove Deferred Guard
```

---

## 37. Banyan-wide Invariants

```text
Deferred != Undefined
Deferred != Forgotten
Deferred != Unowned
Deferred != Authorized

Deferred != Architecture Gap
when boundary / owner / trigger are sufficient

Unbounded Material Deferred
may be Architecture Gap

Deferred Obligation != Backlog Task
Deferred Obligation != Implementation Task

Future Owner != Current Authorization
Assigned Future Stage != Activated Capability

Trigger Reached != Work Authorized
Trigger Reached → Resolution Required

DEFERRED != UNKNOWN
DEFERRED != UNRESOLVED

Must-Happen-Before reached
→ cannot remain silently Deferred

Deferred Resolved != Implementation Completed
Implementation Completed != Activated
Deferred Resolution != Final Activation Authorization

Future Extension Point != Roadmap Commitment
Future Capability Reserved != Current Capability

Deferred Handoff != Authority Transfer
Deferred Handoff != Implementation Authorization

Index != Deferred Authority
Index Miss != Deferred Obligation Absent

Migration-owned != Migration Authorized
Retirement Planning != Retirement Authorized
Runtime-owned != Runtime Activated
UX-owned != Governance Authority

Implementation-owned Deferred
cannot redefine Architecture

Premature Deferred Activation = FORBIDDEN

FUTURE != Owner
FUTURE != Miscellaneous Unowned Bucket

Later Stage != Higher Authority
Implementation Detail != Architecture Authority

Deferred Governance Audit
!= Deferred Implementation Design

Reviewing Deferred
!= Freezing Implementation

Future Extensibility
!= Current Authorization
```

---

## 38. Forbidden Interpretations

禁止：

1. Deferred = TODO；
2. Deferred = 可以无人负责；
3. Deferred = 未来自动实现；
4. Future Owner = 当前 Implementation Authority；
5. 所有 Deferred 都是 Current Architecture Gap；
6. 所有 Deferred 都必须现在解决；
7. 所有 Deferred 都必须人工审批；
8. 所有 Deferred 都必须建立独立 Artifact；
9. `FUTURE` = 通用 Owner；
10. `when needed` 永远是充分 Trigger；
11. Must-Happen-Before 到达后仍静默 Deferred；
12. F9 Index 获得 Deferred Authority；
13. F10 Future Owner = Runtime 已授权；
14. F11 UX Owner = Governance Authority；
15. F12 Migration Owner = Cutover Authority；
16. Implementation 以实现方便为由改写 Frozen Architecture；
17. Deferred Audit 自动进入 Implementation Design；
18. Batch 6 提前冻结 Exact DDL / Schema / API；
19. Extension Point = Roadmap Commitment；
20. Future Capability = Current Capability；
21. AI 自动激活 Future Capability；
22. Later Stage 自动覆盖 Earlier Owner；
23. Current Code 自动成为 Architecture Truth；
24. Deferred Handoff 转移当前 Authority；
25. Deferred Resolution 自动等于 Activation Authorization；
26. Pilot Success 自动等于 Final Activation；
27. RP2 Planned 自动等于 RP2 Authorized；
28. Legacy Retirement Owner 自动获得 Retirement Authorization；
29. 本 Patch 授权 Implementation / RP2 / Final Activation。

---

## 39. Deferred by This Patch

本 Patch 自身不冻结：

```text
Exact Deferred enum
Deferred Record Schema
Deferred Registry
Deferred Index Schema
Deferred ID Format
Deferred file path
Trigger engine
Notification engine
Dashboard
CLI
WebUI
Automation implementation
```

---

## 40. No-Loss Mapping

本 Patch 保留并补充：

- F1 Closed-but-extensible Core；
- F2 Physical Store Topology Deferred Gate；
- F3 Taxonomy Change Gate；
- F4/F5/F6/F7/F8 Owner Matrix；
- F7 Governed Change / Canonical Apply；
- F8 Project Instance Boundary；
- F9 Future Index / Freshness / Impact；
- F10 Future Runtime；
- F11 Future UX；
- F12 Future Migration / Retirement；
- RP0 Rebaseline 的 RP2 Cutover / RP9 Retirement 规划；
- Stage16 Readiness-only / Stage17 Pilot-only 边界；
- 所有 `Implementation / RP2 / Authority Cutover / Final Activation / Legacy Retirement = NOT_AUTHORIZED` 边界。

---

## 41. Human Decision

用户明确：

```text
B6-PATCH-01 HUMAN_APPROVED
```

因此：

```text
AUDIT-PATCH-016 = HUMAN_APPROVED
B6-CHAIN-01 = ARCHITECTURALLY_RESOLVED
```

---

## 42. Authorization Boundary

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

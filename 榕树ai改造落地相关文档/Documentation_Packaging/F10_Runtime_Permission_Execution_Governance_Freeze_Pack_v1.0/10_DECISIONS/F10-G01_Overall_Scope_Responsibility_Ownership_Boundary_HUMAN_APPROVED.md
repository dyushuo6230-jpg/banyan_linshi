# F10-G01 — Overall Scope / Responsibility / Ownership Boundary

**阶段：** F10 — Runtime Permission / Execution Governance Architecture  
**主题：** F10 总体范围、职责与 Owner 边界  
**状态：** `HUMAN_APPROVED`  
**类型：** Architecture Governance Decision  
**Implementation Authorization：** `NO`

---

## 1. 决策目的

F10 用于解决 Banyan 从“已经知道当前任务是什么、适用于哪里、当前上下文是什么”进入“真正准备执行某个具体动作”以后所需要的运行时治理问题。

F10 的核心责任不是重新解释：

- 产品需求；
- UI / Design（设计）；
- Project Identity（项目身份）；
- Project Binding（项目绑定）；
- Canonical Truth（规范事实）；
- Canonical Change（规范变更）；

而是解决：

> **在当前 Task（任务）/ Action（动作）、Scope（范围）、Context（上下文）、Authorization（授权）、Gate（关卡）、Provider（提供方）以及运行环境下，这个具体动作现在是否能够合法、安全、可靠地继续执行，以及执行过程中应如何受控。**

正式：

```text
F10
=
Task / Action Scoped
Runtime Permission
+
Execution Governance
```

---

## 2. F10 在整体 Banyan 中的位置

当前总体责任链为：

```text
F5
Product / Requirement Governance

↓

F6
Design / UI Governance

↓

F7
Governed Change / Canonical Apply

↓

F8
Project Instance
Binding
Profile
Provider Binding
Project Runtime Handoff

↓

F9
Scope / Context / Freshness
Dependency / Impact
Retrieval / Projection / Cache
Current Applicable Derived State

↓

F10
Runtime Permission
Point-of-use Validation
Runtime Routing
Execution Governance
Runtime Recovery

↓

Actual Execution
```

正式：

```text
F9 Context Ready
!=
Runtime Authorized
```

因此 F10 不重复 F9，而是消费 F8 / F9 及其他 Applicable Domain Owner（适用领域责任方）已经提供的有效输入。

---

## 3. F10 Primary Owner

F10 的 Primary Owner（主要责任）正式定义为：

```text
Task / Action Scoped Runtime Execution Governance
```

即：

> 针对某一次具体任务或动作，解析其当前运行条件，验证其执行资格，决定是否可以继续，并控制实际执行过程。

F10 不拥有：

```text
Project-global semantic authority
Repository-global authority
Banyan-global authority
```

因此：

```text
Task / Action Scoped Runtime Decision
!=
Global Governance Decision
```

---

## 4. Project / Module / Scope Boundary

正式保持：

```text
Project Identity
!= Git Repository

Project Identity
!= Directory

Project Identity
!= Module
```

一个 Banyan Project 可以：

```text
Project
├── platform-admin
├── tenant-admin
├── backend
├── miniapp
├── h5
├── shared
└── other modules
```

Git Repository（Git 仓库）可以是当前 Project Instance 的主要物理承载方式，但：

```text
Git Repository
!= Project Definition
```

同一 Project 可以未来跨多个 Git Repository。

一个 Git Repository 也可以在适用治理下承载多个逻辑 Project / Project Instance。

F10 不负责重新定义 Project Identity。

---

## 5. Module / Source Scope Boundary

`tenant-admin`、`platform-admin`、`backend`、`miniapp` 等通常属于：

```text
Application
Module
Source Role
Source Binding
Task Scope
```

而不是因为目录独立就自动成为独立 Project。

例如：

```text
Project = x_shop

Task Scope =
tenant-admin.goods
+
backend.goods
+
applicable shared contract
```

这是正常的单 Project 多模块开发。

因此：

```text
Cross-directory
!= Cross-project

Cross-module
!= Scope Violation

Dependency-discovered module
!= Material Scope Expansion
```

---

## 6. Dynamic Task Scope

F10 消费的是：

```text
Current Effective Task / Action Scope
```

该 Scope 可以依据已有合法事实和规则进行确定性解析。

正式区分：

### 6.1 Deterministic Scope Resolution

如果：

```text
Task semantics
+
Dependency
+
Project mapping
+
Applicable rules
```

可以唯一确定一个新的相关模块属于本次任务，则：

```text
Automatic Scope Resolution
→ Continue
```

不要求人工重新批准。

例如：

```text
tenant-admin.goods
↓ dependency resolution
backend.goods
```

若 `backend.goods` 明确属于同一业务任务：

```text
!= Material Scope Expansion
```

### 6.2 Implementation Surface Discovery

实现过程中发现必须共同修改：

```text
api
service
model
shared types
tests
```

若这些内容属于已经确定的任务语义，则：

```text
Implementation Surface Discovery
!= New Governance Scope
```

不得因为发现新文件或新目录频繁打扰用户。

### 6.3 Material Scope Expansion

只有当准备进入：

```text
new business domain
new authority domain
new protected target
new materially different semantic objective
```

且不能从原任务确定性推导时，才属于：

```text
Material Scope Expansion
```

此时：

```text
Pause affected action
→ Route applicable Owner
→ Re-resolution
```

F10 不自行扩大 Authority。

---

## 7. F10 Responsibility Domains

F10 总体拥有以下运行时责任。

### 7.1 Runtime Permission Resolution

F10 负责判断：

> 当前这一次动作，在当前有效治理条件下是否允许执行。

可能形成运行时状态，例如：

```text
ALLOW
BLOCK
PAUSE
NEEDS_INPUT
```

Exact enum（精确枚举）本 G01 不冻结。

### 7.2 Point-of-use Validation

在真正执行受保护动作前，F10 负责验证会影响合法执行的 Current Effective Preconditions（当前有效前置条件）。

可能包括：

```text
Scope
Authorization validity
Gate state
Expected base
Freshness
Provider compatibility
Execution environment
Deferred Guard
```

但：

```text
Point-of-use Validation
!= Full Architecture Re-resolution
```

只检查当前动作需要的相关条件。

### 7.3 Runtime Provider Resolution

F10 可以从当前已经治理有效的 Provider Candidate Set（提供方候选集合）中，为当前动作解析实际 Provider。

正式：

```text
Runtime Provider Resolution
!= Provider Binding Authority
```

F10：

```text
may select within valid governed candidates
```

但：

```text
may not silently enlarge valid candidate set
```

### 7.4 Adapter Routing

F10 负责将合法动作路由到合适的 Adapter（适配器），例如：

```text
Git Adapter
Filesystem Adapter
Editor Adapter
CLI Adapter
HTTP Adapter
Future Adapter
```

正式：

```text
Adapter
= Execution Channel

Adapter
!= Permission Authority
```

### 7.5 Execution Lifecycle Governance

F10 负责运行时执行生命周期语义，包括但不限于：

```text
Prepare
Validate
Execute
Pause
Resume
Retry
Cancel
Complete
Fail
```

Exact State Machine（精确状态机）延后到后续 F10 Decision 冻结。

### 7.6 Runtime Failure / Recovery

F10 负责分类并处理运行时失败和恢复。

例如：

```text
temporary provider failure
network interruption
execution environment change
stale prerequisite
target mismatch
adapter failure
```

能够确定性恢复的：

```text
Automatic Recovery
```

无法安全确定的：

```text
Route applicable Owner
```

### 7.7 Runtime Result / Evidence / Trace

F10 可以产生：

```text
Execution Result
Observation
Evidence
Trace
Failure Evidence
Mismatch Evidence
Runtime State
```

但：

```text
Execution Result
!= Canonical Truth

Trace
!= Authority

Observation
!= Semantic Decision

Runtime Success
!= Final Activation
```

---

## 8. F10 Does Not Own

F10 明确不拥有：

```text
Product Requirement Authority
Design Authority
Canonical Truth Authority
Project Identity Authority
Project Binding Authority
Provider Definition Authority
Canonical Mutation Authority
Global Scope Authority
Global Authorization Authority
Human Governance Authority
Migration / Retirement Authority
Final Activation Authority
```

---

## 9. Later Stage != Higher Authority

正式继承：

```text
Later Stage
!= Higher Authority
```

因此 F10 虽然最接近实际执行，也不得覆盖前置领域 Owner。

例如：

```text
Runtime detects product mismatch
→ route Product Owner
```

而不是：

```text
Runtime rewrites requirement
```

同样：

```text
Runtime detects design mismatch
→ route Design Owner
```

而不是：

```text
Runtime rewrites design semantics
```

---

## 10. Runtime Permission != Authority

F10 的 Runtime Permission（运行时许可）属于：

```text
Current Action Execution Decision
```

不是：

```text
Semantic Authority
```

正式：

```text
Runtime ALLOW
!= Authorization

Runtime ALLOW
!= Authority

Runtime ALLOW
!= Canonical Truth

Runtime ALLOW
!= Project Semantic Decision
```

---

## 11. Runtime Permission Composition

逻辑上：

```text
Runtime Permission
depends on:

Applicable Authorization
+
Current Effective Scope
+
Applicable Preconditions
+
Current Gate State
+
Provider / Adapter Eligibility
+
Point-of-use Validity
```

这只是逻辑关系，本 G01 不冻结具体计算方式、字段或算法。

---

## 12. Authorization Boundary

F10 不建立：

```text
GlobalAuthorizationAuthority
```

Authorization 可以来源于不同治理 Owner。

F10 负责：

```text
consume
validate
enforce
```

Applicable Authorization。

正式：

```text
F10 validates Authorization
!= F10 universally creates Authorization
```

---

## 13. Provider Boundary

F8 继续负责：

```text
Provider Binding
Provider Selection Governance
Project-scoped Provider Context
```

F10 负责：

```text
Runtime Provider Resolution
Runtime Provider Availability
Applicable Runtime Fallback
```

例如：

```text
Governed Candidates:
A
B

Primary = A
Fallback = B
```

若：

```text
A unavailable
+
B remains semantically compatible
+
B remains authorized
```

则：

```text
F10 may automatically select B
```

无需人工确认。

但如果只有新 Provider C 可以继续，而 C 不属于当前治理候选：

```text
F10 must not silently activate C
```

---

## 14. Provider Availability != Semantic Eligibility

正式：

```text
Provider Available
!= Provider Eligible

Provider Healthy
!= Provider Authorized

Provider Capable
!= Provider Semantically Compatible
```

F10不得因为 Provider 技术上可调用，就自动扩大合法使用范围。

---

## 15. Adapter Boundary

Adapter 主要负责：

```text
how to execute
```

而不是：

```text
whether execution is allowed
```

因此：

```text
Permission Resolution
→ before protected execution
```

Adapter 不独立获得治理 Authority。

---

## 16. Retry Boundary

正式：

```text
Retry
!= Blind Repeat
```

对于确定性的临时技术故障：

```text
same action
same valid scope
same valid authorization
same valid target
same required preconditions
```

可以自动 Retry。

如果 Material Condition（重要条件）发生变化，则：

```text
Retry
→ Revalidation
```

而不是直接重复。

---

## 17. Pause Boundary

正式：

```text
Pause
!= Failure

Pause
!= Cancel
```

F10 可以因为：

```text
temporary unavailable condition
stale prerequisite
provider outage
target mismatch
required revalidation
```

暂停受影响动作。

Pause 不自动取消整个 Task。

---

## 18. Resume Boundary

正式：

```text
Resume
!= Blind Continue
```

恢复前根据实际变化进行 Targeted Revalidation（定向再校验）。

如果相关条件仍然有效：

```text
Automatic Resume
```

如果条件已经变化：

```text
Re-resolution / Route Owner
```

---

## 19. Cancel Boundary

正式：

```text
Cancel
!= Rollback
```

停止未来执行动作和撤销已经发生的改变属于不同语义。

Rollback（回滚）的具体 Owner 和 Contract 不在本 G01 提前冻结。

---

## 20. Failure Boundary

正式：

```text
Execution Failure
!= Authorization Revoked

Execution Failure
!= Source Invalid

Execution Failure
!= Requirement Invalid

Execution Failure
!= Design Invalid
```

Runtime Failure 是 Evidence（证据）。

是否影响上游语义由对应 Domain Owner 判断。

---

## 21. Runtime Uncertainty Boundary

正式：

```text
Runtime Uncertainty
!= Human Decision Required
```

出现不确定状态时，系统应优先尝试：

```text
targeted revalidation
deterministic re-resolution
governed fallback
recoverable retry
context refresh
```

只有仍存在：

```text
Material Semantic Choice
Authority Conflict
Material Scope Expansion
Multiple Legitimate Incompatible Outcomes
High-impact Governance Decision
```

才进入 Human Governance。

---

## 22. Reliable Automatic Routing × Minimal Human Decision

F10 正式遵循：

```text
Reliable Automatic Routing
×
Minimal Human Decision Governance
```

普通确定性运行时工作应自动完成。

例如：

```text
scope resolution
provider availability check
compatible fallback
adapter routing
freshness check
ordinary retry
recoverable resume
runtime precondition validation
```

不得因为治理机制存在，就将正常开发过程变成人工审批流水线。

---

## 23. Human Attention Boundary

Human Decision（人工决策）不是 F10 正常执行链的固定步骤。

只有：

```text
machine cannot reliably resolve
OR
governance explicitly requires human authority
```

时才占用人的注意力。

正式：

```text
Governance Cost
must not be shifted to Human by default
```

---

## 24. F9 / F10 Boundary

F9 继续拥有：

```text
Index
Retrieval
Context Selection
Context Assembly
Freshness Evidence
Fingerprint / Change Detection
Dependency / Potential Impact
Derived Projection / Cache
Deferred Obligation Discovery
```

F10 消费这些结果用于运行时治理。

正式：

```text
F9 Current Context
!= F10 Permission

F9 Freshness Evidence
!= F10 Authorization

F9 Impact Discovery
!= Scope Expansion Authorization
```

---

## 25. F8 / F10 Boundary

F8 继续拥有：

```text
Project Identity
Project Instance
Source Mapping
Location Binding
Profile Instance
Project Facts
Provider Binding
Version Pin
Feature / Gate Project State
```

F10 消费 F8 的 Task-scoped Runtime Handoff。

正式：

```text
Runtime Handoff
!= Project Truth Copy

Runtime ALLOW
!= Project Binding Decision
```

---

## 26. F7 / F10 Boundary

F7 继续拥有适用范围内的：

```text
Governed Change
Canonical Apply
Revision
History
Supersession
Canonical Mutation Governance
```

F10 可以执行已经合法授权的受治理动作，但：

```text
Runtime Executor
!= Canonical Mutation Authority
```

发现 Apply 前提失效时：

```text
Pause
→ Evidence
→ Applicable Re-resolution
```

F10不得自行重写 Change Authority。

---

## 27. Protected Action Boundary

F10 可以作为受保护动作执行前的重要运行时 Gatekeeper（守门层）。

但：

```text
Gatekeeper
!= Authority Owner
```

其作用是：

```text
check
enforce
block unsafe continuation
route mismatch
```

不是产生新的领域 Authority。

---

## 28. Point-of-use Efficiency

F10不得采用：

```text
every action
→ full repository scan
→ full architecture reload
→ full authority recomputation
```

正确原则：

```text
Action
→ Current Scope
→ Required Context
→ Relevant Preconditions
→ Targeted Revalidation
→ Execute
```

正式：

```text
Reliability
!= Full Scan Every Time
```

同时：

```text
Performance Optimization
must not remove governance-critical meaning
```

---

## 29. Current Implementation Reality Boundary

现有 Runtime Code、Stage14 / Stage15 Runtime Evidence、Pilot / Shadow 实现可作为：

```text
Evidence
Compatibility Input
Implementation Reality
```

但：

```text
Current Code
!= F10 Architecture Authority
```

如果当前代码与正式 F10 Architecture 冲突：

```text
Architecture Decision
→ Implementation Alignment later
```

不得因为已有实现方便，就反向修改架构语义。

---

## 30. Current Runtime Safety State

F10 Architecture Stage 当前继续保留：

```text
Current Project Execution = DRY_RUN_ONLY where currently governed

Canonical Write = BLOCKED

Protected Business Write = BLOCKED

Pilot / Shadow
!= Final Activation
```

这些当前事实不因为 F10 Architecture Entry 自动解除。

---

## 31. Deferred Obligation Boundary

F10 必须继承所有 Materially Relevant Deferred Obligations（仍有实质相关性的延期义务）。

正式：

```text
F10 Entry
!= Deferred Closure

Future Owner
!= Current Authorization

Trigger Reached
!= Implementation Authorized
```

对于属于 F10 Future Owner 的 Deferred：

```text
trigger reached
→ resolution required
```

但仍须依据 Applicable Authorization Boundary 判断可以进行到哪个层级。

---

## 32. AI Autonomous Capability Boundary

当前 F10 不引入：

```text
AI Autonomous Learning
AI Autonomous Policy Mutation
AI Autonomous Authority Promotion
AI Autonomous Canonical Promotion
AI Autonomous Governance Rewrite
```

F10 可以：

```text
deterministically resolve
automatically route
automatically validate
automatically recover
```

但这些：

```text
!= Autonomous Governance Evolution
```

未来 AI Learning（AI 学习）只保留扩展边界，不在 F10 激活。

---

## 33. Architecture / Implementation Separation

本 G01 只冻结 Logical Architecture Boundary（逻辑架构边界）。

不冻结：

```text
Exact Runtime API
Exact Go Interface
Exact Python Interface
Exact State Enum
Exact Permission Enum
Exact Provider API
Exact Adapter Interface
Exact Retry Algorithm
Exact Timeout
Exact Database Schema
Exact Serialization
Exact Directory Structure
Exact Runtime Storage
Exact Event Bus
Exact RPC
Exact Queue
Exact Trace Storage
```

这些应由后续 F10 Decision 或未来 Implementation Stage 依据需要处理。

---

## 34. Core Invariants

F10-G01 正式建立以下总体不变量：

```text
Runtime Permission
!= Authority

Runtime ALLOW
!= Authorization

Runtime Result
!= Canonical Truth

Runtime Observation
!= Semantic Decision

Execution Failure
!= Upstream Semantic Invalidity

Project
!= Git Repository

Module
!= Project by default

Cross-module
!= Cross-project

Deterministic Scope Resolution
!= Material Scope Expansion

Implementation Surface Discovery
!= New Governance Scope

Provider Available
!= Provider Eligible

Provider Selection at Runtime
!= Provider Binding Authority

Adapter
!= Permission Authority

Retry
!= Blind Repeat

Pause
!= Failure

Resume
!= Blind Continue

Cancel
!= Rollback

Runtime Uncertainty
!= Human Decision Required

Point-of-use Validation
!= Full Architecture Re-resolution

Later Stage
!= Higher Authority

Gatekeeper
!= Authority Owner

Execution Result
!= Final Activation

Future Owner
!= Current Authorization
```

---

## 35. Forbidden Interpretations

明确禁止：

1. 把 F10 解释成 Banyan 全局 Authority；
2. 把 Runtime ALLOW 当成新的 Authorization；
3. 把 Runtime ALLOW 当成 Canonical Truth；
4. 把 F10 当成 Product / Design / Project Owner；
5. 把一个 Git Repository 永久定义为一个 Project；
6. 把 `tenant-admin` 这样的模块默认定义成独立 Project；
7. 因为跨目录就要求人工 Scope 扩展；
8. 因为跨 Module 就视为 Scope Violation；
9. 把实现过程中发现 API / Service / Test 文件视为新的 Governance Scope；
10. Provider 技术可用就自动认为治理可用；
11. F10 任意添加未治理 Provider；
12. Adapter 自行决定权限；
13. Retry 不校验变化直接重复执行；
14. Resume 不检查 Material Condition 直接继续；
15. Runtime Failure 自动推翻上游 Requirement / Design；
16. Runtime Unknown 自动升级成人工审批；
17. 每个动作都重新扫描完整仓库；
18. 为减少 Token 而丢弃 Scope / Authority / Gate 等治理关键含义；
19. Current Code 反向成为 Architecture Truth；
20. F10 Architecture Entry 自动授权 Implementation；
21. F10 Future Owner 自动获得当前 Implementation Permission；
22. Pilot / Shadow 成功自动等于 Final Activation；
23. Runtime Result 自动获得 Canonical Mutation Authority；
24. F10 自行突破现有 Deferred Guard；
25. 建立 Runtime God Object 吞并所有领域 Owner。

---

## 36. Current Hard Prohibitions

继续保持：

```text
Implementation = NOT_AUTHORIZED

RP2 = NOT_AUTHORIZED

Authority Cutover = NOT_AUTHORIZED

Canonical Replacement = NOT_AUTHORIZED

Final Activation = NOT_AUTHORIZED

Legacy Retirement = NOT_AUTHORIZED

SQLite Physical Schema = NOT_FROZEN
```

F10-G01 Approval 不改变以上状态。

---

## 37. Relationship to Later F10 Decisions

F10-G01 只建立 Overall Boundary。

后续可在此边界下继续讨论：

```text
Runtime Permission Model

Authorization Validation

Execution Context

Provider Runtime Resolution

Adapter Boundary

Execution Lifecycle

Pause / Resume / Retry / Cancel

Point-of-use Revalidation

Failure / Recovery

Result / Evidence / Trace

Stage Exit / F11 Handoff
```

具体 Dxx 编号和拆分，应根据后续讨论自然形成，不在 G01 中为了目录整齐提前固定数量。

---

## 38. Acceptance Meaning

用户已明确批准：

```text
F10-G01 HUMAN_APPROVED
```

因此正式成立：

```text
F10 Overall Scope = FROZEN
F10 Responsibility Boundary = FROZEN
F10 Ownership Boundary = FROZEN
Project / Module / Runtime Scope Interpretation = FROZEN
Runtime Authority Separation = FROZEN
Automatic Routing / Human Escalation Principle = FROZEN
```

但不表示批准任何：

```text
Implementation
Physical API
Runtime write activation
RP2
Authority Cutover
Final Activation
Legacy Retirement
```

---

## 39. Approval Status

```text
F10-G01 = HUMAN_APPROVED
```

普通：

```text
好的
下一步
继续
按建议
```

均不视为后续 Decision 的批准。

---

**END**

# F10-D06 — Runtime Result × Evidence × Trace × Acceptance Boundary

**阶段：** F10 — Runtime Permission / Execution Governance Architecture  
**主题：** Runtime Result（运行结果）× Evidence（证据）× Trace（追踪）× Acceptance（接受）边界  
**状态：** `HUMAN_APPROVED`

**上游依赖：**
- `F10-G01 HUMAN_APPROVED`
- `F10-D01 HUMAN_APPROVED`
- `F10-D02 HUMAN_APPROVED`
- `F10-D03 HUMAN_APPROVED`
- `F10-D04 HUMAN_APPROVED`
- `F10-D05 HUMAN_APPROVED`

**Implementation Authorization：** `NO`

---

## 1. 决策目的

F10-D06 解决：

> 一个 Runtime Action 执行以后，Banyan 应如何表达“实际发生了什么”“凭什么相信”“执行过程怎么发生”“哪个层级有权接受这个结果”，并防止 Provider Success、日志、Trace 或物理 Mutation 被错误升级成 Product / Design / Canonical Acceptance。

核心关系：

```text
Execution
↓
Runtime Result
↓
Evidence / Trace
↓
Applicable Validation
↓
Runtime Action Acceptance
↓
Domain-specific downstream acceptance where required
```

---

## 2. 四个核心概念必须分离

```text
Runtime Result
!= Evidence
!= Trace
!= Acceptance
```

---

## 3. Runtime Result 定义

Runtime Result 回答：

> 当前 Action / Execution Attempt 实际发生了什么。

可描述：

```text
requested operation
observed execution outcome
target state
known side effect
validation outcome
provider / adapter route
failure / recovery outcome
material qualifiers
```

但不自动形成上游 Semantic Truth。

---

## 4. Evidence 定义

Evidence 回答：

> 为什么系统有理由相信某个 Result / Claim。

例如：

```text
Provider response
Target inspection
File fingerprint
Git diff
Test result
Validation result
Expected Base observation
Adapter observation
Runtime state inspection
```

---

## 5. Trace 定义

Trace 回答：

> 这个 Result 是通过什么运行过程形成的。

例如：

```text
Action
→ Attempt 1
→ Provider A timeout
→ State Reconciliation
→ No Side Effect
→ Fallback Provider B
→ Attempt 2
→ Validation
→ Complete
```

---

## 6. Acceptance 定义

Acceptance 回答：

> 当前结果是否满足某个拥有明确 Owner 的 Contract（合同）。

不同领域的 Acceptance 不属于同一个 Authority。

---

## 7. Result / Evidence / Trace / Acceptance 基础边界

```text
Runtime Result != Canonical Truth
Evidence != Authority
Evidence != Authorization
Trace != Authority
Trace != Authorization
Trace != Runtime Permission
Trace != Canonical Truth
Trace != Acceptance
```

---

## 8. Provider / Adapter Success 边界

Provider 返回 SUCCESS 首先只是 Provider Result Evidence。

```text
Provider Success != Runtime Action Accepted
Adapter Success != Runtime Action Accepted
Execution Completed != Execution Accepted
```

---

## 9. Mutation / Canonical Apply 边界

继续继承 F7：

```text
Mutation Completed != Canonical Apply Succeeded
File Write != Canonical Apply
Git Commit != Canonical Apply
```

---

## 10. Result 层级

```text
Execution Attempt Result
↓
Action Result
↓
Task / Workflow Result
```

并在需要时连接 Domain Result。

```text
Attempt Result != Action Result
Action Result != Task Result
F10 Execution Result != F7 Apply Result
Attempt Result != Apply Result != Change Result
```

---

## 11. Runtime Result 最小语义

Material Runtime Result 应能在逻辑上解释：

```text
Task Ref where applicable
Action Ref
Attempt Ref
Scope
Target
Operation
Outcome
Side-effect state
Validation state
Runtime route
Relevant permission / authorization refs
Material qualifiers
Evidence refs
Downstream obligations
```

Exact Schema 不冻结。

---

## 12. Outcome 不能只有 SUCCESS / FAILED

逻辑上必须允许表达：

```text
Completed
Failed
Cancelled
Blocked
Paused
Partial / Mixed
Outcome Unknown
No Change Required
Skipped where applicable
```

Exact Enum 不冻结。

---

## 13. 非 Failure 状态边界

```text
Cancelled != Failed
Blocked != Failed
Outcome Unknown != Failed != Success
No Change Required != Failed
Skipped != Failed
```

---

## 14. Partial Result

允许：

```text
Partial / Mixed Result
```

正式：

```text
Partial Completion != Full Success
Partial Completion != Whole Task Failure
```

需要依据 Dependency / Required Obligations 判断。

---

## 15. Side-effect State 与 Validation State

Runtime Result 在相关情况下应保留：

```text
Known No Side Effect
Known Side Effect
Side Effect Unknown
Partial Side Effect
```

并保持：

```text
Mutation State != Validation State
```

例如：

```text
Mutation = COMPLETED
Validation = FAILED
```

不能压缩成单一 SUCCESS。

---

## 16. Runtime Action Acceptance

F10 自己可以接受的是：

> 当前 Runtime Action 是否满足其 Applicable Execution Contract。

可能需要：

```text
correct target
expected operation occurred
required side-effect state known
required validation passed
required execution guarantees satisfied
required evidence available
no unresolved runtime blocker
```

---

## 17. Acceptance Owner Boundary

```text
Runtime Action Acceptance != Product Acceptance
Runtime Action Acceptance != Design Acceptance
Runtime Action Acceptance != F7 Canonical Acceptance
Later Executor != Higher Authority
```

谁能 Acceptance，由“哪个 Contract 被接受”决定，而不是谁最后执行。

---

## 18. F7 Canonical Acceptance

对于 F7 Canonical Apply：

```text
Mutation
→ Post-Mutation Validation
→ Reconciliation
→ Canonical Acceptance
```

继续归 F7。

F10向 F7 提供：

```text
Execution Result
Actual Mutation Evidence
Validation Evidence
Attempt / Recovery Evidence
Expected Base observation
Trace / Provenance refs
```

但不代替 F7 Acceptance。

---

## 19. Result Qualifier Preservation

正式：

```text
Result without required qualifiers
!= Same Semantic Result
```

Scoped Result 必须保持 Scope 可解释。

如果影响安全解释，应保留适用：

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
Deferred Guard
Material Downstream Obligation
```

---

## 20. Positive Result 不能吞掉 Blocking State

```text
One positive Result
!= Override applicable HOLD / BLOCKED
```

Result Compression 不能变成 Governance Compression。

---

## 21. Evidence Projection

Evidence 跨组件 / 跨阶段传递时不要求复制完整 Body。

允许：

```text
Evidence Ref
Evidence Type
Relevant Claim
Provenance
Summary / Outcome
```

正式：

```text
Evidence Preservation != Full Evidence Duplication
```

---

## 22. Provenance

Material Evidence / Result 在需要时应能回答：

```text
Where did this come from?
Who / what produced it?
For what Action / Attempt?
For what Scope?
Under what relevant basis?
```

但：

```text
Provenance != Authority
Evidence Provider != Semantic Owner
```

---

## 23. Material Runtime Trace

Trace 聚焦真正影响：

```text
Permission decision
Execution start / completion
Provider / Adapter route
Fallback
Pause
Resume
Retry
Cancel
Failure
Recovery
Validation
Material side effect
Runtime Acceptance
Owner routing
```

的事件。

---

## 24. Traceability != Log Everything

不要求把所有：

```text
internal read
token
temporary thought
irrelevant low-level operation
```

升级成治理 Trace。

是否记录应考虑：

```text
governance relevance
execution relevance
recovery relevance
audit relevance
explainability relevance
```

---

## 25. Trace != Hidden Model Chain-of-thought

运行时应保存：

```text
decision basis
applicable rule
evidence refs
reason / reason code
result
route / lifecycle event
```

而不是依赖模型私有推理链。

---

## 26. Explainable Basis

Material 自动决策应能够解释：

```text
What happened?
Why did the system take this route?
What governed basis allowed it?
What evidence supported it?
```

但：

```text
Explainability != Authority
```

---

## 27. Downstream Obligation

Runtime Result 可以产生或保留：

```text
Downstream Obligation
```

例如：

```text
Mutation completed
Test required
Acceptance pending
Revalidation required
```

因此：

```text
Runtime Result Produced != All Obligations Resolved
```

---

## 28. Acceptance Pending

如果：

```text
Mutation = completed
Validation = pending
```

则不能提前标记最终 Accepted。

逻辑上允许：

```text
Execution Completed
Acceptance Pending
```

Exact 状态名不冻结。

---

## 29. Result Closeout Boundary

Action 是否可正式完成，应依据：

```text
Applicable Execution Contract
+
Required Validation
+
Required Runtime Obligations
```

而不是 Provider response。

---

## 30. Historical Result Preservation

例如：

```text
Attempt 1 = FAILED
Attempt 2 = SUCCESS
```

不能最终只剩：

```text
SUCCESS
```

从而丢失恢复链。

正式：

```text
Current Action Result != Individual Historical Attempt Results
New Runtime Result != Erase Previous Attempt Evidence
```

---

## 31. History / Trace 不产生 Current Effective

历史可作为：

```text
diagnostic evidence
health evidence
provenance
recovery input
```

但：

```text
History != Current Effective Authority
```

---

## 32. Runtime Result 的下游消费

F10 Result 可以作为：

```text
F7 acceptance evidence
F8 drift / health evidence
F9 index / lookup input
F11 presentation input
```

但被多个阶段消费不提升 Authority。

---

## 33. F9 Boundary

F9 可支持：

```text
Result Lookup
Failure History Lookup
Health Evidence Lookup
Provenance Lookup
Index / Retrieval
```

但：

```text
F9 Index != Runtime Result Authority
Indexed Runtime Result != Canonical Truth
Search Rank != Authority
```

---

## 34. F11 Control Plane Boundary

F11未来可以消费：

```text
Runtime State
Runtime Result
Trace
Evidence refs
Failure state
Pause reason
Provider route
Recovery state
Human-action requirement
```

用于 Control Plane UX。

但：

```text
F11 UI != Runtime Authority
```

---

## 35. UI Action State 必须来自受治理状态

未来 F11 不得自行把：

```text
BLOCKED
```

放宽成可执行 Action。

正式：

```text
Button Enabled != Authorization
UI displays ALLOW != UI grants ALLOW
Trace rendered in UI != Authorization
```

---

## 36. UX Simplification != Governance Semantic Loss

F11 可以做白话化展示，但不能丢掉影响用户判断的：

```text
Status
Scope
Reason
Blocking state
Required user action if any
Relevant trace / evidence
Recovery state
```

---

## 37. Human Attention Boundary

如果 Runtime 可以自动：

```text
retry
refresh
fallback
reconcile
route owner
```

则 Result 不应错误标记：

```text
User Action Required
```

正式：

```text
Failure occurred != User must be interrupted
```

---

## 38. Result Reason

Material Result 应尽量支持清晰 Reason。

例如：

```text
BLOCKED
Reason:
Authorization revoked
```

但：

```text
Reason Code != Authority
```

---

## 39. 与 D01～D05 的关系

D01：
`Permission Result / basis`

D02：
`Execution Context basis`

D03：
`Provider / Adapter route`

D04：
`Attempt / Lifecycle`

D05：
`Failure / Recovery routing`

D06：
`Result / Evidence / Trace / Runtime Acceptance / Downstream handoff`

---

## 40. Runtime Result 不得创造上游状态

明确：

```text
Runtime Result
!= Durable Provider Binding

Runtime Result
!= Scope Expansion Authorization

Runtime Result / Failure
!= Deferred Obligation Automatically

Runtime Evidence
!= Canonical Mutation Authority
```

---

## 41. Result Projection / Cache

允许：

```text
Result Projection
Trace Index
Evidence Index
```

但：

```text
Projection != Source Result Authority
Cached Result != Eternal Current Result
```

需要 Current 时仍应结合适用 Freshness / Current Effective Basis。

---

## 42. Sensitive Evidence Boundary

Evidence / Trace 不应因为可追踪要求就默认复制：

```text
credentials
secrets
unnecessary sensitive payload
```

正确原则：

```text
Minimum Necessary Evidence
```

足以支持 Material Runtime Claim 和 Recovery 即可。

---

## 43. Success Evidence 同样重要

Trace 不只记录 Failure。

Material Success 也应在需要时保留 Evidence，例如：

```text
protected mutation completed
validation passed
fallback selected
action accepted
```

---

## 44. Model / Provider-neutral Result Contract

Result Core 不应硬编码：

```text
CodexSuccess
CursorSuccess
ClaudeSuccess
```

Provider 名称只属于 Runtime Route Evidence。

更换 AI Provider 后，只要遵守同样 Contract，Result / Evidence / Trace 语义应保持稳定。

---

## 45. Acceptance Depth 可按 Action 变化

不同 Action 类型可有不同 Execution Acceptance Requirements。

```text
Same Result Framework
!= Same Acceptance Cost
```

普通 Read、Code Write、Git Commit、Protected Mutation 可以有不同 Validation Depth。

---

## 46. Acceptance Failure

如果：

```text
Execution Completed
+
Acceptance Not Satisfied
```

应进入 D05 Failure Classification / Recovery Routing。

正式：

```text
Runtime Acceptance Failure
!= Automatic Rollback
```

---

## 47. Runtime Result 可驱动 Workflow，但不拥有 Workflow

F4 / Workflow 可以消费：

```text
Action completed
blocked
failed
cancelled
partial
```

决定后续节点。

但：

```text
Runtime Result != Workflow Authority
```

---

## 48. Consumer-specific Projection

不同 Consumer 可以获取不同 Result Slice。

例如 F11 可能只需要：

```text
status
reason
user action
```

F7 可能需要：

```text
mutation evidence
validation evidence
expected-base observation
```

但：

```text
Projection for Consumer
!= Change underlying Runtime Result semantics
```

---

## 49. Result Integrity

跨阶段传递必须保持：

```text
same relevant meaning
+
required qualifiers preserved
```

如果 Consumer 所需关键限定缺失：

```text
→ UNKNOWN / UNRESOLVED
```

不得猜 PASS。

---

## 50. Evidence Missing / Conflict

```text
Evidence Missing != Claim False
```

但如果 Acceptance 必须依赖该 Evidence：

```text
Missing Required Evidence
→ cannot accept claim
```

若 Evidence 存在 Material Conflict：

```text
preserve conflict
→ route applicable owner / reconciliation
```

禁止选择方便的 Winner。

---

## 51. Evidence Authority Boundary

```text
Latest Evidence != Highest Authority
More Evidence != More Authority
```

---

## 52. Architecture / Implementation Separation

D06 不冻结：

```text
Exact Result Enum
Exact Result Schema
Exact Evidence Schema
Exact Trace Event Schema
Exact Audit Storage
Exact Trace Storage
Exact Result Database
Exact Retention Policy
Exact Event Bus
Exact Reason Code List
Exact Log Format
Exact UI Payload
Exact API Endpoint
Exact Serialization
Exact Hashing
Exact Compression
Exact Storage Technology
```

---

## 53. Current Hard Prohibitions

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

---

## 54. AI Autonomous Boundary

F10 可以自动：

```text
construct Runtime Result
attach Evidence refs
emit Material Trace
evaluate Runtime Execution Contract
route downstream Result
```

但不代表 AI 可以：

```text
promote Evidence to Authority
declare Product Acceptance
declare Design Acceptance
declare Canonical Acceptance outside F7
modify governance policy
hide blocking qualifiers
```

---

## 55. Core Invariants

```text
Runtime Result != Evidence != Trace != Acceptance
Runtime Result != Canonical Truth
Evidence != Authority
Evidence != Authorization
Trace != Authority
Trace != Authorization
Trace != Runtime Permission
Trace != Canonical Truth
Trace != Acceptance
Provider Success != Runtime Action Accepted
Adapter Success != Runtime Action Accepted
Execution Completed != Execution Accepted
Mutation Completed != Canonical Apply Succeeded
Attempt Result != Action Result
Action Result != Task Result
F10 Result != F7 Apply Result
Apply Result != Change Result
Mutation State != Validation State
Runtime Action Acceptance != Product Acceptance
Runtime Action Acceptance != Design Acceptance
Runtime Action Acceptance != Canonical Acceptance
Later Executor != Higher Authority
Result without required qualifiers != Same Semantic Result
Evidence Preservation != Full Evidence Duplication
Provenance != Authority
Evidence Provider != Semantic Owner
Traceability != Log Everything
Trace != Hidden Model Chain-of-thought
Partial Completion != Full Success
Partial Completion != Whole Task Failure
Runtime Result Produced != All Obligations Resolved
F11 UI != Runtime Authority
UI Display != Authorization
Indexed Runtime Result != Canonical Truth
Recovery Result != Original Action Result
More Evidence != More Authority
Latest Evidence != Highest Authority
```

---

## 56. Forbidden Interpretations

明确禁止：

1. Provider SUCCESS 直接等于 Action 最终接受；
2. Adapter 成功直接等于业务目标成功；
3. File Write / Git Commit 直接等于 Canonical Apply 成功；
4. 最后 Attempt SUCCESS 删除之前 Failure 历史；
5. Runtime Result 自动成为 Canonical Truth；
6. Evidence 自动产生 Authority / Authorization；
7. Trace 自动产生 Authorization / Runtime Permission；
8. 历史 ALLOW 自动授权未来 Action；
9. Trace Event 写入即等于 Acceptance；
10. 为审计无限记录低价值内部细节；
11. 把私有推理链作为审计合同；
12. Result 只支持 SUCCESS / FAILED；
13. Cancelled / Blocked / Unknown 全部错误归类 Failure；
14. Partial Completion 自动视为 Full Success；
15. Result 投影时丢失 Scope / HOLD / BLOCKED / Freshness；
16. Mutation 成功但 Validation Pending 时提前宣布 DONE；
17. Runtime Acceptance 升级为 Product / Design / Canonical Acceptance；
18. F9 Index 成为 Result Authority；
19. F11 UI 创造或放宽 Runtime Permission；
20. Trace UI 渲染成 Authorization；
21. Runtime Result 自动修改 Provider Binding / Scope；
22. Failure Evidence 自动修改 Canonical Truth；
23. Missing Required Evidence 时猜 PASS；
24. Evidence Conflict 时选择方便 Winner；
25. Latest Evidence 自动压过 Authority；
26. D06 Approval 自动授权 Implementation / Real Write / Final Activation。

---

## 57. 与 F7 / F9 / F11 的关系

F7继续拥有：

```text
Apply Attempt
Apply Result
Canonical Acceptance
Change Result
Semantic Rollback
Change Closeout
```

F9只支持 Result / Evidence / Trace / Provenance 的查询、索引和恢复，不拥有 Result Authority。

F11未来负责 Control Plane UX 与结果展示，但：

```text
F11 UI != Runtime Decision Authority
```

受保护 Action 仍必须经过 F10 Runtime Contract。

---

## 58. 后续边界

D06 不完整冻结：

```text
Cross-action execution orchestration
Runtime batch / parallel coordination
F10 stage exit
F10 → F11 formal handoff
F10 final review / freeze closure
```

---

## 59. Acceptance Meaning

用户已明确批准：

```text
F10-D06 HUMAN_APPROVED
```

因此正式成立：

```text
Runtime Result / Evidence / Trace / Acceptance separation
Attempt / Action / Task Result layering
F10 Result remains separate from F7 Apply / Change Result
Provider / Adapter success is only execution evidence
Runtime Acceptance only accepts Execution Contract
Product / Design / Canonical Acceptance remain domain-owned
Result qualifiers must survive handoff
Evidence supports claims but creates no Authority
Trace records material execution history but grants no Permission
Partial / Cancelled / Blocked / Unknown outcomes remain expressible
Downstream obligations prevent premature completion
F9 may index / retrieve but not own Result semantics
F11 may present Runtime state but cannot loosen or create Permission
```

但不表示批准 Exact Result / Evidence / Trace Schema、Acceptance Algorithm、Audit Storage、Retention Policy、F11 UI Payload、Implementation、Real Project Write、RP2、Authority Cutover、Canonical Replacement、Final Activation 或 Legacy Retirement。

---

## 60. Approval Status

```text
F10-D06 = HUMAN_APPROVED
```

普通“好的 / 下一步 / 继续 / 按建议继续”均不代表后续 Decision 的批准。

---

**END**

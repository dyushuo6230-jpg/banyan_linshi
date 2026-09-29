# F10-D05 — Failure Classification × Recovery Routing × Containment Boundary

**阶段：** F10 — Runtime Permission / Execution Governance Architecture  
**主题：** Failure Classification（失败分类）× Recovery Routing（恢复路由）× Containment（影响收敛）边界  
**状态：** `HUMAN_APPROVED`  
**上游依赖：**
- `F10-G01 HUMAN_APPROVED`
- `F10-D01 HUMAN_APPROVED`
- `F10-D02 HUMAN_APPROVED`
- `F10-D03 HUMAN_APPROVED`
- `F10-D04 HUMAN_APPROVED`

**Implementation Authorization：** `NO`

---

## 1. 决策目的

F10-D05 解决：

> 当 Runtime 发现异常、失败、不一致、阻塞、未知结果或恢复失败时，应如何判断“这到底是什么问题、影响到哪里、真正由谁负责解决、下一步应该自动恢复还是路由上游治理”。

核心流程：

```text
Observed Abnormal Condition
↓
Classify
↓
Capture Evidence
↓
Determine Affected Scope / Blast Radius
↓
Resolve Semantic Owner
↓
Resolve Recovery Options
↓
Deterministic?
├─ YES → Automatic Recovery
└─ NO  → Governance Routing
          ↓
        Human only if genuine judgment gap
```

---

## 2. Failure Detection != Failure Ownership

正式：

```text
Failure detected by F10
!= Failure semantically owned by F10
```

F10 是最接近执行的一层，所以经常最先发现问题。

但最先发现：

```text
!=
拥有该领域的最终解释权
```

---

## 3. Runtime Failure != Semantic Authority

正式：

```text
Runtime Failure
!= Semantic Authority
```

F10 可以：

```text
detect
classify
capture
contain
route
recover where authorized
```

但不能因为执行失败就修改上游语义。

---

## 4. Operational Failure 与 Governed Exception 分离

继续继承：

```text
Operational Exception
!= Governed Exception
```

Operational Failure（运行异常）描述执行过程中实际发生的问题。

Governed Exception（受治理例外）表示：

> 明确请求突破或例外适用某个既有 Rule / Boundary。

因此：

```text
Operational Failure
!= Automatic Exception Request
```

---

## 5. Failure Classification != Recovery Decision

正式：

```text
Failure Classification
!= Recovery Decision
```

知道：

```text
Provider Failure
```

不自动等于：

```text
Retry
```

恢复路径仍需要结合当前状态和治理条件解析。

---

## 6. Failure Cause != Fixed Recovery Action

正式：

```text
Same Failure Cause
may produce
different Recovery Routes
```

例如：

```text
Provider unavailable
```

可能形成：

```text
Retry
Fallback
Pause
Route F8
Block
```

取决于当前实际条件。

---

## 7. Failure Classification 的用途

分类主要用于回答：

```text
What failed?
Why?
What subject / scope is affected?
Who owns semantic resolution?
What recovery paths are eligible?
```

不是为了建立庞大的错误码体系。

---

## 8. D05 不冻结完整 Error Enum

本 Decision 不提前冻结：

```text
ERROR_001
ERROR_002
...
```

也不冻结技术栈专属一级分类。

Exact Failure Taxonomy（精确分类体系）延后。

---

## 9. Core Failure Categories

逻辑上至少允许表达以下类别：

```text
Operational / Infrastructure Failure
Provider Failure
Adapter Failure
Context / Freshness Failure
Dependency / Availability Failure
Permission / Authorization Failure
Target / Expected Base Mismatch
Validation Failure
Binding / Project Reality Mismatch
Governance Block
Semantic Conflict
Outcome / Reality Unknown
Recovery Failure
```

具体名称不冻结。

---

## 10. Technology-neutral Failure Model

Core 不应以：

```text
GitError
CursorError
CodexError
VueError
GoError
```

作为主要治理分类。

这些可以作为：

```text
Technical Reason / Evidence
```

但不能锁死 Core。

---

## 11. Runtime-recoverable Failure

Runtime-recoverable Failure 表示：

> 不改变原任务语义、Scope、Authority 和治理目标，可以在现有授权边界内通过确定性运行时操作恢复。

例如：

```text
temporary network interruption
temporary provider outage
adapter transient failure
refreshable stale context
governed compatible fallback
safe retry
safe resume
```

---

## 12. Runtime-recoverable Failure 的处理

如果符合既有治理：

```text
F10 Recovery Orchestration
→ Automatic
```

不要求人工。

---

## 13. Governance-affecting Failure

当问题涉及：

```text
Authority
Authorization
Material Scope
Product Meaning
Design Meaning
Project Binding
Canonical Apply semantics
Material Security Boundary
```

则属于：

```text
Governance-affecting condition
```

F10不得自行改变这些语义。

---

## 14. Governance-affecting Failure 的处理

正确：

```text
Pause / contain affected execution
↓
Capture Evidence
↓
Route Applicable Domain Owner
↓
Re-resolution
↓
Return updated governed result
↓
F10 revalidate / resume if allowed
```

---

## 15. Reality Unknown

继续继承 D04：

```text
Outcome Unknown
```

并在 D05 中进一步规定：

```text
Unknown
!= Operational Failure
!= Semantic Conflict
!= Human Decision
```

Unknown 首先表示：

> 现实状态还没有解析清楚。

---

## 16. Reality Unknown 的第一动作

优先：

```text
Inspect
Reconcile
Resolve actual state
```

而不是：

```text
Retry immediately
Ask human immediately
```

---

## 17. Error != Failure

继续保持：

```text
Error
!= Failure
```

例如某个内部调用产生 error，但系统通过合法 fallback 完成目标，则最终 Action 不一定 Failure。

---

## 18. Attempt Failure != Action Failure

正式继承 D04：

```text
Attempt Failure
!= Final Action Failure
```

可能继续：

```text
Retry
Fallback
Recovery
Resume
```

---

## 19. Action Failure != Workflow / Task Failure

正式：

```text
Action Failure
!= Task Failure
!= Workflow Failure
!= Goal Failure
```

是否向上扩散，需要看 Dependency 和 Workflow Contract。

---

## 20. Failure 必须绑定 Subject

Material Failure 至少在逻辑上应能识别：

```text
Subject
Operation / Action
Attempt
Scope
Expected
Observed
Relevant Dependency
Provider / Adapter where applicable
Mutation / side-effect state
Impact
Resolution Owner
```

Exact Schema 不冻结。

---

## 21. Failure Evidence != Canonical Truth

正式：

```text
Failure Evidence
!= Canonical Semantic Truth
```

Failure Evidence 可以触发：

```text
Retry
Fallback
Recovery
Reconciliation
Re-resolution
Change Candidate
```

但不直接修改目标语义。

---

## 22. Failure Evidence != Authority

同样：

```text
Failure Evidence
!= Authority
```

错误记录不能自己授权后续 Mutation。

---

## 23. Validation Failure 边界

正式：

```text
Validation Failure
!= Product Semantic Decision
```

验证失败说明某个验证条件没有满足，不自动说明 Requirement wrong / Design wrong / Code definitely wrong。

---

## 24. Validation Failure 必须继续分类原因

例如：

```text
Compile Failure
Contract Validation Failure
Acceptance Validation Failure
Apply Validation Failure
Design Consistency Failure
```

可能分别路由不同 Owner。

---

## 25. Validation Failure != Automatic Rollback

正式：

```text
Validation Failure
!= Rollback Everything
```

必须结合 Cause / Side Effect / Atomicity / Scope / Recovery Contract 判断。

---

## 26. Dependency Failure

Dependency unavailable 不要求下游统一变成 FAILED，可以根据语义解析为 UNKNOWN / BLOCKED / STALE / UNAFFECTED / DEGRADED where governed。

---

## 27. Source Unavailable != Source Invalid

继续继承既有 F9 边界：

```text
Source Unavailable
!= Source Invalid
```

临时无法获取事实不能自动推翻事实本身。

---

## 28. Provider Failure != Binding Invalid

正式继续：

```text
Provider Failure
!= Provider Binding Invalid
```

即使多次失败，也首先形成 Health / Compatibility / Drift Evidence，而不是自动 Durable Rebinding。

---

## 29. Adapter Failure != Provider Invalid

继续：

```text
Adapter Failure
!= Provider Invalid
```

可优先尝试同 Provider 的其他合法 Adapter。

---

## 30. Runtime Failure != Semantic Conflict

正式：

```text
Operational Failure
!= Semantic Conflict
```

例如网络 timeout 不是产品语义冲突。

---

## 31. Divergence != Conflict

继续保持：

```text
Divergence != Conflict
Stale != Invalid
```

差异可以是可确定性 reconciliation 的输入。

---

## 32. Semantic Conflict != Retryable Failure

正式：

```text
Semantic Conflict
!= Retryable Failure
```

如果真实存在两个互斥语义，重复执行不能解决。

---

## 33. Governance Block != Operational Failure

Authorization missing、Gate = BLOCKED、Governed HOLD、Scope unauthorized 属于 Governance State，不是普通技术故障。

```text
Governance Block
!= Operational Failure
```

---

## 34. Retry 不能绕过 Governance Block

```text
Retry cannot bypass Governance Block
```

---

## 35. Fallback 不能绕过 HOLD

```text
Fallback cannot bypass Governed HOLD
```

---

## 36. Technical Recovery != Gate Override

```text
Technical Recovery != Gate Override
```

恢复机制没有额外 Authority。

---

## 37. Failure Blast Radius

D05 正式引入 Failure Blast Radius，表示一个 Failure 实际会影响哪些 Execution / Action / Dependency / Scope。

---

## 38. Blast Radius 不是严重度

```text
Blast Radius != Severity
```

---

## 39. 最小必要 Containment

```text
Failure Scope
↓
Dependency / Atomicity Analysis
↓
Minimum Necessary Containment Scope
```

---

## 40. Local Failure != Global Project Failure

```text
Local Operational Failure
!= Global Project Failure
```

---

## 41. Partial Failure != Global Failure

```text
Partial Failure
!= Global Project Failure
```

需要根据 Dependency / Atomicity / Scope / Required-vs-Optional relation 判断影响。

---

## 42. Failure Propagation 必须经过 Dependency Evaluation

禁止：

```text
Action A FAILED
→ copy FAILED to everything downstream
```

正确：

```text
Upstream Failure Evidence
↓
Dependency Evaluation
↓
Downstream derives appropriate state
```

---

## 43. Unaffected 必须允许存在

如果其他 Action 与故障无 Material Dependency，应保持 UNAFFECTED，不能为了简单统一全部暂停。

---

## 44. Failure Containment × Atomicity

如果适用 F7 Atomicity Contract：

```text
Failure Containment must preserve Atomicity Boundary
```

---

## 45. Failure Severity Boundary

未来可有 warning / error / critical 等 Severity，但：

```text
Severity != Owner
```

---

## 46. Severity != Recovery Strategy

```text
Critical != Always Human
Warning != Always Continue
```

---

## 47. Warning != BLOCKED

```text
Warning != BLOCKED
```

---

## 48. Violation != Governed Exception

```text
Violation != Governed Exception
```

---

## 49. Recovery Routing

Recovery Routing 的目标是把问题送到真正拥有其语义解决权的 Owner，而不是默认送给用户。

---

## 50. Route to Owner != Ask Human

```text
Route Domain Owner
!= Ask Human
```

很多 Domain Owner 是自动 Resolver / Rule / Reconciliation Contract。

---

## 51. Recovery Routing 不是固定阶段回退

禁止：

```text
F10 Failure → always F9
F10 Failure → restart F1-F9
```

正确：

```text
identify affected semantic domain
→ route only necessary owner
```

---

## 52. F5 Routing

Product Meaning / Requirement Gap / Material Product Conflict / Product-level Decision → F5 / Product Governance。

---

## 53. F6 Routing

Design Meaning / Design Drift / UI semantic conflict / Design validation / repair governance → F6。

---

## 54. F7 Routing

Apply Scope / Expected Base semantic conflict / Apply Plan / Partial canonical mutation / Canonical Acceptance / Semantic Rollback / Compensating Change boundary → F7。

---

## 55. F8 Routing

Project Identity / Instance / Binding / Provider Binding / Version Compatibility / Feature / Gate Project State / Project Reality Drift / Project Reconciliation → F8。

---

## 56. F9 Routing

Freshness / Index / Retrieval evidence / Dependency / Impact lookup / Context Recovery / Provenance lookup / Failure history / health evidence lookup → F9。

```text
F9 Index / Telemetry != Failure Authority
```

---

## 57. F10 Routing

F10 自己继续拥有 Runtime Invocation / Runtime Permission enforcement / Provider runtime resolution / Adapter execution routing / Runtime Attempt / Runtime Retry enforcement / Runtime Pause / Resume coordination / Technical recovery orchestration。

```text
F10 Runtime Failure != Semantic Authority
```

---

## 58. F4 Workflow Boundary

F4 继续拥有 Workflow-level 的 Retry / Pause / Resume / Skip / Replace / Partial Blocking / Escalation / Workflow coordination。

F10-D05 负责 Action / Attempt runtime enforcement + runtime recovery routing。

```text
Workflow Control Semantics
!= Concrete Runtime Attempt Handling
```

---

## 59. F4 × F10 不重复 Owner

Workflow 决定某 Action 是否允许 retry；F10 决定当前具体 Attempt 现在是否安全 retry。两层责任互补。

---

## 60. Recovery Eligibility

Automatic Recovery 必须同时满足：

```text
deterministic
within existing authorization envelope
no semantic-intent change
no material scope expansion
no gate bypass
required evidence / history preserved
applicable safety constraints satisfied
```

---

## 61. Automatic Recovery First

满足条件时，Automatic Recovery 优先于人工。

---

## 62. Recovery Action != Governance Exemption

```text
Recovery Action != Governance Exemption
```

---

## 63. Recovery Action 仍走 D01 Permission

write / retry mutation / switch provider / resume 等 Recovery Action 仍必须满足适用 Runtime Permission。

---

## 64. Recovery × D03 Provider Fallback

```text
D03 resolves route
↓
D01 validates execution eligibility
↓
D04 creates / resumes Attempt
```

Provider 不得自行切换。

---

## 65. Recovery × D02 Context

Context Failure 使用 D02 / F9 targeted refresh，只更新必要 Slice，不默认重新加载整个 Task。

---

## 66. Recovery × F8 Binding

Provider Binding / Project Binding 本身已不适用时，F10 不自行修复 Binding，应路由 F8。

---

## 67. Technical Recovery != Reconciliation

```text
Technical Recovery != Reconciliation
```

---

## 68. Reconciliation != Re-resolution

```text
Reconciliation != Re-resolution
```

---

## 69. Re-resolution != Semantic Rollback

```text
Re-resolution != Semantic Rollback
```

---

## 70. Recovery Success != Original Operation Success

```text
Technical Recovery Success
!= Original Action Success
```

恢复成功只说明系统回到安全可继续位置。

---

## 71. Recovery Success != Canonical Acceptance

```text
Recovery Success != Canonical Acceptance
```

---

## 72. Degraded Mode Boundary

D05 承认 Degraded Mode 可以作为某些 Domain 的受治理运行状态，但：

```text
Degraded != Unrestricted Success
```

---

## 73. Degraded Mode 不能自动降低 Governance

```text
Degraded Mode
!= Ignore Permission
!= Ignore Scope
!= Ignore Gate
!= Ignore Safety
```

---

## 74. Fallback Active != Primary Recovered

```text
Fallback Active != Primary Recovered
```

---

## 75. Failure != Deferred Obligation Automatically

```text
Failure != Deferred Obligation Automatically
```

---

## 76. Repeated Failure

重复 Failure 可以产生 Health Evidence / Compatibility Evidence / Drift Evidence / Operational History，但：

```text
Repeated Failure
!= Durable Rebinding
!= Semantic Invalidity
```

---

## 77. Failure History 的作用

历史可用于 runtime diagnosis / health evidence / recovery decision input / trend observation，但：

```text
History != Authority
```

---

## 78. Recovery Option Resolution

恢复策略根据：

```text
Failure Classification
+
Current Runtime State
+
Blast Radius
+
Governed Recovery Options
+
Permission / Scope / Authority
```

动态解析。

---

## 79. Recovery Option 不是固定 if-error

禁止把 Provider Error→retry exactly 3、Context Error→full reload、Validation Error→rollback 作为通用架构法则。

---

## 80. Multiple Recovery Paths

如果多个 Recovery Path 可由既有治理规则唯一确定，Automatic Resolve。

---

## 81. Multiple Recovery Paths != Human Decision

```text
Multiple Recovery Paths != Human Decision Required
```

---

## 82. Human Escalation Boundary

只有最终存在：

```text
Material Semantic Choice
Authority Conflict
Material Scope Expansion
High-risk Irreversible Action
Governed Exception Request
Unknown material side effect that cannot be reconciled
Multiple Legitimate Incompatible Recovery Strategies
```

且没有确定性 Winner 时，才进入 Human Governance。

---

## 83. Operational Failure != Human Decision Required

```text
Operational Failure != Human Decision Required
Recovery Failure != Immediate Human Decision
Failure != Human Judgment
```

---

## 84. Human Escalation 前的系统义务

在问人之前，系统应优先完成适用的 classification / evidence capture / blast-radius analysis / retry eligibility / fallback eligibility / technical recovery / reconciliation / owner routing / deterministic re-resolution。

---

## 85. Ask Human 不是 Error Handler

```text
Human != Default Error Handler
```

---

## 86. Recovery Failure

某次 Recovery Attempt 自身失败，应再次分类，不能因为 recovery failed once 立刻找人。

---

## 87. Recovery Failure 可以有自己的 Owner

fallback adapter failed 仍可能是 Runtime Infrastructure；reconciliation reveals semantic conflict 则应路由 Semantic Owner。

---

## 88. Failure Handling Order 不是固定 Call Order

```text
Observe
Classify
Capture Evidence
Resolve Scope / Owner
Resolve Recovery Eligibility
Route / Recover
```

这些是逻辑检查维度，不是固定 Runtime Call Order。

---

## 89. Failure Handling Order != Authority Priority

```text
Later Recovery Handler != Higher Authority
```

---

## 90. Locality / Speed

```text
local failure
→ local evidence
→ local owner
→ local recovery
```

---

## 91. No Full-system Recovery by Default

禁止 Any Failure → reload all architecture → rescan all repositories → recompute all stages。

---

## 92. Recovery 必须可解释

Material Recovery Decision 应能够回答 What failed / What was affected / Why this recovery / Which Owner or Rule allowed it / Did Scope and Authorization remain valid。

---

## 93. Recovery Provenance != Authority

```text
Recovery Provenance != Authority
```

---

## 94. Runtime Evidence 可以返回上游

Failure Evidence / Drift Evidence / Runtime Observation / Provider Health Evidence 可以交回对应 Owner，但：

```text
Evidence Delivery != Semantic Decision
```

---

## 95. Execution Result / Failure 不自动修改 Project Truth

```text
Runtime Failure != Automatic Project State Mutation
```

---

## 96. Failure × Permission

Failure 后的新 Recovery Action 不得盲用旧 ALLOW；相关 Material Basis 变化时使用 D01 targeted revalidation。

---

## 97. Failure × Context

旧 Execution Context 不自动永久有效，只刷新受影响 Context Slice。

---

## 98. Failure × Provider Route

旧 Provider Route 失败不等于所有 Provider Route 都失效；D03 定向解析剩余合法路线。

---

## 99. Failure × Attempt

D04 负责 same Action → new Attempt；D05 负责 whether / where recovery should route。

---

## 100. Failure × Deferred State

失败触发已有 Deferred Obligation Trigger 时，Trigger Reached 仍不等于 Implementation Authorized。

---

## 101. Current Safety State

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

D05 Approval 不改变这些状态。

---

## 102. Architecture / Implementation Separation

D05 不冻结 Exact failure enum / error codes / severity levels / retry counts / recovery algorithm / backoff / circuit breaker / monitoring stack / alerting stack / health score / failure database / trace schema / queue / scheduler / logging format / degraded-mode implementation。

---

## 103. AI Autonomous Boundary

允许 Automatic Classification / Owner Routing / Retry Eligibility / Fallback Eligibility / Technical Recovery / deterministic Reconciliation。

但不代表 AI invents Authority / changes semantic intent / expands Scope / approves governed exception / rewrites policy / promotes runtime evidence to truth。

---

## 104. Core Invariants

```text
Failure Detection != Failure Ownership
Runtime Failure != Semantic Authority
Operational Exception != Governed Exception
Failure Classification != Recovery Decision
Failure Cause != Fixed Recovery Action
Error != Failure
Attempt Failure != Action Failure
Action Failure != Task Failure
Failure Evidence != Canonical Truth
Failure Evidence != Authority
Validation Failure != Product Semantic Decision
Validation Failure != Automatic Rollback
Provider Failure != Provider Binding Invalid
Adapter Failure != Provider Invalid
Operational Failure != Semantic Conflict
Semantic Conflict != Retryable Failure
Governance Block != Operational Failure
Retry cannot bypass Governance Block
Fallback cannot bypass Governed HOLD
Local Failure != Global Project Failure
Partial Failure != Global Project Failure
Blast Radius != Severity
Severity != Owner
Severity != Recovery Strategy
Route Owner != Ask Human
Recovery Action != Governance Exemption
Technical Recovery != Reconciliation
Reconciliation != Re-resolution
Re-resolution != Semantic Rollback
Recovery Success != Original Operation Success
Recovery Success != Canonical Acceptance
Degraded != Unrestricted Success
Fallback Active != Primary Recovered
Failure != Deferred Obligation Automatically
Repeated Failure != Durable Rebinding
Multiple Recovery Paths != Human Decision Required
Operational Failure != Human Decision Required
```

---

## 105. Forbidden Interpretations

明确禁止：

1. F10 发现 Failure 就认为 F10 拥有语义解决权；
2. 所有 Failure 都归 Runtime；
3. 所有 Runtime Error 都等于 Action Failure；
4. Attempt Failure 自动等于 Task Failure；
5. Provider Failure 自动删除 Provider Binding；
6. Adapter Failure 自动判定 Provider 无效；
7. Timeout 自动解释成 Semantic Conflict；
8. Validation Failure 自动判定产品需求错误；
9. Validation Failure 自动 Rollback Everything；
10. Governance Block 当普通技术错误 Retry；
11. 用 Fallback 绕过 HOLD；
12. 用 Recovery 绕过 Authorization；
13. Local Failure 自动扩大成 Project Failure；
14. 一个 Action 失败就重跑整个 Task；
15. Failure 传播不做 Dependency Analysis；
16. Severity 高就自动转人工；
17. Severity 低就自动继续；
18. Recovery Success 自动等于 Action Success；
19. Recovery Success 自动等于 Canonical Acceptance；
20. Degraded Mode 自动放宽 Permission / Gate；
21. Fallback 正在工作就认为 Primary 已恢复；
22. 一次 Failure 自动生成 Deferred Obligation；
23. 重复 Failure 自动永久 Rebind Provider；
24. Recovery Action 免除 D01 Permission；
25. 多个 Recovery Option 自动询问用户；
26. 用户成为默认 Error Handler；
27. F10 为方便自己修改 F7/F8/F9 Semantic State；
28. Failure Evidence 自动升级为 Canonical Truth；
29. 任意 Failure 导致完整 F1～F10 重算；
30. D05 Approval 自动授权 Implementation / 真实写入 / Final Activation。

---

## 106. 与 F4 的关系

F4 继续负责 Workflow-level Retry / Pause / Resume / Skip / Replace / Partial Blocking / Escalation / Workflow Coordination。

F10 负责 Action / Attempt 级 Runtime Enforcement。两者 complement, not replace。

---

## 107. 与 F7 的关系

F7 继续负责 Apply Failure / Partial Mutation / Expected Base / Technical Recovery boundary for Apply / Semantic Rollback / Compensating Change / Canonical Acceptance / Apply Result / Closeout。

F10 发现相关问题后路由 F7，不重新解释 F7 语义。

---

## 108. 与 F8 的关系

F8 继续负责 Project Reality Reconciliation / Binding / Provider Binding / Fallback Governance / Version Compatibility / Project Drift / Project Re-resolution。

F10 不做 Durable Rebinding。

---

## 109. 与 F9 的关系

F9 继续负责 Failure Evidence Lookup / History / Health Evidence / Freshness / Dependency / Impact / Provenance / Context Recovery。

```text
Index / Telemetry != Failure Authority
```

---

## 110. 与 D01～D04 的关系

D01：Recovery Action still needs Runtime Permission。  
D02：Recovery refreshes only necessary Execution Context slices。  
D03：Provider / Adapter failures use governed route resolution。  
D04：Pause / Resume / Retry / Attempt / Outcome Unknown provide lifecycle mechanics。  
D05：classifies failure / determines blast radius / resolves recovery owner and route。

---

## 111. 后续 Decision 边界

D05 不完整冻结：

```text
Execution Result / Evidence / Trace Contract
Action Acceptance Criteria
Cross-action Orchestration
Runtime reporting / UX
F10 → F11 handoff
F10 stage closeout
```

---

## 112. Acceptance Meaning

用户已明确批准：

```text
F10-D05 HUMAN_APPROVED
```

因此正式成立：

```text
Failure Detection != Failure Ownership
Runtime-recoverable vs Governance-affecting vs Reality-unknown separation
Technology-neutral failure classification
Owner-based targeted recovery routing
Failure Blast Radius / minimum containment
Local failure does not automatically become global failure
Recovery remains inside Scope / Authorization / Gate
Automatic recovery first
Human escalation only for genuine unresolved judgment
F4 workflow control and F10 runtime enforcement remain separate
Failure evidence remains evidence, not semantic authority
```

但不表示批准 Exact Failure Enum / Exact Error Code / Exact Severity Model / Exact Recovery Algorithm / Exact Retry Count / Implementation / Real Project Write / RP2 / Authority Cutover / Canonical Replacement / Final Activation / Legacy Retirement。

---

## 113. Approval Status

```text
F10-D05 = HUMAN_APPROVED
```

普通“好的 / 下一步 / 继续 / 按建议继续”均不代表后续 Decision 的批准。

---

**END**

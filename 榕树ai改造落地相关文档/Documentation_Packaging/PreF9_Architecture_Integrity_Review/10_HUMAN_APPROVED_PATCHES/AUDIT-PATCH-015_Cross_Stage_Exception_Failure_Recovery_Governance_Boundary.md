# AUDIT-PATCH-015 — Cross-stage Exception Classification × Operational Failure Routing × Recovery / Governance Boundary

> Formal Audit Patch ID: `AUDIT-PATCH-015`  
> Source Finding: `B5-CHAIN-02`  
> Source Approval ID: `B5-PATCH-02`  
> Status: `HUMAN_APPROVED`  
> Audit Batch: `Audit Batch 5 — Cross-stage State / Exception Semantics`  
> Classification: `GAP / P1`  
> Primary Scope: `F1～F8 Cross-stage Exception / Failure Semantics`  
> Primary Owners: `Domain-owned Exception / Failure / Recovery Owners`  
> Cross-stage Coordination: `F4 / F7 / F8`  
> Reuses: `AUDIT-PATCH-005 / 007 / 008 / 009 / 013 / 014`  
> Implementation Authorization: `NO`

---

## 1. Problem

Banyan 已分别冻结 Retry / Fallback / Recovery / Rollback / Conflict / Drift / Divergence / Governed Exception / Reconciliation 等语义，但缺少跨阶段共同合同，明确异常条件如何分类、由谁处理、自动处理到哪一步，以及什么时候才进入 Governance / Human Decision。

如果缺少共同边界，未来可能产生：

```text
Operational Failure → Semantic Conflict
Runtime Exception → Governed Exception
Failure → Semantic Rollback
Fallback → Durable Rebinding
Recovery Success → Canonical Acceptance
Failure → Human by default
```

---

## 2. Core Exception Separation

正式：

```text
Operational Exception != Governed Exception
```

### Governed Exception

```text
Applicable Rule / Standard
→ Exception Eligibility
→ Required Exception Authority
→ Scope / Boundary
→ Approved Exception
```

继续由 AUDIT-PATCH-009 管理。

### Operational Exception

表示某次执行、调用、Provider、Adapter、Validation、Mutation 或 Runtime 过程中出现的异常条件。

正式：

```text
Bare Exception Label = SEMANTICALLY_AMBIGUOUS
```

架构合同中不得依赖未限定语义的裸 `Exception`。

---

## 3. Classification Before Handling

统一逻辑：

```text
Observed Abnormal Condition
→ Capture Evidence
→ Classify Semantic Kind
→ Resolve Scope / Owner
→ Resolve Handling Eligibility
→ Route
```

禁止：

```text
anything failed → rollback
anything failed → human
```

最低逻辑分类包括：

```text
Operational Error / Failure
Validation Failure
Dependency / Availability Failure
Drift / Divergence
Semantic Conflict
Governance Block
Governed Exception Request
Recovery / Rollback Need
```

Exact enum deferred。

---

## 4. Error / Failure Boundary

```text
Error
=
observed erroneous condition / fault signal
```

```text
Failure
=
an intended operation / obligation did not successfully complete
```

正式：

```text
Error != Failure
Error != State
Failure != Automatically State
```

并保持：

```text
Attempt Failure != Final Operation Failure

Invocation Failure
!= Node Failure
!= Workflow Failure
!= Goal Failure
```

Failure 必须绑定正确 Subject / Operation / Attempt / Scope。

---

## 5. Retry

```text
Retry
=
repeat the same logical operation
after a retry-eligible failure
under the same authorized semantic objective
```

正式：

```text
Retry != Fallback
Retry != Reauthorization
Retry Allowed != Retry Until Success
Unbounded Retry = FORBIDDEN
```

Retry 必须保留相同 Semantic Objective；改变 Scope / Requirement / Target Meaning / Authority 后不再属于 Retry。

Retry 创建新的 Attempt，历史 Attempt 不覆盖。

---

## 6. Fallback

Fallback 是：

> Primary Path 不可用时使用预先合法、语义兼容、受治理的替代执行路径。

正式：

```text
Fallback requires pre-governed eligibility

Fallback != Retry
Fallback != Override
Fallback != Governed Exception

Runtime Fallback != Durable Rebinding
Fallback Success != Durable Rebinding
```

Fallback 不得绕过 Governed HOLD / Hard Gate。

---

## 7. Technical Recovery

Technical Recovery 处理：

> 执行失败后，将技术环境恢复到安全、可继续治理的位置。

正式：

```text
Technical Recovery
!= Semantic Rollback
!= Compensating Change
!= Data Restoration

Technical Recovery Success
!= Original Operation Success

Recovery Success
!= Canonical Acceptance
```

---

## 8. Semantic Rollback

Semantic Rollback 表示：

> 已经正式接受的语义需要通过新的受治理动作恢复到先前语义。

继续：

```text
Semantic Rollback != Restore Old Bytes
Post-close Semantic Rollback → New Change Case
Semantic Rollback != Compensating Change
Semantic Rollback != Data Restoration
```

---

## 9. Drift / Divergence / Conflict

正式：

```text
Difference != Drift

Drift != Error
Drift != Conflict

Divergence != Conflict
Divergence != Operational Failure

Operational Failure != Semantic Conflict

Semantic Conflict != Retryable Failure
```

语义冲突不是通过重复执行即可解决的问题。

---

## 10. Governed Exception Boundary

完整复用 AUDIT-PATCH-009。

正式：

```text
Governed Exception != Error Handling
Approved Governed Exception != Runtime Permission
Operational Failure != Automatic Governed Exception Request

Exception Approval != Authority Expansion
Implementation Necessity != Exception Authority
Convenience != Exception Authority
Low Risk != Exception Authority
```

---

## 11. Governance Block

Governance Block 可来自：

```text
Authority missing
Gate blocked
Scope not authorized
Governed HOLD
```

正式：

```text
Governance Block != Operational Failure

Retry cannot bypass Governance Block

Fallback cannot bypass Governed HOLD

Technical Recovery != Gate Override
```

---

## 12. Detection / Evidence Boundary

正式：

```text
Detection != Mutation Authorization

Failure Evidence != Canonical Semantic Truth
```

Failure Evidence 可以触发 Retry / Fallback / Recovery / Reconciliation / Re-resolution / Change Candidate，但不能自行修改 Target Semantics。

Failure Evidence 至少逻辑上可描述：

```text
Subject
Operation
Attempt
Scope
Expected
Observed
Provider / Executor
Dependency
Mutation state
Impact
Owner
```

Exact schema deferred。

---

## 13. Partial Failure / Mutation

正式：

```text
Partial Failure != Global Project Failure
```

Partial Failure 必须结合 Atomicity Boundary / Dependency / Scope 判断。

若发生 Partial Physical Mutation，继续走 F7：

```text
Checkpoint
→ Technical Recovery
→ Post-mutation Validation
→ Canonical Acceptance Boundary
```

继续：

```text
Physical Mutation Completed != Apply Succeeded
Canonical Apply Accepted != Whole Change Closed
Executor Success != Canonical Acceptance
```

---

## 14. Timeout / Dependency / Provider Failure

Timeout 是 Operational Condition，不自动意味着 Provider Invalid / Binding Invalid / Feature Unsupported / Semantic Conflict。

具体 Retry / Fallback / Recovery / Block 顺序由 Domain Contract 决定。

正式：

```text
Provider Failure != Provider Binding Invalid

Repeated Failure
may produce Health / Compatibility / Drift Evidence
but
Repeated Failure != Automatic Durable Rebinding
```

Dependency unavailable 时，下游可由 Domain Resolver 得到 UNKNOWN / BLOCKED / STALE / UNAFFECTED，而不是统一 FAILED。

---

## 15. Validation Failure

正式：

```text
Validation Failure != Product Semantic Decision
```

Validation Failure 可触发 Repair / Drift Classification / Reconciliation，但不能自行修改 Product Meaning。

Regression Failure 也必须先 Classify Cause，不得自动 Rollback Everything。

---

## 16. Automatic Recovery Eligibility

只有满足：

```text
deterministic action
+ within existing authorization envelope
+ no semantic-intent change
+ no scope expansion
+ no gate bypass
+ required evidence/history preserved
```

才允许自动 Recovery。

继续：

```text
Automatic != Ungoverned
Governed != Manual Every Time
```

---

## 17. Human Escalation Boundary

正式：

```text
Operational Failure != Human Decision Required
Recovery Failure != Immediate Human Decision
Failure != Human Judgment
```

系统优先完成：

```text
classification
evidence capture
retry eligibility
fallback eligibility
technical recovery
owner routing
```

只有最终存在：

```text
Material Semantic Choice
Authority Conflict
Scope Expansion
High-risk Irreversible Action
Governed Exception Request
Multiple Legitimate Incompatible Recovery Strategies
```

且 deterministic rule 无法唯一解决时，才进入 Governance / Informed Decision。

继续复用 AUDIT-PATCH-005。

---

## 18. Failure Handling Order

以下只是逻辑检查维度，不是固定 Runtime Call Order：

```text
Observed Abnormal Condition
→ Classification
→ Evidence Capture
→ Scope / Owner Resolution
→ Retry Eligibility
→ Fallback Eligibility
→ Technical Recovery Eligibility
→ Reconciliation / Re-resolution Need
→ Governance / Exception Eligibility
→ Human only for genuine judgment gap
```

正式：

```text
Failure Handling Order = Domain Contract
Failure Handling Order != Governance Precedence
```

---

## 19. Owner / Authority Boundary

正式：

```text
Failure Owner != Semantic Authority Owner
Recovery Owner != Canonical Mutation Authority
Error Handler != Authority
Operational Exception Handler != Governed Exception Authority
Failure Handling != Scope Expansion Authorization
```

### F4
Workflow control semantics：Retry / Pause / Resume / Skip / Replace / Partial Blocking / Escalation。

### F5
Product Semantic Conflict / Product Gap / Decision Required / Governed Product Exception where applicable。

### F6
Validation Failure / Design Drift / Repair Failure / Repair Retry / Escalation。

### F7
Apply Failure / Partial Mutation / Technical Recovery / Semantic Rollback Governance / Compensating Change Boundary / Closeout。

### F8
Provider Binding / Fallback semantics / Version Compatibility / Project Drift / Reconciliation / Project Re-resolution。

### F9
未来提供 Failure Evidence Lookup / History / Health Evidence / Freshness / Impact / Provenance；Index / Telemetry != Failure Authority。

### F10
未来负责 Runtime Invocation / Runtime Permission / Provider Runtime / Adapter Execution / Runtime Retry Enforcement；Runtime Failure != Semantic Authority。

### F11
Future UX only；UI Action != Authority。

---

## 20. Scope / Locality

正式：

```text
Local Operational Failure != Global Project Failure
```

Failure containment 应按：

```text
Failure Scope
→ Dependency / Atomicity Analysis
→ Minimum Necessary Containment Scope
```

Failure 传播不得直接复制一个通用 FAILED：

```text
Upstream Failure Evidence
→ Dependency Evaluation
→ Downstream Domain resolves
   UNKNOWN / BLOCKED / STALE / UNAFFECTED
```

复用 AUDIT-PATCH-014。

---

## 21. Recovery / Reconciliation / Re-resolution

正式：

```text
Technical Recovery != Reconciliation
Reconciliation != Semantic Rollback
Technical Recovery != Re-resolution
```

它们可以连续发生，但不得合并成同一个概念。

---

## 22. Non-failure Outcomes

正式：

```text
Cancelled != Failed
Rejected != Failed
Superseded != Failed
Skipped != Failed
No Change Required != Failed
Partial Blocking != Whole Workflow Failure
```

Degraded Mode exact semantics deferred，但：

```text
Degraded != Unrestricted Success
```

---

## 23. Warning / Violation

正式：

```text
Warning != BLOCKED
Violation != Governed Exception
Violation != Operational Error
```

Hard Governance Violation 应拒绝 / 阻塞 Unauthorized Action，不得通过 Retry / Fallback 绕过。

---

## 24. Provenance

任何自动 Retry / Fallback / Recovery 必须可追踪：

```text
why eligible
which rule / policy allowed it
scope
attempt
result
downstream impact
```

正式：

```text
Silent Governed Exception = FORBIDDEN
Silent Durable Rebinding = FORBIDDEN
```

合法 pre-governed / compatible / scope-valid / runtime-authorized Fallback 可自动执行，但必须可追踪。

---

## 25. Exception Expiry / Revocation

Governed Exception 的 Authority / Scope / Reason / Validity / Revision / Supersession / Revocation 继续由 AUDIT-PATCH-009 管理。

正式：

```text
Governed Exception Expired / Revoked
!= Operational Error
```

正确：

```text
Exception no longer applicable
→ affected resolution / state may become STALE
→ Domain-owner re-resolution
```

复用 AUDIT-PATCH-008 / 014。

---

## 26. Common Core Boundary

Banyan Common Contract 只统一：

```text
classify
scope
owner
eligibility
route
provenance
```

具体 Retry / Recovery / Rollback 算法仍由 Domain Owner 管理。

禁止：

```text
GlobalExceptionManager
UniversalFailureEngine
GlobalErrorAuthority
UniversalRecoveryEngine
```

---

## 27. Legacy Compatibility

Legacy 资料中的：

```text
error
exception
failure
rollback
```

不能直接一对一提升为新的正式语义。

必须：

```text
Legacy Term
→ Context Inspection
→ Semantic Classification
→ Domain / Owner Resolution
→ deterministic mapping if unique
```

无法确定则：

```text
UNKNOWN / UNRESOLVED MAPPING
```

AI 不得猜测。

不要求一次性全量迁移。

---

## 28. Banyan-wide Invariants

```text
Operational Exception != Governed Exception
Bare Exception Label = Semantically Ambiguous
Abnormal Condition != Automatically Exception
Error != Failure
Error != State
Failure != Automatically State
Attempt Failure != Final Operation Failure
Invocation Failure != Node Failure != Workflow Failure != Goal Failure
Retry != Fallback
Retry != Reauthorization
Fallback != Override
Fallback != Governed Exception
Runtime Fallback != Durable Rebinding
Technical Recovery != Semantic Rollback != Compensating Change != Data Restoration
Recovery Success != Original Operation Success
Recovery Success != Canonical Acceptance
Drift != Error != Conflict
Divergence != Conflict != Operational Failure
Operational Failure != Semantic Conflict
Semantic Conflict != Retryable Failure
Governed Exception != Error Handling
Approved Exception != Runtime Permission
Implementation Necessity != Exception Authority
Governance Block != Operational Failure
Retry cannot bypass Governance Block
Fallback cannot bypass Governed HOLD
Detection != Mutation Authorization
Failure Evidence != Canonical Truth
Partial Failure != Global Project Failure
Mutation Completed != Apply Succeeded
Canonical Apply Accepted != Whole Change Closed
Executor Success != Canonical Acceptance
Validation Failure != Product Decision
Operational Failure != Human Decision Required
Failure Owner != Semantic Authority Owner
Recovery Owner != Canonical Mutation Authority
Error Handler != Authority
Operational Exception Handler != Governed Exception Authority
Failure Handling != Scope Expansion Authorization
Local Operational Failure != Global Project Failure
Failure Propagation != Failure State Copy
Technical Recovery != Reconciliation != Re-resolution
Cancelled != Failed
Rejected != Failed
Superseded != Failed
Skipped != Failed
No Change Required != Failed
Violation != Governed Exception
Warning != BLOCKED
Future Extensibility != Current Authorization
```

---

## 29. Forbidden Interpretations

禁止：

1. 裸 Exception 作为全局统一分类；
2. Runtime Exception 自动等于 Governed Exception；
3. Governed Exception 自动等于 Error；
4. 任意 Error 自动等于 Failure；
5. Attempt Failure 自动等于 Operation Failure；
6. Timeout 自动等于 Provider Binding Invalid；
7. Retry 自动获得新 Authorization；
8. Retry 无限直到成功；
9. Retry 自动换 Provider；
10. Fallback 自动永久 Rebinding；
11. Fallback 绕过 HOLD / Hard Gate；
12. Technical Recovery 自动等于 Semantic Rollback；
13. Restore Old Bytes 自动等于 Semantic Rollback；
14. Recovery Success 自动等于原任务成功；
15. Recovery Success 自动等于 Canonical Acceptance；
16. Failure 自动升级 Semantic Conflict；
17. Semantic Conflict 通过 Retry 解决；
18. Drift 自动等于 Error；
19. Divergence 自动等于 Conflict；
20. Validation Failure 自动修改 Product Semantics；
21. Runtime Failure 自动取得 Canonical Mutation Authority；
22. Error Handler 获得 Authority；
23. Operational Exception Handler 获得 Governed Exception Authority；
24. Failure 自动升级人工；
25. 局部 Failure 自动全项目失败；
26. Warning 自动 BLOCK；
27. Violation 自动成为 Approved Exception；
28. Exception Approval 扩大 Authority；
29. Implementation Necessity 自动获得 Exception；
30. AI 根据历史 Failure 自动修改长期 Policy；
31. 本 Patch 授权 Implementation / RP2 / Final Activation。

---

## 30. Deferred

不冻结：

```text
Exact Exception / Error / Failure enum
HTTP / Provider SDK error mapping
Go error interface
Retry count / backoff
Circuit breaker
Timeout values
Health / fallback scoring
Recovery algorithm
Checkpoint implementation
Transaction strategy
Saga / compensation engine
Fault / Incident taxonomy
Root-cause correlation implementation
Observability stack
Log / telemetry format
F9 failure index schema
F10 error API
F11 exception UX
Bulk legacy migration
Autonomous failure-policy learning
```

---

## 31. No-Loss Mapping

本 Patch 保留并补充：

- F4 — Retry / Pause / Resume / Skip / Partial Blocking / Escalation；
- F5 — Gap / Conflict / Decision Required / Hold / Cancellation；
- F6 — Difference != Drift / bounded Retry / Validation / Repair；
- F7 — Divergence != Conflict / Recovery / Rollback / Apply result separation；
- F8 — Retry != Fallback / Drift != Conflict != Error != Change Case；
- AUDIT-PATCH-009 — Governed Exception / Authority / Scope；
- AUDIT-PATCH-012 — Runtime Fallback != Durable Rebinding；
- AUDIT-PATCH-013 — deterministic non-success resolution / Human Escalation；
- AUDIT-PATCH-014 — Typed State Domain / Event != State / Exception != State。

---

## 32. Human Decision

用户明确：

```text
B5-PATCH-02 HUMAN_APPROVED
```

因此：

```text
AUDIT-PATCH-015 = HUMAN_APPROVED
B5-CHAIN-02 = ARCHITECTURALLY_RESOLVED
```

---

## 33. Authorization Boundary

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

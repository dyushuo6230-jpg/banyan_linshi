# F9-D10 — Failure / Fallback / Degraded Mode

**中文名称：失败、回退与降级模式**

## 0. 文档身份

- Stage：F9 — Index / Projection / Cache Architecture
- Decision：F9-D10
- 状态：`HUMAN_APPROVED`
- 精确批准语句：`F9-D10 HUMAN_APPROVED`
- 前置批准：F9-G01、F9-D01～F9-D09 均为 `HUMAN_APPROVED`
- Implementation：`NOT_AUTHORIZED`
- RP2：`NOT_AUTHORIZED`
- Authority Cutover：`NOT_AUTHORIZED`
- Canonical Replacement：`NOT_AUTHORIZED`
- Final Activation：`NOT_AUTHORIZED`
- Legacy Retirement：`NOT_AUTHORIZED`
- SQLite Physical Schema：`NOT_FROZEN`
- AI Autonomous Learning：`NOT_CURRENT_CAPABILITY`
- AI Autonomous Policy Mutation：`FORBIDDEN`

本决策冻结 F9 中 Failure、Fallback、Degraded、Blocked、Unknown、Retry、Circuit Breaking、Recovery、Failback、Persistent Degradation、Failure Evidence Lifecycle 与 Handoff 的架构语义；不冻结异常枚举、重试次数、超时时间、熔断阈值、Provider SDK、队列、健康检查、数据库结构等物理实现。

---

## 1. 核心定位

F9-D10 负责：当 F9 的 Retrieval、Index、Projection、Freshness、Dependency、Impact、Recovery、Provider、Protection 或 Rebuild 等能力发生失败、不可用、证据不足或部分能力损失时，确定当前 Purpose 下应该继续、重试、回退、降级、阻塞、恢复或转交其他 Owner。

D10 不是 Canonical Truth Owner、Authority Resolver、Recovery Engine、Rebuild Engine、Runtime Permission Owner 或 Human Decision Center。

```text
Failure Policy != Canonical Truth Resolution
Failure Policy != Recovery Implementation
Failure Policy != Rebuild Ownership
```

---

## 2. Failure 基本语义

Failure 必须是 Layer / Capability / Purpose-relative，不能只有全局 `ERROR`。重要 Failure 至少要表达：What failed、At which layer、For which capability、For which purpose、For which scope、What material obligation is affected、What remains usable。

```text
Component Failure != Whole F9 Failure
Provider Failure != Capability Failure
Capability Failure != Whole F9 Failure
Failure Reachability != Effective Failure Propagation
Branch Failure != Sibling Branch Failure
Shared Provider != Identical Failure Consequence
```

Failure Propagation 必须依据真实 Capability Dependency、Purpose、Materiality、Fallback Availability、Coverage 与 Protection。

---

## 3. Failure / Unavailable / Unknown / Blocked / Degraded / Fallback 分离

- Failure：某个操作或能力未按预期完成。
- Unavailable：Source / Provider / Capability 当前不可访问或不可执行。
- Unknown：当前证据不足以可靠确认某个事实。
- Blocked：当前 Purpose 的 Material Obligation 无法安全满足。
- Degraded：当前 Purpose 仍可继续，但 Capability / Coverage / Claim / Action 范围受限。
- Fallback：Primary Path 不可用时使用另一条允许的替代路径或证据。

```text
Failure != Blocked
Failure != Degraded
Failure != Fallback
Unavailable != Unknown
Unknown != Blocked
Blocked != Degraded
Same Failure != Same Consequence
Failure Cause != Failure Consequence
```

D10 禁止全局 Universal Fail-open / Fail-closed。失败后果必须 Purpose / Materiality / Risk / Protection / Authority Role / Freshness / Coverage / Action Consequence-aware。

---

## 4. Failure Classification

```text
Technical Error Type != Failure Governance Class
Source Unavailable != Source Invalid
Provider Failure != Subject Invalidity
Operational Failure State != Domain Semantic State
Evidence Unavailable != Negative Evidence
```

Failure Classification 应多维表达 Layer、Capability、Cause、Materiality、Scope、Temporal、Retryability、Fallback Availability、Protection Consequence 与 Freshness Consequence。具体 enum 不冻结。

---

## 5. Degraded Mode

Degraded Mode 表示部分能力或证据不可用，但当前 Purpose 仍能在明确限制下安全继续。

```text
Degraded Mode != Silent Capability Loss
Degraded != Incorrect
Degraded Availability != Universal Usability
```

Degraded Capability Envelope 至少逻辑表达：
- Available Capabilities
- Unavailable Capabilities
- Allowed Claims
- Claim Limitations
- Allowed Actions
- Disallowed Actions
- Coverage
- Freshness Limitation
- Protection Limitation
- Temporal Limitation

```text
Degraded Evidence must constrain claim strength
Last Known Claim must not be phrased as Current Confirmed Claim
Degraded Claim Eligibility != Degraded Action Eligibility
```

---

## 6. Fallback

Fallback 不产生 Authority Promotion。

```text
Fallback Source != Higher Authority Source
Fallback Use != Authority Promotion
Primary Circuit Open != Authority Transfer
Fallback Exists != Fallback Eligible
Fallback Candidate != Selected Fallback
Fallback Selection != Authority Election
Fallback Order != Authority Order
```

Fallback Eligibility 至少考虑 Identity、Purpose、Scope、Temporal、Profile / Applicability、Protection、Freshness、Coverage、Authority Role、Materiality、Action Consequence。

Fallback Candidate 先经过 Eligibility Filter，再进入 Operational Selection。Operational Preference 可在 Eligible Set 内考虑 Availability、Latency、Cost、Locality、Health，但不能创造 Eligibility。

```text
Latest Fallback != Best Applicable Fallback
Fallback Selection != Latency Optimization
Fallback Candidate Count != Truth Confidence
```

禁止 Majority Voting。

---

## 7. Equivalent / Degraded Fallback

Equivalent Fallback 必须有既有 Governed Equivalence；Degraded Fallback 可以继续服务，但语义、Coverage、Freshness 或 Capability 有明确降低。

```text
Fallback does not imply semantic equivalence
Equivalent Transport != Equivalent Semantic Fallback
Similarity != Fallback Equivalence
Last Known Validated != Current Confirmed
```

已有 Governed Provider Contract，且 Identity / Scope / Protection / Freshness Compatible 时，可自动切换 Secondary Provider。Historical-only、Protection 不兼容、Identity Mapping unresolved 或 Coverage 不完整的 Provider 不得自动升级为 Equivalent Fallback。

---

## 8. Protection / Consumer / Purpose / Temporal 边界

```text
Fallback must not bypass protection
Cached Visibility != Current Consumer Eligibility
Fallback Data Presence != Fallback Visibility Permission
Protection Denial != Availability Failure
Protection Denial != Provider Health Failure
Fallback Eligible For Consumer A != Fallback Eligible For Consumer B
Fallback Eligible For Purpose A != Fallback Eligible For Purpose B
Historical Accuracy != Current Applicability
```

Fallback Scope Narrowing 必须显式暴露 Coverage Reduction。

```text
Degraded Service Scope != Resolved Query Scope Mutation
Partial != Degraded
Operation Failed != Task Blocked
No Technical Failure != Task Can Continue
Unknown != Blocked Automatically
```

正式 Query Scope 变化返回 D03。

---

## 9. Retry / Fallback Chain

Failure 可逻辑区分 Transient、Structural / Persistent、Governance-blocked、Unknown；具体 enum 不冻结。

```text
Retryable != Retry Required
Retry must be cause-aware
Retry without new evidence/progress must be bounded
Fallback Chain must be bounded and progress-aware
```

Fallback Lineage 至少记录 Root Failure、Attempted Paths、Selection Basis、Selected Fallback、Equivalent / Degraded Status、Known Limitation、Final Outcome。

```text
Fallback Lineage != Authority Chain
```

---

## 10. Circuit Breaking

重复、近期且与 Provider / Capability Health 相关的 Failure 可触发 Circuit Breaking，以避免持续无价值地打 Primary Path。

```text
Circuit Open != Provider Permanently Invalid
Circuit State != Domain State
Primary Circuit Open != Authority Transfer
Circuit Open != Fallback Authorization
Failure Event != Circuit-breaker Evidence Automatically
```

Circuit State 必须 Provider / Capability / Scope / Operation Type / Temporal-aware。Protection / Governance Denial 不得伪装为 Provider Health Failure。

Circuit Open 后仍需重新做 Fallback Eligibility；没有 Eligible Fallback 时可以 BLOCKED。

---

## 11. Recovery / Failback

Recovery Probe 用于确认 Primary 是否具备重新进入正常服务的基础，具体实现不冻结。

```text
Circuit Timeout Expired != Primary Recovered
Single Recovery Success != Full Primary Recovery
No universal recovery confidence score
Primary Recovery != Immediate Fallback Retirement
Primary Availability Restored != Primary Currently Applicable
Operational Failback != Authority Cutover
Primary Path != Authority Winner Automatically
Primary/Fallback Difference != Governance Conflict Automatically
```

Failback 必须重新检查 Identity、Scope、Temporal、Effective Basis、Protection、Freshness，并防止 Failover / Failback Flapping。

---

## 12. Failure Recovery Lineage

Failure、Retry、Circuit、Fallback、Degraded Envelope、Recovery Probe、Failback Basis 与 Final Outcome 形成 Failure Recovery Lineage。

```text
Failure Recovery Lineage != Canonical Domain History
```

---

## 13. Persistent Degradation

Persistent Degradation 表示降级 / Fallback 状态已持续到需要成为治理可见问题，不能继续只按普通短暂故障处理。

```text
Persistent Degradation is policy- and materiality-aware
Persistent Degradation != Human Escalation Automatically
Persistent Degradation != Approved Deferred Obligation
Failure Persistence != Approved Deferral
D10 Deferred Candidate != Approved Deferred Obligation
Temporary Recovery != Deferred Obligation Resolution
Transient Resolved Failure != Deferred Obligation Candidate Automatically
```

Long-lived Unsupported Capability、Architecture Gap、Material Degradation、Permanent Weaker Fallback、Repeated Non-recovery、Protection Limitation 等可形成 D11 Deferred Obligation Candidate，但是否正式延期由 D11 / Governance Owner 决定。

---

## 14. Failure Evidence Lifecycle

```text
Historical Failure Evidence != Current Failure State
Failure Evidence Identity != Provider Identity
Failure Evidence Identity != Subject Identity
Failure Evidence Revision != Domain Revision
Failure Evidence Reuse requires purpose and basis compatibility
Previously Failed != Currently Failed
Previously Recovered != Currently Healthy
Failure Timeline != Canonical Domain History
Current Failure State != Canonical Domain State
Latest Failure/Recovery Event != Current Failure State Automatically
```

Current Failure State 是 Derived Operational State，必须综合 Failure Scope、Capability Coverage、Recovery Coverage、Temporal Relevance、Materiality、Fallback、Circuit 与 Protection。

```text
Branch Recovery != Whole Capability Recovery
Capability Recovery != Whole F9 Recovery
Operational Recovery != Root Cause Resolution
Current Operational Recovery != Historical Reliability Concern Closed
Failure Lifecycle != Domain Lifecycle
Recovered Failure != Failure Evidence Deletion
Failure Evidence Retention != AI Autonomous Learning
Observed Failure Pattern != Autonomous Policy Mutation
```

---

## 15. Cross-session Recovery

D10 复用 D05 Continuation State。需要恢复的最小状态可包括 Primary Path、Current Failure State、Circuit State、Current Fallback、Fallback Eligibility Basis、Degraded Capability Envelope、Pending Retry / Probe、Persistent Degradation、Blocked Material Obligation、Failure Recovery Lineage Ref。

```text
Recovered Failure State != Current Reconfirmed Failure State
Session Change != Failure Reset
Session Change != Circuit Reset
Session Change != Recovery Trigger
Recovered Fallback Pointer without eligibility basis is insufficient
```

换窗口不是系统恢复正常，也不是故障重置。

---

## 16. Failure Handling Completion

Failure Handling Completion 表示当前 Failure Branch 已完成可靠分类，Retry、Fallback、Degraded、Blocked、Unknown、Owner Route 与 Material Limitation 已明确。

```text
Failure Handling Complete != Primary Recovered
Failure Handling Complete != Normal Operation
Failure Handling Complete != Runtime Authorized
```

Handling Complete、Failure Resolved、Root Cause Resolved 必须分离。

Failure Handling Completion 是 Purpose-relative。

`DEGRADED_CONTINUING`、`BLOCKED`、`UNKNOWN`、`FALLBACK_ACTIVE`、`RECOVERING` 均可成为合法 Handling Outcome，只要 Cause、限制、Material Unknown、Owner 与 Next Action 明确。

```text
Degraded Continuation != Mutation Authorization
Unknown Outcome != Silent Failure
```

---

## 17. Owner Boundary

```text
F9-D03 → Scope / Profile / Query Re-resolution
F9-D04 → Context Selection / Context Sufficiency
F9-D05 → Missing Source / Context / Continuation Recovery
F9-D06 → Freshness Evaluation / Freshness Sufficiency
F9-D07 → Change Detection / Invalidation Trigger
F9-D08 → Dependency / Potential Impact Discovery
F9-D09 → Derived Artifact / Rebuild / Publication / Retention
F9-D10 → Failure Policy / Fallback Eligibility / Degraded Mode / Failure Propagation / Circuit / Recovery Policy / Persistent Degradation / Failure Handling Completion
F9-D11 → Deferred Obligation Discovery / formal obligation routing
F9-D12 → F9 → F10 Stage Handoff
```

```text
Fallback Scope Reduction != Query Re-resolution
Degraded Service Available != Context Sufficient
Failure Recovery Policy != Recovery Semantics Ownership
Fallback Policy Eligibility != Freshness Satisfaction
Fallback Policy != Derived Artifact Maintenance
D10 != Rebuild Owner
```

---

## 18. D10 → D11 / D12

D10 → D11 可提供 Persistent Degradation、Unresolved Material Failure、Long-lived Fallback、Unsupported Capability、Architecture Gap、Repeated Non-recovery、Persistent Protection Limitation、Manual Workaround Dependence，均只作为 Deferred Obligation Candidate。

D10 → D12 至少携带：
- Current Failure State
- Degraded State
- Active Fallback
- Fallback Eligibility Basis
- Capability / Claim / Action Limitation
- Blocked Material Obligation
- Circuit / Recovery State
- Persistent Degradation
- Unresolved Owner Route
- Failure Recovery Lineage
- Provenance

```text
Degraded Handoff must preserve semantic envelope
D10 Handoff != F10 Activation
```

---

## 19. 自动化与 Human Boundary

```text
Deterministic Degradation should be automatic
Failure != Human Escalation Automatically
Degraded != Human Escalation Automatically
Persistent Degradation != Human Escalation Automatically
```

可由现有规则可靠决定的 Failure Routing、Retry、Fallback、Degradation、Circuit、Probe 和 Owner Route 应自动完成。

Human / Applicable Governance Owner 仅处理真正的 Governance Ambiguity，例如多条合法 Fallback 有实质不同治理后果、Authority Equivalence 无法确定、Protection 规则冲突、Material Governance Choice 无 Deterministic Winner。AI uncertainty 本身不足以要求 Human。

---

## 20. Failure Handling Semantic Envelope

D10 最终输出至少逻辑包含：

```text
Root Failure
Affected Capability
Affected Purpose
Failure Cause
Failure Propagation Boundary
Retry Outcome
Circuit State
Fallback Candidates
Selected Fallback
Fallback Eligibility Basis
Degraded Capability Envelope
Partial / Blocked / Unknown
Protection Limitation
Freshness Limitation
Persistent Degradation
Owner Route
Next Action
Failure Recovery Lineage
Provenance
```

具体 Schema 不冻结。

---

## 21. 架构主链

```text
Failure Evidence
↓
Failure Classification
↓
Failure Propagation Boundary
↓
Materiality / Purpose Check
↓
Retryability
↓
Retry / Circuit Decision
↓
Fallback Candidate Discovery
↓
Fallback Eligibility
↓
Equivalent Fallback
or
Degraded Fallback
or
BLOCKED
or
UNKNOWN
↓
Degraded Capability Envelope
↓
Recovery Probe
↓
Failback Eligibility
↓
Current Failure State
↓
Failure Handling Completion
↓
Persistent Degradation?
    ├─ No → Normal / Degraded Continuing
    └─ Yes → D11 Candidate
↓
D12 Handoff
```

---

## 22. 核心不变量

```text
Failure != Domain Invalidity
Component Failure != Whole F9 Failure
Provider Failure != Capability Failure
Capability Failure != Whole F9 Failure
Failure Reachability != Effective Failure Propagation
Branch Failure != Sibling Branch Failure
Shared Provider != Identical Failure Consequence

Failure != Blocked != Degraded != Fallback
Unavailable != Unknown != Blocked != Degraded
Failure Cause != Failure Consequence
Same Failure != Same Consequence

Technical Error Type != Failure Governance Class
Source Unavailable != Source Invalid
Provider Failure != Subject Invalidity
Evidence Unavailable != Negative Evidence

Degraded Mode != Silent Capability Loss
Degraded != Incorrect
Degraded Availability != Universal Usability
Degraded Claim Eligibility != Degraded Action Eligibility

Fallback Source != Higher Authority Source
Fallback Use != Authority Promotion
Fallback Exists != Fallback Eligible
Fallback Candidate != Selected Fallback
Fallback Selection != Authority Election
Fallback Order != Authority Order
Latest Fallback != Best Applicable Fallback
Fallback Candidate Count != Truth Confidence
Fallback does not imply semantic equivalence
Equivalent Transport != Equivalent Semantic Fallback
Similarity != Fallback Equivalence
Last Known Validated != Current Confirmed

Protection Denial != Availability Failure
Fallback Data Presence != Fallback Visibility Permission
Fallback Eligible For Consumer A != Fallback Eligible For Consumer B
Fallback Eligible For Purpose A != Fallback Eligible For Purpose B
Historical Accuracy != Current Applicability

Degraded Service Scope != Resolved Query Scope Mutation
Partial != Degraded
Operation Failed != Task Blocked
No Technical Failure != Task Can Continue
Unknown != Blocked Automatically

Retryable != Retry Required

Circuit Open != Provider Permanently Invalid
Circuit State != Domain State
Primary Circuit Open != Authority Transfer
Circuit Open != Fallback Authorization
Circuit Timeout Expired != Primary Recovered
Single Recovery Success != Full Primary Recovery
Primary Recovery != Immediate Fallback Retirement
Primary Availability Restored != Primary Currently Applicable
Operational Failback != Authority Cutover
Primary Path != Authority Winner Automatically
Primary/Fallback Difference != Governance Conflict Automatically

Failure Recovery Lineage != Canonical Domain History
Persistent Degradation != Human Escalation Automatically
Persistent Degradation != Approved Deferred Obligation
Failure Persistence != Approved Deferral
Temporary Recovery != Deferred Obligation Resolution

Historical Failure Evidence != Current Failure State
Previously Failed != Currently Failed
Previously Recovered != Currently Healthy
Failure Timeline != Canonical Domain History
Current Failure State != Canonical Domain State
Latest Failure/Recovery Event != Current Failure State Automatically
Branch Recovery != Whole Capability Recovery
Capability Recovery != Whole F9 Recovery
Operational Recovery != Root Cause Resolution
Current Operational Recovery != Historical Reliability Concern Closed
Failure Lifecycle != Domain Lifecycle
Recovered Failure != Failure Evidence Deletion
Failure Evidence Retention != AI Autonomous Learning
Observed Failure Pattern != Autonomous Policy Mutation

Recovered Failure State != Current Reconfirmed Failure State
Session Change != Failure Reset != Circuit Reset != Recovery Trigger

Failure Handling Complete != Primary Recovered
Failure Handling Complete != Normal Operation
Failure Handling Complete != Runtime Authorized
Degraded Continuation != Mutation Authorization

Fallback Policy Eligibility != Freshness Satisfaction
Degraded Service Available != Context Sufficient
Fallback Scope Reduction != Query Re-resolution
Failure Recovery Policy != Recovery Semantics Ownership
Fallback Policy != Derived Artifact Maintenance

D10 Deferred Candidate != Approved Deferred Obligation
D10 Handoff != F10 Activation
```

---

## 23. HUMAN_APPROVED Effect

本文件已获得：

```text
F9-D10 HUMAN_APPROVED
```

因此以下边界正式进入 `ARCHITECTURALLY_FROZEN`：

- Failure Semantic Boundary
- Failure Classification Boundary
- Failure Propagation Boundary
- Unavailable / Unknown / Blocked / Degraded Boundary
- Fallback Eligibility Boundary
- Fallback Selection Boundary
- Equivalent / Degraded Fallback Boundary
- Degraded Capability Envelope Boundary
- Claim / Action Limitation Boundary
- Retry Boundary
- Fallback Lineage Boundary
- Circuit Breaking Boundary
- Recovery Probe / Failback Boundary
- Persistent Degradation Boundary
- Failure Evidence Lifecycle Boundary
- Cross-session Failure Recovery Boundary
- Failure Handling Completion Boundary
- D10 → D11 / D12 Handoff Boundary

继续保持：

```text
F9 Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
AI Autonomous Learning = NOT_CURRENT_CAPABILITY
AI Autonomous Policy Mutation = FORBIDDEN
```

`F9-D10 HUMAN_APPROVED` 只表示 Failure / Fallback / Degraded Mode 的架构语义冻结，不代表 Provider、Circuit Breaker、Retry Engine、Fallback Engine、Health Check、Scheduler、Runtime、Agent 或任何具体实现获得施工授权。

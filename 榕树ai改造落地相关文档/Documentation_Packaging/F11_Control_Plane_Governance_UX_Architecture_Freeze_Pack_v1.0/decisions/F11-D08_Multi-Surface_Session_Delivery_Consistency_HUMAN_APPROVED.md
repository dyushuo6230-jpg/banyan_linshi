# F11-D08 — Multi-Surface / Session / Delivery Consistency
## 多端界面 / 会话 / 投递一致性

**Stage:** F11 — Control Plane / Governance UX Architecture  
**Decision ID:** F11-D08  
**Status:** HUMAN_APPROVED / FROZEN

**Upstream**
- F11-G01 = HUMAN_APPROVED / FROZEN
- F11-D01 = HUMAN_APPROVED / FROZEN
- F11-D02 = HUMAN_APPROVED / FROZEN
- F11-D03 = HUMAN_APPROVED / FROZEN
- F11-D04 = HUMAN_APPROVED / FROZEN
- F11-D05 = HUMAN_APPROVED / FROZEN
- F11-D06 = HUMAN_APPROVED / FROZEN
- F11-D07 = HUMAN_APPROVED / FROZEN

**Implementation Authorization:** NO  
**RP2 Authorization:** NO  
**Authority Cutover Authorization:** NO  
**Canonical Replacement Authorization:** NO  
**Final Activation Authorization:** NO  
**Legacy Retirement Authorization:** NO

---

## 1. 决策目标

F11-D08 冻结 Surface、Session、Logical Interaction、Delivery、Delivery Attempt、Draft、Pending Submission、Cross-surface Continuity、Reconnect、Offline Recovery 之间的语义与责任边界。

核心原则：

```text
Current Truth first
Semantic consistency over UI identity
No blind replay
No stale snapshot authority
No transport-driven business semantics
```

不同 Surface 可以有不同表现形式、信息密度和交互能力，但不得各自产生 Runtime Truth、Decision Truth、Attention Truth、Control Truth 或 Permission Truth。

---

## 2. 身份与对象边界

正式冻结：

```text
Surface != Authority
Surface State != Domain Truth
Multiple Surface Views != Multiple Domain Subjects

Session != Task
Session != Action
Session != Attempt
Session != Decision
Session != Attention Requirement

ControlSession != Runtime Execution Lifetime
Session End != Runtime Stop
Session Disconnect != Runtime Pause
Session Loss != Decision Requirement Loss
Session Loss != Attention Requirement Loss
Session Context != Current Domain Context
```

Identity 必须保持分离：

```text
User Identity != Session Identity
Session Identity != Surface Identity
Session Identity != Interaction Identity
Interaction Identity != Delivery Identity
Delivery Identity != Domain Subject Identity
```

Lifecycle 必须保持分离：

```text
Interaction Lifetime != Session Lifetime
Session End != Interaction End
Domain Subject Lifetime != Session Lifetime
Surface Close != Session Close != Domain Close

Closed != Expired
Expired != Superseded
Superseded != No Longer Applicable
No Longer Applicable != Deleted

Session Expiry != Domain Expiry
Session Expiry != Submitted Interaction Cancellation
Interaction Applicability != Session Validity
Later Object != Superseding Object by default
```

每个逻辑对象拥有自己的 Lifecycle Semantics，不建立 Global Lifecycle。

---

## 3. Reconnect / Resume

Reconnect 采用：

```text
Recover Current Truth first,
then restore Presentation Context
```

正式冻结：

```text
Reconnect != Mandatory Full Replay
Current State Recovery != Complete Historical Replay
Session Resume != Blind UI Restoration
Presentation Intent may be restored,
Current Semantic State must be re-resolved
Session Resume != Runtime Resume
```

重连优先恢复 Minimum-sufficient Current Projection；历史 Trace 仅按 Purpose / Demand 补充。

---

## 4. Logical Interaction 与 Delivery

正式冻结：

```text
UI Event != Logical Interaction
Delivery Attempt != Logical Interaction
Transport Duplication must not redefine Logical Interaction Identity
Duplicate Delivery != New Intent
```

同时必须保护真实的新用户意图：

```text
Deduplication must preserve Explicit New User Intent
Temporal Proximity != Duplicate Intent Proof
Time Distance != New Intent Proof
Same User + Same Subject != Same Interaction
```

同一个 Logical Interaction 可以拥有多个 Delivery Attempt；多个 Delivery Attempt 不自动产生多个业务交互。

---

## 5. 跨 Surface 并发

正式冻结：

```text
Cross-surface Concurrent Intents
!= Multiple Authorized Consequences

Multi-surface Coordination
!= Runtime Concurrency Authority
```

D08 只保证交互身份与连续性正确；最终 Runtime Consequence 仍由 D03 / F10 的 Point-of-use Revalidation 决定。

---

## 6. Optimistic / Shared Interaction State

正式冻结：

```text
Optimistic Surface State != Shared Domain Truth
Shared Interaction State != Shared Runtime State
```

例如 `Pause requested` 不等于 `Runtime PAUSED`。

Surface 可以共享“请求已提交”，但不能因此直接共享“Runtime 已成功改变”。

---

## 7. Draft / Decision Continuity

正式冻结：

```text
Surface-local Draft != Shared Governed Decision
Cross-surface Draft != Governed Decision Record

Draft Sync != Submission
Draft Sync Success != Decision Submission
Draft Persistence != Human Decision
```

Shared Draft 必须保留其 Applicability Basis，并在恢复时重新对照 Current Decision Basis。

```text
Draft Applicability
must be re-evaluated
against current Decision Basis

Draft Recovery
must follow Current Decision Applicability

Late Draft Delivery != Current Draft Authority
Last Draft Delivery != Latest Meaningful Draft
Draft Conflict != Governance Decision Conflict
Draft Resolution != Decision Resolution
```

Cross-surface Concurrent Decision Inputs 不采用 Last-delivery-wins。

```text
Cross-surface Concurrent Decision Inputs
!= Last-delivery-wins Decision Resolution

Duplicate Decision Input Delivery
!= Multiple Human Decisions
```

---

## 8. Reconnect 恢复责任顺序

逻辑责任顺序冻结为：

```text
1. Restore identity / session eligibility
2. Recover minimum-sufficient Current Projection
3. Resolve current Subject / Decision / Attention / Control applicability
4. Correlate pending / unknown previous submissions
5. Reconcile Draft / Pending Interaction / Offline captured intent
6. Restore valid Presentation Context
7. Load additional History / Trace only when needed
```

这是责任模型，不是固定 API Workflow。

---

## 9. Unknown Submission Outcome

正式冻结：

```text
Current Subject State != Previous Submission Outcome

Recovery should prefer
Logical Interaction Correlation
over State Inference

Correlation != Authorization

Unresolved Submission Outcome
must remain explicitly representable

UNKNOWN != Human Decision Required

Unknown Prior Outcome
!= Current Retry Availability
```

不得把 Unknown 自动当成失败，也不得据此盲目 Retry。

---

## 10. Protected Interaction Replay

正式冻结：

```text
Transport Timeout
!= Permission to Replay Protected Interaction

Protected Interaction
with Unknown Outcome
must not be blindly replayed

Session Crash Recovery
!= Automatic Protected Resubmission

Presentation Reload
!= Interaction Replay

Navigation History
!= Current Interaction Availability
```

Protected Interaction 包括但不限于 RuntimeControlIntent、GovernanceDecisionInput、Apply / Canonical Mutation Request、Authority-sensitive Operation、Irreversible Protected Action。Exact 分类暂缓。

---

## 11. Offline 边界

正式冻结：

```text
Offline Projection
!= Current Confirmed Projection

Offline Intent Capture
!= Deferred Runtime Permission

Offline Captured Intent
!= Automatically Executable Intent

Offline Pending Interaction
must be applicability-checked
before submission

Queued Offline Interaction
!= Pre-authorized Future Action

Offline Interaction Queue
!= Runtime Command Queue

Offline Interaction History
!= Required Future Execution Sequence

Offline Intent Reconciliation
must be rule-backed,
not free-form AI interpretation

Intent Withdrawal
!= Runtime Cancellation
```

离线期间可保存 Draft 或 Pending User Intent，但上线后必须依据 Current Context 重解析，不得 FIFO 机械执行。

---

## 12. Submission / Pending / Failure 分离

正式冻结：

```text
Local Send Failure
!= Unknown Remote Submission Outcome

Pending Submission
!= Pending Domain State

Submission Outcome
!= Domain Outcome

Pending
must remain lifecycle-qualified
```

例如：

```text
Submission Pending
Delivery Pending
Runtime Waiting
Decision Required
```

不得压成一个 Global `PENDING`。

Failure 同样必须限定生命周期：

```text
Delivery Failed
Submission Failed
Attempt Failed
Validation Failed
```

---

## 13. Delayed / Out-of-order Delivery

正式冻结：

```text
Delayed Delivery
must be evaluated
against current applicability basis
before presentation mutation

Delivery Order != Semantic Order

Last Received Message
!= Current Effective Projection

Out-of-order Delivery
must not silently overwrite
newer applicable state
```

表面状态“倒退”必须基于 Subject / Attempt / Revision 解释：

```text
Apparent State Regression
must be interpreted
against Subject / Attempt / Revision Basis
```

Consistency Comparison 必须 Semantically Typed，不允许用一个模糊全局 `version`。

---

## 14. Revision 与 Current Recovery

继续继承：

```text
Projection Revision
!= Subject Revision
!= Canonical Revision
!= Attempt Revision
```

正式冻结：

```text
Consistency Basis
must preserve revision meaning

Missed Delivery
!= Mandatory Replay Before Current Recovery

Current Consistency Recovery
!= Historical Completeness Recovery

Trace Recovery
should be Demand- or Purpose-driven

Reconnect Recovery
should prefer Minimum-sufficient Current Context

Minimum Sufficient
must preserve Material Governing Qualifiers
```

包括 Stale、Historical、Superseded、Restricted、No Longer Applicable、Unknown Outcome 等关键限定。

---

## 15. Query Replay 与 Mutation Replay

正式冻结：

```text
Query Replay Semantics
!= Protected Mutation Replay Semantics

Transport Retry Policy
must respect Interaction Semantics

Transport Retry != Runtime Retry

Transport Cancellation != Runtime Cancellation

Idempotent Delivery
!= Same Semantic Interaction
```

不得设计“所有网络失败请求统一自动 Retry N 次”的通用策略。

---

## 16. Cross-surface Consistency

正式冻结：

```text
Different Observation Time
!= Semantic Inconsistency by default

Stale Surface Projection
must not masquerade
as Current Confirmed State

Cross-surface Consistency
does not require zero-latency synchronization

Cross-surface Consistency
!= Identical UI State

Cross-surface Consistency
means Semantic Consistency,
not UI-state Consistency

Semantic Synchronization
should be preferred over
Presentation Synchronization
```

Surface 可以短暂不同，但必须向 Current Authoritative Projection 收敛。

---

## 17. 四层共享模型

D08 正式冻结四层模型：

```text
Layer 1
Authoritative Domain Projection

Layer 2
Shared Logical Interaction State

Layer 3
Session Continuity State

Layer 4
Surface-local Presentation State
```

### Layer 1
包括 Runtime Projection、Decision Requirement、Decision Current Context、Result / Acceptance、Attention Underlying Requirement、Current Applicability。

```text
Shared Visibility != Shared Ownership
```

### Layer 2
包括 Intent Submitted、Submission Outcome、Logical Correlation、Decision Input Submitted、Attention Acknowledged、Material Pending Interaction、Unknown Submission Outcome。

```text
Shared Logical Interaction State
!= Authoritative Domain State
```

### Layer 3
包括 Draft、Currently Viewed Subject、Navigation Intent、Recoverable Work Context。

```text
Session Continuity State
!= Governance Truth
```

### Layer 4
包括 Tabs、Panels、Scroll、Animation、Local Loading 等。

```text
Surface-local Presentation State
need not be globally synchronized
```

Lower Layer 不得提升为 Higher Layer Truth：

```text
button enabled != Runtime Permission
Draft choice = B != Decision = B
Intent submitted != Runtime consequence succeeded
```

Higher-level Semantic Change 可以使下层 Continuity State 失效，但 No Longer Applicable != Deleted。

---

## 18. Read / Acknowledge / Snooze

正式冻结：

```text
Logical Read State
!= Delivery Read Receipt

Attention Read
does not require
every Delivery to be read

Logical Acknowledgement
should be shared
across eligible Surfaces
unless explicitly governed otherwise

Shared Acknowledge
!= Shared Domain Completion

Shared Attention Handling
!= Shared Detail Visibility

Logical Snooze
!= Surface-local Dismiss

Logical Snooze
may coordinate Delivery
but must not suppress
contextual truth presentation
```

Material Pending Interaction 应跨相关 Surface 可发现；Surface Loading State 不等于 Shared Pending Interaction。

---

## 19. 跨端收敛机制边界

正式冻结：

```text
Cross-surface Consistency
should converge through
shared authoritative semantics,
not peer UI-state replication

Surface-local Cache
must not become
cross-surface truth source

Interaction Correlation may be shared
Point-of-use Permission must be re-resolved

Recent Read != Current Write Permission

Observed Permission Hint
!= Transferable Runtime Permission

Same User
!= Same Runtime Permission Snapshot
```

---

## 20. Authentication / Session 与 Permission

正式冻结：

```text
Authenticated Session
!= Runtime Permission

Session Authentication
!= Domain Authorization
!= Runtime Permission

Session Handoff
!= Authority Handoff

Surface Handoff
!= Authority Transfer
```

---

## 21. Session Store 与 Domain Correctness

正式冻结：

```text
Session Continuity Failure
!= Domain Correctness Failure

Session Store
must not become
Domain Truth dependency

Cross-surface Notification Sync Failure
!= Attention Requirement Loss
```

---

## 22. D08 与 D03 边界

D03 拥有 RuntimeControlIntent、Intent Semantics、Point-of-use Revalidation、Resolution、Runtime Consequence Handoff。

D08 负责 Interaction Continuity、Session / Surface / Delivery Recovery、Logical Identity Preservation。

正式：

```text
D08 preserves interaction continuity
D03 owns control semantics

Interaction Recovery
!= Runtime Permission Recovery
```

---

## 23. D08 与 D04 边界

D04 拥有 Human Decision Requirement、Decision Context、Alternative、GovernanceDecisionInput、Decision Validation。

D08 负责 Draft Continuity、Submission Continuity、Cross-surface Recovery、Unknown Outcome Recovery。

正式：

```text
D08 Decision Continuity
!= Decision Authority
```

---

## 24. D08 与 D07 边界

D07 决定 Attention 是否存在、何时、何地、通知谁。

D08 决定同一个 Logical Attention 如何跨 Surfaces / Sessions / Deliveries 保持连续一致。

正式：

```text
Attention Policy
!= Delivery Consistency Mechanism

Delivery Recovery
must remain subordinate
to Attention Policy
```

---

## 25. D08 与 D09 边界

D09 拥有 Visibility、Sensitive Data、Redaction、Presentation Safety。

正式：

```text
Cross-surface Synchronization
must not bypass Visibility Policy

Shared Semantic State
!= Shared Raw Sensitive Payload

Draft Synchronization
must remain Visibility- and Policy-aware
```

---

## 26. D08 与 F10 边界

F10 继续拥有 Runtime State、Runtime Permission、Execution Lifecycle、Attempt、Runtime Result、Runtime Failure / Recovery。

正式：

```text
Session Resume != Runtime Resume
Transport Retry != Runtime Retry
Transport Cancellation != Runtime Cancellation
```

D08 不得从 UI Event、Delivery Success、Session Resume 推导 Runtime Truth。

---

## 27. 禁止 Global UI / Session Truth Store

正式冻结：

```text
Global UI Synchronization
must not collapse
Presentation State
and Domain Truth
into one model

F11-D08 must not create
a global UI truth store
that becomes authoritative
for Runtime / Decision /
Attention / Result / Permission
```

Session Store 也不得成为 Domain Truth Store。

---

## 28. Explicitly Forbidden Designs

禁止将以下设计提升为正式架构：

```text
Surface = Authority
Web state = Runtime Truth
Mobile state = Decision Truth
Session = Task lifecycle
Close browser = Pause runtime
Disconnect = Cancel operation
Session expired = Decision expired
Session lost = Attention lost
Restore session = restore old Permission
Reconnect = replay all previous actions
Network timeout = retry protected action
Unknown submission = failed submission
Unknown submission = safe to resubmit
Offline click = future authorized runtime action
Offline queue = Runtime command queue
Page reload = repeat protected interaction
App restart = repeat Decision Input
Browser back = current control availability
Latest network message = Current Truth
Last write wins = cross-surface consistency
Last draft delivery = latest valid draft
Same button twice = duplicate by definition
Same button twice = new intent by definition
Same user = same interaction
Same user = transferable permission
UI optimistic state = runtime success
Draft choice = Human Decision
Draft synced = Decision submitted
Decision submitted = Decision accepted
Delivery succeeded = Runtime succeeded
Acknowledge synced = Domain completed
Read synced = Decision handled
Email link = permanent control permission
Push button = permanent runtime availability
Old notification = Current Decision Context
Peer UI state replication = cross-surface truth
Surface cache = shared truth source
Session store = Domain truth store
Global UI State = Runtime + Decision + Attention + Permission Truth
Transport retry = Runtime retry
Transport cancellation = Runtime cancellation
Cross-surface sync = visibility bypass
```

---

## 29. Deferred

F11-D08 暂缓：

```text
Exact Session Enum
Exact Session TTL
Exact Session State Machine
Exact Surface Enum
Exact Interaction ID Format
Exact Delivery ID Format
Exact Delivery Attempt Model
Exact Draft Revision Model
Exact Draft Merge Algorithm
Exact Offline Queue Implementation
Exact Reconnect Algorithm
Exact Unknown Outcome Algorithm
Exact Correlation Storage
Exact Event Sequence Mechanism
Exact Ordering Mechanism
Exact Idempotency Implementation
Exact Transport Retry Count
Exact Optimistic UI Mechanism
Exact Cross-device Sync Protocol
Exact Session Store
Exact Draft Store
Exact Read Sync Protocol
Exact Acknowledge Sync Protocol
Exact Snooze Sync Protocol
Exact WebSocket / SSE / Polling Selection
Exact Visibility Sync Mechanism
Database Tables
SQLite Physical Schema
Redis Structure
REST API
WebSocket
SSE
Go Struct
TypeScript Interface
UI Layout
```

---

## 30. Final Freeze Effect

`F11-D08 HUMAN_APPROVED` 正式冻结：

- Surface / Session / Interaction / Delivery / Domain Subject separation
- Identity separation
- Lifecycle separation
- Session / Runtime lifetime boundary
- Reconnect Current-first recovery
- No blind replay
- Unknown Submission Outcome semantics
- Offline interaction boundary
- Draft continuity semantics
- Delayed / Duplicate / Out-of-order Delivery semantics
- Semantic consistency instead of identical UI consistency
- Minimum-sufficient Current Projection recovery
- Trace-on-demand recovery
- Logical Interaction identity across Surfaces
- Four-layer shared-state model
- Cross-surface Read / Acknowledge / Snooze boundaries
- Session Resume / Runtime Resume separation
- Transport Retry / Runtime Retry separation
- Transport Cancel / Runtime Cancel separation
- D03 Control boundary
- D04 Decision boundary
- D07 Attention boundary
- D09 Visibility / Sensitive Data boundary
- F10 Runtime Authority boundary
- No Global UI Truth Store
- No Session Truth Store

仍然不代表：

```text
Exact session implementation frozen
Exact sync engine frozen
Exact offline engine frozen
Exact WebSocket architecture frozen
Exact conflict merge algorithm frozen
Exact idempotency implementation frozen
Exact database model frozen
Implementation authorized
RP2 authorized
Authority Cutover authorized
Canonical Replacement authorized
Final Activation authorized
Legacy Retirement authorized
```

---

## 31. Final Decision

```text
F11-D08
— Multi-Surface / Session / Delivery Consistency

DECISION:
HUMAN_APPROVED / FROZEN
```

Banyan 正式保持：

- Surface、Session、Logical Interaction、Delivery 与 Domain Truth 分离。
- Session 不拥有 Runtime、Decision、Attention 或 Result Truth。
- Reconnect 先恢复 Current Truth，再恢复 Presentation Context。
- Unknown Outcome 不允许 Blind Resubmission。
- Offline Capture 不创造未来 Runtime Permission。
- Draft 可跨 Session 保存，但仍只是 Draft。
- Cross-surface Consistency 追求语义一致，而不是 UI 完全一致。
- Late / Duplicate / Missing / Out-of-order Delivery 不得重新定义 Domain Truth。
- Logical Interaction Identity 独立于 Transport Attempt。
- Lower-layer UI / Continuity State 不得提升为 Higher-layer Domain Truth。
- Runtime Permission 必须在 Point-of-use 重新解析。
- Session Resume != Runtime Resume。
- Transport Retry != Runtime Retry。
- Transport Cancellation != Runtime Cancellation。
- F10 保持 Runtime Authority。
- D03 保持 Control Semantics。
- D04 保持 Decision Semantics。
- D07 保持 Attention Policy。
- D09 保持 Visibility / Sensitive Data。
- F11-D08 不建立 Global UI Truth Store 或 Session Truth Store。

**Implementation remains NOT_AUTHORIZED.**

---

**END OF F11-D08 HUMAN_APPROVED FREEZE**

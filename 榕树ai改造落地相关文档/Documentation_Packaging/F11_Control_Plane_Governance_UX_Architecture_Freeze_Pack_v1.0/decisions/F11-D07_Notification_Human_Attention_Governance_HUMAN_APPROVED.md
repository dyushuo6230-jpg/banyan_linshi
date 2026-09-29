# F11-D07 — Notification & Human Attention Governance
## 通知与人工注意力治理

**Stage:** F11 — Control Plane / Governance UX Architecture  
**Decision ID:** F11-D07  
**Status:** HUMAN_APPROVED / FROZEN

**Implementation:** NOT_AUTHORIZED

---

## 1. 决策定位

F11-D07 冻结 Human Attention（人工注意力）与 Notification（通知）之间的治理边界。

核心原则：

```text
Event != Notification
Operational Event != Human Attention Required
Human Attention Requirement != Notification Mechanism
Attention Required != Immediate Notification
```

F11 的目标不是“发生事件就通知人”，而是把人的注意力作为稀缺治理资源，仅在当前语义真正需要人工参与、知情或处理时进行受控路由。

---

## 2. Attention 维度分离

Attention 至少从以下维度理解：

```text
Impact
Materiality
Urgency
Actionability
```

并冻结：

```text
Decision Materiality != Notification Urgency
Governance Materiality != Time Urgency
Technical Severity != Human Attention Priority
System Severity != Notification Priority
Blocker Exists != Notify Human
```

---

## 3. Attention / Notification / Delivery 分离

正式冻结：

```text
Attention != Notification
Notification != Delivery
Delivery != Delivery Attempt
```

一个逻辑 AttentionSignal 可以产生多个 Delivery；多个 Delivery 不代表多个 Attention Requirement。

```text
Multiple Deliveries != Multiple Attention Requirements
Duplicate Delivery != New Attention Requirement
```

---

## 4. Acknowledge / Read / Dismiss / Snooze

正式冻结：

```text
Read != Acknowledged
Read Receipt != Human Understanding

Acknowledge
!= Resolution
!= Approval
!= Human Decision
!= Blocker Resolved

Dismiss != Acknowledge by default
Dismiss != Resolution
```

Snooze 只影响主动提醒/投递：

```text
Snooze
!= Governance Decision Defer
!= Obligation Deadline Mutation
```

Mute / Suppression 也不得改变底层治理义务：

```text
Notification Suppression != Requirement Suppression
Suppressed != Resolved
```

---

## 5. Reminder / Escalation

Reminder 必须基于仍然适用的 Attention Requirement：

```text
Scheduled Reminder != Eternal Authorization
Reminder Schedule != Requirement Deadline
Notification Timing Change != Obligation Timing Change
Reminder != Escalation
```

Escalation 必须来自 Material Attention Context 变化或明确治理规则。

```text
Unread alone != Escalation Basis
Lack of acknowledgement alone != New Materiality
Escalation != Unlimited Repetition
```

---

## 6. Dedup / Aggregation

多个 Event 可以映射为同一个 Attention Requirement：

```text
Multiple Events
may map to
one Attention Requirement
```

但：

```text
Same Subject != Same Attention Requirement
```

Dedup 不能只靠文本相同或时间接近，而应基于 Requirement / Subject / Human Participation / Material Basis / Lifecycle 等语义。

Aggregation 不得把不同治理语义合并掉：

```text
Aggregation != Semantic Merge
```

---

## 7. Human Participation

逻辑上区分：

```text
Human Decision Required
Human Action Required
Awareness
No Human Participation Required
```

Exact Enum Deferred。

正式：

```text
Informational Update != Action-required Attention
Attention Type != Urgency Rank
Attention Intensity != Governance Authority Level
```

---

## 8. Attention 生命周期

Attention 的完成来自底层 Requirement：

```text
Notification Completion != Domain Completion
Attention Completion follows underlying requirement
```

Attention 也可能因为当前要求 No Longer Applicable 而结束：

```text
Superseded Attention != Resolved by Human
Historical Notification != Current Attention Requirement
Attention History != Current Attention Queue
Unread Count != Outstanding Obligation Count
Attention Badge != Domain Obligation Truth
```

---

## 9. Recipient Governance

Recipient 必须依据 governed basis 解析，例如：

```text
Domain ownership
Governance authority
Project binding
Role assignment
Workflow responsibility
Subscription
Escalation policy
```

并保持：

```text
Notification Recipient != Decision Authority
Observer != Decision Actor
Responsible Owner != Required Actor by default
Escalation Recipient != Authority Transfer
Attention Escalation != Governance Delegation
Subscription != Ownership
Subscription != Authority
```

Multiple recipient candidates 不自动要求人工决策，应先使用既有 Role / Authority / Binding / Policy 解析。

---

## 10. Multi-surface / Delivery

同一个 Attention 可以通过 Web / IDE / Email / Mobile 等多个 Surface 投递，但：

```text
Multiple Surface Deliveries
remain one logical Attention

Surface != Attention Authority
Channel Delivery Result != Global Attention Result
Delivery Identity != Attention Identity
Delivery Retry != New Attention Requirement
```

跨 Surface 的 Acknowledge 不等于 Domain Resolution。

---

## 11. Notification Action Routing

通知中的动作必须保持原语义：

```text
Retry
→ D03 RuntimeControlIntent

Decide
→ D04 HumanDecisionInteraction

Acknowledge
→ D07 Attention Handling
```

正式：

```text
Action Surface != Authority Owner
Notification-contained Control Hint != Eternal Control Availability
Notification Link != Eternal Decision Applicability
Notification Snapshot != Current Attention Truth
```

打开历史通知时，应先恢复当前上下文。

---

## 12. Visibility Boundary

D07 决定：

```text
who / why / when attention
```

D09 决定：

```text
what detail may be safely shown
```

正式：

```text
Attention Eligibility != Full Detail Visibility
Notification Eligibility != Evidence Visibility
Data Visibility != Notification Eligibility
```

Redaction 不得把 “Decision Required” 变成普通 FYI。

---

## 13. 与其他 Decision 的边界

```text
D04:
Decision Interaction != Notification

D05:
Reason != Notification Priority

D06:
Result / Evidence Presence != Notification Requirement

D08:
D07 owns attention meaning / recipient / urgency / dedup / aggregation /
reminder / escalation / suppression;
D08 owns multi-surface / session / delivery continuity

D09:
D09 owns visibility / sensitive-data / presentation safety
```

---

## 14. Core Flow

```text
Observe
↓
Resolve whether human attention is required
↓
Classify human participation
↓
Evaluate impact / materiality / urgency / actionability
↓
Resolve recipient
↓
Deduplicate
↓
Aggregate where semantically safe
↓
Apply reminder / suppression / escalation policy
↓
Deliver
↓
Handle acknowledgement / snooze / dismissal
↓
Refresh applicability
↓
Reflect current and historical state
```

---

## 15. Core Invariants

```text
Event != Notification
Operational Failure != Human Notification Required
Human Attention Requirement != Notification Mechanism
Attention Required != Immediate Notification
Decision Materiality != Notification Urgency
Technical Severity != Human Attention Priority
Blocker Exists != Notify Human
AttentionSignal != Notification Delivery
Attention != Notification != Delivery != Delivery Attempt
Read != Acknowledged
Acknowledge != Human Decision
Acknowledge != Domain Resolution
Dismiss != Resolution
Snooze != Governance Decision Defer
Notification Suppression != Requirement Suppression
Reminder != Escalation
Multiple Deliveries != Multiple Attention Requirements
Aggregation != Semantic Merge
Notification Recipient != Decision Authority
Escalation Recipient != Authority Transfer
Attention Escalation != Governance Delegation
Surface != Attention Authority
Delivery Identity != Attention Identity
Delivery Retry != New Attention Requirement
Notification Eligibility != Full Detail Visibility
```

---

## 16. Deferred

```text
Exact Attention Enum
Exact Notification Priority Enum
Exact Recipient Enum
Exact notification channel catalog
Exact reminder schedule implementation
Exact escalation algorithm
Exact dedup implementation
Exact aggregation implementation
Exact delivery retry model
Exact notification store
Exact cross-device read / ack / snooze store
Exact UI layout
DB / Redis / REST / WebSocket / SSE / Go / TypeScript implementation
```

**END OF F11-D07 HUMAN_APPROVED FREEZE**

# F10 → F11 Formal Architecture Handoff

**Source Stage:** F10 — Runtime Permission / Execution Governance  
**Target Stage:** F11 — Control Plane / Governance UX Architecture  
**F10 Status:** `FINAL ARCHITECTURE FREEZE = HUMAN_APPROVED`  
**Implementation Authorization:** `NO`

---

## 1. F11 Entry Basis

F11 must treat the F10 freeze baseline as the formal Runtime-side contract.

F11 may design UX, projection and control surfaces around F10, but may not redefine F10 runtime authority.

---

## 2. F10 Responsibilities That Remain Active

```text
Runtime Permission
Point-of-use validation
Execution Context consumption
Runtime Provider resolution
Adapter routing
Execution Attempt lifecycle
Pause / Resume / Retry / Cancel enforcement
Failure classification / runtime recovery coordination
Runtime Result / Evidence / Trace
Cross-Action Runtime Scheduling
```

```text
F11 Stage Entry != F10 Retirement
```

---

## 3. F11 May Consume

F11 may consume purpose-sensitive runtime projections including:

```text
Subject / Task / Action references
Current Runtime State
Current Result
Failure / Recovery State
Progress basis where reliable
Reason / blocker / HOLD
Available governed Control Intents
Human Decision requirement
Trace / Evidence / Provenance refs
Relevant Scope
Downstream obligations
```

---

## 4. F11 May Submit

F11 may submit structured **Control Intent** such as:

```text
Inspect
Pause
Resume
Retry
Cancel
Acknowledge
Governed Decision Input
```

Exact catalog is deferred.

---

## 5. F11 Must Not Own

```text
Runtime Permission Authority
Runtime State Truth
Provider Binding Authority
Runtime Provider Resolution
Adapter Routing
Execution Attempt lifecycle
Product Authority
Design Authority
Apply Authorization
Canonical Mutation Authority
```

---

## 6. Critical Guards

```text
UI Action != Authority
Control Request != Runtime Permission
UI Enabled != Permission Granted
UI Disabled != Security Boundary
Button Visible != Action Authorized
User Runtime Control != Human Governance Decision
One UI Click != Decision + Authorization + Permission + Execution
Trace rendered in UI != Authorization
UNKNOWN != Human Decision Required
Missing Context != Human Input Required
```

---

## 7. Human Decision

Only genuine unresolved governance judgment should interrupt the user.

F11 is the presentation/input surface; it is not the DecisionProtocolDefinition owner.

```text
AI Recommendation != Human Decision
Decision Evidence != Apply Authorization != Runtime Permission
Human Decision != Immediate Canonical Mutation
```

---

## 8. Dynamic Runtime Handoff

D08 remains the dynamic runtime projection contract.

```text
D08 = Dynamic Runtime State Handoff
D09 = Stable Architecture Stage Handoff
```

F11 must obtain current runtime state from F10 rather than reconstructing it from history.

---

## 9. Point-of-use Revalidation

Any protected control intent returns to F10 for current-state validation.

```text
UI State Snapshot != Eternal Runtime State
Handoff Accepted != Eternal Validity
Cached Available Control != Eternal Available Control
```

---

## 10. Current Hard Prohibitions

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

F11 Architecture Entry does not change these.

---

## 11. Required F11 Working Method

At F11 start:

1. Perform four-source reconciliation.
2. Use repository formal freeze files as baseline.
3. Do not reopen F10 unless a real baseline conflict or new approved change appears.
4. Explain each F11 subtopic in plain Chinese with concrete examples.
5. Discuss first, then produce a complete approval draft.
6. Only explicit `HUMAN_APPROVED` approval counts.
7. Do not enter Implementation.

---

**END**

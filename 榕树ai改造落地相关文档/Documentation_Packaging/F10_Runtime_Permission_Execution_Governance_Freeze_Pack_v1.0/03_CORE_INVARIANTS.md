# F10 Core Invariants

This file is the compact invariant index for the F10 freeze baseline.

```text
Authorization != Runtime Permission
Runtime ALLOW != New Authorization
Runtime ALLOW != Semantic Decision

Execution Context != Canonical Truth
Minimum Sufficient != Governance-incomplete
More Context != More Authority

Provider Binding != Runtime Provider Resolution
Runtime Provider Selection != Durable Provider Binding
Provider Can Do It != Provider May Do It
Fallback != Retry
Adapter != Provider Selector
Adapter Capability != Permission

Task != Action != Execution Attempt
F10 Execution Attempt != F7 Apply Attempt
Retry != New Business Action
Pause != Failure
Pause != Cancel
Resume != Blind Continue
Retry != Blind Repeat
Cancel != Rollback
Timeout != No Side Effect
Outcome Unknown != Failure
Checkpoint != Canonical Acceptance

Failure Detection != Failure Ownership
Runtime Failure != Semantic Authority
Operational Failure != Semantic Conflict
Semantic Conflict != Retryable Failure
Recovery Action != Governance Exemption
Technical Recovery != Semantic Rollback
Recovery Success != Canonical Acceptance
Failure != Human Decision Required

Runtime Result != Evidence != Trace != Acceptance
Evidence != Authority
Trace != Authorization
Trace != Runtime Permission
Provider Success != Runtime Action Accepted
Execution Completed != Execution Accepted
Mutation Completed != Canonical Apply Succeeded
Attempt Result != Action Result
F10 Result != F7 Apply Result
Apply Result != Change Result
Runtime Acceptance != Product / Design / Canonical Acceptance

Workflow Orchestration != Runtime Scheduling
Runtime Scheduler != Workflow Authority
Action Ready != Runtime ALLOW
Waiting != Failed
Waiting != Blocked
Same Task != Shared Runtime Permission
Permission(A) != Permission(B)
Execution Context(A) != Execution Context(B)
Parallelism != Authority
Parallelism != Scope Expansion
Minimum Necessary Serialization
Runtime Dependency Evidence != Canonical Dependency
Resource Waiting != Semantic Dependency
Priority != Authority

F11 UI != Runtime Authority
UI Action != Authority
Control Request != Runtime Permission
UI Enabled != Permission Granted
UI Disabled != Security Boundary
User Runtime Control != Human Governance Decision
Decision Evidence != Apply Authorization != Runtime Permission
UNKNOWN != Human Decision Required
Missing Context != Human Input Required
Runtime State != User Action Required
UI Session Lifetime != Runtime State Lifetime
Duplicate Control Delivery != Duplicate Authorized Action

D08 Runtime Handoff != D09 Stage Handoff
Formal Handoff != Authority Transfer
F11 Stage Entry != F10 Retirement
F11 Stage Entry != Implementation Authorization

Architecture Complete != Implementation Authorized
Architecture Freeze != Runtime Activation
Stage Exit != Final Activation
Blocking Architecture Gap != Non-blocking Implementation Deferred
Deferred Obligation != Implementation Authorization
Architecture Exit Gate PASS != Implementation Entry Gate PASS
```

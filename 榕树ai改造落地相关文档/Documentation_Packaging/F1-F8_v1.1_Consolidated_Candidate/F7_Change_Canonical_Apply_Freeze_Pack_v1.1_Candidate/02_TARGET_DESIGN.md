# F7 Change / Canonical Apply — Target Design

> **Candidate status:** `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW`. v1.0 approval/freeze statements below are retained as historical source-contract evidence; this v1.1 text is not a new freeze or implementation authorization.


## 0. Target

F7 定义 Banyan 的 Governed Change / Canonical Apply 架构：

> 从 Change Intake / Workspace 开始，经 Base Reconciliation、Semantic Delta、Draft/Candidate、Decision/Approval/Authorization、Apply Plan、Freshness/Impact/Reference Validation、Stable Identity/Revision/Supersession、Atomic Canonical Apply、Concurrent Change Reconciliation，到 Semantic Rollback、History 和 Change Closeout 的完整治理闭环。

F7 的目标不是“所有变化都人工审批”，而是：

> **确定性的治理工作自动完成，真正需要 Authority / Value Judgment 的点才打扰人。**

---

## 1. End-to-End Architecture

```text
Intent / Change Intake / changes_temp / Provider Input
                         ↓
                    F7-D01
        Change Identity / Case / Workspace
                         ↓
                    F7-D02
        Base Binding / Reconciliation / Delta
                         ↓
                    F7-D03
        Draft / Candidate / Working Revision
                         ↓
                    F7-D04
 Decision / Approval / Apply Authorization Resolution
                         ↓
                    F7-D05
 Apply Scope / Expected Base / Write Set / Apply Plan
                         ↓
                    F7-D06
 Freshness / Divergence / Conflict / Impact / Reference
            ↙                     ↘
      D05 Replan              D04 Revalidation
            ↓                     ↓
                    F7-D08
 Stable ID / Canonical Revision / Reference / Supersession
                         ↓
                    F7-D07
 Canonical Apply Governance / Atomicity / Apply Attempt
                         ↓
                    F10 Runtime
 Permission / Adapter / Concrete Mutation Enforcement
                         ↓
               D07 Acceptance Evidence
                         ↓
                    F7-D09
 Related Open Change / Stale Draft Reconciliation
                         ↓
                    F7-D10
 Apply Result / Semantic Rollback / History / Closeout
```

`D-number != Runtime Call Order`。实际执行由 Contract Dependency / Workflow / Gate 编排。

---

## 2. Core Object Model

### 2.1 Change
```text
Change Case
- stable Change ID
- intent / problem
- scope
- target relations
- base bindings
- semantic deltas
- candidate lineage
- decision / approval / authorization lineage
- apply plans
- attempts / results
- history / closeout
```

### 2.2 Workspace
```text
Logical Change Workspace
- provider-neutral
- non-canonical
- 0..1 active provider binding by default
- OpenSpec may be reference provider
```

### 2.3 Draft / Candidate / Revision
```text
Draft = mutable non-canonical work
Candidate = meaningful option
Working Revision = governed snapshot of same Candidate evolution
```

### 2.4 Apply Plan
```text
Apply Plan
- stable plan identity
- plan revision
- apply scope
- expected base per target
- resolved write set
- preservation constraints
- impact set
- authorization binding / envelope
- dependencies / atomicity obligations
```

### 2.5 Apply Attempt
```text
Apply Attempt
- exact plan revision
- authorization ref
- observed expected bases
- actual mutation set
- atomicity strategy
- checkpoint
- mutation / validation / recovery result
```

---


### Candidate integration — durable mutation boundary

A task-scoped Assignment, workflow selection, binding resolution or effective result is not a Change. Durable protected Assignment/Binding/Profile/Authority mutation enters F7 only when its owner has established the semantic target and applicable authorization. F7 does not acquire the domain authority of F1/F3/F5/F6/F8 by applying it.
## 3. Truth / Authority Separation

```text
Change Workspace != Canonical Truth
Draft != Canonical Truth
Candidate != Human Decision
Selected Candidate != Apply Authorization
Apply Plan != Apply Authorization
Runtime ALLOW != Product / Design Decision
Index / SQLite / Trace != Canonical Relationship Authority
History / Audit != Authorization
```

Source / Product / Design / Apply / Runtime Authorities remain distinct.

---


### Candidate integration — authority and reconciliation

Valid human decision evidence may rank high in reconciliation, but does not replace current canonical truth. Effective Authority is a scope/domain/action-specific derived result from governed bindings; identity, role, evidence, later handoff or gate PASS creates none. Target semantic delta requires governed change, approval where applicable, apply authorization, protected apply, post-mutation validation and canonical acceptance. Selected workflow and approved exception are not blanket Apply Authorization.
## 4. Scope Model

```text
Change Scope
!= Apply Scope
!= Authorization Scope
```

Typical relation:

```text
Apply Scope ⊆ Change Scope
Apply Scope ⊆ Valid Authorization Envelope
```

Scope expansion requires Governance Routing.

---

## 5. Base / Freshness Model

```text
Change Base State
!= Apply Expected Base
```

Each target has its own Expected Base.

```text
Expected Base per Target
vs
Current Canonical State
→ Divergence Detection
```

Then:

```text
Divergence != Conflict
```

Deterministic, meaning-preserving reconciliation may auto rebase/replan.

---


### Candidate integration — scoped invalidation

Before protected mutation, check semantic delta, active dependency, scope, applicability and current-effective provenance. Upstream revision alone need not stale every dependent; STALE preserves history and blocks reliance on current effectiveness until owner re-resolution. Automatic re-resolution does not reauthorize expanded scope or new high-risk writes. Future F9 impact/index evidence is not mutation authority.
## 6. Semantic Delta / Write / Impact Model

```text
Semantic Delta = what meaning changes
Write Set = what canonical targets are directly mutated
Impact Set = what may be affected
```

```text
Semantic Delta != Write Set != Impact Set
```

Hidden Write is forbidden.

---

## 7. Stable Identity / Revision Model

```text
Stable ID = semantic subject identity
Revision = state of same subject
```

```text
Stable ID != Revision
Path != Stable ID
Provider ID != Stable ID
Latest Revision != Current Effective Revision
```

Subject change requires new Stable ID.

Accepted Canonical Revision history may not be silently rewritten.

---


### Candidate integration — references and links

Stable ID remains subject identity across path changes; Revision is accepted semantic evolution; Version is a governed release target, distinct from both. Product/design typed links and binding lifecycle relations retain reference identity, scope, provenance and explicit split/merge/supersession. Relation existence does not imply impact or authorization.

Version is not a Version Scheme, SemVer, or a patch-number alias for Revision. Not every accepted Revision is published as a Version and not every object needs a Version. Once published, an exact Version must keep its precise Release Target—one exact Revision or a coherent immutable release set. Repointing the same exact Version to another target silently would break historical reproducibility; a new Version or governed supersession is required. Governance-relevant `Latest` must be qualified by ordering domain; Latest Revision, Latest Canonical Revision, Latest Published Version, Latest Compatible Version and Latest Observed State are not interchangeable or Current Effective.
## 8. Reference Model

Core supports at least:

```text
Semantic Reference
→ Stable ID / current applicable resolution

Revision-Pinned Reference
→ Stable ID + exact revision

Version Reference
→ Stable ID + exact published version

Version Constraint Reference
→ Stable ID + governed version constraint
```

Reference relationships are semantic and evidence-backed.

```text
Reference != Authority
Supersession != Universal Retarget
Historical Reference != Broken Reference
```

Reference mutation is Canonical Mutation and must enter Write Set.

---

## 9. Canonical Apply Model

```text
Canonical Apply
!= File Write
!= Git Commit
!= DB Transaction
```

Canonical Apply is a governed formal state mutation.

Default:

```text
1 Apply Plan
→ 1 Semantic Atomicity Boundary
```

A Provider may implement:
- native transaction；
- stage + validate + atomic swap；
- checkpoint + mutate + recovery；
- other governed strategy。

Provider capability must satisfy required atomicity before mutation starts.

---


### Candidate integration — final guards

An applicable Development Entry state is required before development-driving protected mutation; a valid Apply Plan alone cannot supply it. At point of use, revalidate qualified handoff scope, authority, expected base, revision/version, freshness, gate/decision state, blockers and deferred guards. A mismatch pauses affected scope and routes to owner; it cannot grant F7 new semantic authority. Missing required qualifier is not PASS.

An earlier valid authorization and a later applicable HOLD are both retained; handoff sequence never determines authority priority. If authority expires, scope changes or a gate changes, pause the affected action, capture evidence and seek domain-owner re-resolution. A missing required qualifier yields UNKNOWN/UNRESOLVED, including for legacy boolean approval records; automatic check failure does not automatically mean human decision.
## 10. Validation / Acceptance Model

```text
Mutation Completed
!= Canonical Apply Succeeded
```

Success requires applicable:

```text
Mutation
→ Post-Mutation Validation
→ Reconciliation
→ Canonical Acceptance
```

Current Effective must not switch at the first physical write.

---

## 11. Concurrency Model

Banyan does not require a global one-change-at-a-time lock.

```text
Concurrent Change != Conflict
Stale != Invalid
File Overlap != Semantic Conflict
Different Files != Semantically Independent
```

Deterministic rebase is automatic.

Unresolved semantic merge is forbidden.

Provider lock / Git lock / DB lock is execution coordination, not semantic authority.

---

## 12. Recovery / Rollback Model

Before Canonical Acceptance:

```text
Failed Apply Attempt
→ Technical Recovery
```

After Canonical Acceptance:

```text
Semantic Rollback Intent
→ governed Change / Apply path
```

```text
Technical Recovery
!= Semantic Rollback
!= Compensating Change
!= Data Restoration
```

Post-close semantic rollback creates a new Change Case.

---


### Candidate integration — classified recovery

Classify failure before acting: a failed attempt, index refresh failure, partial canonical write, validation failure and governance block have different owners and recovery. Bounded retry keeps the same authorized semantic objective; pre-governed fallback is not retry or rebinding; technical recovery restores consistency and is not semantic rollback. Partial apply cannot be SUCCESS; a valid canonical success is not undone only because a derived index refresh failed.

Technical Recovery success does not mean the original operation succeeded or gained canonical acceptance. Rolling back an already accepted semantic change is a new governed Change Case, not restoring old bytes, compensating an operation or restoring data. Cancelled, rejected, superseded, skipped and no-change-required are typed non-failure outcomes; partial blocking does not imply whole-workflow failure.
## 13. Result / Closeout Model

```text
Attempt Result
!= Apply Result
!= Change Result
```

Change may close through:
- fully applied；
- no change required；
- rejected；
- cancelled；
- superseded；
- governed blocked/terminated outcome。

Closeout requires required obligations resolved, not necessarily mutation.

```text
Closed != Archived
Archive != Delete
```

---

## 14. Cross-Stage Runtime Handoff

```text
F8 → current project-instance bindings / project reconciliation
F9 → freshness / impact / index / retrieval evidence
F7 → governed interpretation and change/apply semantics
F10 → runtime permission / concrete execution enforcement
```

```text
Capability != Authority
Evidence Provider != Semantic Owner
Runtime Executor != Decision Authority
```

---


### Candidate integration — handoff qualifiers

The handoff preserves purpose, source owner, consumer, target, scope, authority and resolution basis, expected base/revision, freshness, typed state, UNKNOWN/BLOCKED/HOLD, provenance, downstream checks and active deferred guard. Acceptance of a handoff does not freeze its basis forever. Future F9 provides discovery evidence and F10 independently checks runtime permission; neither gains F7 or domain authority.
## 15. Performance Model

Normal path:

```text
Scope
→ Profile / Binding
→ Index / Stable ID
→ Targeted Canonical Read
→ Minimum Sufficient Evidence
→ Governed Resolver
```

Not:

```text
scan whole repository
load all history
load all rules
ask human every time
```

Human attention is reserved for genuine unresolved judgment.

---

## 16. AI Boundary

AI may:
- detect；
- classify；
- reconcile；
- recommend；
- build Draft / Candidate / Plan；
- perform deterministic rebase；
- route conflicts；
- execute already-authorized deterministic steps through runtime contracts。

AI may not:
- invent Authority；
- silently expand Boundary；
- choose arbitrary winner；
- silently merge unresolved semantics；
- grant Apply Authorization；
- convert Model Confidence into Authority；
- autonomously learn and activate governance rules。

---

## 17. Stage Result

```text
F7 Architecture Freeze = PASS
Implementation Authority = false
RP2 = false
Authority Cutover = false
Final Activation = false
```

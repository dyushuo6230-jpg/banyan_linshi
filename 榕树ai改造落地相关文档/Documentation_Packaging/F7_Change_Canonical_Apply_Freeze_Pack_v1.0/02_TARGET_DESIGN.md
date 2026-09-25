# F7 Change / Canonical Apply — Target Design

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

## 8. Reference Model

Core supports at least:

```text
Semantic Reference
→ Stable ID / current applicable resolution

Revision-Pinned Reference
→ Stable ID + exact revision
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

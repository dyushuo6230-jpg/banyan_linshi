# F7 Change / Canonical Apply — Implementation Boundary

## 0. Interpretation

`F7_Change_Canonical_Apply_Freeze_Pack_v1.0` 是 Architecture Freeze，不是 Implementation Freeze。

本 Pack 冻结：

```text
Change / Workspace semantics
Base / Delta semantics
Draft / Candidate / Revision semantics
Decision / Approval / Apply Authorization boundaries
Apply Plan / Expected Base / Write Set contract
Freshness / Conflict / Impact / Reference governance
Stable ID / Canonical Revision / Supersession rules
Canonical Apply / Atomicity / Apply Attempt obligations
Concurrency / Stale Draft reconciliation
Semantic Rollback / Result / Closeout / History semantics
Cross-stage handoff boundaries
```

它不直接批准真实项目写入。

---

## 1. Future Implementation MAY Realize

在后续 owner-stage contract、Implementation Plan、Implementation Freeze 和 slice-specific authorization 全部满足后，可以实现：

- Change Case registry；
- Logical Change Workspace；
- Workspace Provider Port / OpenSpec binding；
- Base Binding / Semantic Delta resolver；
- Draft / Candidate / Working Revision store；
- Decision / Approval / Apply Authorization binding；
- Apply Plan builder；
- Expected Base token binding；
- Write Set / Preservation / Impact Set；
- Apply Preview；
- Freshness / Divergence evaluation；
- Conflict owner routing；
- Reference discovery / reverse-reference query；
- Stable Semantic ID registry；
- Canonical Revision lineage；
- Supersession / reference migration support；
- Apply Attempt ledger；
- Atomicity strategy adapters；
- Checkpoint / recovery；
- bounded retry；
- Concurrent Change interaction analysis；
- stale-work rebase；
- Semantic Rollback planning；
- Apply Result / Change Result aggregation；
- History / Closeout / Archive semantics；
- F8/F9/F10 handoff adapters；
- audit / trace / provenance。

---

## 2. Explicitly NOT Frozen as Implementation

本 Pack 不固定：

- exact file/directory layout；
- exact YAML / JSON field names；
- exact enums；
- exact database schema；
- exact SQLite DDL；
- exact Stable ID syntax；
- exact revision number syntax；
- exact hash/fingerprint algorithm；
- exact lock/lease/CAS implementation；
- exact Git branch/commit strategy；
- exact OpenSpec file layout；
- exact transaction API；
- exact rollback API；
- exact retry count；
- exact timeout；
- exact CLI；
- exact WebUI；
- exact F8/F9/F10 concrete adapter API；
- production Canonical Apply execution；
- full migration / retirement implementation。

---

## 3. Mandatory Truth / Authority Guards

Future implementation must preserve:

```text
Workspace != Canonical Truth
Draft != Canonical Truth
Candidate != Human Decision
Decision != Approval
Approval != Apply Authorization
Apply Authorization != Runtime Permission
Runtime ALLOW != Semantic Decision
Reference != Authority
Index / SQLite / Trace != Canonical Relationship Authority
History / Audit != Authorization
```

Implementation convenience must not collapse these boundaries.

---

## 4. Mutation Guards

No Protected Canonical Mutation may bypass:

```text
Resolved Change / Scope
Applicable Semantic Delta
Valid Apply Plan Revision
Resolved Write Set
Expected Base / freshness requirements
Impact / Reference obligations
Valid Apply Authorization
Runtime permission enforcement
Final pre-mutation guard
Atomicity capability
Checkpoint / nonrollback disclosure where applicable
Post-mutation validation
Reconciliation / Canonical Acceptance
Audit / Trace
```

---

## 5. Hidden Write Guard

Future implementation must reject:

```text
Actual Mutation Target
not present in
Resolved Write Set
```

Any newly discovered protected target must return to D05/D06/D08/D09 as applicable.

---

## 6. Runtime Handoff Boundary

F7 defines the governance contract.

F10 owns concrete runtime enforcement.

```text
F7 defines WHAT MUST BE TRUE
F10 enforces HOW at runtime
```

F10 must not create Semantic Authority.

F7 must not embed Provider-specific executor details into Core semantics.

---

## 7. F9 Boundary

F9 may implement:

```text
Index
Search
Fingerprint
Cache
Freshness Evidence
Impact Query
Reverse Reference Query
```

But:

```text
F9 Evidence != F7 Governance Result
```

F7-D06 remains owner of the governed interpretation for a Change / Apply Plan.

---

## 8. F8 Boundary

F8 may implement:

```text
Project Instance
Binding
Profile Instance
Provider Selection
Version Pin
Project Reconciliation
```

F7 consumes the current project world but does not own project-instance truth.

---

## 9. Rollback Boundary

Implementation must preserve:

```text
Failed pre-acceptance Attempt
→ Technical Recovery

Accepted Canonical Meaning reversal
→ Semantic Rollback / governed Change path
```

A Git reset, file restore, DB restore, or local checkpoint restore must never be reported as Semantic Rollback unless the full D10 governance contract is satisfied.

---

## 10. Concurrency Boundary

Core must not require a global project-wide one-change-at-a-time lock.

Provider locks may coordinate execution but:

```text
Lock != Authority
Lock != Semantic Conflict Resolution
```

Expected Base / Final Guard / Atomicity / scoped conflict resolution remain mandatory.

---

## 11. Performance Boundary

Normal implementation path must prefer:

```text
Scope
→ Project Binding / Profile
→ Index / Stable ID
→ Targeted Canonical Read
→ Minimum Sufficient Evidence
→ Resolver
```

Do not implement normal operation as:
- full repository scan；
- full history load；
- all-rule load；
- user re-confirmation for deterministic work。

Token/performance optimization must not reduce governance fidelity.

---

## 12. AI Boundary

AI may execute deterministic governed work through authorized runtime contracts.

AI may not:
- invent Change Authority；
- invent Product/Design Meaning；
- silently create semantic winner；
- silently merge unresolved meanings；
- silently expand Apply Scope；
- silently add Hidden Writes；
- self-authorize Canonical Apply；
- self-authorize Semantic Rollback；
- convert Model Confidence into Authority；
- autonomously learn/promote governance policies。

---

## 13. Current Framework Reality

Current `banyan-framework` evidence includes:
- RuntimeAPI / evaluator；
- dry-run current-project execution；
- isolated-fixture execution；
- CommitPlanner / CommitExecutor；
- append-only trace；
- per-group checkpoint / recovery。

This does **not** prove:
- whole-plan semantic atomicity；
- production Canonical Apply；
- reference-safe mutation transaction；
- semantic rollback；
- F7 closeout；
- stable semantic revision registry。

Implementation gap analysis must be performed later against this pack.

---

## 14. Authorization Boundary

```text
Architecture Freeze = PASS
Implementation = NOT AUTHORIZED
RP2 = NOT AUTHORIZED
Authority Cutover = NOT AUTHORIZED
Real Canonical Apply Execution = NOT AUTHORIZED
Final Activation = NOT AUTHORIZED
```

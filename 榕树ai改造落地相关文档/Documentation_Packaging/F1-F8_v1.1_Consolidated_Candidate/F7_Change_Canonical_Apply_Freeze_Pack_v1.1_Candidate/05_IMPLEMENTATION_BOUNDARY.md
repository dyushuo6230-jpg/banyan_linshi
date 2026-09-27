# F7 Change / Canonical Apply — Implementation Boundary

> **Candidate status:** `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW`. v1.0 approval/freeze statements below are retained as historical source-contract evidence; this v1.1 text is not a new freeze or implementation authorization.


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

## Candidate deferred-obligation boundary

Deferred eligibility / Architecture Hole Test: a Material Deferred is valid only when its frozen boundary, explicit or deterministically derivable owner, specific resolution trigger, applicable must-happen-before, and forbidden-before-resolution actions are known, and currently authorized architecture remains correct and safe without the answer. Otherwise it is a current Architecture Gap; a material item with neither explicit nor derivable owner is a gap. "When needed" alone != Sufficient Trigger. The trigger determines when resolution must start, not authorization. Expected Future Artifact Type != Need To Create Empty Artifact Now. Deferred != Human Decision Required: deterministic owner/routing stays automatic; only multiple legitimate material choices with material consequence and no deterministic governance winner enter applicable informed/human decision. F2 PHYSICAL_STORE_TOPOLOGY retains its specific human-decision gate.

Logical lifecycle permits DEFERRED, READY_FOR_RESOLUTION, RESOLUTION_IN_PROGRESS, RESOLVED, SUPERSEDED and NOT_APPLICABLE; exact physical enum/schema remain deferred. DEFERRED != UNKNOWN (insufficient evidence) and DEFERRED != UNRESOLVED (resolution required now without a valid result). Trigger or Must-Happen-Before reached → RESOLUTION_REQUIRED / UNRESOLVED; it cannot remain silently DEFERRED, and a protected downstream action is BLOCKED. Closure by the applicable future owner records who declared and why, original trigger, future owner and owner changes, resolution, supersession and closure provenance; SUPERSEDED does not delete history and NOT_APPLICABLE is not failure. Deferred Obligation Resolved != Implementation Completed; Implementation Completed != Activated; Deferred Resolution != Final Activation Authorization.

Deferred-specific handoff adds the deferred topic, frozen boundary, trigger, dependencies, forbidden actions and expected future resolution to the applicable general Patch 017 handoff qualifiers, including owner, scope, provenance, must-happen-before and active guard. Deferred Handoff != Current Authority Transfer. Deferred Handoff != Implementation Authorization. Receipt confers neither canonical mutation nor other present permission.

Common Deferred Contract + domain-owned declaration + future index/discovery is the governance structure; GlobalDeferredAuthority = FORBIDDEN and UniversalFutureOwnerRegistry = FORBIDDEN. Future F9 may index obligation, owner, trigger, dependency and must-happen-before, but Index != Deferred Authority and Index Miss != Deferred Obligation Absent. Future F11 may display pending decisions/gates/obligations, but UX Status != Resolution Authority and UX-owned != Governance Authority. F12 may plan migration/retirement, but Migration-owned != Migration Authorized and Retirement Planning != Retirement Authorized. Resolve future-owner conflicts first through existing Owner Matrix, domain semantics, scope and authority; Later Stage Wins is invalid, and only a genuinely unresolved material conflict reaches applicable human governance.

Implementation-owned Deferred may cover exact Go interface, serialization, cache representation or physical enum only after architecture semantics are sufficiently frozen. Implementation-owned Deferred cannot silently redefine Architecture Contract: Implementation Evidence → Architecture Change Proposal → Applicable Owner; Current Code does not become Architecture Truth. Premature Deferred Activation = FORBIDDEN: future capability, migration, runtime or canonical change cannot execute before its Deferred gate and lawful resolution. Future Owner != Current Authorization; Assigned Future Stage != Activated Capability.

A Deferred Obligation is a governed obligation reserved for resolution by a future owner or gate, not a new F1 top-level object or an already executable development task. Deferred Obligation != Backlog Task. Deferred Obligation != Implementation Task. Reaching its trigger requires governed resolution; it does not turn the obligation into authorized implementation work.

Material deferred items retain subject, question, rationale, declaring owner, explicit or deterministically derivable future owner, trigger, preconditions, must-happen-before, forbidden-before-resolution guard, expected resolution, authority requirement, dependencies, status, provenance and closure/supersession history. Implementation Detail Deferred, Required Future Decision, Future Capability Reserved, and Migration/Cutover Deferred are distinct. DEFERRED is intentional postponement, unlike UNKNOWN evidence or UNRESOLVED required judgment; it is not undefined, forgotten, unowned or authorized work. A planning/governance dependency is not a runtime resolution dependency; implicit deferred cycles require architecture/planning resolution. Trigger reached requires a resolution attempt, not authorization; if prerequisites are absent the result is NOT_READY/UNKNOWN, and a protected action reaching its must-before boundary is BLOCKED. RESOLVED is neither IMPLEMENTED nor ACTIVATED. Supersession or NOT_APPLICABLE retains history. FUTURE is not an owner or miscellaneous unowned bucket; a future capability without a present implementation owner retains an explicit Owner Resolution Gate. Canonical mutation belongs to F7, project binding/reconciliation to F8, index/retrieval/freshness/impact to F9, runtime permission/execution to F10, UX/control plane to F11, and migration/retirement to F12. A later stage is not higher authority; future ownership grants no current authorization. Future Capability Reserved, including AI_AUTONOMOUS_LEARNING, is neither a roadmap commitment, current capability nor current authorization; activation requires a separate future proposal and applicable review. Exact schema/enum/API/UI/lock/CAS/index/migration mechanics remain deferred. Implementation, RP2, authority cutover, canonical replacement, final activation and legacy retirement remain NOT_AUTHORIZED; SQLite Physical Schema remains NOT_FROZEN.


### Exhaustive clause closure — remaining Patch 016 inequalities

Declaring Owner != Future Resolution Owner. The future implementation owner cannot redefine upstream architecture semantics, and the declaring owner must not pre-freeze that future owner's exact implementation. Deferred Guard != Authority. Convenience != Deferred Guard Override. Deferred category != priority. A material deferred item needs strong governance when it bears authority, canonical truth, owner, canonical apply, runtime permission, migration, cutover, or another protected boundary. Runtime-owned != Runtime Activated. Deferred governance audit != deferred implementation design. Reviewing a deferred item != freezing its implementation. Future extensibility != current authorization. A valid deferred item remains safe, owned or owner-resolvable, bounded, and future-recoverable. Reliable automatic routing applies when the owner is explicit or deterministically derivable; a safe deferred item does not become a human decision.

AI may inventory deferred items, classify them, resolve an already derivable owner, detect a reached trigger, detect premature activation, detect an owner conflict, and prepare a decision package. AI must not turn Deferred into Implemented, invent authority, silently choose a material future architecture, activate a future capability, treat a future owner as current permission, or remove a Deferred Guard.

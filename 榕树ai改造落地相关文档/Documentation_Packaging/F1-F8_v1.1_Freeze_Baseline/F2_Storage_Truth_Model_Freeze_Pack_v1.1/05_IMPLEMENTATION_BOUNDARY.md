# F2 Storage & Truth Model Freeze Pack v1.0

> **Freeze status:** `FROZEN_ARCHITECTURE_CONTRACT`. Human approval, architecture freeze, and this v1.1 freeze baseline are established. v1.0 approval/freeze statements below remain historical source-contract evidence. This freeze does not authorize implementation.

## 05_IMPLEMENTATION_BOUNDARY.md

F2 authorizes downstream architecture discussions to consume D01–D37 as frozen upstream design.

It does **not** authorize:

```text
RP2 implementation
Artifact authority cutover
Loader authority change
package/wheel authority change
.banyan activation
Runtime DB creation
Index DB creation
SQLite DDL
migration SQL
Final Activation
physical DB topology selection
```

Downstream ownership:

```text
F7 → Change / Decision / Canonical Apply workflow
F8 → ProjectInstance structure and configuration layout
F9 → Context / Index / Memory / Evidence / Impact / Query policy
F10 → Runtime / Provider / Permission / Adapter / Commit runtime

Storage Implementation Freeze
→ physical store topology + DDL + migrations
```

Mandatory future gate:

```text
F8 PASS
+
F9 PASS
+
F10 PASS
↓
Storage Implementation Freeze
```

At that gate, compare one DB vs separate Runtime/Index DBs, and a separate Evidence/Trace store if justified, then perform impact analysis and obtain Human Decision before any persistent DDL/migration work.

Examples such as Order / Payment / Inventory / Coupon are non-normative and must never become mandatory Banyan Core business-domain types.

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

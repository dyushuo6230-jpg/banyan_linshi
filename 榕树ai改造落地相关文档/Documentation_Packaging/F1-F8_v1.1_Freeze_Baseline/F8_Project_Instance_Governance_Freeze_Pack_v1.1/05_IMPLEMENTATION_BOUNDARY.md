# F8 Project Instance Governance — Implementation Boundary

> **Freeze status:** `FROZEN_ARCHITECTURE_CONTRACT`. Human approval, architecture freeze, and this v1.1 freeze baseline are established. v1.0 approval/freeze statements below remain historical source-contract evidence. This freeze does not authorize implementation.


## 0. Position

本 Pack 是 Architecture Freeze，不是 Implementation Freeze。

它冻结：

```text
Project Identity / Project Instance semantics
Source / Location Binding semantics
Project Profile / Overlay / Project Fact semantics
Provider Selection / Binding semantics
Version Pin / Compatibility semantics
Feature Activation / Gate / Effective State semantics
Existing / New Project Adoption semantics
Project Reconciliation / Drift / Refresh semantics
Project Instance Evolution boundary
Runtime Handoff boundary
Final Owner Map
Stage Closeout conditions
```

它不直接授权真实项目修改。

---

## 1. Future Implementation MAY Realize

在后续 Implementation Plan、Implementation Freeze、适用 Authority / Boundary / Gate 全部满足后，可以实现：

- Project Identity / Project Instance registry；
- Source Role / Mapping / Location Binding store；
- Project Profile Instance / Overlay store；
- Project Fact resolver；
- Provider Binding / Eligibility / Fallback resolver；
- Version Pin / Compatibility resolver；
- Feature Activation / Gate resolver；
- Effective Project Instance resolution；
- Existing Project discovery/adoption adapter；
- New Project initialization adapter；
- Observation / Drift / Reconciliation engine；
- scoped refresh / invalidation；
- task-scoped Project Instance Context builder；
- F9 Index/Freshness handoff adapter；
- F10 Runtime handoff adapter；
- Trace / Generated / Migration-lineage project surfaces；
- validation / audit / provenance。

---

## 2. Explicitly NOT Frozen as Implementation

本 Pack 不固定：

- exact `.banyan` physical schema；
- exact YAML / JSON field names；
- exact database / SQLite DDL；
- exact Stable ID syntax；
- exact directory layout for business sources；
- exact Profile file layout；
- exact Provider config shape；
- exact Version Pin syntax；
- exact Gate enum；
- exact Runtime Handoff DTO；
- exact cache/index implementation；
- exact revalidation timeout；
- exact polling / file watcher strategy；
- exact Git integration；
- exact WebUI；
- exact CLI；
- exact Provider runtime adapter；
- exact Legacy migration mechanics；
- exact Final Activation sequence。

---

## 3. Mandatory Truth / Authority Guards

Future implementation must preserve：

```text
Project Identity != Project Instance
Project Instance != Physical Directory
Source Role != Path
Mapping != Canonical Truth
Profile Instance != Authority
Overlay != Authority Override
Project Fact != Product / Design Truth
Provider Binding != Runtime Permission
Version != Revision
Latest != Current Effective
Feature Activated != Runtime Permission
Gate PASS != Authority
Observation != Truth
Drift Detection != Mutation Authorization
Index != Truth / Authority
Runtime ALLOW != Semantic Decision
```

---

## 4. Preserve-in-Place Guard

Existing Project 默认：

```text
PRESERVE_IN_PLACE
```

Implementation 不得因为 Banyan 接入而强迫：

- docs 搬家；
- source 重排；
- frontend/backend 重命名；
- 所有项目采用统一 root；
- 业务内容塞进 `.banyan`；
- 现有项目复制为“Banyan 项目”。

---

## 5. Binding Mutation Guard

Protected durable Binding change 必须进入：

```text
domain owner semantic resolution
→ F7 Governed Change / Canonical Apply
```

Implementation 不得建立：

```text
Rebinding bypass
Runtime self-healing canonical rewrite
Index-driven binding rewrite
Latest-file-wins mutation
```

---

## 6. Reconciliation Guard

D08 implementation 可以：

```text
observe
compare
classify
route
refresh derived state
```

但不得：

```text
silently rewrite canonical Project Instance facts
auto-create new Project Identity
promote Drift to Conflict without rules
ask Human for every Drift
```

---

## 7. Runtime Handoff Guard

F8 → F10 只交：

```text
Task-scoped
Minimum Sufficient
Derived
Rebuildable
Context
```

不得建立第二份 Canonical Project Instance。

F10 发现 stale/mismatch 时：

```text
→ re-resolve through F8/F9/domain owner
→ F7 if durable mutation required
```

不得由 Runtime 自己永久修改 Binding / Profile / Provider / Version / Feature truth。

---

## 8. F9 Boundary

F9 可以实现：

```text
Index
Search
Fingerprint
Cache
Freshness Evidence
Impact Query
Rebuild
```

但：

```text
F9 Evidence != F8 Semantic Authority
```

---

## 9. F10 Boundary

F10 可以实现：

```text
Runtime Permission
Provider Runtime
Adapter Execution
Pause / Resume / Retry Enforcement
Actual Action Execution
```

但：

```text
Runtime ALLOW != Project Instance Semantic Decision
```

---

## 10. F11 Boundary

F11 负责 WebUI / Control Plane / Governance UX。

F8 implementation 不提前把项目实例模型绑定到某个具体 UI。

---

## 11. F12 Boundary

F12 负责：

```text
Legacy Reconciliation
Migration
Retirement
Archive/Delete Gate
```

F8 Freeze 不允许直接删除 `.banyan-refactor`、Legacy 或进行 Final Cutover。

---

## 12. AI Learning Boundary

当前 Implementation 不设计：

```text
AI autonomous learning
AI automatic governance-rule creation
AI automatic Authority expansion
AI automatic stable-scope promotion from repeated use
AI autonomous policy optimization
```

可以保留扩展点，但不得为了未来能力增加当前 Core 复杂度。

---

## 13. Entry Boundary

F8 Architecture Freeze alone does not authorize implementation.

进入真实 Implementation 仍需：

```text
Applicable implementation plan
Implementation Freeze
Current Authority facts
Current Boundary
Current Gate
Current project evidence
F9/F10 applicable contracts
Slice-specific acceptance criteria
Explicit execution authorization where required
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

# F5 PRD Governance — Implementation Boundary

> **Freeze status:** `FROZEN_ARCHITECTURE_CONTRACT`. Human approval, architecture freeze, and this v1.1 freeze baseline are established. v1.0 approval/freeze statements below remain historical source-contract evidence. This freeze does not authorize implementation.


## 0. Freeze Meaning

`F5_PRD_Governance_Freeze_Pack_v1.0` represents **Architecture Freeze only**.

It freezes：

- Product semantic objects / responsibilities
- Authority boundaries
- Source of Truth boundaries
- Product lifecycle semantics
- Decision / Approval / Apply separation
- Change / CR product-side obligations
- Trace / impact obligations
- AI modification boundary
- Cross-stage ownership and invariants

It does **not** freeze implementation details and does **not** authorize implementation.

---

## 1. Global Authorization State

```text
Implementation Authorized       = false
RP2 Implementation Authorized   = false
Authority Cutover               = NOT_AUTHORIZED
Full Legacy Migration           = NOT_AUTHORIZED
Legacy Retirement/Delete        = NOT_AUTHORIZED
Final Activation                = NOT_AUTHORIZED
Cursor Coding                   = NOT_AUTHORIZED_BY_F5_FREEZE
```

F5 Architecture Freeze 不能被解释为“开始施工”的用户授权。

---

## 2. What a Future F5 Implementation MAY Realize

在独立 Implementation Entry Authorization 后，未来实现可以根据 Frozen Contract 构建：

- Requirement identity / revision / lifecycle representation
- Product Definition reconciliation and delta generation
- Gap classification and decision routing
- Candidate / Assumption / Deferred representation
- Decision / Approval evidence capture
- Product Definition version / baseline / effective-state semantics
- Requirement-side trace obligations and impact triggers
- Meeting / Review projection routing
- AI modification classification and write guards
- F5→F7 handoff contract
- F5→F9 trace/freshness/evidence requirements
- F5→F10 authority/permission enforcement requirements

但实现必须消费后续 owner-stage 的冻结合同，不能由 F5 单独臆造 F7/F9/F10 机制。

---

## 3. Explicitly Forbidden by F5 Freeze

在没有后续独立 Human Authorization 前，禁止：

- 修改当前项目业务代码。
- 修改正式数据库状态。
- 修改正式 API contract。
- 执行 real Canonical Apply。
- 对 Current Effective Product Semantics 做直接 free-edit。
- 以 AI recommendation / code / UI / test / design 替代 Human Product Decision。
- 把 Change Workspace / OpenSpec / SQLite / Index / Meeting Pack 变成第二 Product Truth。
- 让 Runtime `ALLOW` 自动产生 Product Decision。
- 根据 Role / Editor / Git Identity / Provider 推断 Product Authority。
- 进入 RP2。
- Authority Cutover。
- Full Legacy Migration。
- Legacy Retirement / Delete。
- Final Activation。

---

## 4. Deferred Implementation Details

以下内容明确留到 Implementation Freeze 或 owner stage：

```text
exact directory
exact YAML / JSON schema
exact field names
exact enums
SQLite DDL / indexes
exact version syntax
exact PRD physical decomposition
exact Change Workspace schema
exact AuthorizationRecord schema
Canonical Apply API
Runtime API
CLI
WebUI routes / pages / dialogs
RBAC / ABAC mechanics
Git branch / commit mechanics
Apply transaction implementation
rollback algorithm
OpenSpec physical representation
exact L0-L4 runtime mapping
```

任何后续设计不得引用 F5 Freeze Pack 来声称上述实现细节已经批准。

---

## 5. Owner-stage Boundaries

### F6
Owns UI_SPEC / Design Truth / Visual Governance details. Must not override Product Truth.

### F7
Owns Change Workspace execution / Canonical Apply / reference-safe mutation / rollback / supersession mechanics. Must consume F5 decisions rather than invent Product Meaning.

### F8
Owns Project Instance / binding / overlay / project-level authority/source/provider resolution mechanics. Must not infer UNKNOWN authority.

### F9
Owns Context / Index / Memory / Evidence / Freshness / Query / Rebuild. Its stores remain derived/noncanonical where F5 says so.

### F10
Owns Runtime Permission / Authorization Validation / Provider / Adapter / Write Guard / Execution. Runtime permission cannot create Product Authority.

### F11
Owns WebUI / Help / Control Plane UX. UI interaction alone cannot create authority without validated semantics/scope.

### F12
Owns Legacy Reconciliation / Retirement. Retirement requires no-loss/migration/authority gates.

---

## 6. Implementation Entry Preconditions

Future implementation must not start until a separate implementation-entry decision confirms at minimum：

- F5 Freeze Pack remains current and unsuperseded.
- Required owner-stage contracts for the intended implementation slice are frozen.
- No unresolved high-impact Authority / Source-of-Truth ambiguity affects the target scope.
- Migration / rollback boundary for the implementation slice is defined where mutation occurs.
- Acceptance / plan-conformance gates for that implementation slice are defined.
- User explicitly authorizes implementation entry.

Until then：`IMPLEMENTATION HOLD`.

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

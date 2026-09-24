# F5 PRD Governance — Implementation Boundary

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

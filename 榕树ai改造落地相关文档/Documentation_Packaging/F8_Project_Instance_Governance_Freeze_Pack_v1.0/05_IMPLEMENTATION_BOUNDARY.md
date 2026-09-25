# F8 Project Instance Governance — Implementation Boundary

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

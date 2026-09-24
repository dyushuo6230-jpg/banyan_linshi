# F2 Storage & Truth Model Freeze Pack v1.0
## 01_RECONCILIATION.md

### 1. Purpose

This document records the final reconciliation basis for **F2 — Storage & Truth Model**.

F2 freezes the logical authority, truth, persistence, history, migration, rebuild, recovery, and indexing model that downstream Banyan stages must consume.

F2 does **not** authorize Runtime implementation, SQLite DDL, schema migration, RP2 authority cutover, `.banyan` activation, or Final Activation.

Final status:

```text
F2_ARCHITECTURE_FREEZE = PASS
F2_DECISIONS = D01..D37
HUMAN_APPROVED = 37/37

CODE_IMPLEMENTATION_AUTHORIZED = false
RP2_IMPLEMENTATION_AUTHORIZED = false
FINAL_ACTIVATION = NOT_AUTHORIZED
PHYSICAL_DB_TOPOLOGY_FROZEN = false
```

### 2. Reconciliation Sources

F2 was reconciled against four source families:

```text
A. Historical human-confirmed conversation decisions
B. Legacy v3.1 / CURRENT governance semantics
C. Accepted Refactor / Stage 03–15 evidence
D. Current Framework / R0 / R1 / RP1 accepted state
```

Evidence themes consumed include:

- Stage 03: Stable ID, Artifact/Registry, Source Role, Reference Integrity, Version / Status / Provenance.
- Stage 04: Project Instance, Source Mapping, Overlay, Provider Binding, runtime/index/trace/generated/migration logical locations, one writable truth migration design.
- Stage 06: Change Workspace, Canonical Apply, Preview, Impact, Reference Check, Apply Plan, Validation, Evidence, Reconciliation, Rollback.
- Stage 11: SQLite Shadow Index, Stable-ID Index, Reference Graph, Trace, History, Rebuild Pipeline, Unresolved Reference Registry, Query Surface.
- Stage 12: Context Selection, Freshness, current-vs-historical resolution, non-canonical memory/summary.
- Stage 13: Evidence, Impact Graph, typed impact classes, provenance, causality boundary.
- Stage 14/15: Permission / Governance / Runtime / Semantic Commit separation.
- R0/R1/RP1: accepted authority and migration state remain protected.

### 3. Protected Upstream Facts

```text
CURRENT Governance = v1.9.1 FINAL_FREEZE
FINAL_ACTIVATION = NOT_AUTHORIZED

R0 = PASS
R1 = PASS
RP1 = PASS

RP1 shadow artifacts = 43/43
R0/R1 authority remains unchanged until RP2
.banyan remains protected Project Instance pilot state
```

F2 is a target architecture freeze only.

### 4. Major Reconciliation Result

```text
Artifact Semantic Truth
→ governed file-based canonical sources

ProjectInstance / Binding Structured Truth
→ governed durable ProjectInstance configuration sources

RuntimeExecution Truth
→ durable operational store

Git Truth
→ commit object, author/committer, diff, parents, history

EvidenceTrace
→ durable evidence source

Context / Memory
→ non-canonical derived / ephemeral context

SQLite Index
→ derived, rebuildable query/index/navigation layer
```

No layer may silently promote itself into another layer's authority.

### 5. Historical Wording Reconciliation

Earlier Stage 04 language stated:

```text
Runtime/index are not truth
```

F2 resolves that wording as:

```text
Runtime / Index are not Artifact Semantic Truth.
```

Final interpretation:

```text
SQLite Index
= NOT Artifact Semantic Truth
= NOT Runtime Operational Authority

Runtime Store
= NOT Artifact Semantic Truth
= YES Durable Operational Truth
```

### 6. SQLite Purpose Reconciliation

SQLite is retained as a precise, fast, relationship-aware navigation and query layer for locating authoritative source files and source fragments relevant to a question, task, change, or impact analysis.

```text
User Question / Task
        ↓
SQLite Index
  - Stable IDs
  - Source locators
  - Derived retrieval data
  - Freshness
  - Typed relationship graph
        ↓
Context / Impact Policy
        ↓
Canonical Source Read
        ↓
Answer / Plan / Change
```

A search hit is a retrieval candidate, not truth by itself.

### 7. Relationship and Adaptive Query Reconciliation

```text
F2
→ graph/data substrate

F9
→ expand / stop / cross-module / full Impact policy
```

The relationship graph must be typed, directional, source/evidence-traceable, freshness-aware, and distinguish Explicit / Derived / Inferred relations.

Keyword similarity, path similarity, same commit, same batch, or temporal proximity must not automatically become engineering dependency.

All business-domain names used in examples such as Order / Payment / Inventory / Coupon / Refund / AfterSale are illustrative only and do not define framework-native modules or business semantics.

### 8. Canonical Apply Reconciliation

F2 does not replace F7 Change / Decision / Canonical Apply ownership.

F2 freezes only storage-level invariants:

```text
Predeclared Apply Plan / Write Set
Expected Base
Durable Apply Journal
Logical Apply Unit
No partial-success claim
Technical Recovery
Derived failure isolation
Human escalation boundary
```

### 9. Git / Identity Reconciliation

```text
Git Commit Object
= canonical Git history fact

Git Author name + email
= contribution identity

Contributor Profile
= optional display enhancement

Banyan Trace / Evidence
= semantic relationship between commit and Banyan work context

SQLite
= rebuildable index of those relationships
```

### 10. Migration / Cutover Reconciliation

```text
Before Cutover
Old Source = writable authority
New Target = shadow/read-only

Validate equivalence

Controlled Authority Cutover

After Cutover
New Target = writable authority
Old Source = historical / compatibility / rollback material
```

Long-term dual writable truth is forbidden.

### 11. Storage Implementation Decision Deferred

```text
PHYSICAL_STORE_TOPOLOGY
```

must be decided after F8 + F9 + F10 architecture freezes and before any persistent Runtime/Index DDL or migrations.

At least compare:

```text
A. One physical DB
B. Separate Runtime DB + Index DB
C. Runtime DB + Index DB + separate Evidence/Trace store, if justified
```

Then:

```text
Impact Analysis
→ Human Review
→ Human Decision
→ Physical Topology Freeze
→ DDL / Migration implementation
```

### 12. Final Reconciliation Result

```text
HARD_CONFLICT = 0
AUTHORITY_COLLISION = 0
DUPLICATE_WRITABLE_TRUTH = 0
F1_MODEL_CONFLICT = 0
R0_R1_RP1_AUTHORITY_DRIFT = 0
PREMATURE_PHYSICAL_DB_DECISION = 0
UNOWNED_FUTURE_DECISION = 0

F2_ARCHITECTURE_FREEZE = PASS
```

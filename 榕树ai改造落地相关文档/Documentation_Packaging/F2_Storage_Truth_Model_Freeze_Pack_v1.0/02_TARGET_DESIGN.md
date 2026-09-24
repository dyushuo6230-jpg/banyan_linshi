# F2 Storage & Truth Model Freeze Pack v1.0
## 02_TARGET_DESIGN.md

### 1. Target Architecture

```text
Definition / Project Artifact
→ Canonical Semantic Truth
→ governed Markdown / YAML / formal files

ProjectInstance / Binding
→ durable structured configuration truth

RuntimeExecution
→ durable operational truth

Git
→ commit/history/identity truth

EvidenceTrace
→ durable evidence source

Context / Memory
→ non-canonical derived context

SQLite Index
→ derived, rebuildable query/index/navigation layer
```

### 2. Core Rules

- One semantic fact has exactly one Canonical Write Target.
- A logical Artifact may be composite across multiple physical files.
- SQLite may store retrieval-oriented projections, not canonical semantics.
- ProjectInstance durable configuration is its own Structured Truth domain.
- RuntimeExecution may own Operational Truth without becoming Artifact Semantic Truth.
- Git native facts remain Git truth.
- EvidenceTrace must have durable backing where evidence is non-reconstructible.
- Context/Memory remain non-canonical unless explicitly promoted through governance.

### 3. Retrieval Model

```text
Question / Task
↓
Identify subject(s)
↓
Query index
↓
Retrieve stable IDs + source locators + freshness + relations
↓
F9 Query Scope Policy
↓
Select context set
↓
Read canonical sources
↓
Answer / Analyze / Plan
```

### 4. Relationship Model

Relationships must be:

```text
Typed
Directed
Provenance-aware
Freshness-aware
Explicit / Derived / Inferred distinguishable
```

Exact relation taxonomy is deferred.

### 5. Adaptive Query Scope

F2 provides the graph and retrieval substrate.

F9 decides when to expand, stop, cross domains, or escalate to full Impact Analysis.

SQLite must not perform uncontrolled recursion.

### 6. Freshness / Currentness / Authority

```text
Freshness
≠ Currentness
≠ Authority
```

No latest-wins, mtime-wins, or max-version-wins rule is allowed.

### 7. Stable ID / Version / Status / History

```text
Stable ID → logical identity
Version   → evolution
Status    → typed lifecycle state
History   → evolution path
Supersession → explicit replacement/split/merge/deprecation lineage
```

Stable ID is independent of file path, filename, ordinary edits, version bump, and Git commit.

### 8. Canonical Apply Consistency

```text
Governed Change
↓
Apply Plan / Write Set
↓
Expected Base validation
↓
Durable Apply Journal
↓
Canonical writes
↓
Canonical validation
↓
Apply finalization
↓
Derived index refresh
```

Logical atomicity is required; fake cross-file physical ACID is not.

### 9. Failure Rules

- Partial canonical write inside one Apply Unit cannot be SUCCESS.
- Technical Recovery should restore a known consistent state where possible.
- Unknown canonical consistency becomes RECOVERY_REQUIRED.
- Valid canonical success must not be rolled back merely because index/cache/generated projection refresh failed.
- Safe deterministic technical recovery is automatic; ambiguous/high-risk cases escalate to Human Decision.

### 10. Migration / Cutover

Exactly one writable truth is allowed.

```text
Old Authority writable
→ Target shadow/read-only
→ validate
→ controlled cutover
→ Target writable
→ Old source historical/compatibility/rollback
```

### 11. Recovery Classes

```text
CANONICAL_SEMANTIC
DURABLE_EVIDENCE
DURABLE_OPERATIONAL
DERIVED_REBUILDABLE
```

Backup, rebuild, restore validation, and failure severity follow the class.

### 12. Rebuild Acceptance

A rebuilt derived store must prove semantic equivalence, not merely file creation.

Required dimensions include:

```text
Stable ID coverage
Canonical source resolution
Relationship integrity
Status/version projection integrity
Freshness semantics
Unresolved-reference preservation
Query integrity
```

Byte identity may be additional evidence but is not the universal rule.

### 13. Runtime Store vs Index Store

```text
Runtime Store
= Durable Operational Truth

Index Store
= Derived Rebuildable Query Projection
```

Index rebuild/cleanup/migration must never destroy runtime truth.

Physical topology is deferred.

### 14. Mandatory Future Physical Store Gate

After F8/F9/F10 Architecture Freeze and before persistent DDL/migrations:

```text
Storage Implementation Freeze
```

must explicitly compare one DB vs separate Runtime/Index DBs, and a third Evidence/Trace store if justified, then obtain Human Decision.

### 15. Non-Goals

F2 does not freeze DDL, table/index names, exact YAML layout, one-vs-many DB count, WAL, locking, vacuum, backup cadence, RPO/RTO, exact Apply Journal medium, exact Evidence medium, exact status enums, full relation taxonomy, F9 query policy, or F7 Change workflow details.

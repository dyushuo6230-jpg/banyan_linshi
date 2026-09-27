# F2 Storage & Truth Model Freeze Pack v1.0

> **Freeze status:** `FROZEN_ARCHITECTURE_CONTRACT`. Human approval, architecture freeze, and this v1.1 freeze baseline are established. v1.0 approval/freeze statements below remain historical source-contract evidence. This freeze does not authorize implementation.

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


#### Candidate integration — canonical truth and derived results

Canonical Engineering Standard semantics have one write target under their standard owner. Project adoption, profile, pin and approved local facts are governed inputs. The project's current effective standard set is a scoped, rebuildable resolution result, even if cached or persisted. Neither that cache nor an index creates a second standard truth.

Typed state and freshness projections retain subject, domain, scope, provenance and owner. A shared label such as `CURRENT` or `BLOCKED` cannot be interpreted without its state domain. Reconciliation precedence ranks evidence for target intent; it does not grant canonical write authority.
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


#### Candidate integration — dependency-aware freshness

Relevant upstream semantic delta, active dependency, applicability and effective-result provenance determine whether a dependent projection needs re-evaluation. A revision change alone does not invalidate every downstream result. `STALE` suspends current-effective reliance while preserving historical truth; `UNKNOWN` cannot be projected into `PASS`. Future F9 indexes can identify a candidate impact set, but owners re-read canonical facts and resolve semantics.
### 7. Stable ID / Version / Status / History

```text
Stable ID → logical identity
Version   → evolution
Status    → typed lifecycle state
History   → evolution path
Supersession → explicit replacement/split/merge/deprecation lineage
```

Candidate supersession (AUDIT-PATCH-003): the diagram line `Version → evolution` is retained v1.0 wording. Current contract: Stable ID is subject identity; Revision is accepted evolution of that same subject; Version is a governed release coordinate. `Version != Revision`. Historical F2-D24 stays under `source_baseline` and is not the current version-axis definition. Every file save is not a new semantic revision. A physical move, rename, or binding change is not by itself a new object revision. A task effective context is not the project production current effective. One global framework version does not automatically cover every internal object version. Reactivating a prior revision does not rewrite revision history.

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


#### Candidate integration — failure classification

Classify observed abnormal conditions before recovery: operational error/failure, validation failure, dependency availability, drift/divergence, semantic conflict, governance block, governed exception request, or rollback need. Bounded retry repeats the same authorized semantic objective; pre-governed fallback changes an execution path; technical recovery restores consistency; semantic rollback is an F7 governed change. None is interchangeable. Derived-index refresh failure cannot erase a valid canonical success.
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

### Candidate integration — exhaustive approved-clause closure

Typed state keeps subject, domain, dimension, value, scope, context, basis, provenance, and owner. The same label in another domain is not the same state. Shared minimum meanings: STALE suspends current reliance and keeps history; UNKNOWN is insufficient evidence and is not false or absent; BLOCKED stops the affected protected action; CONFLICTED is a real incompatibility and is not a cycle, drift, divergence, error, or unknown; REVIEW_REQUIRED is an unresolved governance choice; HOLD waits for an authorized release and is not REVIEW_REQUIRED and not BLOCKED; SUPERSEDED is replaced and is not deleted. UNRESOLVED is a required resolution without a valid result and is not CONFLICTED. Adaptive gate states PASS, BLOCKED, HOLD, REVIEW_REQUIRED, UNRESOLVED, and STALE stay expressible and distinct. Event != State. Exception != State. Error != Conflict. State projection != state copy != authority transfer. Handoff state != receiving-domain state. State consumer != state owner. Governed state fact != derived effective state. Derived state != canonical truth. A cross-domain state change is not a direct downstream transition; the path is impact, then STALE or another typed non-current state, then owner re-resolution. Current effective != lifecycle != freshness. A new current value does not rewrite history. A snapshot is not authority. A local state block is not a global project block. Index miss != state absent. Legacy status that cannot be determined stays UNKNOWN or UNRESOLVED. AI guess != state-domain resolution.

A bare exception label is semantically ambiguous. Error != failure. A failed attempt != the final operation failure. Unbounded retry is forbidden. Retry allowed != retry until success. Warning != BLOCKED. A violation is not by itself a governed exception and is not by itself an operational error. Silent governed exception is forbidden. Silent durable rebinding is forbidden. GlobalExceptionManager, UniversalFailureEngine, and UniversalRecoveryEngine are forbidden. A downstream consumer may resolve UNKNOWN, BLOCKED, STALE, or UNAFFECTED. Failure propagation != state copy. Technical recovery != reconciliation != re-resolution. Failure handling order is a domain contract and is not governance precedence. Degraded != unrestricted success. Detection direction != authority direction. An index or trace that detects a condition does not gain authority to rewrite the upstream canonical fact.

Handoff integrity: GlobalHandoffAuthority and UniversalHandoffResolver are forbidden. Handoff composition != state-domain merge and != authority merge. Multiple authority references are not a combined authority. The same payload with a different handoff purpose is not the same authorization. Context compression != governance compression. Handoff projection != semantic downgrade. Upstream STALE cannot silently become CURRENT. BLOCKED and HOLD cannot disappear during handoff projection. Handoff accepted != basis valid forever. Point-of-use revalidation != full re-resolution and != recomputing the whole architecture every time. Missing required qualifier != PASS. Later consumer != higher authority. Handoff order != authority priority. Authority reference != authority transfer. Authority reference exists != authority still applicable. Decision evidence != apply authorization != runtime permission. Freshness evidence != authority. Handoff integrity != full evidence duplication. Effective resolution context != canonical truth. Index != handoff authority. Trace != handoff authority. Scope projection may narrow and must not silently enlarge. Revalidation failure != human decision required. Current effective handoff != eternal effective truth.

F2 closure: every file save != a new semantic revision. Non-semantic format, wording, or metadata change does not by itself invalidate every downstream result. F9 freshness or impact evidence != upgrade authorization. Shared engineering standard != global mandatory standard != project current effective standard != forced latest. Project adoption, profile, pin, scope, applicability, approved local exception, authority, policy, and freshness are resolution inputs. A project-local exception does not rewrite the shared canonical standard body. The effective standard set stays a scoped rebuildable result. Index miss != semantic absence. Canonical standard semantics keep one write target under the standard owner. A runtime mismatch must not rewrite upstream canonical truth, and there is no global impact authority center.

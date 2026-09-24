# F6 UI Design Governance — Implementation Boundary

## 0. Freeze Meaning

`F6_UI_Design_Governance_Freeze_Pack_v1.0` represents **Architecture Freeze only**.

It freezes:

- UI / Design governance objects and semantic responsibilities；
- Design Evidence / Design Truth / Design Package / UI_SPEC boundaries；
- Rule / Profile / Index / Context contracts；
- Token / Shared Foundation / Behavior / UI Data semantic boundaries；
- Implementation Guidance / IR / Pack boundaries；
- Validation / Drift / Regression semantics；
- Governed Repair / Mutation / Revalidation semantics；
- Authority vs Effective State separation；
- cross-stage owner obligations；
- key invariants and future implementation acceptance gates。

It does **not** freeze all physical implementation details and does **not by itself** grant permission to modify a real project.

---

## 1. Authorization Interpretation

Do not model the F6 stage as a permanent manually maintained Core boolean:

```text
Implementation = AUTHORIZED / NOT_AUTHORIZED
```

Instead distinguish:

```text
Architecture Contract Approval
```

from:

```text
Effective Execution Authorization State
```

Actual execution must be resolved from current:

```text
Scope
+ Profile
+ Applicable Rules
+ Authority Facts
+ Context
+ Gates
+ Revision / Freshness
↓
Resolver
↓
Effective State
```

This pack itself does not create project mutation authority.

Formal:

```text
Architecture Freeze
!=
Runtime Mutation Authorization

Governance Definition
!=
Issue-Level Mutation Authority
```

---

## 2. What Future Implementation MAY Realize

After applicable owner-stage contracts are frozen and an execution slice obtains valid effective authorization, implementation may realize contracts such as:

- material intake / batch / provenance / routing；
- design source provider contracts；
- scene normalization and semantic design evidence；
- UI Design / Frontend Rule module registry；
- Rule / Module stable IDs and versions；
- Profile / Binding；
- Module Index / Rule Association Index；
- Authority / applicability resolver；
- Effective Design Context compiler；
- Effective Implementation Context compiler；
- Token / Shared Foundation projection；
- Behavior / Interaction model；
- UI Data Semantic / Fixture support；
- Design Package / UI_SPEC workflow support；
- Effective UI Contract snapshot binding；
- Implementation Guidance / framework-neutral IR / Pack；
- Framework Adapter implementation；
- D09 target/scope/evidence/coverage validation；
- drift / regression classification；
- D10 authorization envelope / mutation scope / repair plan；
- bounded auto-repair policy；
- necessary local revalidation；
- retry budget / escalation / repair lineage；
- audit / trace / provenance。

But physical details must consume F7～F10 contracts where those stages own apply/runtime/index/project-instance mechanics.

---

## 3. Explicitly Forbidden Interpretations

F6 Freeze Pack must not be used to claim that the following have already been approved as concrete implementation:

- exact repository directory layout；
- exact YAML / JSON field names；
- exact enum names；
- SQLite DDL / indexes；
- vector DB / embedding engine；
- exact cache/fingerprint algorithm；
- exact API routes；
- exact CLI commands；
- exact WebUI pages；
- exact Figma / 墨刀 / AnyDesign SDK binding；
- exact React / Vue / AntD / Element Plus implementation；
- exact CSS strategy；
- exact retry count across all tasks；
- exact migration / rollback transaction；
- actual business code modification；
- actual project-wide refactor；
- RP2 entry；
- Final Activation；
- AI Autonomous Learning。

---

## 4. Authority and Truth Guards

Future implementation must preserve:

```text
PRD owns Product Meaning
UI_SPEC owns approved UI WHAT
Implementation owns HOW
```

It must not allow:

- Design Source → silent UI Authority promotion；
- Current Code → Design Truth promotion；
- Index / Cache / Context → Canonical Truth promotion；
- Validation Result → UI_SPEC rewrite；
- Repair Result → Canonical Truth；
- Runtime ALLOW → Design/Product Decision；
- Low Risk → Auto Repair Permission；
- AI recommendation → Authority；
- Profile order / file order / latest version → implicit priority；
- implementation convenience → reverse mutation of Design Truth。

---

## 5. Performance and Context Boundary

Future implementation must preserve targeted loading:

```text
Scope
→ Profile
→ Index
→ Targeted Canonical Read
→ Resolver
→ Minimum Sufficient Context
```

Do not implement normal operation as:

```text
scan whole repository
+ load whole rule catalog
+ load all history
+ re-ask user every time
```

Mandatory Authority / Safety / Current Contract / Blocker / Unknown information may not be omitted for token saving.

---

## 6. Automation Boundary

Future runtime should automatically execute deterministic work when all required governance conditions are already resolved.

Human/Governance intervention should be reserved for cases such as:

- Authority Change；
- Authority Conflict；
- unresolved semantic relation；
- High-Risk Gate；
- Canonical Truth Change；
- explicit rule requiring Human Decision。

Formal:

```text
Governed
!=
Manual Every Time

Automatic
!=
Ungoverned
```

AI may derive states and apply already-authorized deterministic operations.

AI may not:

- invent Authority；
- create permanent rules from history on its own；
- silently promote project rules to shared rules；
- silently change Hard Governance Invariant；
- silently expand mutation scope；
- silently convert unknown into fact。

---

## 7. D09 / D10 Implementation Boundary

### D09

D09 runtime may:

- resolve target；
- collect actual evidence；
- compare target/actual；
- classify difference/drift；
- run impact-driven regression checks；
- produce Validation Result；
- route findings。

D09 runtime may not:

- auto-create repair authorization；
- rewrite UI_SPEC / Design Package / PRD；
- automatically enter unbounded repair loop。

The explicit full-session trigger belongs specifically to D09 Full Conformance Session; it is not a general requirement for all deterministic validation/revalidation operations.

### D10

D10 runtime may mutate only when effective governance resolves:

```text
Valid Authorization
+
Authorized / Effective Mutation Scope
+
Repair Plan
+
Applicable Gate
```

Shared/high-impact mutation needs applicable authorization coverage.

Retry requires finite budget and stop conditions.

Escalation suspends affected mutation first.

---

## 8. Owner-Stage Boundaries

### F7
Owns:

- governed Change execution；
- Canonical Apply；
- rollback；
- reference-safe mutation；
- promotion apply；
- supersession apply mechanics。

F6 describes semantic obligations but must not invent F7 physical mechanisms.

### F8
Owns:

- Project Instance；
- `.banyan`；
- project Profile / Binding；
- provider selection；
- version pin；
- project init/adopt/migrate/reconcile mechanics。

### F9
Owns:

- SQLite / index implementation；
- retrieval；
- FTS / embedding；
- dependency graph；
- fingerprint；
- cache；
- freshness engine；
- impact query；
- rebuild mechanics。

F6 only freezes semantic contracts for Index / Context / Freshness / Impact consumption.

### F10
Owns:

- runtime permission；
- authorization validation enforcement；
- provider runtime；
- adapter runtime；
- execution / pause / resume / retry enforcement。

### F11
Owns:

- WebUI / Help / Control Plane UX；
- human review / conflict / impact presentation。

### F12
Owns:

- Legacy reconciliation；
- compatibility migration；
- retirement / archive / optional deletion gates。

---

## 9. Future AI Learning Boundary

Current stage only reserves extension points.

Future AI Learning must:

```text
produce Candidate / Recommendation
→ reuse Stable ID / Version / Trace
→ enter existing Governance / Change
→ obtain Authority
→ Canonical Apply through owner stage
```

It must not create a second Rule Store, Design Truth or Authority system.

---

## 10. Future Implementation Entry Preconditions

An actual implementation slice should not start merely because F6 Architecture Freeze exists.

Before mutation, the applicable execution process must be able to establish at least:

- relevant F6 Frozen Contract remains current and unsuperseded；
- applicable F7/F8/F9/F10 owner contracts for the intended slice are available；
- target Scope is explicit；
- required Authority facts are available；
- applicable Profile / Rule versions are resolvable；
- no unresolved blocking Authority / Canonical Truth conflict exists；
- expected mutation impact is bounded；
- rollback / recovery boundary exists where necessary；
- Acceptance / Plan Conformance gates for the slice are defined；
- Effective Execution Authorization State resolves to a mutation-eligible state。

Until these are satisfied for a concrete slice:

```text
NO MUTATION FROM F6 FREEZE ALONE
```

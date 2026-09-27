# F2 Storage & Truth Model Freeze Pack v1.0

> **Candidate status:** `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW`. v1.0 approval/freeze statements below are retained as historical source-contract evidence; this v1.1 text is not a new freeze or implementation authorization.

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

Material deferred items retain subject, question, declaring/future owner (or deterministic owner rule), trigger, preconditions, must-happen-before, forbidden-before-resolution guard, expected resolution, authority requirement, provenance and closure/supersession. Implementation Detail Deferred, Required Future Decision, Future Capability Reserved, and Migration/Cutover Deferred are distinct. DEFERRED is intentional postponement, unlike UNKNOWN evidence or UNRESOLVED required judgment. Trigger reached requires a resolution attempt, not authorization; if prerequisites are absent the result is NOT_READY/UNKNOWN, and a protected action reaching its must-before boundary is BLOCKED. RESOLVED is neither IMPLEMENTED nor ACTIVATED. Supersession or NOT_APPLICABLE retains history. Future owner is not current authority. Exact schema/enum/API/UI/lock/CAS/index/migration mechanics remain deferred. Implementation, RP2, authority cutover, canonical replacement, final activation and legacy retirement remain NOT_AUTHORIZED; SQLite Physical Schema remains NOT_FROZEN.

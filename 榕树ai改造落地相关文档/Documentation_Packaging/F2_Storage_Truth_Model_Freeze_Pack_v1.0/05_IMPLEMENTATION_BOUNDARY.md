# F2 Storage & Truth Model Freeze Pack v1.0
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

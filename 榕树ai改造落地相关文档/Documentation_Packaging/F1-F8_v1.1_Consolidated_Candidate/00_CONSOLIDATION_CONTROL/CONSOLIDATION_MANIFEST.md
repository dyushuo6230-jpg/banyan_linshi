# F1～F8 v1.1 Consolidated Candidate Manifest

| Field | Value |
|---|---|
| Input baseline | Eight immutable `F1_*_Freeze_Pack_v1.0` through `F8_*_Freeze_Pack_v1.0` directories; 48 files |
| Input audit layer | `PreF9_Architecture_Integrity_Review/10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-001` through `AUDIT-PATCH-017`, plus approved `AUDIT-PATCH-002-SUP-01` |
| Audit closeout | Batch 1～6 CLOSED; Final Cross-stage Review CLOSED |
| Output candidate | `F1-F8_v1.1_Consolidated_Candidate/` |
| Generated stage packs | F1 Core Object Model; F2 Storage Truth Model; F3 Definition Artifact Taxonomy; F4 Orchestration Semantic; F5 PRD Governance; F6 UI Design Governance; F7 Change Canonical Apply; F8 Project Instance Governance, each `v1.1_Candidate` |
| Control documents | Patch-to-Baseline Integration Map; Per-stage Merge Plan; Supersession Compatibility Matrix; No-Loss Reconciliation Report; Cross-stage Invariant Reconciliation; this Manifest; historical Final Consolidated Freeze Review; FCFR Correction Pass 01; historical Final Review Rerun 01; FCFR Correction Pass 02; historical Final Review Rerun 02; FCFR Correction Pass 03; Deferred Obligation Reconciliation; Final Exhaustive Discovery Before Repair; Final Normative Clause Coverage Matrix; FCFR Exhaustive Batch Correction |
| Candidate status | `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW` |
| Candidate / historical YAML state separation | `COMPLETED` across all 24 candidate YAML files; current lifecycle, approval, freeze and authorization are under `candidate_metadata`, while v1.0 approval/freeze evidence is under `source_baseline` |
| No-loss status | FCFR-001～005 repaired in Correction Pass 01; FCFR-R1-001 repaired in Correction Pass 02; Rerun 02's FCFR-R2-001～005 repaired in Correction Pass 03. Patch 016 clause-group coverage COMPLETE as correction evidence; independent Final Review rerun pending |
| Conflict status | First Final Review remains BLOCKED historical evidence; the identified Rule Entry owner ambiguity was repaired in FCFR-002, without granting approval |
| Remaining deferred | 14 material topics individually reconciled in `DEFERRED_OBLIGATION_RECONCILIATION.md`: 14 Still Deferred, 0 Resolved/Superseded/Not Applicable, 0 blocking architecture gaps. Item 5 boundary changed once: CON-002 architecture is resolved and only physical representation stays deferred. Owner changes remain 0. Exact schema/enum, physical SQLite DDL/topology, runtime API, CLI/WebUI, lock/CAS, index schema, migration mechanics, autonomous AI learning and later-owned F9/F10/F11/F12 details remain governed by their owner/gates |
| Authorization status | Implementation, RP2, authority cutover, canonical replacement, final activation and legacy retirement: `NOT_AUTHORIZED`; SQLite Physical Schema: `NOT_FROZEN` |
| Next required gate | Independent Final Consolidated Freeze Review Rerun 03; explicit human approval remains a separate later gate only if that review passes |

The candidate preserves each v1.0 pack's six-file order for reviewable diffs. YAML parsers can distinguish current Candidate state from historical v1.0 approval/freeze evidence without reading comments. This metadata restructuring does not change the integrated architecture semantics or complete the Final Consolidated Freeze Review. No F9 pack is included. Original v1.0 packs and the independent audit patch history remain untouched.

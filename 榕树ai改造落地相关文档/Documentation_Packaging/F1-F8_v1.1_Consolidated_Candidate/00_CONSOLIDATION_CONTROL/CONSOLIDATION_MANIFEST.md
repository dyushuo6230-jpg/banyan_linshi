# F1～F8 v1.1 Consolidated Candidate Manifest

| Field | Value |
|---|---|
| Input baseline | Eight immutable `F1_*_Freeze_Pack_v1.0` through `F8_*_Freeze_Pack_v1.0` directories; 48 files |
| Input audit layer | `PreF9_Architecture_Integrity_Review/10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-001` through `AUDIT-PATCH-017`, plus approved `AUDIT-PATCH-002-SUP-01` |
| Audit closeout | Batch 1～6 CLOSED; Final Cross-stage Review CLOSED |
| Output candidate | `F1-F8_v1.1_Consolidated_Candidate/` |
| Generated stage packs | F1 Core Object Model; F2 Storage Truth Model; F3 Definition Artifact Taxonomy; F4 Orchestration Semantic; F5 PRD Governance; F6 UI Design Governance; F7 Change Canonical Apply; F8 Project Instance Governance, each `v1.1_Candidate` |
| Control documents | Patch-to-Baseline Integration Map; Per-stage Merge Plan; Supersession Compatibility Matrix; No-Loss Reconciliation Report; Cross-stage Invariant Reconciliation; this Manifest; historical Final Consolidated Freeze Review; FCFR Correction Pass 01 |
| Candidate status | `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW` |
| Candidate / historical YAML state separation | `COMPLETED` across all 24 candidate YAML files; current lifecycle, approval, freeze and authorization are under `candidate_metadata`, while v1.0 approval/freeze evidence is under `source_baseline` |
| No-loss status | First Final Review found 003/004/005/016 incomplete and one F8 machine defect; FCFR Correction Pass 01 records deterministic repair 5/5 and 0 remaining known FCFR blockers; independent rerun pending |
| Conflict status | First Final Review remains BLOCKED historical evidence; the identified Rule Entry owner ambiguity was repaired in FCFR-002, without granting approval |
| Remaining deferred | Exact schema/enum, physical SQLite DDL/topology, runtime API, CLI/WebUI, lock/CAS, index schema, migration mechanics, autonomous AI learning and later-owned F9/F10/F11/F12 details |
| Authorization status | Implementation, RP2, authority cutover, canonical replacement, final activation and legacy retirement: `NOT_AUTHORIZED`; SQLite Physical Schema: `NOT_FROZEN` |
| Next required gate | Independent Final Consolidated Freeze Review rerun, then separate explicit approval before any new v1.1 Freeze Baseline |

The candidate preserves each v1.0 pack's six-file order for reviewable diffs. YAML parsers can distinguish current Candidate state from historical v1.0 approval/freeze evidence without reading comments. This metadata restructuring does not change the integrated architecture semantics or complete the Final Consolidated Freeze Review. No F9 pack is included. Original v1.0 packs and the independent audit patch history remain untouched.

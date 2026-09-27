# F1～F8 v1.1 Consolidated Candidate Manifest

| Field | Value |
|---|---|
| Input baseline | Eight immutable `F1_*_Freeze_Pack_v1.0` through `F8_*_Freeze_Pack_v1.0` directories; 48 files |
| Input audit layer | `PreF9_Architecture_Integrity_Review/10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-001` through `AUDIT-PATCH-017`, plus approved `AUDIT-PATCH-002-SUP-01` |
| Audit closeout | Batch 1～6 CLOSED; Final Cross-stage Review CLOSED |
| Output candidate | `F1-F8_v1.1_Consolidated_Candidate/` |
| Generated stage packs | F1 Core Object Model; F2 Storage Truth Model; F3 Definition Artifact Taxonomy; F4 Orchestration Semantic; F5 PRD Governance; F6 UI Design Governance; F7 Change Canonical Apply; F8 Project Instance Governance, each `v1.1_Candidate` |
| Control documents | Patch-to-Baseline Integration Map; Per-stage Merge Plan; Supersession Compatibility Matrix; No-Loss Reconciliation Report; Cross-stage Invariant Reconciliation; this Manifest |
| Candidate status | `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW` |
| No-loss status | Candidate integration mapping PASS: 17/17 formal patches plus 002-SUP-01; no mapped omission |
| Conflict status | No unresolved semantic/authority consolidation conflict identified in candidate; final human review pending |
| Remaining deferred | Exact schema/enum, physical SQLite DDL/topology, runtime API, CLI/WebUI, lock/CAS, index schema, migration mechanics, autonomous AI learning and later-owned F9/F10/F11/F12 details |
| Authorization status | Implementation, RP2, authority cutover, canonical replacement, final activation and legacy retirement: `NOT_AUTHORIZED`; SQLite Physical Schema: `NOT_FROZEN` |
| Next required gate | Human Final Consolidated Freeze Review, then separate explicit approval before any new v1.1 Freeze Baseline |

The candidate preserves each v1.0 pack's six-file order for reviewable diffs. Existing v1.0 approval/freeze fields carried within candidate copies are historical source-contract evidence only; candidate metadata takes precedence for candidate status. No F9 pack is included. Original v1.0 packs and the independent audit patch history remain untouched.

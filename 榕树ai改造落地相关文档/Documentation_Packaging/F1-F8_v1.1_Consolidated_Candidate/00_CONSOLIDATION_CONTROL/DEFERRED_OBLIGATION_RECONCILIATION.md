# Deferred Obligation Reconciliation — Correction Pass 03

Source authority: HUMAN_APPROVED `AUDIT-PATCH-016` §§6,8,29,33–34. Scope: existing F1～F8 v1.1 Candidate material future decisions, capability, cutover and safety-bearing implementation boundaries. `Stage / Topic` is a review reference, not a permanent Deferred ID, schema, registry or new authority. The eight common `05_IMPLEMENTATION_BOUNDARY.md` clauses are the governing test, not eight extra obligations. Routine exact fields/enums/API shapes are represented under their material parent where needed; no empty future artifact is created.

For each row, `Still Deferred` means the current Candidate has no valid resolution or authorization. `Owner Changed` and `Boundary Changed` compare the carried obligation with its earlier Candidate/source declaration, not the addition of the common Patch 016 explanation. No evidence of a completed resolution, supersession or non-applicability was found. The current guard is operative until the named trigger, prerequisites, owner decision and separate authorization are satisfied. A reached trigger never by itself grants work permission.

## Item reconciliation

### 1. F2 / PHYSICAL_STORE_TOPOLOGY — Required Future Decision

- **Source / declaring owner / future owner:** F2 `04_FROZEN_CONTRACT.yaml:118–148` and `05_IMPLEMENTATION_BOUNDARY.md:37–49`; F2 Storage Truth Model → `STORAGE_IMPLEMENTATION_FREEZE`. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** After F8/F9/F10 Architecture Freeze PASS, before persistent runtime/index DDL or storage migration; all three are prerequisites. Resolve before persistent runtime DDL, persistent index DDL and storage migration; those actions are forbidden while unresolved.
- **Dependencies / output / guard:** F8/F9/F10 PASS; human-approved physical store topology decision after comparing one DB with separate runtime/index and justified evidence store. Current guard: no physical topology selection or persistent DDL/migration. Existing `requires_human_decision: true` stays intact.
- **Validity:** Safe **YES** (logical truth boundary remains); owner-resolvable **YES** (explicit gate); bounded **YES** (DDL/migration deadline); future-recoverable **YES** (YAML carries fields/history). **VALID_DEFERRED**.

### 2. F3 / CONTEXT_RECOVERY_MAPPING — Implementation Detail Deferred

- **Source / declaring owner / future owner:** F3 `02_TARGET_DESIGN.md:93,101`, `05_IMPLEMENTATION_BOUNDARY.md:27–29`; F3 taxonomy → F9 Context/Index owner. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** When F9 Context architecture design starts; settle mapping before any Context Recovery reclassification or authority-moving migration. Current R1/RP1 artifacts may not be moved/reclassified by F3.
- **Dependencies / output / guard:** F3 frozen taxonomy and F9 context design; expected F9 mapping specification. Current guard: preserve current artifacts and authority until a separately governed migration.
- **Validity:** Safe **YES** (existing categories persist); owner-resolvable **YES**; bounded **YES**; future-recoverable **YES** (explicit F3→F9 carryover). **VALID_DEFERRED**.

### 3. F3 / PHYSICAL_TAXONOMY_MIGRATION — Migration / Cutover Deferred

- **Source / declaring owner / future owner:** F3 `05_IMPLEMENTATION_BOUNDARY.md:27–44`; F3 taxonomy → applicable Implementation Freeze for physical change, with F12 migration ownership and F7 governed mutation boundary. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** Before any physical taxonomy migration; resolve source/target, Stable ID, lineage, references, validation, compatibility, authority cutover, rollback and acceptance in Implementation Freeze before execution. No silent inferred mapping or physical reclassification.
- **Dependencies / output / guard:** F3 type contract, applicable F7/F12 and authority gates; expected migration plan plus implementation freeze. Current guard: RP1 artifacts and existing authority remain in place.
- **Validity:** Safe **YES** (no current migration); owner-resolvable **YES** (domain and execution owners distinct); bounded **YES**; future-recoverable **YES**. **VALID_DEFERRED**.

### 4. F4 / FULL_LEGACY_SEMANTIC_MIGRATION — Migration / Cutover Deferred

- **Source / declaring owner / future owner:** F4 `05_IMPLEMENTATION_BOUNDARY.md:15–33`; F4 orchestration → F12 legacy migration, with applicable domain owners for discovered semantics. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** When a full legacy migration is proposed/authorized; `CROSS-STAGE-GATE-01` and owner-stage resolution must precede execution. Full semantic migration and invented type/authority are forbidden before gate.
- **Dependencies / output / guard:** Cross-stage architecture and F12 migration planning; expected governed migration plan and owner-resolved exception proposals. Current guard allows inventory, discovery, classification, mapping, shadow work, compatibility and dry-run only.
- **Validity:** Safe **YES**; owner-resolvable **YES**; bounded **YES**; future-recoverable **YES** (named gate and permitted preparatory scope). **VALID_DEFERRED**.

### 5. F5 / CON-002_CONCRETE_AUTHORITY_WINNER — Required Future Decision

- **Source / declaring owner / future owner:** F5 `04_FROZEN_CONTRACT.yaml:245–262`, `01_RECONCILIATION.md:241`; F5 Product Authority declaration → applicable human Project Authority governance, with F8 project binding/reconciliation. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** When the concrete CON-002 project authority is needed for an applicable project action; resolve before projecting that project's authority as PASS or enabling protected work. No guessed concrete winner.
- **Dependencies / output / guard:** Specific project authority evidence and F8 scoped binding; expected governed project authority decision. Current guard is `TYPED_BLOCKED_HUMAN_PROJECT_AUTHORITY`, not a claim that F5 Product Semantic Architecture is undefined. The existing future human gate does not require a new decision in this correction pass.
- **Validity:** Safe **YES** (the affected action stays blocked); owner-resolvable **YES**; bounded **YES**; future-recoverable **YES** (explicit carried blocker). **VALID_DEFERRED**.

### 6. F6 / AI_AUTONOMOUS_LEARNING — Future Capability Reserved

- **Source / declaring owner / future owner:** F6 `05_IMPLEMENTATION_BOUNDARY.md:334–348`, F7 `04_FROZEN_CONTRACT.yaml:280–300`; F6 design and F7 apply boundaries → Owner Resolution Gate on explicit future capability proposal, then applicable semantic owner. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** Only when explicitly proposed as a future capability; owner and architecture/governance review before any implementation or activation. No autonomous promotion into Rule Store, Design Truth, Authority or Canonical Apply.
- **Dependencies / output / guard:** Future proposal and applicable F6/F7/domain review; expected capability approval and owner-resolved contract if proposed. Current guard: reserved extension point only, no roadmap commitment or current capability.
- **Validity:** Safe **YES**; owner-resolvable **YES** (explicit owner resolution gate); bounded **YES**; future-recoverable **YES**. **VALID_DEFERRED**.

### 7. F7 / CANONICAL_APPLY_IMPLEMENTATION — Implementation Detail Deferred

- **Source / declaring owner / future owner:** F7 `05_IMPLEMENTATION_BOUNDARY.md:30–87,149–160,223–234`; F7 canonical mutation semantics → later F7 Implementation Freeze, with F10 runtime enforcement. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** Before real Canonical Apply implementation/execution; exact transaction, lock/lease/CAS, rollback and API must follow frozen F7 guards and applicable implementation authorization. No production canonical write under this Candidate.
- **Dependencies / output / guard:** F7 expected-base/final-guard/atomicity and F10 permission contract; expected implementation specification. Current guard: lock is not authority and current canonical replacement remains forbidden.
- **Validity:** Safe **YES**; owner-resolvable **YES**; bounded **YES**; future-recoverable **YES**. **VALID_DEFERRED**.

### 8. F8 / PROJECT_INSTANCE_BINDING_IMPLEMENTATION — Implementation Detail Deferred

- **Source / declaring owner / future owner:** F8 `05_IMPLEMENTATION_BOUNDARY.md:31–77,168–185`; F8 Project Instance → later F8 Implementation Freeze, with F9 evidence/F10 execution consumers. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** Before real project binding/reconciliation, `.banyan` mutation or runtime handoff implementation; settle physical layout, version pin, gate DTO and invalidation mechanics under F8 semantics. No current project write or final cutover.
- **Dependencies / output / guard:** F8 effective-resolution/authority gates and F9/F10 applicable contracts; expected project-instance implementation specification. Current guard: typed UNKNOWN/BLOCKED/HOLD and separate runtime permission remain.
- **Validity:** Safe **YES**; owner-resolvable **YES**; bounded **YES**; future-recoverable **YES**. **VALID_DEFERRED**.

### 9. F9 / INDEX_FRESHNESS_DISCOVERY — Implementation Detail Deferred

- **Source / declaring owner / future owner:** F2 `05_IMPLEMENTATION_BOUNDARY.md:25–34`, F6 `05_IMPLEMENTATION_BOUNDARY.md:295–308`, F7 `05_IMPLEMENTATION_BOUNDARY.md:166–186`, F8 `05_IMPLEMENTATION_BOUNDARY.md:193–210`; these domain declarations → F9. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** When F9 architecture design starts, before persistent index DDL or operational index/freshness reliance. No derived index may become canonical truth or Deferred authority.
- **Dependencies / output / guard:** F2 storage topology gate and domain-owned truth/impact semantics; expected F9 architecture/index specification. Current guard: F9 may later discover obligation/owner/trigger/dependencies/must-before, but Index Miss != Deferred Obligation Absent.
- **Validity:** Safe **YES**; owner-resolvable **YES**; bounded **YES**; future-recoverable **YES** through domain declarations even without index. **VALID_DEFERRED**.

### 10. F10 / RUNTIME_PERMISSION_EXECUTION — Implementation Detail Deferred

- **Source / declaring owner / future owner:** F4 `05_IMPLEMENTATION_BOUNDARY.md:20–21`, F6 `05_IMPLEMENTATION_BOUNDARY.md:310–317`, F7 `05_IMPLEMENTATION_BOUNDARY.md:149–160`, F8 `05_IMPLEMENTATION_BOUNDARY.md:215–231`; domain semantics → F10 Runtime. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** Before F10 runtime implementation and any real execution/activation; resolve concrete permission and provider/adapter enforcement under owner-stage authority inputs. No current provider execution or permission-engine change.
- **Dependencies / output / guard:** F5 entry, F6 design, F7 apply, F8 binding/gate and relevant F9 freshness; expected runtime contract/implementation specification. Current guard: F10 enforces how, cannot create semantic authority.
- **Validity:** Safe **YES**; owner-resolvable **YES**; bounded **YES**; future-recoverable **YES**. **VALID_DEFERRED**.

### 11. F11 / GOVERNANCE_UX — Implementation Detail Deferred

- **Source / declaring owner / future owner:** F4 `05_IMPLEMENTATION_BOUNDARY.md:22`, F5 `05_IMPLEMENTATION_BOUNDARY.md:131–132`, F6 `05_IMPLEMENTATION_BOUNDARY.md:319–323`, F8 `05_IMPLEMENTATION_BOUNDARY.md:235–239`; domain declarations → F11 UX/Control Plane. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** When F11 UX design starts, before operational UX presents/acts on pending gates or decisions. No current WebUI implementation or UI-created authority.
- **Dependencies / output / guard:** Domain-owned state, scope, provenance and authority contracts; expected UX contract. Current guard: UX Status != Resolution Authority; display alone does not decide or authorize.
- **Validity:** Safe **YES**; owner-resolvable **YES**; bounded **YES**; future-recoverable **YES**. **VALID_DEFERRED**.

### 12. Cross-stage / RP2_AUTHORITY_CUTOVER — Migration / Cutover Deferred

- **Source / declaring owner / future owner:** F1 `05_IMPLEMENTATION_BOUNDARY.md:12–16`, F2 `05_IMPLEMENTATION_BOUNDARY.md:9–23`, F3 `05_IMPLEMENTATION_BOUNDARY.md:10–25`, F8 `05_IMPLEMENTATION_BOUNDARY.md:243–254`; current domain owners retain authority → separate RP2 cutover governance with F12 migration planning and applicable authority owners. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** Only on an explicit future RP2 authority-cutover proposal; architecture, discovery/package alignment, migration and authority gates before any loader/registry/package authority switch. Current RP1/R0 authority must not be silently replaced.
- **Dependencies / output / guard:** Approved RP2 plan and applicable owner decisions; expected governed cutover decision/plan. Current guard: `RP2 = NOT_AUTHORIZED` and Authority Cutover = NOT_AUTHORIZED.
- **Validity:** Safe **YES**; owner-resolvable **YES** through applicable domain/cutover governance; bounded **YES**; future-recoverable **YES** from multiple Stage guards and Patch 016 §29. **VALID_DEFERRED**.

### 13. Cross-stage / FINAL_ACTIVATION — Required Future Decision

- **Source / declaring owner / future owner:** F2 `05_IMPLEMENTATION_BOUNDARY.md:21`, F5 `05_IMPLEMENTATION_BOUNDARY.md:26–34`, F8 `05_IMPLEMENTATION_BOUNDARY.md:55–77`; domain declarations → applicable human final-activation governance (Patch 016 §29). Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** Explicit future final-activation proposal plus applicable readiness/dependency gates; resolve before production/final activation, canonical replacement or treating pilot as final. None are authorized by the Candidate.
- **Dependencies / output / guard:** Stage16 readiness and Stage17 pilot/shadow evidence plus applicable architecture/authority gates; expected explicit final-activation decision. Current guard: `final_activation = false`, `PASS_PILOT_ONLY`, no production activation.
- **Validity:** Safe **YES**; owner-resolvable **YES** (named governance gate); bounded **YES**; future-recoverable **YES**. **VALID_DEFERRED**.

### 14. F12 / LEGACY_RETIREMENT — Migration / Cutover Deferred

- **Source / declaring owner / future owner:** F4 `05_IMPLEMENTATION_BOUNDARY.md:23,28–33`, F5 `05_IMPLEMENTATION_BOUNDARY.md:131–135`, F8 `05_IMPLEMENTATION_BOUNDARY.md:243–254`; declaring domain owners → F12/RP9 legacy reconciliation/migration/retirement, with separate retirement authority. Status **Still Deferred**; Owner Changed **NO**; Boundary Changed **NO**.
- **Trigger / must-before / forbidden:** When legacy migration/retirement is explicitly authorized for planning; resolve completeness and exit gates before retirement/delete. Legacy deletion and replacement are forbidden now.
- **Dependencies / output / guard:** No-loss mapping, migration completeness, zero runtime dependency, rollback rehearsal, no valuable capability unmapped and applicable authority gate (Patch 016 §29); expected migration/retirement plan and separate authorization. Current guard: `Legacy Retirement = NOT_AUTHORIZED`.
- **Validity:** Safe **YES**; owner-resolvable **YES**; bounded **YES**; future-recoverable **YES**. **VALID_DEFERRED**.

## Consolidation result

| Measure | Result |
|---|---:|
| Material Deferred reviewed | 14 |
| Still Deferred / Resolved / Superseded / Not Applicable | 14 / 0 / 0 / 0 |
| Owner Changed / Boundary Changed | 0 / 0 |
| VALID_DEFERRED / BLOCKING_GAP | 14 / 0 |

Each still-deferred item can leave the present architecture correct and safe because its protected action remains barred until a specific future trigger and gate. This is a consolidation evidence finding, not a future implementation design, human decision, Final Review PASS, freeze or activation. The per-item status and history remain in the domain-owned source contracts; future F9 discovery may aid retrieval but cannot replace those sources.

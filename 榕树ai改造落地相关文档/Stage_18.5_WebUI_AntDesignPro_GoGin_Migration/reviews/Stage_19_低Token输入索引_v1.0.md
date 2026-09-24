# Stage 19 低 Token 输入索引 v1.0

## Primary Inputs

Read first:

1. `Stage_18.5_to_Stage_19_Gate_Review_v1.0.md`
2. Stage18.5:
   - `ACCEPTANCE_REPORT.md`
   - `STAGE19_RC_HANDOFF.yaml`
   - `evidence/FINAL_VERIFICATION.yaml`
   - `evidence/STAGE18_5_COVERAGE_REPORT.yaml`
3. Stage18:
   - Acceptance / Adapter validation / Next-stage handoff
4. Stage17:
   - Pilot activation acceptance / `.banyan` integrity
5. Stage15:
   - Runtime API handoff / compiler-runtime tests / Git safety
6. Stage14:
   - governance hard contracts
7. Stage11/12:
   - index/rebuild/freshness evidence only when required

## Do NOT Full-Read

Do not automatically load:

```text
all Stage01-18 source artifacts
all 1026 legacy assets
all project docs
all trace/history rows
```

Use evidence-on-demand.

## Acceptance Bundles

Group checks by:

```text
Architecture
Core Purity
Runtime/Policy
Git/Semantic Commit
WebUI/GoGin/Bridge
Adapters
Pilot Project Instance
Index/Trace/Provenance
Freshness/Blockers
No-Loss
RC Packaging
```

## Evidence-on-Demand Triggers

```text
CLAIM_WITHOUT_EVIDENCE
HASH_MISMATCH
CONTRACT_DRIFT
PURITY_SUSPECT
RUNTIME_BRIDGE_REGRESSION
POLICY_REGRESSION
ADAPTER_REGRESSION
PILOT_INTEGRITY_MISMATCH
INDEX_REBUILD_MISMATCH
PROVENANCE_GAP
NOLOSS_GAP
RC_BUILD_FAILURE
```

## Explicit Non-goals

```text
Legacy rediscovery
project document migration
Runtime rewrite
WebUI redesign
new adapter implementation
final activation
Stage20 execution
```

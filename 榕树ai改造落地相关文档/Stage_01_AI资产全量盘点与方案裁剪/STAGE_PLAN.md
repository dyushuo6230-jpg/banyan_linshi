# Stage 01 — STAGE PLAN

> Pack Version：1.9.1  
> Charter：v1.9.1 FINAL_FREEZE  
> Upstream Gate：Stage 00 → Stage 01 PASS

## 1. Plan

```text
01.0 Pack / Upstream Gate Check
↓
01.1 Baseline Freshness / Protected Scope Recheck
↓
01.2 Repository-wide Discovery Universe Build
↓
01.3 AI Asset Inventory
↓
01.4 Legacy Classification / Core Candidate
↓
01.5 Capability Discovery
↓
01.6 AI Generated Artifact Inventory
↓
01.7 Operational Artifact Inventory
↓
01.8 Duplicate / Conflict / Gap
↓
01.9 Git Identity / Commit Practice Inventory
↓
01.10 Preliminary Capability Preservation Matrix
↓
01.11 Preliminary Artifact Migration Matrix
↓
01.12 Discovery Coverage / No-Loss Gate
↓
01.13 Bootstrap Register / Trace Update
↓
01.14 Acceptance / NEXT_STAGE_HANDOFF
```

## 2. Upstream Gate

必须读取并验证：

```text
Stage 00 actual ACCEPTANCE_REPORT
Stage 00 NEXT_STAGE_HANDOFF
Stage 00 Gate Review
Bootstrap MIGRATION_REGISTER
Bootstrap BANYAN_REFACTOR_TRACE
```

如果用户在 Stage 00 后修改了 Repository：

- 记录 `BASELINE_DRIFT`；
- 评估是否影响 Secret/Protected Scope/Checkpoint；
- 不影响 Discovery 安全时记录后继续；
- 影响安全边界时 BLOCK，不静默沿用过期基线。

## 3. Output Location

```text
${REFRACTOR_CONTROL_ROOT}/stages/01/${RUN_ID}/
```

本阶段不写正式 `.banyan`。

## 4. Stage 02 Handoff 必须携带

```text
真实资产 Inventory
Capability Inventory
Generated/Operational Artifact Inventory
Duplicate/Conflict/Gap
Core Candidate Report
Preliminary Preservation / Migration Matrix
Git/Commit Practice Inventory
Open Questions
Existing Project Layout Preservation Contract candidate
13 Secret inherited protection
```

## 5. Definition of Done

```text
Discovery complete
+ Preliminary No-Loss complete
+ hard metrics = 0
+ no protected-path violation
+ Bootstrap trace/register updated
+ actual Acceptance Report
+ NEXT_STAGE_HANDOFF
+ Stage 02 Entry Gate PASS
```

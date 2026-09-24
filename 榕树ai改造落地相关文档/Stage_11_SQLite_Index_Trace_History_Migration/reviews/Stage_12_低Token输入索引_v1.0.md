# Stage 12 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_11_to_Stage_12_Gate_Review_v1.0.md`
2. Stage 11:
   - `evidence/NEXT_STAGE_HANDOFF.yaml`
   - `STAGE12_QUERY_SURFACE.yaml`
   - `UNRESOLVED_REFERENCE_REGISTRY.yaml`
   - `REBUILDABILITY_REPORT.yaml`
   - Shadow Index query results（只查询，不重建）
3. Stage 10:
   - Knowledge Freshness / Rebuildability / Handover contracts
4. Stage 05:
   - Decision Level / Human Confirmation
5. Stage 04:
   - Source Mapping / Project Instance
6. Stage 03:
   - Source Role / Authority
   - Version / Status / Provenance
   - AI Runtime Governance Contract

## 2. CON-002 定点读取

只读取：

```text
CON-002 conflict record
涉及的 source IDs
相关 source role
version/status/provenance
supersession
freshness observations
current/historical query result
```

不要重新读取全仓候选文档。

## 3. 四条历史缺目标引用

仅允许 exact-locator / exact-history 定点检查：

```text
nunu-go-api/app/admin/web/CONTRIBUTING.md
nunu-go-api/app/admin/web/CHANGELOG.en.md
```

及对应 source history/evidence。

禁止 broad repository search 猜目标。

## 4. Context Recovery 默认查询

优先使用 Stage 11 Query Surface：

```text
entity_freshness
source_version_history
conflict_state
current_progress
latest_handover_with_as_of
related_canonical_refs
related_operational_refs
subject_state_history
unresolved_references
projection_to_sources
source_to_projections
subject_trace
run_trace
```

## 5. Evidence-on-Demand Triggers

```text
FRESHNESS_CONFLICT_UNRESOLVED
AUTHORITY_COLLISION
CURRENTNESS_AMBIGUITY
HANDOVER_STALENESS
SUMMARY_SOURCE_GAP
TOKEN_BUDGET_QUALITY_RISK
REFERENCE_DISPOSITION_AMBIGUITY
MISSING_EVIDENCE
```

## 6. 默认禁止

```text
repository rediscovery
full docs reload
Git history reanalysis
full Stage01 asset body reload
Stage11 DB rebuild unless integrity issue
```

## 7. Token 主要花费对象

```text
CON-002
Freshness Policy
Context Selection
Context Recovery
Memory Layers
Compaction
Token Budget Gate
Cache Reuse
Historical Reference Disposition
```

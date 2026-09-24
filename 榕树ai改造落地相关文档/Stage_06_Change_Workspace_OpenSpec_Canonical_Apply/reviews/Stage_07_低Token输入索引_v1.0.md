# Stage 07 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_06_to_Stage_07_Gate_Review_v1.0.md`
2. Stage 06 `evidence/NEXT_STAGE_HANDOFF.yaml`
3. Stage 06:
   - `CHANGE_WORKSPACE_SCHEMA.yaml`
   - `CHANGE_LIFECYCLE_SCHEMA.yaml`
   - `ARTIFACT_RELATIONSHIP_SCHEMA.yaml`
   - `PARALLEL_DRAFT_CONTRACT.yaml`
   - `DRAFT_PROMOTION_CONTRACT.yaml`
   - `CANONICAL_APPLY_CONTRACT.yaml`
   - `REFERENCE_SAFE_RECONCILIATION_CONTRACT.yaml`
   - `ROLLBACK_CONTRACT.yaml`
4. Stage 05:
   - Workflow / Decision / Human Confirmation frozen contracts
   - CON-001 Resolution
5. Stage 04:
   - Project Instance Schema
   - Source Mapping Registry
   - Project Overlay Bindings
   - Variable Resolution
   - Provider Bindings
6. Stage 03:
   - Capability Contract Registry
   - Source Role Registry
   - Artifact Registry Schema
   - Reference Integrity Contract
   - Version/Status/Provenance Rules
7. Stage 01:
   - `PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX.yaml`
   - `PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX.yaml`
   - `AI_ASSET_INVENTORY.jsonl`
   - `LEGACY_AI_CAPABILITY_INVENTORY.jsonl`
   - `AI_GENERATED_ARTIFACT_INVENTORY.jsonl`
   - `OPERATIONAL_ARTIFACT_INVENTORY.jsonl`

## 2. Stage 01 大文件读取策略

不要一次性全文加载。

优先：

```text
按 capability_id
按 asset_id
按 artifact_id
按 source_role
按 candidate target
按 risk
```

定点读取。

## 3. v3.1 Legacy 定点范围

仅针对已在 Stage 01 Inventory 中登记的：

```text
common_prd_v3.1
项目 AI 文档治理入口
AI rules / skills / prompts
Progress / Handover / Trace
UI governance
Plain Document
Change / Draft / Reconciliation
```

读取证据。

禁止重新枚举整个仓库。

## 4. Evidence-on-Demand Triggers

```text
NOLOSS_GAP
REFERENCE_MAPPING_GAP
LEGACY_STATUS_AMBIGUITY
COMPATIBILITY_GAP
DERIVED_REBUILDABILITY_UNKNOWN
SOURCE_ROLE_COLLISION
MISSING_EVIDENCE
```

## 5. Token 主要花费对象

```text
Legacy → Frozen Contract Mapping
No-Loss Matrix
Compatibility Strategy
Reference Migration
Shadow Migration
Rollback
```

而不是重新做 Inventory。

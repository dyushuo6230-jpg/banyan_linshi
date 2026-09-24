# Stage 11 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_10_to_Stage_11_Gate_Review_v1.0.md`
2. Stage 10:
   - `evidence/NEXT_STAGE_HANDOFF.yaml`
   - `STAGE11_INDEX_REQUIREMENTS.yaml`
   - `KNOWLEDGE_SOURCE_AUTHORITY_CONTRACT.yaml`
   - `KNOWLEDGE_PROJECTION_CONTRACT.yaml`
   - `PROJECTION_REBUILDABILITY_CONTRACT.yaml`
3. Stage 03:
   - `ARTIFACT_REGISTRY_SCHEMA.yaml`
   - `SOURCE_ROLE_SCHEMA.yaml`
   - `SOURCE_ROLE_REGISTRY.yaml`
   - `REFERENCE_INTEGRITY_CONTRACT.yaml`
   - `VERSION_STATUS_PROVENANCE_RULES.yaml`
4. Stage 04:
   - `PROJECT_INSTANCE_SCHEMA.yaml`
   - `SOURCE_MAPPING_REGISTRY.yaml`
   - `PROVIDER_BINDING_SCHEMA.yaml`
5. Stage 05:
   - Workflow / Decision / Semantic Commit registries
6. Stage 06:
   - Change Workspace / Apply / Reconciliation contracts
7. Stage 07:
   - Capability / Artifact Migration Matrices
   - Reference Migration Map
   - No-Loss Coverage
8. Stage 08 / 09:
   - UI Governance / Design Intelligence registries and provenance-bearing outputs
9. Bootstrap:
   - `MIGRATION_REGISTER.bootstrap.yaml`
   - `BANYAN_REFACTOR_TRACE.bootstrap.yaml`

## 2. 不重新读取正文

默认不要读取：

```text
1026 assets bodies
425 artifact bodies
289 operational bodies
全部 PRD / ADR / UI_SPEC
全部 Plain Document
全部 Design Image corpus
全部 Git History
```

Index 先从 structured records 构建。

## 3. Evidence-on-Demand Triggers

仅：

```text
INDEX_ID_COLLISION
MISSING_STABLE_ID
REFERENCE_TARGET_AMBIGUITY
TRACE_LINEAGE_GAP
HISTORY_STATUS_AMBIGUITY
SOURCE_ROLE_MISMATCH
PROVENANCE_GAP
MISSING_EVIDENCE
```

才定点读取 source refs。

## 4. 4 条历史缺目标引用

直接继承为：

```text
UNRESOLVED_REFERENCE
```

不要全文搜索仓库试图“猜目标”。

## 5. 2 条正则字面量

保持：

```text
NOT_A_REFERENCE
```

不进入 unresolved reference count。

## 6. Token 主要花费对象

```text
Schema normalization
Stable IDs
Relations
Trace lineage
History semantics
Query contracts
Integrity validation
Rebuildability
```

而不是重新理解项目正文。

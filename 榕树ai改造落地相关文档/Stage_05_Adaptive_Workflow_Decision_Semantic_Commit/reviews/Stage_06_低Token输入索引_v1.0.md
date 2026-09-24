# Stage 06 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_05_to_Stage_06_Gate_Review_v1.0.md`
2. Stage 05 `evidence/NEXT_STAGE_HANDOFF.yaml`
3. Stage 05:
   - `WORKFLOW_POLICY_REGISTRY.yaml`
   - `DECISION_POLICY_REGISTRY.yaml`
   - `DECISION_LEVEL_SCHEMA.yaml`
   - `HUMAN_CONFIRMATION_CONTRACT.yaml`
   - `CON001_RESOLUTION_RECORD.yaml`
4. Stage 03:
   - `CAPABILITY_CONTRACT_REGISTRY.yaml`
   - `REFERENCE_INTEGRITY_CONTRACT.yaml`
   - `ARTIFACT_REGISTRY_SCHEMA.yaml`
   - `SOURCE_ROLE_SCHEMA.yaml`
   - `PROVIDER_PORT_SCHEMA.yaml`
5. Stage 04:
   - `PROJECT_INSTANCE_SCHEMA.yaml`
   - `SOURCE_MAPPING_REGISTRY.yaml`
   - `PROVIDER_BINDING_SCHEMA.yaml`
   - `PROJECT_OVERLAY_BINDINGS.yaml`

## 2. 定点能力

只围绕：

```text
CAP-CHANGE
CAP-PARALLEL
CAP-RECONCILE
CAP-IDREF
CAP-TRACE
```

读取 Stage 01 / Stage 02 对应 evidence refs。

不要重新加载全部 35 项能力正文。

## 3. OpenSpec 相关

仅在需要确认实际 legacy 行为时定点读取：

```text
OpenSpec 现有目录 / 模板 / change 生命周期
现有 proposal / specs / tasks / design 关系
现有 apply / archive / reconciliation 规则
```

不要扫描整个 docs 或 tools。

## 4. Evidence-on-Demand Trigger

```text
CHANGE_LIFECYCLE_AMBIGUITY
PROVIDER_BINDING_GAP
CANONICAL_APPLY_CONFLICT
REFERENCE_MIGRATION_RISK
PARALLEL_DRAFT_CONFLICT
MISSING_EVIDENCE
```

## 5. 默认禁止

```text
repository rediscovery
full asset inventory rebuild
full Git history analysis
Stage 03 contract rewrite
Stage 04 project instance redesign
Stage 05 decision policy redesign
```

## 6. Token 主要花费对象

```text
Change Workspace abstraction
Provider-neutral lifecycle
OpenSpec binding
Draft / Parallel Draft
Canonical Apply
Reference-safe promotion
Reconciliation
Rollback / recovery
```

# Stage 10 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_09_to_Stage_10_Gate_Review_v1.0.md`
2. Stage 09:
   - `evidence/NEXT_STAGE_HANDOFF.yaml`
   - `DESIGN_PACKAGE_CONTRACT.yaml`
   - `DESIGN_TRUTH_CONTRACT.yaml`
   - `CONFIDENCE_PROVENANCE_CONTRACT.yaml`
3. Stage 08:
   - `PRD_AUTHORITY_CONTRACT.yaml` 或等价冻结产物
   - `UI_SPEC_AUTHORITY_CONTRACT.yaml`
   - `UI_SPEC_SCHEMA.yaml`
   - `UI_VALIDATION_EVIDENCE_CONTRACT.yaml`
4. Stage 07:
   - `V31_GOVERNANCE_COMPATIBILITY_MAP.yaml`
   - `LEGACY_ARTIFACT_MIGRATION_MATRIX.yaml`
   - `LEGACY_CAPABILITY_MIGRATION_MATRIX.yaml`
5. Stage 03:
   - `SOURCE_ROLE_REGISTRY.yaml`
   - `ARTIFACT_REGISTRY_SCHEMA.yaml`
   - `REFERENCE_INTEGRITY_CONTRACT.yaml`
   - `VERSION_STATUS_PROVENANCE_RULES.yaml`

## 2. 定点 Legacy Knowledge 能力

只读取与以下能力相关的 evidence：

```text
Knowledge projection
Project guide
Progress / worklog
Handover
Context recovery
Plain document
Architecture diagram
Documentation map / navigation
```

## 3. Plain Document 定点读取

优先只读这些规划/规则类文档：

```text
白话文档总体编写规划
白话文档生成方案
plain-document 文档地图编写说明
总览相关文档编写方案
功能需求相关文档编写方案
分端页面相关文档编写方案
技术设计相关文档编写方案
架构图相关文档编写方案
```

不要全量读取所有生成正文。

## 4. Project Guide 定点读取

只读取支持：

```text
现有 Project Guide / AI Documentation Guide
当前文档入口
Progress / Handover
Canonical Source Map
```

的段落。

不要全文重读所有 docs/project。

## 5. Evidence-on-Demand Triggers

```text
KNOWLEDGE_AUTHORITY_AMBIGUITY
PROJECTION_SOURCE_GAP
PROJECTION_FRESHNESS_GAP
REBUILDABILITY_UNKNOWN
AUDIENCE_VIEW_COLLISION
PROGRESS_CURRENTNESS_CONFLICT
HANDOVER_CONTEXT_GAP
MISSING_EVIDENCE
```

## 6. 默认禁止

```text
repository rediscovery
full docs/project crawl
full plain-document corpus load
all PRD/ADR/API reload
Stage 11 index implementation
```

## 7. Token 主要花费对象

```text
Knowledge Authority
Projection
Guide
Audience Views
Freshness
Rebuildability
Provenance
Navigation
Progress / Handover
Stage11 Index Requirements
```

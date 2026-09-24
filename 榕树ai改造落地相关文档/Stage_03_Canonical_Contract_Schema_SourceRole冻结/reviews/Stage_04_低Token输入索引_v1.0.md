# Stage 04 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_03_to_Stage_04_Gate_Review_v1.0.md`
2. Stage 03 `evidence/NEXT_STAGE_HANDOFF.yaml`
3. `CAPABILITY_CONTRACT_REGISTRY.yaml`
4. `SOURCE_ROLE_SCHEMA.yaml`
5. `SOURCE_ROLE_REGISTRY.yaml`
6. `PROJECT_OVERLAY_SCHEMA.yaml`
7. `PROVIDER_PORT_SCHEMA.yaml`
8. `BOOTSTRAP_CANONICAL_STATE_CONTRACT.yaml`
9. `EXISTING_PROJECT_LAYOUT_PRESERVATION_CONTRACT.yaml`
10. `AI_RUNTIME_GOVERNANCE_CONTRACT.yaml`
11. `CONFLICT_CARRYOVER_REGISTER.yaml`
12. `CONTRACT_COVERAGE_REPORT.yaml`

## 2. 按需读取

仅当出现：

```text
CONTRACT_AMBIGUITY
MISSING_BINDING
PROJECT_MAPPING_COLLISION
PROVIDER_PORT_GAP
ACTIVATION_BLOCKER
```

才读取：

```text
Stage 03 Acceptance
Stage 03 Validation
Stage 02 Capability Mapping
Stage 02 Candidate files
Stage 01 specific evidence_refs
```

## 3. 默认禁止

不要：

```text
重新扫描 Repository
重新生成 AI Asset Inventory
重新跑 Git History
重新分类 35 Capability
重新设计 Stage 03 Frozen Contract
```

## 4. Stage 04 主要 Token 花费对象

应集中在：

```text
Project Instance Layout
Source Mapping
Project Overlay
Profile / Variable Resolution
Provider Binding
Initialization / Adoption
Bootstrap → Canonical Migration Design
```

## 5. 目标

把 Stage 03 Frozen Contract 转成：

```text
可实施的 Project Instance / Mapping / Binding 设计
```

而不是再做一次 Discovery。

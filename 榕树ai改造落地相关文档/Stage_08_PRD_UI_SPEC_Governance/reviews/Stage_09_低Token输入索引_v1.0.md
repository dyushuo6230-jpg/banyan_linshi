# Stage 09 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_08_to_Stage_09_Gate_Review_v1.0.md`
2. Stage 08:
   - `evidence/NEXT_STAGE_HANDOFF.yaml`
   - `DESIGN_EVIDENCE_SCHEMA.yaml`
   - `UI_SPEC_SCHEMA.yaml`
   - `UI_SPEC_AUTHORITY_CONTRACT.yaml`
   - `UI_GOVERNANCE_SCOPE_SCHEMA.yaml`
   - `UI_IMPLEMENTATION_READINESS.yaml`
   - `UI_VALIDATION_EVIDENCE_CONTRACT.yaml`
3. Stage 03:
   - UI-related capability contracts
   - Provider Port Schema
   - Version / Status / Provenance Rules
4. Stage 04:
   - Provider Binding Schema
   - Project Overlay / Variable Resolution

## 2. 定点 Legacy / UI 设计能力

只读取与以下能力相关的 evidence：

```text
Design analysis
CSS token extraction
Page visual capture
Image palette extraction
Contrast evaluation
Design document lint
Design token build
Design drift check
Design package export
```

## 3. 定点设计规范

优先读取已登记的这些规范/版本：

```text
UI Design Pack 数据结构与目录规范
UI设计图驱动开发协议
Implementation 产物生成规则
前端 UI 布局开发指导
前端设计图驱动开发与视觉一致性治理方案
```

只读支持当前 Contract 设计所需章节，不整份全文重载。

## 4. Evidence-on-Demand Triggers

```text
DESIGN_SOURCE_AMBIGUITY
SCENE_SCHEMA_GAP
SEMANTIC_CONFIDENCE_GAP
BEHAVIOR_EVIDENCE_GAP
DATA_EVIDENCE_GAP
LAYOUT_INFERENCE_CONFLICT
PROVIDER_PORT_GAP
MISSING_EVIDENCE
```

## 5. 默认禁止

```text
repository rediscovery
full image corpus analysis
all UI docs full reload
Stage 08 governance redesign
frontend implementation
```

## 6. Token 主要花费对象

```text
Normalized Scene
Semantic Tree
Design Truth
Tokens
Behavior/Data Evidence
Confidence/Provenance
Provider Port
Implementation IR input
Visual validation input
```

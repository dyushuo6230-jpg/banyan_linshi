# Stage 03 低 Token 输入索引 v1.0

## 默认读取顺序

1. `Stage_02_to_Stage_03_Gate_Review_v1.0.md`
2. Stage 02 `evidence/NEXT_STAGE_HANDOFF.yaml`
3. `CAPABILITY_MAPPING_WORKBOOK.yaml`
4. `CONTRACT_CHAIN_DESIGN.md`
5. `ARCHITECTURE_DECISION_RECORDS.yaml`
6. `CONFLICT_RISK_REGISTER.yaml`
7. `AI_RUNTIME_COST_GOVERNANCE_DESIGN.md`

## 按需读取

- `CORE_CANDIDATES.yaml`
- `PROJECT_CANDIDATES.yaml`
- `PROVIDER_CANDIDATES.yaml`
- `COMPATIBILITY_CANDIDATES.yaml`
- `ASSET_BOUNDARY_MAP.jsonl`
- `ARTIFACT_BOUNDARY_MAP.jsonl`

## 默认禁止重新读取

- Stage 01 全量 Inventory 原始内容
- 100k+ Repository 路径
- 全量 Git 历史
- 已封存 Stage 00/01 全部 Evidence

除非 Stage 03 出现：

`CONFLICT / LOW_CONFIDENCE / MISSING_EVIDENCE / SCHEMA_COLLISION`

才按 `evidence_refs` 定点回读。

## 目标

Stage 03 消耗 Token 的主要对象应是：

`35 Capability Candidates + Contract/Schema Design`

而不是重新盘点项目。

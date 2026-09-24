# Stage 03：Canonical Contract / Schema / Source Role 冻结

## 1. 本阶段定位

Stage 01 找出“有什么”，Stage 02 形成“候选边界”，Stage 03 才把可以被后续实现依赖的契约与数据结构冻结下来。

本阶段不是重新设计 Banyan，也不是开始迁移。

目标：

```text
Candidate Semantics
→ Validated Contract
→ Canonical Schema
→ Source Role / Authority Rules
→ Frozen Contract Registry
```

## 2. 省 Token 总原则

默认只读：

```text
Stage 02 Gate Review
Stage 03 低Token输入索引
Stage 02 NEXT_STAGE_HANDOFF
CAPABILITY_MAPPING_WORKBOOK
CONTRACT_CHAIN_DESIGN
ARCHITECTURE_DECISION_RECORDS
CONFLICT_RISK_REGISTER
AI_RUNTIME_COST_GOVERNANCE_DESIGN
```

只有出现：

```text
CONFLICT
LOW_CONFIDENCE
MISSING_EVIDENCE
SCHEMA_COLLISION
```

才按照 `evidence_refs` 回读 Stage 01/02 的具体文件。

禁止重新扫描 100k+ Repository 路径。

## 3. 必须冻结什么

### Contract

所有进入后续实现的 Capability 必须至少定义：

```text
contract_id
capability_id
contract_version
inputs
outputs
preconditions
guards
side_effect_policy
failure_semantics
authority
evidence_lineage
extension_points
compatibility_expectation
```

### Source Role

Source Role 描述“这个来源承担什么权威语义”，不是硬编码物理目录。

必须明确：

```text
role_id
semantic_purpose
authority_level
writable_policy
canonicality
freshness_rule
conflict_rule
provenance_required
mapping_strategy
```

### Artifact / Registry

必须定义：

```text
artifact identity
type
status
version
authority/source-role
provenance
references
supersession
immutability
migration lineage
```

## 4. 不允许冻结的东西

本阶段不能冻结：

```text
某项目 docs/project 就是 Core 固定目录
某个 Provider 厂商是唯一实现
某个模型是永久默认模型
具体 Token 百分比阈值
最终 Framework 安装方式
Legacy Migration 执行路径
```

这些属于 Project Mapping、Provider Runtime 或后续 benchmark。

## 5. 35 项能力保护

35 项高价值能力必须全部进入：

```text
FROZEN_CONTRACT
DEFERRED_WITH_OWNER
PROJECT_OVERLAY_CONTRACT
PROVIDER_PORT_CONTRACT
COMPATIBILITY_CONTRACT
```

之一。

不能静默消失。

`DEFERRED_WITH_OWNER` 只允许用于当前证据不足、且不会阻塞 Schema 基础闭环的项，并必须：

```text
reason
owner_stage
blocking_before_activation
evidence_needed
```

## 6. Core 与 Project 的边界

Generic Core Schema 中不得出现：

```text
x_shop_server
项目业务名称
固定项目路径
固定端口
当前项目业务 ID
当前项目 UI 页面
当前项目人员姓名
```

Project-specific 事实必须通过：

```text
Project Overlay
Source Mapping
Profile / Variable
Provider Configuration
```

进入。

## 7. Existing Project Layout Preservation Contract

正式冻结：

```text
EXISTING_PROJECT = PRESERVE_IN_PLACE
BANYAN = DISCOVER + MAP + CLASSIFY/DESIGN
RELAYOUT = EXPLICIT_MIGRATION_ONLY
```

这不是“建议目录”，而是已有项目接入的默认契约。

## 8. AI Runtime Cost Governance

本阶段冻结的是**治理接口**，不是数值阈值：

```text
task_class
execution_mode
budget_policy
model_capability_class
batchability
cacheability
escalation_condition
quality_gate
telemetry_fields
```

不冻结：

```text
具体厂商
具体模型名
固定 token 阈值
固定价格
```

后续通过配置/benchmark 决定。

## 9. 两项 HIGH Conflict

CON-001 / CON-002 不允许被 Stage 03 静默“选一个”。

Stage 03 只冻结：

```text
precedence contract
conflict representation
freshness/source authority rule
activation blocker
owner stage
```

实际业务/项目层裁决仍由对应 Owner Stage 完成。

## 10. 输出

真实执行后至少生成：

```text
CANONICAL_CONTRACT_SCHEMA.yaml
CAPABILITY_CONTRACT_REGISTRY.yaml
SOURCE_ROLE_SCHEMA.yaml
SOURCE_ROLE_REGISTRY.yaml
ARTIFACT_REGISTRY_SCHEMA.yaml
PROVIDER_PORT_SCHEMA.yaml
PROJECT_OVERLAY_SCHEMA.yaml
REFERENCE_INTEGRITY_CONTRACT.yaml
VERSION_STATUS_PROVENANCE_RULES.yaml
BOOTSTRAP_CANONICAL_STATE_CONTRACT.yaml
EXISTING_PROJECT_LAYOUT_PRESERVATION_CONTRACT.yaml
AI_RUNTIME_GOVERNANCE_CONTRACT.yaml
CONTRACT_FREEZE_REGISTER.yaml
CONTRACT_COVERAGE_REPORT.yaml
CONFLICT_CARRYOVER_REGISTER.yaml
ACCEPTANCE_REPORT.md
evidence/**
```

## 11. 完成条件

必须：

```text
35/35 Capability accounted
0 silent capability drop
0 project path hardcoded in Core Schema
0 contract without failure semantics
0 source role without authority rule
0 unowned schema collision
```

并生成 Stage 04 Handoff 后停止。

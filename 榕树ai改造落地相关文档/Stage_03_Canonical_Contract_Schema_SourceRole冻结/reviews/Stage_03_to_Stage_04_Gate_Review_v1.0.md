# Stage 03 → Stage 04 Gate Review v1.0

> Review Basis：Stage 03 Acceptance Report、NEXT_STAGE_HANDOFF、VALIDATION_RESULTS、CONTRACT_FREEZE_REGISTER  
> Stage 03 Run：`stage03-20260920T135702Z`  
> Review Result：**PASS_FOR_IMPLEMENTATION_DESIGN**  
> Stage 04 Execution：**NOT_STARTED / NOT_AUTHORIZED**

---

## 1. 最终结论

```text
Stage 03 = COMPLETED
Stage 03 Acceptance = PASS_CONTRACT_FREEZE
Stage 04 Entry Gate = PASS_FOR_IMPLEMENTATION_DESIGN
Stage 04 Execution = NOT_STARTED
```

Stage 03 已完成 Contract / Schema / Source Role 冻结。

本次冻结的是：

```text
语义契约
Schema
Source Role / Authority
Artifact Registry
Provider Port
Project Overlay
Reference Integrity
Version / Status / Provenance
Bootstrap → Canonical State
Existing Project Layout Preservation
AI Runtime Cost Governance
```

没有冻结：

```text
Runtime implementation
Provider selection
Physical installation layout
Migration execution
具体模型 / 厂商
具体预算阈值
```

---

## 2. 已验证成果

### Capability Coverage

```text
35 / 35 high-value capabilities accounted
21 FROZEN_CONTRACT
2 PROJECT_OVERLAY_CONTRACT
9 PROVIDER_PORT_CONTRACT
3 COMPATIBILITY_CONTRACT
```

### Frozen Surfaces

共 12 个已冻结 Schema / Contract Surface：

```text
CANONICAL_CONTRACT_SCHEMA
CAPABILITY_CONTRACT_REGISTRY
SOURCE_ROLE_SCHEMA
SOURCE_ROLE_REGISTRY
ARTIFACT_REGISTRY_SCHEMA
PROVIDER_PORT_SCHEMA
PROJECT_OVERLAY_SCHEMA
REFERENCE_INTEGRITY_CONTRACT
VERSION_STATUS_PROVENANCE_RULES
BOOTSTRAP_CANONICAL_STATE_CONTRACT
EXISTING_PROJECT_LAYOUT_PRESERVATION_CONTRACT
AI_RUNTIME_GOVERNANCE_CONTRACT
```

### Source / Artifact Coverage

```text
Source Roles = 9
Artifact/Operational Records = 714 / 714
Provider Ports = 35
Project Overlay Records = 35
```

---

## 3. Stage 04 必须消费 Stage 03 Frozen Contract

Stage 04 不允许再以 Stage 02 Candidate 为直接设计依据。

优先消费：

```text
CAPABILITY_CONTRACT_REGISTRY.yaml
CANONICAL_CONTRACT_SCHEMA.yaml
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
CONFLICT_CARRYOVER_REGISTER.yaml
CONTRACT_COVERAGE_REPORT.yaml
NEXT_STAGE_HANDOFF.yaml
```

Stage 04 只在出现：

```text
CONTRACT_AMBIGUITY
MISSING_BINDING
PROJECT_MAPPING_COLLISION
PROVIDER_PORT_GAP
ACTIVATION_BLOCKER
```

时定点回读 Stage 02/01 Evidence。

---

## 4. Stage 04 的职责边界

Stage 04 应进入：

```text
Implementation Design / Project Instance Design / Mapping Design
```

但仍不是全面 Legacy Migration。

Stage 04 重点应该完成：

```text
Project Instance 结构设计
Source Mapping 实现设计
Project Overlay 实现设计
Provider Binding 机制设计
Profile / Variable Resolution 实现设计
Framework / Project Instance 物理边界落地设计
初始化 / 接入模式设计
旧项目接入 / 新项目初始化模式设计
Bootstrap → Canonical `.banyan` 迁移施工设计
```

注意：

Stage 04 可以设计最终 `.banyan` Project Instance 结构，
但是否实际创建/迁移必须由 Stage 04 Pack 明确 Gate 控制。

---

## 5. 必须继承的风险

### R03-PURITY

```text
severity = HIGH
owner = 04 / 19
blocking_before_activation = true
```

21 Core 候选仍缺独立第二项目执行证明。

Stage 04 可以验证：

```text
Core 不依赖当前项目目录
Project Overlay 能承载当前项目差异
Source Mapping 可适配散列项目目录
```

但不能把“当前项目跑通”当成跨项目证明。

### R03-SOURCE

Artifact authorship / rebuildability 可能仍为 UNKNOWN。

禁止：

```text
自动覆盖
自动重新生成 Canonical Artifact
自动删除旧产物
```

### CON-001 / CON-002

继续 OPEN。

Stage 04 不裁决业务 Winner。

### R03-SECRET

13 个本地运行配置继续：

```text
SECRET_METADATA_ONLY
PRESERVE_IN_PLACE
PARTIAL_APPROVED
```

不得读取正文。

---

## 6. Existing Project Layout Preservation Contract

已经在 Stage 03 正式冻结：

```text
EXISTING_PROJECT = PRESERVE_IN_PLACE
BANYAN = DISCOVER + MAP + CLASSIFY/DESIGN
RELAYOUT = EXPLICIT_MIGRATION_ONLY
```

因此 Stage 04 的实现设计必须围绕：

```text
Mapping
Overlay
Profile
Provider Binding
```

展开。

禁止为了“目录整齐”要求当前项目：

```text
搬 docs
搬 tools
搬业务代码
创建统一 project-sources/
```

---

## 7. Stage 04 低 Token 原则

Stage 04 默认只读取：

```text
本 Gate Review
Stage 04 Low-Token Input Index
Stage 03 NEXT_STAGE_HANDOFF
Frozen Contract / Schema surfaces
Stage 03 Contract Coverage / Conflict Carryover
```

不读取：

```text
Stage 01 全量 1026 资产正文
100k+ Repository 路径
全量 Git 历史
Stage 02 全量 Candidate 资料
```

除非 Frozen Contract 无法映射当前 Project Instance。

---

## 8. Stage 04 需要解决的关键设计问题

至少：

```text
1. Framework Distribution 与 Project Instance 的物理边界
2. `.banyan/` Project Instance 最终结构
3. Source Mapping
4. Project Overlay
5. Profile / Variable Resolution
6. Provider Binding
7. Existing Project Adoption
8. New Project Initialization
9. Migration / Bootstrap Canonical Transition
10. Generated / Runtime / Index / Trace 数据归属
11. Banyan Framework 与项目 Canonical Sources 的关系
12. Adapter Output 与真源的关系
```

---

## 9. 不允许遗漏的用户要求

Stage 04 必须继续保护：

```text
docs/ = 项目目录，默认保留
docs/temp = 只读临时/历史交接区
docs/agreements = 当前项目使用，继续保留
tools = 通用开源 Skill 共享候选，不擅自搬
Existing project scattered roots = 原位保留
```

同时：

```text
Banyan Core 中不能写入当前项目业务内容。
```

---

## 10. Stage 04 Entry Gate

结论：

```text
PASS_FOR_IMPLEMENTATION_DESIGN
```

含义：

可以生成 Stage 04 Delivery Pack。

不代表：

```text
Provider 已选择
Migration 已授权
`.banyan` 已允许直接初始化
Legacy 已允许删除
CON-001/002 已解决
跨项目通用性已最终证明
```

---

## 11. Gate Decision

```text
Stage 03 → Stage 04 = PASS_FOR_IMPLEMENTATION_DESIGN
Stage 04 Pack Generation = ALLOWED
Stage 04 Execution = NOT YET AUTHORIZED
```

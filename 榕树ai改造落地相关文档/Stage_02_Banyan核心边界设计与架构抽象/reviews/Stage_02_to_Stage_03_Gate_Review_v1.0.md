# Stage 02 → Stage 03 Gate Review v1.0

> Review Basis：Stage 02 实际验收报告、`CAPABILITY_MAPPING_WORKBOOK.yaml`、`NEXT_STAGE_HANDOFF.yaml`  
> Stage 02 Run：`stage02-20260920T131746Z`  
> Review Result：**PASS_FOR_CONTRACT_DESIGN**  
> Stage 03 Execution：**NOT_STARTED / NOT_AUTHORIZED_BY_STAGE_02**

---

## 1. 最终结论

```text
Stage 02 = COMPLETED
Stage 02 Acceptance = PASS_CANDIDATE_DESIGN
Stage 03 Entry Gate = PASS_FOR_CONTRACT_DESIGN
Stage 03 Execution = NOT_STARTED
```

Stage 02 已完成“候选架构边界设计”，但没有把候选设计误写成最终 Contract、Schema、Provider 选择、Source Role 或物理目录。

Stage 03 的职责不是重新做 Stage 01/02，而是基于已封存候选输入完成 **Schema / Contract / Source Role 的验证与冻结**。

---

## 2. 已验证输入

### Capability / Boundary

```text
Capabilities = 35
Core Candidates = 21
Project Instance Candidates = 2
Provider Candidates = 9
Compatibility Candidates = 3
```

全部 35 项能力均已进入：

```text
Capability → Contract → Provider → Artifact → Runtime
```

候选映射链。

### Asset / Artifact

```text
Mapped Assets = 1026
Generated Artifacts = 425
Operational Artifacts = 289
```

Stage 03 不应重新进行全仓 Discovery，也不应重新生成 Stage 01 Inventory。

---

## 3. Stage 02 明确“尚未冻结”的内容

来自 `CAPABILITY_MAPPING_WORKBOOK.yaml`：

```text
final contract schema
physical layout
runtime implementation
provider selection
source role
migration
```

因此 Stage 03 不得把 Stage 02 的 Candidate 当成已经批准的实现事实。

---

## 4. Stage 03 必须消费的 Stage 02 实际产物

优先读取：

```text
CAPABILITY_MAPPING_WORKBOOK.yaml
CONTRACT_CHAIN_DESIGN.md
CORE_CANDIDATES.yaml
CORE_BOUNDARY_CANDIDATE.md
PROJECT_CANDIDATES.yaml
PROJECT_INSTANCE_CANDIDATE.md
PROVIDER_CANDIDATES.yaml
PROVIDER_CANDIDATE.md
COMPATIBILITY_CANDIDATES.yaml
COMPATIBILITY_LAYER_CANDIDATE.md
ASSET_BOUNDARY_MAP.jsonl
ARTIFACT_BOUNDARY_MAP.jsonl
CONFLICT_RISK_REGISTER.yaml
CONFLICT_RESOLUTION_PLAN.md
ARCHITECTURE_DECISION_RECORDS.yaml
AI_RUNTIME_COST_GOVERNANCE_DESIGN.md
ACCEPTANCE_REPORT.md
```

不要默认重读 1,026 项原始资产正文；除非 Stage 03 对具体 Candidate 需要定点追证。

---

## 5. 风险继承

### HIGH / 必须保留

```text
R02-PURITY-001
R02-SOURCE-002
R02-SECRET-004
CON-001
CON-002
```

其中：

- Core 可移植性目前没有独立第二项目执行证明；
- Source / Provenance 仍需 Stage 03 冻结 Source Role Schema；
- 13 份本地运行配置继续 `SECRET_METADATA_ONLY / PARTIAL_APPROVED`；
- 知情决策规则差异继续由后续 Owner 处理；
- 项目入口/进度陈旧冲突继续保留 Evidence，不允许 Stage 03 静默覆盖。

### MEDIUM

```text
R02-COST-003
R02-LOCAL-005
```

AI Runtime Cost Governance 已有设计，但预算阈值、模型路由阈值仍需后续真实 workload benchmark；本地 Evidence 仍不是独立异机备份。

---

## 6. Existing Project Layout Preservation

继续继承：

```text
EXISTING_PROJECT -> PRESERVE_IN_PLACE
BANYAN -> DISCOVER + MAP + DESIGN
RELAYOUT -> EXPLICIT_MIGRATION_ONLY
```

Stage 03 不得为了冻结 Schema/Source Role：

```text
移动项目目录
统一归并 docs/code/tools
创建 project-sources/
强制创建最终 banyan-framework/
```

物理布局仍属于未冻结项。

---

## 7. 能力保护

`capabilities_preserved = true`

Stage 03：

- 可以规范 Schema；
- 可以收紧 Contract；
- 可以合并“重复实现表达”；
- 不可以删除已经确认有价值的能力；
- 不可以用“暂时不通用”作为删除理由；
- 不可以把 Project-specific overlay 硬塞进 Generic Core。

---

## 8. Stage 03 省 Token 执行策略

Stage 03 默认使用 **Contract-First / Evidence-on-Demand**：

```text
Gate Review
→ NEXT_STAGE_HANDOFF
→ Capability Mapping Workbook
→ Candidate Boundary Files
→ Conflict/Risk Register
→ 对需要冻结的少数条目定点读取原始 Evidence
```

禁止：

```text
重新扫描 100k+ 路径
重新分析 1,026 项资产正文
重新跑 Stage 01 Discovery
重新生成 Stage 02 Candidate Mapping
```

只有出现：

```text
CONFLICT
LOW_CONFIDENCE
MISSING_EVIDENCE
SCHEMA_COLLISION
```

时，才定点回读对应 Evidence。

---

## 9. Stage 03 Entry Gate

结论：

```text
PASS_FOR_CONTRACT_DESIGN
```

含义：

> 可以开始生成 Stage 03 Delivery Pack，并在用户明确执行后进入 Contract / Schema / Source Role 冻结阶段。

它不表示：

```text
Stage 02 Candidate 已全部批准
Runtime 已实现
Provider 已选择
Migration 已执行
Physical Layout 已冻结
```

---

## 10. Stage 03 必须完成后才能交给 Stage 04 的内容

至少应形成：

```text
Canonical Contract Schema
Capability Contract Schema
Artifact / Registry Schema
Source Role Schema
Reference Integrity Contract
Provider Port Schema
Project Overlay Schema
Bootstrap → Canonical State Schema
Version / Status / Provenance Rules
```

并把 35 项能力的 Candidate 映射迁入可验证 Schema，不丢失 Stage 01/02 Evidence Lineage。

---

## 11. Gate Decision

```text
Stage 02 → Stage 03 = PASS_FOR_CONTRACT_DESIGN
Stage 03 Pack Generation = ALLOWED
Stage 03 Runtime/Implementation = NOT YET AUTHORIZED
```

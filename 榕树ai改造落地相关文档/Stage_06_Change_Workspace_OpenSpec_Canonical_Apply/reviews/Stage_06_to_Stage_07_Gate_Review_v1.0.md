# Stage 06 → Stage 07 Gate Review v1.0

> Review Basis：Stage 06 Acceptance Report、VALIDATION_RESULTS、STAGE06_COVERAGE_REPORT、NEXT_STAGE_HANDOFF  
> Stage 06 Run：`stage06-20260920T151243Z`  
> Review Result：**PASS_FOR_STAGE07_REFERENCE_MIGRATION_DESIGN_WITH_INHERITED_BLOCKERS**  
> Stage 07 Execution：**NOT_STARTED / NOT_AUTHORIZED**

---

## 1. 最终结论

```text
Stage 06 = COMPLETED
Stage 06 Acceptance = PASS_CHANGE_WORKSPACE_AND_CANONICAL_APPLY_CONTRACT_FREEZE
Stage 07 Entry Gate = PASS_FOR_STAGE07_REFERENCE_MIGRATION_DESIGN_WITH_INHERITED_BLOCKERS
Stage 07 Execution = NOT_STARTED
```

Stage 06 已冻结 Change Workspace / Provider / Canonical Apply / Reconciliation / Rollback 合同，
但没有实现 Provider Runtime，也没有真实修改 Canonical 文档或 Legacy Workspace。

Stage 07 可以开始“参考项目 v3.1 Legacy / No-Loss Migration 设计与影子演练”。

---

## 2. Stage 06 已验证成果

```text
Generic Change Workspace = Provider-neutral
Provider Port operations = 9 / 9
OpenSpec Binding = DESIGN_ONLY_INACTIVE
Change Lifecycle States = 11 / 11
Artifact Relationship Types = 8 / 8
Parallel Draft Resolution Paths = 5 / 5
Apply Mandatory Gates = 10 / 10
Reconciliation Checks = 9 / 9
V06-01..V06-20 = PASS
Hard Metrics = 7 / 7 all zero
```

OpenSpec 没有被伪造为已激活 Provider。

---

## 3. Stage 07 的正式职责

Stage 07 应以当前参考项目的 v3.1 Legacy 体系作为“参考项目迁移样本”，完成：

```text
Legacy → Banyan Contract Mapping
Legacy Artifact → Source Role / Artifact Role Mapping
Legacy Capability → Frozen Capability Contract Mapping
Legacy Workflow → Stage 05 Workflow Mapping
Legacy Change/OpenSpec-like behavior → Stage 06 Change Workspace Mapping
Legacy Project Variables → Project Instance / Overlay Mapping
Legacy Generated/Operational Artifact → Preserve / Index / Rebuild / Archive Strategy
Reference Integrity Migration Plan
Compatibility Layer Plan
No-Loss Migration Matrix
Shadow / Dry-Run Migration Plan
Rollback / Recovery Plan
Stage 08+ Handoff
```

---

## 4. 本阶段“设计 + 影子演练”，不做真实迁移

默认禁止：

```text
移动现有 docs/project
重写 Legacy Prompt / Rule / Skill
删除旧 AI 资产
执行真实 Canonical Apply
创建并激活正式 .banyan/
切换 writable truth
归档/删除 Legacy Workspace
修改业务代码
```

Stage 07 可以在 `.banyan-refactor/stages/07/...` 下生成：

```text
migration mapping
shadow target model
dry-run apply result
reference migration simulation
compatibility plan
no-loss evidence
```

但这些都不是正式 Project Instance 激活。

---

## 5. No-Loss 是 Stage 07 的最高优先级

No-Loss 不等于“文件都复制一份”。

必须分别验证：

```text
Capability No-Loss
Artifact No-Loss
Reference No-Loss
Status/Version No-Loss
Decision/Workflow No-Loss
Provider Behavior No-Loss
Generated/Operational Evidence No-Loss
Git Identity / Commit Practice No-Loss
UI Governance Capability No-Loss
Handover / Context Recovery No-Loss
```

任何一项无法证明：

```text
MIGRATION_BLOCKED
```

不能用“后面再补”掩盖。

---

## 6. Legacy 资产处理动作必须受控

每个 Legacy 资产/能力必须进入以下动作之一：

```text
PRESERVE_IN_PLACE
MAP_TO_CORE
MAP_TO_PROJECT_INSTANCE
MAP_TO_PROVIDER
MAP_TO_COMPATIBILITY
INDEX_ONLY
DERIVED_REBUILDABLE
KEEP_HISTORICAL
DEFER_WITH_OWNER
```

Stage 07 不允许：

```text
DELETE
RETIRE
REGENERATE_CANONICAL
```

除非已有明确、独立授权和完整 Reference/Lineage 证明。

---

## 7. v3.1 Legacy 兼容原则

参考项目中现有：

```text
G0～G11
PROJECT_STAGE
TBD
知情决策
PRD / DEC / ADR / CR
TRACE_MATRIX
UI Contract / UI_SPEC
Progress / Worklog / Handover
Plain Document
AnyDesign / UI Governance
```

不能因为 Banyan 新模型更通用就直接废弃。

Stage 07 要回答：

```text
保留语义是什么
未来由哪个 Contract 承担
项目层需要什么 Overlay
哪些只是 Compatibility Layer
哪些仍只在 Legacy 中保留
```

---

## 8. OpenSpec / Change Workspace

Stage 06 已确认：

```text
OpenSpec = Provider Binding
Change Workspace = Generic Abstraction
```

如果当前参考项目没有可验证 Legacy OpenSpec 实例：

```text
不得假造实例
不得编造已迁移状态
```

只能记录：

```text
NOT_OBSERVED / DESIGN_ONLY / DEFERRED_VALIDATION
```

---

## 9. Reference Integrity

任何 Legacy Canonical Artifact 必须保留：

```text
stable identity
version
status
references
supersession
provenance
source role
```

影子迁移必须能追溯：

```text
legacy source
→ mapping
→ target semantic object
→ validation result
```

---

## 10. CON-002

继续继承：

```text
CON-002 = OPEN
Owner = Stage 12
```

Stage 07 可以登记 Freshness 风险和迁移影响，
但不能替 Stage 12 决定最终 Source Freshness 策略。

---

## 11. Low-Token 原则

默认只读取：

```text
本 Gate Review
Stage 07 Low-Token Input Index
Stage 06 Handoff / Apply Contracts
Stage 05 Workflow/Decision Contracts
Stage 04 Project Instance / Mapping / Overlay
Stage 03 Source Role / Artifact / Reference schemas
Stage 01 No-Loss matrices and inventories（按映射索引，不全量正文）
```

禁止：

```text
重新扫描 100k+ paths
重跑 Git history
重新分析 1026 Assets 正文
重新定义 35 Capability
```

---

## 12. 继承风险

```text
R03-PURITY
R03-SOURCE
CON-002
R03-COST
R03-SECRET
R03-LOCAL
```

13 Secret：

```text
SECRET_METADATA_ONLY
PARTIAL_APPROVED
```

---

## 13. Gate Decision

```text
Stage 06 → Stage 07 = PASS_FOR_STAGE07_REFERENCE_MIGRATION_DESIGN_WITH_INHERITED_BLOCKERS
Stage 07 Pack Generation = ALLOWED
Stage 07 Execution = NOT YET AUTHORIZED
```

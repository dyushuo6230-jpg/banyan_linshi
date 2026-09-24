# Stage 07：Reference Project v3.1 Legacy / No-Loss Migration

## 1. 定位

本阶段把当前参考项目既有 v3.1 AI 软件工程体系映射到已冻结的 Banyan Contract。

目标不是“换目录”，而是证明：

```text
旧能力不丢
旧 Canonical 不丢
旧引用不丢
旧状态不丢
旧 Workflow 语义不丢
旧 Evidence 不丢
```

## 2. 迁移模型

```text
Legacy Asset / Capability
→ Stage 01 Inventory Identity
→ Stage 03 Contract
→ Stage 04 Project Instance / Source Mapping
→ Stage 05 Workflow / Decision
→ Stage 06 Change Workspace / Apply
→ Stage 07 Migration Disposition
```

## 3. No-Loss 维度

必须分别核验：

```text
Capability
Artifact
Reference
Version / Status
Workflow
Decision
Provider Behavior
Generated Artifact
Operational Evidence
Git Identity / Commit Practice
Context / Handover
UI Governance
```

## 4. 动作枚举

每项只能进入：

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

Stage 07 不执行 DELETE / RETIRE。

## 5. v3.1 Governance

必须保留语义：

```text
G0～G11
PROJECT_STAGE
TBD
知情决策
PRD / DEC / ADR / CR
TRACE_MATRIX
UI Contract
Progress / Worklog / Handover
```

Banyan 可以重新承载这些语义，
但不能因为“新架构更漂亮”就抹掉现有治理事实。

## 6. Compatibility Layer

有些 Legacy 行为不应进入 Generic Core，但仍需继续工作：

```text
Legacy-specific naming
Legacy document projection
Old entry prompts
Editor compatibility shims
Old progress/handover projections
```

这些进入 Compatibility，不等于失败。

## 7. Artifact Migration

Canonical Artifact：

```text
默认 PRESERVE_IN_PLACE + MAP + INDEX
```

Derived Artifact：

```text
只有可证明重建时才标 DERIVED_REBUILDABLE
否则继续 PRESERVE / KEEP_HISTORICAL
```

Operational Record：

```text
保留真实状态，不把 in_progress / stopped / reverted 改写成 success
```

## 8. Shadow Migration

本阶段可以构造：

```text
shadow Project Instance
shadow registry
shadow source mappings
shadow artifact registry
shadow change/workflow relations
```

全部只在 Stage 07 Run Evidence 内。

不得创建正式 `.banyan/`。

## 9. Shadow Apply

可模拟：

```text
Apply Preview
Impact
Reference Check
Reconciliation
Rollback
```

但：

```text
real apply = false
```

## 10. Migration Readiness

最终要回答：

```text
哪些已经可迁移
哪些需要 Compatibility
哪些需要 Provider
哪些被 blocker 阻塞
哪些必须等 Stage 08+ 才处理
```

## 11. 完成后

Stage 08 才进入：

```text
PRD × UI_SPEC governance
```

Stage 07 不修改产品治理真源。

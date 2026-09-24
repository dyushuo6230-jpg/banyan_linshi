# Stage 07 v1.10 — Codex 正式开始提示词（低 Token / No-Loss）

这是 Stage 07 正式执行，不是重跑 Stage 01～06。

当前阶段：

```text
Stage 07 — Reference Project v3.1 Legacy / No-Loss Migration
```

## 1. 最小读取

先读：

```text
榕树ai改造落地相关文档/Stage_06_Change_Workspace_OpenSpec_Canonical_Apply/reviews/Stage_06_to_Stage_07_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_06_Change_Workspace_OpenSpec_Canonical_Apply/reviews/Stage_07_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_07_Reference_Project_v3.1_Legacy_NoLoss_Migration/
```

然后按低 Token 索引读取 Stage 06 / 05 / 04 / 03 冻结输入与 Stage 01 Inventory/Matrix。

## 2. 不重新盘点

禁止：

```text
全仓 Discovery
100k+ path rescan
Git history full analysis
重新生成 1026 Asset Inventory
重新定义 35 Capability
```

Stage 01 Inventory 是本阶段资产入口。

## 3. 最高优先级：No-Loss

必须证明：

```text
Capability
Canonical Artifact
Operational Artifact
Reference
Version / Status
Workflow / Decision
Provider / Compatibility
Generated Evidence
Context / Handover
UI Governance
```

无损。

出现无法解释 Gap：

```text
MIGRATION_BLOCKED
```

不得伪造 PASS。

## 4. Legacy Action

每项必须归入：

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

禁止默认 DELETE / RETIRE / REGENERATE_CANONICAL。

## 5. Shadow Migration Only

本阶段允许：

```text
Shadow Project Instance
Shadow Registry
Shadow Mapping
Shadow Apply Preview
Shadow Reconciliation
Rollback Simulation
```

全部写在 Stage 07 Run。

禁止：

```text
创建/激活正式 .banyan
切换 writable truth
真实修改 Canonical
移动 Legacy 项目目录
删除 Legacy
```

## 6. v3.1 Governance

必须保留 G0～G11、PROJECT_STAGE、TBD、知情决策、PRD/DEC/ADR/CR、TRACE_MATRIX、UI Contract、Progress/Handover 等语义。

可以映射/兼容，不可静默废弃。

## 7. OpenSpec

若没有可验证 Legacy OpenSpec 实例：

```text
保持 NOT_OBSERVED / DESIGN_ONLY
```

不得编造已迁移状态。

## 8. CON-002

继续 OPEN / Stage 12。

Stage 07 只登记 migration impact。

## 9. Secret

13 Secret 继续：

```text
metadata-only
PARTIAL_APPROVED
```

正文禁止 read/copy/hash/write/delete/move/commit。

## 10. Validation

执行 V07-01～V07-22。

8 个 Hard Metrics 全部必须为 0。

## 11. 写入

仅：

```text
.banyan-refactor/stages/07/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

## 12. 完成

生成：

```text
ACCEPTANCE_REPORT.md
evidence/NEXT_STAGE_HANDOFF.yaml
```

更新 Bootstrap。

Stage 07 完成后停止，不进入 Stage 08。

# Stage 10 v1.10 — Codex 正式开始提示词（低 Token）

这是 Stage 10 正式执行，不是重跑 Stage 01～09。

当前阶段：

```text
Stage 10 — Project Guide / Knowledge Publishing
```

## 1. 最小读取

先读：

```text
榕树ai改造落地相关文档/Stage_09_UI_Design_Intelligence/reviews/Stage_09_to_Stage_10_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_09_UI_Design_Intelligence/reviews/Stage_10_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_10_Project_Guide_Knowledge_Publishing/
```

然后按低 Token 索引定点读取。

## 2. 核心原则

```text
Canonical / Approved Source = Truth
Project Guide / Plain Document / Meeting Pack = Projection
```

Projection 不得成为第二套需求或架构真源。

## 3. 必须冻结

```text
Knowledge Source Authority
Knowledge Projection
Project Guide
Audience Views
Navigation
Freshness
Rebuildability
Generated Knowledge Provenance
Plain Document Compatibility
Progress / Worklog
Handover / Context
Architecture Diagram Projection
Meeting / Discussion Pack
Publish Lifecycle
Knowledge Provider Port
Stage11 Index Requirements
```

## 4. Plain Document

必须保留：

```text
单向同步
不是第二套需求
按批刷新
冲突记账
```

Generic Core 不绑定当前中文目录结构。

## 5. Freshness / Rebuildability

任何 stale projection 不得声称 CURRENT。

任何 `NOT_PROVEN_REBUILDABLE` 产物不得自动覆盖式再生成。

## 6. Progress / Handover

必须区分 current / historical / worklog / derived summary。

旧 Progress 不得直接当当前状态。

## 7. Stage11 边界

本阶段不实现 SQLite / Trace / History Runtime。

只输出索引需求。

## 8. Inherited Blockers

真实迁移继续：

```text
MIGRATION_BLOCKED
```

CON-002 / 四条历史缺目标引用 / R03 风险继续保留。

## 9. 禁止

```text
全仓扫描
全文重读 docs/project
全量重读 Plain Document
修改 Canonical 文档
实现 SQLite
创建正式 .banyan
进入 Stage 11
```

## 10. Validation

执行 V10-01～V10-22。

8 项 Hard Metrics 必须全部为 0。

## 11. 写入

仅：

```text
.banyan-refactor/stages/10/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

完成 Acceptance + Handoff 后停止。

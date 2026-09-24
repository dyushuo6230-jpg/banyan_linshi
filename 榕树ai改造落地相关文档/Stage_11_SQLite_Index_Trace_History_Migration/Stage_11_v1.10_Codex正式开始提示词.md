# Stage 11 v1.10 — Codex 正式开始提示词（Structured Input / Low Token）

这是 Stage 11 正式执行，不是重跑 Stage 01～10。

当前阶段：

```text
Stage 11 — SQLite Index / Trace / History Migration
```

## 1. 最小读取

先读：

```text
榕树ai改造落地相关文档/Stage_10_Project_Guide_Knowledge_Publishing/reviews/Stage_10_to_Stage_11_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_10_Project_Guide_Knowledge_Publishing/reviews/Stage_11_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_11_SQLite_Index_Trace_History_Migration/
```

然后严格按 Low Token Index 读取结构化上游产物。

## 2. 本阶段允许真实构建 Shadow SQLite

允许：

```text
.banyan-refactor/stages/11/${RUN_ID}/shadow/banyan_index.sqlite
```

但它必须标记：

```text
SHADOW
REBUILDABLE
NOT_CANONICAL_TRUTH
NOT_FINAL_RUNTIME_DB
```

严禁创建正式 `.banyan/`。

## 3. 核心原则

```text
Canonical Source = Truth
SQLite = Rebuildable Index
Trace = Evidence
History = Historical View
```

禁止数据库反向覆盖 Canonical。

## 4. Structured Input First

优先从：

```text
Registry
Matrix
Coverage Report
Handoff
Bootstrap Register/Trace
```

导入。

禁止：

```text
全仓扫描
Git 全历史重分析
1026 asset body reload
425 artifact body reload
289 operational body reload
```

只有出现明确字段缺口才 Evidence-on-Demand。

## 5. 4 条历史缺目标引用

必须：

```text
status = UNRESOLVED_REFERENCE
target = UNKNOWN / NULL
owner = Stage 12
```

不得猜目标。

## 6. 2 条正则字面量

必须保持：

```text
NOT_A_REFERENCE
```

不得重新计入 unresolved。

## 7. History

failed / stopped / reverted / blocked 等真实状态必须保留。

不得归一化成 success。

## 8. Trace

Trace 不授权动作。

actor identity 不可用时使用 UNKNOWN，不猜。

## 9. Secret

13 个 Secret 只允许 metadata。

不得读/hash/copy/index body 或 derived secret value。

## 10. CON-002

继续 OPEN，Owner Stage 12。

Stage 11 只提供 freshness/history/query evidence。

## 11. Validation

执行 V11-01～V11-24。

9 项 Hard Metrics 必须全部为 0。

必须实际验证：

```text
SQLite schema init
structured import
reference counts
query suite
isolated rebuildability
```

## 12. 写入

仅：

```text
.banyan-refactor/stages/11/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

禁止业务/Canonical/Legacy 写入。

## 13. 完成

生成：

```text
ACCEPTANCE_REPORT.md
evidence/NEXT_STAGE_HANDOFF.yaml
STAGE12_QUERY_SURFACE.yaml
REBUILDABILITY_REPORT.yaml
```

更新 Bootstrap。

完成 Stage 11 后停止，不进入 Stage 12。

# 文档进度

| 字段 | 值 |
|---|---|
| 文档名称 | 文档进度 |
| 文档编号 | DOC-G4-DOC-PROG |
| 版本 | 0.21.0 |
| 状态 | Draft |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-19 |

资料已冻结（BATCH-001 + BATCH-002）。正式 UI_SPEC 仅源品分闸（UI-DEC-001）。2026-09-19 第 29 节已批准 `gongyi_online` UI_SPEC 0.1.5 **Approved Partial**（含附近列表；**不是** Baselined，**仍不计文档进度分母**）。底栏/首页/分类已点名换皮。附近换皮/32A 须另开口令。Contract **0.1.5**。其它应用关闭。视觉修复循环可选、不计分母。G5：上一基线 v0.1.29 Baselined 只读；上一批准包 v0.1.30 Approved 只读；上一业务真源 **v0.1.43 Approved** 只读；当前业务真源 **v0.1.44 Approved**（CR-051 / DEC-073）。G5.5 已同步 UI 逻辑范围（不计入本表权重）。G6～G9 已 **Baselined**（ADR-047）。G9.1 目录已生成（ADR-044；不计入本表权重）。G10 批次文档 **Draft**（ADR-045）。治理模板 **v3.1.15**。

状态系数：Not Started=0，Draft=30，In Review=60，Approved=90，Baselined=100。

文档进度 = Σ(权重 × 系数) / Σ(计划权重) = 11790 / 170 = **69%**。

| 文档 | 阶段 | 状态 | 权重 | 系数 | 证据 |
|---|---|---|---|---|---|
| 来源登记 | G1 | Draft | 5 | 30 | SOURCE_REGISTER.md |
| 批次摘要 | G1 | Draft | 3 | 30 | batches/BATCH-001.md、BATCH-002.md |
| 来源盘点 | G2 | Draft | 8 | 30 | baseline/01 |
| 决策基线 | G2 | Draft | 10 | 30 | baseline/02 |
| 版本差异 | G2 | Draft | 6 | 30 | baseline/03 |
| 冲突矩阵 | G2 | Draft | 8 | 30 | baseline/04 |
| 待确认问题 | G2 | Draft | 10 | 30 | baseline/05 |
| 一致性审计 | G2 | Draft | 8 | 30 | baseline/06 |
| 总 PRD | G5 | Approved | 25 | 90 | prd/PRODUCT_PRD.md（v0.1.44 Approved；v0.1.43 Approved 只读） |
| 模块 PRD | G5 | Approved | 15 | 90 | prd/modules/（本版受影响模块 Approved） |
| 追踪矩阵 | G5 | Approved | 5 | 90 | acceptance/TRACE_MATRIX.md |
| 总体架构 | G6 | Baselined | 15 | 100 | architecture/ 五份；ADR-040 |
| 模块边界 | G7 | Baselined | 8 | 100 | architecture/MODULE_BOUNDARIES.md |
| 模块技术设计 | G8 | Baselined | 12 | 100 | 十份 ADR-030～039；整夹 ADR-041 |
| API 契约 | G9 | Baselined | 8 | 100 | api/；ADR-043 |
| 数据模型 | G9 | Baselined | 8 | 100 | database/；ADR-043 |
| 工程规范 | G9 | Baselined | 6 | 100 | standards/；ADR-043；STD-PIN 已补 |
| 开发批次 | G10 | Draft | 10 | 30 | delivery/DEVELOPMENT_BATCHES.md；ADR-045 |
| **合计** | | | **170** | | 加权 11790 |

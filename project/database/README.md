# 数据模型与迁移

| 字段 | 值 |
|---|---|
| 文档名称 | 数据模型与迁移 |
| 文档编号 | DOC-G9-DB |
| 版本 | 0.1.0 |
| 状态 | Baselined |
| 负责人 | TBD |
| 创建日期 | 2026-09-05 |
| 更新时间 | 2026-09-05 |
| 关联来源 | ADR-042 |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | G9-DRAFT=A |
| 适用版本 | 文档体系 v0.1.3 |
| 替代文档 | 无 |

本夹是数据模型唯一真源（G9 **Baselined**，ADR-043；TECH_BASELINE=v0.1.5）。不灌库、不改业务代码。列名未标明 TBD 的现码列可引用。用户池列已由 DEC-045 确认（`user_pool`）。其余新列/并表未确认者标 TBD。

| 文件 | 职责 |
|---|---|
| [DATA_MODEL.md](./DATA_MODEL.md) | 逻辑实体、关系、所有权 |
| [DATA_DICTIONARY.md](./DATA_DICTIONARY.md) | 字段、约束、敏感级别 |
| [MIGRATION_PLAN.md](./MIGRATION_PLAN.md) | 迁移、回滚、存量；改表必须走 `deploy/sql` 可重复增量 |

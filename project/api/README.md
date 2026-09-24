# API 契约

| 字段 | 值 |
|---|---|
| 文档名称 | API 契约 |
| 文档编号 | DOC-G9-API |
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

本夹是 API 契约唯一真源（G9 **Baselined**，ADR-043；TECH_BASELINE=v0.1.5）。不改业务代码。不创建 `app/mall-online`。模块设计只引用本夹。

| 文件 | 职责 |
|---|---|
| [API_OVERVIEW.md](./API_OVERVIEW.md) | 进程、鉴权、本期变更操作 |
| [ERRORS_AND_IDEMPOTENCY.md](./ERRORS_AND_IDEMPOTENCY.md) | 错误码、分页、幂等、兼容 |
| [openapi/openapi.yaml](./openapi/openapi.yaml) | 机器可读规划（本期变更 + 安全方案） |

现码未改接口继续以各进程 `internal/router` 为准，不在本期重录全量路径。

# 前端应用 UI 目录

| 字段 | 值 |
|---|---|
| 文档名称 | 前端应用 UI 目录 |
| 文档编号 | DOC-G0-UI-PROD |
| 版本 | 0.1.0 |
| 状态 | Draft |
| 负责人 | TBD |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-18 |
| 关联来源 | ADR-044、PROJECT_STRUCTURE |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | ADR-044 |
| 适用版本 | 文档体系 v0.1.3 |
| 替代文档 | 无 |

G9.1 已按真实前端创建子目录。映射真源：`../UI_APPLICATION_MAPPING.yaml`。除 `gongyi_online` 外，子目录内 `UI_SPEC.md` 仅为占位。`gongyi_online/UI_SPEC.md` 为 0.1.3 **Approved Partial**。落地覆盖项须另点名 Contract / 32A。

| slug | 仓库路径 | 说明 |
|---|---|---|
| [admin_web](./admin_web/) | `nunu-go-api/app/admin/web` | 平台后台；现码 Element Plus |
| [merchant_web](./merchant_web/) | `nunu-go-api/app/merchant/web` | 租户后台；现码 Element Plus |
| [local_life_miniapp](./local_life_miniapp/) | `go-uni-app` | 众享营销 - 本地生活 |
| [gongyi_online](./gongyi_online/) | `go-uni-app-online` | 众享源品 - 在线商城多端（DEC-008） |
| [onboarding_h5](./onboarding_h5/) | `nunu-go-api/app/h5` | 入驻 H5 |
| [gongyi_h5_host](./gongyi_h5_host/) | `nunu-go-api/app/h5-online/web/dist` | 整包产物进 Go，不是第二套逛买 |

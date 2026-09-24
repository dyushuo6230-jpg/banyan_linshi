# gongyi_h5_host

| 字段 | 值 |
|---|---|
| 文档名称 | 众享源品 - 在线商城 H5 托管产物 UI 应用目录 |
| 文档编号 | UI-APP-gongyi_h5_host |
| 版本 | 0.1.0 |
| 状态 | Mapped |
| 创建日期 | 2026-09-05 |
| 更新时间 | 2026-09-05 |
| 关联来源 | ADR-044、PROJECT_STRUCTURE、ADR-001 |
| 关联决策 | ADR-044 |

- application_id / slug：`gongyi_h5_host`
- repository_path：`nunu-go-api/app/h5-online/web/dist`
- 类型：众享源品 - 在线商城 H5 整包托管产物（进 `h5-online-server` embed）
- 设备：h5
- 逻辑终端：无（不是第二套逛买产品）
- 映射 PRD 模块：M07（仅作为托管落点）
- UI 现状：C 端页面真源是 `gongyi_online`（`go-uni-app-online`）。本目录只登记整包产物路径。本机进程 8036，外网根路径进首页（DEC-049）。
- `UI_SPEC.md`：占位，未启用，不能当验收。

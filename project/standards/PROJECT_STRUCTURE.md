# 项目结构

| 字段 | 值 |
|---|---|
| 文档名称 | 项目结构 |
| 文档编号 | STD-G9-STRUCT |
| 版本 | 0.1.0 |
| 状态 | Baselined |
| 负责人 | TBD |
| 创建日期 | 2026-09-05 |
| 更新时间 | 2026-09-10 |
| 关联来源 | ADR-001、ADR-004、ADR-007、ADR-042、OVERALL_ARCHITECTURE |
| 关联需求 | REQ-066 |
| 关联决策 | G9-DRAFT=A |
| 适用版本 | 文档体系 v0.1.3 |
| 替代文档 | 无 |

本文件是 G9 **Baselined**（ADR-043；TECH_BASELINE=v0.1.5）。G9.1 正式 UI 应用目录已按 ADR-044 生成（只映射，不启用 UI_SPEC）。生产域名见 DEC-049。

**叠加 DEC-049 v1.0.2：** mall-online 本机 **8035**；众享源品 - 在线商城 H5 独立进程 **8036**，整包 embed。

## 1. 仓库

仓库根为 `CURRENT_BASELINE`。本期后端在 `nunu-go-api/`。文档真源在 `docs/project/`。

忽略且不做考虑：`nunu-go-api/mall-uniapp`、仓库根 `admin/`、`uni-app/`、`niucloud`。

## 2. 后端进程（暴露面，不是技术模块）

| application_id | 路径 | 本机端口（现状） | 职责 |
|---|---|---|---|
| admin | `nunu-go-api/app/admin` | 8031 | 平台 API + 配套 `web/` |
| mall | `nunu-go-api/app/mall` | 8032 | 本地生活 C 端 API |
| merchant | `nunu-go-api/app/merchant` | 8033 | 租户后台 API + 配套 `web/` |
| h5 | `nunu-go-api/app/h5` | 8034 | 入驻 H5 静态托管 |
| home | `nunu-go-api/app/home` | 8081 | 保持；mall-online 不得占用 |
| mall-online | `nunu-go-api/app/mall-online` | **8035** | 众享源品 - 在线商城 C 端；按 mall 模板复制；去掉本地生活专用路由（ADR-004） |
| h5-online | `nunu-go-api/app/h5-online` | **8036** | 众享源品 - 在线商城 H5 整包静态进程（`web/dist` embed）；不是 API |

mall-online 配置目录目标：`nunu-go-api/config/mall-online`（`local` / `test` / `prod` + `.yml.example`）。真实 yml 不进 Git。sms/db/redis/upload/storage 沿用 mall 连接。jwt.secret、wechat 独立。

单进程内部沿用现码：`cmd/server`、`internal/{handler,service,repository,router,middleware}`、`api/v1`。不抽本期公共 internal 包（ADR-004）。共有模型在 `nunu-go-api/model/`。

## 3. 前端应用交付单元

只登记真实存在的前端。不预建虚构的 `admin` / `miniapp` slug。

| application_id | application_slug | repository_path | 类型 | 设备 |
|---|---|---|---|---|
| admin_web | admin_web | `nunu-go-api/app/admin/web` | 平台后台 SPA | desktop |
| merchant_web | merchant_web | `nunu-go-api/app/merchant/web` | 租户后台 SPA | desktop |
| local_life_miniapp | local_life_miniapp | `go-uni-app` | 众享营销 - 本地生活 | miniapp |
| gongyi_online | gongyi_online | `go-uni-app-online` | 众享源品 - 在线商城多端 | ios / android / harmony / miniapp / h5 |
| onboarding_h5 | onboarding_h5 | `nunu-go-api/app/h5` | 入驻 H5 | h5 |
| gongyi_h5_host | gongyi_h5_host | `nunu-go-api/app/h5-online/web/dist` | 众享源品 - 在线商城 H5 整包产物（进 Go embed） | h5 |

页面口径：众享源品 - 在线商城以 `go-uni-app-online` 为准（DEC-008）。开发代理指向 mall-online **8035**。H5 外网根路径进首页（DEC-049）。

## 4. 文档真源

| 目录 | 真源 |
|---|---|
| `docs/project/prd/` | 业务 |
| `docs/project/architecture/` | 总体架构与模块边界 |
| `docs/project/design/modules/` | 模块设计（只引用 api/database，不复制契约） |
| `docs/project/api/` | API |
| `docs/project/database/` | 数据 |
| `docs/project/standards/` | 本夹 |
| `docs/project/delivery/` | G10 批次（未生成） |

`nunu-go-api/docs` 不作为真源。

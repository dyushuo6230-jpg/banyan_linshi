# UI-DEC-001 仅对众享源品启用正式 UI 规范分闸

| 字段 | 值 |
|---|---|
| 文档名称 | 仅对众享源品启用正式 UI 规范分闸 |
| 文档编号 | UI-DEC-001 |
| 版本 | 1.0.0 |
| 状态 | Approved |
| 负责人 | TBD |
| 创建日期 | 2026-09-18 |
| 更新时间 | 2026-09-18 |
| 关联来源 | v3.1.14 第 23A 节、ADR-044、DEC-008 |
| 关联需求 | 无（不改业务字段/流程） |
| 关联决策 | UI-SPEC-SCOPE-001=A |
| 适用版本 | 治理模板 v3.1.14 |
| 替代文档 | 无。收窄 GOV-003 / G0「全项目跳过 UI_SPEC」对 `gongyi_online` 的适用；不改 DEC-008 页面范围与分类例外 |

- 主题：正式 UI 规范开不开、开给谁
- 选择：方案 A
- 限制条件：总闸 true，分闸仅 `gongyi_online`；其它应用仍关；不生成 UI_SPEC；不改业务代码；Draft 不能当验收；F3/F4 须待批准 UI_SPEC
- 被拒方案：B（保持全关）、C（多应用一起开）
- 知情决策证据：INFORMED_REVIEW → INFORMED_CONFIRMATION（用户回复「确认该决策」）→ DECISION_APPLY

## 已确认规则

1. `ENABLE_UI_SPEC_GENERATION=true`。
2. `UI_SPEC_ENABLED_APPLICATIONS=gongyi_online`。
3. `admin_web`、`merchant_web`、`local_life_miniapp`、`onboarding_h5`、`gongyi_h5_host` 不得走 G9.5，占位 UI_SPEC 不能当验收。
4. 本决策 **不** 生成、不批准 UI_SPEC，**不** 跑 anydesign，**不** 改 `go-uni-app-online`。
5. DEC-008 的页面范围、新页优先、有 PNG 按图还原、分类页例外（DEC-071）仍然有效。DEC-008 第 5 条「正式 UI 规范本期仍关闭」仅对源品收窄为：允许走 G9.5；未经批准的 Draft 仍不能当验收。
6. `UI_CONSTRAINT_MODE` 保持 `NONE`，直到存在 Approved/Baselined 的源品 UI_SPEC。
7. 回滚：总闸改回 false，分闸名单清空。

## 未扩大

- 不把 anydesign 产物标 Approved
- 不给后台 / 本地生活 / 入驻开分闸
- 不启动视觉修复循环（另需点名）

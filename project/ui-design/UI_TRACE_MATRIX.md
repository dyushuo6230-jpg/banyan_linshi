# UI 追踪矩阵

| 字段 | 值 |
|---|---|
| 文档名称 | UI 追踪矩阵 |
| 文档编号 | DOC-G55-UI-TRACE |
| 版本 | 0.1.3 |
| 状态 | Draft |
| 负责人 | TBD |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-19 |
| 关联来源 | UI_SCOPE_MAP、PRODUCT_PRD Approved、ADR-044 |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | DEC-015、ADR-044、UI-DEC-001 |
| 适用版本 | 文档体系 v0.1.3 |
| 替代文档 | 无 |

UI-DEC-001：仅 `gongyi_online` 允许走 G9.5。`UI_SPEC.md` 0.1.5 **Approved Partial**（底栏/首页/分类/附近列表；分类听 `category.vue`；附近听第 4 节 PRD 覆盖）。2026-09-18 已点名换皮底栏/首页/分类。2026-09-19 已点名换皮附近列表。其它应用本期仍跳过。Contract 0.1.5 已对齐。32A 须另开口令。

| PRD 模块 | 逻辑终端 | 应用 | 设备 | UI_SPEC | 批次 | 视觉测试 |
|---|---|---|---|---|---|---|
| M01-business-type | LT-platform-web | admin_web | desktop | 本期跳过 | — | 不适用 |
| M01-business-type | LT-onboarding-h5 | onboarding_h5 | h5 | 本期跳过 | — | 不适用 |
| M02-onboarding | LT-onboarding-h5 | onboarding_h5 | h5 | 本期跳过 | — | 不适用 |
| M02-onboarding | LT-platform-web | admin_web | desktop | 本期跳过 | — | 不适用 |
| M03-merchant-workspace | LT-platform-web | admin_web | desktop | 本期跳过 | — | 不适用 |
| M03-merchant-workspace | LT-merchant-web | merchant_web | desktop | 本期跳过 | — | 不适用 |
| M04-goods | LT-merchant-web | merchant_web | desktop | 本期跳过 | — | 不适用 |
| M04-goods | LT-platform-web | admin_web | desktop | 本期跳过 | — | 不适用 |
| M05-local-life | LT-local-life-miniapp | local_life_miniapp | miniapp | 本期跳过 | — | 不适用 |
| M05-local-life | LT-merchant-web | merchant_web | desktop | 本期跳过 | — | 不适用 |
| M06-group-seckill | LT-merchant-web | merchant_web | desktop | 本期跳过 | — | 不适用 |
| M06-group-seckill | LT-local-life-miniapp | local_life_miniapp | miniapp | 本期跳过 | — | 不适用 |
| M06-group-seckill | LT-platform-web | admin_web | desktop | 本期跳过 | — | 不适用 |
| M07-online-mall | LT-merchant-web | merchant_web | desktop | 本期跳过 | — | 不适用 |
| M07-online-mall | LT-platform-web | admin_web | desktop | 本期跳过 | — | 不适用 |
| M07-online-mall | LT-gongyi-youxuan-c | gongyi_online | ios / android / harmony / miniapp / h5 | Approved Partial 0.1.5（底栏/首页/分类/附近列表已点名换皮） | gongyi_online-partial-001 | 首页已跑；分类左栏两态已跑；附近未跑 32A；Contract 0.1.5 |
| M08-user-pool | LT-local-life-miniapp | local_life_miniapp | miniapp | 本期跳过 | — | 不适用 |
| M08-user-pool | LT-gongyi-youxuan-c | gongyi_online | 多端 | Approved Partial（本范围不含「我的」） | — | 未跑 |
| M08-user-pool | LT-merchant-web | merchant_web | desktop | 本期跳过 | — | 不适用 |
| M09-auth-session | LT-platform-web | admin_web | desktop | 本期跳过 | — | 不适用 |
| M09-auth-session | LT-merchant-web | merchant_web | desktop | 本期跳过 | — | 不适用 |
| M09-auth-session | LT-local-life-miniapp | local_life_miniapp | miniapp | 本期跳过 | — | 不适用 |
| M09-auth-session | LT-gongyi-youxuan-c | gongyi_online | 多端 | Approved Partial（本范围不含登录页） | — | 未跑 |
| M10-order-settlement | LT-gongyi-youxuan-c | gongyi_online | 多端 | Approved Partial（本范围不含订单） | — | 未跑 |
| M10-order-settlement | LT-local-life-miniapp | local_life_miniapp | miniapp | 本期跳过 | — | 不适用 |
| M10-order-settlement | LT-merchant-web | merchant_web | desktop | 本期跳过 | — | 不适用 |
| M10-order-settlement | LT-platform-web | admin_web | desktop | 本期跳过 | — | 不适用 |
| M11-platform-ops | LT-platform-web | admin_web | desktop | 本期跳过 | — | 不适用 |
| M11-platform-ops | LT-gongyi-youxuan-c | gongyi_online | 多端 | Approved Partial（本范围不含运营位细则） | — | 未跑 |
| M12-promoter | LT-platform-web | admin_web | desktop | 本期跳过 | — | 不适用 |
| M12-promoter | LT-merchant-web | merchant_web | desktop | 本期跳过 | — | 不适用 |

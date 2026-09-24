# UI 逻辑范围

| 字段 | 值 |
|---|---|
| 文档名称 | UI 逻辑范围 |
| 文档编号 | DOC-G55-UI-SCOPE |
| 版本 | 0.1.1 |
| 状态 | Draft |
| 负责人 | TBD |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-05 |
| 关联来源 | PRODUCT_PRD v0.1.0 Approved、DEC-015 |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | DEC-001～DEC-015、ADR-044 |
| 适用版本 | 文档体系 v0.1.0 |
| 替代文档 | 无 |

G5.5 根据 Approved PRD 登记逻辑页面终端。不生成正式 UI_SPEC，不虚构颜色、布局、组件和交互。G9.1（ADR-044）已按真实前端填写 slug，并创建 `products/{application_slug}/`。禁止虚构 admin / miniapp slug。

`application_id` / `application_slug` / `repository_path` 已按 `PROJECT_STRUCTURE.md` 回填。`gongyi_h5_host` 无独立逻辑终端。

本期明确不做的页面能力不登记为实现范围：外卖；在线商城拼团秒杀；众享源品 - 在线商城 AI/发现**对接**（页面可留样式、不接业务，DEC-008 / REQ-063）。平台 banner 菜单保留，众享源品 - 在线商城首页读取（DEC-039）。小魔推不纳入本期必验（DEC-010）。

## 逻辑终端（非应用目录）

| 逻辑终端 ID | 显示名称 | 对应 PRD 端 | 目标设备（业务） | application_id | application_slug | repository_path |
|---|---|---|---|---|---|---|
| LT-platform-web | 平台后台 | 平台后台 | Web | admin_web | admin_web | nunu-go-api/app/admin/web |
| LT-merchant-web | 租户后台 | 租户后台（一套系统、四套菜单模板） | Web | merchant_web | merchant_web | nunu-go-api/app/merchant/web |
| LT-onboarding-h5 | 租户入驻 H5 | 租户入驻 H5 | H5 | onboarding_h5 | onboarding_h5 | nunu-go-api/app/h5 |
| LT-local-life-miniapp | 众享营销 - 本地生活 | 众享营销 - 本地生活 | 小程序 | local_life_miniapp | local_life_miniapp | go-uni-app |
| LT-gongyi-youxuan-c | 众享源品 - 在线商城 C 端 | 众享源品 - 在线商城 C 端 | iOS / 安卓 / 鸿蒙 / 小程序 / H5（交付节奏非正式批次） | gongyi_online | gongyi_online | go-uni-app-online |

## 模块 × 逻辑终端

| PRD 模块 | 逻辑终端 | 可选页面范围（只来自 PRD，不编造逐页清单） | 备注 |
|---|---|---|---|
| M01-business-type | LT-platform-web | 业态与经营类目树配置；费率挂节点 | DEC-001、DEC-011、DEC-012 |
| M01-business-type | LT-onboarding-h5 | 入驻时选择业态；在线商城强制 1～3 个启用中的一级 | DEC-032 |
| M02-onboarding | LT-onboarding-h5 | 全业态同一入驻提交；执照沿用现码页 | DEC-032 |
| M02-onboarding | LT-platform-web | 入驻审核 | |
| M03-merchant-workspace | LT-platform-web | 四套菜单模板、同一配置页、隐藏 | 租户已点名项见 DEC-020；平台侧栏见 DEC-031 |
| M03-merchant-workspace | LT-merchant-web | 按业态套模板工作台 | 四套侧栏隐藏小魔推（DEC-019）；租户已点名显示名与轮播入口见 DEC-020 |
| M04-goods | LT-merchant-web | 发品；在线商城树选择器；品牌可选 | DEC-009、DEC-012 |
| M04-goods | LT-platform-web | 在线商城商品审核；品牌库保留 | 类目停用后不可再售（DEC-035）；编辑重审待配置 |
| M05-local-life | LT-local-life-miniapp | 按业态首页；餐饮扫桌；美发/商超核销；不做外卖 | 一次核销 DEC-034；无天数无过期自动退 DEC-037 |
| M05-local-life | LT-merchant-web | 店内分类发品、履约相关后台 | |
| M06-group-seckill | LT-merchant-web | 本地生活拼团秒杀租户发布/上下架 | 停用后不可新参 DEC-038；在线商城无此菜单 |
| M06-group-seckill | LT-local-life-miniapp | 店内可见拼团秒杀 | 平台不审、不建场次 |
| M06-group-seckill | LT-platform-web | 去掉拼团秒杀经营功能；「秒杀管理」「拼团审核」删行 | DEC-031；改库 DEV-008 |
| M07-online-mall | LT-merchant-web | 在线商城供应商发品送审；无独立小程序 | |
| M07-online-mall | LT-platform-web | 在线商城商品审核 | |
| M07-online-mall | LT-gongyi-youxuan-c | 逛买、独立登录；页面以 go-uni-app-online 为准（新页优先） | 进程拆分不在此图；AI/发现不对接 |
| M08-user-pool | LT-local-life-miniapp | 店铺池账号 | DEC-003 |
| M08-user-pool | LT-gongyi-youxuan-c | 众享源品 - 在线商城池独立注册 | |
| M08-user-pool | LT-merchant-web | 租户子账号（权限细节待配置） | |
| M09-auth-session | LT-platform-web | Cookie+CSRF 网页登录 | DEC-005 |
| M09-auth-session | LT-merchant-web | Cookie+CSRF 网页登录 | |
| M09-auth-session | LT-local-life-miniapp | Header；认店只限本端 | |
| M09-auth-session | LT-gongyi-youxuan-c | 独立登录；可作废会话 | 口令复杂度 DEC-062 |
| M10-order-settlement | LT-local-life-miniapp | 支付到租户 | REQ-100 |
| M10-order-settlement | LT-gongyi-youxuan-c | 平台统一支付 | 订单字段沿用现表（DEC-039） |
| M10-order-settlement | LT-merchant-web | 租户侧订单；本地生活结算账单=佣金对账 | DEC-033 |
| M10-order-settlement | LT-platform-web | 订单财务；本地生活佣金勾已收 | DEC-013、DEC-033 |
| M11-platform-ops | LT-platform-web | banner 菜单和表保留；众享源品 - 在线商城首页读取 | DEC-039 |
| M11-platform-ops | LT-gongyi-youxuan-c | 不把平台 banner 当本期 C 端验收 | |
| M12-promoter | LT-platform-web | 现码保留；方案未展开是否本期改造 | 与小魔推 DEC-010 分开 |
| M12-promoter | LT-merchant-web | 现码有入口则保留现状 | 不纳入本期必验除非另定 |

废弃模块：无。

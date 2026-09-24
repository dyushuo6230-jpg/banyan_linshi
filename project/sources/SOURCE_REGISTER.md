# 来源总登记

| 字段 | 值 |
|---|---|
| 文档名称 | 来源总登记 |
| 文档编号 | DOC-G1-SRC-REG |
| 版本 | 0.1.0 |
| 状态 | Draft |
| 负责人 | TBD |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-17 |
| 关联来源 | BATCH-001、BATCH-002（均已冻结）、BATCH-003（变更稿纳入转存，未冻结为第 3 批方案包） |
| 关联需求 | 无 |
| 关联决策 | DEC-001、DEC-002、DEC-003、DEC-004、DEC-005、DEC-006、DEC-007、DEC-008、DEC-009、DEC-010、DEC-011、DEC-012、DEC-013、DEC-014、DEC-015、DEC-016、DEC-017、DEC-018、DEC-019、DEC-020、DEC-021、DEC-026 |
| 适用版本 | 文档体系 v0.0.0 |
| 替代文档 | 无 |

角色说明：

- **现码基底**：回答「现在有什么」，`CURRENT_BASELINE`
- **本期方案**：回答「这期要做成什么」
- **理解用历史参考**：只读，不覆盖现码，也不覆盖本期方案
- **清理候选**：不作为真源

未登记且明确忽略：`nunu-go-api/mall-uniapp`、仓库根目录 `admin/`、`uni-app/`、`niucloud`。

资料范围已于 2026-09-04 冻结 **BATCH-001 + BATCH-002**。**BATCH-003** 为 2026-09-15 变更稿纳入转存的设计源（SRC-UI-003），不删除第 1、2 批。新增资料须走 CR 或新版本，不得删除历史行。落地标准见 DEC-029 v1.3.0（CR-043）。拼团秒杀两种流程见 ADR-011 v1.1。平台运营含板块见 ADR-016 v1.1。

已应用业务决策：`DEC-001`～`DEC-047`。已应用架构决策：`ADR-001`、`ADR-002`、`ADR-003`、`ADR-004`、`ADR-005`、`ADR-006`、`ADR-007`、`ADR-008`、`ADR-009`、`ADR-010`、`ADR-011`、`ADR-012`、`ADR-013`、`ADR-014`、`ADR-015`、`ADR-016`、`ADR-017`、`ADR-018`、`ADR-019`、`ADR-020`、`ADR-021`、`ADR-022`、`ADR-023`、`ADR-024`、`ADR-025`、`ADR-026`、`ADR-027`、`ADR-028`、`ADR-029`、`ADR-030`、`ADR-031`、`ADR-032`、`ADR-033`、`ADR-034`、`ADR-035`、`ADR-036`、`ADR-037`、`ADR-038`、`ADR-039`、`ADR-040`、`ADR-041`、`ADR-042`、`ADR-043`、`ADR-044`、`ADR-045`、`ADR-046`、`ADR-047`、`ADR-048`、`ADR-049`。已应用变更：`CR-001`、`CR-002`、`CR-003`、`CR-004`、`CR-005`、`CR-006`、`CR-007`、`CR-008`、`CR-009`、`CR-010`、`CR-011`、`CR-012`、`CR-013`、`CR-014`、`CR-015`、`CR-016`、`CR-017`、`CR-018`、`CR-019`。冻结本批来源不得改写。SRC-REQ-002/003 落地口径见 DEC-005。页面归纳口径见 DEC-008。品牌口径见 DEC-009。小魔推口径见 DEC-010、DEC-019。无业态老店默认餐饮见 DEC-011。类目与计佣一级同一套见 DEC-012。一级以平台类目为准、经营类目不挂子见 DEC-021（CR-006）。未挂一级不可售见 DEC-013。待审拼团秒杀改未上架见 DEC-014。PRD 已批准见 DEC-015。本地生活普通商品**不审**、只审在线商城见 DEC-026（CR-007；废止 DEC-016 本地生活必审；SRC-REQ-001「只审在线商城」恢复有效）。存量：本期测试可清库见 DEC-017（「已在售视为已通过」不再作为本地生活审核迁移条件）。商品审核批量通过/驳回仅在线商城见 DEC-018（经 DEC-026 收窄）。商户四套菜单显示名与轮播入口见 DEC-020；在线商城内容轮播已删见 DEC-039。剩余侧栏有无见 DEC-027。在线商城店铺资料见 DEC-028。落地标准见 DEC-029 v1.2.0（CR-010）。众享源品 - 在线商城首页读平台 banner 见 DEC-039。mall-online 独立进程见 ADR-001。JWT 独立见 ADR-002。支付/微信独立见 ADR-003。工程模板见 ADR-004。其余主题延期见 ADR-005。G6 Draft 已生成见 ADR-006。技术模块按能力域切见 ADR-007。admin/merchant 只作后台暴露面见 ADR-008。商品一个能力域两种流程见 ADR-009。交易一个能力域两种支付通道见 ADR-049。ToB 营销独立进程见 ADR-010。拼团秒杀独立能力域见 ADR-011。用户与认证会话两个能力域见 ADR-012。业态树与入驻两个能力域见 ADR-013。履约独立能力域见 ADR-014。推广独立能力域且本期只保留现状见 ADR-015。平台运营独立能力域见 ADR-016（C 端改挂以 DEC-039 为准）。十个技术模块稳定 ID 与 PRD 映射见 ADR-017。模块边界 Draft 见 ADR-018。模块边界 Approved 见 ADR-019。G8 先设计 tree 见 ADR-020。G8 下一份 onboarding 见 ADR-021。G8 下一份 goods 见 ADR-022。G8 下一份 trade 见 ADR-023。G8 下一份 fulfillment 见 ADR-024。G8 下一份 group-seckill 见 ADR-025。G8 下一份 auth-session 见 ADR-026。G8 下一份 user 见 ADR-027。G8 下一份 promotion 见 ADR-028。G8 下一份 platform-ops 见 ADR-029。G8 批准 tree 见 ADR-030。G8 批准 onboarding 见 ADR-031。G8 批准 goods 见 ADR-032。G8 批准 trade 见 ADR-033。G8 批准 fulfillment 见 ADR-034。G8 批准 group-seckill 见 ADR-035。G8 批准 auth-session 见 ADR-036。G8 批准 user 见 ADR-037。G8 批准 promotion 见 ADR-038。G8 批准 platform-ops 见 ADR-039。G6 五份架构批准见 ADR-040。G8 整夹批准见 ADR-041。G9 三夹 Draft 见 ADR-042。G9 三夹批准见 ADR-043。G9.1 目录见 ADR-044。G10 批次文档见 ADR-045。终审审计见 ADR-046。交付文档 Baselined 见 ADR-047。开工门禁见 ADR-048。

| 来源编号 | 名称 | 类型 | 路径 | 版本/年代 | 日期 | 范围 | 优先级 | 状态 | 角色 | 摘要 |
|---|---|---|---|---|---|---|---|---|---|---|
| SRC-REQ-001 | 迭代多业态商户入驻系统方案 | 新版需求与技术参考 | docs/project/sources/inbox/BATCH-001/迭代多业态商户入住系统方案.md | 第二次迭代 2026-09 | 2026-09-04 | 本期目标、范围候选、物资索引、待讨论问题 | 最高 | 已登记 | 本期方案 | BATCH-001 投放原文。含多业态目标、明确不做、各端描述、技术建议、知情决策题。不是现码盘点结论。 |
| SRC-REQ-002 | 登录机制与安全改造实施方案 | 新版需求与技术参考 | docs/project/sources/inbox/BATCH-002/登录机制与安全改造实施方案.md | 2026-09-03 方案稿 | 2026-09-04 | 登录/会话/口令原理与现码盘点；范围写 admin/merchant/mall + go-uni-app | 最高 | 已冻结 | 本期方案补充 | 原理与现码盘点。落地口径见 DEC-005（改什么以 SRC-REQ-003 为准）。 |
| SRC-REQ-003 | 登录会话与口令相关全部修改项和修改方案 | 新版需求与技术参考 | docs/project/sources/inbox/BATCH-002/登录会话与口令相关全部修改项和修改方案.md | 2026-09-03 方案稿 | 2026-09-04 | 一期修改项 A1～A17、职责、验收；自称改什么以本文为准 | 最高 | 已冻结 | 本期方案补充 | 改什么与验收以本文为准。已由 DEC-005 确认本期一次落地，并收口众享源品 - 在线商城/认店/Cookie。 |
| SRC-CODE-001 | 平台后台 admin | 代码现状 | nunu-go-api/app/admin | 当前分支 feature/multiple_business_model | 2026-09-04 | 平台 API + web，端口 8031 | 最高 | 已盘点 | 现码基底 | 入驻审核、商户、经营类目、平台类目/品牌、商品审核、订单财务、拼团秒杀审核、轮播、商户菜单（单树、无隐藏、无业态） |
| SRC-CODE-002 | C 端 API mall | 代码现状 | nunu-go-api/app/mall | 当前分支 | 2026-09-04 | 本地生活 C 端 API，端口 8032 | 最高 | 已盘点 | 现码基底 | 登录/点餐/附近/券/支付；含拼团秒杀下单接口；小魔推已迁入 mall。无独立 mall-online |
| SRC-CODE-003 | 商户后台 merchant | 代码现状 | nunu-go-api/app/merchant | 当前分支 | 2026-09-04 | 商家 API + web，端口 8033 | 最高 | 已盘点 | 现码基底 | 一套菜单全店共用。有商品/桌台/装修/拼团秒杀/小魔推。无按业态菜单，无模板市场分业态 |
| SRC-CODE-004 | 本地生活 H5 静态托管 | 代码现状 | nunu-go-api/app/h5 | 当前分支 | 2026-09-04 | 托管 go-uni-app H5 产物，无业务 API | 高 | 已盘点 | 现码基底 | 入驻 H5 / 本地生活 H5 静态站点，接口走 mall |
| SRC-CODE-005 | 在线商城 H5 静态托管 | 代码现状 | nunu-go-api/app/h5-online | 当前分支 | 2026-09-10 | 众享源品 - 在线商城 H5 独立进程 | 高 | **已落地（DEC-049 v1.0.2）** | 现码基底 | 整包 `web/dist` embed；本机 8036；根路径进首页。不是 API。与入驻 `app/h5` 部分 embed 不同 |
| SRC-CODE-006 | 众享营销 - 本地生活 | 代码现状 | go-uni-app | 当前分支 | 2026-09-04 | fang_catering、merchant_site、little_demon_pusher 等 | 最高 | 已盘点 | 现码基底 | 餐饮向点餐/附近/入驻 H5；已含小魔推。无美发/商超首页模板，无完整拼团秒杀 C 端页 |
| SRC-CODE-007 | 众享源品 - 在线商城 / 在线商城前端 | 代码现状 | go-uni-app-online | 当前分支 | 2026-09-10 | shop 等页面；开发代理 8035 | 最高 | 已盘点 | 现码基底 | 页面物资已在。C 端只调 mall-online 8035。H5 `build:h5` / `build:h5:test` 整包拷到 h5-online |
| SRC-CODE-008 | 共享数据模型 | 代码现状 | nunu-go-api/model | 当前分支 | 2026-09-04 | merchant/goods/order/user 等 | 最高 | 已盘点 | 现码基底 | 无业态字段；抽佣在商户；user 按 merchant_id 隔离；goods 有 audit_status；merchant.is_self 仍在 |
| SRC-CODE-009 | home 站点壳 | 代码现状 | nunu-go-api/app/home | 当前分支 | 2026-09-04 | 端口示例 8081 | 低 | 已盘点 | 现码基底 | 小魔推已迁 mall，home 仅站点壳。不是本期 5 个产品端 |
| SRC-UI-001 | 拼团秒杀参考图 | 需求阶段设计图 | docs/temp/TypesBusines/materials/秒杀拼团相关参考图/ | 2026-09 | 2026-09-04 | 列表/首页板块截图 | 中 | 已登记 | 理解用 + 需求归纳 | 物资说明要求推理业务逻辑、不参考 UI 视觉。非正式验收基准 |
| SRC-UI-002 | 在线商城 UI 与开发说明 | 需求阶段设计图/说明 | docs/temp/TypesBusines/materials/在线商城UI页面和开发说明/ | 2026-09-04 文档写 v2.1 | 2026-09-04 | 页面收敛、接口对接、第一阶段说明 | 中 | 已登记 | 理解用 + 需求归纳 | 口径见 DEC-008：页面以 go-uni-app-online 为准；新页优先、旧页补缺。用户确认：方案「在线商城页面说明文档.md」即本目录 `线上商城前端收敛与接口对接需求说明.md`。该说明只对照，不是 PRD，不能批准为 UI_SPEC。 |
| SRC-LEGACY-001 | 多业态方案第一版 | 旧版需求 | docs/temp/迭代多业态商户入住系统方案-第一版.md | 2026-08-31 | 2026-08-31 | 旧盘点、旧菜单、旧期限 | 历史参考 | 已登记 | 理解用历史参考 | 可帮助理解现码。期限划分、旧菜单方案、旧「自营后期」结论不得当已确认需求 |
| SRC-LEGACY-002 | TypesBusines 目录 | 旧资料入口 | docs/temp/TypesBusines/ | 2026-09 | 2026-09-04 | 物资与目录说明 | 历史参考 | 已登记 | 理解用历史参考 | 方案点名的登录两份 md 原路径仍无文件；投放副本在 BATCH-002（SRC-REQ-002/003） |
| SRC-LEGACY-003 | docs/temp 其余历史指导 | 旧资料 | docs/temp/ | 不等 | — | SaaS、装修、入驻、部署、小魔推合并等 | 历史参考 | 已登记 | 理解用历史参考 | 只读理解。不作为维护真源 |
| SRC-LEGACY-004 | nunu-go-api/docs | 脱节文档 | nunu-go-api/docs | 旧 | — | 旧架构/库表/后台说明 | 清理候选 | 已登记 | 清理候选 | 不以它为真源，日后考虑清理 |
| SRC-GAP-001 | 登录机制与安全改造实施方案（原路径） | 方案点名路径 | docs/temp/TypesBusines/登录机制与安全改造实施方案.md | 2026-09-03 | 2026-09-04 | 历史点名 | 高 | **已关闭** | 文件缺口已补 | 真源：SRC-REQ-002。原 temp 路径仍无文件，不要求再拷。 |
| SRC-GAP-002 | 登录会话与口令修改方案（原路径） | 方案点名路径 | docs/temp/TypesBusines/登录会话与口令相关全部修改项和修改方案.md | 2026-09-03 | 2026-09-04 | 历史点名 | 高 | **已关闭** | 文件缺口已补 | 真源：SRC-REQ-003。原 temp 路径仍无文件，不要求再拷。 |
| SRC-GAP-003 | 在线商城页面说明文档.md | 方案点名文件名 | docs/temp/TypesBusines/materials/在线商城UI页面和开发说明/线上商城前端收敛与接口对接需求说明.md | 文档写 v2.1 | 2026-09-04 | 在线商城页面对照 | 中 | **已对应 · 对照参考（DEC-008）** | 理解用 + 需求归纳 | 用户确认该文件名即上述 md（SRC-UI-002 目录内）。DEC-008：只作对照，不升格为 PRD/UI_SPEC；冲突条款不采用。 |
| SRC-GAP-004 | mall-online 服务 | 技术建议 vs 现码 | nunu-go-api/app/mall-online | 当前分支 | 2026-09-10 | 在线商城独立 API | 高 | **已创建（DEV-010 Ready 未合入）** | 技术建议，ADR-001 已批准独立进程 | 本机 **8035**（DEC-049）。测试 API `https://test-shop-online-api-go.gyyx.store`；正式 API `https://shop-online-api-go.zhengdeyunqi.cn`。H5 测试 `https://test-shop-online-h5-go.gyyx.store/`、正式 `https://shop-online-h5-go.zhengdeyunqi.cn/`，本机 h5-online **8036**。go-uni-app-online 开发代理 8035，不得改到 mall 8032 |
| SRC-UI-003 | 在线商城前端页面 UI（19 PNG） | 需求阶段设计图 | docs/project/sources/inbox/BATCH-003/在线商城前端页面UI/ | 2026-09-14 投放 | 2026-09-15 | 源品 C 端有图页 | 中 | 已登记 | 理解用 + 需求归纳 | 变更稿纳入转存。有图页一比一见 DEC-008 v1.2。AI 视频/生图子页本批不做。原文未改写。2026-09-18 起由 `gongyi_online/materials/MATERIALS_MANIFEST.yaml` 引用（不复制）；anydesign Draft 待确认。 |
| SRC-CAT-001 | 平台类目导入定稿 | 灌库底稿 | docs/project/sources/platform-categories/平台类目整理.md | 2026-09-17 定稿 | 2026-09-17 | 众享源品平台类目受控重导 | 高 | **本机已灌入** | 本期方案补充 | DEC-072 裁剪稿。33/469/4831。不是 PRD。京东原文在 docs/temp/类目截图。种子 `04-goods-category-seed.sql`。 |
| SRC-CHANGE-001 | 变更稿袋（BAG-D1～D24） | 变更稿纳入来源 | 原路径 docs/project/changes_temp/（已删；gitignore 仍忽略该目录） | 2026-09-14 | 2026-09-15 | 已确认应用条目 | 最高 | **已纳入完成（袋已删）** | 本期方案补充 | 正式落点 CR-043～047、DEC-068/069、REQ-131～133、DEV-013、BATCH-003。用户 2026-09-15 回复「纳入完成」后删袋。真源以正式 CR/DEC/PRD 为准，不以已删袋为准。 |

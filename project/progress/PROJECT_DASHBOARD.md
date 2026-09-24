# 项目看板

| 字段 | 值 |
|---|---|
| 文档名称 | 项目看板 |
| 文档编号 | DOC-G0-DASH |
| 版本 | 0.73.0 |
| 状态 | Draft |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-18 |
| 关联来源 | G5 PRD 上一基线 v0.1.29；上一批准包 v0.1.30；上一业务真源 v0.1.43 Approved 只读；当前业务真源 v0.1.44 Approved（CR-051 / DEC-073） |
| 适用版本 | 文档体系 v0.1.44 |

进度数据真源：`PROGRESS_REGISTER.yaml`。

## 总览

| 项 | 值 |
|---|---|
| 项目名称 | 多业态租户入驻系统 |
| 当前阶段 | IMPLEMENTATION（DEV-001～002 Ready；DEV-013 In Progress；DEV-014 In Progress） |
| 仓库作用 | CURRENT_BASELINE |
| 允许改业务代码 | true（仅点名批次；DEV-013、DEV-014 已发第 35 节开工口令） |
| 文档进度 | 69% |
| 开发执行进度 | 0%（未合 main 不虚涨） |
| 正式交付完成度 | N/A |
| 测试通过率 | N/A |
| 当前阻塞数 | 0（P0/P1） |
| 当前里程碑 | PRD v0.1.44 Approved。DEV-014 In Progress。不是 Baselined |
| 当前负责人 | TBD |
| 当前分支 | feature/huanpipro |
| 当前 Commit | dc326a30 |
| 当前 PR | 无 |

## 阶段

| 阶段 | 状态 |
|---|---|
| G0 文档初始化 | 已完成 |
| G1 资料投放 | 已完成（冻结范围：BATCH-001 + BATCH-002；BATCH-003 为变更稿转存设计源） |
| G2 来源和决策基线 | Draft（DEC-001～029、ADR-001～048 已应用，P0/P1=0） |
| G3 PRD 准入 | PASS |
| G4 PRD Draft | 已完成（Draft 历史保留） |
| G5 PRD 评审和批准 | **上一基线 Baselined v0.1.29 只读；当前业务真源 Approved v0.1.44（CR-051 / DEC-073）。上一 Approved v0.1.43 只读。不是 Baselined** |
| G5.5 UI 逻辑范围同步 | **已完成**（不生成 UI_SPEC） |
| G6 总体技术架构 | **Baselined**（ADR-040；TECH_BASELINE=v0.1.5；待配置保留） |
| G7 技术模块划分 | **Baselined**（ADR-019） |
| G8 模块详细技术设计 | **Baselined**（ADR-041；十份 ADR-030～039） |
| G9 API、数据和编码规范 | **Baselined**（ADR-043；待配置保留） |
| G9.1 正式 UI 应用目录 | **已生成**（ADR-044；只目录/映射；不启用 UI_SPEC） |
| G10 开发批次 | **Draft**（ADR-045；DEV-013 In Progress；DEV-014 In Progress；无 UI Contract） |
| G9.5 可选 UI 规范 | 源品 UI_SPEC 0.1.5 Approved Partial（含附近列表）；Contract 0.1.5；底栏/首页/分类已点名换皮；附近换皮/32A 须另开口令；未 Baselined |
| G11 开发实施 | 已进入（DEV-001～004 In Progress） |

## P0 / P1

- P0：无
- P1：无

## 已应用决策

- DEC-001：经营类目树 + 四业态 + 抽佣挂节点（QUESTION-001=A）
- DEC-002：一套租户后台 + 四套菜单模板 + 同一配置页（QUESTION-003=A）
- DEC-003：`user` 表分池（众享营销 - 本地生活 vs 众享源品 - 在线商城）（QUESTION-002=A）
- DEC-004：本地生活拼团秒杀租户发布、平台不审（QUESTION-004=A）
- DEC-005：登录安全按 SRC-REQ-003 全部落地并收口众享源品 - 在线商城/认店/Cookie（QUESTION-005=A）
- DEC-006：平台无自营店，`is_self` 退出业务规则（QUESTION-006=A）
- DEC-007：平台 banner 保留菜单和表，不纳入 C 端/众享源品 - 在线商城本期验收（QUESTION-007=A）
- DEC-008：众享源品 - 在线商城页面以 go-uni-app-online 为准；新页优先、旧页补缺；说明只对照（QUESTION-008=A）；v1.2 分类页例外 DEC-071
- DEC-009：品牌库保留，发品可选不强制（QUESTION-009=A）
- DEC-010：小魔推保留现状，不纳入本期必验；v1.1 补写 mall 扫码进店现状，在线商城的顾客端仍禁止（QUESTION-010=A；DOC-36A-1=B）
- DEC-011：无业态老店默认迁餐饮（QUESTION-011=A）
- DEC-012：在线商城类目与计佣一级同一套；树选择器；通用树可改名（QUESTION-012=A）
- DEC-013：未挂一级不可售不可下单（QUESTION-013=A）
- DEC-014：待审拼团秒杀改未上架，不自动开卖（QUESTION-014=A）
- DEC-015：PRD 批准为 Approved，待配置保留（G5-PRD-APPROVE=A）
- ADR-001：新建独立 mall-online 进程；sms/db/redis/upload/storage 沿用 mall；本机 8035；众享源品 - 在线商城 H5 整包进 h5-online 8036（G6-ARCH-001=A；端口/H5 见 DEC-049）
- ADR-002：mall-online 独立 jwt.secret 与作废名单键（G6-ARCH-002=A）
- ADR-003：mall-online 独立 wechat；平台商户号；回调打 mall-online（G6-ARCH-003=A）
- ADR-004：按 mall 模板复制独立工程；去掉本地生活专用路由（G6-ARCH-004=A）
- ADR-005：消息/搜索/监控细则延期 G7～G9；不自动生成 Draft（G6-ARCH-005=A）
- ADR-006：生成五份总体架构 Draft（G6-DRAFT=A）
- ADR-007：技术模块按能力域切；mall / mall-online 只作暴露面；共库不按进程独占表（G7-BOUND-001=A）
- ADR-008：admin / merchant 只作能力域后台暴露面；四套菜单不是四个模块（G7-BOUND-002=A）
- ADR-009：商品为一个能力域、两种流程；审核台不拆（G7-BOUND-003=A）
- ADR-049：交易为一个能力域、两种支付通道（G7-BOUND-004=A；迁自原 ADR-010）
- ADR-010：ToB 营销独立进程 mall-tob / h5-tob（CR-042 / DEC-067）
- ADR-011：拼团秒杀为独立能力域；本期仅本地生活/mall（G7-BOUND-005=A）
- ADR-012：用户与认证会话为两个能力域（G7-BOUND-006=A）
- ADR-013：业态树与入驻为两个能力域；入驻只读树（G7-BOUND-007=A）
- ADR-014：履约为独立能力域；餐饮扫桌、美发/商超核销（G7-BOUND-008=A）
- ADR-015：推广为独立能力域；本期只保留现状、不纳入必验（G7-BOUND-009=A）
- ADR-016：平台运营为独立能力域；本期只保留 banner、不对接 C 端（G7-BOUND-010=A）
- ADR-017：冻结 10 个技术模块稳定 ID 与 PRD 映射（G7-BOUND-011=A）
- ADR-018：生成 `MODULE_BOUNDARIES.md` Draft（G7-DRAFT=A）
- ADR-019：批准 `MODULE_BOUNDARIES.md` 为 Approved，待配置保留，不是 Baselined（G7-APPROVE=A）
- ADR-020：G8 先设计 `tree`；产物 `design/modules/tree.md` 为 Draft（G8-001=A）
- ADR-021：G8 下一份设计 `onboarding`；产物 `design/modules/onboarding.md` 为 Draft；`tree.md` 保持 Draft（G8-002=A）
- ADR-022：G8 下一份设计 `goods`；产物 `design/modules/goods.md` 为 Draft；已有设计保持 Draft（G8-003=A）
- ADR-023：G8 下一份设计 `trade`；产物 `design/modules/trade.md` 为 Draft；已有设计保持 Draft（G8-004=A）
- ADR-024：G8 下一份设计 `fulfillment`；产物 `design/modules/fulfillment.md` 为 Draft；已有设计保持 Draft（G8-005=A）
- ADR-025：G8 下一份设计 `group-seckill`；产物 `design/modules/group-seckill.md` 为 Draft；已有设计保持 Draft（G8-006=A）
- ADR-026：G8 下一份设计 `auth-session`；产物 `design/modules/auth-session.md` 为 Draft；已有设计保持 Draft（G8-007=A）
- ADR-027：G8 下一份设计 `user`；产物 `design/modules/user.md` 为 Draft；已有设计保持 Draft（G8-008=A）
- ADR-028：G8 下一份设计 `promotion`；产物 `design/modules/promotion.md` 为 Draft；已有设计保持 Draft（G8-009=A）
- ADR-029：G8 下一份设计 `platform-ops`；产物 `design/modules/platform-ops.md` 为 Draft；已有设计保持 Draft（G8-010=A）
- ADR-030：批准 `tree.md` 为 Approved；待配置保留；不是 Baselined；其余九份保持 Draft（G8-011=A）
- ADR-031：批准 `onboarding.md` 为 Approved；待配置保留；不是 Baselined；其余八份保持 Draft（G8-012=A）
- ADR-032：批准 `goods.md` 为 Approved；待配置保留；不是 Baselined；其余七份保持 Draft（G8-013=A）
- ADR-033：批准 `trade.md` 为 Approved；待配置保留；不是 Baselined；其余六份保持 Draft（G8-014=A）
- ADR-034：批准 `fulfillment.md` 为 Approved；待配置保留；不是 Baselined；其余五份保持 Draft（G8-015=A）
- ADR-035：批准 `group-seckill.md` 为 Approved；待配置保留；不是 Baselined；其余四份保持 Draft（G8-016=A）
- ADR-036：批准 `auth-session.md` 为 Approved；待配置保留；不是 Baselined（G8-017=A）
- ADR-037：批准 `user.md` 为 Approved；一张表两个池；待配置保留；不是 Baselined（G8-018=A）
- ADR-038：批准 `promotion.md` 为 Approved；本期不改造、不纳入必验；不是 Baselined（G8-019=A）
- ADR-039：批准 `platform-ops.md` 为 Approved；只保留平台 banner、不对接 C 端；不是 Baselined；本批停止（G8-020=A）
- ADR-040：批准 G6 五份总体架构为 Approved；待配置保留；不是 Baselined；不升 G8 整夹；不进入 G9（G6-APPROVE=A）
- ADR-041：批准 G8 整夹为 Approved；待配置保留；不是 Baselined；不进入 G9（G8-FOLDER=A）
- ADR-042：生成 G9 三夹 Draft；待配置保留；不是 Approved；不改代码；不创建 mall-online（G9-DRAFT=A）
- ADR-043：批准 G9 三夹为 Approved；待配置保留；不是 Baselined；不自动开 G10（G9-APPROVE=A）
- ADR-044：生成 G9.1 UI 应用目录与映射；不启用正式 UI_SPEC；不改现有 UI（G9.1-DRAFT=A）
- ADR-045：生成 G10 批次文档 Planned/Draft；知情例外未 Baselined；不改代码（G10-DRAFT=A）
- ADR-046：进入技术文档终审；本窗不盖章（NEXT-GATE=A）
- ADR-047：交付文档 Baselined TECH_BASELINE=v0.1.5；待配置保留；不改代码
- ADR-048：打开改代码；DEV-001 升 Ready；其余批次仍 Planned；不创建 mall-online（CODE-GATE=A）
- DEC-016：本地生活普通商品须平台审核（QUESTION-015=A；**已被 DEC-026 废止该条**；在线商城仍审）
- DEC-017：本期测试可清库（QUESTION-016=A；CR-002；「已在售视为已通过」不再作为审核迁移，DEC-026）
- DEC-018：商品审核台批量通过/驳回；范围经 DEC-026 收窄为仅在线商城（QUESTION-017=A；CR-003）
- DEC-019：四套租户菜单隐藏小魔推；代码与小程序页不拆；以后改造另议（QUESTION-018=A；CR-004）
- DEC-020：租户已点名显示名与有无；轮播按业态拆入口；其余侧栏先复制；平台沿用现码（QUESTION-019=A；CR-005）
- DEC-021 / CR-006：在线商城一级以平台类目为准；经营类目不挂子；已收进 PRD v0.1.6
- DEC-022：物流设置仅在线商城侧栏有；餐饮/美发/商超无（本批结束走 CR）
- DEC-023：第二轮已点名删减（通道用量仅在线商城无；本批结束走 CR）
- DEC-024：财务侧栏跟钱走（本批结束走 CR）
- DEC-025：暂停新编码；先盘主链闭环再开发（PROC-001=A；**已由 DEC-040 解除暂停**）
- DEC-026 / CR-007：两类生意主口径（LOOP-Q0=A）；入驻平台审；本地生活普通商品不审；平台负责在线商城含设置与多支付留口；券按业态拆开；PRD v0.1.7
- DEC-027：剩余侧栏 LOOP-Q1=A（库存/评价/消息/统计四套有；店铺券仅本地生活；OSS/短信仅本地生活；WiFi 四套无；本窗不改库）
- DEC-028：在线商城店铺资料供应商自改；员工/角色本期不做（LOOP-Q2=A）
- DEC-029 / CR-010：必打端含微信小程序；多端条件编译；仅页面前端接口先做打包/申请支付够用；其余功能闭口；PRD v0.1.10
- DEC-031 / CR-012：平台侧栏点名；秒杀/拼团审核删行；补通道用量；其余现码名保留；PRD v0.1.12
- DEC-032 / CR-013：入驻资质沿用现码执照；在线商城强制 1～3 个启用中的一级；PRD v0.1.13
- DEC-033 / CR-014：本地生活佣金只对账、线下核销、禁止假入账；PRD v0.1.14
- DEC-034 / CR-015：美发/商超整单一次核销；过期自动退不写死；PRD v0.1.15
- DEC-035 / CR-016：类目/一级停用后已上架商品不可再售；不改商品行；已下单不改快照；店内分类同样；PRD v0.1.16
- DEC-036：抽回「不问」包，本轮 Q10～Q12 问完；资质文案不再问
- DEC-037 / CR-017：本期不设核销天数；过期自动退不做；PRD v0.1.17
- DEC-038 / CR-018：拼团停用后不可新参；已下单不自动退；PRD v0.1.18
- DEC-039 / CR-019：众享源品 - 在线商城首页读平台 banner；删供应商内容轮播；时区上海；密码/容量/订单字段沿用现码；PRD v0.1.19
- DEC-040：恢复编码；先收口 DEV-002；不创建 mall-online；不改 admin_menu
- DEC-041：本期会撞待配置先问完再开 DEV-003；大面积推倒先问；R8 留 DEV-009
- DEC-042：一组最多 5 题；现码能收口则自决；盘到位；假数据竣工清理
- DEC-043：入驻再提、商品草稿保持驳回/提交回待审、拼团不另出核销码（现码自决）
- DEC-044 / CR-020：R2～R6=A；PRD v0.1.20
- DEC-045：用户分池列 `user_pool`；存量一律店铺池；DEV005-Q1=A
- DEC-049：mall-online 本机 8035；测试一律 `.gyyx.store`、正式一律 `.zhengdeyunqi.cn`；众享源品 - 在线商城 H5 独立进程 8036、整包 embed、根路径进首页（不进 PRD；v1.0.2）
- DEC-052 / CR-027：订单无 40；确认收货即 50；售后仅 20/30；PRD v0.1.28
- DEC-053 / CR-028：协议分业态；推荐双轨；地址复用；众享源品 - 在线商城 C 端本轮能力收口；PRD v0.1.29
- DEC-054 / CR-029：订单展示对齐（后台书面语、平台只读售后、人看元、C 端口语与入口）；已收进 PRD v0.1.30
- DEC-055 / CR-030：在线商城发品必须挂叶子；筛祖先含子孙；计佣仍取一级；已收进 PRD v0.1.30
- DEC-056：PRD v0.1.30 整包一次批准为 Approved；不是 Baselined；不开工
- DEC-057 / CR-031：OPEN-01/02=A 部分退与退货物流仍不进本期；OPEN-03=A 美发/商超 C 端待核销；OPEN-04=B 真评价含在线商城顾客端商品详情；OPEN-05=B 人手批量改挂；PRD v0.1.31 Draft
- DEC-058 / CR-032：OPEN-06～09=A 真扣款/新地址表/类目名单/根费率死数字仍不冻结；空或 0 不抽佣；未挂一级仍不可售；已收进 PRD v0.1.32
- DEC-059：PRD v0.1.32 整包一次批准为 Approved；不是 Baselined；不开工
- DEC-060 / CR-034：超时未付打开列表/详情或去支付立刻关成 60；定时仍留
- DEC-061 / CR-034：本地生活现用订单与众享源品未付页要有倒计时、到点不能去支付；挂当前实施不新开 DEV（UX-D3=A）
- DEC-010 v1.1 / CR-035：DOC-36A-1=B 补写本地生活扫码进店现状；仍不改造、不加必验；在线商城的顾客端不应有此入口
- CR-036：人话统一为租户 / 租户后台 / 在线商城的顾客端；不改业务规则；PRD v0.1.34
- DEC-062 / CR-037：PWD-001=A 口令复杂度后台严、顾客端中等；设密处写明该端规则；废止 DEC-039 第 5 条；PRD v0.1.35；本窗不改代码
- DEC-063 / CR-038：PWD-002=A 存量后台下次登录强制改密，不交总清单；顾客端不批量改；PRD v0.1.36；本窗不改代码
- DEC-064 / CR-039：ADM-001=A 平台超管登录名改为 ZadminDister；各端登录页不写死账号密码；该号仍走强制改密；PRD v0.1.37；本窗不改代码
- DEC-065 / CR-040：SUP-001=A 平台超管只属于 ZadminDister；那四项别人勾不上；PRD v0.1.38；本窗不改代码
- DEC-066 / CR-041：AFL-001=A 登录与密钥框声明不要浏览器自动填；不承诺 Chrome 对登录框 100% 不填；PRD v0.1.39；本窗不改代码
- CR-043～047 / DEC-068 / DEC-069：变更稿纳入并整包批准 PRD v0.1.41 Approved（吸收 CR-042）。DEV-013 已按第 35 节开工。不是 Baselined
- DEC-070 / CR-048：本地生活拼团秒杀店自发重写。2026-09-16 `PRD_APPROVAL=v0.1.42`。不是 Baselined。
- DEC-071 / CR-049：源品商品分类页去掉甄选上新、平台类目多模块定位。2026-09-17 `PRD_APPROVAL=v0.1.43`。分类页已按本条改。不是 Baselined。
- DEC-072 / CR-050：平台类目受控重导。定稿已确认并灌入本机 shop（33/469/4831）。三级图本机已抠传 OSS（4517/4831）。测试/正式未灌。不是 Baselined。
- DEC-073 / CR-051：本地生活店资料先置。2026-09-17 `PRD_APPROVAL=v0.1.44`。DEV-014 In Progress。不结束 DEV-013。不是 Baselined。

## 下一步

**DEV-014 已开工。** 本袋结束前走第 36A 节。不结束 DEV-013。DEC-072 本机类目已灌；测试/正式仍须另发口令。

- 本轮源品仍不真扣款。本地生活活动单支付到该店账户。板块三表不进 PRD。
- 盖章基线仍是 v0.1.29。改已确认规则须走 CR。

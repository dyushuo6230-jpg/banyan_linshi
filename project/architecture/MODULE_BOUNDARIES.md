# 模块边界

| 字段 | 值 |
|---|---|
| 文档名称 | 模块边界 |
| 文档编号 | ARCH-G7-BOUND |
| 版本 | 1.0.0 |
| 状态 | Baselined |
| 负责人 | TBD |
| 创建日期 | 2026-09-05 |
| 更新时间 | 2026-09-10 |
| 关联来源 | PRODUCT_PRD Approved、ADR-001～040 |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | ADR-007～ADR-019、DEC-001～DEC-018 |
| 适用版本 | 文档体系 v0.1.3 |
| 替代文档 | 无 |

本文件是 G7 **Baselined**（ADR-019；TECH_BASELINE=v0.1.5）。切法与稳定 ID 见 ADR-007～017。总体架构见 `OVERALL_ARCHITECTURE.md`（G6 **Baselined**，ADR-040）。待配置与延期项不得编造。

**叠加 DEC-049 v1.0.2：** mall-online 本机 **8035** 已建；众享源品 - 在线商城 H5 独立进程 **8036**、整包 embed、根路径进首页。盖章正文「不创建 mall-online」是开工前口径，已被 DEV-010 / DEC-049 覆盖。

## 1. 原则

- 技术模块按**能力域**切。模块 ID ≠ 进程名（ADR-007）。
- admin / merchant / mall / mall-online 只作**暴露面**（ADR-007、ADR-008）。
- 数据共库，不按进程独占表。
- 不按页面数量或数据库表机械拆分。
- 消息、任务、通知、搜索、监控容灾 **TBD**（ADR-005），**不**列入本期技术模块。

## 2. PRD 业务模块

| PRD | 名称 | 优先级 | 说明 |
|---|---|---|---|
| M01 | 业态、经营类目与抽佣挂靠 | P0 | DEC-001；老店默认餐饮 DEC-011 |
| M02 | 租户入驻与审核 | P0 | 同一套入驻 H5 |
| M03 | 租户后台、菜单与权限 | P0 | 一套后台、四套菜单；**不是**技术模块 |
| M04 | 商品、类目与审核 | P0 | 两种发品流程；同一审核台 DEC-018 |
| M05 | 众享营销 - 本地生活与履约 | P0 | 扫桌/核销；认店与支付不在本 PRD 独占 |
| M06 | 本地生活拼团秒杀 | P0 | 平台不审 DEC-004 |
| M07 | 众享源品 - 在线商城与在线商城供应商 | P0 | mall-online 暴露面；**不是**技术模块 |
| M08 | 用户账号与用户池 | P0 | 共表分池 DEC-003 |
| M09 | 登录、会话与口令 | P0 | DEC-005 |
| M10 | 订单、支付与结算 | P0 | 两种支付通道 |
| M11 | 平台运营与待配置项 | P2 | banner DEC-007；小魔推已映射到 `promotion` |
| M12 | 推广员 | P2 | 现码保留 |

## 3. 技术模块与稳定 ID

| 稳定 ID | 中文 | 依据 |
|---|---|---|
| `tree` | 业态与经营类目树 | ADR-013 |
| `onboarding` | 入驻 | ADR-013 |
| `goods` | 商品 | ADR-009 |
| `group-seckill` | 拼团秒杀 | ADR-011 |
| `fulfillment` | 履约 | ADR-014 |
| `trade` | 交易 | ADR-049 |
| `user` | 用户 | ADR-012 |
| `auth-session` | 认证会话 | ADR-012 |
| `promotion` | 推广 | ADR-015 |
| `platform-ops` | 平台运营 | ADR-016 |

**不是**技术模块：admin、merchant、mall、mall-online、h5、h5-online、M03、M07。

## 4. 职责与非职责

| ID | 职责 | 非职责 |
|---|---|---|
| `tree` | 四业态根、一棵经营类目树、节点费率配置；平台维护 | 不审店、不发品、不下单；租户不改树；抽佣快照不在本域 |
| `onboarding` | 同一套入驻 H5、按业态采集、平台审店、过审绑定业态/可售一级 | 不拥有树；不配置四套菜单；不签发登录票 |
| `goods` | 两种发品流程；品牌库附属；同一审核台可混勾批量审 | 不拆两个商品模块；不拆独立审核模块；不管支付 |
| `group-seckill` | 本地生活活动生命周期；租户自发、平台不审 | 不并入商品或交易；mall-online 不暴露；成交走 `trade` |
| `fulfillment` | 餐饮扫桌；美发/商超核销 | 不并入交易；本期餐饮不走核销码；不做外卖；mall-online 不暴露 |
| `trade` | 下单、支付、抽佣快照、结算；两种支付通道 | 不拆订单/支付；不按业态拆两套订单；不跨进程分布式事务 |
| `user` | 注册、共表分池、池内唯一、启用/禁用 | 不签发票、不作废会话；不按进程拆两套用户表 |
| `auth-session` | 口令、登录、可作废会话、Cookie+CSRF、Header 票、认店 | 不拥有用户主数据；票不得跨 mall / mall-online；认店不套众享源品 - 在线商城 |
| `promotion` | 推广员入驻注入 + 小魔推现码；本期保留 | 不改造、不纳入必验、不拥有审店；mall-online 不新做小魔推 |
| `platform-ops` | 平台 `banner` 表与轮播管理现码 | 众享源品 - 在线商城首页可读（DEC-039）；本地生活不读；不拥有审店/审品/树/菜单/财务/小魔推；三套 banner 不混 |

## 5. PRD 到技术模块映射

| PRD | 技术模块 | 说明 |
|---|---|---|
| M01 | `tree` | 抽佣**快照**在 `trade` |
| M02 | `onboarding` | 只读 `tree` |
| M03 | 无 | merchant 暴露面；菜单模板按业态套（ADR-008、DEC-002） |
| M04 | `goods` | 品牌附属本域（DEC-009） |
| M05 | `fulfillment` + mall 暴露面 | 认店 → `auth-session`；付钱 → `trade` |
| M06 | `group-seckill` | 成交 → `trade` |
| M07 | 无 | mall-online 暴露面；读 `goods` / `user` / `trade` |
| M08 | `user` | |
| M09 | `auth-session` | |
| M10 | `trade` | |
| M11 | `platform-ops` | 小魔推在 `promotion` |
| M12 | `promotion` | |

## 6. 暴露面（进程，不是模块）

| 进程 | 暴露的能力域 | 不暴露 |
|---|---|---|
| admin :8031 | `tree`、`onboarding`（审店）、`goods`（审品）、`trade`（财务）、`platform-ops`；菜单模板配置 | 不经营拼团秒杀场次；banner 不进 C 端验收 |
| merchant :8033 | `goods`、`fulfillment`、`group-seckill`、`trade`（店订单）、`promotion`（现码） | 不是四个技术模块；在线商城菜单不露拼团秒杀 |
| mall :8032 | `fulfillment`、`trade`（店账户）、`auth-session`（店铺池）、`user`（店铺池）、`group-seckill` C 端、`promotion` 现码 | 不服务众享源品 - 在线商城；不作废 mall-online 票 |
| mall-online :8035 | `trade`（平台商户号）、`auth-session`（众享源品 - 在线商城池）、`user`（众享源品 - 在线商城池）、`goods`（众享源品 - 在线商城可见集） | 扫桌、认店、店支付、本地生活拼团秒杀 C 端、小魔推新做 |
| h5 :8034 | 入驻 H5 静态；部分文件 embed；属 `onboarding` 页面 | 不是 API 进程 |
| h5-online :8036 | 众享源品 - 在线商城 H5 整包 embed；根路径进首页 | 不是 API 进程 |

## 7. 数据所有权

权威写入在能力域；进程只是暴露面。共库。表结构留 G8/G9，本文不冻结列名。

| 数据 | 权威写入 | 读取 |
|---|---|---|
| 业态 / 类目树 / 节点费率 | `tree`（admin） | `onboarding`、`goods`、`trade`（下单时快照） |
| 入驻申请与审店记录 | `onboarding` | 各端读租户业态绑定 |
| 菜单模板绑定 | 平台配置 + 租户维护；属 merchant 暴露面，不是独立模块 | merchant |
| 商品与审核状态 | `goods` | mall / mall-online 各读本端可见集 |
| 拼团秒杀活动 | `group-seckill` | mall、本地生活租户后台 |
| 扫桌 / 核销状态 | `fulfillment` | mall、本地生活租户后台 |
| 用户主数据 | `user`（共表分池） | 本池各端 |
| 会话 / 作废名单 | `auth-session`（按进程隔离键） | 本端鉴权 |
| 订单 / 支付 / 费率快照 / 结算 | `trade`（订单落在拥有该单的进程） | 租户后台、平台财务 |
| 平台 banner | `platform-ops` | 众享源品 - 在线商城首页读取（DEC-039）；本地生活不读 |
| 推广员注入 / 小魔推现码 | `promotion` | 现码入口 |

店铺 `merchant_banner`、周边 `nearby_banner` **不属于** `platform-ops`。

## 8. 依赖方向

允许读下游；禁止反向拥有。进程间 **无**同步 RPC，不共享 JWT（ADR-002）。

```text
tree          <--- 只读 --- onboarding
tree          <--- 只读 --- goods（在线商城挂一级）
tree          <--- 下单快照 --- trade
goods         <--- 可售校验 --- trade
goods         <--- 活动引用 --- group-seckill
group-seckill --- 成交 ---> trade
user          <--- 签发对象 --- auth-session
user          <--- 下单买家 --- trade
auth-session  --- 认店 ---> 仅 mall / 本地生活
trade         --- 已支付 ---> fulfillment（到店）
onboarding    <--- 现码注入 --- promotion（不拥有审店）
platform-ops  独立；C 端不依赖
```

`onboarding` 不得写 `tree`。`fulfillment` 不得写支付结果。`promotion` 不得改入驻审核状态机。

## 9. 事务与一致性

| 边界 | 口径 |
|---|---|
| 下单 + 支付 + 费率快照 | 落在**拥有该订单的进程**内（mall 或 mall-online）；不新增跨进程分布式事务（ADR-007、ADR-049） |
| 本地生活 vs 众享源品 - 在线商城订单 | 两套通道、两套回调域名；失败互不影响被动下线 |
| 审品 / 审店 | 与支付不在同一事务；过审后才可售（DEC-016） |
| 未挂一级 | 不可售、不可下单；不得用缺省费率或 0 抽佣放行（DEC-013） |
| 退出 / 改密 | 只作废**本端**会话（ADR-012、ADR-002） |
| 拼团秒杀成交 | 活动状态在 `group-seckill`；资金在 `trade` |
| 幂等 / 补偿 | 支付回调按现码通道；细则留 G8。不在本文发明队列 |

## 10. 测试、发布、回滚

| 边界 | 口径 |
|---|---|
| 测试 | 按能力域测；不以完整小魔推、平台 banner C 端展示为多业态必验 |
| 发布 | mall-online 与 h5-online 可独立进程发布；失败时 mall 不被动下线（ADR-001、DEC-049） |
| 回滚 | 停 mall-online 或 h5-online，不要求与 mall 同发。灰度细则 **TBD**（ADR-005） |
| 迁移 | 无业态老店默认迁餐饮（DEC-011）；待审拼团秒杀改未上架（DEC-014）；本期测试可清库、上线已在售视为已通过（DEC-017）。**不批准生产清库** |
| 安全验收 | 忙不踢、闲必踢、闸立刻废、串不了店、库无明文密码（REQ-080～091） |

## 11. G8 技术设计文档清单

| 模块 ID | 计划路径 | 状态 |
|---|---|---|
| `tree` | `docs/project/design/modules/tree.md` | **Baselined**（ADR-030） |
| `onboarding` | `docs/project/design/modules/onboarding.md` | **Baselined**（ADR-031） |
| `goods` | `docs/project/design/modules/goods.md` | **Baselined**（ADR-032） |
| `group-seckill` | `docs/project/design/modules/group-seckill.md` | **Baselined**（ADR-035） |
| `fulfillment` | `docs/project/design/modules/fulfillment.md` | **Baselined**（ADR-034） |
| `trade` | `docs/project/design/modules/trade.md` | **Baselined**（ADR-033） |
| `user` | `docs/project/design/modules/user.md` | **Baselined**（ADR-037） |
| `auth-session` | `docs/project/design/modules/auth-session.md` | **Baselined**（ADR-036） |
| `promotion` | `docs/project/design/modules/promotion.md` | **Baselined**（ADR-038） |
| `platform-ops` | `docs/project/design/modules/platform-ops.md` | **Baselined**（ADR-039） |

本文件与十份设计均已 **Baselined**（TECH_BASELINE=v0.1.5）。不得把盖章理解成已开工或已允许改代码。

## 12. 已关闭的拆分争议

| 争议 | 选择 | ADR |
|---|---|---|
| G7-BOUND-001 | A 按能力域切；进程只作暴露面 | ADR-007 |
| G7-BOUND-002 | A admin/merchant 只作暴露面 | ADR-008 |
| G7-BOUND-003 | A 商品一个域、两种流程 | ADR-009 |
| G7-BOUND-004 | A 交易一个域、两种支付通道 | ADR-049 |
| G7-BOUND-005 | A 拼团秒杀独立域 | ADR-011 |
| G7-BOUND-006 | A 用户与认证会话两个域 | ADR-012 |
| G7-BOUND-007 | A 树与入驻两个域 | ADR-013 |
| G7-BOUND-008 | A 履约独立域 | ADR-014 |
| G7-BOUND-009 | A 推广独立域，本期只保留 | ADR-015 |
| G7-BOUND-010 | A 平台运营独立域，本期只保留 banner | ADR-016 |
| G7-BOUND-011 | A 冻结 10 个 ID 与 PRD 映射 | ADR-017 |

被拒方案见各 ADR，本文不重开。

## 13. 明确不写 / TBD

- 盖章时本文件 **不是** Baselined（现已随 ADR-047 Baselined）
- 不写路由清单正文
- **叠加 DEC-049：** mall-online 本机端口已写死 8035；众享源品 - 在线商城 H5 8036。下列仍不编造：过审后改一级、存量映射、核销有效期、最短密码、Redis db、jwt.expire
- 不设计：众享源品 - 在线商城拼团秒杀、餐饮核销（本期不做）、众享源品 - 在线商城物流、banner 改挂
- 消息/搜索/监控产品选型 **TBD**（ADR-005）

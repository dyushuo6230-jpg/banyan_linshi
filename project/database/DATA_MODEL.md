# 数据模型

| 字段 | 值 |
|---|---|
| 文档名称 | 数据模型 |
| 文档编号 | DB-G9-MODEL |
| 版本 | 0.1.0 |
| 状态 | Baselined |
| 负责人 | TBD |
| 创建日期 | 2026-09-05 |
| 更新时间 | 2026-09-07 |
| 关联来源 | ADR-042、G8 十份 Approved、nunu-go-api/model |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | G9-DRAFT=A |
| 适用版本 | 文档体系 v0.1.3 |
| 替代文档 | 无 |

共库。权威写入在能力域；进程只是暴露面。独立进程 ≠ 独立库。费率数字与现码一致候选：整数万分比；是否冻结该精度随树表落地，不另编造百分比口径。

## 1. 所有权

| 数据 | 现码表（事实） | 权威模块 | 本期目标 |
|---|---|---|---|
| 经营类目树 / 节点费率 | `merchant_category`（四业态根）+ `goods_category.commission_rate` | `tree` | 四业态根在经营类目；在线商城一级读平台类目（DEC-021），不并表删除 |
| 平台商品类目 | `goods_category` | `tree` / `goods` | 结构权威；与计佣一级同一套（DEC-012/021）；本批不并表删除 |
| 入驻申请 | `merchant_apply` | `onboarding` | 增加业态、可售一级；`merchant_category_id` 不再作主数据 |
| 店铺 | `merchant` | `onboarding` 绑定 + 租户资料 | 业态/可售一级；`commission_rate` 不作新单权威；`is_self` 退出业务规则，列可留默认 0 |
| 商品 | `goods` | `goods` | 继续一表两种流程；审核台不拆 |
| 品牌 | `goods_brand` | `goods` | 保留，发品可选 |
| 店内分类 | `shop_goods_category` | `goods` | 本地生活用 |
| 拼团/秒杀 | `groupon_*`、`seckill_*` | `group-seckill` | 仅本地生活；待审存量改未上架 |
| 扫桌 | `dining_table` | `fulfillment` | 下单前扫桌 |
| 核销 | 现码核销相关表 | `fulfillment` | 美发/商超支付后核销；有效期 **TBD** |
| 用户 | `user` | `user` | **一张表两个池**；列 `user_pool`（DEC-045：1 店铺 / 2 众享源品 - 在线商城） |
| 订单 | `order_info` | `trade` | 带池（`user_pool`，DEC-045）；抽佣快照；完善字段清单 **TBD** |
| 支付 | `pay_record` | `trade` | 两通道；回调各打本进程 |
| 结算 | `settlement` 等 | `trade` | 在线商城按快照入账/提现；本地生活应付佣金对账（DEC-033）；周期 **TBD** |
| 平台 banner | `banner` | `platform-ops` | 保留管理现码；众享源品 - 在线商城首页读取（DEC-039） |
| 店铺/周边 banner | `merchant_banner`、`nearby_banner` | 非 platform-ops | 不混 |
| 推广员 / 小魔推 | `promoter`、`magic_push` 等 | `promotion` | 保留现码，不改造。本地生活扫码进店可写现状、不必验；在线商城的顾客端不新做 |

## 2. 逻辑实体（本期要收口的）

### 2.1 TreeNode（`tree`）

四根 `code`：`catering` / `hair` / `supermarket` / `online-mall`。在线商城子树本批直接读 `goods_category`（DEC-021）；经营类目不再挂子节点。

目标：业态根在 `merchant_category`（`02-business-tree.sql`）；平台类目费率在 `goods_category.commission_rate`（`03-goods-category-rate.sql`，NULL=未配置）。**不并表删除** `goods_category`。

不存：店铺业态、入驻已选一级、商品挂点、订单快照。

### 2.2 Apply / MerchantBinding（`onboarding`）

`merchant_apply`：业态代码、在线商城已选一级 ID 列表（1～3，DEC-032）、`sales_id`、status（0 待审 / 1 通过 / 2 驳回）。资质本期沿用执照采集（DEC-032）；不把身份证列写成必填。

过审后 `merchant` 绑定业态与可售一级。在线商城强制 1～3 个一级（DEC-032）。

### 2.3 Goods（`goods`）

继续 `goods`。在线商城挂树节点（所属一级由树解析）；本地生活用店内分类。`audit_status` + `status` 共同决定可售，并认树/店内分类启用状态（DEC-035）。品牌 `brand_id` 可选。

类目停用后已上架商品：**不可再售、不改商品行、已下单不改快照**（DEC-035）。驳回再提/编辑是否重审 **TBD**。

### 2.4 UserAccount（`user`）

继续一张 `user`。店铺池：店 + 手机号。众享源品 - 在线商城池：商城池 + 手机号/账号。老数据视为店铺池。`merchant_id=0` **不得**默认成众享源品 - 在线商城。池如何落列 **TBD**。禁止拆表。

### 2.5 Order / CommissionSnapshot（`trade`）

继续 `order_info`。订单必须带用户池。已付单必有节点费率快照（节点 ID、费率、抽佣额）。快照列名实施时定，语义不得改回店铺 `commission_rate`。退款状态机沿用现码。部分成功拆单 **TBD**。

### 2.6 Session / Credential（`auth-session`）

口令不可逆；无业务含义的明文旁路口令。作废名单按进程隔离（Redis 键或 db **TBD**）。不在用户表存会话。

### 2.7 其余

`group-seckill` / `fulfillment` / `promotion` / `platform-ops`：沿用现码表；本期不迁表、不合并中台。拼团是否出核销码 **TBD**。活动进行中停用：**停后不可新参、旧单不自动退**（DEC-038）。

## 3. 关系（逻辑）

```text
TreeNode 1---n TreeNode
MerchantBinding n---1 TreeNode(业态根)
MerchantBinding n---n TreeNode(可售一级，仅 online-mall)
Goods n---1 TreeNode(在线商城挂点) 或 n---1 ShopCategory(本地生活)
Order n---1 UserAccount（必须同池）
Order n---1 CommissionSnapshot（已付）
Apply n---0..1 Merchant
```

## 4. 敏感级别

| 级别 | 例子 | 规则 |
|---|---|---|
| 秘密 | jwt.secret、mini_secret、支付密钥、明文旁路口令（应消除） | 不进 Git、不进响应、不进日志 |
| 隐私 | 手机号、身份证图、执照、票 | 最小可见；入驻票面无手机号 |
| 内部 | 费率、抽佣快照、审核原因 | 后台按权 |
| 公开 | 已上架可售商品、树的启用节点（对入驻/发品需要的） | C 端可见集按渠道 |

Redis db 数字、jwt.expire 秒数 **TBD**。

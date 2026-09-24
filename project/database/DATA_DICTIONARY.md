# 数据字典

| 字段 | 值 |
|---|---|
| 文档名称 | 数据字典 |
| 文档编号 | DB-G9-DICT |
| 版本 | 0.1.0 |
| 状态 | Baselined |
| 负责人 | TBD |
| 创建日期 | 2026-09-05 |
| 更新时间 | 2026-09-12 |
| 关联来源 | ADR-042、nunu-go-api/model、CR-035 |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | G9-DRAFT=A、DEC-010、CR-035 |
| 适用版本 | 文档体系 v0.1.34 |
| 替代文档 | 无 |

只列本期语义变更与必须遵守的约束。未列出的现码列沿用 `nunu-go-api/model`。**TBD 不得在实施时擅自写死。**

## 1. 业态代码（逻辑枚举）

| 值 | 含义 | 约束 |
|---|---|---|
| `catering` | 餐饮 | 根不可删；费率可配 |
| `hair` | 美发 | 同上 |
| `supermarket` | 商超 | 同上 |
| `online-mall` | 在线商城 | 根不是计佣一级；计佣在平台类目一级（DEC-021） |

禁止第五业态。显示名可改，代码不可改。落地表：扩 `merchant_category`（`parent_id`/`code`/`level`/`updated_by`；`commission_rate` 可 NULL）。`goods_category.commission_rate` 可 NULL（`03-goods-category-rate.sql`）。经营类目不再挂子节点。

## 2. 入驻申请 `merchant_apply`

| 逻辑字段 | 现码 | 目标 | 约束 |
|---|---|---|---|
| status | 0/1/2 | 保持 | 待审不可经营 |
| sales_id | 有 | 保持 | 只注入，不改审核状态 |
| merchant_category_id | 主数据 | **不再作新申请主数据** | 可留兼容只读 |
| 业态代码 | `business_type` 已落列 | 必有 | 四选一；存量待审可空，审核时补选 |
| 可售一级 ID 列表 | `sellable_level_ids` 已落列 | 在线商城必有 1～3 个（DEC-032）；本地生活空 | 只读树 ID；停用不静默删 |
| 资质列 | 现码执照（身份证列闲置） | 本期必填仅沿用执照（DEC-032） | 不把身份证/行业许可证升格必填 |

## 3. 店铺 `merchant`

| 逻辑字段 | 现码 | 目标 |
|---|---|---|
| commission_rate | 店铺抽佣权威 | 列可留；**新单不以它为权威** |
| is_self | 自营 | 退出业务规则；默认 0；何时删列 **TBD** |
| merchant_category_id | 扁平类目 | 新绑定改业态根 + 可售一级 |
| 业态代码 / 可售一级 | `business_type` / `sellable_level_ids` 已落列 | 过审或迁移后写入 |

无业态老店默认迁 `catering`。`is_self=1` 不迁在线商城。

## 4. 商品 `goods`

| 逻辑字段 | 现码 | 目标 |
|---|---|---|
| category_id | 平台类目 | 在线商城挂 `goods_category`；计佣一级即该类目树的一级（DEC-021） |
| shop_category_id | 店内分类 | 本地生活继续用 |
| brand_id | 可选 | 继续可选，不得强制 |
| audit_status | 0 待审 1 通过 2 驳回 | 本地生活普通商品与在线商城同一审核台 |
| status | 草稿/上架/下架/违规下架 | 可售 = 过审 ∧ 上架 ∧ 渠道规则 |

未挂一级：不可售。批量审核每条独立结果；整批回滚 **TBD**。

## 5. 用户 `user`

| 逻辑字段 | 现码 | 目标 |
|---|---|---|
| merchant_id | 所属店，0 为脏数据风险 | 店铺池用店；空店脏数据不得默认众享源品 - 在线商城 |
| user_pool | 无（DEV-005 加列） | `TINYINT`：1=店铺池，2=众享源品 - 在线商城池（DEC-045）。存量一律 1 |
| mobile | 同店非空唯一 | 店铺池：店+手机号；众享源品 - 在线商城池：池+手机号/账号 |
| password | 扫码入口 bcrypt | 口令存储属 `auth-session`；最短长度 **TBD**。本地生活扫码进店：本店一人一机；密码错不注册（DEC-010 v1.1） |
| 池 | 无 | 列名 `user_pool`（DEC-045）；语义：两个池，一张表 |

openid 全局唯一是现码事实；与分池并存时如何约束 **随实施不改变分池语义**。

## 6. 订单 `order_info`

| 逻辑字段 | 现码 | 目标 |
|---|---|---|
| user_id | 有 | 必须同时带**池**（`user_pool`，DEC-045），防串号 |
| user_pool | 无（DEV-005 加列） | 下单从用户拷贝；mall 只认 1 |
| 抽佣 | 偏店铺费率 | 已付必有节点费率快照 |
| 完善字段 | 现码列 | 沿用现列，本期不增补（DEC-039 / REQ-104） |

金额单位沿用现码（分）。结算周期 **TBD**。

## 7. 会话与配置（不落业务表的）

| 项 | 口径 |
|---|---|
| jwt.secret | mall-online 独立，数值不进本文 |
| jwt.expire | **TBD** |
| Redis db | mall 现用 2；mall-online 独立键或独立 db，数字 **TBD** |
| 本机端口 8035 | 建议，是否死写 **TBD** |

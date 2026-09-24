# 技术文档终审审计

| 字段 | 值 |
|---|---|
| 文档名称 | 技术文档终审审计 |
| 文档编号 | BASE-07 |
| 版本 | 0.1.0 |
| 状态 | Draft |
| 负责人 | TBD |
| 创建日期 | 2026-09-05 |
| 更新时间 | 2026-09-05 |
| 关联来源 | PRODUCT_PRD v0.1.5、architecture/、design/modules/、api/、database/、standards/、ADR-046 |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | NEXT-GATE=A、ADR-046、ADR-047、TECH_BASELINE=v0.1.5 |
| 适用版本 | 文档体系 v0.1.5 |
| 替代文档 | 无 |

本文件是 G10 之后、盖章之前的一致性审计。**已应用：TECH_BASELINE=v0.1.5（ADR-047）。** 审计当时不是盖章；盖章后本文件保留为证据，不改业务代码。待配置不得编造。

审计范围：PRD、总体架构五份、`MODULE_BOUNDARIES.md`、G8 十份设计、`api/`、`database/`、`standards/`。G10 批次文档只作对照（Planned），不纳入本次拟盖章集合。

## 结论

| 等级 | 数量 | 是否阻断盖章 |
|---|---|---|
| P0 | 0 | 否 |
| P1 | 0 | 否 |
| P2 | 有 | 否（已标明 TBD 或账务漂移，不构成互斥规则） |

**门禁：P0/P1 = 0。** 用户已确认并应用 `TECH_BASELINE=v0.1.5`（ADR-047）。

## 1. P0

无。未发现两份 Approved 文档对同一业务规则给出相反已确认结论。

已核对且一致的硬规则：

| 主题 | 一致口径 |
|---|---|
| 四业态、一棵树、到店不是业态 | PRD / DEC-001 / `tree.md` / DATA_MODEL |
| 一套租户后台、四套模板 | PRD / DEC-002 / ADR-008 |
| 一张 `user` 表、共表分池、禁止拆表 | DEC-003 / `user.md` / DATA_MODEL / 安全架构 |
| 本地生活拼团秒杀租户自发、平台不审；在线商城无此菜单 | DEC-004 / `group-seckill.md` / MODULE_BOUNDARIES |
| 登录五条、网页 Cookie+CSRF、小程序 Header、认店只限本地生活 | DEC-005 / 安全架构 / `auth-session.md` / API 总览 |
| 无平台自营、`is_self` 退出业务规则 | DEC-006 / platform-ops / trade |
| 三套 banner 不混；平台 `banner` 不对接本期 C 端 | DEC-007 / ADR-016 / DATA_MODEL |
| 本地生活普通商品平台必审 | 盖章当时 DEC-016 / goods / API；**盖章后已被 DEC-026 / CR-007 废止**（见 GAP-006） |
| 两种支付通道：店账户→mall；平台号→mall-online | REQ-100/101 / ADR-003 / ADR-049 / trade |
| mall-online 独立进程、目录尚未创建、共库 | ADR-001～004 / PROJECT_STRUCTURE |
| 十个技术模块 ID；M03/M07 不是技术模块 | ADR-017 / MODULE_BOUNDARIES / G10 DEV-002/010 |

编号 CONFLICT-001～010 均已关闭。QUESTION-001～019 均已关闭。

**盖章后变更（不改本审计当时结论）：** CR-007 / DEC-026 废止本地生活普通商品必审。业务真源以 PRD v0.1.7 为准。架构/G8 旧句见 GAP-006。

## 2. P1

无。无未关闭的金额/权限/状态机互斥。

## 3. P2（不阻断盖章；盖章后也不得编造）

### 3.1 无编号待配置（产品/技术落地）

- 在线商城入驻是否强制 1～3 个一级；入驻资质字段清单
- 核销有效期 / 一次核销 / 过期退款 / 部分核销
- 完善订单信息字段清单（REQ-104）：**已由 DEC-039 收口**
- 最短密码长度数字：**已由 DEC-062 收口**（后台 10 位四类至少三类；顾客端 8 位字母+数字）；jwt.expire、Redis db 仍待配置
- 拼团进行中停用：**已由 DEC-038 收口**；类目停用后已上架商品：**已由 DEC-035 收口**；驳回再提/编辑是否重审；批量审核整批失败策略
- 用户池落库列名；`goods_category` 并表已否决本批删除（DEC-021），费率列已加
- 平台菜单改名；其余复制侧栏项是否再按业态藏
- 在线商城「内容管理→轮播管理」接到哪路 C 端：**已由 DEC-039 收口**
- 生产域名证书、商户号/appid；Cookie/CSRF 跨域落地
- `is_self` 列何时删除；结算周期、部分成功拆单

### 3.2 账务与回写漂移（语义未反转）

- G6/G7 文首「关联决策」多停在 DEC-018，正文已引用后续 DEC/ADR
- G8 各份仍写「关联来源：OVERALL_ARCHITECTURE Draft」，实际 G6 已 Approved（ADR-040）
- `baseline/06_REQUIREMENT_ALIGNMENT_AUDIT.md` 仍写「菜单最终名称待 PRD」「支付账户待写入 PRD」，已被 DEC-020 / PRD 覆盖，本文未改 BASE-06
- TRACE 的架构 / 技术模块 / API 列多为 `—`，映射已在 `MODULE_BOUNDARIES.md` 与 G10 批次列
- `platform-ops.md` 与 DEC-039：众享源品 - 在线商城首页读平台 `banner`；店铺 `merchant_banner` 仍为本地生活店内轮播。不构成「两套表」冲突

### 3.3 明确不纳入本期必验（盖章后仍不做）

外卖；在线商城拼团秒杀；众享源品 - 在线商城 AI/发现；餐饮核销码；小魔推改造；正式 UI_SPEC；消息/搜索/监控产品；物理删除 `is_self` 列。

## 4. 已盖章范围（TECH_BASELINE=v0.1.5 已应用）

纳入：

- PRD v0.1.5（`prd/`）现为 Baselined
- G6 五份（`architecture/` 除边界外的总体架构）现为 Baselined
- G7 `MODULE_BOUNDARIES.md` 现为 Baselined
- G8 十份设计 + 整夹现为 Baselined
- G9 `api/` `database/` `standards/` 现为 Baselined
- 已应用 DEC-001～020、ADR-001～047、CR-001～005

不纳入本次盖章：

- G10 批次文档（保持 Draft/Planned）
- G9.1 占位 `UI_SPEC.md`（非正式规范）
- `ENABLE_UI_SPEC_GENERATION=false` 下的 UI Contract
- 无编号待配置的具体取值
- 业务代码与 `app/mall-online` 目录

盖章后这些文档只读。再改业务规则走 CR + 知情决策。

## 5. 不可变约束（盖章后编码也不得推翻）

1. `ALLOW_CODE_CHANGES` 已由 ADR-048 打开；盖章本身 ≠ 开工，且只改 Ready 批次。
2. 四业态枚举与一棵经营类目树；抽佣新单以节点费率快照为准。
3. 一套租户后台、四套模板；菜单有无与已点名显示名以 DEC-020 为准。
4. 一张 `user` 表、两个池；mall 与 mall-online 票不互认。
5. 本地生活支付到该租户、回调 mall；众享源品 - 在线商城平台统一收、回调 mall-online。
6. 三套 banner 不混。
7. 独立进程 ≠ 独立库。改真表走 `deploy/sql` 可重复增量，禁止 AutoMigrate 当发布手段。
8. 待配置保持 TBD，实施时停下来再决策，不得编造。

## 6. 迁移与回滚影响（盖章本身）

盖章只改文档状态，不迁数据、不发版。

以后获准改代码时：迁移/回滚以 `database/MIGRATION_PLAN.md` 与 `delivery/ROLLBACK_PLAN.md` 为准。测试可清库；生产禁止清库。回滚代码不得把已确认规则倒回去（例如再把店铺抽佣当新单权威，或拆两张用户表）。

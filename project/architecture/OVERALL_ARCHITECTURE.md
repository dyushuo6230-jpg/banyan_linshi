# 总体应用架构

| 字段 | 值 |
|---|---|
| 文档名称 | 总体应用架构 |
| 文档编号 | ARCH-G6-OVR |
| 版本 | 1.0.0 |
| 状态 | Baselined |
| 负责人 | TBD |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-05 |
| 关联来源 | PRODUCT_PRD Approved、ADR-001～040 |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | ADR-001～ADR-040、DEC-001～DEC-018 |
| 适用版本 | 文档体系 v0.1.3 |
| 替代文档 | 无 |

本文件是 G6 **Baselined**（ADR-040；TECH_BASELINE=v0.1.5）。不能当作已开工。上下文见 `SYSTEM_CONTEXT.md`；认证见 `SECURITY_ARCHITECTURE.md`；部署见 `DEPLOYMENT_ARCHITECTURE.md`；非功能见 `NON_FUNCTIONAL_REQUIREMENTS.md`；模块边界见 `MODULE_BOUNDARIES.md`（G7 **Baselined**，ADR-019）。

**叠加 DEC-049 v1.0.2：** mall-online 本机 8035；众享源品 - 在线商城 H5 独立进程 8036、整包 embed、根路径进首页。测试 `.gyyx.store` / 正式 `.zhengdeyunqi.cn`。

## 1. 架构目标与质量属性

| 目标 | 质量属性 | 引用 |
|---|---|---|
| 四业态可入驻、按业态套租户菜单、抽佣挂树节点费率快照 | 正确性、可演进 | REQ-001～007、DEC-001、DEC-002 |
| 本地生活履约与店账户支付仍走现 mall | 兼容、隔离 | REQ-040～045、REQ-100 |
| 众享源品 - 在线商城逛买与登录闭合，独立 API 进程 | 可独立发布 | REQ-060～066、ADR-001 |
| 用户分池、会话可作废、认店只限本地生活 | 安全、隐私 | REQ-070～073、REQ-080～091、DEC-003、DEC-005、ADR-002 |
| 众享源品 - 在线商城平台统一收款 | 资金归属正确 | REQ-101、ADR-003 |
| 基于现码扩展，不大改技术栈 | 迁移成本可控 | G0、CURRENT_BASELINE |

资料未给量化容量/SLA。优先级（不编造数字）：会话与资金隔离正确 > 进程可独立发布 > 性能容量本期不验收（DEC-039）。

## 2. 应用与组件

沿用现码 Go 多进程，不抽本期公共 internal 包（ADR-004）。

```text
[平台后台 Web] ----Cookie+CSRF----> admin API     :8031
[租户后台 Web] ----Cookie+CSRF----> merchant API  :8033   一套系统，四套菜单模板
[入驻 H5]      ----静态/部分 embed----> app/h5        :8034
[众享营销 - 本地生活] --Header 票------> mall API      :8032   支付到店
[众享源品 - 在线商城多端]   --Header 票------> mall-online   :8035   平台统一收
[众享源品 - 在线商城 H5]   ----整包 embed----> app/h5-online :8036   根路径进首页
                      |
                      +--> MySQL（同一套库）
                      +--> Redis（同一实例；mall-online 键或 db 隔离）
                      +--> 短信 / OSS（沿用 mall 连接）
```

| 进程 | 现状 | 目标职责（能力面） | 非职责 | 引用 |
|---|---|---|---|---|
| admin | 已有 :8031 | 业态树、入驻审核、四套菜单配置、在线商城与本地生活普通商品审品、订单财务；去掉拼团秒杀经营 | 不经营本地生活场次；banner 菜单保留，众享源品 - 在线商城首页读取见 DEC-039 | REQ-010～014、REQ-032、REQ-110、DEC-004、DEC-007、DEC-039 |
| merchant | 已有 :8033 | 一套后台按业态套模板：发品、履约、本地生活拼团秒杀（租户自发布） | 不为在线商城露出拼团秒杀；不是四套独立后台 | REQ-020～025、REQ-050～052、DEC-002、DEC-004 |
| mall | 已有 :8032 | 本地生活 C 端：扫桌/核销、认店、店账户支付、本地生活拼团秒杀 C 端 | 不服务众享源品 - 在线商城逛买；不作废 mall-online 票 | REQ-040～045、REQ-100、DEC-005 |
| mall-online | 已有 :8035 | 众享源品 - 在线商城 C 端登录与逛买、平台统一支付回调 | 不暴露扫桌、认店、店支付、本地生活拼团秒杀 C 端 | REQ-060～066、REQ-101、ADR-001～004 |
| h5 | 已有 :8034 | 入驻 H5；只嵌部分静态文件 | 不是 API 进程 | REQ-010 |
| h5-online | 已有 :8036 | 众享源品 - 在线商城 H5 整包 embed；根路径进首页 | 不是 API 进程；不挂微信业务域名校验文件 | REQ-065、ADR-001、DEC-049 |

前端对照：本地生活 `go-uni-app`；众享源品 - 在线商城 `go-uni-app-online`（页面口径 DEC-008）。开发代理打 mall-online **8035**。H5 打包域名与端口见 DEC-049。

忽略且不做考虑：`nunu-go-api/mall-uniapp`、仓库根 `admin/`、`uni-app/`、`niucloud`。

## 3. 数据架构（逻辑，不冻结表结构）

独立进程 ≠ 独立库（ADR-001）。本期共库，逻辑隔离靠业态、用户池、订单池字段，表结构细节留 G8/G9。

| 逻辑域 | 权威写入 | 读取方 | 引用 |
|---|---|---|---|
| 业态 / 经营类目树 / 节点费率 | 树能力域（ADR-013）：平台维护四业态一棵树与节点费率 | 入驻、租户发品、下单计佣 | REQ-001～007、DEC-001、DEC-012、ADR-013 |
| 入驻申请与审店 | 入驻能力域（ADR-013）：同一套 H5、按业态采集、平台审店；只读树 | merchant、mall、mall-online | REQ-010～014、DEC-011、ADR-013 |
| 租户资料与菜单模板绑定 | 平台配置 + 租户维护；四套菜单是 merchant 暴露面（ADR-008） | merchant | REQ-020、DEC-002、ADR-008 |
| 商品 | 一个能力域、两种流程（ADR-009）：本地生活店内分类发品，平台审后本店可售；在线商城挂经营类目树，平台审后众享源品 - 在线商城可售 | mall / mall-online 各读本端可见集 | REQ-030～034、DEC-009、DEC-013、DEC-016、ADR-009 |
| 拼团秒杀 | 独立能力域（ADR-011）：本期仅本地生活租户自发、平台不审；成交走交易模块 | mall、本地生活租户后台 | REQ-050～054、DEC-004、DEC-014、ADR-011 |
| 履约 | 独立能力域（ADR-014）：餐饮扫桌；美发/商超核销；本期餐饮不走核销码 | mall、本地生活租户后台 | REQ-040～045、ADR-014 |
| 用户 | 用户能力域（ADR-012）：共表分池、池内唯一 | mall=店铺池；mall-online=众享源品 - 在线商城池 | REQ-070～073、DEC-003、ADR-012 |
| 本地生活订单与店支付 | 交易能力域的 mall 暴露面（ADR-049）：店账户通道 | 租户后台、平台财务 | REQ-100、REQ-040、ADR-049 |
| 众享源品 - 在线商城订单与平台支付 | 交易能力域的 mall-online 暴露面（ADR-049）：平台商户号通道 | 租户后台、平台财务 | REQ-101、REQ-060、ADR-049 |
| 抽佣 | 下单时节点费率**快照**（属交易能力域，ADR-049）；店铺抽佣字段不再作新单权威 | 结算读快照 | REQ-102、REQ-103、DEC-001、DEC-013、ADR-049 |
| 会话作废名单 | 认证会话能力域（ADR-012）：各端 Redis 键（mall 与 mall-online 隔离） | 本端鉴权 | REQ-080～091、ADR-002、ADR-012 |
| 平台运营 | 独立能力域（ADR-016）：平台 `banner` 表与轮播管理现码；众享源品 - 在线商城首页读取（DEC-039）；本地生活不读 | admin / mall-online | REQ-110、DEC-007、DEC-039、ADR-016 |
| 推广 | 独立能力域（ADR-015）：推广员入驻注入 + 小魔推现码；本期不改造、不纳入必验 | mall、merchant、众享营销 - 本地生活现码入口 | REQ-111、REQ-120、DEC-010、ADR-015 |

未挂一级的在线商城商品：不可售、不可下单，不得用缺省费率或 0 抽佣放行（DEC-013）。

## 4. API 与通信

| 通道 | 约定 | 引用 |
|---|---|---|
| 平台 / 租户网页 | Cookie + CSRF；不改成纯 Header 票 | REQ-080、DEC-005 |
| 众享营销 - 本地生活、众享源品 - 在线商城 C 端 | Header 票 | REQ-080、DEC-005、ADR-002 |
| 进程间 | **无**同步 RPC 要求；不共享 JWT | ADR-002 |
| 支付回调 | 本地生活 → mall 域名；众享源品 - 在线商城 → mall-online 自己的域名 | REQ-100、REQ-101、ADR-003 |
| 路由清单 | mall-online 复制后去掉本地生活专用路由；清单正文留 G8 | ADR-004 |

不在本文发明 REST 路径、消息队列主题或网关产品。

## 5. 认证、授权与数据隔离

见 `SECURITY_ARCHITECTURE.md`。要点：分池（DEC-003）；可作废会话（DEC-005）；mall-online 独立 `jwt.secret` 与作废名单键（ADR-002）；认店只限本地生活（DEC-005）；网页 Cookie+CSRF。

## 6. 缓存、任务与消息

| 能力 | 本期口径 | 引用 |
|---|---|---|
| 缓存 / 会话黑名单 | Redis 同一实例；mall 现用 db 2；mall-online 用独立键前缀或独立 db，数字不冻结 | ADR-001、ADR-002 |
| 任务、消息、通知 | **TBD**，延期 G7～G9 | ADR-005 |
| 搜索 | **TBD**，延期 G7～G9 | ADR-005 |

不得把未确认的队列或搜索引擎写成已选。

## 7. 第三方服务

| 服务 | 谁用 | 口径 | 引用 |
|---|---|---|---|
| 阿里云短信 | mall 与 mall-online | 沿用 mall 连接 | ADR-001、REQ-080 |
| 上传 / OSS | 各后台与 C 端 | 沿用 mall 的 upload/storage | ADR-001 |
| 微信支付（店） | 仅 mall | 支付到该店账户 | REQ-100 |
| 微信支付（平台商户号） | 仅 mall-online | 统一收；回调打 mall-online；商户号/appid 数值 TBD | REQ-101、ADR-003 |
| 微信小程序 appid | mall 与 mall-online 各配 | mall-online **不得默认抄 mall** | DEC-005、ADR-003 |

## 8. 安全、隐私与审计

见 `SECURITY_ARCHITECTURE.md`。验收五条（REQ-080～091）：忙不踢、闲必踢、闸立刻废、串不了店、库无明文密码。本期不做：短信二次验证、设备列表、异地提示、加密 JWT、登录密码再套 RSA、C 端 30 分钟闲置（PRODUCT_PRD §5.4）。

## 9. 性能、可用性、容灾

见 `NON_FUNCTIONAL_REQUIREMENTS.md`。量化指标资料未给，**TBD**。监控/容灾/回滚细则延期 ADR-005。已确认的发布单元：mall-online 可独立进程发布；失败时本地生活 mall 不被动下线。

## 10. 部署、灰度、降级、回滚

见 `DEPLOYMENT_ARCHITECTURE.md`。入驻 H5 进 `app/h5` 部分 embed；众享源品 - 在线商城 H5 整包进 `app/h5-online/web/dist` 再编独立二进制（本机 8036，根路径进首页，DEC-049）。灰度/回滚细则 **TBD**（ADR-005）；进程级回滚：停 mall-online 或 h5-online 不必强制回退 mall。

## 11. 当前实现 / 目标 / 差距 / 迁移

| 项 | 当前 | 目标 | 差距 | 迁移要点 |
|---|---|---|---|---|
| 业态 | 无 | 四业态一棵树 | G8/G9 | 无业态老店默认迁餐饮（DEC-011）；`is_self` 不因此变在线商城 |
| 商户菜单 | 单树 | 四套模板同一配置页 | G8 | 隐藏非安全边界（DEC-002）；菜单名待配置 |
| C 端 API | mall 8032 + mall-online 8035 | mall + mall-online | 测/正式 Nginx 仓库外 | 已建进程；代理已打 8035（DEC-049） |
| 用户 | 按店 | 共表分池 | 池字段 G8 | 同一手机号三账号：店 A、店 B、众享源品 - 在线商城（REQ-070） |
| 登录 | 明文旁路等缺口 | SRC-REQ-003 一次落地 | 开发批次 | 网页 Cookie+CSRF；C 端 Header |
| 支付 | 仅店账户路径成熟 | 另增平台商户号路径 | 通道申请 TBD | 本地生活不改 REQ-100；众享源品 - 在线商城 REQ-101 |
| 拼团秒杀 | 平台有审核 | 独立能力域；租户自发、平台不审；在线商城无此能力；成交走交易 | 菜单与数据 | 待审改未上架，不自动开卖（DEC-014、ADR-011） |
| 抽佣 | 店铺字段 | 节点费率快照 | G8/G9 | 未挂一级不可售（DEC-013） |

不做外卖；在线商城无拼团秒杀；众享源品 - 在线商城本期不做 AI/发现对接（PRODUCT_PRD §5.2）。

## 12. ADR 清单

| ADR | 状态 | 主题 |
|---|---|---|
| ADR-001 | Approved | 独立 mall-online 进程；连接沿用 mall；本机 8035；H5 整包进 h5-online 8036（DEC-049） |
| ADR-002 | Approved | 独立 jwt.secret 与作废名单键；票不得跨进程 |
| ADR-003 | Approved | 独立 wechat；平台商户号；回调打 mall-online |
| ADR-004 | Approved | 按 mall 模板复制独立工程；去掉本地生活专用路由；不抽公共包 |
| ADR-005 | Approved | 消息/搜索/监控细则延期 G7～G9 |
| ADR-006 | Approved | 生成本组 G6 Draft |
| ADR-040 | Approved | 批准本组五份为 Approved；待配置保留；不是 Baselined |
| ADR-007 | Approved | 技术模块按能力域切；mall / mall-online 只作暴露面 |
| ADR-008 | Approved | admin / merchant 只作能力域后台暴露面 |
| ADR-009 | Approved | 商品为一个能力域、两种流程；审核台不拆 |
| ADR-049 | Approved | 交易为一个能力域、两种支付通道（迁自原 ADR-010） |
| ADR-010 | Approved | ToB 营销独立进程 mall-tob / h5-tob |
| ADR-011 | Approved | 拼团秒杀为独立能力域；本期仅本地生活/mall |
| ADR-012 | Approved | 用户与认证会话为两个能力域 |
| ADR-013 | Approved | 业态树与入驻为两个能力域；入驻只读树 |
| ADR-014 | Approved | 履约为独立能力域；餐饮扫桌、美发/商超核销 |
| ADR-015 | Approved | 推广为独立能力域；本期只保留现状、不纳入必验 |
| ADR-016 | Approved | 平台运营为独立能力域；本期只保留 banner、不对接 C 端 |
| ADR-017 | Approved | 冻结 10 个技术模块稳定 ID 与 PRD 映射 |
| ADR-018 | Approved | 生成 `MODULE_BOUNDARIES.md` Draft |
| ADR-019 | Approved | 批准 `MODULE_BOUNDARIES.md` 为 Approved |

候选（不在 G6 冻结）：消息任务通知方案、搜索引擎、监控产品、mall-online 路由清单正文、Redis db 号、jwt.expire、本机端口是否写成死 8035。

## 13. 明确不写

- 盖章 ≠ 自动写完所有批次；`ALLOW_CODE_CHANGES=true` 后仍只改 Ready 批次（当前仅 DEV-001）
- `app/mall-online` 目录或业务代码
- 无编号待配置的编造值（jwt.expire、Redis db、8035 是否死写等；最短密码/核销有效期/入驻一级个数已由后续 DEC 收口）

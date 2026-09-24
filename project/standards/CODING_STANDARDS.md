# 编码规范

| 字段 | 值 |
|---|---|
| 文档名称 | 编码规范 |
| 文档编号 | STD-G9-CODE |
| 版本 | 0.1.3 |
| 状态 | Baselined |
| 负责人 | TBD |
| 创建日期 | 2026-09-05 |
| 更新时间 | 2026-09-09 |
| 关联来源 | ADR-042、ADR-001～007、DEC-005、DEC-029、CURRENT_BASELINE `nunu-go-api/deploy/sql` |
| 关联需求 | REQ-080～REQ-091、REQ-065 |
| 关联决策 | G9-DRAFT=A；CR-010；STD-PIN=A |
| 适用版本 | 文档体系 v0.1.3 |
| 替代文档 | 无 |

本文件是 G9 **Baselined**（ADR-043；TECH_BASELINE=v0.1.5）。沿用现仓库 Go / Vue / uni-app 习惯，不另起目录规范。

## 1. 命名

- 技术模块稳定 ID 用短横线：`tree`、`auth-session`、`group-seckill`、`platform-ops`。
- 业态代码冻结：`catering` / `hair` / `supermarket` / `online-mall`。禁止 `dine-in`。
- Go：包名小写；导出类型 PascalCase；JSON 字段 snake_case，与现码一致。
- 表名沿用现码（`user`、`goods`、`order_info`、`merchant_apply`）。新表名小写蛇形。**池字段落库列名 TBD**，不得在本规范指定。
- 接口继续 `/api/v1/...`。进程用目录区分，不在路径上发明 `/mall-online` 前缀作为第二套风格。

## 2. 错误与响应

- 沿用现码 JSON 包络，不新造第二套 envelope。
- 业务失败给稳定错误码与可读 message；不把堆栈、SQL、密钥返回客户端。
- 鉴权失败与权限失败分开；废票与未登录分开。
- 日志：密码、完整票、授权头、明文旁路口令、小程序密钥脱敏（DEC-005）。

## 3. API

细则真源：`../api/`。本文件只定工程约束：

- 网页后台：Cookie + CSRF，禁止先改成纯 Header 票。
- C 端：Header 票。mall 与 mall-online 票不得互认。
- 写操作要幂等键或业务单号；支付回调按现码通道幂等。
- 分页沿用现码 query（页码/条数），不另发明 cursor 除非现码已有。

## 4. 数据库与事务

细则真源：`../database/`。

- 共库；不按进程独占表。
- 下单 + 支付 + 费率快照落在拥有该单的进程内；禁止 mall 与 mall-online 两阶段提交。
- 新单抽佣只写节点费率快照；店铺 `commission_rate` 不作新单权威。
- 用户读写必须带池；一张 `user` 表两个池，禁止拆成两张用户表。
- 改真表必须走 `nunu-go-api/deploy/sql/` 编号增量 SQL，且可重复执行；同一提交改 `nunu-go-api/model/`。细则见 `../database/MIGRATION_PLAN.md`。
- 禁止 `make migrate` 和 AutoMigrate 对齐测试库/正式库。生产清库不批准。

## 5. 安全

- 口令不可逆；不得回读明文或旁路口令。
- 设密复杂度以 DEC-062 为准：平台/租户至少 10 位且大小写、数字、符号四类至少三类；两套顾客端至少 8 位且字母+数字。服务端为权威。不得把旧的「不另定」或前端 6～20 当真源。
- Redis 会话键按进程隔离；mall-online 独立 `jwt.secret` 与作废名单键。db 号 **TBD**。
- 认店只限本地生活 mall；不信客户端店号。
- 生产密钥不进 Git、不进本文。
- 本地自测新设密不得再用 `123456`，须符合 DEC-062 对应端规则。正式环境禁止默认口令；各端登录页禁止写死账号或密码（DEC-064）。登录与密钥框须声明不要浏览器自动填（DEC-066）。库如何存密码仍走 DEC-005。

## 6. 禁止事项

- 创建 `app/mall-online`（属 DEV-010；本题未授权）。
- 用 AutoMigrate / `make migrate` 改测试库或正式库。
- 把推荐 TBD 写成已确认。
- 新增跨进程同步 RPC 或共享 JWT。
- 把 M03 / M07 / admin / merchant / mall 当成技术模块 ID。
- 三套 banner 混用；小魔推当本期必验；众享源品 - 在线商城做拼团秒杀 C 端。
- 考虑 `nunu-go-api/mall-uniapp`、仓库根 `admin/`、`uni-app/`、`niucloud`。

## 7. 众享源品 - 在线商城多端（DEC-029 / CR-010）

- 工程：`go-uni-app-online` **同一套代码**打本期必打端（iOS / 安卓 / H5 / 微信小程序）。鸿蒙非本期必打，不为鸿蒙另起工程。
- 有平台差异必须用 uni-app 条件编译（`#ifdef` / `#ifndef` 等）；编译产物只保留对应平台代码，避免把其他端逻辑打进包里造成冗余。
- 禁止为某一端复制第二套工程或整页拷贝双份业务逻辑。无差异处不要硬套条件编译。
- 不在本规范编造各端差异清单、appid、支付商户号。

# 测试、Git 与 Code Review

| 字段 | 值 |
|---|---|
| 文档名称 | 测试、Git 与 Code Review |
| 文档编号 | STD-G9-QG |
| 版本 | 0.1.1 |
| 状态 | Baselined |
| 负责人 | TBD |
| 创建日期 | 2026-09-05 |
| 更新时间 | 2026-09-10 |
| 关联来源 | ADR-042 |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | G9-DRAFT=A |
| 适用版本 | 文档体系 v0.1.3 |
| 替代文档 | 无 |

本文件是 G9 **Baselined**（ADR-043；TECH_BASELINE=v0.1.5）。量化 SLA / 覆盖率数字 **TBD**，不得编造。消息/搜索/监控产品 **TBD**（ADR-005）。

**叠加 DEC-049 v1.0.2：** 众享源品 - 在线商城 H5 独立二进制 `h5-online-server`（本机 8036），与 mall-online API 分开发版。

## 1. 测试

- 每个开发批次必须能独立测、独立验收、独立回滚（G10）。
- 必验对齐 PRD Given/When/Then 与模块设计测试节；小魔推（含本地生活扫码进店）、平台 banner C 端、众享源品 - 在线商城拼团秒杀 **不**纳入多业态必验。
- 至少覆盖：四业态入驻；未挂一级不可售不可下单；店账户 vs 平台支付；一张表两池不串号；mall 与 mall-online 票不互认；餐饮下单前扫桌、美发/商超支付后核销。
- TBD 未收口的规则：测试标 skip 或「沿用现码」，不得当已确认断言。
- 自动化框架沿用现码；不指定新测试产品。
- 本地自测登录口令约定见 `CODING_STANDARDS.md`「5. 安全」（统一 `123456`；正式环境禁止默认口令与登录页预填）。

## 2. Git

- 业务代码只在已授权开发批次且 `ALLOW_CODE_CHANGES=true` 时改。
- 配置真源：`*.yml.example` 进库；真实密钥 yml 不进库。
- 文档真源只改 `docs/project/`；不把 `nunu-go-api/docs` 当维护入口。
- 提交说明写清批次 ID 与需求号；不在提交信息写密钥。

## 3. Code Review

- 对照：PRD → 模块设计 → `api/` → `database/`。发现业务分歧停下来开 CR，不在代码里改规则。
- 检查：池条件、进程隔离、快照不回溯、Cookie/CSRF 网页通道、无跨进程分布式事务。
- 静态检查沿用现码 Go / 前端流水线；不新指定 linter 产品名。

## 4. 发布与回滚原则

- mall 与 mall-online 两个 API 二进制，可不同步发版。众享源品 - 在线商城 H5 是第三个二进制 `h5-online-server`，测/正式须先按环境 `npm run build:h5:test` 或 `build:h5` 再编。
- mall-online 回滚不必强制回退 mall；h5-online 回滚不必强制回退 mall-online。
- 灰度比例、网关切流、监控告警产品 **TBD**（ADR-005）。

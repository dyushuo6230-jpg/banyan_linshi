# 部署架构

| 字段 | 值 |
|---|---|
| 文档名称 | 部署架构 |
| 文档编号 | ARCH-G6-DEP |
| 版本 | 1.0.0 |
| 状态 | Baselined |
| 负责人 | TBD |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-05 |
| 关联来源 | ADR-001～ADR-006、ADR-040、CURRENT_BASELINE |
| 关联需求 | REQ-010、REQ-065、REQ-066、REQ-100、REQ-101 |
| 关联决策 | ADR-001、ADR-003、ADR-004、ADR-005、ADR-040 |
| 适用版本 | 文档体系 v0.1.3 |
| 替代文档 | 无 |

本文件是 G6 **Baselined**（ADR-040；TECH_BASELINE=v0.1.5）。监控、容灾、灰度、回滚的**细则**延期（ADR-005），不编造监控产品或编排工具。待配置保持 TBD，不得编造。

**叠加 DEC-049 v1.0.2（2026-09-10）：** 测试域名一律 `.gyyx.store`，正式一律 `.zhengdeyunqi.cn`。mall-online 本机 **8035**。众享源品 - 在线商城 H5 独立进程 `app/h5-online` 本机 **8036**，外网根路径进首页，`go-uni-app-online` 整包拷到 `web/dist` 后 `go:embed` 打进二进制。入驻 `app/h5` 仍只嵌部分文件。盖章正文历史保留；下表已按该 DEC 对齐。

## 1. 运行单元（本机现状 + 目标）

| 单元 | 本机端口 | 目标 | 引用 |
|---|---|---|---|
| admin API | 8031 | 保持 | 现码 |
| mall API | 8032 | 保持；本地生活 + 店支付 | REQ-100、ADR-001 |
| merchant API | 8033 | 保持；一套租户后台 | REQ-020、DEC-002 |
| 入驻 H5 | 8034 | 静态托管 `app/h5`（部分文件 embed） | REQ-010 |
| home | 8081 | 保持；不得被 mall-online 占用 | ADR-001 |
| mall-online API | **8035** | 独立监听；测试/正式域名见 DEC-049 | ADR-001、DEC-049 |
| 众享源品 - 在线商城 H5 | **8036** | 独立进程 `app/h5-online`；整包 embed；根路径进首页 | ADR-001、DEC-049、REQ-065 |

生产按 mall 习惯：容器内口 + Nginx 反代 + 独立域名（ADR-001）。测试/正式外网域名见 DEC-049。

`go-uni-app-online` 开发代理打 mall-online **8035**（DEC-049），不得改到 mall 8032 或 merchant 8033。

## 2. 配置与密钥

| 项 | 口径 | 引用 |
|---|---|---|
| 配置目录 | `nunu-go-api/config/mall-online` 与 `config/h5-online`；形态 `local` / `test` / `prod` + `.yml.example` | ADR-001、DEC-049 |
| 真实 yml | 不进 Git | ADR-001 |
| sms / db / redis / upload / storage | **沿用 mall 连接** | ADR-001 |
| http 端口 | 只沿用结构，不沿用 mall 端口 | ADR-001 |
| jwt.secret | 独立，不抄 mall | ADR-002 |
| wechat | 独立；回调 URL 用 mall-online 域名 | ADR-003 |
| 工程形态 | mall-online 按 mall 模板复制独立工程；h5-online 为独立静态进程 | ADR-004、DEC-049 |

目录与进程已按 DEV-010 / DEC-049 创建。真实 yml 仍不进 Git。

## 3. 数据与中间件拓扑

```text
admin :8031 ──┐
mall  :8032 ──┼── MySQL（同一套）
merchant:8033─┤
mall-online──┘        Redis 同一实例
   （:8035）              mall db=2（现状）
h5-online :8036           mall-online：独立键前缀或独立 db（数字不冻结）
                         mall-online：独立键前缀或独立 db（数字不冻结）

短信 / OSS：沿用 mall 通道
微信支付：mall → 店商户号回调；mall-online → 平台商户号回调（各域名）
```

独立进程 ≠ 独立数据库。Redis 实例共用，会话键必须隔离（ADR-002）。

## 4. 环境

| 环境 | 口径 |
|---|---|
| local | 本机多端口并存；mall-online **8035**；众享源品 - 在线商城 H5 **8036** |
| test / prod | 结构对齐 mall；外网域名见 DEC-049（测试 `.gyyx.store`，正式 `.zhengdeyunqi.cn`） |
| 支付 | 申请通道是交付依赖；未配齐可先发登录与逛买以外的进程骨架 |

## 5. 灰度、降级、回滚（已确认原则 vs TBD 细则）

| 项 | 已确认 | TBD（ADR-005） |
|---|---|---|
| 发布单元 | mall-online 与 mall 两个二进制，可不同步发版 | 具体灰度比例、网关切流产品 |
| 降级 | mall-online 不可用时，本地生活 mall 与租户后台仍应可运行 | 自动熔断与开关名称 |
| 回滚 | 回退 mall-online 进程或静态 H5，不必强制回退 mall | 编排脚本、监控告警 |
| H5 | 入驻：产物覆盖 `app/h5/web` 部分 embed。众享源品 - 在线商城：整包进 `app/h5-online/web/dist` 再编 `h5-online-server`；独立域名、根路径 | CDN / 缓存刷新步骤 |

不把未选的 K8s/云厂商写成已定。

## 6. 当前 / 目标 / 差距 / 迁移

| 项 | 当前 | 目标 | 差距 |
|---|---|---|---|
| mall-online | 独立进程 + 配置；本机 8035 | 独立进程 + 配置 + 独立域名 | 测/正式 Nginx 与 Jenkins 加编（仓库外） |
| online 前端代理 | 指向 mall-online 8035 | 指向 mall-online | 已改 |
| 众享源品 - 在线商城 H5 | 独立进程 8036；整包 embed | 同左；测/正式容器与 Jenkins | 1Panel / Jenkins 由运维加 |
| 支付回调 | 仅 mall 店账户 | 增加 mall-online 平台商户号回调 | 通道与域名 TBD |
| 监控 | 沿用现网习惯（未写入本期资料） | 细则延期 | ADR-005 |

## 7. 明确不做

- 本期不把部署工具、监控 SaaS、日志平台写成已选
- 不因本文修改现码端口或 Nginx
- 本机 mall-online **8035**、众享源品 - 在线商城 H5 **8036**（DEC-049）

# 总体技术架构

| 字段 | 值 |
|---|---|
| 文档名称 | 总体技术架构 |
| 文档编号 | DOC-G0-ARCH |
| 版本 | 1.0.0 |
| 状态 | Draft |
| 负责人 | TBD |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-10 |
| 关联来源 | PRODUCT_PRD Baselined、ADR-001～047 |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | ADR-001、ADR-002、ADR-003、ADR-004、ADR-005、ADR-006、ADR-007、ADR-008、ADR-009、ADR-010、ADR-011、ADR-012、ADR-013、ADR-014、ADR-015、ADR-016、ADR-017、ADR-018、ADR-019、ADR-020、ADR-021、ADR-022、ADR-023、ADR-024、ADR-025、ADR-026、ADR-027、ADR-028、ADR-029、ADR-030、ADR-031、ADR-032、ADR-033、ADR-034、ADR-035、ADR-036、ADR-037、ADR-038、ADR-039、ADR-040、ADR-041、ADR-042、ADR-043、ADR-044、ADR-045、ADR-046、ADR-047、ADR-049 |
| 适用版本 | 文档体系 v0.1.0 |
| 替代文档 | 无 |

G6 五份总体架构已按 ADR-040 **Baselined**（TECH_BASELINE=v0.1.5）。G7 边界已按 ADR-019 **Baselined**。稳定 ID 见 ADR-017。G8 整夹已 **Baselined**（ADR-041；十份 ADR-030～039）。G9 三夹已 **Baselined**（ADR-043）。G9.1 目录已生成（ADR-044）。G10 批次仍为 Draft。

**叠加 DEC-049 v1.0.2：** `app/mall-online` 本机 8035 已建；众享源品 - 在线商城 H5 `app/h5-online` 本机 8036、整包 embed。盖章正文「不得创建 mall-online」是开工前口径。

## 文件

| 文件 | 编号 | 状态 |
|---|---|---|
| [SYSTEM_CONTEXT.md](./SYSTEM_CONTEXT.md) | ARCH-G6-CTX | **Baselined**（ADR-040 / ADR-047） |
| [OVERALL_ARCHITECTURE.md](./OVERALL_ARCHITECTURE.md) | ARCH-G6-OVR | **Baselined**（ADR-040 / ADR-047） |
| [SECURITY_ARCHITECTURE.md](./SECURITY_ARCHITECTURE.md) | ARCH-G6-SEC | **Baselined**（ADR-040 / ADR-047） |
| [DEPLOYMENT_ARCHITECTURE.md](./DEPLOYMENT_ARCHITECTURE.md) | ARCH-G6-DEP | **Baselined**（ADR-040 / ADR-047） |
| [NON_FUNCTIONAL_REQUIREMENTS.md](./NON_FUNCTIONAL_REQUIREMENTS.md) | ARCH-G6-NFR | **Baselined**（ADR-040 / ADR-047） |
| [MODULE_BOUNDARIES.md](./MODULE_BOUNDARIES.md) | ARCH-G7-BOUND | **Baselined**（ADR-019 / ADR-047） |

## ADR 清单

| ADR | 状态 | 说明 |
|---|---|---|
| ADR-001～005 | Approved | 进程 / JWT / 支付 / 工程复制 / 延期项 |
| ADR-006 | Approved | 生成本组 Draft（G6-DRAFT=A） |
| ADR-007 | Approved | 技术模块按能力域切；进程只作暴露面（G7-BOUND-001=A） |
| ADR-008 | Approved | admin / merchant 只作能力域后台暴露面（G7-BOUND-002=A） |
| ADR-009 | Approved | 商品为一个能力域、两种流程；审核台不拆（G7-BOUND-003=A） |
| ADR-049 | Approved | 交易为一个能力域、两种支付通道（G7-BOUND-004=A；迁自原 ADR-010） |
| ADR-010 | Approved | ToB 营销独立进程 mall-tob / h5-tob（CR-042 / DEC-067） |
| ADR-011 | Approved | 拼团秒杀为独立能力域；本地生活 + 源品第二种流程（ADR-011 v1.1 / DEC-068） |
| ADR-012 | Approved | 用户与认证会话为两个能力域（G7-BOUND-006=A） |
| ADR-013 | Approved | 业态树与入驻为两个能力域；入驻只读树（G7-BOUND-007=A） |
| ADR-014 | Approved | 履约为独立能力域；餐饮扫桌、美发/商超核销（G7-BOUND-008=A） |
| ADR-015 | Approved | 推广为独立能力域；本期只保留现状、不纳入必验（G7-BOUND-009=A） |
| ADR-016 | Approved | 平台运营为独立能力域；banner + 板块（ADR-016 v1.1 / DEC-069） |
| ADR-017 | Approved | 冻结 10 个技术模块稳定 ID 与 PRD 映射（G7-BOUND-011=A） |
| ADR-018 | Approved | 生成 `MODULE_BOUNDARIES.md` Draft（G7-DRAFT=A） |
| ADR-019 | Approved | 批准 `MODULE_BOUNDARIES.md` 为 Approved（G7-APPROVE=A） |
| ADR-040 | Approved | 批准 G6 五份总体架构为 Approved（G6-APPROVE=A） |
| ADR-041 | Approved | 批准 G8 整夹为 Approved（G8-FOLDER=A） |
| ADR-042 | Approved | 生成 G9 三夹 Draft（G9-DRAFT=A） |
| ADR-043 | Approved | 批准 G9 三夹为 Approved（G9-APPROVE=A） |
| ADR-044 | Approved | 生成 G9.1 UI 应用目录与映射（G9.1-DRAFT=A） |

候选未冻结：消息任务通知、搜索、监控产品、路由清单正文、Redis db、jwt.expire、本机端口是否写成死 8035。

约束：沿用现有技术栈；mall-online 独立进程、独立 JWT、独立微信与平台支付；工程按 mall 模板复制并去掉本地生活专用路由。目录尚未创建。

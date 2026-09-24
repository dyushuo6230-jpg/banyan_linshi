# 多业态租户入驻系统 · 项目文档入口

| 字段 | 值 |
|---|---|
| 文档名称 | 项目文档入口 |
| 文档编号 | DOC-G0-README |
| 版本 | 0.0.0 |
| 状态 | Draft |
| 负责人 | TBD |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-05（DEC-020）|
| 关联来源 | G0 用户初始化口令 |
| 关联需求 | 无 |
| 关联决策 | DEC-001～DEC-020、ADR-001～ADR-048 |
| 适用版本 | 文档体系 v0.0.0 |
| 替代文档 | 无 |

## 当前状态

- 当前阶段：`IMPLEMENTATION`（DEV-003 入驻与审店 In Progress）
- 仓库作用：`CURRENT_BASELINE`（当前代码是正式系统，未来方案必须兼容）
- 是否允许改业务代码：`true`（仅 Ready 批次；DEC-025 期间不新改）
- 文档总进度：72%（PRD/G6～G9 Baselined；G10 Draft；PRD 业务规则 v0.1.7 / CR-007）
- 当前分支：`feature/multiple_business_model`
- 当前 Commit：`dc326a30`
- 治理规范：`docs/governance/common_prd_v3.1/`

已确认：业态、经营类目树、抽佣、租户四套菜单、众享源品 - 在线商城用户分池、本地生活拼团秒杀不审、**本地生活普通商品不审、只审在线商城（DEC-026；废止 DEC-016 该条）**、本期测试可清库（DEC-017）、登录安全全部落地（已收口）、平台无自营店（`is_self` 退出业务规则）、平台 banner 保留且众享源品 - 在线商城首页读取（DEC-039）、众享源品 - 在线商城页面以 go-uni-app-online 为准（说明只对照）、品牌库保留且发品可选、小魔推保留代码且四套侧栏隐藏（DEC-010、DEC-019）且不纳入本期必验、租户已点名菜单与轮播按业态拆入口（DEC-020）、无业态老店默认迁餐饮、在线商城类目与计佣一级同一套、未挂一级不可售、待审拼团秒杀改未上架。编号 P2 已清。PRD 已批准（DEC-015），业务规则 v0.1.7（CR-001～007），盖章基线 ADR-047 v0.1.5。mall-online 独立进程已确认（ADR-001），JWT 已确认独立（ADR-002），支付/微信已确认独立（ADR-003），工程按 mall 模板复制（ADR-004），其余主题延期（ADR-005），G6 Draft 已生成（ADR-006），G6 五份已批准（ADR-040），技术模块按能力域切（ADR-007），admin/merchant 只作后台暴露面（ADR-008），商品一个能力域两种流程（ADR-009），交易一个能力域两种支付通道（ADR-049），拼团秒杀独立能力域（ADR-011），用户与认证会话两个能力域（ADR-012），业态树与入驻两个能力域（ADR-013），履约独立能力域（ADR-014），推广独立能力域且本期只保留现状（ADR-015），平台运营独立能力域且本期只保留 banner（ADR-016），十个技术模块稳定 ID 已冻结（ADR-017），`MODULE_BOUNDARIES.md` 已 Baselined（ADR-019），G6 五份总体架构已 Baselined（ADR-040），G8 整夹已 Baselined（ADR-041），G9 三夹已 Baselined（ADR-043），G9.1 目录已生成（ADR-044），G10 批次文档 Draft（ADR-045），DEV-001 In Progress，mall-online 目录尚未创建。

## 阅读顺序

1. 本文件
2. [PROJECT_VARIABLES.md](./PROJECT_VARIABLES.md)
3. [AI_DOCUMENTATION_GUIDE.md](./AI_DOCUMENTATION_GUIDE.md)
4. [progress/PROJECT_DASHBOARD.md](./progress/PROJECT_DASHBOARD.md)
5. G5：`prd/PRODUCT_PRD.md`（Baselined）→ `prd/modules/` → `acceptance/TRACE_MATRIX.md`
6. G5.5：`ui-design/UI_SCOPE_MAP.md`（逻辑范围；不生成 UI_SPEC）
7. G6：`decisions/ADR-001.md`～`ADR-006.md`、`ADR-040.md`；`architecture/` 五份 **Baselined**
8. G7：`decisions/ADR-007.md`～`ADR-019.md`；`architecture/MODULE_BOUNDARIES.md`（**Baselined**）
9. G8：`decisions/ADR-020.md`～`ADR-039.md`、`ADR-041.md`；十份设计与整夹均 **Baselined**
10. G9：`decisions/ADR-042.md`、`ADR-043.md`；`api/` `database/` `standards/` 均为 **Baselined**
11. G9.1：`decisions/ADR-044.md`；`ui-design/products/` 六个真实前端目录（非正式 UI_SPEC）
12. G10：`decisions/ADR-045.md`；`delivery/DEVELOPMENT_BATCHES.md` 为 **Draft**（11 批 Planned；不是 Ready）

## 目录职责

| 目录 | 职责 | 当前内容 |
|---|---|---|
| `sources/` | 原始资料与来源登记 | 已冻结 BATCH-001 + BATCH-002 |
| `baseline/` | PRD 前的来源和决策基线 | DEC-001～020 已应用 |
| `prd/` | 产品需求唯一真源 | Baselined v0.1.5 |
| `acceptance/` | 验收和追踪 | TRACE / OPEN_ITEMS Baselined |
| `architecture/` | 总体技术架构 | G6 五份 **Baselined**；G7 `MODULE_BOUNDARIES.md` **Baselined** |
| `design/` | 模块详细技术设计 | 十份与整夹均 **Baselined**（ADR-041） |
| `api/` | API 契约唯一真源 | G9 **Baselined**（ADR-043） |
| `database/` | 数据模型和迁移唯一真源 | G9 **Baselined**（ADR-043） |
| `standards/` | 工程和编码规范 | G9 **Baselined**（ADR-043） |
| `ui-design/` | UI 逻辑范围与应用目录 | G5.5 逻辑范围；G9.1 六个 slug 已映射；本期不启用 UI_SPEC |
| `decisions/` | ADR | ADR-001～048 已应用 |
| `changes/` | 需求变更 CR | CR-001～005 已应用 |
| `progress/` | 进度、日志、交接 | 看板 72%；开发执行 0% |
| `delivery/` | 开发批次和发布 | G10 Draft；DEV-001/002 In Progress；其余 Planned |
| `operations/` | 上线后运维 | 未生成 |
| `iteration-suggestions/` | 扩展优化建议（非本期必做） | 仅预留入口 |
| `templates/` | 通用文档模板 | G0 模板 |

## 下一步

CODE-GATE=A 已应用（ADR-048）。`ALLOW_CODE_CHANGES=true`。DEV-004 overlay 第 36A 节已收口，不要自动开下一批。一组最多 5 题；现码能收口则自决。mall-online 本机 8035、众享源品 - 在线商城 H5 8036 已建（DEC-049）。待配置不得编造。升 Ready DEV-008/011 或改 `admin_menu` 前按 DEC-031。大面积推倒必须先问。

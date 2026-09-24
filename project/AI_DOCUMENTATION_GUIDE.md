# AI 文档生产规则

| 字段 | 值 |
|---|---|
| 文档名称 | AI 文档生产规则 |
| 文档编号 | DOC-G0-GUIDE |
| 版本 | 0.0.0 |
| 状态 | Draft |
| 负责人 | TBD |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-18 |
| 关联来源 | docs/governance/common_prd_v3.1 |
| 关联需求 | 无 |
| 关联决策 | 无 |
| 适用版本 | 文档体系 v0.0.0；治理模板 v3.1.15 |
| 替代文档 | 无 |

本文件约束后续 AI 如何生产本项目文档。它不是 PRD，也不是已批准业务规则。

## 1. 必须遵循的规范

1. `docs/governance/common_prd_v3.1/通用文档提示词v3.1.md` 主提示词全文。
2. `docs/governance/common_prd_v3.1/通用文档提示词v3.1完整使用说明.md` 阶段门禁和第 2A 节知情决策协议。
3. 本仓库 `docs/project/PROJECT_VARIABLES.md` 中的项目变量。

每次只执行一个明确阶段。未经用户明确批准不得跨越阶段门槛。启用 G9.5 时禁止跳步：anydesign → 令牌确认 → 第 28A 节 Draft → 第 29 节批准 → 点名换皮；用户预定页只记 Partial。G9.5 每步收工必须报当前节、下一节口令、禁止说成什么。用户已授权：流程口令按看板推荐路径自动执行；遇门禁停止并给出下一步提示词；遇知情决策停止，只在当前会话窗口正文提问（禁止弹框/问卷卡；须含背景、方案对比、推荐理由、开发技术决策清单和生动例子），等待文字选择。业务问题按四个业态分别考虑；不确定就问用户，不从现码单树推断分业态显隐。升 Ready DEV-008/011 或改平台菜单时按 DEC-031 落地，不必再整表点名（`progress/LOOP_GAPS.md`）。开发须对齐平台与商户菜单，不能闭环的记入该文件。**DEC-042：一组最多 5 题；现码能收口则自决。** 大面积推倒必须先问。用户意见先评判再采纳或退回知情决策；不过度设计、收口边界（见 `PROJECT_VARIABLES` 第 16 条）。

## 2. 文档真源

| 类型 | 唯一真源 | 当前状态 |
|---|---|---|
| 业务需求 | `prd/` | Baselined v0.1.5 |
| API | `api/` | G9 Baselined（ADR-043 / ADR-047） |
| 数据 | `database/` | G9 Baselined（ADR-043 / ADR-047） |
| 工程规范 | `standards/` | G9 Baselined（ADR-043 / ADR-047） |
| UI 规范 | `ui-design/` | 源品 UI_SPEC 0.1.5 Approved Partial（含附近列表）；Contract 0.1.5；底栏/首页/分类已点名换皮；附近换皮/32A 须另开口令；其它应用占位 |
| 文档进度 | `progress/PROGRESS_REGISTER.yaml` | 文档进度 72% |
| 项目变量 | `PROJECT_VARIABLES.md` | G0 Draft |

## 3. 工作边界

1. 文档阶段默认只能修改 `docs/project/`。已打开改代码后，**仅 Ready 批次**可改业务代码、配置和 `deploy/sql`。
2. `ALLOW_CODE_CHANGES=true`（ADR-048）。**DEC-042：一组最多 5 题；现码能收口则自决。** R1～R7 已收口，DEV-003 可开工。mall-online / h5-online 已建（DEC-049），不要再当「尚未创建」。不改 `admin_menu`（除非该批点名）。大面积推倒必须先问。
3. 原始资料只能登记和归档，不得改写原件。
4. 不得把当前代码行为自动视为未来需求；`CURRENT_BASELINE` 只用于区分现状、目标和差距。
5. 未知信息使用 `TBD`，不得虚构。
6. PRD 不写数据库表、类名、函数名和框架实现。
7. 不得记录密码、Token、私钥或生产凭证。
8. 所有选择、裁决、批准和状态变更走 `INFORMED_DECISION_PROTOCOL`：只在当前会话窗口正文解释（禁止弹框）→ 用户文字初选 → 影响复述 → 二次确认 → 受控应用。初次选择不是确认。`INFORMED_REVIEW` 必须含决策背景、生动例子、方案对比、推荐理由、开发技术决策清单。功能描述按第 2A 节人话 6 问。

## 4. G0 工作约束（待资料归纳，非 DEC）

1. 基于现码迭代，不超纲设计；能完成需求为主。
2. 正式 UI 规范按应用分闸（UI-DEC-001）：总闸 true，仅 `gongyi_online`。其它应用 `UI_CONSTRAINT_MODE=NONE`，跳过 G9.5。源品占位 UI_SPEC 未经批准不能当验收。视觉修复循环可选、未点名不得执行，不计文档进度分母。
3. 表结构不大面积破坏；必要时可增改字段、增表、删无用表。该条在进入技术设计前仍须按高影响决策确认。
4. `docs/project/` 是以后需求迭代的维护真源，需与后续需求同步。
5. `docs/temp/` 只读参考，不作为维护文档迭代。
6. `nunu-go-api/docs` 已脱节，只作日后清理候选，不以它为真源。
7. 忽略且不做任何考虑：`nunu-go-api/mall-uniapp`、仓库根目录 `admin/`、`uni-app/`、`niucloud`。
8. 本期范围已随 PRD Draft 写明（不另开 DEC）：不做外卖；在线商城拼团秒杀不做；众享源品 - 在线商城本期不做 AI 和发现对接。
9. 扩展优化写入 `iteration-suggestions/`，不进入本期必做范围；G0 只预留目录。
10. 升 Ready DEV-008/011 或改平台菜单时按 DEC-031 落地，不必再整表点名；平台与商户菜单能对齐的要对齐；不能闭环记 `progress/LOOP_GAPS.md`。
11. **DEC-042**：一组最多 5 题；现码能收口则自决事后告知；盘点必须列清问/自决/后置。假数据竣工清理 SQL 不带编号。

## 5. 阶段门禁摘要

```text
G0 文档初始化
G1 资料投放
G2 来源和决策基线
G3 PRD 准入审计
G4 PRD Draft
G5 PRD 评审和批准     ← 已完成（Baselined；TECH_BASELINE=v0.1.5）
G5.5 UI 逻辑范围同步   ← 已完成（生成 UI_SCOPE_MAP，不生成 UI_SPEC）
G6 总体技术架构        ← 已完成（五份 Baselined；ADR-040）
G7 技术模块划分        ← 已完成（MODULE_BOUNDARIES Baselined；ADR-007～019）
G8 模块详细技术设计    ← 已完成（十份 Baselined；整夹 Baselined；ADR-041）
G9 API、数据和编码规范    ← 已完成（三夹 Baselined；ADR-043）
G9.1 正式 UI 应用目录    ← 已完成（只目录/映射；不启用正式 UI_SPEC；ADR-044）
G9.5 可选 UI 规范      （源品已分闸 UI-DEC-001；尚无 Draft/Approved UI_SPEC；其它应用仍跳过）
G10 开发批次            ← Draft（ADR-045；DEV-001/002 In Progress；其余 Planned）
G11 开发、测试、发布和维护  ← 已进入（DEV-001/002 In Progress）
视觉修复循环            （独立手续，不占 G 号；目录已备，未跑）
```

资料范围未冻结时，文档总进度显示 `N/A`。存在 P0/P1 时不得进入下一必经阶段。

## 6. 编号规则

- `SRC-REQ-XXX` 需求资料
- `SRC-UI-XXX` 设计图和 UI 素材
- `SRC-STD-XXX` 设计系统和工程规范
- `SRC-LEGACY-XXX` 旧版资料
- `SRC-CODE-XXX` 代码现状
- `SRC-CHANGE-XXX` 需求变更来源
- `DEC-XXX` 业务决策
- `UI-DEC-XXX` 纯 UI 决策
- `CONFLICT-XXX` 业务冲突
- `UI-CONFLICT-XXX` UI 冲突
- `QUESTION-XXX` 待确认问题
- `CR-XXX` 需求变更
- `ADR-XXX` 架构决策
- `MXX` PRD 模块
- `REQ-XXX` 正式需求
- `TD-XXX` 技术设计
- `BATCH-XXX` 开发批次
- `TEST-XXX` 测试用例
- `WORKLOG-XXX` 工作日志
- `HANDOVER-XXX` 人员交接

## 7. 结论标签

已确认 / 现状 / 候选 / 推断 / 待确认 / 已废弃

不得把「候选」「推断」「待确认」写成「已确认」。

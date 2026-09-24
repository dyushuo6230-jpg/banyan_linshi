# 项目变量

| 字段 | 值 |
|---|---|
| 文档名称 | 项目变量 |
| 文档编号 | DOC-G0-VARS |
| 版本 | 0.0.0 |
| 状态 | Draft |
| 负责人 | TBD |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-18（UI-DEC-001：仅源品分闸） |
| 关联来源 | G0 用户初始化口令 |
| 关联需求 | 无 |
| 关联决策 | UI-DEC-001 |
| 适用版本 | 文档体系 v0.0.0 |
| 替代文档 | 无 |

本文件只登记项目元信息。未列出项保持 `TBD`。不得把本文件中的工作约束写成已批准业务规则。

## 已确定变量

```text
PROJECT_NAME=多业态租户入驻系统
PROJECT_TYPE=已有项目功能扩展（多终端、多业态本地生活 + 在线商城）
PROJECT_GOAL=基于当前分支现码做多业态迭代，并重新梳理一套可长期维护的 PRD；现有功能与本期迭代功能写入同一套文档；扩展优化类需求另出独立迭代建议文档，不进入本期必做范围
TARGET_USERS=平台运营、入驻租户（餐饮/美发/商超/在线商城供应商）、众享营销 - 本地生活用户、众享源品 - 在线商城用户、推广员
TARGET_PLATFORMS=平台后台；租户后台；租户入驻 H5；众享营销 - 本地生活；众享源品 - 在线商城 C 端（iOS / 安卓 / 鸿蒙 / 小程序 / H5）
PROJECT_STAGE=IMPLEMENTATION
REPOSITORY_ROLE=CURRENT_BASELINE
DOC_ROOT=docs/project/
SOURCE_PATH=docs/project/sources/inbox/
LANGUAGE=中文，技术标识和 API 字段使用英文
TECH_STACK=沿用当前仓库现有技术栈与目录（nunu-go-api 的 admin / mall / merchant / mall-online / h5 / h5-online，以及 go-uni-app、go-uni-app-online、各自配套后台前端）。mall-online 本机 8035；众享源品 - 在线商城 H5 本机 8036、整包 embed（DEC-049）。本期不大改技术架构和目录规范，技术文档按现有架构生成
TARGET_RELEASE=TBD
PRODUCT_OWNER=TBD
TECH_OWNER=TBD
PROJECT_OWNER=TBD
BUSINESS_TIMEZONE=Asia/Shanghai
ALLOW_CODE_CHANGES=true
ENABLE_PROGRESS_TRACKING=true
ENABLE_WORKLOG=true
ENABLE_HANDOVER=true
INFORMED_DECISION_MODE=MANDATORY
ARCHITECTURE_PARTICIPATION_MODE=MANDATORY
ARCHITECTURE_DECISION_REVIEW_STATUS=COMPLETED
ARCHITECTURE_DECISION_APPLY_STATUS=COMPLETED
ALLOW_ARCHITECTURE_DRAFT_WITH_TBD=false
MODULE_BOUNDARY_PARTICIPATION_MODE=INHERIT
MODULE_BOUNDARY_DECISION_REVIEW_STATUS=COMPLETED
MODULE_BOUNDARY_DECISION_APPLY_STATUS=COMPLETED
ALLOW_MODULE_BOUNDARIES_DRAFT_WITH_TBD=false
MODULE_DESIGN_PARTICIPATION_MODE=INHERIT
MODULE_DESIGN_FIRST_MODULE=tree
MODULE_DESIGN_CURRENT_MODULE=platform-ops
GENERATE_UI_REFERENCE_TREE=true
SYNC_UI_TREE_WITH_PRD=true
GENERATE_UI_APPLICATION_TREE=true
UI_APPLICATION_DIRECTORY_SOURCE=PROJECT_STRUCTURE
ENABLE_UI_SPEC_GENERATION=true
UI_SPEC_ENABLED_APPLICATIONS=gongyi_online
GENERATE_EFFECTIVE_UI_CONTRACT=true
UI_CONSTRAINT_MODE=NONE
UI_SPEC_DEFAULT_STATUS=Draft
ANYDESIGN_SKILL_PATH=.cursor/skills/anydesign/
ANYDESIGN_TOOLS_PATH=tools/anydesign/
VISUAL_LOOP_SKILL_PATH=.cursor/skills/visual-repair-loop/
VISUAL_LOOP_DEFAULT_VIEWPORT=390x844
VISUAL_LOOP_DIFF_THRESHOLD=关键尺寸±1px；颜色必须匹配令牌或点名设计图主色
VISUAL_LOOP_RUNS_DIR=docs/project/ui-design/visual-loop/LOOP_RUNS/
```

## G0 工作约束（非已批准业务规则）

以下条目来自 G0 初始化口令，状态为**工作约束 / 待 G1 资料归纳**，不是 DEC、不是 Approved PRD。

1. 基于现码迭代，不超纲设计；能完成需求为主。
2. 正式 UI 规范按应用分闸。已确认 `UI-SPEC-SCOPE-001=A` / UI-DEC-001：总闸 `ENABLE_UI_SPEC_GENERATION=true`，分闸仅 `gongyi_online`。源品 `UI_SPEC.md` 0.1.5 **Approved Partial**（含附近列表）。点名换皮底栏+首页+分类已开工；附近入 Partial 后换皮/32A 须另开口令（Contract：`delivery/ui-contracts/gongyi_online-partial-001/` **0.1.5**）。全局 `UI_CONSTRAINT_MODE` 仍为 NONE。其它应用仍关。视觉修复循环可点名。打开或扩大分闸须再走第 23A 节。
3. 表结构不大面积破坏；必要时可增改字段、增表、删无用表。若认为必须大面积推倒（整模块重写、换表当局、另起进程替代现码主路径）：先停、问用户、说明为什么小改闭不了口；无文字同意不做（DEC-041）。
4. 新文档作为以后需求迭代的维护真源，需与后续需求同步。
5. `docs/temp` 及其中历史指导文档只读参考，不作为项目维护文档迭代。
6. `nunu-go-api/docs` 已严重脱节，只作日后清理候选，不以它为真源。
7. 以下目录全部忽略、不做任何考虑，后期可能删除：`nunu-go-api/mall-uniapp`、仓库根目录 `admin/`、`uni-app/`、`niucloud`。
8. 本期范围已随 PRD Draft 写明（不另开 DEC）：不做外卖；在线商城拼团秒杀不做；众享源品 - 在线商城本期不做 AI 和发现对接。
9. 扩展开优化放到独立「迭代建议」文档；G0 只预留 `iteration-suggestions/`，不展开内容。
10. 流程步骤：文档阶段按看板上的「下一步」一项执行。**禁止默认批准**：Approved / Baselined / 第 15 节必须用户在本会话书面确认后才做。**禁止默认开工**：第 35 节必须用户点名批次后才改业务代码；未发开工口令不得开发。遇到阶段门禁或知情决策必须停止。知情决策只在**当前会话窗口正文**提问（禁止弹框/问卷卡）。初次选择不写 DEC，不改正式结论。
11. 业务与菜单相关问题必须从**四个业态**分别考虑（餐饮 / 美发 / 商超 / 在线商城）。现码单树不能当成四套已拆好的显隐。吃不准就问用户，不得按「看起来像本地生活/像商城」自行推断。
12. 平台侧栏已点名（DEC-031 v1.1 / LOOP-Q4=A）。升 Ready DEV-008 或 DEV-011 或 DEV-013、以及任何要改平台 `admin_menu` 时，按该表落地，不必再整表重问；若改表须新 DEC。DEV-002 不改平台菜单。改库默认：DEV-008 删秒杀管理/拼团审核；DEV-011 补通道用量；DEV-013 加商城秒杀/拼团与板块。真源：`progress/LOOP_GAPS.md` REMIND-PLATFORM-MENU。
13. 后续开发：平台菜单与商户菜单能对齐的功能必须对齐；须考虑整体闭环。不能闭环的写入 `progress/LOOP_GAPS.md`，告知用户，不得假装已闭环。
14. **DEC-042 / PROC-004=A**：一组最多 5 题；现码能收口则自决事后告知；盘点必须一次列清问/自决/后置。假数据竣工后给清单和不带编号的清理 SQL。R1～R7 已收口（DEC-043/044），DEV-003 可开工。R8 留 DEV-009。大面积推倒必须先问。待配置不得编造。不创建 mall-online。不改 `admin_menu`。
15. 决策后须保证流程能闭环、模块够用。不过度设计；先上线能用。「三端」是笼统说法；任何决策必须按多租户、四业态分别考虑（各店众享营销 - 本地生活/用户池 vs 多家在线商城供应商 + 众享源品 - 在线商城用户池），不能收成一个用户、一个租户、一个平台。
16. 助手须以产品、架构、开发、测试、项目经理标准工作。用户的意见和决策先判断是否合理：合理则采纳；会撑破本期边界或与已确认口径冲突则指出问题并走知情决策，不得直接照收。不过度设计时必须收口边界。真源：`.cursor/rules/collaboration-judgment.mdc`。
17. **落地标准（DEC-029 v1.3.0）：** 众享源品 - 在线商城 C 端现用页已出现的能力必须接到 mall-online 并能办完，或按已确认表藏掉。不得再用「仅页面前端接口先做到打包/申请支付够用」当半成品借口。真扣款仍不要求（DEC-050）。其余所有功能必须开发完成，能闭口就闭口。不得以商城页面未完为由把平台/租户/本地生活/入驻做成半成品。众享源品 - 在线商城多端同一套代码，有差异必须条件编译。鸿蒙非本期必打。

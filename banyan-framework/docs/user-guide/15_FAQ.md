# FAQ（常见问题）

> 关键术语：WebUI（网页控制界面：辅助观察与受限操作入口）；Workflow（工作流：按规则组织任务步骤）；Work Mode（工作模式：按风险调整检查深度）；Change（变更：一组有范围和状态的拟议修改）；Project Instance（项目实例：连接项目来源、变量和 Provider 的状态集合）；Shadow Pilot（影子试点：尚未替代正式真相的受控投影）；Final Activation（最终激活：正式启用 Project Instance 的独立治理动作）；Freshness（时效状态：内容是否仍与当前有效来源一致）。

## 这篇解决什么问题

集中回答普通开发者最常遇到的 Banyan 使用问题。

## 什么时候需要看

遇到状态、证据、文档类型、多人协作、Git 或 Project Instance 疑问时。

## 核心概念

Banyan 当前由已实现的受限 Runtime / Adapter surface、frozen contracts、Pilot 和规划能力共同组成。Implementation Status（实现状态：说明能力当前是已实现、合同冻结、试点、规划、未实现或阻塞）必须逐项判断。

## 推荐操作方式

先从问题标题定位答案；需要精确枚举或边界时继续打开对应 Reference。

## 常见问题

### 我只会在 Cursor / Codex 输入需求，可以吗？

可以。自然语言编辑器是主入口。请说清目标、范围、材料、约束、期望输出和是否允许修改。当前 Adapter 不是完整 autonomous workflow，复杂任务最好明确“先规划 / 再施工”。

### Banyan 会自动决定所有事情吗？

不会。Adaptive Workflow contract 已冻结，但自动 router / executor 尚未实现；高影响、Authority 不明或安全相关事项仍需人决定。

### 为什么有时让我提供证据？

Evidence（证据：支持判断的可核验材料）用于确认事实、Freshness、影响和验证结果。缺关键证据时继续可能产生错误或越权。

### 为什么会停在 `NEEDS_INPUT`？

它表示缺少可补充输入，例如有效 Work Mode、某项 precondition 或 identity 信息。它与 Policy / safety violation 导致的 `BLOCK` 不同。

### 为什么有些能力写在文档里但不能执行？

有些内容是 `FROZEN_CONTRACT`，只表示语义和边界已冻结；executor 或 Provider 仍可能 `NOT_IMPLEMENTED`。35 个 `CAP-*` 就是 Capability Contract，不是 35 个 Skill。

### WebUI Help Center 在哪里？

当前没有。`/help` 为 `NOT_IMPLEMENTED`，计划在 D7 作为 Documentation UX Enhancement 建设。现在从仓库中的 `banyan-framework/docs/README.md` 阅读文档。

### 我需要记住所有 ID 吗？

不需要。日常只需描述目标和范围。需要对账、自动化或跨文档引用时，再查 ID Reference；不要自行发明 ID。

### 多人开发怎么避免冲突？

按模块、目录、独立需求或 Change 隔离；使用 Draft Change Package，Pull Latest 后 Reconcile，再 Review 和 Human Decision。Canonical Apply 是治理流程，当前没有一键 API。

### `.banyan` 是什么？

它是 Project Instance（项目实例：连接项目来源、变量和 Provider 的状态集合）的 Shadow Pilot。它不是真正的业务 Canonical truth，也没有替代现有项目布局。

### Framework 发布后项目是不是自动激活？

不是。Framework `v1.10-additive.1` 是 additive release；`.banyan` Final Activation 仍为 `NOT_AUTHORIZED`，并且 `CON-002` 仍需 Human Project Authority。

### 为什么不能直接 `git add .`？

工作树可能同时包含 `INCOMPLETE`、`UNRELATED`、`LOCAL_ONLY` 或 `SECRET_RISK`。盲目 stage 会混入不应提交的内容；当前 Git Adapter 也明确禁止 `git add .`、`git add -A` 和 `git add --all`。

### PRD / UI_SPEC / ADR / DEC 分别是什么？

- PRD（Product Requirements Document，产品需求文档）：产品/业务需求 Canonical truth。
- UI_SPEC（User Interface Specification，界面规格）：批准后且限定范围的 UI contract projection。
- ADR（Architecture Decision Record，架构决策记录）：记录架构选择、理由和影响。
- DEC（Decision Record，决策记录）：记录一般决策、理由、范围和确认。

Design Source 是 Evidence，不自动成为 PRD 或已批准 UI_SPEC。

## 自然语言示例

> 我看到文档里写了 Canonical Apply。请先告诉我它是 IMPLEMENTED 还是 FROZEN_CONTRACT，并指出当前可执行边界，不要假设 API 已存在。

## 当前实现状态

本 FAQ 描述 D0/D1 已确认事实。完整自然语言自动编排、Adaptive Workflow executor、Canonical Apply executable API 和 WebUI `/help` 均未实现；`.banyan` 仍是 Pilot。

## 常见误区

- “写在文档里”不等于“已经可执行”。
- “已发布”不等于“项目已激活”。
- “有证据”不等于“有授权”。
- “有角色”不等于“有权限”。

## 相关 Reference

- [中英双语术语表](../reference/GLOSSARY_BILINGUAL.md)
- [实现状态参考](../reference/IMPLEMENTATION_STATUS_REFERENCE.md)
- [关键文档类型参考](../reference/KEY_DOCUMENT_TYPES_REFERENCE.md)
- [工作流参考](../reference/WORKFLOW_REFERENCE.md)

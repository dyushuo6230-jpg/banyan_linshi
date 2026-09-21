# Banyan 如何自动选择工作流

> 关键术语：Workflow（工作流：按规则组织任务步骤）；Adapter（适配器：转换不同入口的请求格式）；Evidence（证据：支持判断的可核验材料）；Decision（决策：需要人作出的明确选择）；Trace（追踪记录：动作和结果的审计记录）。

## 这篇解决什么问题

准确说明 Adaptive Workflow 的目标设计、当前实现状态，以及今天怎样人工给出足够明确的工作模式。

## 什么时候需要看

你希望 Banyan 根据任务风险自动决定分析深度和门禁，或看到 Workflow contract 后想确认它是否已经可运行时。

## 核心概念

Adaptive Workflow（自适应工作流：根据任务、风险、范围和治理状态选择步骤的策略）合同 `banyan.workflow.adaptive.v1` 已冻结。它定义了输入和路由输出，但自动 router / executor 尚未实现。

Work Mode（工作模式：按风险和范围调整检查深度）有 `LIGHT / STANDARD / FULL`。模式不能降低风险类别、Decision Level 或安全责任。

## 推荐操作方式

在自动路由实现前，直接告诉编辑器你希望怎样工作：

- 低风险查询：“只读检查并给简洁结论”。
- 普通修改：“先规划，确认后施工，完成后验证”。
- 高风险或跨边界：“完整盘点 Evidence、Authority、影响、rollback 和需要的人类决策，不满足就停止”。

看到 `BLOCK` 时处理安全或策略问题；看到 `NEEDS_INPUT` 时补充可解决的输入。不要用 LIGHT 绕过 Gate（门禁：条件不足时阻止下一步的检查点）。

## 自然语言示例

> 这是跨前后端的改动，请按 FULL 深度先分析。列出 required gates、Evidence、Human Decision 和 blocked actions，不要自动施工。

## 当前实现状态

- Adaptive Workflow contract：`FROZEN_CONTRACT`。
- 自动 router / executor：`NOT_IMPLEMENTED`。
- 当前真实 request flow：Editor → Adapter → Control Plane → Runtime API → Policy → Evidence Trace，受限部分为 `IMPLEMENTED`。
- 七步目标用户旅程不是 Runtime 自动状态机。

## 常见误区

- “合同已冻结”不等于“自动路由已经上线”。
- UI 展示某个状态不表示 Workflow 已执行后续动作。
- 35 个 `CAP-*` 是 Capability Contract，不是自动装载的 35 个 Skill。

## 相关 Reference

- [工作流参考](../reference/WORKFLOW_REFERENCE.md)
- [实现状态参考](../reference/IMPLEMENTATION_STATUS_REFERENCE.md)
- [状态与枚举参考](../reference/STATUS_AND_ENUM_REFERENCE.md)

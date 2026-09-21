# Change（变更）与 Decision（决策）使用说明

> 关键术语：Evidence（证据：支持判断的可核验材料）；Freshness（时效状态：内容是否仍与当前有效来源一致）。

## 这篇解决什么问题

区分“提出一组变更”“作出选择”“授予执行权限”和“把结果应用到正式来源”。

## 什么时候需要看

需求会改变 PRD、UI_SPEC、技术合同或其他 Canonical source，或者存在多个方案需要人选择时。

## 核心概念

Change（变更：具有稳定 ID、状态和范围的一组拟议修改）管理提议的生命周期。Decision（决策：对选项、影响和范围作出的明确选择）记录人的选择。Authorization（授权：允许特定动作作用于特定目标的有效依据）控制能否执行。

Canonical Apply（正式真相应用：经预览、决策、授权和验证后应用到权威来源）合同已冻结，但当前 Runtime / Control Plane 没有 executable API。

## 推荐操作方式

1. 给 Change 一个稳定 `change_id`，说明来源、范围和关联任务。
2. 在 Draft 阶段收集影响、Evidence、候选方案和未知项。
3. 需要选择时单独形成 Decision，记录选项、理由、适用范围和确认。
4. 再检查 Authorization 是否绑定到正确 action、target 和 scope。
5. 通过预览、Freshness、引用、冲突、checkpoint 和 rollback 检查。
6. 当前没有一键 Canonical Apply API；需要把它视为受治理流程，不得声称自动执行。

## 自然语言示例

> 为这个需求建立 Change 分析：列出受影响的 PRD/UI_SPEC、Evidence、冲突和决策项。只准备 Draft Change Package，不应用到 Canonical source。

> 我选择方案 B。请记录 Decision 的影响和适用范围，但不要把这个选择解释为 Git 或 Canonical Apply 的执行授权。

## 当前实现状态

Stage 06 Change lifecycle 与 Canonical Apply state contract 是 `FROZEN_CONTRACT`。Stage 06 当时最大状态为 `APPLY_PLANNED`；当前 Runtime 只有 plan / dry-run 等受限 surface，没有 Canonical Apply executable API。

## 常见误区

- Provider 的 change ID 不能替代 Banyan `change_id`。
- Draft、Review 或 Decision 不自动成为 Authorization。
- 文件更新时间或 Provider status 不会自动推动 Change 状态。
- `AUTHORIZED` 这一 frozen state 存在，不代表当前 API 能执行 Apply。

## 相关 Reference

- [关键文档类型参考](../reference/KEY_DOCUMENT_TYPES_REFERENCE.md)
- [工作流参考](../reference/WORKFLOW_REFERENCE.md)
- [关键 ID 与变量参考](../reference/KEY_IDS_AND_VARIABLES_REFERENCE.md)

# 在 Codex / Cursor 中使用 Banyan

> 关键术语：Authorization（授权：允许特定动作作用于特定目标的有效依据）；Evidence（证据：支持判断的可核验材料）；Permission（权限判定：Runtime 根据 Policy 给出的结论）；Trace（追踪记录：动作及结果的审计记录）。

## 这篇解决什么问题

说明自然语言编辑器入口当前能做什么、不能做什么，以及怎样给出可执行的清晰请求。

## 什么时候需要看

你主要在 Codex 或 Cursor 中输入需求，想知道 Adapter（适配器：把编辑器请求转换为统一格式）的真实能力边界时。

## 核心概念

当前链路是 `Editor → Adapter → Control Plane（控制面：转发请求并展示结果） → Runtime API → Policy → Evidence Trace`。Cursor、Codex 与 Generic Editor 使用不同请求形状，但进入同一 Runtime，不各自拥有一套权限逻辑。

## 推荐操作方式

1. 用自然语言提供目标、范围、材料、约束、输出和修改许可。
2. 明确当前阶段：“只读分析”“只给计划”“允许施工”或“只生成提交计划”。
3. 要求它报告实际执行结果和未处理项。
4. 对写入、高风险和 Governance（治理）决定给出目标绑定的明确 Authorization。

当前 Editor Adapter 支持的 action 是：`runtime_status`、`project_safety`、`preflight`、`commit_plan`、`commit_dry_run`、`trace`、`provenance`。

## 自然语言示例

> 只读检查当前项目安全状态和相关来源，不改文件。给出事实、未知项和下一步建议。

> 先对这个改动做 preflight 和 commit plan。不要执行 Git mutation，不要读取 Secret body。

## 当前实现状态

Cursor、Codex、Generic Editor Adapter 已实现并通过兼容性验证。它们不是完整 autonomous workflow（自主工作流），不支持直接 Git mutation、commit execute、Canonical write、protected write execute、activate、identity write 或 secret body read。

## 常见误区

- 编辑器里的普通确认不自动成为 Runtime Authorization。
- Adapter 返回 `OK` 表示请求处理成功，不表示目标动作已执行。
- Codex 与 Cursor Adapter 不拥有 Canonical truth 或 Permission Policy。

## 相关 Reference

- [工作流参考](../reference/WORKFLOW_REFERENCE.md)
- [实现状态参考](../reference/IMPLEMENTATION_STATUS_REFERENCE.md)
- [角色参考](../reference/ROLE_REFERENCE.md)
- 下一篇：[如何向 Banyan 描述需求](04_如何向Banyan描述需求.md)

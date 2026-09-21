# 权限、Gate（门禁）与安全

> 关键术语：WebUI（网页控制界面：展示 Runtime 结果的辅助入口）；Adapter（适配器：转换不同入口的请求格式）；Decision（决策：对选项作出的明确选择）；Work Mode（工作模式：按风险和范围调整检查深度）。

## 这篇解决什么问题

读懂为什么 Banyan 有时允许、有时阻塞、有时要求补输入，并避免把角色、证据或 UI 操作误当作授权。

## 什么时候需要看

看到 `ALLOW`、`BLOCK`、`NEEDS_INPUT`，准备写入、提交、外部动作或处理 Secret 时。

## 核心概念

- Permission（权限判定：Runtime 根据 Policy 对动作给出的结论）。
- Authorization（授权：允许特定动作作用于特定目标和范围的有效依据）。
- Gate（门禁：条件不满足时阻止进入下一步的检查点）。
- Preflight（执行前预检：正式动作前检查风险、权限、前置条件和 Evidence）。
- Evidence（证据：支持判断的可核验材料）。
- Trace（追踪记录：记录动作、结果和证据关系）。

Permission Result 为 `ALLOW / BLOCK / NEEDS_INPUT / NOT_APPLICABLE`。`BLOCK` 通常表示安全或 Policy 问题；`NEEDS_INPUT` 表示缺少可补充输入。两者不能互换。

## 推荐操作方式

1. 先 Preflight，再决定是否进入动作。
2. `NEEDS_INPUT` 时只补所需的可验证输入，不猜默认值。
3. `BLOCK` 时处理 blocker，不能通过改措辞或换入口绕过。
4. 写入授权要绑定 action、target、scope 和限制。
5. Secret 只处理允许的 metadata，不复制、预览或展示 body。
6. 保留 Trace，但不把 Trace 当作 Authorization。

## 自然语言示例

> 对这个动作做 Preflight。请分别说明 Risk Class、Decision Level、Permission Result、缺少的 preconditions 和 reason codes；不要执行动作。

## 当前实现状态

Runtime permission evaluation 与 Preflight 已实现，并采用 fail-closed。未知 action 按 `PROTECTED_WRITE` 处理并阻塞。当前项目 mutation 禁用，commit 仅 dry-run；isolated fixture 执行也必须通过 Gate。

## 常见误区

- `ALLOW != EXECUTED`。
- `Evidence != Authorization`。
- WebUI confirmation、Adapter request、Trace、Commit Plan、Role 和 Git Identity 都不单独构成 Authorization。
- `Role != Permission != Git Identity != Authentication`。
- Work Mode 不能降低 Risk Class 或 Decision Level。

## 相关 Reference

- [状态与枚举参考](../reference/STATUS_AND_ENUM_REFERENCE.md)
- [角色参考](../reference/ROLE_REFERENCE.md)
- [实现状态参考](../reference/IMPLEMENTATION_STATUS_REFERENCE.md)

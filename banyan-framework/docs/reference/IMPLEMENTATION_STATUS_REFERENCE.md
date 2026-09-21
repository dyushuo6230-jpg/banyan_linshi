# Implementation Status Reference

以下标签是 Documentation status labels（文档展示状态标签），用于统一说明“现在做到哪一步”。它们不是新增 Runtime enum，不能作为 API 返回值或状态机输入。

## 标签

### `IMPLEMENTED`

当前 implementation source 中存在，并可在已声明边界内调用。它不表示没有安全限制，也不表示调用已实际发生。

### `FROZEN_CONTRACT`

结构、语义或门禁合同已冻结，可作为文档依据；executor、Provider 或完整产品入口可能仍不存在。`FROZEN_CONTRACT != IMPLEMENTED`。

### `PILOT`

已建立受控试点或影子投影，但尚未 Final Activation，也不能替代 Canonical truth。

### `PLANNED`

已进入文档或路线规划，尚不能作为当前能力使用。

### `NOT_IMPLEMENTED`

当前实现没有对应 executor、API、页面或独立 schema。它可以与 `FROZEN_CONTRACT` 同时出现，例如合同已冻结而执行器未实现。

### `BLOCKED`

当前因授权、Authority、Evidence、安全条件或 Human Decision 不能进入下一状态。应同时写出实际 blocker 或 accepted state。

## D0 映射示例

- `RuntimeAPI.evaluate_action`：`IMPLEMENTED`。
- Adaptive Workflow：合同 `FROZEN_CONTRACT`；自动 router / executor `NOT_IMPLEMENTED`。
- 35 个 `CAP-*`：`FROZEN_CONTRACT`，注册表为 `FROZEN_CONTRACTS_IMPLEMENTATION_UNBOUND`。
- `.banyan`：`PILOT`，accepted state 为 `PROJECT_INSTANCE_SHADOW_PILOT`。
- WebUI `/help`：`NOT_IMPLEMENTED`；D7 规划为 `PLANNED`。
- Canonical Apply：合同 `FROZEN_CONTRACT`；Runtime / Control Plane API `NOT_IMPLEMENTED`。
- Final Activation：`BLOCKED`，实际状态 `NOT_AUTHORIZED`。

## 三个容易混淆的关系

`ALLOW != EXECUTED`：`ALLOW` 是 Permission Result。当前 `ActionResult.executed` 默认仍为 `false`，预检尤其不会执行动作。

`RELEASED != PROJECT_ACTIVATED`：Framework `v1.10-additive.1` 已发布为 additive supplement；`.banyan` 仍是 Shadow Pilot，Final Activation 未授权。

`PRESENT != CANONICAL`：文件、Trace 或 Evidence 存在，不表示它已成为 Canonical truth。Authority、scope、Freshness、approval 和 decision evidence 仍需成立。

相关事实见 [Documentation Source of Truth](../DOCUMENTATION_SOURCE_OF_TRUTH.yaml) 和[工作流参考](WORKFLOW_REFERENCE.md)。

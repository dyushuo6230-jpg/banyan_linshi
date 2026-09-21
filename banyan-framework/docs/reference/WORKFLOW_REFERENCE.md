# Workflow Reference

本页区分 frozen Workflow contract、当前实际 request flow 和文档化过程。合同状态不能替代 executor 状态。

## `banyan.workflow.adaptive.v1`

- 中文解释：自适应工作流策略，根据 task class、risk、scope、confidence、governance mode、project stage、authorization、budget 和 Change state 产生路由结果。
- 当前状态：`FROZEN_CONTRACT / NOT_IMPLEMENTED` executor；原始状态为 `FROZEN_POLICY_NOT_IMPLEMENTED`。
- 输入/步骤：9 类 routing input；输出 mode、gates、evidence、human decisions、allowed/blocked actions 和 rationale。
- 是否自动执行：否，当前没有 Framework 内完整自动 router / executor。
- 当前限制：不能声称自然语言请求会自动完成完整研发旅程。

## Stage 05 Workflow State Machine

- 中文解释：从收到请求到路由、检查、提议、确认、规划、验证、执行证据和完成的冻结状态合同。
- 当前状态：`FROZEN_CONTRACT`，部分概念由后续 Runtime surface 实现。
- 输入/步骤：`RECEIVED → ROUTED → INSPECTED → PROPOSED`，随后按门禁进入等待确认、阻塞或授权与规划；完整状态见[状态与枚举参考](STATUS_AND_ENUM_REFERENCE.md)相关合同说明。
- 是否自动执行：否，不是当前 Runtime 的完整自动状态机。
- 当前最大可达状态/限制：Stage 05 当时终态为 `READY_FOR_EXECUTOR_OR_BLOCKED`，执行 transition 当时未实现。

## Stage 06 Change Lifecycle

- 中文解释：管理 Change 从讨论、草稿、提议、评审、批准到应用、对账和归档的冻结生命周期。
- 当前状态：`FROZEN_CONTRACT`；当前 Runtime / Control Plane 没有 Canonical Apply executable API。
- 输入/步骤：稳定 Change ID、promotion precheck、review evidence、decision gate、preview、authorization、validation 和 reconciliation。
- 是否自动执行：否。
- 当前最大可达状态/限制：Stage 06 最大状态为 `APPLY_PLANNED`；当时 future executor 尚未存在。

## `current-runtime-request-flow`

- 中文解释：当前真实实现的编辑器请求链。
- 当前状态：`IMPLEMENTED`。
- 输入/步骤：`Editor → Adapter → Control Plane → Runtime API → Policy → Evidence Trace`。
- 是否自动执行：仅自动完成选定、受支持 action 的转换、派发、判定与记录；不自动编排完整需求。
- 当前限制：Editor Adapter 仅支持 `runtime_status`、`project_safety`、`preflight`、`commit_plan`、`commit_dry_run`、`trace`、`provenance`。禁止 Git mutation、commit execute、Canonical write、protected write execute、activate、identity write 和 secret body read。

## `semantic-commit-dry-run`

- 中文解释：检查工作树、形成语义提交计划、预检并演练结果的受限流程。
- 当前状态：current-project plan / dry-run 为 `IMPLEMENTED`。
- 输入/步骤：`inspect → plan_commit → preflight → dry_run → evidence`。
- 是否自动执行：可执行 plan 和 dry-run；不会在当前项目创建 commit。
- 当前限制：当前项目为 `DRY_RUN_ONLY`；真实 mutation 只允许显式 isolated fixture root 并通过 gates。Commit Plan 不是 Authorization。

## Stage 20 Upgrade Lifecycle

- 中文解释：未来升级应遵循的治理过程。
- 当前状态：`PLANNED / DOCUMENTED_PROCESS`，不是自动化 Runtime Workflow。
- 输入/步骤：`Change → Impact → Migration → Preview → Validation → Apply → Rollback → Acceptance`。
- 是否自动执行：否。
- 当前限制：不能把 `.banyan-refactor` 重新当作普通升级机制；apply、rollback 与 acceptance 仍需各自门禁和证据。

## Documentation Target User Journey

`Understand（理解） → Collect（收集） → Plan（规划） → Decide（决策） → Execute（施工） → Validate（验证） → Deliver（交付）`

这是 Documentation Target User Journey（文档目标用户旅程），用于组织后续 User Guide 和 Scenario。它当前不是已实现的 Runtime 自动编排，也不是可从 API 读取的状态机。

## Canonical Apply 边界

Canonical Apply contract 已冻结，包含 preview、impact、reference/freshness check、decision、authorization、checkpoint、post-validation、trace 与 reconciliation。当前 Runtime / Control Plane 不提供 executable API，因此任何 Workflow 文档都不得把它写成现有可调用步骤。

参见[Skill 与 Capability 参考](SKILL_REFERENCE.md)、[实现状态参考](IMPLEMENTATION_STATUS_REFERENCE.md)和[角色参考](ROLE_REFERENCE.md)。

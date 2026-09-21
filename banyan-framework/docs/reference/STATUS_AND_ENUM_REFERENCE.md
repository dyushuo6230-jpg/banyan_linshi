# Status and Enum Reference

同一个字符串可以出现在不同 schema 中。例如 Artifact、Runtime、Conflict 和 Project Instance 都可能出现 `BLOCKED`，但含义、转换条件和 owner 不同。使用枚举时必须同时写所属对象与 context。

## Contract Status

- 所属对象：frozen contract schema。
- 实际值：`DRAFT`（草拟）、`FROZEN`（已冻结）、`DEPRECATED`（不再推荐）、`SUPERSEDED`（被后继替代）、`BLOCKED`（合同推进受阻）。
- 实现性质：`FROZEN_CONTRACT`。
- 常见误用：`FROZEN` 只表示合同稳定，不表示 executor 为 `IMPLEMENTED`。

## Artifact Status

- 所属对象：受管 Artifact。
- 实际值：`DRAFT`（草稿）、`IN_REVIEW`（评审中）、`APPROVED`（已批准）、`BASELINED`（已建立基线）、`NEEDS_REVIEW`（需要评审）、`SUPERSEDED`（被替代）、`DEPRECATED`（弃用）、`ARCHIVED`（归档）、`UNKNOWN`（未知）。
- 实现性质：Artifact registry `FROZEN_CONTRACT`。
- 常见误用：文件存在不等于 `APPROVED`；时间较新不等于 `BASELINED`。

## Runtime Status

- 所属对象：Runtime operation / state record。
- 实际值：`PENDING`（待处理）、`RUNNING`（运行中）、`PAUSED`（暂停）、`BLOCKED`（阻塞）、`SUCCEEDED`（成功）、`FAILED`（失败）、`CANCELLED`（取消）、`PARTIAL`（部分完成）、`UNKNOWN`（未知）。
- 实现性质：status contract 为 `FROZEN_CONTRACT`；不能假定每个 Runtime API 都实现完整转换。
- 常见误用：Runtime `BLOCKED` 不是 Conflict `BLOCKED`，`PARTIAL` 也不是成功别名。

## Conflict Status

- 所属对象：冲突记录。
- 实际值：`OPEN`（开放）、`IN_REVIEW`（评审中）、`RESOLVED`（已解决）、`ACCEPTED_RISK`（接受风险）、`SUPERSEDED`（被后继记录替代）。
- 实现性质：`FROZEN_CONTRACT`。
- 常见误用：`ACCEPTED_RISK` 不等于冲突消失；`RESOLVED` 需要有效 resolution evidence。

## Permission Result

- 所属对象：Runtime permission decision。
- 实际值：`ALLOW`（允许继续已评估动作）、`BLOCK`（策略或安全阻塞）、`NEEDS_INPUT`（缺少可补充输入）、`NOT_APPLICABLE`（不适用）。
- 实现性质：`IMPLEMENTED`，同时有 frozen schema。
- 常见误用：`ALLOW != EXECUTED`；当前 `ActionResult.executed` 默认仍为 `false`。

## Risk Class

- 所属对象：动作风险分类。
- 实际值：`READ_ONLY`（只读）、`REVERSIBLE_WRITE`（可逆写入）、`CANONICAL_WRITE`（正式真相写入）、`PROTECTED_WRITE`（受保护写入）、`IRREVERSIBLE_OR_EXTERNAL`（不可逆或外部动作）。
- 实现性质：Policy 中 `IMPLEMENTED`；治理合同为 `FROZEN_CONTRACT`。
- 常见误用：Work Mode 不能降低 Risk Class；未知 action 在当前 Runtime fail-closed 为 `PROTECTED_WRITE`。

## Execution Scope

- 所属对象：`ActionRequest.execution_scope`。
- 实际值：`CURRENT_PROJECT_DRY_RUN`（当前项目仅演练）、`ISOLATED_FIXTURE`（隔离 fixture）、`AUTHORIZED_PROJECT_EXECUTION`（已授权项目执行范围）。
- 实现性质：enum 为 `IMPLEMENTED`；`AUTHORIZED_PROJECT_EXECUTION` 当前 evaluator 明确禁用。
- 常见误用：枚举值存在不等于该 scope 当前可用。

## Work Mode

- 所属对象：工作深度与治理检查模式。
- 实际值：`LIGHT`（低风险窄范围）、`STANDARD`（常规范围与验证）、`FULL`（高风险、跨边界或不确定工作）。
- 实现性质：合同为 `FROZEN_CONTRACT`；Runtime 校验输入值。
- 常见误用：LIGHT 不能移除 secret protection、authorization 或 human confirmation gate。

## Decision Level

- 所属对象：动作决策要求。
- 实际值：`L0`（AUTO_SAFE，安全自动）、`L1`（AUTO_WITH_TRACE，带追踪自动）、`L2`（PROPOSE_AND_CONTINUE_IF_POLICY_ALLOWS，按显式策略提议后继续）、`L3`（HUMAN_CONFIRMATION_REQUIRED，需要人确认）、`L4`（BLOCKED_OR_OWNER_DECISION_REQUIRED，阻塞或需 owner 决策）。
- 实现性质：schema 为 `FROZEN_CONTRACT`；Runtime permission result 会返回 level。
- 常见误用：L0–L4 不是任务优先级；Work Mode 不能下调 Decision Level。

## Variable Resolution Status

- 所属对象：Project variable binding。
- 实际值：`EXPLICIT`（明确给定）、`DERIVED`（可追溯派生）、`DEFAULTED`（使用已声明默认）、`UNKNOWN`（未知）、`BLOCKED`（存在明确 blocker）。
- 实现性质：Stage 04 schema 为 `FROZEN_CONTRACT`；当前具体值见[ID 与变量参考](KEY_IDS_AND_VARIABLES_REFERENCE.md)。
- 常见误用：`UNKNOWN` 不能静默变成 `DEFAULTED`；关键 unknown 必须阻塞依赖动作。

## Adapter Response Status

- 所属对象：Editor `AdapterResponse.status`。
- 实际值：`OK`（请求成功返回）、`BLOCKED`（不支持或禁止的动作被 Runtime boundary 阻塞）、`FAILED`（无效请求或 Runtime failure）。
- 实现性质：`IMPLEMENTED`。
- 常见误用：`OK` 仅表示 Adapter 请求处理成功，不表示业务动作已执行或获授权。

## Project Instance State

- 所属对象：`.banyan` Pilot 与 Stage 20 accepted state。
- 实际值：`PILOT_SHADOW`（具体 Stage 17 instance 状态）、`PROJECT_INSTANCE_SHADOW_PILOT`（Stage 20 接受的总状态）。
- 实现性质：`PILOT`。
- 常见误用：两个值是不同层级的状态表达，不代表两套已激活 Project Instance。

## Project Instance Activation

- 所属对象：feature、binding、Control Plane 与 Final Activation context。
- 实际值：`INACTIVE`（默认功能未激活）、`PILOT`（试点 binding）、`NOT_ACTIVATED`（控制面未激活）、`NOT_AUTHORIZED`（最终激活未获授权）。
- 实现性质：当前整体为 `PILOT / BLOCKED`。
- 常见误用：Framework Release、Pilot creation 或 UI 操作都不等于 Final Activation。

## Framework Release State

- 所属对象：Stage 20 Framework Release。
- 实际值：`RELEASED_AS_ADDITIVE_SUPPLEMENT_NOT_CURRENT`（作为增量补充发布，但未成为 CURRENT）。
- 实现性质：accepted Stage 20 state。
- 常见误用：`RELEASED` 不表示 governance pointer 已切换，也不表示项目已激活。

## Governance Pointer State

- 所属对象：治理版本指针与 transition proposal。
- 实际值：`CURRENT_FINAL_FREEZE`（当前最终冻结指针）、`READY_FOR_HUMAN_APPROVAL`（变更提案等待人批准）。
- 实现性质：accepted governance state。
- 常见误用：proposal ready 不等于 pointer changed；当前仍是 `v1.9.1`。

## Blocker State

- 所属对象：`CON-002`。
- 实际值：`TYPED_BLOCKED_HUMAN_PROJECT_AUTHORITY`（带类型阻塞，需 Human Project Authority）。
- 实现性质：accepted carried blocker。
- 常见误用：不能由模型、文件时间或 Framework Release 静默选定赢家。

## UI_SPEC Status

- 所属对象：Stage 08 UI_SPEC lifecycle；D0 group key 为 `ui_spec_status`。
- 实际值：`NOT_ENABLED`（未启用）、`DRAFT`（草稿）、`IN_REVIEW`（评审中）、`APPROVED`（完整范围已批准）、`PARTIAL_APPROVED`（仅声明范围部分批准）、`STALE`（已批准内容失去时效）、`REVIEW_REQUIRED`（需要重新评审）、`SUPERSEDED`（被后继批准版本替代）、`BLOCKED`（受阻）。
- 实现性质：`FROZEN_CONTRACT_NOT_IMPLEMENTED`。
- 常见误用：Draft 不授权实现；部分批准不能外推到未声明 surface。

## Canonical Apply State

- 所属对象：Stage 06 Canonical Apply contract。
- 实际值：`PREVIEWED`（已预览）、`READY_FOR_DECISION`（可进入决策）、`AUTHORIZED`（已获目标绑定授权）、`APPLYING`（应用中）、`APPLIED`（已应用）、`VALIDATED`（已验证）、`RECONCILED`（已对账）、`FAILED`（失败）、`ROLLED_BACK`（已回滚）。
- 实现性质：`FROZEN_CONTRACT_NOT_EXECUTED`；当前 Runtime / Control Plane 无 executable API。
- 常见误用：这些 frozen states 不是当前 Runtime 可调用的完整状态机。

另见[实现状态参考](IMPLEMENTATION_STATUS_REFERENCE.md)。

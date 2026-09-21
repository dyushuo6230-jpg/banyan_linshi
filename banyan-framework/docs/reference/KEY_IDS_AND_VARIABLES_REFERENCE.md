# Key IDs and Variables Reference

ID 用于稳定引用对象，Variable 用于绑定项目或 Runtime 输入。ID 的存在不证明对象已批准、已执行或已成为 Canonical。

## 稳定 ID

- `capability_id`：Capability Contract 标识，例如 `CAP-AUTH`。
- `contract_id`：合同标识，例如版本化的 Banyan contract ID。
- `artifact_id`：受管 Artifact 的标识。
- `stable_id`：跨路径或标题变化仍保持的稳定标识。
- `action_id`：一次请求或动作的标识。
- `target_id`：动作目标标识。
- `decision_id`：决策记录标识。
- `authorization_id`：授权记录标识。
- `change_id`：Banyan authority 下的 Change 标识。
- `provider_change_id`：Provider 自己的 Change 标识；不能替代 `change_id`。
- `project_instance_id`：Project Instance 标识。
- `group_id`：Semantic Commit 分组标识。
- `binding_id`：Provider 或 Overlay binding 标识。
- `port_id`：Provider port 标识。
- `provider_id`：Provider 标识。
- `policy_id`：Policy 标识。
- `workflow_policy_id`：Workflow Policy 标识。
- `run_id`：一次 Stage 或工作运行标识。
- `pilot_id`：Pilot 标识。
- `rollback_id`：Rollback plan 标识。

稳定 ID 不能复用于不同 subject；subject 变化需要新 ID。路径、标题和 Git commit hash 不自动等于 Stable ID。

## 版本字段

- `schema_version`：数据结构版本。
- `artifact_version`：Artifact 内容/生命周期版本。
- `contract_version`：合同语义版本。
- `runtime_state_version`：Runtime state 表示版本。

这些字段属于不同版本维度。同理，Framework Release、Governance CURRENT pointer 与 Python package / Runtime version 也必须分开解释。

## Runtime bridge 环境变量

- `BANYAN_REPOSITORY`：项目仓库路径；bridge 必需。
- `BANYAN_POLICY`：Policy 文件路径；bridge 必需。
- `BANYAN_TRACE`：可选 audit trace 路径。
- `BANYAN_PROVIDERS`：可选 Provider binding 文件路径。
- `BANYAN_PROVENANCE`：可选 Provenance index 路径。
- `BANYAN_STAGES`：可选 Stage record 路径。

环境变量传入路径不构成 Authorization，也不改变当前项目 `DRY_RUN_ONLY` 边界。

## Stage 04 Project Variables

Resolution status（解析状态）实际集合为 `EXPLICIT / DERIVED / DEFAULTED / UNKNOWN / BLOCKED`。D0 记录的当前值如下：

- `project_profile`：`EXPLICIT`，值指向 `PROJECT_PROFILE_SCHEMA.yaml`。
- `authorization_scope`：`UNKNOWN`，不擅自补值。
- `design_gate`：`UNKNOWN`，不擅自补值。
- `editor_entry`：`UNKNOWN`，不擅自补值。
- `project_endpoints`：`BLOCKED`，来源为 `CON-002`。
- `delivery_convention`：`UNKNOWN`，不擅自补值。
- `commit_practice`：`UNKNOWN`，有低 confidence 的 Stage 01 Git metadata 来源，但不能静默确定。

关键 unknown 必须阻塞依赖它的动作；默认值只有在明确声明时才允许。完整枚举见[状态与枚举参考](STATUS_AND_ENUM_REFERENCE.md)。

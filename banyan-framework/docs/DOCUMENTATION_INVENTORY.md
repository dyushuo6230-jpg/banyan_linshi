# Banyan Documentation Inventory（D0）

本文件是 Stage 20 之后的文档事实盘点。它只回答“当前已实现什么、已冻结什么、仍缺什么”，不把规划、合同或用户期望写成已经可用的 Framework 能力。机器可读明细见 `DOCUMENTATION_SOURCE_OF_TRUTH.yaml`。

## 1. 冻结基线

- Stage 20 验收结果：`PASS_STAGE20_DOCUMENTATION_FRAMEWORK_RELEASE_FINAL_HANDOFF_WITH_PROJECT_ACTIVATION_BLOCKED`。
- Framework Release：`v1.10-additive.1`，状态为 `RELEASED_AS_ADDITIVE_SUPPLEMENT_NOT_CURRENT`。
- 当前治理版本指针仍是 `v1.9.1 / CURRENT_FINAL_FREEZE`，未切换到 v1.10。
- Python 包与 Runtime 自报版本为 `0.1.0`。这与 Framework Release、治理版本是三个不同版本维度。
- 当前架构：Ant Design Pro Simple → Go/Gin `go:embed` → `LOCAL_STDIO` → Python Stage 15 Runtime。
- `.banyan` 是 `PROJECT_INSTANCE_SHADOW_PILOT`；Final Activation 未授权，`CON-002` 仍由 Human Project Authority 决策。
- `.banyan-refactor` 仍是施工与验收证据目录，仅在 Final Activation 之后才可能归档/退役。
- `docs/project` 保持原位，D0 未迁移。

## 2. 实际可执行入口

### CLI

Python CLI `banyan` 当前提供：

- `policy validate`、`policy compile`、`policy compile-stage14`
- `runtime preflight`
- `git inspect`
- `commit plan`
- `commit execute`，但必须显式选择 `--dry-run` 或受控 `--fixture-root`
- `trace validate`、`trace emit`
- `provider list`

控制面有两个已存在入口：Python 包中的 `banyan-control-plane`，以及 Stage 18.5 后当前架构使用的 Go 二进制 `banyan-control`。Go 入口只允许 loopback host，必须提供 repository 和 policy。

### Runtime API

`banyan.runtime.api.RuntimeAPI` 实际实现了 permission evaluate/preflight、Pilot scope preflight、Git inspect、commit plan、受控 commit execute、current-project dry-run、trace query/emit、provider binding load 和 status。

当前项目写入边界始终是 `DRY_RUN_ONLY`。`AUTHORIZED_PROJECT_EXECUTION` 在 evaluator 中被禁用；实际变更只允许在显式 isolated fixture root 内并通过门禁。Runtime 没有 Canonical Apply API。

### HTTP API

Go/Gin 控制面实际暴露 12 个路由：status、policy、project safety、preflight、commit plan、commit dry-run、trace、provenance、providers、stages、activation readiness，以及三类 editor adapter 的统一入口。它不暴露 current-project Git mutation、Canonical Apply、protected-write execution、provider activation 或 Project Instance Final Activation。

## 3. 实际 WebUI 页面

当前 Ant Design Pro Simple 前端有 12 个页面：

1. `/dashboard`
2. `/runtime-policy`
3. `/project-safety`
4. `/gate-blockers`
5. `/preflight`
6. `/commit-plan`
7. `/dry-run-result`
8. `/trace-audit`
9. `/provenance`
10. `/provider-bindings`
11. `/stage-run`
12. `/activation-readiness`

WebUI 是 Runtime 结果展示和意图提交界面，不授予授权，不允许当前项目 Git mutation。`/help`、Markdown 文档树、Docs API 均尚未实现。

## 4. 实际 Adapter

已验证的编辑器适配器是 `cursor`、`codex`、`generic-editor`。它们将各自请求形状归一化为 `AdapterRequest`，再进入 `AdapterGateway → Control Plane → Runtime API → Policy → Evidence Trace`。

适配器支持 `runtime_status`、`project_safety`、`preflight`、`commit_plan`、`commit_dry_run`、`trace`、`provenance`。它们不拥有 Permission Policy、Canonical Truth 或直接 Git mutation 权限。

另外存在 Pilot 专用 `CursorPilotAdapter`，以及内部 `FilesystemAdapter`、`ProcessRunner`。后两者是实现组件，不是用户编辑器入口。

## 5. Skill 与 Capability 的事实边界

`banyan-framework` 内没有 Framework-native `SKILL.md`。当前仓库实际存在两个被保留的项目 Skill：

- `anydesign`：真源是 `tools/anydesign/SKILL.md`，`.cursor/skills/anydesign` 是符号链接；归类为 provider-owned、preserve in place。
- `visual-repair-loop`：位于 `.cursor/skills/visual-repair-loop/SKILL.md`；归类为 compatibility layer、preserve in place。

Stage 03 冻结了 35 个 `CAP-*` Capability Contract，覆盖授权、项目变量、来源、PRD、决策、架构、Artifact、Trace、Change、并行草稿、对账、测试、进度、交接、上下文、UI、知识发布、编辑器、项目 Overlay、Git 协作和设计 Provider 等。但注册表总状态是 `FROZEN_CONTRACTS_IMPLEMENTATION_UNBOUND`，每项 `implementation_frozen=false`、`provider_selected=false`。文档不能把这 35 项写成 35 个已安装 Skill 或全部可执行能力。

## 6. Workflow 的事实边界

- `banyan.workflow.adaptive.v1` 已冻结，但状态是 `FROZEN_POLICY_NOT_IMPLEMENTED`。
- Stage 05 Workflow state machine 已冻结；Stage 05 的终态只到 `READY_FOR_EXECUTOR_OR_BLOCKED`，当时未实现执行迁移。
- Stage 06 Change lifecycle 已冻结；Stage 06 最大状态只到 `APPLY_PLANNED`。
- 当前真正可执行的流程是受限的 request flow、preflight、commit plan、commit dry-run、trace/provenance 查询和 provider binding 查询。
- Stage 20 的 Upgrade 生命周期是文档化过程，不是自动化 Runtime workflow。

因此，“Understand → Collect → Plan → Decide → Execute → Validate → Deliver”是文档目标用户旅程，当前不能整体描述为 Runtime 已自动编排。

## 7. Role、Status 与 Enum

已冻结的 Source Role 有 9 个：`DECISION_CHANGE_HISTORY`、`DERIVED_PROJECTION`、`OPERATIONAL_HISTORY`、`PROJECT_CANONICAL_DOCUMENT`、`PROJECT_GUIDE_DERIVED`、`REQUIREMENT_SOURCE`、`TECHNICAL_CONTRACT_SOURCE`、`UI_DESIGN_DERIVED`、`UI_SPEC_SOURCE`。

Human Project Authority 是解决 `CON-002` 与 Final Activation 的真实治理角色概念，但当前没有对应 Runtime role enum。Pilot Contributor Profile 的 `permission_role` 当前为 `NONE`，身份值未持久化，也不构成授权。

已冻结或实现的主要枚举包括：

- Permission Result：`ALLOW / BLOCK / NEEDS_INPUT / NOT_APPLICABLE`
- Risk Class：`READ_ONLY / REVERSIBLE_WRITE / CANONICAL_WRITE / PROTECTED_WRITE / IRREVERSIBLE_OR_EXTERNAL`
- Execution Scope：`CURRENT_PROJECT_DRY_RUN / ISOLATED_FIXTURE / AUTHORIZED_PROJECT_EXECUTION`
- Work Mode：`LIGHT / STANDARD / FULL`
- Decision Level：`L0` 至 `L4`
- Contract、Artifact、Runtime、Conflict 各自的状态集合
- Variable Resolution：`EXPLICIT / DERIVED / DEFAULTED / UNKNOWN / BLOCKED`
- Adapter Response：`OK / BLOCKED / FAILED`
- UI_SPEC、Change、Canonical Apply 的合同状态集合

完整枚举见 YAML；使用时必须保留它们所属的 schema/语境，不能把同名 `BLOCKED` 混为同一个状态机。

## 8. ID 与 Variable

已出现并承担稳定引用作用的 ID 包括 `capability_id`、`contract_id`、`artifact_id/stable_id`、`action_id`、`target_id`、`decision_id`、`authorization_id`、`change_id`、`provider_change_id`、`project_instance_id`、`group_id`、`binding_id`、`port_id`、`provider_id`、`policy_id`、`workflow_policy_id`、`run_id`、`pilot_id`、`rollback_id`。

版本字段明确区分 `schema_version`、`artifact_version`、`contract_version`、`runtime_state_version`。

Runtime bridge 实际读取 `BANYAN_REPOSITORY`、`BANYAN_POLICY`、`BANYAN_TRACE`、`BANYAN_PROVIDERS`、`BANYAN_PROVENANCE`、`BANYAN_STAGES`。

Stage 04 项目变量中，只有 `project_profile` 是 `EXPLICIT`；`authorization_scope`、`design_gate`、`editor_entry`、`delivery_convention`、`commit_practice` 为 `UNKNOWN`，`project_endpoints` 因 `CON-002` 为 `BLOCKED`。

## 9. 关键文档类型

已有明确合同或实际文件证据的类型包括 PRD、UI_SPEC、DEC、ADR、CR、UI-DEC、Change、Draft Change Package、Evidence、Trace、Project Guide、Handover、Worklog。

PRD 是产品/业务需求的 Canonical truth；UI_SPEC 是已批准且限定应用范围的 UI contract projection，不能建立第二份业务真相。Design Source 只作 Evidence。

`TBD` 是未解决值标记，不是文档类型。Documentation Packaging 要求覆盖 `RFC` 和 `TBC` 术语，但本次 accepted evidence 定点盘点没有找到专门的 RFC artifact schema 或 TBC enum，不能自行补定义。

## 10. 实际目录与 Project Instance

Framework 实际目录包括 Python source、frontend、Go control plane、policies 和 tests。`banyan-framework/docs` 是 D0 文档输出目录。

`.banyan` 当前有 13 个 Pilot 文件，包含 instance、mappings、overlays、profiles、providers、runtime、trace、index、generated、migrations 等内部面。其关键状态是：

- `PILOT_SHADOW / PROJECT_INSTANCE_SHADOW_PILOT`
- `canonical_truth=false`
- `canonical_replacement=false`
- `existing_project_layout=PRESERVE_IN_PLACE`
- `docs_project_migration=NOT_PERFORMED`
- `git_mutation=NOT_AUTHORIZED`
- `current_project_git_execution=DRY_RUN_ONLY`
- `canonical_write=BLOCKED`
- `protected_business_write=BLOCKED`

Stage 04 的 Project Instance schema 是冻结设计，Stage 17 的 `.banyan` 是具体 Pilot 投影。Framework Release 不等于 Project Final Activation。

## 11. Git 与 Permission 事实

- Runtime fail-closed；未知 action 按 `PROTECTED_WRITE` 处理并阻塞。
- `ALLOW` 是 permission decision，不代表动作已经执行；`ActionResult.executed` 默认是 `false`。
- 当前项目 commit 只有 dry-run；真实 mutation 仅可在显式 isolated fixture 内通过门禁执行。
- mutation 需要 authorization；commit 还要求 identity present。
- WebUI confirmation、Adapter request、Trace、Commit Plan、Role、Git Identity 都不单独构成授权。
- Secret body 不允许通过 WebUI/provenance 文档面展示。

## 12. DOC-GAP-CANDIDATE

1. `DOC-GAP-CANDIDATE-001`：规划中的 `/help` Help Center 尚不存在。
2. `DOC-GAP-CANDIDATE-002`：自然语言编辑器只有受限 Adapter 请求面，没有 Framework 内完整端到端自然语言 Workflow 编排。
3. `DOC-GAP-CANDIDATE-003`：Adaptive Workflow 是冻结合同，尚未实现为自动路由器。
4. `DOC-GAP-CANDIDATE-004`：Implementation Owner、Draft Contributor、Reviewer、Project Authority 尚没有完整的 Runtime role enum/binding schema；仅 Human Project Authority 是已使用的治理概念。
5. `DOC-GAP-CANDIDATE-005`：Canonical Apply 与完整 Change 生命周期有合同，但没有当前 Runtime/Control Plane 可执行入口。
6. `DOC-GAP-CANDIDATE-006`：35 个 Capability Contract 没有对应的 35 个 Framework-native Skill。
7. `DOC-GAP-CANDIDATE-007`：RFC 与 TBC 缺少独立冻结定义，后续文档不能自行发明枚举。
8. `DOC-GAP-CANDIDATE-008`：Framework Release、治理 CURRENT 指针、Python Package/Runtime 版本是不同维度，后续文档必须分别说明。
9. `DOC-GAP-CANDIDATE-009`：Framework 已发布，但 `.banyan` 仍是 Pilot，Final Activation 未授权。

## 13. D0 变更边界

D0 只新增本盘点文件和机器可读 Source of Truth。未修改 Banyan Core、Runtime、Policy、Permission、Git、`.banyan`；未迁移 `docs/project`；未启动 WebUI Help Center；未改变 version pointer；未执行 Final Activation。

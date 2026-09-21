# Banyan 中英双语术语表

状态标签见[实现状态参考](IMPLEMENTATION_STATUS_REFERENCE.md)，文档类型见[关键文档类型参考](KEY_DOCUMENT_TYPES_REFERENCE.md)。“当前状态”描述 D0 已确认事实。

## 需求、决策与标记

### PRD

- 英文：Product Requirements Document
- 推荐中文：产品需求文档
- 小白解释：说明产品为什么做、为谁做、要解决什么问题。
- Banyan 正式含义：产品/业务需求的 Canonical truth（权威正式来源）。
- 当前状态：`FROZEN_CONTRACT`；已冻结 authority contract。
- 常见误解：PRD 不是技术实现说明，UI_SPEC 也不能替代 PRD 的业务真相地位。

### ADR

- 英文：Architecture Decision Record
- 推荐中文：架构决策记录
- 小白解释：记录一项重要架构选择及其理由和影响。
- Banyan 正式含义：Decision contract 中存在的技术决策文档类型。
- 当前状态：`FROZEN_CONTRACT`；accepted Stage evidence 中也有实际 ADR。
- 常见误解：ADR 不等于任何讨论记录，也不因文件存在自动生效。

### DEC

- 英文：Decision Record
- 推荐中文：决策记录
- 小白解释：把人的明确选择、理由和适用范围记录下来。
- Banyan 正式含义：用于承载有效决策及其 Evidence、影响和确认关系。
- 当前状态：`FROZEN_CONTRACT`；项目文档中有实际 DEC。
- 常见误解：模型建议、沉默或取消都不自动成为 DEC。

### UI_SPEC

- 英文：User Interface Specification
- 推荐中文：界面规格
- 小白解释：说明某个应用范围内界面应该怎样表现。
- Banyan 正式含义：批准后且限定 application scope 的 UI contract projection；不能创建第二份业务真相。
- 当前状态：`FROZEN_CONTRACT`；lifecycle executor 未因此自动存在。
- 常见误解：截图、Design Source 或 Draft UI_SPEC 都不是已批准 UI_SPEC。

### TBD

- 英文：To Be Determined
- 推荐中文：待确定
- 小白解释：这个值或结论还没有确定。
- Banyan 正式含义：unresolved value marker；未知必须显式保留。
- 当前状态：标记，不是文档类型或独立 Runtime enum。
- 常见误解：TBD 不等于默认值，也不等于可以忽略。

### TBC

- 英文：To Be Confirmed
- 推荐中文：待确认
- 小白解释：已有候选说法，但仍需要确认。
- Banyan 正式含义：Documentation Packaging 要求覆盖的术语；当前无独立 frozen Banyan schema / enum。
- 当前状态：`NOT_IMPLEMENTED`（独立 Banyan 定义）。
- 常见误解：不能自行把 TBC 加入某个 Runtime 状态集合。

### RFC

- 英文：Request for Comments
- 推荐中文：征求意见稿
- 小白解释：供相关人员评议的方案或提案。
- Banyan 正式含义：可按通用工程含义理解；当前没有独立 frozen Banyan artifact schema。
- 当前状态：`NOT_IMPLEMENTED`（独立 Banyan schema）。
- 常见误解：RFC 不是默认批准的 Decision，也不是 Canonical truth。

## 事实、来源与证据

### Artifact

- 英文：Artifact
- 推荐中文：工程产物
- 小白解释：研发过程中产生并可被识别、引用的文件或记录。
- Banyan 正式含义：具有 `artifact_id`、类型、版本、状态、Source Role、Provenance 和引用关系的受管对象。
- 当前状态：`FROZEN_CONTRACT`。
- 常见误解：Artifact 不一定是 Canonical，也不一定是文档。

### Canonical

- 英文：Canonical
- 推荐中文：权威正式来源
- 小白解释：多个说法冲突时，可作为正式事实依据的来源。
- Banyan 正式含义：由 Source Role、scope、authority、freshness 和决策证据共同确定，不能只看文件名或时间。
- 当前状态：`FROZEN_CONTRACT`；Canonical Apply API 当前不存在。
- 常见误解：最新文件、生成结果或 Provider workspace 不会自动成为 Canonical。

### Derived

- 英文：Derived
- 推荐中文：派生内容
- 小白解释：根据其他正式来源计算或整理出来的内容。
- Banyan 正式含义：必须保留输入引用与生成沿革；source hash/version 不匹配时可能过期。
- 当前状态：`FROZEN_CONTRACT`。
- 常见误解：Derived 内容不能反向覆盖它依赖的 Canonical source。

### Provenance

- 英文：Provenance
- 推荐中文：来源沿革
- 小白解释：说明内容从哪里来、何时产生、经过什么处理。
- Banyan 正式含义：可包括 source、timestamp、input refs、generator/tool、confidence；未知必须显式写 `UNKNOWN`。
- 当前状态：`FROZEN_CONTRACT`，Control Plane 有 `IMPLEMENTED` 查询面。
- 常见误解：来源不明时不能用模型确信度补造来源。

### Evidence

- 英文：Evidence
- 推荐中文：证据
- 小白解释：支持某项判断、状态或结果的可核验材料。
- Banyan 正式含义：可被稳定引用并进入 permission、decision、validation 或 acceptance 判断的记录。
- 当前状态：schema 为 `FROZEN_CONTRACT`；部分 Runtime evidence surface 为 `IMPLEMENTED`。
- 常见误解：Evidence 本身不授予 Authorization，也不自动成为 Canonical。

### Trace

- 英文：Trace
- 推荐中文：追踪记录
- 小白解释：按事件记录做过什么、结果怎样、关联了哪些证据。
- Banyan 正式含义：当前实现为可校验、可分页查询的 JSONL audit surface。
- 当前状态：`IMPLEMENTED`。
- 常见误解：Trace 不是 Authorization，也不能证明未记录的动作已获批准。

### Stable ID

- 英文：Stable Identifier
- 推荐中文：稳定标识符
- 小白解释：对象移动或改标题后仍能引用它的固定编号。
- Banyan 正式含义：同一 ID 不得复用于不同 subject；subject 改变需要新 ID。
- 当前状态：`FROZEN_CONTRACT`。
- 常见误解：文件路径和显示标题不一定是 Stable ID。

### Source Role

- 英文：Source Role
- 推荐中文：来源角色
- 小白解释：说明一个来源在事实判断中扮演什么角色。
- Banyan 正式含义：9 个已冻结角色决定 authority、freshness 与 conflict handling。
- 当前状态：`FROZEN_CONTRACT`；详见[角色参考](ROLE_REFERENCE.md)。
- 常见误解：Source Role 不是人员角色，也不授予权限。

### Authority

- 英文：Authority
- 推荐中文：权威性
- 小白解释：某个来源在特定范围内能否作为正式依据。
- Banyan 正式含义：与 Source Role、scope、freshness、approval 和 decision evidence 一起判断。
- 当前状态：`FROZEN_CONTRACT`。
- 常见误解：作者身份、Git 历史或文件新旧不能单独决定 Authority。

### Freshness

- 英文：Freshness
- 推荐中文：时效状态
- 小白解释：内容是否仍与当前有效来源一致。
- Banyan 正式含义：不能仅凭 mtime、文件名顺序或“最近看到”判断。
- 当前状态：`FROZEN_CONTRACT`。
- 常见误解：新创建的文件不一定比已批准版本更新或更权威。

### Version

- 英文：Version
- 推荐中文：版本
- 小白解释：说明某个 schema、Artifact、合同或 Runtime state 处于哪个修订层次。
- Banyan 正式含义：至少区分 `schema_version`、`artifact_version`、`contract_version`、`runtime_state_version`。
- 当前状态：版本字段为 `FROZEN_CONTRACT`；Framework、Governance 和 Python Runtime 另有三个独立版本维度。
- 常见误解：不能用 `v1.10-additive.1` 同时代表 Governance pointer 和 Python package version。

### Status

- 英文：Status
- 推荐中文：状态
- 小白解释：说明特定对象当前处在哪个生命周期位置。
- Banyan 正式含义：必须带所属 schema / context；Contract、Artifact、Runtime、Conflict 等各有状态集合。
- 当前状态：多组 enum 已冻结或实现，详见[状态与枚举参考](STATUS_AND_ENUM_REFERENCE.md)。
- 常见误解：不同状态机里的 `BLOCKED` 不能合并成一个全局状态。

## 变更与应用

### Change

- 英文：Change
- 推荐中文：变更
- 小白解释：一组有稳定编号、状态和影响范围的拟议修改。
- Banyan 正式含义：遵循 Stage 06 Change lifecycle，并区分 Banyan `change_id` 与 Provider ID。
- 当前状态：`FROZEN_CONTRACT`；完整 executor 未实现。
- 常见误解：工作目录里有改动不等于 Change 已获批准。

### Draft Change Package

- 英文：Draft Change Package
- 推荐中文：变更草稿包
- 小白解释：供对账、评审和决策的临时变更材料集合。
- Banyan 正式含义：在 Canonical Apply 前隔离保存提议、影响和证据的合同对象。
- 当前状态：`FROZEN_CONTRACT`。
- 常见误解：Draft 不会因 Provider 状态或文件时间自动晋升为正式真相。

### Canonical Apply

- 英文：Canonical Apply
- 推荐中文：正式真相应用
- 小白解释：经预览、决策、授权和验证后，把批准变更应用到正式来源。
- Banyan 正式含义：Stage 06 已冻结状态与门禁合同。
- 当前状态：`FROZEN_CONTRACT`，Runtime / Control Plane executable API 为 `NOT_IMPLEMENTED`。
- 常见误解：`ALLOW`、评审通过或 Draft 存在都不等于已执行 Canonical Apply。

## 组织能力

### Role

- 英文：Role
- 推荐中文：角色
- 小白解释：说明一个来源、人员或协作参与者承担什么职责。
- Banyan 正式含义：需先说明属于 Source、Governance、Contributor Profile 或 Documentation Collaboration context。
- 当前状态：各 context 不同；详见[角色参考](ROLE_REFERENCE.md)。
- 常见误解：`Role != Permission != Git Identity != Authentication`。

### Skill

- 英文：Skill
- 推荐中文：技能说明包
- 小白解释：告诉 AI 在特定任务中如何工作的一组可加载说明。
- Banyan 正式含义：Framework-native Skills 当前为空；项目保留 `anydesign` 与 `visual-repair-loop`。
- 当前状态：两个现有 Skill 均在 Core 外 preserve in place。
- 常见误解：35 个 `CAP-*` 不是 35 个 Skill。

### Capability

- 英文：Capability
- 推荐中文：能力
- 小白解释：系统应该提供的一类行为及其输入、输出和边界。
- Banyan 正式含义：35 个 `CAP-*` 是 `FROZEN_CONTRACTS_IMPLEMENTATION_UNBOUND` 的 Capability Contract。
- 当前状态：`FROZEN_CONTRACT`，不能整体标为 `IMPLEMENTED`。
- 常见误解：合同存在不等于 Provider 已选择或 executor 已交付。

### Workflow

- 英文：Workflow
- 推荐中文：工作流
- 小白解释：按照条件和状态组织任务步骤的过程。
- Banyan 正式含义：既包括冻结的 adaptive/state/lifecycle 合同，也包括当前实际 request flow。
- 当前状态：逐 Workflow 判断；详见[工作流参考](WORKFLOW_REFERENCE.md)。
- 常见误解：目标用户旅程不是当前 Runtime 自动状态机。

## 安全与执行

### Gate

- 英文：Gate
- 推荐中文：门禁
- 小白解释：条件不满足就不能进入下一步的检查点。
- Banyan 正式含义：依据 Evidence、Authority、Authorization、Freshness、risk 等产生受类型约束的结果。
- 当前状态：合同与部分 Runtime evaluation 已存在。
- 常见误解：按钮确认或角色名称不能绕过 Gate。

### Preflight

- 英文：Preflight
- 推荐中文：执行前预检
- 小白解释：正式动作前检查权限、风险、前置条件和证据。
- Banyan 正式含义：当前 RuntimeAPI 与 CLI / Control Plane 均有受限 preflight surface。
- 当前状态：`IMPLEMENTED`。
- 常见误解：预检返回 `ALLOW` 不表示动作已经执行。

### Permission

- 英文：Permission
- 推荐中文：权限判定
- 小白解释：根据规则判断某个动作现在允许、阻塞或缺少输入。
- Banyan 正式含义：Runtime fail-closed，结果为 `ALLOW / BLOCK / NEEDS_INPUT / NOT_APPLICABLE`。
- 当前状态：`IMPLEMENTED`。
- 常见误解：Permission 与 Authorization 不是同一概念。

### Permission Result

- 英文：Permission Result
- 推荐中文：权限判定结果
- 小白解释：预检或权限评估给出的明确结论。
- Banyan 正式含义：实际值为 `ALLOW / BLOCK / NEEDS_INPUT / NOT_APPLICABLE`。
- 当前状态：`IMPLEMENTED`。
- 常见误解：`ALLOW` 不等于 `EXECUTED`，`NEEDS_INPUT` 也不等于策略拒绝。

### Authorization

- 英文：Authorization
- 推荐中文：授权
- 小白解释：允许特定主体在特定范围执行特定动作的有效依据。
- Banyan 正式含义：mutation 需有效且与 action/target/scope 绑定的授权证据。
- 当前状态：schema 为 `FROZEN_CONTRACT`，Runtime 执行门禁有实际检查。
- 常见误解：Role、Git Identity、WebUI confirmation、Trace 和 Commit Plan 都不单独构成授权。

### Work Mode

- 英文：Work Mode
- 推荐中文：工作模式
- 小白解释：按风险和范围调整检查深度的模式。
- Banyan 正式含义：`LIGHT / STANDARD / FULL`；模式不能降低安全责任或决策级别。
- 当前状态：合同与 Runtime 输入校验存在。
- 常见误解：LIGHT 不能绕过高风险门禁。

### Risk Class

- 英文：Risk Class
- 推荐中文：风险类别
- 小白解释：按动作影响和可逆性决定需要多严格的门禁。
- Banyan 正式含义：`READ_ONLY / REVERSIBLE_WRITE / CANONICAL_WRITE / PROTECTED_WRITE / IRREVERSIBLE_OR_EXTERNAL`。
- 当前状态：Policy 中 `IMPLEMENTED`，治理合同为 `FROZEN_CONTRACT`。
- 常见误解：Work Mode 不能把高风险动作降成低风险。

### Execution Mode

- 英文：Execution Mode
- 推荐中文：执行模式
- 小白解释：说明动作在哪种边界内运行，例如只演练或隔离执行。
- Banyan 正式含义：当前项目运行状态为 `DRY_RUN_ONLY`；请求 schema 另使用 Execution Scope 枚举。
- 当前状态：current-project dry-run 为 `IMPLEMENTED`，正式项目执行为禁用状态。
- 常见误解：Execution Mode 不是 Authorization，也不能与 `AUTHORIZED_PROJECT_EXECUTION` 枚举值是否存在混为一谈。

### Decision Level

- 英文：Decision Level
- 推荐中文：决策级别
- 小白解释：说明动作能自动进行、需记录、需提议、需人确认或必须阻塞。
- Banyan 正式含义：`L0` 至 `L4`，由风险、权限和不确定性决定。
- 当前状态：`FROZEN_CONTRACT`；Runtime 返回对应 level。
- 常见误解：数值高低不是优先级，也不能由 Work Mode 下调。

### Semantic Commit

- 英文：Semantic Commit
- 推荐中文：语义化提交
- 小白解释：按变更含义分组并生成可审查的提交计划。
- Banyan 正式含义：当前支持 inspect、plan 和 current-project dry-run；真实当前项目 commit 被禁用。
- 当前状态：计划和 dry-run 为 `IMPLEMENTED`。
- 常见误解：Commit Plan 不是授权，dry-run 不会创建 commit。

## 架构与接入

### Provider

- 英文：Provider
- 推荐中文：能力提供方
- 小白解释：在约定接口后提供某项具体能力的实现或工具。
- Banyan 正式含义：通过 binding/port 接入，不能拥有 Runtime Permission Policy 或自动成为 Canonical truth。
- 当前状态：binding load 为 `IMPLEMENTED`；各能力 provider selection 不能从合同存在推断。
- 常见误解：Provider 可运行不代表它已获激活或通过等价性验证。

### Overlay

- 英文：Overlay
- 推荐中文：项目覆盖层
- 小白解释：在通用规则之上绑定项目自己的变量和约定。
- Banyan 正式含义：Project Instance 内的项目级 binding；不能削弱 Core safety floor。
- 当前状态：schema 为 `FROZEN_CONTRACT`，`.banyan` 中为空 Pilot binding。
- 常见误解：Overlay 不是复制一套 Core，也不是绕过 Policy 的配置。

### Project Instance

- 英文：Project Instance
- 推荐中文：项目实例
- 小白解释：把通用 Banyan 与某个具体项目连接起来的配置和状态集合。
- Banyan 正式含义：包含 project、mappings、overlays、profiles、bindings、activation、locations 和 lineage。
- 当前状态：`.banyan` 为 `PILOT`，Final Activation 未授权。
- 常见误解：Framework Release 不等于 Project Instance 已激活。

### Runtime

- 英文：Runtime
- 推荐中文：运行时核心
- 小白解释：实际执行权限判断、预检和受控动作的核心。
- Banyan 正式含义：Python Stage 15 Runtime 是 policy 与 execution authority。
- 当前状态：受限 API 为 `IMPLEMENTED`，当前项目为 `DRY_RUN_ONLY`。
- 常见误解：Go/Gin Control Plane 不是第二套 Runtime。

### Control Plane

- 英文：Control Plane
- 推荐中文：控制面
- 小白解释：把 WebUI 或 Adapter 请求转交给 Runtime 并展示结果的本地入口。
- Banyan 正式含义：Go/Gin 本地 web host，经 `LOCAL_STDIO` 调用 Python Runtime。
- 当前状态：`IMPLEMENTED`，仅允许 loopback bind。
- 常见误解：Control Plane 不拥有独立 Policy，也不授予授权。

### Adapter

- 英文：Adapter
- 推荐中文：适配器
- 小白解释：把不同编辑器的请求格式转换成统一格式。
- Banyan 正式含义：Cursor、Codex、Generic Editor 通过同一 Gateway 使用受限 action surface。
- 当前状态：三类编辑器 Adapter 为 `IMPLEMENTED` 且已验证。
- 常见误解：Adapter 不是完整自然语言 agent，也不拥有 Git mutation 权限。

### Shadow Pilot

- 英文：Shadow Pilot
- 推荐中文：影子试点
- 小白解释：先在受限范围验证结构和连接，不替代正式项目真相。
- Banyan 正式含义：`.banyan` 的当前状态，`canonical_truth=false`、`canonical_replacement=false`。
- 当前状态：`PILOT`。
- 常见误解：Pilot 文件存在不代表正式激活。

### Final Activation

- 英文：Final Activation
- 推荐中文：最终激活
- 小白解释：经过独立治理决定后，把 Project Instance 正式启用。
- Banyan 正式含义：需 Human Project Authority、门禁、checkpoint、rollback readiness 和单独授权。
- 当前状态：`BLOCKED / NOT_AUTHORIZED`。
- 常见误解：Stage 20 Framework Release 不构成 Final Activation。

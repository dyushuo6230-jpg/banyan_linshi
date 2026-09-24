# Banyan Documentation Packaging — D1 Foundation

请完整读取以下事实底座与施工约束：

```text
banyan-framework/docs/DOCUMENTATION_SOURCE_OF_TRUTH.yaml
banyan-framework/docs/DOCUMENTATION_INVENTORY.md
榕树ai改造落地相关文档/Documentation_Packaging/Banyan_Documentation_Packaging_Master/Banyan_Documentation_Packaging_总指挥文档_v1.0.md
```

如果当前目录中的总指挥文档实际路径不同，使用用户已放入的 Documentation_Packaging 对应文件；不得因为路径差异自行改变任务目标。

## 任务

执行 D1 Documentation Foundation，只建设文档地基。

在：

```text
banyan-framework/docs/
```

创建或更新：

```text
README.md
DOCUMENTATION_MAP.md
WRITING_STYLE_GUIDE.md

reference/
├── GLOSSARY_BILINGUAL.md
├── IMPLEMENTATION_STATUS_REFERENCE.md
├── KEY_DOCUMENT_TYPES_REFERENCE.md
├── KEY_IDS_AND_VARIABLES_REFERENCE.md
├── STATUS_AND_ENUM_REFERENCE.md
├── ROLE_REFERENCE.md
├── SKILL_REFERENCE.md
└── WORKFLOW_REFERENCE.md
```

## Source of Truth 优先级

严格使用 D0 已冻结优先级：

```text
1. current implementation source
2. Stage 20 accepted evidence
3. earlier frozen contracts referenced by Stage 20
4. Documentation Packaging expectations
```

如果低优先级内容与高优先级冲突，以高优先级为准。

## 关键事实边界

必须保留以下边界，不得“写顺手”后抹掉：

- 35 个 `CAP-*` 是 frozen Capability Contract，不是 35 个已安装 Skill。
- Framework-native Skills 当前为空。
- `anydesign` 与 `visual-repair-loop` 是保留的项目/兼容层 Skill，不属于 Banyan Core。
- Adaptive Workflow 已冻结但未实现自动路由。
- `Understand → Collect → Plan → Decide → Execute → Validate → Deliver` 是目标用户旅程，不是当前 Runtime 完整自动状态机。
- Cursor / Codex / Generic Editor Adapter 当前只有实际支持的 action surface。
- Canonical Apply 尚无 Runtime/Control Plane executable API。
- `/help` 尚未实现。
- `Human Project Authority` 是治理概念，不是 Runtime enum。
- `Implementation Owner / Draft Contributor / Reviewer` 如果用于文档，只能标为 Documentation Collaboration Role。
- Role != Permission != Git Identity != Authentication。
- `TBD` 是 unresolved value marker，不是文档类型。
- `RFC` 与 `TBC` 无独立 frozen Banyan schema/enum。
- Framework Release、Governance CURRENT、Python package/runtime version 分开解释。
- `.banyan` 是 Shadow Pilot，Final Activation 未授权。

## 文档写作要求

### README.md
作为整个 Banyan Documentation 的入口页，按用户角色导航：

```text
普通开发者
项目负责人
高级/自动化用户
Banyan 维护者
```

明确：
- 主入口：Codex / Cursor 自然语言编辑器
- WebUI：辅助观察与操作入口
- CLI：高级/调试/自动化入口

但必须标注：完整自然语言自动 Workflow 编排目前仍是 Gap，不得声称已经完整实现。

### DOCUMENTATION_MAP.md
说明：
- user-guide 是什么
- scenarios 是什么
- reference 是什么
- maintainer 是什么
- 当前 D1 已完成哪些、哪些将在 D2/D3/D4/D5 生成

不得创建假链接到尚不存在的正文而不注明“后续阶段”。

### WRITING_STYLE_GUIDE.md
至少规范：
- 英文第一次出现时中文解释
- 缩写展开
- 中英文括号格式
- 实现状态标签
- “已实现 / 已冻结 / 规划 / Pilot / Blocked”措辞
- 示例代码与真实枚举的区别
- 禁止把目标体验写成当前实现
- 用户文档使用“小白表达”，Reference 保持精确
- Canonical / Provenance / Evidence / Trace / Gate / Preflight 等推荐中文解释

### GLOSSARY_BILINGUAL.md
至少覆盖：
- PRD / ADR / DEC / UI_SPEC / TBD / TBC / RFC
- Artifact / Canonical / Derived / Provenance / Evidence / Trace
- Stable ID / Source Role / Authority / Freshness
- Change / Draft Change Package / Canonical Apply
- Role / Skill / Capability / Workflow
- Gate / Preflight / Permission / Authorization
- Provider / Overlay / Project Instance
- Runtime / Control Plane / Adapter
- Work Mode / Decision Level
- Semantic Commit
- Shadow Pilot / Final Activation

每条包含：
- 英文
- 推荐中文
- 小白解释
- Banyan 正式含义
- 当前实现状态或参考链接
- 常见误解

### IMPLEMENTATION_STATUS_REFERENCE.md
定义文档展示标签：

```text
IMPLEMENTED
FROZEN_CONTRACT
PILOT
PLANNED
NOT_IMPLEMENTED
BLOCKED
```

强调这些是 Documentation status labels，不是 Runtime 新增 enum。

给出至少这些例子：
- RuntimeAPI.evaluate_action = IMPLEMENTED
- Adaptive Workflow = FROZEN_CONTRACT / NOT_IMPLEMENTED executor
- `.banyan` = PILOT
- `/help` = NOT_IMPLEMENTED
- Final Activation = BLOCKED / NOT_AUTHORIZED
- 35 CAP-* = FROZEN_CONTRACT

### KEY_DOCUMENT_TYPES_REFERENCE.md
严格区分“文档类型”和“状态/标记”。

至少覆盖：
- PRD
- UI_SPEC
- DEC
- ADR
- CR
- UI-DEC
- Change
- Draft Change Package
- Evidence
- Trace
- Project Guide
- Handover
- Worklog

另设“常见但当前 Banyan 未独立冻结”：
- RFC
- TBC

另设“不是文档类型”：
- TBD

必须说明 PRD 与 UI_SPEC 的 Canonical 边界：
- PRD：产品/业务需求 Canonical truth
- UI_SPEC：批准后且限定范围的 UI contract projection
- Design Source：Evidence，不建立第二份业务真相

### KEY_IDS_AND_VARIABLES_REFERENCE.md
以 D0 为准覆盖：
- capability_id
- contract_id
- artifact_id
- stable_id
- action_id
- target_id
- decision_id
- authorization_id
- change_id
- provider_change_id
- project_instance_id
- group_id
- binding_id
- port_id
- provider_id
- policy_id
- workflow_policy_id
- run_id
- pilot_id
- rollback_id

版本字段：
- schema_version
- artifact_version
- contract_version
- runtime_state_version

Runtime bridge 环境变量：
- BANYAN_REPOSITORY
- BANYAN_POLICY
- BANYAN_TRACE
- BANYAN_PROVIDERS
- BANYAN_PROVENANCE
- BANYAN_STAGES

并解释 Stage04 project variables 的 resolution 状态，但不要擅自补值。

### STATUS_AND_ENUM_REFERENCE.md
按 schema / context 分组，严禁把所有 `BLOCKED` 混成同一个状态。

至少覆盖 D0 已确认的：
- contract_status
- artifact_status
- runtime_status
- conflict_status
- permission_result
- risk_class
- execution_scope
- work_mode
- decision_level
- variable_resolution_status
- adapter_response_status
- project_instance_state
- project_instance_activation
- framework_release_state
- governance_pointer_state
- blocker_state
- ui_spec_status
- canonical_apply_state

对每组写：
- 所属对象
- 所有实际值
- 中文含义
- 是否 Runtime 实现 / frozen contract / Pilot 等
- 常见误用

### ROLE_REFERENCE.md
至少分四类：
1. Source Role
2. Governance Role
3. Project Instance Contributor Profile
4. Documentation Collaboration Role

Documentation Collaboration Role 可说明：
- Implementation Owner（主要施工负责人）
- Draft Contributor（变更稿贡献者）
- Reviewer（评审者）

但必须明确这些不是当前 Runtime role enum，也不自动授予权限。

必须反复保持：
`Role != Permission != Git Identity != Authentication`

### SKILL_REFERENCE.md
先解释：
- Skill 是什么
- Capability Contract 是什么
- Provider capability 是什么
- 三者为什么不能混用

真实现状：
- Framework-native Skills = none
- anydesign = provider-owned / preserved in place
- visual-repair-loop = compatibility layer / preserved in place
- 35 CAP-* = FROZEN_CONTRACTS_IMPLEMENTATION_UNBOUND

可以列 35 CAP-* 的索引，但标题必须叫 Capability Contract，不能叫“35 个 Skill”。

### WORKFLOW_REFERENCE.md
至少区分：
- `banyan.workflow.adaptive.v1`
- Stage05 workflow state machine
- Stage06 Change lifecycle
- current-runtime-request-flow
- semantic-commit-dry-run
- Stage20 upgrade lifecycle

对每个说明：
- 中文解释
- 当前状态
- 输入/步骤
- 是否自动执行
- 当前最大可达状态/限制

另外单独写：
`Understand → Collect → Plan → Decide → Execute → Validate → Deliver`
为 Documentation Target User Journey（目标用户旅程），当前不是已实现 Runtime 自动编排。

## 交叉链接

D1 文档之间建立真实相对链接。
不要链接到尚不存在的 D2/D3 文档，除非明确标记：
`（D2/D3 后续生成）`。

## Gap 保留

D0 的 9 个 `DOC-GAP-CANDIDATE` 全部保留。
D1 不修复、不隐藏、不重命名成“已完成”。

如果 D1 新发现事实缺口：
- 记录为 `D1-DOC-GAP-CANDIDATE-*`
- 不修改 Banyan Core 来迎合文档。

## 禁止事项

不允许：
- 修改 `banyan-framework/src/**`
- 修改 `banyan-framework/policies/**`
- 修改 Runtime / Permission / Git safety
- 修改 `.banyan/**`
- 迁移 `docs/project/**`
- 实现 WebUI `/help`
- 创建完整 `user-guide/**` 和 `scenarios/**`
- 修改 version pointer
- Final Activation
- 删除 `.banyan-refactor`

## 验证

至少执行：

1. Markdown 文件存在性检查。
2. 相对链接检查。
3. D0 中关键枚举/ID 与 D1 Reference 一致性检查。
4. 搜索是否存在把 `FROZEN_CONTRACT` 误写为 `IMPLEMENTED` 的明显错误。
5. 搜索是否把 35 CAP-* 写成“35 个 Skill”。
6. 搜索是否声称 `/help` 已实现。
7. 搜索是否声称完整自然语言自动编排已实现。
8. 搜索 Role 是否被描述为 Authorization。
9. 确认仅修改 `banyan-framework/docs/**`。

## 完成报告

生成：

```text
banyan-framework/docs/D1_FOUNDATION_ACCEPTANCE_REPORT.md
```

至少包括：
- 新增/修改文件
- 验证结果
- D0 事实一致性
- 仍保留的 9 个 DOC-GAP-CANDIDATE
- 新发现 Gap
- 需要 Human Decision 的术语/命名问题
- Git diff 范围声明

完成后停止，不进入 D2。

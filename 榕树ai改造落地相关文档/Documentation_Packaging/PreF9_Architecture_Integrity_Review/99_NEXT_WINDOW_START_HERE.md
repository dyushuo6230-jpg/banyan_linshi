# Banyan / 榕树 AI — Pre-F9 下一窗口从这里开始 v2.1

## 当前状态

- F1～F8 v1.0：Original Frozen Baseline，保持不变。
- Phase 0：完成。
- Audit Batch 1：正在逐 Patch 审批。
- `B1-PATCH-01`：`HUMAN_APPROVED`
- `B1-PATCH-02`：`HUMAN_APPROVED`
- `B1-PATCH-02-SUP-01`：`HUMAN_APPROVED`
- `B1-PATCH-03`：`HUMAN_APPROVED`
- `B1-PATCH-04`：`HUMAN_APPROVED`
- `B1-PATCH-05`：`HUMAN_APPROVED`

## 已批准正式 Patch

### AUDIT-PATCH-001

文件：

`10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-001_Assignment_Binding_Resolution.md`

批准内容：

- Assignment 成为 F1 First-Class Object Family；
- Assignment = Responsibility Allocation；
- Binding = 受治理 Adoption / Association / Constraint；
- Resolution = Current Effective Result 解析；
- Generic RoleBinding / SkillBinding 在目标架构退休；
- 历史语义 No-Loss Mapping；
- Durable Protected Assignment / Binding Mutation → F7；
- Task-scoped 动态 Assignment / Resolution 不自动进入 F7。

## 当前候选


### B1-PATCH-02-SUP-01

`Configuration Profile` 运行维护责任补充候选：

- 默认由 Banyan / AI 在治理下维护；
- AI Maintenance != Autonomous Authority；
- 用户只介入真正的语义 / 采用 / Authority / 高影响选择；
- 项目局部差异不默认写回共享 Profile。

文件：

`04_B1_PATCH02_SUP01_MAINTENANCE_RESPONSIBILITY_CANDIDATE.md`

### AUDIT-PATCH-003

文件：

`10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-003_StableID_Revision_Version_CurrentEffective.md`

批准内容：

- Stable ID（稳定标识）= Semantic Subject Identity（语义主体身份）；
- Revision（修订）= 同一 Stable Subject 的受治理可寻址状态节点；
- Version（版本）= Governed Release Coordinate（受治理发布坐标）；
- Version != Revision；
- 不是每个 Revision 都需要发布 Version，也不是所有对象都必须 Versioned（版本化）；
- Published Exact Version（已发布精确版本）不得静默重绑定；
- Latest（最新）必须显式限定排序域；
- All Latest Forms != Current Effective；
- Current Effective（当前有效）= Scope / Context-aware Derived Resolution Result（范围 / 上下文相关的派生解析结果）；
- Version Pin / Constraint（版本固定 / 约束）是解析输入，Effective Version（有效版本）是解析结果；
- Revision Lineage != Supersession；
- Superseded != Deleted；
- Exact Historical Pin 不因 Supersession 自动重定向。

### AUDIT-PATCH-004

文件：

`10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-004_Rule_Policy_Module_Engineering_Standard.md`

批准内容：

- Rule Entry（规则条目）= 最小稳定、可寻址、可治理的规则语义单元；
- 不新增 `RuleDefinition（规则定义）` 顶级类型；
- PolicyDefinition（策略定义）围绕明确治理目标组织一个或多个 Rule Entry；
- Rule Module（规则模块）= 最小连贯知识责任 / 组织 / 加载 / 维护边界；
- Rule Entry 默认一个 Canonical Primary Module（正式主模块），但可被多个 Policy（策略）引用；
- Rule System（规则系统）= 独立知识治理 / 解析规则空间，不按技术栈爆炸；
- Rule Effect（规则效果）继续使用多维解析，不退化成单一 Priority（优先级）；
- Engineering Standard（工程规范）继续是独立受治理工程语义领域；
- 不新增 `StandardDefinition（规范定义）`；
- Engineering Standard Pack（工程规范包）= 规范内容组合 / 分发层；
- Engineering Standard Pack != ConfigurationProfileDefinition（配置组合定义）；
- Shared Engineering Standard Pack != Project Current Effective Engineering Standards；
- AI Maintenance（AI 维护） != Authority（权威）；
- Future AI Learning（未来 AI 学习）只能产生 Candidate（候选），不能自动晋升正式 Rule / Policy。


### AUDIT-PATCH-005

文件：

`10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-005_Dynamic_Workflow_Choice_Informed_Decision.md`

批准内容：

- Dynamic Workflow Composition（动态工作流组合）是 Banyan-wide（全局）能力；
- AI 只能动态组合已有受治理 WorkflowDefinition / Subworkflow / Control Semantics（工作流定义 / 子工作流 / 控制语义），不得运行时自动发明新的 Canonical WorkflowDefinition（正式工作流定义）；
- Workflow Candidate（工作流候选）必须先经过 Governance / Policy / Authority / Scope / Reliability（治理 / 策略 / 权威 / 范围 / 可靠性）过滤；
- Multiple Candidates（多个候选）不自动触发 Informed Decision（知情决策）；
- 只有多个 Valid（合法）且 Materially Distinct（具有实质差异）的候选才形成用户可感知 Workflow Choice（工作流选择）；
- Workflow Choice Preference（工作流选择偏好）第一版基础模式为 AUTO（自动选择）和 ASK_WHEN_MULTIPLE_VALID（多个实质差异合法方案时询问）；
- 单一合法、实质等价和可确定性解析路径默认自动处理；
- User Explicit Choice / Auto Intent（用户明确选择 / 自动意图）可形成 Task-level Override（任务级覆盖）；
- Workflow Choice Preference != Execution Governance Mode（工作流选择偏好 ≠ 执行治理模式）；
- Selected Workflow（选中的工作流）不等于 Product Decision / Approval / Apply Authorization / Runtime Permission（产品决策 / 批准 / 应用授权 / 运行时权限）；
- AUTO 不得绕过 Mandatory Governance（强制治理）、Reliability Floor（可靠性底线）或静默扩大 Scope（范围）；
- F11 后续负责具体 Control Plane UX（控制面交互）。


## 新窗口恢复顺序

1. GitHub F1～F8 v1.0 Freeze Pack
2. `00_AUDIT_GOVERNANCE_AND_PACKAGING_PROTOCOL.md`
3. `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-001_Assignment_Binding_Resolution.md`
4. `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-002_Configuration_Profile.md`
5. `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-003_StableID_Revision_Version_CurrentEffective.md`
6. `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-004_Rule_Policy_Module_Engineering_Standard.md`
7. `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-005_Dynamic_Workflow_Choice_Informed_Decision.md`
5. `01_BATCH01_WORKING_CORRECTION_PROPOSAL.md`
6. 其余最新审批稿 / Patch
7. `04_B1_PATCH02_SUP01_MAINTENANCE_RESPONSIBILITY_CANDIDATE.md`
8. `05_B1_PATCH03_APPROVAL_DRAFT.md`
9. 审阅 B1-PATCH-03；补充候选保持未批准状态

## 下一步

不要重新讨论 B1-PATCH-01，除非发现新的明确冲突。

下一步直接进入：

`B1-PATCH-05 — Dynamic Workflow Composition × Workflow Choice Preference × Informed Decision`

完整修正设计与审批讨论。

## 固定禁止事项

- Implementation：禁止
- RP2：禁止
- Authority Cutover：禁止
- Final Activation：禁止
- Canonical Replacement：禁止
- Legacy Retirement：禁止


### B1-PATCH-05

已形成完整审批稿：

`07_B1_PATCH05_APPROVAL_DRAFT.md`

核心：

- Dynamic Workflow Composition（动态工作流组合）保持 Banyan-wide（全局）能力；
- Multiple Candidates（多个候选）不自动触发 Informed Decision（知情决策）；
- 新增 Workflow Choice Preference（工作流选择偏好）；
- 基础模式：AUTO（自动选择）/ ASK_WHEN_MULTIPLE_VALID（多个实质差异合法方案时询问）；
- Selected Workflow（选中的工作流）不等于 Product Decision / Approval / Apply Authorization / Runtime Permission；
- AUTO 不得绕过强制治理或静默扩大 Scope（范围）。

下一步：

审阅 `07_B1_PATCH05_APPROVAL_DRAFT.md`，由用户决定是否 `B1-PATCH-05 HUMAN_APPROVED`。


## 当前下一步

Audit Batch 1 的五个主 Patch（补丁）均已 HUMAN_APPROVED（人工批准）。

仍有一个未决补充候选：

`B1-PATCH-02-SUP-01 — Configuration Profile 运行维护责任补充`

在进入 Batch 1 Final Closeout（最终收口）前，下一步应先审阅该补充候选，决定：

- 是否直接 HUMAN_APPROVED；
- 是否修改后批准；
- 或明确 RETIRE / MERGE（退役 / 合并）到其他正式 Patch。

不得因为五个主 Patch 已批准就自动将该补充候选视为已批准。


## Audit Batch 1 Final Closeout

第一批审计已正式收口。

Closeout 文件：

`08_BATCH01_FINAL_CLOSEOUT.md`

正式补充 Patch：

`10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-002-SUP-01_Configuration_Profile_Maintenance_Responsibility.md`

当前 Batch 1 全部批准项：

- AUDIT-PATCH-001
- AUDIT-PATCH-002
- AUDIT-PATCH-002-SUP-01
- AUDIT-PATCH-003
- AUDIT-PATCH-004
- AUDIT-PATCH-005

F1～F8 v1.0 保持不变。

下一步：

`Audit Batch 2 — Authority / Truth / Decision / Governance`
（权威 / 真相 / 决策 / 治理）

进入 Batch 2 前仍执行四源对账，不提前进入 F9 Implementation / RP2 / Authority Cutover / Final Activation。

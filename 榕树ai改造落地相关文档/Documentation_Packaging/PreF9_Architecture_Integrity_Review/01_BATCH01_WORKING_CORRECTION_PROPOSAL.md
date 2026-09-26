# Banyan / 榕树 AI — Audit Batch 1 修正方案工作稿 v0.3

> 状态：WORKING  
> F1～F8 v1.0 仍为 Original Frozen Baseline，不得直接修改。

## 当前 Patch 状态

### B1-PATCH-01 — HUMAN_APPROVED

Assignment / Binding / Resolution（指派 / 绑定 / 解析）统一边界；
Generic RoleBinding / SkillBinding（泛化角色绑定 / 技能绑定）在目标架构退休。

正式 Patch：

`10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-001_Assignment_Binding_Resolution.md`

已批准核心：

- Assignment 成为 F1 First-Class Object Family；
- Assignment = Responsibility Allocation；
- Binding = 受治理 Adoption / Association / Constraint 关系；
- Resolution = Current Effective Result 解析；
- Generic RoleBinding / SkillBinding 退休；
- 历史语义通过 No-Loss Mapping 保留；
- Durable Protected Assignment / Binding Mutation → F7；
- Task-scoped 动态 Assignment / Resolution 不自动升级为 F7 Change。

---

### B1-PATCH-02 — HUMAN_APPROVED

ConfigurationProfileDefinition（配置组合定义）候选新增为 F3 第 11 个 DefinitionArtifact Type；
F4 FAST / NORMAL / CONTROLLED Profile 术语改为 Execution Governance Mode（执行治理模式）候选。

正式 Patch：

`10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-002_Configuration_Profile.md`

---


### B1-PATCH-02-SUP-01 — CANDIDATE / NOT HUMAN_APPROVED

Configuration Profile（配置组合档）运行维护责任补充候选：

- ConfigurationProfileDefinition 默认由 Banyan / AI 在治理下系统维护；
- 用户不承担日常手工同步、引用整理、影响分析和任务级解析；
- AI Maintenance（AI 维护） != Autonomous Authority（自主权威）；
- 项目局部差异优先进入 ProjectProfileInstance / Overlay，不污染共享 Profile；
- 新 Profile 版本不会静默升级项目。

候选文件：

`04_B1_PATCH02_SUP01_MAINTENANCE_RESPONSIBILITY_CANDIDATE.md`

---

### B1-PATCH-03 — HUMAN_APPROVED

Stable ID / Revision / Version / Current Effective
（稳定标识 / 修订 / 版本 / 当前有效）全局共同合同。

正式 Patch：

`10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-003_StableID_Revision_Version_CurrentEffective.md`

---

### B1-PATCH-04 — HUMAN_APPROVED

Rule / Policy / Module / Engineering Standard Pack
（规则 / 策略 / 模块 / 工程规范包）通用治理与组合模型。

正式 Patch：

`10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-004_Rule_Policy_Module_Engineering_Standard.md`

---

### B1-PATCH-05 — HUMAN_APPROVED

Dynamic Workflow Composition × Workflow Choice Preference × Informed Decision
（动态工作流组合 × 工作流选择偏好 × 知情决策）

目标是 Banyan-wide（全局）动态工作流选择机制，不局限开发 / 测试场景。

当前候选原则：

- Banyan 已采用 Goal-oriented Dynamic Workflow；
- AI 可组合已有 Workflow / Subworkflow / Control Semantics，形成 Minimum Valid Workflow Graph；
- AI 不得临时创造新的正式 WorkflowDefinition 或绕过 Mandatory Governance；
- 只有合法 Workflow Candidate 才能进入选择；
- Multiple Candidates != Automatic Informed Decision；
- 只有多个合法候选存在 Material Workflow Difference 时才具有用户选择价值；
- Workflow Choice Preference：
  - AUTO
  - ASK_WHEN_MULTIPLE_VALID
- Preference=ASK 且条件满足时复用 Banyan-wide Informed Decision Protocol；
- 用户只能在合法候选之间选择，不能绕过 Policy / Authority / Reliability Floor；
- Workflow Choice Preference != Governance Mode；
- Control Plane UX 留给 F11；
- Project Default / User Preference / Task-local Override 可作为后续正式设计维度。

---

## 下一步

进入：

`B1-PATCH-05 — Dynamic Workflow Composition × Workflow Choice Preference × Informed Decision`

完整修正设计与审批讨论。

B1-PATCH-01 不再回到 Candidate，除非后续审计发现明确冲突并通过新的 governed superseding patch 处理。


B1-PATCH-05 正式 Patch：

`10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-005_Dynamic_Workflow_Choice_Informed_Decision.md`


---

## Batch 1 当前收口状态

当前已 HUMAN_APPROVED（人工批准）：

- AUDIT-PATCH-001 — Assignment / Binding / Resolution
- AUDIT-PATCH-002 — Configuration Profile
- AUDIT-PATCH-003 — Stable ID / Revision / Version / Current Effective
- AUDIT-PATCH-004 — Rule / Policy / Module / Engineering Standard
- AUDIT-PATCH-005 — Dynamic Workflow Composition × Workflow Choice Preference × Informed Decision

仍未批准：

- AUDIT-PATCH-002-SUP-01 — Configuration Profile 运行维护责任补充（HUMAN_APPROVED）

补充候选已完成 HUMAN_APPROVED；Audit Batch 1 已通过 `08_BATCH01_FINAL_CLOSEOUT.md` 正式收口。

# 榕树 AI 改造阶段文档生成清单 v1.9.1

> 用途：后续 00～20 逐阶段生成 Stage Delivery Pack 的独立权威索引。  
> 权威来源：《榕树AI多编辑器AI软件工程框架改造总纲指导方案_v1.9.1.md》第 25 节。  
> 使用方式：**一次只生成、执行、验收一个 Stage**；下一个 Stage 必须消费上一阶段真实 `ACCEPTANCE_REPORT + NEXT_STAGE_HANDOFF`。  
> 重要：本清单只规定“需要生成什么”，不提前伪造 Inventory、Diff、Evidence、Migration Result、Commit Result 或 Acceptance Result。  
> Freeze Audit：v1.9.1 不新增 Stage，不扩展功能范围，只修正 Bootstrap Trace/Register、Semantic Commit Policy Owner、Capability Lifecycle、Git Identity 缺失行为和 Dependency Matrix 用词一致性。  
> 兼容：已经生成的 Stage 00 v1.8 Delivery Pack 与 v1.9.1 兼容，无需重新生成。

---

# 25. 后续必须生成的阶段文档与物资清单

本节是后续逐阶段生成文档的**唯一权威文件名清单**。如果某个“条件型”文档经 Precheck 证明不适用，应在 `STAGE_MANIFEST.yaml` 标记 `NOT_APPLICABLE + reason`，而不是生成空文件。

## 25.1 每个阶段统一拥有的 Common Pack

除明确 `NOT_APPLICABLE` 外，每阶段统一包含：

```text
STAGE_MANIFEST.yaml
STAGE_PLAN.md
PRECHECK_AND_SCOPE.md
VALIDATION_AND_ROLLBACK.md
ACCEPTANCE_REPORT.md        # 真实施工完成后生成
```

涉及写入、迁移或多步骤执行时再强制：

```text
EXECUTION_RUNBOOK.md
MIGRATION_MAP.md
COMPATIBILITY_MATRIX.md
DATA_RECONCILIATION.md
```

`ACCEPTANCE_REPORT.md` 不在施工前预填“通过”。

### 25.1A 条件型施工物资默认适用矩阵

以下是默认要求；真实 Precheck 可以用 `NOT_APPLICABLE + reason` 收口，但不能静默省略。

| Stage | Runbook | Migration Map | Compatibility Matrix | Data Reconciliation |
|---|---|---|---|---|
| 00 | 必须 | N/A | N/A | N/A |
| 01 | 必须 | N/A | N/A | N/A |
| 02 | 条件 | N/A | N/A | N/A |
| 03 | 条件 | N/A | 条件 | N/A |
| 04 | 必须 | 必须 | 条件 | 条件 |
| 05 | 必须 | N/A | N/A | N/A |
| 06 | 必须 | 条件 | 必须 | N/A |
| 07 | 必须 | 必须 | 必须 | 条件 |
| 08 | 必须 | 条件 | 必须 | N/A |
| 09 | 必须 | 必须 | 必须 | 条件 |
| 10 | 必须 | 必须 | 必须 | 条件 |
| 11 | 必须 | 必须 | 必须 | 必须 |
| 12 | 必须 | 条件 | 必须 | 条件 |
| 13 | 必须 | N/A | 条件 | 条件 |
| 14 | 必须 | N/A | 必须 | N/A |
| 15 | 必须 | 条件 | 必须 | N/A |
| 16 | 必须 | 条件 | 必须 | 条件 |
| 17 | 必须 | 必须 | 必须 | 条件 |
| 18 | 必须 | 条件 | 必须 | 条件 |
| 19 | 必须 | 条件 | 必须 | 必须 |
| 20 | 必须 | N/A | 必须 | N/A |

说明：这里的 `Data Reconciliation` 只在有结构化导入/索引/历史数据重建时真正生成；“条件”不意味着可忽略，而是由该 Stage Precheck 明确决定。

## 25.2 全改造工程只维护一份的跨阶段物资

```text
MIGRATION_REGISTER.yaml
BANYAN_REFACTOR_TRACE.yaml
AI_CAPABILITY_PRESERVATION_MATRIX.yaml
AI_ARTIFACT_MIGRATION_MATRIX.yaml
LEGACY_BEHAVIOR_REGRESSION_MATRIX.yaml
DOCUMENTATION_SOURCE_MAP.yaml        # Stage 20 生成/维护
REFRACTOR_PLAN_CHANGE/*              # 实际命名由 Stage 03 冻结
```

路径说明：

- Stage 00～正式 Project Instance 路径冻结前，`MIGRATION_REGISTER / BANYAN_REFACTOR_TRACE` 可以存在于 `REFRACTOR_CONTROL_ROOT` 的 Bootstrap 位置；
- 正式 `.banyan/migrations/` 路径冻结后必须迁移并校验 lineage/hash；
- 迁移完成后不得保留两个可写真源。

最终阶段额外形成：

```text
CORE_PURITY_REPORT
CROSS_PROJECT_PORTABILITY_REPORT
CROSS_EDITOR_EQUIVALENCE_REPORT
FINAL_ROLLBACK_REHEARSAL_REPORT
TECHNICAL_RELEASE_CANDIDATE_REPORT
FINAL_RELEASE_REPORT
```

## 25.3 Stage 00：安全基线

阶段主文档：

```text
00_改造安全基线与仓库保护.md
```

专项：

```text
00-A_Repository_Baseline与Protected_Paths.md
00-B_Snapshot_Hash_Checkpoint与Rollback.md
```

执行后物资：

```text
BASELINE_MANIFEST
PROTECTED_PATHS_MANIFEST
CHECKPOINT_RECORD
DISCOVERY_SCOPE_BASELINE
```

> 兼容说明：已生成的 Stage 00 v1.8 Delivery Pack 与 v1.9.1 Contract 兼容，不需要重新生成；执行时以上位总纲 v1.9.1 为准，并在 Acceptance Report 记录兼容版本。

## 25.4 Stage 01：资产盘点

```text
01_AI资产全量盘点与方案裁剪.md
01-A_AI_Asset_Inventory_Schema.md
01-B_Legacy_Classification与Core_Candidate_Mapping.md
01-C_Duplicate_Conflict_Gap_Report.md
01-D_Reference_Project与Generic_Core边界审计.md
01-E_AI_Generated_Artifact_Inventory.md
01-F_AI_Capability_Discovery_Report.md
01-G_AI_Asset_Migration_Master_Map.md
01-H_Discovery_Coverage与NoLoss_Preliminary_Gate.md
01-I_Git_Identity与AI提交现状盘点.md
```

执行后物资：

```text
AI_ASSET_INVENTORY
LEGACY_CLASSIFICATION_REPORT
CORE_CANDIDATE_REPORT
CONFLICT_GAP_REPORT
LEGACY_AI_CAPABILITY_INVENTORY
AI_GENERATED_ARTIFACT_INVENTORY
OPERATIONAL_ARTIFACT_INVENTORY
DISCOVERY_COVERAGE_REPORT
PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX
PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX
GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY
```

## 25.5 Stage 02：目标架构

```text
02_Banyan目标架构与目录定稿.md
02-A_Framework_Distribution与Project_Instance边界.md
02-B_Target_Layout与Package_Strategy.md
02-C_Source_Role与Truth_Model.md
02-D_Capability_Ownership与Dependency_Map.md
02-E_Extension_Provider_Interface.md
02-F_Legacy_Capability_Architecture_Coverage_Gate.md
02-G_Contribution_Identity与Commit_Provenance架构.md
```

## 25.6 Stage 03：Artifact / Schema / Registry

```text
03_AI产物契约Schema与Registry.md
03-A_Artifact_Metadata_Schema.md
03-B_Registry_Schema与Discovery.md
03-C_Version_Dependency_Compatibility.md
03-D_Generated_Artifact_Contract.md
03-E_Validation_Error与Explanation_Schema.md
03-F_Refactor_Plan_Change_Schema.md
03-G_Legacy_Capability与Artifact_Migration_Schema.md
03-H_Parallel_Draft_Workspace与Reference_Integrity_Schema.md
03-I_Git_Identity_Contributor_Profile与Commit_Provenance_Schema.md
```

## 25.7 Stage 04：Project Instance / Onboarding / Migration

```text
04_Project_Instance_Source_Mapping与Profile.md
04-A_Project_Instance_Schema.md
04-B_Source_Mapping与Project_Profile.md
04-C_Project_Onboarding与Discovery.md
04-D_Legacy_Variable_Migration.md
04-E_Migration_Importer_Contract.md
04-F_Framework_Version_Lock与Upgrade.md
04-G_Contributor_Profile与Git_Identity_Discovery.md
```

## 25.8 Stage 05：Adaptive Workflow / Decision

```text
05_Adaptive_Workflow_Orchestrator与决策路由.md
05-A_Task_Classification与Delta_Detection.md
05-B_Workflow_Atom与Workflow_Composer.md
05-C_Workflow_Family_Catalog.md
05-D_Workflow_Graph_Node_Contract与Runtime_State.md
05-E_ReRoute_Escalation_DeEscalation与Reconciliation.md
05-F_Decision_Interrupt_Pause_Resume与Partial_Blocking.md
05-G_Experiment_Mode与Candidate_Delta.md
05-H_Dependency_Invalidation与Checkpoint.md
05-I_Workflow_Governance_Confidence与Evidence.md
05-J_Adaptive_Workflow验收场景集.md
05-K_Parallel_Draft_Workspace_Runtime.md
05-L_Semantic_Commit_Planner与Batch_Commit_Workflow.md
```

## 25.9 Stage 06：Change Provider / OpenSpec / Canonical Apply

```text
06_Change_Workspace_Provider_OpenSpec与Canonical_Apply.md
06-A_Change_Workspace_Provider_Contract.md
06-B_OpenSpec_Reference_Integration.md
06-C_Change_Necessity与Change_CR_Mapping.md
06-D_Canonical_Apply_Contract.md
06-E_Discussion_Pack_Contract.md
06-F_Final_Review_Pack_Contract.md
06-G_Change_Cancel_Archive与History.md
06-H_Change_Governance_Integration.md
06-I_Parallel_Draft_Promotion_Contract.md
06-J_Batch_Canonical_Reconciliation.md
```

## 25.10 Stage 07：Reference Project v3.1 Compatibility

```text
07_Reference_Project_v3.1超级提示词拆分与兼容层.md
07-A_v3.1_Inventory与Semantic_Mapping.md
07-B_Role_Policy_Skill_Workflow_State_Split.md
07-C_Legacy_Compatibility_Loader.md
07-D_Numbering_Status_Baseline_Compatibility.md
07-E_Shadow_Semantic_Equivalence.md
07-F_Legacy_Retirement与Rollback.md
07-G_v3.1功能能力完整保留矩阵.md
07-H_v3.1_Legacy_Feature_Regression_Cases.md
07-I_Parallel_Draft_Workspace迁移.md
07-J_Worklog_Handover_Progress兼容迁移.md
07-K_Legacy_Safety_Policies兼容映射.md
07-L_AI_Generated_Artifact迁移矩阵.md
```

## 25.11 Stage 08：PRD × UI_SPEC Governance

```text
08_PRD与UI_SPEC协同及UI版本治理.md
08-A_PRD_UI职责与冲突裁决.md
08-B_Design_Revision管理规范.md
08-C_UI_SPEC版本治理规范.md
08-D_Effective_UI_Contract生成规则.md
08-E_Batch版本冻结与升级规则.md
08-F_UI_Change_Classification.md
08-G_UI版本治理验收与回滚.md
```

## 25.12 Stage 09：UI Design Intelligence

```text
09_UI_Design_Intelligence子系统整合.md
09-A_UI_Protocol归并与职责矩阵.md
09-B_UI_Design_Pack_Schema.md
09-C_Frontend_Layout_Guidance_Standard.md
09-D_Implementation_IR与Compiler.md
09-E_UI_Framework_Adapter_Contract.md
09-F_Visual_Validation与Repair_Loop.md
09-G_Historical_UI_Artifact_Compatibility.md
09-H_UI_Intelligence_Acceptance.md
```

## 25.13 Stage 10：Project Guide / Knowledge Publishing

```text
10_Project_Guide与知识发布体系改造.md
10-A_现有Plain体系审计与问题报告.md
10-B_Project_Guide信息架构设计.md
10-C_Project_Guide编写规范.md
10-D_Project_Guide文章类型与模板规范.md
10-E_GUIDE_SYNC与来源图谱设计.md
10-F_旧Plain文档迁移映射.md
10-G_Project_Guide质量验收规范.md
10-H_Project_Guide迁移回滚与旧体系退役方案.md
```

## 25.14 Stage 11：SQLite / Trace / Historical Migration

```text
11_SQLite索引Trace与历史数据迁移.md
11-A_Index_Schema与Source_Parsers.md
11-B_Trace_Graph与Relationship_Model.md
11-C_Historical_Import与Migration_Manifest.md
11-D_Code_Trace与Reverse_Query.md
11-E_GUIDE_SYNC与Impact_Index.md
11-F_Rebuild与Integrity_Check.md
11-G_Data_Reconciliation.md
11-H_Index_Migration_Rollback.md
```

## 25.15 Stage 12：Context / Memory / Token

```text
12_动态Context记忆与Token优化.md
12-A_Context_Builder与Context_Plan.md
12-B_Context_Policy与Token_Budget.md
12-C_Runtime_Context与Session_Recovery.md
12-D_Memory_Tiers与Promotion.md
12-E_Project_Fact_Retrieval.md
12-F_Context_Explainability与Freshness.md
12-G_Context_Quality_Acceptance.md
12-H_Legacy_Handover与Session_Recovery兼容.md
```

## 25.16 Stage 13：Evidence / Impact / Event / Learning

```text
13_EvidenceImpact与Prompt学习闭环.md
13-A_Evidence_Model.md
13-B_Impact_Analysis_Engine.md
13-C_Event_Activity_Model.md
13-D_Prompt_Learning与Review.md
13-E_Lesson_Pattern_Promotion.md
13-F_Completion_Claim与Evidence_Gate.md
13-G_Evidence_Trace_Audit_Integration.md
13-H_Test_Integrity与Temporary_Stub_Governance.md
13-I_Legacy_Worklog_Event_Evidence_Mapping.md
```

## 25.17 Stage 14：Permission / Governance

```text
14_AI工作模式权限与Governance_Check.md
14-A_Work_Mode与Permission_Model.md
14-B_Governance_Check_Engine.md
14-C_Protected_Path与Write_Guard.md
14-D_Decision_Change_Gate_Integration.md
14-E_High_Risk_Operation_Policy.md
14-F_Governance_Audit与Evidence.md
14-G_Governance_Acceptance_Cases.md
14-H_Reference_Integrity与Legacy_Safety_Gates.md
14-I_Git_Commit_Governance与Safety_Gate.md
```

## 25.18 Stage 15：CLI / Runtime API / Compiler / Adapter Framework

```text
15_Banyan_CLI_Runtime_API规则编译器与Adapter框架.md
15-A_CLI_Command_Model.md
15-B_Runtime_API_Contract.md
15-C_Rule_Compiler.md
15-D_Adapter_Framework.md
15-E_Generated_Output_Drift_Check.md
15-F_Provider_Capability_Interface.md
15-G_Framework_Distribution与Versioning.md
15-H_CLI_Runtime_Acceptance.md
15-I_Banyan_Commit_CLI与统一提交策略.md
```

## 25.19 Stage 16：Control Plane / WebUI

```text
16_Banyan_Control_Plane与动态工程看板.md
16-A_Project_Entry_UI与Wizard_Flow.md
16-B_Project_Discovery_Source_Mapping与Legacy_Migration_UI.md
16-C_Control_Plane信息架构.md
16-D_WebUI字段权限与Explanation_Contract.md
16-E_Multi_Dimensional_Progress_Model.md
16-F_Event_Activity_Freshness_Model.md
16-G_Control_Plane_Command与Governance集成.md
16-H_WebUI安全权限与Secrets.md
16-I_Control_Plane验收与回滚.md
16-J_Runtime_Workflow可视化与ReRoute时间线.md
16-K_Migration_Center_UI与变量迁移视图.md
16-L_Parallel_Draft_Workspace_UI.md
16-M_Capability_Artifact_NoLoss_Migration_UI.md
16-N_Contributor_Commit_Provenance_UI.md
```

## 25.20 Stage 17：Reference Project Cursor Pilot

```text
17_Cursor零回退迁移.md
17-A_Current_Cursor_Inventory.md
17-B_Cursor_Adapter_Mapping.md
17-C_Rule_Semantic_Equivalence.md
17-D_Cursor_Shadow_Mode.md
17-E_Real_Task_Pilot.md
17-F_Cursor_Cutover与Rollback.md
17-G_Cursor_Acceptance.md
```

## 25.21 Stage 18：Codex / Claude / Generic Adapter

```text
18_CodexClaude与GenericAdapter适配.md
18-A_Codex_Adapter.md
18-B_Claude_Adapter.md
18-C_Generic_Adapter.md
18-D_Adapter_Capability_Compatibility_Matrix.md
18-E_Cross_Editor_Semantic_Equivalence.md
18-F_Adapter_Drift与Rebuild.md
18-G_Multi_Editor_Acceptance.md
```

## 25.22 Stage 19：Technical Final Acceptance / Release Candidate

```text
19_全链路技术验收回滚Legacy收口与Release_Candidate.md
19-A_Final_Requirement_Trace_Audit.md
19-B_Core_Purity_Audit.md
19-C_Existing_Project_E2E.md
19-D_New_Project_E2E.md
19-E_Cross_Project_Portability.md
19-F_Multi_Editor_E2E.md
19-G_Rebuild与Disaster_Recovery.md
19-H_Rollback_Rehearsal.md
19-I_Legacy_Retirement_Readiness.md
19-J_Release_Candidate与Bootstrap_Pack.md
19-K_AI_Capability_No_Loss_Audit.md
19-L_AI_Generated_Artifact_Migration_Audit.md
19-M_Legacy_Behavior_Regression_Final_Report.md
19-N_Contribution_Identity与Commit_Provenance_Acceptance.md
```


## 25.23 Stage 20：Usage Documentation / Adoption / Final Release

```text
20_榕树AI使用说明体系与Final_Release.md
20-A_快速开始与核心概念.md
20-B_新项目初始化与已有项目接入迁移.md
20-C_日常开发与Adaptive_Workflow使用指南.md
20-D_需求变更_Decision_Change与Parallel_Draft指南.md
20-E_PRD_UI_SPEC_设计图与视觉修复指南.md
20-F_Project_Guide_Context_Memory_Progress与Control_Plane指南.md
20-G_多编辑器_Cursor_Codex_Claude_Generic使用指南.md
20-H_管理员配置_变量_权限_安全与Secrets指南.md
20-I_CLI_Runtime_API_WebUI命令与操作参考.md
20-J_迁移_升级_回滚_灾难恢复与故障排查.md
20-K_Artifact_状态_Schema与概念词典.md
20-L_Extension_Provider_Skill_Adapter开发指南.md
20-M_典型场景_最佳实践与FAQ.md
20-N_使用说明一致性_Drift与Final_Release验收.md
20-O_Git提交_贡献身份与AI分批提交指南.md
```

执行后物资：

```text
DOCUMENTATION_SOURCE_MAP
DOCUMENTATION_COVERAGE_REPORT
DOCUMENTATION_DRIFT_REPORT
BANYAN_USAGE_DOCUMENTATION_PACK
FINAL_RELEASE_REPORT
```

## 25.24 后续你需要主动提供什么

当前进入 Stage 00 前，**不需要再人工制作新的项目说明文档**。

默认由 Codex / Banyan 在真实仓库 Precheck 中读取已有：

```text
Git / Git History / Git Identity / Commit Convention
Code
Current Governance Docs
Rules / Skills / Prompts / Commands / Hooks
PRD / DEC / ADR / CR
UI Assets / UI Specs / Design Packs / Visual Records
Plain / Guide Assets
Progress / Worklog / Handover / Dashboard
AI Generated Canonical / Derived / Operational Artifacts
Tests / Build / CI
```

只有阶段现场产生：

```text
NEEDS_INPUT
CONFLICT
无法自动验证的外部约束
必须由你选择的方案
```

时才让你决策。

因此接下来你的主要动作就是：

> **一次只让我生成一个阶段的 Stage Delivery Pack。**

---

---

# 施工顺序与冻结规则

```text
00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09
→ 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17 → 18 → 19 → 20
```

规则：

- 每个 Stage 必须先通过上一 Stage 的 Sequential Gate。
- Dependency Matrix 中额外列出的 Schema / Capability / Evidence 是语义前置，不能被解释成允许跳 Stage。
- 后阶段发现上游 Contract 缺陷必须走 `REFRACTOR_PLAN_CHANGE`。
- Stage 19 只生成 `VERIFIED / RELEASE_CANDIDATE`。
- Stage 20 Documentation/Adoption Gate 通过后才 `FINAL_RELEASE`。

# B1-PATCH-01 — Assignment / Binding / Resolution 完整审批稿 v0.1

> Status: SUPERSEDED_BY_APPROVED_PATCH  
> Approved Patch: `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-001_Assignment_Binding_Resolution.md`

## 1. 修正目标

消除 F1 早期 `RoleBinding / SkillBinding` 宽泛语义与 F4/F8 后续成熟模型之间的歧义，形成 Banyan-wide（全局）一致的：

- Assignment（指派）
- Binding（绑定）
- Resolution（解析）

三分语义。

## 2. Assignment（指派）

### 2.1 Core Classification（核心归类）

新增 `ASSIGNMENT` 为 F1 First-Class Object Family（一等对象家族）：

```text
ARTIFACT
PROJECT_INSTANCE
ASSIGNMENT
BINDING
RUNTIME_EXECUTION
CONTEXT
EVIDENCE_TRACE
INFRASTRUCTURE
```

### 2.2 语义

Assignment 只表达 Responsibility Allocation（责任分配）：

> 某个 Subject（主体）在指定 Scope（范围）与 Lifetime（有效期）内承担某项 Responsibility（责任）。

典型：

`RoleAssignment（角色指派）`

### 2.3 边界

- Assignment != Binding
- Assignment != RuntimeExecution
- RoleAssignment != Permission
- RoleAssignment != Authority
- Assignment 可为 Project-scoped / Task-scoped / Run-scoped，但语义始终是责任承担。
- Assignment 可由 Explicit Assignment（显式指派）或 Responsibility Resolution（责任解析）产生。

## 3. Binding（绑定）

### 3.1 语义

Binding 表达在明确 Scope 下，受治理对象之间持久、可查询、可追踪、可重新解析的：

- Adoption（采用）
- Association（关联）
- Constraint（约束）

关系。

### 3.2 分类原则

Binding 主要按 Relation Purpose（关系语义目的）分类，而不是按技术领域分类。

基础候选家族：

- Source Binding
- Configuration Profile Binding
- Provider Binding
- Version Pin / Version Constraint
- Feature Activation Binding
- Standard Adoption Binding

Domain（领域）与 Scope（范围）作为适用维度，而不是主要类别。

### 3.3 Binding 判定标准

一个关系要成为正式 Binding，原则上应：

- 超出单次瞬时执行仍具有意义；
- 值得被治理、查询、追踪或重新解析；
- 具有明确 Scope / Applicability；
- 不因“关系存在”而自动成为 Current Effective。

### 3.4 边界

- Binding != Assignment
- Binding != Resolution
- Binding != Effective Binding
- Binding != Permission
- Binding != Authority
- temporary runtime selection != durable rebinding

## 4. Resolution（解析）

### 4.1 语义

Resolution 是根据已有：

- Definition
- Assignment
- Binding
- Policy
- Scope
- Context
- Authority
- Compatibility
- Version
- Gate / Constraint

计算 Current Effective Result（当前有效结果）的过程。

### 4.2 输出属性

Resolution Result（解析结果）默认：

- Derived（派生）
- Rebuildable（可重建）
- Scope / Task-aware（范围 / 任务相关）
- Traceable（可追踪）

### 4.3 边界

- Resolution != Execution
- Resolution Result != Canonical Truth
- Resolution Result != Authority
- Latest != Current Effective
- temporary resolved selection != durable mutation

## 5. Generic RoleBinding（泛化角色绑定）退休

目标架构中退休 `Generic RoleBinding`。

无损映射：

- “谁承担 Role” → RoleAssignment
- “某 Workflow / Node 需要某 Role” → RoleRequirement
- “当前最终解析到哪个 Role” → Responsibility Resolution / Resolved Role

禁止继续用 `RoleBinding` 同时表达上述不同语义。

## 6. Generic SkillBinding（泛化技能绑定）退休

目标架构中退休 `Generic SkillBinding`。

无损映射：

- 必须使用某 Skill → SkillRequirement
- 固定具体 Skill → SkillPin
- 排除某 Skill → SkillExclude
- Skill 当前是否适用 → SkillEligibility
- 当前选择哪个 Skill → SkillResolution / ResolvedSkill
- 实际执行一次 Skill → SkillInvocation
- 项目 / 任务默认允许或推荐 Skill → Configuration Profile / Policy / Execution Constraint

`SkillPin / SkillRequirement / SkillExclude` 不重新包装成新的 `Skill*Binding`，避免换名后重新产生同一歧义。

## 7. Cross-Stage Owner Boundary（跨阶段 Owner 边界）

### F1
- 定义 Assignment / Binding 为一等对象家族与共同边界。

### F4
- RoleAssignment 属于 Assignment；
- Role / Skill / Provider 等 Resolution 继续由对应解析语义负责；
- Skill Requirement / Pin / Exclude 属于 Execution Constraint，不属于泛化 Binding。

### F7
- 不成为 Assignment / Binding 的领域 Owner；
- 仅在 Durable Protected Assignment / Binding Mutation（持久受保护指派 / 绑定变更）需要正式修改时，提供 Governed Change / Canonical Apply（受治理变更 / 正式应用）。

### F8
- 继续拥有 Project Instance 相关 Binding 领域语义；
- Binding != Effective Binding；
- Rebinding != Independent Governance Domain。

### F9
- 未来负责检索 Assignment / Binding / Relation、Freshness / Impact Evidence；
- Index Match != Effective Assignment / Binding；
- F9 不获得 Owner / Authority。

### F10
- 消费已解析的 Assignment / Binding / Execution Plan；
- Runtime Permission 不创造 Assignment / Binding 的语义 Authority。

## 8. No-Loss / Compatibility（无损 / 兼容）

- F1 v1.0 历史 `RoleBinding / SkillBinding` 保留为历史原文；
- v1.1 整合时通过本 Patch 标记其目标架构语义已 Superseded（被替代）；
- Legacy 物理记录不在本 Patch 删除；
- F12 未来负责 Legacy Migration / Retirement；
- 任何旧 `RoleBinding / SkillBinding` 迁移前必须先识别其真实语义，再映射到新的明确概念。

## 9. Forbidden Interpretations（禁止解释）

- Assignment 不得被解释为 Authority / Permission。
- Binding 不得被解释为 Current Effective。
- Binding 不得成为所有对象关系的万能容器。
- Resolution 不得创造 Canonical Truth / Authority。
- Generic RoleBinding / SkillBinding 不得继续作为模糊兜底字段。
- 不得建立 Universal Resolver（万能解析器）作为新的 God Object（上帝对象）。
- 不得因为存在 Governance 就把所有 Task-scoped Assignment / Resolution 强制升级为 F7 Change。
- 本 Patch 不授权 Implementation / RP2 / Authority Cutover / Final Activation / Legacy Retirement。

## 10. Integration Target（整合目标）

若 HUMAN_APPROVED：

- F1_Core_Object_Model_Freeze_Pack_v1.1 Candidate
- F4_Orchestration_Semantic_Freeze_Pack_v1.1 Candidate
- F8_Project_Instance_Governance_Freeze_Pack_v1.1 Candidate（以澄清/引用补充为主）
- F7 / F9 / F10 仅保留跨阶段边界与消费约束，不重分 Owner。

## 11. Approval Meaning（批准含义）

批准本 Patch 表示：

1. 接受 Assignment / Binding / Resolution 三分语义；
2. 接受 Assignment 成为 F1 一等对象家族；
3. 接受 Generic RoleBinding / SkillBinding 在目标架构中退休；
4. 接受历史内容保留、通过无损映射迁移，而不是立即物理删除；
5. 接受 Durable Protected Mutation → F7，但动态任务级 Assignment / Resolution 不自动进入 F7；
6. 不授权任何实现或真实迁移。

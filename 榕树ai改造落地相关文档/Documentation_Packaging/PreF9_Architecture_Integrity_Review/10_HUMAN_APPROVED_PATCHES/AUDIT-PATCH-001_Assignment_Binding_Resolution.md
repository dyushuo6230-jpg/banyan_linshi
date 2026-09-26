# AUDIT-PATCH-001 — Assignment / Binding / Resolution

> Patch ID: `AUDIT-PATCH-001`  
> Source Candidate: `B1-PATCH-01`  
> Status: `HUMAN_APPROVED`  
> Approval Scope: Pre-F9 F1～F8 Architecture Integrity & Optimization Review — Audit Batch 1  
> Implementation Authorization: `NO`  
> RP2 Authorization: `NO`  
> Authority Cutover Authorization: `NO`  
> Final Activation Authorization: `NO`  
> Legacy Retirement Authorization: `NO`

---

## 1. Affected Stage（受影响阶段）

### Primary

- F1 — Core Object Model
- F4 — Orchestration Semantic
- F8 — Project Instance Governance

### Cross-stage Boundary / Consumer

- F7 — Governed Change / Canonical Apply
- F9 — Index / Search / Freshness / Impact（未来消费边界）
- F10 — Runtime Permission / Execution（未来消费边界）

本 Patch 不重新分配上述阶段既有 Owner，只收口 Assignment / Binding / Resolution 的全局共同语义。

---

## 2. Problem（问题）

F1 早期 `Binding` 示例包含：

- `RoleBinding`
- `SkillBinding`
- `ProviderBinding`
- `SourceMapping`
- `OverlayBinding`

随着 F4 / F8 架构成熟，原 `RoleBinding / SkillBinding` 已不能无歧义表达其真实语义：

- “谁承担责任”
- “Workflow / Node 需要什么 Role / Skill”
- “某 Skill 是否适用”
- “某次最终解析选择什么”
- “某项目长期采用什么”
- “某次真实执行调用什么”

这些语义不能继续统一塞入泛化 `Binding`。

若保留泛化 `RoleBinding / SkillBinding`，运行时和未来 F9 / F10 会被迫依赖上下文猜测，破坏 Banyan 的对象边界与确定性解析。

---

## 3. Existing Contract（既有冻结合同）

### F1

`Binding` 已是一等对象家族，且 `Binding != Artifact`。

早期示例包括：

```text
RoleBinding
SkillBinding
ProviderBinding
SourceMapping
OverlayBinding
```

### F4

已经冻结：

```text
RoleDefinition != RoleAssignment
```

并明确：

```text
RoleAssignment = subject + scope + time
```

同时：

- Role / Assignment 不授予 Permission / Authority；
- Skill eligibility 是 contextual（上下文相关）；
- Role / Skill / Provider / Binding 使用 late-bound resolution（延迟解析）；
- Resolution 与 Execution 分离。

### F8

已经冻结：

```text
Binding != Effective Binding
```

并发展出：

- Source Binding
- Profile Binding
- Provider Binding
- Version Pin / Binding Constraint
- Feature Activation Binding

因此后续冻结事实已经证明 F1 早期的宽泛 `RoleBinding / SkillBinding` 需要正式语义收口。

---

## 4. Target Contract（目标合同）

### 4.1 Assignment（指派）成为 F1 First-Class Object Family（一等对象家族）

F1 目标一等对象家族增加：

```text
ASSIGNMENT
```

目标结构：

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

### 4.2 Assignment（指派）的唯一核心职责

Assignment 只表达：

> Responsibility Allocation（责任分配）

即：

```text
Subject
+
Responsibility
+
Scope
+
Lifetime
```

典型正式语义：

```text
RoleAssignment
```

Assignment 可以是：

- Project-scoped
- Task-scoped
- Run-scoped

但生命周期变化不得改变其核心语义：**谁在什么范围 / 有效期内承担什么责任。**

Assignment 可来自：

- Explicit Assignment（显式指派）
- Responsibility Resolution（责任解析）

### 4.3 Assignment 边界

```text
Assignment != Binding
Assignment != RuntimeExecution
RoleAssignment != Permission
RoleAssignment != Authority
```

被指派承担某 Role，不自动获得：

- Product Decision Authority
- Apply Authorization
- Runtime Permission
- Source Authority

---

## 5. Binding（绑定）正式语义

Binding 表达：

> 在明确 Scope 下，受治理对象之间具有持续治理价值的 Adoption / Association / Constraint（采用 / 关联 / 约束）关系。

Binding 不是“任意两个对象连一条线”。

成为正式 Binding 的关系原则上应：

- 超出单次瞬时执行仍有语义价值；
- 值得被治理、查询、追踪或重新解析；
- 具有明确 Scope / Applicability；
- 可以参与 Effective Resolution；
- 不因关系记录存在而自动成为 Current Effective。

### 5.1 Binding 分类原则

Binding 主要按 **Relation Purpose（关系语义目的）** 分类，而不是按技术领域分类。

当前基础关系家族包括：

```text
Source Binding
Configuration Profile Binding
Provider Binding
Version Pin / Version Constraint
Feature Activation Binding
Standard Adoption Binding
```

未来可以扩展新的 Binding Kind，但不通过：

```text
FrontendBinding
BackendBinding
DatabaseBinding
```

这类技术栈类别无限扩张 Core。

### 5.2 Domain / Scope

`Domain（领域）` 和 `Scope（范围）` 是 Binding 的适用维度，不是主类型体系。

### 5.3 Binding 边界

```text
Binding != Assignment
Binding != Resolution
Binding != Effective Binding
Binding != Permission
Binding != Authority
Temporary Runtime Selection != Durable Rebinding
```

---

## 6. Resolution（解析）正式语义

Resolution 是：

> 根据已有 Definition / Assignment / Binding / Policy / Scope / Context / Authority / Compatibility / Version / Gate / Constraint 等受治理事实，计算 Current Effective Result（当前有效结果）的过程。

Resolution 不等于 Binding，也不等于 Execution。

### 6.1 Resolution Result（解析结果）

默认属性：

```text
Derived
Rebuildable
Scope-aware
Task-aware when applicable
Traceable
```

### 6.2 Resolution 边界

```text
Resolution != Execution
Resolution Result != Canonical Truth
Resolution Result != Authority
Latest != Current Effective
Temporary Resolved Selection != Durable Mutation
```

Resolution 不得因为“本次选中了某个对象”就自动形成长期 Canonical Binding。

---

## 7. Generic RoleBinding（泛化角色绑定）退休

目标架构中：

```text
Generic RoleBinding = RETIRED
```

### 7.1 No-Loss Mapping（无损映射）

旧 `RoleBinding` 真实语义按实际含义迁移：

| 旧语义 | 新正式语义 |
|---|---|
| 谁承担某 Role | `RoleAssignment` |
| Workflow / Node 需要某 Role | `RoleRequirement` |
| 当前解析到哪个 Role | `Responsibility Resolution / Resolved Role` |

禁止继续使用 `RoleBinding` 同时承载多个不同含义。

---

## 8. Generic SkillBinding（泛化技能绑定）退休

目标架构中：

```text
Generic SkillBinding = RETIRED
```

### 8.1 No-Loss Mapping（无损映射）

| 旧 `SkillBinding` 实际含义 | 新正式语义 |
|---|---|
| 必须使用某 Skill | `SkillRequirement` |
| 固定具体 Skill | `SkillPin` |
| 排除某 Skill | `SkillExclude` |
| 当前 Skill 是否适用 | `SkillEligibility` |
| 当前最终选择哪个 Skill | `SkillResolution / ResolvedSkill` |
| 实际执行一次 Skill | `SkillInvocation` |
| 项目 / 任务默认允许或推荐 Skill | `Configuration Profile / Policy / Execution Constraint` |

### 8.2 禁止换皮恢复

不得在退休 `SkillBinding` 后重新创造：

```text
SkillRequirementBinding
SkillPinBinding
SkillExcludeBinding
```

来重新形成同一个泛化 Binding 问题。

`SkillRequirement / SkillPin / SkillExclude` 属于明确的 Execution Constraint（执行约束）语义。

---

## 9. Supersession（替代关系）

本 Patch 在目标架构中替代 F1 v1.0 对：

```text
RoleBinding
SkillBinding
```

作为泛化 Binding 示例的继续使用。

注意：

- F1 v1.0 原文件不修改；
- 历史原文继续保留；
- 新的 Current Architecture Baseline 未来由 v1.1 整合包吸收本 Patch；
- `ProviderBinding / Source Binding / Profile Binding / Version Constraint / Feature Activation Binding` 等仍保留为合法 Binding 语义。

---

## 10. Compatibility（兼容规则）

### 10.1 历史资料

旧 Stage、Legacy 配置、旧文档中存在：

```text
RoleBinding
SkillBinding
```

不因此立即非法或被物理删除。

读取旧数据时必须：

```text
Legacy Term
↓
Semantic Identification
↓
No-Loss Mapping
↓
New Explicit Semantic
```

### 10.2 Legacy Retirement

本 Patch：

```text
DOES NOT AUTHORIZE LEGACY RETIREMENT
```

物理迁移、字段删除、历史兼容清理仍由后续 F12 或其正式 Owner 处理。

---

## 11. Cross-Stage Owner Boundary（跨阶段 Owner 边界）

### F1

负责：

- Assignment / Binding 一等对象家族；
- 两者的全局共同边界。

### F4

负责：

- RoleAssignment 的编排语义；
- Responsibility Resolution；
- Skill Requirement / Pin / Exclude 等执行约束；
- Role / Skill / Provider 等对应 Resolution；
- 不恢复泛化 RoleBinding / SkillBinding。

### F7

F7 不是 Assignment / Binding 的领域语义 Owner。

只有在：

```text
Durable Protected Assignment / Binding Mutation
```

需要正式持久修改时，才进入：

```text
Governed Change / Canonical Apply
```

Task-scoped 动态 Assignment / Resolution 不因具备治理语义而自动成为 F7 Change。

### F8

继续拥有：

- Project Instance Binding
- Source / Profile / Provider / Version / Feature 等项目实例关系语义；
- `Binding != Effective Binding`；
- `Rebinding != Independent Governance Domain`。

### F9

未来仅负责：

- 查找 Assignment / Binding / Relation；
- Freshness Evidence；
- Impact Evidence；
- Index / Retrieval。

不得：

```text
Index Match = Effective Assignment / Binding
```

也不得获得 Authority。

### F10

消费已经解析出的：

- Assignment
- Binding
- Effective Result
- Execution Plan

Runtime Permission / Execution 不得反向创造 Assignment / Binding 的语义 Authority。

---

## 12. Downstream Impact（下游影响）

### Positive Impact

本 Patch 将减少未来：

- F9 索引时的对象歧义；
- F10 Runtime 中对 RoleBinding / SkillBinding 的上下文猜测；
- Binding 类型爆炸；
- temporary selection 被误写成 durable binding；
- responsibility / relation / effective result 三种语义混淆。

### No Architecture Rewrite

本 Patch 不推翻：

- F4 Adaptive Workflow；
- F7 Change Governance；
- F8 Project Instance Binding；
- 既有 Authority / Permission 分离。

---

## 13. Forbidden Interpretation（禁止解释）

禁止：

1. `Assignment = Authority`
2. `Assignment = Permission`
3. `Binding = Current Effective`
4. `Binding = 任意对象关系万能容器`
5. `Resolution Result = Canonical Truth`
6. `Resolution Result = Authority`
7. `Temporary Selection = Durable Rebinding`
8. `RoleBinding / SkillBinding` 继续作为含义不明的兜底字段
9. 建立 `UniversalResolver（万能解析器）` 作为新的 God Object
10. 因存在治理语义而把全部 Task-scoped Assignment / Resolution 强制送入 F7
11. 借本 Patch 执行 Legacy 物理删除
12. 借本 Patch 进入 Implementation / RP2 / Authority Cutover / Final Activation

---

## 14. Human Decision（人工决策）

用户已明确：

```text
B1-PATCH-01 HUMAN_APPROVED
```

因此本 Patch 的架构语义状态为：

```text
HUMAN_APPROVED
```

该批准仅授权：

- 将本 Patch 作为 Pre-F9 审计正式修订依据；
- 在最终 v1.1 Candidate 整合时应用本 Patch；
- 作为后续 Batch / F9 / F10 设计的有效审计补充合同。

不授权真实 Implementation 或 Legacy Migration。

---

## 15. Integration Target（未来整合目标）

最终 F1～F8 审计完成后，本 Patch 应进入：

### F1

`F1_Core_Object_Model_Freeze_Pack_v1.1 Candidate`

主要整合：

- 新增 `ASSIGNMENT` First-Class Object Family；
- Assignment / Binding 全局边界；
- Generic RoleBinding / SkillBinding 退休说明。

### F4

`F4_Orchestration_Semantic_Freeze_Pack_v1.1 Candidate`

主要整合：

- RoleAssignment → Assignment Family；
- Skill Requirement / Pin / Exclude → Execution Constraint；
- Role / Skill Resolution 与 Binding 分离；
- 删除 / 澄清残留的泛化 RoleBinding / SkillBinding 表达。

### F8

`F8_Project_Instance_Governance_Freeze_Pack_v1.1 Candidate`

主要为澄清 / 引用补充：

- Binding 按 Relation Purpose 分类；
- Domain / Scope 为适用维度；
- 继续保持 `Binding != Effective Binding`。

### F7 / F9 / F10

仅整合跨阶段边界与消费约束，不重分 Owner。

---

## 16. Version / Revision Impact（版本 / 修订影响）

本 Patch：

- 不修改 F1～F8 v1.0；
- 不把 v1.0 静默重写；
- 作为独立、可追踪的 Audit Revision Evidence（审计修订证据）存在；
- 最终通过 Consolidation（整合）形成新的 v1.1 Candidate；
- 是否最终发布为 v1.1 Freeze Baseline，仍需整个 Pre-F9 Review 完成后的 Final Reconciliation / Audit。

---

## 17. Current Effective Status（当前有效状态）

从本 Patch 获得 HUMAN_APPROVED 起，在本次 Pre-F9 审计与后续架构讨论中：

```text
Assignment / Binding / Resolution 三分语义
= APPROVED AUDIT CORRECTION
```

```text
Generic RoleBinding
= RETIRED IN TARGET ARCHITECTURE
```

```text
Generic SkillBinding
= RETIRED IN TARGET ARCHITECTURE
```

但 F1～F8 v1.0 仍保持 Original Frozen Baseline 身份，直到最终整合发布新版本。

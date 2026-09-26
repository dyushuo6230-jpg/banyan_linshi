# AUDIT-PATCH-002 — Configuration Profile

> Patch ID: `AUDIT-PATCH-002`  
> Source Candidate: `B1-PATCH-02`  
> Status: `HUMAN_APPROVED`  
> Scope: Pre-F9 F1～F8 Architecture Integrity & Optimization Review — Audit Batch 1  
> Implementation Authorization: `NO`  
> RP2 Authorization: `NO`  
> Authority Cutover Authorization: `NO`  
> Final Activation Authorization: `NO`  
> Legacy Retirement Authorization: `NO`

---

## 1. Affected Stage（受影响阶段）

### Primary
- F3 — Definition Artifact Taxonomy

### Secondary / Clarification
- F4 — Orchestration Semantic
- F6 — UI Design Governance
- F8 — Project Instance Governance

### Consumer / Downstream Boundary
- F7 / F9 / F10 / F11

本 Patch 不重新分配上述阶段既有 Owner。

---

## 2. Problem（问题）

F6 / F8 已经实际依赖 `Profile` 语义：

- Profile references Modules / Rule Sets；
- Profile limits Scope / Applicability；
- Profile may reference legitimate override；
- Profile participates in Effective Context / Effective State Resolution；
- F8 已明确 `Profile Definition != Project Profile Instance`。

但 F3 当前 10 个 DefinitionArtifact Type 中没有一个能无损表达这一可复用、受治理、持续参与解析的“配置组合定义”。

同时 F4 使用：

```text
FAST / NORMAL / CONTROLLED profiles
```

表达执行治理强度，与 F6 / F8 的 Profile 语义不同，形成跨阶段术语碰撞。

---

## 3. Existing Contract（既有合同）

### F3

当前 10 类：

- RoleDefinition
- CapabilityDefinition
- SkillDefinition
- WorkflowDefinition
- PolicyDefinition
- StateModelDefinition
- DecisionProtocolDefinition
- TemplateDefinition
- ProviderContractDefinition
- CompatibilitySpecDefinition

F3 已冻结：

- Single Primary Type；
- Type 与 Domain / Tag / Relation 分离；
- Closed-but-Extensible；
- 新顶级 Type 需要无损表达证明、Impact Analysis、Migration Impact、Versioned Change Proposal、Human Decision；
- Manifest / Registry / Schema / Loader 默认是 Infrastructure / Contract Metadata。

### F6

Profile 已具备：

- Module / Rule Set references；
- Scope / Applicability；
- legitimate override reference；
- versioned evolution；
- composition；
- split / merge / supersession；
- no body copy；
- no ordering-as-priority；
- no silent latest auto-upgrade。

### F8

已冻结：

```text
Profile Definition != Project Profile Instance
Project Profile Instance != Authority
```

### F4

F4-D03 当前使用：

```text
FAST / NORMAL / CONTROLLED profiles
```

---

## 4. Target Contract（目标合同）

### 4.1 新增第 11 个 DefinitionArtifact Type

正式新增：

```text
ConfigurationProfileDefinition
```

F3 目标类型集合：

```text
RoleDefinition
CapabilityDefinition
SkillDefinition
WorkflowDefinition
PolicyDefinition
StateModelDefinition
DecisionProtocolDefinition
TemplateDefinition
ProviderContractDefinition
CompatibilitySpecDefinition
ConfigurationProfileDefinition
```

该新增不改变 F3 的 Closed-but-Extensible 原则。

---

## 5. ConfigurationProfileDefinition 正式语义

`ConfigurationProfileDefinition` 是：

> 一个可复用、可治理的 DefinitionArtifact，用于定义一组受治理语义组件应如何被组合，以及该组合允许在哪些适用边界中被采用。

它主要回答：

```text
这套组合是什么？
由哪些受治理定义 / 模块 / 包组成？
在哪些 Scope / Applicability 下允许采用？
有哪些显式 Version / Compatibility / Composition / Override Reference？
```

---

## 6. Why New Type Is Required（为什么必须新增类型）

### 6.1 Not Manifest

Configuration Profile 不只是引用清单，它持续参与：

- Scope
- Applicability
- Version / Compatibility
- Composition
- Override Reference
- Effective Resolution

因此：

```text
Configuration Profile != Manifest
```

### 6.2 Not PolicyDefinition

Policy 回答“应该遵守什么规则 / 约束”。

Configuration Profile 回答“某类项目 / 任务组合采用哪些受治理语义对象”。

因此：

```text
Configuration Profile != PolicyDefinition
```

### 6.3 Not TemplateDefinition

Template 负责 creation scaffolding。

Configuration Profile 在创建后持续参与解析。

因此：

```text
TemplateDefinition != ConfigurationProfileDefinition
```

### 6.4 Not WorkflowDefinition

Profile 不定义执行控制流。

### 6.5 Not CompatibilitySpecDefinition

Profile 可引用 CompatibilitySpec，但不等于 CompatibilitySpec。

### 6.6 Not ProjectArtifact

同一 ConfigurationProfileDefinition 可以被多个 Project / Scope 复用。

### 6.7 Not Binding

Definition 回答“这套组合是什么”。

Binding 回答“谁采用这套组合”。

---

## 7. Definition / Binding / Instance / Resolution 四分语义

正式区分：

```text
ConfigurationProfileDefinition
!= ProfileBinding
!= ProjectProfileInstance
!= ProfileResolution / Effective Result
```

完整关系：

```text
ConfigurationProfileDefinition
↓
ProfileBinding
↓
ProjectProfileInstance
↓
Overlay / Project Fact / Variable Resolution
↓
ProfileResolution
↓
Applicable / Effective Profile Result
```

---

## 8. Allowed Content（允许内容）

ConfigurationProfileDefinition 在 Architecture 层可以包含 / 引用：

- Composition Purpose
- Typed References
- Applicability Envelope
- Allowed Scope
- Version / Compatibility Constraints
- Explicit Composition Relations
- Legitimate Override References
- Domain / Tag / typed relation metadata
- Stable Identity / lifecycle references

具体物理字段 / Schema / DDL / 文件格式不在本 Patch 冻结。

---

## 9. Forbidden Content（禁止吞并）

ConfigurationProfileDefinition 不得成为以下内容的 Canonical Owner：

- Project current path / location
- Project current Provider selection
- Secret / Credential
- Runtime Permission
- Runtime current state
- User temporary choice
- Canonical Product Truth
- Canonical Design Truth
- Project-local fact
- ProjectInstance identity
- Authority / Approval / Apply Authorization

禁止：

```text
ConfigurationProfileDefinition
= project config dump
= everything config
```

---

## 10. Profile Composition（组合规则）

允许 Profile 组合其他 Profile，但必须：

- 使用显式 typed relation；
- 不依赖文件顺序；
- 不使用隐藏继承承载治理语义；
- 不因组合顺序自动产生 Rule Priority；
- Override 仍由显式 Rule / Policy / Authority / Scope / Applicability 解析。

允许：

```text
Profile A COMPOSES Profile B
Profile A DEPENDS_ON Profile C
```

禁止：

```text
last item wins
file order = priority
implicit extends chain = governance
```

---

## 11. Type Explosion Guard（类型爆炸防护）

新增的是：

```text
ConfigurationProfileDefinition
```

不新增：

```text
FrontendProfileDefinition
BackendProfileDefinition
UIProfileDefinition
DatabaseProfileDefinition
ProviderProfileDefinition
WorkflowProfileDefinition
```

领域、技术栈、用途通过：

- Domain
- Tag
- Typed Relation
- Scope
- Applicability

表达。

---

## 12. F4 Terminology Clarification（术语澄清）

F4-D03 的：

```text
FAST / NORMAL / CONTROLLED profiles
```

正式澄清为：

```text
Execution Governance Mode
（执行治理模式）
```

值仍保持：

```text
FAST
NORMAL
CONTROLLED
```

该修正：

- 不改变 F4-D03 原有治理强度语义；
- 不改变 mandatory governance never bypassed；
- 只消除与 Configuration Profile 的术语碰撞。

---

## 13. F6 Clarification（F6 澄清）

F6 原：

> Profile declares project/task adoption and bindings.

正式收紧为：

```text
ConfigurationProfileDefinition
= reusable governed composition definition
```

```text
ProfileBinding
= project / task / scope adoption relation
```

ConfigurationProfileDefinition 不直接拥有“某项目已经采用我”的事实。

---

## 14. F8 Clarification（F8 澄清）

F8 的：

```text
Profile Definition
```

正式指向：

```text
ConfigurationProfileDefinition
```

继续保持：

```text
Profile Definition != Project Profile Instance
Project Profile Instance != Authority
ProfileBinding != Authority
```

F8-D03 继续拥有：

- Project Profile Instance
- Overlay
- Project Fact
- Variable Resolution

---

## 15. Version / Revision Boundary（边界）

ConfigurationProfileDefinition：

- 有 Stable Identity；
- 支持受治理 Revision；
- 支持 Version / Pin / Compatibility；
- shared latest 不得静默替换 project current effective。

但全局 `Stable ID / Revision / Version / Current Effective` 合同由 `B1-PATCH-03` 负责。

---

## 16. Authority Boundary（权威边界）

必须保持：

```text
ConfigurationProfileDefinition != Authority
ProfileBinding != Authority
ProjectProfileInstance != Authority
ProfileResolution != Authority Creation
```

Profile 只能组合 / 引用，不得越权改变被引用对象的 Canonical Truth。

---

## 17. Engineering Standard Pack Boundary

```text
Engineering Standard Pack
!= Configuration Profile
```

Engineering Standard Pack 负责某工程规范领域中的受治理内容组合 / 分发。

Configuration Profile 负责某类项目 / 任务采用哪些受治理对象的组合方案。

完整 Rule / Policy / Standard 模型由 `B1-PATCH-04` 负责。

---

## 18. No-Loss Mapping（无损映射）

| 既有概念 | 新正式语义 |
|---|---|
| F6 Profile | ConfigurationProfileDefinition（经语义核验） |
| F8 Profile Definition | ConfigurationProfileDefinition |
| F8 Project Profile Instance | 保持 ProjectProfileInstance |
| F8 Profile Binding | 保持 ProfileBinding |
| F4 FAST/NORMAL/CONTROLLED profile | Execution Governance Mode |
| Manifest / Registry / Schema | 保持 Infrastructure / Contract Metadata |

---

## 19. Migration Impact（迁移影响）

### F6

```text
Existing F6 Profile
↓
Semantic Reconciliation
↓
ConfigurationProfileDefinition
```

### F8

现有 `Profile Definition` 映射到：

```text
ConfigurationProfileDefinition
```

### F4

`FAST / NORMAL / CONTROLLED profiles` 不映射为 ConfigurationProfileDefinition，而映射为：

```text
Execution Governance Mode
```

本 Patch 不执行：

- 文件移动
- Schema 变更
- 字段迁移
- Legacy 删除
- Canonical Rewrite

---

## 20. Forbidden Interpretations（禁止解释）

禁止：

1. Profile = Manifest
2. Profile = Policy
3. Profile = Template
4. Profile = ProjectArtifact
5. Profile = Binding
6. Profile = ProjectProfileInstance
7. Profile = Authority
8. Profile ordering = Rule Priority
9. Profile composition = implicit hidden inheritance
10. Profile latest = project current effective
11. ProfileDefinition 存储项目当前 path / credential / runtime permission
12. 为每个领域创建新的 `*ProfileDefinition`
13. 新增第 11 类后把 F3 变成开放式任意加 Type
14. 借本 Patch 进入 Implementation / RP2 / Authority Cutover / Final Activation / Legacy Retirement

---

## 21. Downstream Impact（下游影响）

### Positive

- F3 类型体系补齐 F6 / F8 已存在的真实语义；
- 消除 Profile / Manifest / Policy / Template 混淆；
- 消除 F4 Profile 重名；
- F8 的 Profile Definition / Binding / Instance / Effective Result 形成完整链；
- 为后续 F9 精准检索、F10 解析与运行时消费提供明确对象身份。

### No Rewrite

本 Patch 不推翻 F4 / F6 / F8 主体架构。

---

## 22. Human Decision（人工决策）

用户已明确：

```text
B1-PATCH-02 HUMAN_APPROVED
```

因此本 Patch 状态为：

```text
HUMAN_APPROVED
```

该批准仅授权：

- 将本 Patch 作为 Pre-F9 正式审计修订依据；
- 在最终 F1～F8 v1.1 Candidate 整合时应用本 Patch；
- 作为后续 Batch / F9 / F10 的有效补充合同。

不授权真实 Implementation 或 Legacy Migration。

---

## 23. Integration Target（未来整合目标）

### F3

`F3_Definition_Artifact_Taxonomy_Freeze_Pack_v1.1 Candidate`

主要整合：

- 新增第 11 类 `ConfigurationProfileDefinition`
- 类型定义
- Closed-but-Extensible 补充
- Type Explosion Guard
- Migration mapping

### F4

`F4_Orchestration_Semantic_Freeze_Pack_v1.1 Candidate`

主要整合：

- `FAST / NORMAL / CONTROLLED profiles`
→ `Execution Governance Mode`

### F6

`F6_UI_Design_Governance_Freeze_Pack_v1.1 Candidate`

主要整合：

- `ConfigurationProfileDefinition != ProfileBinding`
- Profile Definition 的组合职责
- 项目采用事实由 Binding / Instance 表达

### F8

`F8_Project_Instance_Governance_Freeze_Pack_v1.1 Candidate`

主要整合：

- `Profile Definition`
→ `ConfigurationProfileDefinition`
- 保持 ProjectProfileInstance / ProfileBinding / Effective Result 分离

---

## 24. Version / Revision Impact（版本 / 修订影响）

本 Patch：

- 不修改 F1～F8 v1.0；
- 不静默重写 F3 v1.0；
- 作为独立 Audit Revision Evidence 存在；
- 最终通过 Consolidation 形成 v1.1 Candidate；
- 是否发布为 v1.1 Freeze Baseline，仍需完整 Pre-F9 Final Reconciliation / Audit。

---

## 25. Current Effective Status（当前有效状态）

从本 Patch HUMAN_APPROVED 起，在当前 Pre-F9 审计与后续架构讨论中：

```text
ConfigurationProfileDefinition
= APPROVED 11th DefinitionArtifact Type
```

```text
FAST / NORMAL / CONTROLLED profiles
= Execution Governance Mode
```

```text
ConfigurationProfileDefinition
!= ProfileBinding
!= ProjectProfileInstance
!= Effective Profile Resolution
```

F1～F8 v1.0 仍保持 Original Frozen Baseline 身份，直到最终整合发布新版本。

# B1-PATCH-02 — Configuration Profile 完整审批稿 v0.1

> Status: `SUPERSEDED_BY_APPROVED_PATCH`  
> Approved Patch: `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-002_Configuration_Profile.md`  
> Candidate ID: `B1-PATCH-02`  
> Scope: Pre-F9 F1～F8 Architecture Integrity & Optimization Review — Audit Batch 1  
> Implementation Authorization: `NO`  
> RP2 Authorization: `NO`  
> Authority Cutover Authorization: `NO`  
> Final Activation Authorization: `NO`

---

## 1. 修正目标

补齐 F6 / F8 已实际使用、但 F3 尚未正式赋予类型身份的 `Profile（配置组合档）` 概念。

目标不是增加一个“万能配置对象”，而是建立一个明确、受治理、可复用、可版本化的组合定义：

```text
ConfigurationProfileDefinition
（配置组合定义）
```

并正式分离：

```text
ConfigurationProfileDefinition
!= ProfileBinding
!= ProjectProfileInstance
!= Effective Profile Resolution
```

同时消除 F4 中 `FAST / NORMAL / CONTROLLED profiles` 与 F6 / F8 `Profile` 的跨阶段术语碰撞。

---

## 2. Existing Contract（既有冻结合同）

### F3

当前 F3 冻结 10 个 DefinitionArtifact Type：

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

F3 同时冻结：

- 每个 DefinitionArtifact 只有一个 Primary Type；
- Domain / Tag / Relation 与 Type 分离；
- Taxonomy 为 Closed-but-Extensible（封闭但可扩展）；
- 新顶级 Type 必须证明现有 Type + Domain / Tag / Relation 无法无损表达；
- 必须有 Impact Analysis、Migration Impact、Versioned F3 Change Proposal、Human Decision；
- Manifest / Registry / Schema / Loader 默认属于 Infrastructure / Contract Metadata，不是 DefinitionArtifact Type。

### F6

F6 已冻结 Profile 具备以下语义：

- references Modules / Rule Sets；
- limits Scope / applicability；
- may reference legitimate override；
- does not copy canonical rule body；
- does not create priority by ordering；
- does not silently auto-upgrade to latest shared version；
- Profile 参与 Rule / Context / Effective State Resolution。

F6 同时允许：

- Profile composition；
- Scope-local overrides；
- Provider replacement；
- versioned evolution；
- split / merge / supersession；
- project-local rules。

### F8

F8 已冻结：

```text
Profile Definition != Project Profile Instance
Project Profile Instance != Authority
```

并由 F8-D03 管理：

```text
Project Profile Instance
× Overlay
× Project Fact
× Variable Resolution
```

### F4

F4-D03 当前使用：

```text
FAST / NORMAL / CONTROLLED profiles
```

表达同一编排语义下不同治理强度。

---

## 3. 反证结论：为什么现有十类不能无损表达 Profile

### 3.1 Profile != Manifest

Manifest / Registry / Schema / Loader 属于基础设施 / 合同元数据。

Configuration Profile 不只是列出对象引用，它还具有：

- Scope
- Applicability
- Version / Compatibility Constraint
- Composition Relation
- Override Reference
- Effective Resolution participation

因此：

```text
Configuration Profile != Manifest
```

### 3.2 Profile != PolicyDefinition

PolicyDefinition 回答：

> 围绕一个治理目标，什么必须、禁止、允许或如何解析。

Configuration Profile 回答：

> 某类项目 / 任务组合采用哪些受治理语义对象。

Profile 可以引用 Policy，但 Profile 本身不应膨胀成 Policy。

因此：

```text
Configuration Profile != PolicyDefinition
```

### 3.3 Profile != TemplateDefinition

TemplateDefinition 负责 creation scaffolding（创建脚手架）。

Configuration Profile 在对象创建后仍持续参与：

```text
Scope
→ Profile
→ Rule / Policy / Standard / Compatibility
→ Resolution
→ Effective Context
```

因此：

```text
TemplateDefinition != ConfigurationProfileDefinition
```

### 3.4 Profile != WorkflowDefinition

Profile 不定义执行控制流、节点顺序或控制语义。

### 3.5 Profile != CompatibilitySpecDefinition

Profile 可引用 CompatibilitySpec，但 Profile 不只是兼容性规则与语义映射。

### 3.6 Profile != ProjectArtifact

同一个 Profile Definition 可被多个项目 / Scope 复用。

具体项目采用关系和项目实例状态分别属于：

```text
ProfileBinding
ProjectProfileInstance
```

### 3.7 Profile != Binding

Definition 回答“这套组合是什么”。

Binding 回答“谁采用这套组合”。

---

## 4. F3 Taxonomy Extension（F3 类型体系扩展）

候选新增第 11 个 DefinitionArtifact Type：

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

建议定义：

> ConfigurationProfileDefinition 是一个可复用、可治理的 DefinitionArtifact，用于定义一组受治理语义组件应如何被组合，以及该组合允许在哪些适用边界中被采用。

它主要回答：

```text
这套组合是什么？
由哪些受治理定义 / 模块 / 包组成？
在哪些 Scope / Applicability 下允许采用？
有哪些显式 Version / Compatibility / Composition / Override Reference？
```

---

## 6. 允许表达的内容

Architecture 级允许包含 / 引用：

- Composition Purpose
- Typed References
- Applicability Envelope
- Allowed Scope
- Version / Compatibility Constraints
- Explicit Composition Relations
- Legitimate Override References
- Domain / Tag / typed relation metadata
- Stable Identity / lifecycle references

具体物理字段、Schema、DDL、文件格式不在本 Patch 冻结。

---

## 7. 禁止吞并的内容

不得直接成为以下内容的 Canonical Owner：

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

## 8. Definition / Binding / Instance / Resolution 四分语义

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

### Definition
回答：这套可复用组合是什么。

### Binding
回答：某 Project / Scope 是否采用它。

### Project Profile Instance
回答：具体项目中的实例化状态、变量、Overlay、Project Fact 组合是什么。

### Resolution
回答：当前 Scope / Context / Authority / Version / Compatibility 下真正适用什么。

---

## 9. Profile Composition（Profile 组合）

允许 Profile 组合其他 Profile，但必须：

- 使用显式 typed relation；
- 不依赖文件顺序；
- 不使用隐藏继承承载治理语义；
- 不因组合顺序自动产生 Rule Priority；
- Override 仍由显式 Rule / Policy / Authority / Scope / Applicability 机制解析。

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

## 10. Type Explosion Guard（类型爆炸防护）

新增的是：

```text
ConfigurationProfileDefinition
```

而不是：

```text
FrontendProfileDefinition
BackendProfileDefinition
UIProfileDefinition
DatabaseProfileDefinition
ProviderProfileDefinition
WorkflowProfileDefinition
```

领域和技术差异继续使用：

- Domain
- Tag
- Typed Relation
- Scope
- Applicability

表达。

---

## 11. F4 Profile 术语冲突修正

F4-D03 的：

```text
FAST / NORMAL / CONTROLLED profiles
```

建议正式改称：

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

该修正只消除术语碰撞，不改变 F4-D03 的治理强度语义，也不改变 mandatory governance never bypassed。

---

## 12. F6 修正点

F6 当前：

> Profile declares project/task adoption and bindings.

需要收紧为：

```text
ConfigurationProfileDefinition
= reusable governed composition definition
```

```text
ProfileBinding
= project / task / scope adoption relation
```

ProfileDefinition 不直接拥有“某项目已经采用我”的事实。

---

## 13. F8 修正点

F8 现有：

```text
Profile Definition != Project Profile Instance
```

未来 `Profile Definition` 正式指向：

```text
ConfigurationProfileDefinition
```

并继续保持：

```text
Project Profile Instance != Authority
ProfileBinding != Authority
```

F8-D03 继续拥有：

- Project Profile Instance
- Overlay
- Project Fact
- Variable Resolution

---

## 14. Version / Revision Boundary

ConfigurationProfileDefinition 应当：

- 有 Stable Identity；
- 支持受治理 Revision；
- 支持 Version / Pin / Compatibility；
- shared latest 不得静默替换 project current effective。

但具体 `Stable ID / Revision / Version / Current Effective` 统一合同由 `B1-PATCH-03` 负责，本 Patch 不重复冻结。

---

## 15. Authority Boundary（权威边界）

必须保持：

```text
ConfigurationProfileDefinition != Authority
ProfileBinding != Authority
ProjectProfileInstance != Authority
ProfileResolution != Authority Creation
```

Profile 可以组合 / 引用，但不能越权改变被引用对象的 Canonical Truth。

---

## 16. Engineering Standard Pack 边界

```text
Engineering Standard Pack
!=
Configuration Profile
```

Engineering Standard Pack 负责某工程规范领域中的受治理内容组合 / 分发。

Configuration Profile 负责某类项目 / 任务采用哪些受治理对象的组合方案。

完整 Rule / Policy / Standard 模型继续由 `B1-PATCH-04` 负责。

---

## 17. Migration Impact（迁移影响）

### F6 Existing Profile

```text
Existing F6 Profile
↓
Semantic Reconciliation
↓
ConfigurationProfileDefinition
```

### F8 Profile Definition

正式映射到：

```text
ConfigurationProfileDefinition
```

### F4 FAST / NORMAL / CONTROLLED

不得映射到 ConfigurationProfileDefinition，而应映射为：

```text
Execution Governance Mode
```

### Legacy Physical Migration

本 Patch 不执行：

- 文件移动
- Schema 变更
- 字段迁移
- Legacy 删除
- Canonical Rewrite

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

## 19. Forbidden Interpretations（禁止解释）

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
12. 为每个领域继续创建新的 `*ProfileDefinition`
13. 新增第 11 类后把 F3 变成开放式任意加 Type
14. 借本 Patch 进入 Implementation / RP2 / Authority Cutover / Final Activation / Legacy Retirement

---

## 20. Affected Stage（受影响阶段）

### F1
无顶级 Family 新增。`ConfigurationProfileDefinition` 仍属于 `Artifact → DefinitionArtifact`。

### F3
Primary Change：
- DefinitionArtifact Taxonomy 10 → 11；
- 新增 `ConfigurationProfileDefinition`；
- 保持 Closed-but-Extensible；
- 增加 Type Explosion Guard。

### F4
Terminology Clarification：
- `FAST / NORMAL / CONTROLLED profiles`
→ `Execution Governance Mode`

### F6
Semantic Clarification：
- Profile Definition 与 Profile Binding 分离；
- 保留现有 Rule / Module / Scope / Override / Version 组合语义。

### F8
Semantic Binding：
- `Profile Definition`
→ `ConfigurationProfileDefinition`
- ProjectProfileInstance / Overlay / Project Fact / Variable Resolution Owner 不变。

---

## 21. Integration Target（未来整合目标）

若 HUMAN_APPROVED：

- `F3_Definition_Artifact_Taxonomy_Freeze_Pack_v1.1 Candidate`
- `F4_Orchestration_Semantic_Freeze_Pack_v1.1 Candidate`
- `F6_UI_Design_Governance_Freeze_Pack_v1.1 Candidate`
- `F8_Project_Instance_Governance_Freeze_Pack_v1.1 Candidate`

F7 / F9 / F10 / F11 只消费或后续实现，不因本 Patch 重分 Owner。

---

## 22. Approval Meaning（批准含义）

批准本 Patch 表示接受：

1. `ConfigurationProfileDefinition` 成为 F3 第 11 个正式 DefinitionArtifact Type；
2. 该新增满足 F3 Closed-but-Extensible 的扩展条件；
3. Profile Definition / Profile Binding / Project Profile Instance / Effective Resolution 四分；
4. Profile 只承担受治理组合定义，不成为万能配置对象；
5. Profile composition 必须显式，顺序不产生优先级；
6. 禁止 `FrontendProfileDefinition / UIProfileDefinition ...` 类型爆炸；
7. F4 `FAST / NORMAL / CONTROLLED profiles` 澄清为 `Execution Governance Mode`；
8. F6 / F8 既有 Profile 语义按 No-Loss Mapping 进入新模型；
9. 本批准不授权真实实现、物理迁移或 Legacy Retirement。

---

## 23. Current Status

当前：

```text
B1-PATCH-02
= APPROVAL_DRAFT
= NOT HUMAN_APPROVED
```

只有用户明确回复：

```text
B1-PATCH-02 HUMAN_APPROVED
```

后，才能生成正式 `AUDIT-PATCH-002`。

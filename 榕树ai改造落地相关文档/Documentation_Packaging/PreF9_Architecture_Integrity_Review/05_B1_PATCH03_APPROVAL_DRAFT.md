# B1-PATCH-03 — Stable ID / Revision / Version / Current Effective 完整审批稿 v0.1

> Status: `SUPERSEDED_BY_APPROVED_PATCH`  
> Approved Patch: `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-003_StableID_Revision_Version_CurrentEffective.md`  
> Candidate ID: `B1-PATCH-03`  
> Scope: Pre-F9 F1～F8 Architecture Integrity & Optimization Review — Audit Batch 1  
> Implementation Authorization: `NO`  
> RP2 Authorization: `NO`  
> Authority Cutover Authorization: `NO`  
> Final Activation Authorization: `NO`

---

## 1. 修正目标

统一 Banyan 全局关于以下四个核心概念的语义：

```text
Stable ID（稳定标识）
Revision（修订）
Version（版本）
Current Effective（当前有效）
```

解决当前 F6 / F7 / F8 已分别使用这些概念，但尚缺少一份完整 Banyan-wide（全局）共同合同的问题。

本 Patch 不推翻 F7 的 Stable ID / Revision 模型，而是在其基础上补齐：

- Version 的正式语义；
- Version 与 Revision 的边界；
- Latest（最新）分类；
- Version Pin / Constraint 与 Effective Version 的关系；
- Current Effective 的全局解析语义；
- Revision Lineage（修订演进）与 Supersession（替代）的边界；
- Reference（引用）的稳定语义。

---

## 2. Existing Contract（既有冻结合同）

### F1

First-Class Object（一等对象）可因 Stable Identity（稳定身份）、Schema（模式）、Lifecycle（生命周期）、Reference（引用）等成为一等对象。

### F6

已冻结：

```text
Latest != Current Effective
Approved != Current Effective
```

Rule / Module 支持：

- stable identity；
- versioned evolution；
- split / merge / supersession；
- shared latest does not auto-upgrade project。

### F7

已冻结：

```text
Stable ID = semantic subject identity
Revision = state of same subject

Stable ID != Revision
Path != Stable ID
Provider ID != Stable ID
Latest Revision != Current Effective Revision
```

并明确：

- Subject change requires new Stable ID；
- accepted Canonical Revision history may not be silently rewritten；
- Revision Lineage != Supersession；
- Superseded != Deleted；
- Semantic Reference 与 Revision-Pinned Reference 分离；
- Supersession != Universal Retarget；
- Reactivate Prior Revision != Rewrite History。

### F8

已冻结：

```text
Stable Identity != Version
Version != Revision
Version Pin != Effective Version
Latest != Current Effective
```

F8-D05 负责：

```text
Version Pin
Compatibility
Effective Version
```

---

## 3. Stable ID（稳定标识）

### 3.1 正式定义

```text
Stable ID
= Semantic Subject Identity
（语义主体身份）
```

Stable ID 回答：

> 这个受治理语义主体“是谁”。

它不回答：

- 当前内容是什么；
- 当前是哪次修订；
- 当前发布了哪个版本；
- 当前哪个版本有效；
- 当前位于哪个路径；
- 当前由哪个 Provider（提供者）提供。

因此：

```text
Stable ID
!= Path
!= Filename
!= Provider ID
!= Revision
!= Version
!= Current Effective
```

### 3.2 Same Subject Evolution（同一主体演进）

若语义主体仍然是同一对象：

```text
Same Stable ID
+
New Revision
```

### 3.3 Subject Change（主体改变）

若对象的语义主体已经改变：

```text
New Stable ID
```

禁止复用旧 Stable ID 偷换语义主体。

### 3.4 Path / Provider 变化

继续保持：

```text
Path Change != Subject Change
Provider Change != Subject Change
```

文件移动、Provider 替换不得自动导致 Stable ID 改变。

---

## 4. Revision（修订）

### 4.1 正式定义

Revision 是：

> 同一个 Stable Subject（稳定语义主体）在某个受治理时间点形成的可寻址状态快照 / 演进节点。

核心：

```text
Same Subject
+
Governed State
+
Addressable Snapshot
```

### 4.2 Revision 不是每次文件保存

禁止：

```text
Every Ctrl+S
→ New Semantic Revision
```

只有 Banyan 需要将某个状态作为：

- 受治理节点；
- 可引用节点；
- 可追踪节点；
- 可比较节点；
- 可恢复 / 回滚目标；

时，才形成 Revision。

### 4.3 Canonical Revision（正式修订）

一旦 Revision 已 Accepted（接受）进入 Canonical History（正式历史）：

```text
Accepted Canonical Revision
= Immutable Historical Node
```

其历史内容不得静默重写。

语义变化必须产生新的 Revision。

### 4.4 文件变化 != 语义修订变化

若只发生：

- Path 移动；
- Physical Storage（物理存储）变化；
- 不属于该对象语义 Owner 的外部关系变化；

则不应强制制造该对象新的 Semantic Revision（语义修订）。

是否产生 Revision 取决于：

> 该对象由其 Owner 管理的 Governed Semantic State（受治理语义状态）是否发生改变。

---

## 5. Version（版本）

### 5.1 正式定义

Version 是：

> 面向消费、复用、依赖、兼容与发布的 Governed Release Coordinate（受治理发布坐标）。

白话：

```text
Revision
= 内部受治理演进节点

Version
= 对外稳定消费 / 依赖 / Pin 的发布坐标
```

因此：

```text
Version != Revision
```

### 5.2 Every Revision != New Version

同一对象可以：

```text
R31
R32
R33
R34
R35
```

只发布：

```text
Version 3.0.0
→ R35
```

中间 Revision 不必全部成为 Version。

### 5.3 Not Every Object Is Versioned（不是所有对象都需要版本）

只有具备下列需求的对象通常才需要 Version：

- Publish（发布）
- Reuse（复用）
- Pin（固定）
- Dependency（依赖）
- Compatibility（兼容性）
- Release Coordination（发布协调）

例如：

- ConfigurationProfileDefinition（配置组合定义）
- WorkflowDefinition（工作流定义）
- PolicyDefinition（策略定义）
- Engineering Standard Pack（工程规范包）
- Framework Release（框架发布）

通常适合版本化。

而：

- WorkflowRun（工作流运行实例）
- ApplyAttempt（应用尝试）
- RuntimeExecution（运行时执行实例）

通常不需要“发布版本”。

---

## 6. Version Scheme（版本方案）与 Version 分离

例如：

```text
2.3.1
```

只是某种 Version Identifier（版本标识）。

Semantic Versioning（语义化版本）只是可能的 Version Scheme（版本方案）。

因此：

```text
Version != SemVer
Revision != Patch Version
```

具体：

- Stable ID 格式；
- Revision 编号算法；
- Version Scheme；
- Major / Minor / Patch 规则；

不在本 Patch 冻结。

---

## 7. Published Version（已发布版本）的稳定性

### 7.1 Exact Version 必须稳定解析

若：

```text
Version 2.3.0
→ Release Target X
```

正式发布后，不得静默变成：

```text
Version 2.3.0
→ Release Target Y
```

否则精确 Pin 将失去可重复性。

### 7.2 Release Target（发布目标）

Version 不强制只能映射到单一 Revision。

Release Target 可以是：

```text
One Exact Revision
```

或：

```text
A Coherent Immutable Release Set
（一个一致且不可静默重写的精确发布集合）
```

这样 Composite Pack（组合包）可以发布一个版本，同时内部引用多个精确 Revision / Version。

---

## 8. Latest（最新）必须明确语义

Architecture Contract（架构合同）和 Resolver（解析器）输入中，禁止使用含义不明的裸：

```text
LATEST
```

凡会影响治理语义，必须明确排序域，例如：

```text
Latest Revision
Latest Canonical Revision
Latest Published Version
Latest Compatible Version
Latest Observed State
```

至少明确区分：

```text
Latest Revision
!= Latest Published Version
!= Latest Compatible Version
```

并继续保持：

```text
All Latest Forms
!= Current Effective
```

---

## 9. Current Effective（当前有效）

### 9.1 正式定义

Current Effective 是：

> 在明确 Scope（范围）和 Context（上下文）下，由 Resolver 根据合法受治理输入计算得到的当前有效结果。

因此：

```text
Current Effective
= Derived Resolution Result
```

而不是：

```text
Current Effective
= Newest Thing
```

### 9.2 Current Effective 必须 Scope-aware（范围相关）

同一个 Stable Subject 可以在不同 Project / Scope 中解析到不同有效版本。

例如：

```text
PROFILE-ADMIN-VUE-ELEMENT

Latest Published Version = 3.1.0

platform-admin
Effective Version = 3.1.0

tenant-admin
Effective Version = 3.0.0
```

这是合法状态。

### 9.3 Current Effective 可能 Task-aware（任务相关）

一个迁移 / 验证任务可能临时解析 Candidate Version（候选版本）用于验证，但项目正式上下文仍保持旧 Version。

因此：

```text
Task Effective Context
!= Project Production Current Effective
```

除非治理合同明确两者一致。

### 9.4 Current Effective 不是 Authority

继续保持：

```text
Resolution != Authority
Current Effective Result != Authority Creation
```

Resolver 只根据已有合法事实解析结果，不创造新的产品 / 设计 / 工程权威。

---

## 10. Version Pin / Version Constraint / Effective Version

正式区分：

```text
Version Pin
= Resolution Input / Binding Constraint
（解析输入 / 绑定约束）
```

```text
Version Constraint
= Resolution Input / Compatibility Range
（解析输入 / 版本范围约束）
```

```text
Effective Version
= Resolution Result
（解析结果）
```

因此：

```text
Version Pin != Effective Version
Version Constraint != Effective Version
```

Pin / Constraint 还需结合：

- Compatibility（兼容性）
- Authority（权威）
- Applicability（适用性）
- Availability（可用性）
- Gate（门禁）
- Policy（策略）
- Freshness Evidence（新鲜度证据）

才能形成 Current Effective Version。

---

## 11. Latest / Upgrade / Freshness 边界

新版本出现：

```text
New Latest Published Version
```

不得自动：

```text
→ Project Current Effective
```

必须继续保持：

```text
Shared Latest
!= Automatic Project Upgrade
```

F9 未来可以提供：

- Freshness Evidence（新鲜度证据）
- Impact Query（影响查询）
- Latest metadata（最新元数据）
- Compatibility evidence retrieval（兼容证据检索）

但：

```text
F9 Evidence != Version Decision
Freshness Evidence != Upgrade Authorization
Impact Query != Upgrade Authorization
```

---

## 12. Revision Lineage（修订演进）与 Supersession（替代）

### 12.1 Revision Lineage

```text
Stable ID A
R1 → R2 → R3
```

表示：

```text
Same Semantic Subject Evolution
（同一语义主体演进）
```

### 12.2 Supersession

若出现新的语义主体：

```text
Stable ID B
SUPERSEDES
Stable ID A
```

这是：

```text
Different Stable IDs
+
Explicit Semantic Relation
```

因此：

```text
Revision Lineage != Supersession
```

### 12.3 Superseded != Deleted

被替代对象仍可能被：

- Historical Reference（历史引用）
- Exact Version Pin（精确版本固定）
- Audit（审计）
- Reproduction（重现）

使用。

因此：

```text
Superseded != Deleted
```

---

## 13. Reference Model（引用模型）

至少区分三类引用语义。

### 13.1 Semantic Reference（语义引用）

```text
Stable ID
→ Current Applicable Resolution
```

表达：

> 引用这个语义主体，并按当前合法治理规则解析适用状态。

### 13.2 Revision-Pinned Reference（修订固定引用）

```text
Stable ID + Exact Revision
```

表达：

> 精确引用某个历史 / 受治理 Revision。

### 13.3 Version Reference / Version Constraint（版本引用 / 版本约束）

```text
Stable ID + Exact Version
```

或：

```text
Stable ID + Version Constraint
```

表达：

> 依赖某个发布版本或可接受版本范围。

### 13.4 引用禁止自动变形

禁止：

```text
Semantic Reference
→ silently becomes Revision Pin
```

也禁止：

```text
Exact Historical Pin
→ silently retargeted by Supersession
```

继续保持：

```text
Supersession != Universal Retarget
```

---

## 14. Rollback / Reactivation（回退 / 重新激活）

若：

```text
R17 → R18 → R19
```

后来重新让：

```text
R17
```

成为 Current Effective：

```text
Reactivate Prior Revision
!= Rewrite History
```

不得删除 / 改写 R18 / R19 来伪造历史。

Technical Recovery（技术恢复）与 Semantic Rollback（语义回退）仍保持分离。

---

## 15. Owner Boundary（Owner 边界）

### F1

负责 Stable Identity（稳定身份）作为一等对象共同能力的基础边界。

不新增新的 Object Family。

### F3

DefinitionArtifact 可拥有：

- Stable ID
- Revision
- Version（若有发布 / Pin / Dependency / Compatibility 需求）

但不是所有 DefinitionArtifact 都必须 Versioned（版本化）。

### F6

继续使用：

- Stable Identity
- Versioned Evolution
- Split / Merge / Supersession
- Latest != Current Effective

但全部遵循本 Patch 的统一定义。

### F7

继续拥有：

```text
Stable ID
Revision
History
Supersession
Canonical Apply
```

的全局治理合同和持久受治理变更路径。

F7 不成为所有 Domain 的“版本策略 Owner”。

### Domain Owner（领域 Owner）

各领域 Owner 继续负责：

- 什么状态有资格发布；
- Compatibility Policy（兼容策略）；
- Release Policy（发布策略）；
- Domain-specific Version Eligibility（领域版本资格）。

### F8

继续拥有 Project Instance 侧：

```text
Version Pin
Version Constraint
Compatibility
Effective Version
```

F8 不重新定义 Version 本体。

### F9

未来负责检索 / 索引：

- Stable ID
- Revision
- Version
- Supersession Relation
- Reference
- Freshness Evidence
- Impact Evidence

但：

```text
Index != Current Effective
Index != Authority
```

### F10

Runtime 消费已解析的 Current Effective Result，不自行重做版本治理决定。

---

## 16. 与 AUDIT-PATCH-002 的衔接

`ConfigurationProfileDefinition（配置组合定义）` 使用本 Patch 后形成：

```text
ConfigurationProfileDefinition
Stable ID
↓
Revision Lineage
↓
Governed Publication
↓
Version
↓
ProfileBinding / Version Constraint
↓
ProjectProfileInstance
↓
ProfileResolution
↓
Current Effective Version / Revision
```

这样：

- Patch-02 定义 Profile 是什么；
- Patch-03 定义它如何拥有身份、修订、发布版本和当前有效状态。

---

## 17. No-Loss Mapping（无损映射）

| 既有语义 | 本 Patch 统一语义 |
|---|---|
| F7 Stable ID | Stable ID = Semantic Subject Identity |
| F7 Revision | Same Stable Subject 的受治理可寻址状态节点 |
| F7 Latest Revision != Current Effective Revision | 保留并纳入全局 Current Effective 模型 |
| F8 Version != Revision | 保留并补齐 Version 正式定义 |
| F8 Version Pin != Effective Version | 保留并解释为 Input Constraint != Resolution Result |
| F6 Latest != Current Effective | 保留并推广为全局规则 |
| F6 shared latest does not auto-upgrade project | 保留 |
| Revision Lineage != Supersession | 保留 |
| Superseded != Deleted | 保留 |
| Historical Reference != Broken Reference | 保留 |

---

## 18. Deferred / Not Frozen Here（本 Patch 不冻结）

不在本 Patch 冻结：

- Stable ID 物理格式；
- Revision 编号算法；
- Version 字符串格式；
- 是否强制使用 Semantic Versioning（语义化版本）；
- Major / Minor / Patch 具体含义；
- Version Storage（版本存储）；
- History Storage（历史存储）；
- Database Schema（数据库结构）；
- Release API（发布接口）；
- Resolver 实现；
- F9 Index Schema（索引结构）。

这些属于后续物理设计 / 实现阶段。

---

## 19. Forbidden Interpretations（禁止解释）

禁止：

1. Stable ID = Path
2. Stable ID = Provider ID
3. Stable ID = Version
4. Stable ID = Revision
5. Path change = Subject change
6. Provider change = Subject change
7. Semantic Subject change 继续复用旧 Stable ID
8. Every file save = new Semantic Revision
9. Accepted Canonical Revision 可静默重写
10. Version = Revision
11. Revision = Patch Version
12. Version = Semantic Versioning 本身
13. Every Revision 必须发布 Version
14. Every object 必须有 Version
15. Published Exact Version 可静默重指新内容
16. Latest = Current Effective
17. Latest Published Version = Effective Version
18. Version Pin = Effective Version
19. Version Constraint = Effective Version
20. Current Effective = Authority
21. F9 Freshness Evidence = Upgrade Decision
22. Superseded = Deleted
23. Supersession = Universal Retarget
24. Reactivate Prior Revision = Rewrite History
25. Global Framework Version 自动覆盖所有内部对象 Version
26. 借本 Patch 进入 Implementation / RP2 / Authority Cutover / Final Activation / Legacy Retirement

---

## 20. Affected Stage（受影响阶段）

### F1
Clarification：Stable Identity 与 Revision / Version 分离。

### F3
Clarification：DefinitionArtifact 可以 Revisioned（可修订），并在有发布 / Pin / Dependency / Compatibility 需求时 Versioned（可版本化）。

### F6
Normalization：统一 Version / Revision / Latest / Current Effective 语义。

### F7
Primary semantic consolidation：保留既有 Stable ID / Revision / History / Supersession 合同，并补 Version / Release Target 边界。

### F8
Clarification：保留 Version Pin / Compatibility / Effective Version Owner，遵循全局 Version 合同。

### F9 / F10
Future consumer boundary only。

---

## 21. Approval Meaning（批准含义）

若本 Patch HUMAN_APPROVED，表示接受：

1. Stable ID = Semantic Subject Identity；
2. Same Subject Evolution 使用同 Stable ID + 新 Revision；
3. Subject Change 必须新 Stable ID；
4. Revision 是受治理、可寻址状态节点，不是每次文件保存；
5. Accepted Canonical Revision 不可静默重写；
6. Version 是面向消费 / 发布 / Pin / Dependency / Compatibility 的 Governed Release Coordinate；
7. Version != Revision；
8. 不是每个 Revision 都成为 Version，也不是所有对象都必须 Versioned；
9. Published Exact Version 必须稳定解析到其 Release Target；
10. Latest 必须明确类型，所有 Latest != Current Effective；
11. Current Effective 是 Scope / Context aware Derived Resolution Result；
12. Version Pin / Constraint 是解析输入，Effective Version 是解析结果；
13. Revision Lineage != Supersession；
14. Superseded != Deleted；
15. Exact Historical Pin 不因 Supersession 自动重定向；
16. 本 Patch 不授权 Implementation 或物理迁移。

---

## 22. Integration Target（未来整合目标）

若 HUMAN_APPROVED：

- `F1_Core_Object_Model_Freeze_Pack_v1.1 Candidate`
- `F3_Definition_Artifact_Taxonomy_Freeze_Pack_v1.1 Candidate`
- `F6_UI_Design_Governance_Freeze_Pack_v1.1 Candidate`
- `F7_Change_Canonical_Apply_Freeze_Pack_v1.1 Candidate`
- `F8_Project_Instance_Governance_Freeze_Pack_v1.1 Candidate`

F9 / F10 继承共同合同，不在本 Patch 提前实现。

---

## 23. Current Status

当前：

```text
B1-PATCH-03
= APPROVAL_DRAFT
= NOT HUMAN_APPROVED
```

只有用户明确回复：

```text
B1-PATCH-03 HUMAN_APPROVED
```

后，才生成正式 `AUDIT-PATCH-003`。

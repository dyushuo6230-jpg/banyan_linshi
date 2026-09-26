# AUDIT-PATCH-003 — Stable ID / Revision / Version / Current Effective

> Patch ID: `AUDIT-PATCH-003`  
> Source Candidate: `B1-PATCH-03`  
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
- F7 — Stable ID / Revision / History / Supersession / Canonical Apply

### Cross-stage Semantic Normalization
- F1 — Core Object Model
- F3 — Definition Artifact Taxonomy
- F6 — UI Design Governance
- F8 — Project Instance Governance

### Downstream Consumer
- F9 — Index / Search / Freshness / Impact
- F10 — Runtime

本 Patch 不重新分配既有阶段 Owner，而是建立 Banyan-wide（全局）统一身份 / 修订 / 版本 / 当前有效语义。

---

## 2. Problem（问题）

F7 已经明确：

```text
Stable ID = semantic subject identity
Revision = state of same subject
Stable ID != Revision
Latest Revision != Current Effective Revision
```

F8 进一步明确：

```text
Stable Identity != Version
Version != Revision
Version Pin != Effective Version
Latest != Current Effective
```

F6 也已经长期使用：

```text
Latest != Current Effective
shared latest != automatic project upgrade
```

但 F1～F8 之间仍缺少一份统一合同完整回答：

- Version（版本）到底是什么；
- Version 与 Revision 的边界；
- 哪些对象需要 Version；
- Latest（最新）有哪些不同含义；
- Version Pin / Version Constraint 与 Effective Version 的关系；
- Current Effective（当前有效）到底是不是持久状态 / Authority；
- Revision Lineage（修订演进）与 Supersession（替代）如何分离；
- Semantic / Revision / Version Reference（语义 / 修订 / 版本引用）如何区分。

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

若语义主体未改变：

```text
Same Stable ID
+
New Revision
```

### 3.3 Subject Change（主体改变）

若语义主体本身改变：

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

### 4.2 Revision 不是每次保存

禁止：

```text
Every File Save
→ New Semantic Revision
```

只有当 Banyan 需要将某个状态作为：

- 受治理节点；
- 可引用节点；
- 可追踪节点；
- 可比较节点；
- 可恢复 / 回滚目标；

时，才形成 Revision。

### 4.3 Accepted Canonical Revision（已接受正式修订）

一旦 Revision 已进入 Canonical History（正式历史）：

```text
Accepted Canonical Revision
= Immutable Historical Node
```

不得静默重写。

语义变化必须形成新的 Revision。

### 4.4 Physical Change（物理变化）不自动等于 Semantic Revision（语义修订）

例如：

- 文件路径改变；
- 存储位置改变；
- 外部 Binding / Location 变化；

如果不属于该对象 Owner 管理的语义状态变化，不应强制生成该对象的新 Revision。

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
= 给外部消费者稳定选择 / Pin / 依赖的发布坐标
```

因此：

```text
Version != Revision
```

### 5.2 Every Revision != New Version

同一对象可以有多个 Revision，只发布其中部分状态：

```text
R31
R32
R33
R34
R35

Version 3.0.0
→ Release Target based on R35
```

### 5.3 Not Every Object Is Versioned（不是所有对象都需要版本）

通常只有存在以下需求的对象才需要 Version：

- Publish（发布）
- Reuse（复用）
- Pin（固定）
- Dependency（依赖）
- Compatibility（兼容性）
- Release Coordination（发布协调）

例如通常适合版本化：

- ConfigurationProfileDefinition（配置组合定义）
- WorkflowDefinition（工作流定义）
- PolicyDefinition（策略定义）
- Engineering Standard Pack（工程规范包）
- Framework Release（框架发布）

而运行实例、尝试记录等对象通常不需要“发布版本”。

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

本 Patch 不冻结：

- Stable ID 物理格式；
- Revision 编号算法；
- Version 字符串格式；
- Major / Minor / Patch 规则。

---

## 7. Published Exact Version（已发布精确版本）的稳定性

若：

```text
Version 2.3.0
→ Release Target X
```

正式发布后，不得静默重绑定为：

```text
Version 2.3.0
→ Release Target Y
```

否则精确 Pin 将失去可重复性。

### Release Target（发布目标）

Version 不强制只能映射到单一 Revision。

Release Target 可以是：

```text
One Exact Revision
```

或：

```text
A Coherent Immutable Release Set
（一个一致、精确且不可静默重写的发布集合）
```

这样 Composite Pack（组合包）可以拥有自己的 Version，同时内部引用多个精确 Revision / Version。

---

## 8. Latest（最新）必须显式限定

在 Architecture Contract（架构合同）和 Resolver（解析器）输入中，凡影响治理语义，禁止使用含义不明的裸：

```text
LATEST
```

必须明确排序域，例如：

```text
Latest Revision
Latest Canonical Revision
Latest Published Version
Latest Compatible Version
Latest Observed State
```

至少保持：

```text
Latest Revision
!= Latest Published Version
!= Latest Compatible Version
```

并且：

```text
All Latest Forms
!= Current Effective
```

---

## 9. Current Effective（当前有效）

### 9.1 正式定义

Current Effective 是：

> 在明确 Scope（范围）与 Context（上下文）下，由 Resolver 根据合法受治理输入计算得到的当前有效结果。

因此：

```text
Current Effective
= Derived Resolution Result
（派生解析结果）
```

而不是：

```text
Current Effective
= Newest Thing
```

### 9.2 Scope-aware（范围相关）

同一个 Stable Subject 可以在不同项目 / Scope 中拥有不同当前有效版本。

例如：

```text
PROFILE-ADMIN-VUE-ELEMENT

Latest Published Version = 3.1.0

platform-admin
Effective Version = 3.1.0

tenant-admin
Effective Version = 3.0.0
```

### 9.3 Task-aware（任务相关）

迁移 / 验证任务可以在任务级上下文中解析候选 Version 进行验证，而项目正式上下文仍保持当前生产有效 Version。

因此：

```text
Task Effective Context
!= Project Production Current Effective
```

除非治理合同明确两者一致。

### 9.4 Current Effective != Authority

继续保持：

```text
Resolution != Authority
Current Effective Result != Authority Creation
```

Resolver 只根据已有合法事实计算当前适用结果，不创造新的产品 / 设计 / 工程权威。

---

## 10. Version Pin / Constraint / Effective Version

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

形成 Effective Version 还需要结合：

- Compatibility（兼容性）
- Authority（权威）
- Applicability（适用性）
- Availability（可用性）
- Gate（门禁）
- Policy（策略）
- Freshness Evidence（新鲜度证据）

---

## 11. Latest / Upgrade / Freshness Boundary（最新 / 升级 / 新鲜度边界）

新版本出现：

```text
New Latest Published Version
```

不得自动：

```text
→ Project Current Effective
```

继续保持：

```text
Shared Latest
!= Automatic Project Upgrade
```

F9 未来可以提供：

- Freshness Evidence（新鲜度证据）
- Impact Query（影响查询）
- Latest Metadata（最新元数据）
- Compatibility Evidence Retrieval（兼容证据检索）

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

表示：

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

至少区分：

### 13.1 Semantic Reference（语义引用）

```text
Stable ID
→ Current Applicable Resolution
```

表达：

> 引用该语义主体，并按当前合法治理规则解析当前适用状态。

### 13.2 Revision-Pinned Reference（修订固定引用）

```text
Stable ID + Exact Revision
```

### 13.3 Version Reference / Version Constraint（版本引用 / 版本约束）

```text
Stable ID + Exact Version
```

或：

```text
Stable ID + Version Constraint
```

### 13.4 引用不得静默变形

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

Technical Recovery（技术恢复）与 Semantic Rollback（语义回退）继续分离。

---

## 15. Owner Boundary（Owner 边界）

### F1

负责 Stable Identity（稳定身份）作为一等对象共同能力的基础边界。

不新增新的 Object Family。

### F3

DefinitionArtifact 可以拥有：

- Stable ID
- Revision
- Version（当存在发布 / Pin / Dependency / Compatibility 需求时）

但不是所有 DefinitionArtifact 都必须 Versioned（版本化）。

### F6

继续使用：

- Stable Identity
- Versioned Evolution
- Split / Merge / Supersession
- Latest != Current Effective

并遵循本 Patch 的统一定义。

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

F7 不成为所有 Domain（领域）的“版本策略 Owner”。

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

未来负责索引 / 检索：

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

Runtime 只消费已经解析出的 Current Effective Result，不重新进行版本治理决策。

---

## 16. No-Loss Mapping（无损映射）

| 既有语义 | 统一语义 |
|---|---|
| F7 Stable ID | Stable ID = Semantic Subject Identity |
| F7 Revision | Same Stable Subject 的受治理可寻址状态节点 |
| F7 Latest Revision != Current Effective Revision | 保留并纳入全局 Current Effective 模型 |
| F8 Version != Revision | 保留并补齐 Version 定义 |
| F8 Version Pin != Effective Version | 保留；Input Constraint != Resolution Result |
| F6 Latest != Current Effective | 保留并推广为全局规则 |
| F6 shared latest does not auto-upgrade project | 保留 |
| Revision Lineage != Supersession | 保留 |
| Superseded != Deleted | 保留 |
| Historical Reference != Broken Reference | 保留 |

---

## 17. Compatibility（兼容性）

本 Patch 是 Cross-Stage Semantic Normalization（跨阶段语义统一），不是物理迁移。

F1～F8 v1.0 历史合同继续保留。

最终 v1.1 Consolidation（整合）时：

- 不改变既有 Stable ID 的语义身份；
- 不重新编号历史 Revision；
- 不把 Revision 强制转换为 Version；
- 不把所有对象强制 Versioned；
- 不重写既有 Exact Pin / Historical Reference；
- 所有修改必须可追踪到本 Patch。

---

## 18. Downstream Impact（下游影响）

### Positive Impact

本 Patch 将：

- 统一 Identity（身份）/ History（历史）/ Release（发布）/ Selection（选择）/ Effective State（有效状态）；
- 防止 Version 与 Revision 混用；
- 防止 Latest 自动成为 Current Effective；
- 防止精确版本静默漂移；
- 为 F9 Index / Freshness / Impact 提供稳定检索键；
- 为 F8 Project Version Resolution 提供明确共同合同；
- 为 F10 Runtime Consumption 提供确定的有效状态边界。

---

## 19. Forbidden Interpretations（禁止解释）

禁止：

1. Stable ID = Path
2. Stable ID = Provider ID
3. Stable ID = Version
4. Stable ID = Revision
5. Path change = Subject change
6. Provider change = Subject change
7. Subject change 继续复用旧 Stable ID
8. Every file save = new Semantic Revision
9. Accepted Canonical Revision 可静默重写
10. Version = Revision
11. Revision = Patch Version
12. Version = Semantic Versioning 本身
13. Every Revision 必须发布 Version
14. Every object 必须 Versioned
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

## 20. Human Decision（人工决策）

用户已明确：

```text
B1-PATCH-03 HUMAN_APPROVED
```

因此本 Patch 状态：

```text
HUMAN_APPROVED
```

该批准授权：

- 作为 Pre-F9 正式审计修订依据；
- 最终 F1～F8 v1.1 Candidate 整合时应用；
- 后续 F9 / F10 架构设计复用本共同合同。

不授权真实 Implementation、物理 Migration（迁移）或 Legacy Retirement（遗留退役）。

---

## 21. Integration Target（未来整合目标）

### F1
`F1_Core_Object_Model_Freeze_Pack_v1.1 Candidate`

### F3
`F3_Definition_Artifact_Taxonomy_Freeze_Pack_v1.1 Candidate`

### F6
`F6_UI_Design_Governance_Freeze_Pack_v1.1 Candidate`

### F7
`F7_Change_Canonical_Apply_Freeze_Pack_v1.1 Candidate`

### F8
`F8_Project_Instance_Governance_Freeze_Pack_v1.1 Candidate`

F9 / F10 继承共同合同，不在本 Patch 提前实现。

---

## 22. Version / Revision Impact（版本 / 修订影响）

本 Patch：

- 不修改 F1～F8 v1.0；
- 不重新编号历史 Revision；
- 不强制发布 Version；
- 不强制所有对象 Versioned；
- 作为独立 Audit Revision Evidence（审计修订证据）存在；
- 最终通过 Consolidation 形成 v1.1 Candidate；
- 只有最终 Pre-F9 Final Reconciliation / Audit 通过后，才形成新的 Freeze Baseline。

---

## 23. Current Effective Status（当前有效状态）

从本 Patch HUMAN_APPROVED 起，在本次 Pre-F9 审计与后续架构讨论中：

```text
Stable ID
= Semantic Subject Identity
```

```text
Revision
= Governed Addressable State of Same Stable Subject
```

```text
Version
= Governed Release Coordinate
```

```text
Current Effective
= Scope / Context-aware Derived Resolution Result
```

并正式保持：

```text
Version != Revision
Latest != Current Effective
Version Pin != Effective Version
Revision Lineage != Supersession
Superseded != Deleted
```

F1～F8 v1.0 仍保持 Original Frozen Baseline（原始冻结基线）身份，直到最终整合发布新版本。

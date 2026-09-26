# AUDIT-PATCH-002-SUP-01 — Configuration Profile Maintenance Responsibility

> Patch ID: `AUDIT-PATCH-002-SUP-01`  
> Parent Patch: `AUDIT-PATCH-002 — Configuration Profile`  
> Source Candidate: `B1-PATCH-02-SUP-01`  
> Status: `HUMAN_APPROVED`  
> Scope: Pre-F9 F1～F8 Architecture Integrity & Optimization Review — Audit Batch 1  
> Implementation Authorization: `NO`  
> RP2 Authorization: `NO`  
> Authority Cutover Authorization: `NO`  
> Final Activation Authorization: `NO`  
> Legacy Retirement Authorization: `NO`

---

## 1. Purpose（目的）

本补充 Patch 解决 `ConfigurationProfileDefinition（配置组合定义）` 已经被正式定义之后的运行维护责任问题：

> ConfigurationProfileDefinition 默认应由 Banyan 在既有治理约束下系统化维护，而不是把日常引用同步、影响分析、版本关系、索引维护和任务级解析职责推给用户。

同时保持：

```text
AI Maintenance（AI 维护）
!= Autonomous Authority（自主权威）
```

本补充不改变 `AUDIT-PATCH-002` 对 ConfigurationProfileDefinition 本体的定义，只补充其 Maintenance Responsibility（维护责任）和 Automation Boundary（自动化边界）。

---

## 2. System-maintained under Governance（治理下系统维护）

ConfigurationProfileDefinition 默认采用：

```text
System-maintained under Governance
```

即：

- Banyan / AI 负责日常结构维护；
- 用户不承担常规引用同步；
- 用户不承担常规影响分析；
- 用户不承担任务级 Profile 解析；
- 用户不需要手工追踪所有 Profile 使用关系；
- 用户主要处理真正的语义、采用、Authority（权威）和高影响选择。

---

## 3. Three-layer Maintenance Model（三层维护模型）

### 3.1 Derived Maintenance（派生维护）

可默认自动执行：

- Index（索引）更新；
- Reference Integrity Check（引用完整性检查）；
- Profile 使用关系查询；
- Impact Analysis（影响分析）；
- Freshness Evidence（新鲜度证据）；
- Version Relation Analysis（版本关系分析）；
- Applicability（适用性）检查；
- Minimum Sufficient Context（最小充分上下文）生成；
- 当前相关 Rule / Policy / Standard 的定向检索。

这些工作不得改变 Canonical Meaning（正式语义）。

---

### 3.2 Change Candidate Preparation（变更候选准备）

Banyan / AI 可以自动：

- 识别 Profile 可能受哪些新 Rule / Module / Policy / Standard 影响；
- 形成 Profile Change Candidate（配置组合变更候选）；
- 准备 No-Loss Mapping（无损映射）；
- 做 Compatibility Analysis（兼容性分析）；
- 做 Project Impact Query（项目影响查询）；
- 形成 Version / Upgrade Candidate（版本 / 升级候选）；
- 形成 Split / Merge / Supersession（拆分 / 合并 / 替代）候选。

但必须保持：

```text
Candidate
!= Canonical Change
```

---

### 3.3 Canonical Profile Mutation（正式配置组合修改）

如果对 ConfigurationProfileDefinition 的正式语义产生持久改变：

```text
ConfigurationProfileDefinition Canonical Change
→ F7 Governed Change
```

是否需要 Human Decision（人工决策）由既有：

- Authority（权威）
- Policy（策略）
- Scope（范围）
- Decision Contract（决策合同）
- Apply Authorization（应用授权）

共同决定。

正式保持：

```text
Canonical Change
!= Always Human
```

同时：

```text
Canonical Change
!= Always Automatic
```

---

## 4. AI Maintenance != Authority（AI 维护不等于权威）

AI / Banyan 可以维护：

- 结构；
- 引用；
- 索引；
- 影响关系；
- 候选；
- 对账；
- Version / Freshness Evidence；
- 最小充分上下文。

但不得因此获得：

- Product Decision Authority（产品决策权）
- Design Authority（设计权威）
- Governance Decision Authority（治理决策权）
- Canonical Apply Authority（正式应用权）
- Project Adoption Authority（项目采用权）
- Autonomous Rule / Profile Promotion Authority（自主规则 / Profile 晋升权）

---

## 5. Project-local Difference != Shared Profile Change

若差异只属于某个具体项目，例如：

```text
tenant-admin
```

特有 UI、Provider、变量或局部规范差异，默认优先进入：

```text
ProjectProfileInstance
+
Project Overlay（项目局部覆盖）
```

不得自动修改共享：

```text
ConfigurationProfileDefinition
```

只有当差异被确认属于共享组合语义时，才进入共享 Profile 的正式受治理变更。

正式保持：

```text
Project-local Difference
!= Shared Profile Change
```

---

## 6. Shared Latest != Automatic Project Upgrade

新 Profile Version（版本）出现后，Banyan 可以自动：

- Detect（检测）；
- 做 Freshness Evidence；
- 做 Compatibility Analysis；
- 做 Impact Query；
- 形成 Upgrade Candidate（升级候选）。

但不得：

```text
Latest Published Version
→ Automatically become
Project Current Effective Version
```

继续保持：

```text
Latest
!= Current Effective
```

以及：

```text
Shared Latest
!= Automatic Project Upgrade
```

---

## 7. Runtime / Task Loading Boundary（运行时 / 任务加载边界）

项目采用某个 ConfigurationProfileDefinition，不代表每个任务都必须加载其全部引用内容。

默认解析路径：

```text
Task / Goal（任务 / 目标）
↓
Scope（范围）
↓
ProfileBinding / ProjectProfileInstance
↓
ConfigurationProfileDefinition
↓
Index / Targeted Retrieval（索引 / 定向检索）
↓
Minimum Sufficient Rule / Policy / Standard Set
（最小充分规则 / 策略 / 规范集合）
↓
Effective Context（当前有效上下文）
```

目标：

> 只加载当前任务真正相关的治理知识。

禁止：

```text
Project adopts Profile
→ Load all referenced governance content every task
```

---

## 8. Human Responsibility Boundary（人工责任边界）

用户主要负责：

- Why / Should（为什么 / 要不要）；
- 真正的语义选择；
- 多个合法方案中的实质性取舍；
- Project Adoption（项目采用）；
- 高影响升级；
- Authority 冲突；
- 现有治理无法唯一解析的合法选择。

Banyan 主要负责：

- What relates to What（什么与什么有关）；
- What is affected（影响什么）；
- What applies now（当前适用什么）；
- 结构维护；
- 引用维护；
- 影响分析；
- 候选准备；
- 版本 / 新鲜度分析；
- 最小充分上下文解析。

---

## 9. Existing Approved Contracts Preserved（保留既有批准合同）

本补充继续遵守：

### AUDIT-PATCH-002

```text
ConfigurationProfileDefinition
!= ProfileBinding
!= ProjectProfileInstance
!= ProfileResolution
```

### AUDIT-PATCH-003

```text
Version != Revision
Latest != Current Effective
Version Pin != Effective Version
```

### AUDIT-PATCH-004

```text
AI Maintenance != Authority
```

### AUDIT-PATCH-005

```text
Multiple Candidates
!= Automatic Informed Decision
```

并继续遵守 F7 Governed Change / Canonical Apply（受治理变更 / 正式应用）边界。

---

## 10. Forbidden Interpretations（禁止解释）

禁止：

1. System-maintained = AI 可以随意修改 Profile；
2. AI Maintenance = Authority；
3. AI Recommendation = Approved Profile Change；
4. Change Candidate = Canonical Change；
5. Canonical Profile Change = Always Human；
6. Canonical Profile Change = Always Automatic；
7. Project-local Difference 默认写回 Shared Profile；
8. 新 Rule / Module 出现 = 所有相关 Profile 自动改变；
9. 新 Profile Version 出现 = 所有项目自动升级；
10. Latest = Current Effective；
11. Profile Adoption = 每次任务全量加载所有引用；
12. 用户承担常规引用同步、索引、影响分析和上下文装配；
13. AI 自动维护可绕过 F7 Governed Change；
14. 本补充授权 Implementation / RP2 / Authority Cutover / Final Activation / Legacy Retirement。

---

## 11. Human Decision（人工决策）

用户已明确：

```text
B1-PATCH-02-SUP-01 HUMAN_APPROVED
```

因此：

```text
AUDIT-PATCH-002-SUP-01
= HUMAN_APPROVED
```

---

## 12. Integration Target（未来整合目标）

最终 F1～F8 v1.1 Candidate（候选整合基线）中，至少应更新：

- F3 / ConfigurationProfileDefinition 维护责任说明；
- F6 / Profile / Context Resolution 运行维护边界；
- F7 / Profile Canonical Change 的 Governed Change 边界；
- F8 / ProjectProfileInstance / ProfileBinding / Current Effective Version 边界。

F1～F8 v1.0 原冻结基线保持不变。

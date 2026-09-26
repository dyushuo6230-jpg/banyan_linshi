# B1-PATCH-02-SUP-01 — Configuration Profile 运行维护责任补充候选 v0.1

> Status: `SUPERSEDED_BY_APPROVED_PATCH`  
> Approved Patch: `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-002-SUP-01_Configuration_Profile_Maintenance_Responsibility.md`  
> Parent Approved Patch: `AUDIT-PATCH-002 — Configuration Profile`  
> Purpose: 补充 ConfigurationProfileDefinition（配置组合定义）的运行维护责任边界。  
> This document DOES NOT modify or supersede AUDIT-PATCH-002 unless separately HUMAN_APPROVED.

---

## 1. 候选补充原则

建议增加：

> `ConfigurationProfileDefinition（配置组合定义）` 默认由 Banyan 在既有治理约束下进行系统化维护；用户不承担日常手工同步、引用整理、影响分析、版本关系维护和任务级解析职责。

同时必须保持：

```text
AI Maintenance（AI 维护）
!= Autonomous Authority（自主权威）
```

AI / Banyan 可以自动完成确定性的结构维护，但不能因此获得产品决策、治理决策、Authority（权威）、Apply Authorization（应用授权）或 Canonical Truth（正式真相）修改权。

---

## 2. 默认由 Banyan / AI 自动完成的维护

在已有治理合同允许的前提下，系统可以自动执行：

- Profile 引用关系整理；
- Module / Rule / Policy / Standard / Compatibility 引用对账；
- Scope（范围）与 Applicability（适用性）检查；
- 版本关系和依赖关系分析；
- Impact Analysis（影响分析）；
- Profile 使用情况查询；
- ProfileBinding（配置绑定）与 ProjectProfileInstance（项目配置实例）的解析准备；
- Effective Context（当前有效上下文）的最小充分生成；
- 新版本 / 新规则出现后的受影响 Profile 候选识别；
- Split / Merge / Supersession（拆分 / 合并 / 替代）候选分析；
- No-Loss Mapping（无损映射）准备；
- 确定性、无争议的元数据和关系维护候选。

这些自动化不得越过既有 Owner / Policy / Authority / F7 Governed Change（受治理变更）边界。

---

## 3. 需要人工介入的情况

用户主要介入真正存在治理或价值判断的情况，例如：

- Profile 的语义目的发生重大改变；
- 多个合法组合方案存在实质差异；
- 某项目是否采用新的 Profile / Version（版本）；
- 高影响升级；
- Authority（权威）冲突；
- 无法通过既有规则唯一解析的合法方案；
- 对多个项目会产生显著语义、范围、风险或长期维护影响的拆分 / 合并；
- 需要改变 Canonical Rule / Policy / Standard 本体。

---

## 4. 项目局部差异不得污染共享 Profile

例如：

```text
ADMIN-VUE-ELEMENT
```

被：

```text
platform-admin
tenant-admin
```

共同采用。

若只有 `tenant-admin` 存在特殊 UI 约束，默认应优先表达为：

```text
ProjectProfileInstance
+
Project Overlay（项目局部覆盖）
```

而不是直接修改共享 `ConfigurationProfileDefinition`。

只有当该差异被确认属于共享组合语义时，才进入共享 Profile 的正式受治理变更。

---

## 5. Runtime / Task 解析模型

运行时不应默认完整加载 Profile 引用的全部规则。

推荐语义：

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

例如修改 `tenant-admin` 用户列表页 UI 时，应主要加载：

- 后台 UI 公共规范；
- Element Plus（Element Plus 组件库）相关布局规则；
- 页面视觉一致性规则；
- 相关项目 Overlay（局部覆盖）。

不需要因为项目 Profile 还引用了安全、Redis、MySQL 等规则就全部加载。

---

## 6. Profile 新版本不得静默升级项目

继续保持：

```text
Latest（最新）
!= Current Effective（当前有效）
```

以及：

```text
Shared Latest
!= Automatic Project Upgrade
```

Profile 新版本出现后，Banyan 可以自动：

- 检测；
- 做 Freshness Evidence（新鲜度证据）；
- Impact Query（影响查询）；
- Compatibility（兼容性）分析；
- 形成升级候选。

但是否成为某项目 `Current Effective Version（当前有效版本）`，必须经过对应 Binding / Pin / Compatibility / Policy / Governance 解析。

---

## 7. Forbidden Interpretations（禁止解释）

禁止：

1. 系统维护 = AI 可随意修改 Profile；
2. AI 推荐 = 已批准变更；
3. AI 分类 = Project Adoption（项目采用）；
4. 新规则出现 = 所有相关 Profile 自动升级；
5. 新 Profile 版本出现 = 所有项目自动切换；
6. Profile 维护责任重新推给用户日常手工操作；
7. 项目局部差异默认写回共享 Profile；
8. AI 自动维护获得新的 Authority。

---

## 8. Approval Boundary（审批边界）

当前状态：

```text
B1-PATCH-02-SUP-01
= CANDIDATE
= NOT HUMAN_APPROVED
```

若未来用户明确：

```text
B1-PATCH-02-SUP-01 HUMAN_APPROVED
```

再生成对应正式补充审计 Patch，并在最终 v1.1 Consolidation（整合）时写入 Configuration Profile 运行维护合同。

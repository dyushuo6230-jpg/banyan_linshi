# B1-PATCH-05 — Dynamic Workflow Composition × Workflow Choice Preference × Informed Decision 完整审批稿 v0.1

> Status: `SUPERSEDED_BY_APPROVED_PATCH`  
> Approved Patch: `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-005_Dynamic_Workflow_Choice_Informed_Decision.md`  
> Candidate ID: `B1-PATCH-05`  
> Scope: Pre-F9 F1～F8 Architecture Integrity & Optimization Review — Audit Batch 1  
> Implementation Authorization: `NO`  
> RP2 Authorization: `NO`  
> Authority Cutover Authorization: `NO`  
> Final Activation Authorization: `NO`

---

## 1. 修正目标

补齐 Banyan / 榕树 AI 已有 Dynamic Workflow Composition（动态工作流组合）能力中的跨阶段治理缺口：

> 当 Banyan 根据 Goal（目标）、Scope（范围）、Context（上下文）和 Governance（治理）解析出多个都合法的 Workflow Candidate（工作流候选）时，系统什么时候自动选择，什么时候让用户选择？

本 Patch 不重新设计 WorkflowDefinition（工作流定义），也不新增新的 Workflow Definition Artifact Type（工作流定义制品类型）。

它主要建立：

- Workflow Candidate（工作流候选）
- Validity Filtering（合法性过滤）
- Material Difference Detection（实质差异识别）
- Workflow Choice Preference（工作流选择偏好）
- Workflow Selection Resolution（工作流选择解析）
- Informed Decision（知情决策）触发边界
- User / Project / Task Scope（用户 / 项目 / 任务范围）偏好覆盖
- Selected Workflow 与 Decision / Approval / Authorization 的边界

---

## 2. Existing Contract（既有冻结合同）

### F4 — Orchestration Semantic（编排语义）

F4 已冻结：

```text
Goal / Desired Outcome
→ Intent / Scope / Constraints
→ Workflow Family Selection / Composition
→ Minimum Valid Workflow Graph
→ Responsibility Resolution
→ Functional Role Resolution
→ Capability Requirements
→ Execution Path Resolution
→ Provider / Binding Resolution
→ Runtime Execution
→ Validation
→ Evidence / Trace
→ Reconcile / Continue / Re-route / Escalate
```

并明确：

- WorkflowDefinition（工作流定义）= governed Goal-oriented Workflow Graph（受治理的目标导向工作流图）
- 不采用固定 Role / Capability / Skill（角色 / 能力 / 技能）流水线
- Graph（图）支持 Branch / Merge / Pause / Resume / Loop / Retry / Skip / Replace / Invalidate / Partial Blocking / Checkpoint / Reconcile / Escalation / De-escalation
- Runtime（运行时）必须优先使用 smallest valid execution graph（最小合法执行图）和 smallest necessary resolution scope（最小必要解析范围）
- Roles（角色）与 Workflow（工作流）解耦
- Resolution（解析）与 Execution（执行）分离
- F4-D03 原 FAST / NORMAL / CONTROLLED profiles 已由 AUDIT-PATCH-002 澄清为 Execution Governance Mode（执行治理模式）

### F5 — Product / Requirement Governance（产品 / 需求治理）

F5 已冻结：

```text
DECISION_REQUIRED
```

仅在 Alternatives（备选方案）会实质影响：

- Semantics（语义）
- Acceptance（验收）
- Authority（权威）
- Risk（风险）
- Downstream Contracts（下游合同）

时成立。

同时：

- 确定性工作默认自动完成
- Human Attention（人工注意力）保留给真正的 Decision（决策）
- Silence / Cancellation / AI Recommendation / Inference / Ambiguous Preference（沉默 / 取消 / AI 建议 / 推断 / 模糊偏好）不构成确认

### F7 — Change / Decision / Authorization（变更 / 决策 / 授权）

F7 已冻结：

```text
Candidate != Human Decision
Selected Candidate != Apply Authorization
```

并明确：

```text
multiple_candidates_require_informed_decision: false
```

即：

> Multiple Candidates（多个候选）本身不自动要求 Informed Decision（知情决策）。

---

## 3. 核心问题

当前 F4 已经支持 Dynamic Workflow Composition（动态工作流组合），但缺少统一合同回答：

```text
多个合法工作流出现
↓
AI 自动选？
还是
用户选择？
```

若默认“多个候选就问用户”，会把 Governance Cost（治理成本）推给用户。

若默认“AI 永远自动选”，又可能在 Scope（范围）、Time / Effort（时间 / 工作量）、Risk（风险）、Output（产物）、Validation Depth（验证深度）、Downstream Impact（下游影响）、Long-term Maintenance（长期维护）存在明显差异时替用户做本应由用户感知的选择。

---

## 4. Dynamic Workflow Composition（动态工作流组合）

Dynamic Workflow Composition 是 Banyan-wide（全局）能力。

适用于但不限于：

- Requirement（需求）
- Product（产品）
- Architecture（架构）
- UI / Design（UI / 设计）
- Development（开发）
- Validation（验证）
- Change（变更）
- Migration（迁移）
- Documentation Governance（文档治理）
- Project Adoption（项目接入）
- Engineering Standard Maintenance（工程规范维护）

它不得被解释成 Code Development Mode Selector（代码开发模式选择器）。

---

## 5. AI 动态组合的边界

AI / Banyan 可以从已有 Governed WorkflowDefinition（受治理工作流定义）、Reusable Subworkflow（可复用子工作流）和合法 Control Semantics（控制语义）中动态组合执行图。

但不得：

```text
Runtime ad-hoc invention
→ New Canonical WorkflowDefinition
```

即运行时临时组合的合法路径，不得自动晋升成新的正式 WorkflowDefinition。

---

## 6. Workflow Candidate（工作流候选）

Workflow Candidate 是：

> Banyan 根据当前 Goal / Scope / Context / Governance（目标 / 范围 / 上下文 / 治理）解析出的一个可执行工作流候选方案。

Workflow Candidate：

```text
!= WorkflowDefinition
!= Human Decision
!= Apply Authorization
!= Runtime Permission
```

---

## 7. Validity Filtering（合法性过滤）

所有 Workflow Candidate 在进入选择之前，必须先通过治理过滤。

至少包括：

- Policy（策略）
- Authority Boundary（权威边界）
- Scope Constraint（范围约束）
- Mandatory Governance（强制治理）
- Reliability Floor（可靠性底线）
- Required Validation（必要验证）
- Compatibility（兼容性）
- Applicable Engineering Standards（适用工程规范）
- Boundary / Gate（边界 / 门禁）

因此：

```text
Technically Possible
!= Governed Valid Candidate
```

非法候选不得展示给用户作为合法选择。

---

## 8. 测试 / 验证示例边界

“带不带测试”只能作为示例，不得形成全局关闭验证开关。

正式保持：

```text
Workflow Choice Preference
!= Disable Validation Switch
```

若 Policy / Engineering Standard / Gate（策略 / 工程规范 / 门禁）要求验证，无验证路径就不是 Valid Candidate（合法候选）。

---

## 9. Multiple Candidates != Automatic Informed Decision

正式保持 F7：

```text
Multiple Candidates
!= Automatic Informed Decision
```

发现两条或更多技术可行 / 合法路径，不意味着自动打断用户。

必须继续判断这些路径之间是否存在：

```text
Material Difference
（实质差异）
```

---

## 10. Materially Distinct Workflow（具有实质差异的工作流）

候选之间只有当差异会对用户目标或治理结果产生实质影响时，才构成真正的 Workflow Choice（工作流选择）。

Material Difference 至少可考虑：

- Scope（范围）
- Time / Effort（时间 / 工作量）
- Cost（成本）
- Risk（风险）
- Reversibility（可逆性）
- Output（最终产物）
- Validation Depth（验证深度）
- Downstream Impact（下游影响）
- External Side Effect（外部副作用）
- Long-term Maintenance（长期维护影响）

不是所有维度都必须存在。

---

## 11. 不构成 Material Difference 的情况

例如两个候选仅仅是：

```text
先加载 Rule Module A，再加载 B
```

和：

```text
先加载 Rule Module B，再加载 A
```

如果最终结果、风险、Scope 和输出一致，只属于 Internal Execution Difference（内部执行差异），不应打扰用户。

---

## 12. Dominated Candidate Elimination（被支配候选消除）

如果 Candidate B 相比 Candidate A：

- 更慢
- 风险更高
- 结果相同
- 没有额外价值

则即使 B 技术上合法，也应在用户交互之前自动消除。

---

## 13. Equivalent Candidate Collapse（等价候选合并）

多个只存在低价值内部差异的候选，应先合并为一个用户可理解的候选。

Banyan 应先完成：

```text
Governance Filtering
+
Equivalent-path Collapse
+
Dominance Elimination
+
Material-difference Grouping
```

再决定是否需要 Informed Decision。

---

## 14. Workflow Choice Preference（工作流选择偏好）

新增跨阶段语义：

```text
Workflow Choice Preference
```

它回答：

> 当存在多个 Valid（合法）且 Materially Distinct（具有实质差异）的工作流候选时，用户希望由谁选择。

本 Patch 不新增新的 F3 DefinitionArtifact Type（定义制品类型）。

---

## 15. 基础模式

### 15.1 AUTO（自动选择）

```text
AUTO
```

表示 Banyan 根据 Goal / Scope / Policy / Standard / Authority / Risk / Reliability（目标 / 范围 / 策略 / 规范 / 权威 / 风险 / 可靠性）自动解析选择。

但：

```text
AUTO != Bypass Governance
AUTO != Silent Scope Expansion
```

### 15.2 ASK_WHEN_MULTIPLE_VALID（多个实质差异合法方案时询问）

正式语义应理解为：

```text
ASK_WHEN_MULTIPLE_MATERIALLY_DISTINCT_VALID
```

只有同时满足：

```text
Multiple
+
Valid
+
Materially Distinct
```

才触发询问。

---

## 16. Workflow Choice Resolution（工作流选择解析）

统一流程：

```text
Goal / Intent / Scope / Context
↓
Dynamic Workflow Composition
↓
Governance / Policy / Authority / Reliability Validation
↓
Valid Workflow Candidates
↓
One Valid Candidate?
├─ YES → 自动使用
└─ NO
    ↓
Materially Distinct?
├─ NO → 自动解析 / 合并
└─ YES
    ↓
Workflow Choice Preference
├─ AUTO → Banyan 自动选择
└─ ASK → Informed Decision
```

---

## 17. AUTO（自动选择）默认行为

AUTO 模式下：

- 优先满足 F4 的 Minimum Valid Workflow Graph（最小合法工作流图）
- 不绕过 Mandatory Governance（强制治理）
- 不降低 Reliability Floor（可靠性底线）
- 不静默扩大用户 Scope（范围）
- 不因为 AI 认为“长期更好”而默认修改更多项目
- 不把未授权的产品 / 设计 / Canonical 语义变更视为自动批准

---

## 18. Minimum Valid Graph 与更大长期优化路线

若存在：

```text
A = Smallest Valid Graph
B = Larger Valid Graph
```

且 B 有明显长期价值，例如：

- 消除跨项目重复
- 统一公共组件
- 降低长期维护成本

则 B 可以成为 Materially Distinct Alternative（具有实质差异的备选工作流）。

AUTO 模式由既有治理规则解析，ASK 模式进入用户选择。

---

## 19. AUTO 不允许静默扩大 Scope

用户要求：

```text
只修 tenant-admin 当前页面
```

Banyan 不得因为发现两个后台共用组件，就自动扩大到 platform-admin + tenant-admin 全部页面，除非已有明确授权 Scope 或合法治理规则允许。

正式保持：

```text
AUTO != Silent Scope Expansion
```

---

## 20. ASK 模式的 Informed Decision（知情决策）

当：

```text
Valid Workflow Candidates >= 2
+
Material Difference = true
+
Workflow Choice Preference = ASK
```

时，调用既有 DecisionProtocolDefinition（决策协议定义）中的 Informed Decision（知情决策）语义。

本 Patch 不新增新的 Informed Decision Protocol。

---

## 21. Informed Decision 最小充分信息

用户应看到 Minimum Sufficient Decision Context（最小充分决策上下文），至少包含：

- 方案名称
- Scope（范围）
- 主要影响
- Validation Scope（验证范围）
- 主要风险
- 长期维护影响
- 关键差异

可附带 AI Recommendation（AI 建议），但：

```text
AI Recommendation != Human Decision
```

---

## 22. AI Recommendation（AI 建议）边界

在 ASK 模式下，AI 可以：

- 总结优缺点
- 推荐一个候选
- 解释推荐原因

但不得因为推荐某一个候选，就隐藏其他具有实质意义的合法候选。

---

## 23. User Explicit Choice Intent（用户显式选择意图）

若用户明确表达：

```text
有几种方案先让我选
```

则形成 Task-level Choice Intent（任务级选择意图）。

即使默认偏好为 AUTO，当前任务也应进入 ASK 逻辑。

---

## 24. User Explicit Auto Intent（用户显式自动意图）

若用户明确表达：

```text
这次按最合理合法方案自动处理，不用问我
```

可形成 Task-level AUTO Override（任务级自动选择覆盖）。

但仍不得绕过 Policy / Authority / Mandatory Validation，也不得静默扩大 Scope 或自动批准后续 Canonical 语义变化。

---

## 25. Preference Scope（偏好范围）

Workflow Choice Preference 至少支持逻辑 Scope：

```text
User Default
Project Preference
Task Override
```

默认解析顺序：

```text
Task Override
> Project Preference
> User Default
```

这是 Preference Resolution Precedence（偏好解析优先顺序），不是 Governance Authority Priority（治理权威优先级）。

---

## 26. Workflow Choice Preference != Execution Governance Mode

正式保持：

```text
Workflow Choice Preference
!= Execution Governance Mode
```

Execution Governance Mode（执行治理模式）回答：

> 当前工作流执行需要多强的治理强度。

Workflow Choice Preference（工作流选择偏好）回答：

> 多个合法且有实质差异的工作流出现时，由谁选择。

两者可以独立组合。

---

## 27. Workflow Choice Preference 不改变 Governance Mode

禁止：

```text
ASK → 自动升级 CONTROLLED
AUTO → 自动降级 FAST
```

两者属于不同维度。

---

## 28. Selected Workflow（选中的工作流）边界

正式保持：

```text
Selected Workflow
!= Product Decision
!= Design Decision
!= Approval
!= Apply Authorization
!= Runtime Permission
```

用户选择一条工作流路线，只表示当前任务采用该路线。

后续若出现 Canonical Design Rule（正式设计规则）或 Product Semantics（产品语义）变化，仍需对应 Authority / Decision / Approval / F7 Governed Change / Apply Authorization。

---

## 29. Workflow Choice 不替代 Product Decision

F4 负责识别和路由工作流选择。

F5 继续判断某个选择是否真正影响 Product Semantics（产品语义）并构成 `DECISION_REQUIRED`。

工作流选择本身不能替代 F5 Product Decision（产品决策）。

---

## 30. Banyan-wide Applicability（全局适用性）

本 Patch 不局限于开发工作流，可应用于：

- Requirement / Product（需求 / 产品）
- Architecture（架构）
- UI / Design（UI / 设计）
- Development（开发）
- Validation（验证）
- Change（变更）
- Migration（迁移）
- Documentation Governance（文档治理）
- Project Adoption（项目接入）
- Engineering Standard Maintenance（工程规范维护）

---

## 31. Candidate Count（候选数量）控制

Banyan 不应直接把内部所有候选图暴露给用户。

内部若生成 12 个合法执行图，应先通过：

- Equivalent Candidate Collapse（等价候选合并）
- Dominated Candidate Elimination（被支配候选消除）
- Material Difference Grouping（实质差异分组）

最终只向用户展示最小有意义候选集。

---

## 32. Default Automation Bias（默认自动化倾向）

Banyan 默认应偏向：

```text
不打扰用户
```

逻辑上：

```text
Can resolve deterministically?
→ YES → 自动

Only one valid path?
→ YES → 自动

Multiple but materially equivalent?
→ YES → 自动

Preference = AUTO?
→ YES → 自动

否则
→ Informed Decision
```

目标继续保持：

```text
Reliable Automatic Routing
×
Minimum Human Decision Governance
```

---

## 33. Owner Boundary（Owner 边界）

### F4

负责：

- Dynamic Workflow Composition
- Workflow Candidate
- Validity Filtering
- Material Difference Detection
- Workflow Choice Preference
- Workflow Selection Resolution
- Decision / Governance Interrupt Node

### F3

DecisionProtocolDefinition（决策协议定义）继续提供共享 Informed Decision 协议语义。

不新增：

```text
WorkflowChoiceDefinition
```

### F5

继续负责：

- Product Semantics
- Requirement Semantics
- DECISION_REQUIRED
- Human Product Decision

### F7

继续负责：

- Candidate != Human Decision
- Selected Candidate != Apply Authorization
- Change / Apply / History

### F11

未来负责实际 Control Plane UX（控制面交互），例如：

- User Default 设置
- Project Preference 设置
- Task Override
- Candidate Comparison UI
- Recommendation 展示
- Informed Decision Card

本 Patch 不提前冻结具体 UI 形态。

---

## 34. No-Loss Mapping（无损映射）

| 既有语义 | 本 Patch 统一语义 |
|---|---|
| F4 Workflow Family Selection / Composition | Dynamic Workflow Composition |
| F4 Minimum Valid Workflow Graph | 保留为默认合法图原则 |
| F4 Decision / Governance Interrupt Node | 承载需要人工工作流选择时的中断 |
| F5 DECISION_REQUIRED | 保持产品 / 需求语义决策边界 |
| F5 deterministic automation default | 保留 |
| F7 multiple_candidates_require_informed_decision=false | 保留并正式解释 |
| F7 Candidate != Human Decision | 保留 |
| F7 Selected Candidate != Apply Authorization | 保留 |
| AUDIT-PATCH-002 Execution Governance Mode | 与 Workflow Choice Preference 明确分离 |

---

## 35. F3 Taxonomy Impact（F3 类型体系影响）

本 Patch：

```text
DOES NOT ADD WorkflowChoiceDefinition
DOES NOT ADD WorkflowCandidateDefinition
DOES NOT ADD WorkflowPreferenceDefinition
```

Workflow Choice Preference 是 Scoped Preference（有范围的偏好语义），不是新的 DefinitionArtifact Type。

---

## 36. Affected Stage（受影响阶段）

### F3
复用 DecisionProtocolDefinition，不新增 WorkflowChoiceDefinition。

### F4
Primary Change：增加 Workflow Candidate / Material Difference / Workflow Choice Preference / Selection Resolution 统一合同。

### F5
Boundary Clarification：Workflow Choice 不替代 Product Decision。

### F7
Boundary Clarification：Multiple Candidates != Automatic Informed Decision；Selected Workflow != Apply Authorization。

### F11
Future UX Owner：Preference Settings / Choice Comparison / Informed Decision UI。

---

## 37. Forbidden Interpretations（禁止解释）

禁止：

1. Multiple Candidates = Automatic Informed Decision
2. 两条技术路径存在 = 必须询问用户
3. Workflow Choice Preference = Disable Validation Switch
4. AUTO = Bypass Governance
5. AUTO = Silent Scope Expansion
6. AUTO = Automatic Product Approval
7. ASK = CONTROLLED Governance Mode
8. AUTO = FAST Governance Mode
9. Workflow Choice Preference = Execution Governance Mode
10. 用户选择 Workflow = 批准后续所有语义修改
11. Selected Workflow = Product Decision
12. Selected Workflow = Apply Authorization
13. Selected Workflow = Runtime Permission
14. AI Recommendation = Human Decision
15. AI 推荐某候选 = 可以隐藏其他实质合法候选
16. 内部候选数量直接暴露给用户
17. Runtime 动态组合 = 自动创建新的 Canonical WorkflowDefinition
18. AI 发现更大长期收益 = 可以静默扩大用户 Scope
19. 用户选择“快速” = 可以绕过 Mandatory Validation
20. User Preference = Authority
21. Candidate = Canonical Truth
22. 借本 Patch 进入 Implementation / RP2 / Authority Cutover / Final Activation / Legacy Retirement

---

## 38. Approval Meaning（批准含义）

若本 Patch HUMAN_APPROVED，表示接受：

1. Dynamic Workflow Composition（动态工作流组合）是 Banyan-wide 全局能力；
2. AI 只能动态组合已有受治理工作流定义 / 子工作流 / 控制语义，不得运行时自动发明新的正式 WorkflowDefinition；
3. Workflow Candidate 必须先经过 Governance / Policy / Authority / Scope / Reliability 等合法性过滤；
4. Multiple Candidates != Automatic Informed Decision；
5. 只有多个 Valid 且 Materially Distinct 的工作流才形成用户可感知 Workflow Choice；
6. 增加 Workflow Choice Preference；
7. 第一版基础模式为 AUTO 与 ASK_WHEN_MULTIPLE_VALID；
8. 单一合法、实质等价和可确定性解析路径默认自动处理；
9. ASK 模式通过既有 Informed Decision 协议提供最小充分比较信息；
10. AI Recommendation != Human Decision；
11. User Explicit Choice / Auto Intent 可形成 Task-level Override；
12. Workflow Choice Preference 支持 User Default / Project Preference / Task Override 逻辑范围；
13. Workflow Choice Preference != Execution Governance Mode；
14. Selected Workflow != Product Decision / Approval / Apply Authorization / Runtime Permission；
15. AUTO 不得绕过 Mandatory Governance / Reliability Floor，也不得静默扩大 Scope；
16. F11 后续负责 UX，本 Patch 不提前实现；
17. 本批准不授权真实 Implementation 或 Legacy Migration。

---

## 39. Integration Target（未来整合目标）

若 HUMAN_APPROVED：

- `F3_Definition_Artifact_Taxonomy_Freeze_Pack_v1.1 Candidate`
- `F4_Orchestration_Semantic_Freeze_Pack_v1.1 Candidate`
- `F5_PRD_Governance_Freeze_Pack_v1.1 Candidate`
- `F7_Change_Canonical_Apply_Freeze_Pack_v1.1 Candidate`

并向未来 F10 Runtime（运行时）和 F11 Control Plane UX（控制面交互）提供共同语义合同。

---

## 40. Current Status

当前：

```text
B1-PATCH-05
= APPROVAL_DRAFT
= NOT HUMAN_APPROVED
```

只有用户明确回复：

```text
B1-PATCH-05 HUMAN_APPROVED
```

后，才能生成正式：

```text
AUDIT-PATCH-005
```

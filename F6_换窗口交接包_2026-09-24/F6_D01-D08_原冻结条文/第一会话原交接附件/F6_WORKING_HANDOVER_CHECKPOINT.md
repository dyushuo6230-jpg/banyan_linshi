# F6_WORKING_HANDOVER_CHECKPOINT

> 用途：切换到新的 ChatGPT 窗口后继续 Banyan 架构冻结工作。  
> 当前阶段：**F6 — UI_SPEC / Design Truth / Visual Governance**  
> F1～F5：已完成并已由用户上传 Git，本交接不重复展开。  
> 本交接只汇总 F6 已确认内容、当前未完成项、全局约束和下一窗口继续方式。  
> **Implementation = NOT_AUTHORIZED**

---

## 1. 当前状态总览

```text
F6-D01 = HUMAN_APPROVED / Architecture Freeze PASS
F6-D02 = HUMAN_APPROVED / Architecture Freeze PASS
F6-D03 = HUMAN_APPROVED / Architecture Freeze PASS
F6-D04 = HUMAN_APPROVED / Architecture Freeze PASS
F6-D05 = HUMAN_APPROVED / Architecture Freeze PASS
F6-D06 = HUMAN_APPROVED / Architecture Freeze PASS
F6-D07 = HUMAN_APPROVED / Architecture Freeze PASS
F6-D08 = HUMAN_APPROVED / Architecture Freeze PASS

F6-D09 = HUMAN_REVIEW / 尚未确认
F6-D10 = 尚未正式形成最终候选稿

Implementation / RP2 / Final Activation / Cursor Coding = NOT_AUTHORIZED
```

---

## 2. F6-D01 — UI Design Governance Foundation

### 已确认核心

- Design Source、Material、Evidence、UDC、Shared Foundation、UI Design Rule、Design Package、UI_SPEC 的职责边界已经拆开。
- Legacy F0～F4 仅表示设计证据 fidelity / compatibility projection，不代表 Design Package 的质量、权威、完整度或恢复等级。
- **无设计图也允许形成高质量、精确、受治理的 Design Package。**
- User Design Constraint（UDC）是用户明确表达的设计约束事实，是受治理输入，但不是最终 UI 施工真源。
- **Current Effective UI_SPEC** 才是批准后的 UI Construction Contract。
- Material Intake 与 UI Design Intelligence 分离。
- Reconciliation Buffer 只保存未解决问题，不成为第二真源。
- Shared Foundation = 项目已经确认的共享 Design WHAT。
- UI Design Rule = 通用 Design SHOULD/WHY。
- Frontend Rule = 通用 Engineering HOW。
- Design Package = page/component-specific Design Target。
- AnyDesign = Provider / Skill，不拥有 Core Authority。
- 文件保存 canonical governed truth；SQLite 后续只做 derived index / map。
- Architecture Freeze ≠ Implementation Authorization。

---

## 3. F6-D02 — Rule / Implementation Knowledge Governance

### 状态

```text
D02-01 ～ D02-10 = HUMAN_APPROVED
FC-01 ～ FC-06 = HUMAN_APPROVED
```

### 已确认核心

- UI Design Rule System 与 Frontend Rule System 分离。
- Rule 不使用简单 priority number，而采用：
  - Strength
  - Authority
  - Scope
  - Applicability
  - Conflict / Relation
- 多规则可能同时匹配时，关系必须显式：
  - COMPOSE
  - SPECIALIZE
  - DEPEND_ON
  - ALTERNATIVE
  - OVERRIDE
  - EXCLUDE
  - CONFLICT
- 未解析关系不能留给执行 AI 猜。
- Module 支持稳定职责、拆分、合并、迁移、版本化；Project Binding 不自动追随 latest。
- Material → Fragment → Rule Candidate → Reconciliation → Delta。
- Module Index + Rule Association 是检索层，不是 Authority。
- Profile 只选择/绑定，不复制 Rule Body。
- Effective Design Context 与 Effective Implementation Context 都是 task-scoped derived context。
- Design Rule 不可改变 Product Semantics，不可覆盖 UDC / Foundation / UI_SPEC。
- Design → Implementation 通过：
  - Design Target
  - Implementation Semantic Need
  - Frontend Rule Resolution
  - Implementation Decision
- 生命周期复用 Stable ID / Version / Freshness / Supersession / Impact。
- 当前不实现 AI autonomous rule learning / promotion。

---

## 4. F6-D03 — Design Source × Scene × Semantic Tree × Design Truth

### 状态

```text
DS-01 ～ DS-32 = HUMAN_APPROVED
```

### 主链

```text
D01 Registered Material
→ Design-relevant role / Design Source Registration
  ├─ scene-capable source
  │  → Raw Scene
  │  → Normalized Scene
  │  → Semantic Interpretation
  │  → Evidence
  ├─ semantic/document/prototype-specific extraction
  │  → Evidence
  └─ governed UDC / Foundation / Rules direct
→ Design Reconciliation
→ Design Truth Model inside Design Package
→ UI Governance
→ UI_SPEC
```

### 已确认核心

- Design Source 是 Material 的 design-relevant role，不自动获得 Authority。
- Raw Scene 是 Provider 派生机器表示，不是 Design Truth。
- Normalized Scene = provider-neutral structural observation。
- Geometry 是观测/测量结果，不等于 fixed CSS。
- Semantic Tree = interpretation layer。
- FACT / INFERENCE / RECOMMENDATION / UNKNOWN 必须分开。
- 静态设计不能脑补 Hover、Loading、Drag、Responsive、业务动作。
- Existing UI / Code 默认是 Current Reality Evidence。
- Reference Design 默认不是 Target Truth。
- UDC / Foundation / Rules 可以绕过 Scene 直接参与 Design Formation。
- Design Truth Model 属于 Design Package，不建立独立 competing truth。
- No-image path 是一等公民。
- Provider / Normalizer / Semantic Interpreter 可替换。

---

## 5. F6-D04 — Visual Property × Design Token × Shared Foundation

### 状态

```text
DT-01 ～ DT-30 = HUMAN_APPROVED
```

### 核心模型

```text
Observed Visual Property
≠ Local Design Value
≠ Design Token Candidate
≠ Governed Design Token
≠ Token Resolution
≠ Shared Foundation
```

### 已确认核心

- 设计图中看到的颜色、圆角、字号、间距等首先只是 Visual Property / Evidence。
- 不是所有视觉值都必须 Token 化。
- Repetition / Frequency ≠ Authority。
- Governed Token 需要 stable Design Meaning + Scope + Identity + Governed Evolution。
- Token 可表达：
  - direct value
  - semantic meaning
  - reference / alias
  - contextual variant
- 不把 Primitive / Semantic / Component 等 taxonomy 永久写死进 Core。
- Shared Foundation 比 Token 大；Token 只是 Foundation 的结构化表达机制之一。
- 同一个 Shared Design Fact 只能有一个 canonical semantic owner。
- Token / Design Value Owner 由真实 Scope 决定。
- 不同 App 值相同，不代表是同一 Token。
- Theme / State / Device 使用 contextual resolution，不默认复制完整真源。
- Alias 必须 resolvable / traceable / acyclic。
- Token Resolution 不使用 last-file-wins / CSS cascade 作为治理优先级。
- W3C DTCG 作为 compatibility/import/export representation，不锁死 Core。
- Existing CSS Variables / Framework Theme = Current Reality Evidence。
- Design Token 与 CSS Variable / Framework Token 分层。
- Shared Token/Foundation Change 进入 Version/Freshness/Impact，不静默改变历史 UI_SPEC。
- 当前不做 autonomous token learning / promotion / foundation optimization。

### 一句话

```text
看到一个值 ≠ Token
成为 Token ≠ Shared Foundation
进入 Shared Foundation ≠ 自动改变所有已有 UI_SPEC / 页面
```

---

## 6. F6-D05 — Behavior × State × Interaction Evidence

### 状态

```text
BI-01 ～ BI-30 = HUMAN_APPROVED
```

### 核心原则

```text
Visible State
≠ Behavior
≠ Business State Transition
```

### 已确认核心

- UI State、Data State、Product/Business State、Runtime State 分离。
- Static Design Source 只能证明明确展示的状态，不能自动证明完整 Behavior。
- State Evidence 与 State Definition 分开。
- Common State Vocabulary 可复用，但必须可扩展。
- Interaction Definition 至少能够表达：
  - Trigger
  - Target
  - Condition
  - Action
  - State Change
  - Transition
  - Overlay
  - Close/Error
- UI Interaction 不拥有 Product Business Logic。
- Component/Button 类型不能自动推出业务动作。
- Hover 等状态必须受 Device / Applicability 限制。
- Responsive 行为必须有证据或明确 Design Decision。
- State Transition 与 Motion/Animation 分离。
- UI Design Rule 可以补 UI-level Behavior Design，不能创造 Product Behavior。
- 没有证据时允许 UNKNOWN。
- 低风险、局部、可逆、可验证的 UI micro-behavior 可受 AUTONOMY-01 处理。
- Behavior Model 属于 Design Package，不成为第二真源。
- Behavior Gap 复用既有 Gap / Decision Routing。
- Existing UI Behavior 默认是 Current Reality Evidence。
- Behavior Revision 必须版本化并进入 Impact。

---

## 7. F6-D06 — Data Evidence × UI Data Semantics × Demo Fixture

### 状态

```text
DU-01 ～ DU-30 = HUMAN_APPROVED
```

### 核心模型

```text
Display Value
≠ Data Evidence
≠ UI Data Slot
≠ UI Field Semantic
≠ Binding Requirement
≠ Demo Fixture
≠ Business/API Data Contract
```

### 已确认核心

- 设计图中的具体值默认是 Display / Fixture Evidence，不是 Business Fact。
- UI Data Slot 表示“这里需要动态数据”，不决定 API 字段。
- UI Field Semantic 描述页面消费的数据意义，不成为 Domain Model。
- Data Binding Requirement 是 UI Semantic ↔ Real Data Source 的桥梁。
- D06 不得自动发明 API / DB 字段 / Product Capability。
- OpenAPI / API / Code 可作为 Data/Technical Evidence。
- Concrete API Binding 属于 Implementation Mapping。
- Demo Fixture 用于稳定设计、视觉、交互验证，不是生产数据。
- Fixture 必须 deterministic / reproducible。
- Fixture Coverage 按 Applicability，不机械要求每个页面覆盖所有场景。
- Data Scenario 与 UI State 分离：
  - D06 owns data scenario
  - D05 owns UI response
- Formatter / Fallback / Overflow 属于 presentation semantics，不能变成业务规则。
- Derived Presentation Value 必须可追溯。
- UI View Model 不成为第二 Domain Truth。
- Partial Binding 合法；未知 Concrete Binding 保持 UNKNOWN。
- DATA_COVERAGE_GAP 显式。
- Fixture Revision 可影响 Validation Baseline freshness。
- 当前不做 autonomous data learning / schema creation。

---

## 8. F6-D07 — Design Package × UI_SPEC Governance

### 状态

```text
UC-01 ～ UC-32 = HUMAN_APPROVED
```

### 核心三分

```text
Design Package
= 具体设计目标

UI_SPEC
= 已批准的 UI Construction Contract

Effective UI Contract
= 某个 Task/Batch 锁定消费的执行快照
```

### 已确认核心

- Design Package = page/component-specific Design Target Owner。
- Design Package 不拥有 Product Authority。
- Draft UI Contract = reviewable derived candidate。
- UI_SPEC = 经 UI Governance 批准的 Construction Contract。
- UI_SPEC 不复制整个 Design Package。
- PRD = Product/Business Truth。
- UI_SPEC = Approved UI Construction Truth。
- Business-affecting UI Change 必须回 Product Governance。
- 相关 PRD 变化可使受影响 UI_SPEC STALE / REVIEW_REQUIRED。
- Design Package Revision 不自动改变 UI_SPEC。
- Design Revision 与 UI_SPEC Version 是独立版本轴。
- Source-only Change 不强制升级 UI_SPEC。
- Version / Approval / Freshness / Current Effective 分离。
- Approved ≠ Current Effective。
- Effective UI Contract 是 derived execution snapshot，不是第二 UI Truth。
- Active Batch 不自动追随 latest UI_SPEC。
- New UI 默认只产生 NEWER_UI_AVAILABLE。
- Design Package Coverage 与 UI_SPEC Coverage 分开。
- Partial UI_SPEC 合法。
- Design Acceptance 与 UI Contract Approval 分开，但同一根 Human Decision 不重复确认。
- UI_SPEC / Effective UI Contract Ready ≠ Implementation Authorization。
- Coding Agent 默认消费：
  - Current Effective PRD
  - Current Effective UI_SPEC
  - Effective Frontend Rules
  - Technical Context

---

## 9. F6-D08 — Implementation Guidance × Implementation IR × Implementation Pack

### 状态

```text
IG-01 ～ IG-32 = HUMAN_APPROVED
```

### 核心模型

```text
Implementation Semantic Need
≠ Implementation Guidance
≠ Implementation IR
≠ Implementation Pack
≠ Framework Adapter Output
```

### 已确认核心

- D08 复用 D02-09 的 Design→Implementation Semantic Bridge，不造第二桥。
- Implementation Guidance = 当前任务的 HOW。
- Frontend Rule = reusable HOW rule。
- Implementation IR = framework-neutral machine-readable HOW semantics。
- Implementation Pack = task/page/component-scoped derived construction pack。
- Implementation Pack ≠ UI_SPEC。
- Scene / Design / Implementation / Framework Representation 分层。
- Rendered Geometry 不自动变 Fixed Sizing。
- Sizing 优先表达 fixed/fill/intrinsic/stretch/fraction/minmax/parent-controlled 等关系。
- Parent-driven Sizing 是一等能力。
- **布局实现关系，不抄截图坐标。**
- Absolute 可使用，但仅用于真正的附着/叠层/定位语义，不作为截图还原默认策略。
- Flex/Grid 是 Implementation Decision/Recommendation，不是 Design Fact。
- 重要 Implementation Decision 保留 Origin/Reason/Trace。
- Behavior/Data/Token 使用 stable refs，不复制第二 Truth。
- Semantic Component 与 Framework Component 分离。
- Existing Components / Code Conventions = Reuse/Technical Evidence。
- Responsive IR 表达 transformation，不只写 breakpoint。
- 无证据不创造 Mobile/Tablet 行为。
- Spacing / Overflow / Box Model / Constraints 结构化。
- CSS / Implementation Hint 只是 Recommendation。
- Legal Alternative 与 Deviation 分开。
- Deviation 必须记录 Expected / Actual / Reason / Approval。
- Adapter limitation → Feasibility / Capability Issue，不静默降级。
- Implementation Revision 与 UI_SPEC Revision 分离。
- Compiler 不重新做 Authority Resolution。
- Coding Agent 不建立第二全局 Resolver。
- Framework Adapter 只做技术栈翻译。
- 当前不做 autonomous implementation learning / pattern promotion。

---

## 10. 全局架构设计质量准则

后续所有定稿内容继续遵循：

### 灵活
不要把结构写死，允许组合、扩展、局部覆盖和演进。

### 有条理
对象、职责、层级、输入输出和状态边界清楚。

### 可扩展
新增 Module / Rule / Provider / 技术栈时不推翻 Core。

### 速度快
优先：

```text
Scope
→ Profile
→ Index
→ Targeted Canonical Read
→ Minimum Sufficient Context
```

避免全量扫描和无意义重复确认。

### 设计符合逻辑
必须持续分开：

```text
FACT ≠ INFERENCE
INFERENCE ≠ RECOMMENDATION
RULE ≠ FACT
EVIDENCE ≠ TRUTH
TRUTH ≠ AUTHORITY
APPROVED ≠ CURRENT EFFECTIVE
READINESS ≠ AUTHORIZATION
DESIGN ≠ IMPLEMENTATION
LATEST ≠ CURRENT EFFECTIVE
CONFIDENCE ≠ AUTHORITY
```

### 使用便捷但可靠

```text
低风险 / 确定 / 可逆 / 可验证
→ 自动完成

真实冲突 / 高风险 / 不可逆 /
权限安全 / 产品语义改变 / Authority 不明
→ 才打扰用户
```

核心体验：

```text
用户表达意图，Banyan 承担治理成本。
```

### 条款兼容且执行无歧义

多规则可匹配时必须提前说明：

```text
COMPOSE
SPECIALIZE
DEPEND_ON
ALTERNATIVE
OVERRIDE
EXCLUDE
CONFLICT
```

不能把“谁赢”留给执行时 AI。

### 当前不实现 AI 自主学习

当前重点是把：

```text
Core
Module
Rule
Skill
Workflow
Provider
Profile
Context
Adapter
Artifact
```

设计成：

```text
Stable ID
Explicit Contract
Version
Revision
Replace
Split/Merge
Supersession
Migration
Registry
Binding
Trace
```

未来 Learning 必须复用现有治理，不给 AI 隐藏自修改权限。

---

## 11. 当前 F6 尚未确认内容

### F6-D09

旧候选名称：

```text
Visual Validation × Design Drift × Interaction Regression
```

旧候选：

```text
VV-01 ～ VV-30
```

状态：

```text
HUMAN_REVIEW
```

**注意：D09 不能直接沿用旧稿冻结。**

因为 D09 候选之后又新增了大量成熟讨论：

- UI Conformance Session；
- Visual Repair Loop 降为 VISUAL + REPAIR compatibility profile；
- 默认 OFF / ON_DEMAND / NON_BLOCKING；
- Target Resolution；
- 只有 PRD、没有 UI Target 时不能直接 Repair；
- Protected Functional Baseline；
- Allowed Mutation Scope；
- Repair 不得破坏已实现功能；
- Repair ≠ 重写页面。

这些需要重新归并进新版 D09/D10。

### F6-D10

尚未正式形成完整最终候选。

建议名称：

```text
Repair Governance
× UI Conformance Action
× Design-Code Synchronization
```

---

## 12. UI Conformance / 视觉循环：当前成熟讨论结论

### 12.1 顶层能力

建议正式使用：

```text
UI Conformance Session
UI 一致性校准会话
```

不再把 `Visual Repair Loop` 作为 Core 顶层能力名。

Legacy：

```text
Visual Repair Loop
```

降为：

```text
UI Conformance Session
mode = VISUAL
action = REPAIR
```

即 Compatibility Profile / Alias。

### 12.2 存在意义

普通指令主要解决：

```text
我要改变 Target
```

UI Conformance Repair 解决：

```text
已有 Target
+
已有 Actual
+
让 Actual 收敛到 Existing Target
```

所以它不是“多一种 AI 改页面方式”，而是：

```text
Inspect
→ Diff
→ Root Cause
→ Bounded Repair
→ Revalidate
```

### 12.3 启动方式

默认：

```text
OFF
ON_DEMAND
NON_BLOCKING
```

- 用户点名才启动；
- 不属于固定开发阶段；
- 不改 PROJECT_STAGE；
- 不计主进度分母；
- 不默认阻塞功能开发；
- 可在开发中、静态预览后、功能完成后、验收前、重构后、补图后启动。

只有显式 Project / Acceptance Policy 才能把某次 Session Result 提升为 Gate。

### 12.4 Scope

支持局部点名：

```text
Application
Page
Region
Component
State
Interaction
```

例如：

```text
tenant-admin
/material
UploadProgressPanel
UPLOADING state
```

未点名区域默认 OUT_OF_SCOPE / PROTECTED。

### 12.5 Action

建议：

```text
INSPECT
= 只检查，不改代码

REPAIR
= 检查 → 修复 → 复验

AUDIT
= 多维度完整校准/审计
```

Loop 只属于 REPAIR 内部。

### 12.6 Mode

可扩展支持：

```text
VISUAL
LAYOUT
STATE
INTERACTION
RESPONSIVE
DATA_SCENARIO
ACCESSIBILITY
FULL_UI
```

---

## 13. Conformance Target Resolution

视觉循环真正目标不是“永远听图片”。

建议概念：

```text
Conformance Target Bundle
```

目标是在明确：

```text
Scope
Authority
Version
Context
```

下解析出的 Current Conformance Target。

### 情况 A：有 Current Effective UI_SPEC

主要 Target：

```text
Current Effective UI_SPEC
```

Design Package / 图片 / Prototype 作为辅助视觉基准。

如果 UI_SPEC 与图片冲突：

```text
REPAIR_NOT_READY
→ 先 Reconcile
```

不能 Repair Agent 自己选。

### 情况 B：无 UI_SPEC，有 Governed Design Package

Target：

```text
Current Design Package / Design Target
```

可做 structural / visual / state / responsive conformance。

### 情况 C：无 UI_SPEC，只有用户明确点名 PNG / Figma / 墨刀

可以启动：

```text
User-Designated Source Target
```

但结果只能称：

```text
Matched Against Design Source
```

不能称：

```text
Approved UI_SPEC Conformance
```

### 情况 D：只有 PRD，没有 UI Target

**不能直接 REPAIR。**

正确：

```text
PRD
→ Design Formation
→ Design Package
→ optional UI Governance / UI_SPEC
→ Conformance Repair
```

核心：

```text
PRD ≠ Visual Repair Target
```

### 情况 E：PRD + “保持现有风格”

Existing UI 默认只是：

```text
Current Reality Evidence
```

先把明确采用的风格形成：

```text
Shared Foundation / Design Package
```

再作为 Repair Target。

### 情况 F：Existing Implementation

默认：

```text
Current Reality
```

用户明确要求“其它区域保持现状”时，可以作为：

```text
Protected Baseline
```

但不自动成为 Design Truth。

---

## 14. Protected Functional Baseline

建议正式概念：

```text
Protected Functional Baseline
```

视觉/一致性 Repair 默认保护：

```text
API integration
Routing
Permission
Business Logic
Business State
Data Contract
Persistence
Upload logic
Delete logic
Pagination
Query behavior
Validated callbacks
Existing accepted interaction
```

这些默认：

```text
PRESERVE
```

### Repair 可修改

在 Allowed Mutation Scope 内可调整：

```text
CSS / Style
Token reference
Layout wrapper
Visual DOM structure
Decoration
Overlay
Scroll container
Local visual component structure
Local layout strategy
```

前提：

```text
不得改变 Product/Business Semantics
```

### 如果视觉 Target 暗示新增功能

例如设计图出现：

```text
暂停上传
永久删除
新权限
新业务状态
```

但 Product/Implementation 没有：

```text
FUNCTIONAL_GAP / BUSINESS_AFFECTING_CHANGE
→ Stop related Repair
→ Return to Product/Change Governance
```

视觉 Repair 不得自己新增 API、业务状态机或数据语义。

---

## 15. 每次 Repair 必须有三重边界

```text
Target Scope
Allowed Mutation Scope
Protected Functional Baseline
```

例如：

```text
Target:
UploadProgressPanel

Allowed:
布局、样式、视觉结构、装饰元素

Protected:
upload API
queue
progress calculation
retry/cancel semantics
route
permission
other page regions
```

---

## 16. Repair 不是推倒重写

视觉循环真正循环的是：

```text
Inspect
→ Diff
→ Repair
→ Revalidate
```

不是：

```text
Rewrite Page
→ Rewrite Page Again
```

修改优先级建议从小到大：

```text
1. Token / CSS value
2. CSS rule
3. Local style structure
4. Local DOM wrapper
5. Local component visual structure
6. Local layout refactor
7. Shared visual component adjustment
8. Wider architectural refactor
```

一旦超出 Allowed Mutation Scope：

```text
STOP / ESCALATE
```

---

## 17. Repair 必须保护功能回归

每轮：

```text
UI/Visual Repair
↓
UI Revalidation
+
Protected Function Smoke/Regression Check
```

成功条件：

```text
Target Conformance = PASS / 达到验收阈值
AND
Protected Functional Regression = 0
```

---

## 18. 下一窗口继续点

下一步不是直接冻结旧 D09。

应该：

```text
1. 重新打开 F6-D09
2. 把最近 UI Conformance / Target Resolution /
   Protected Functional Baseline 讨论归并进去
3. 输出完整新版 D09
4. 用户确认
5. 再进入 D10
```

---

## 19. 当前禁止事项

```text
DO NOT:
- 重新设计 F1～F5
- 重开 F6-D01～D08
- 把 D09 当成已确认
- 把视觉循环变成默认 Gate
- 把 Visual Repair 等同于页面重写
- 让 Repair 修改 API / 业务逻辑 / 权限 / 产品状态
- 只有 PRD 时直接启动视觉 Repair
- 用 latest Design Source 自动覆盖 Current Effective UI_SPEC
- 让 AI 自主学习并修改 Framework / Rule / Foundation
- 进入 Implementation / Cursor Coding
```

---

## 20. 当前 NEXT

```text
NEXT:
F6-D09
Visual Validation × Design Drift × Interaction Regression

但需先吸收：
- UI Conformance Session
- Conformance Target Resolution
- Protected Functional Baseline
- Allowed Mutation Scope
- Inspect vs Repair
- Legacy Visual Repair Loop compatibility
```

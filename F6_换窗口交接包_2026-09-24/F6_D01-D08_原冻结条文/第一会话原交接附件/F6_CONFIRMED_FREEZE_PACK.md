# F6_CONFIRMED_FREEZE_PACK

> 只包含 F6 已经 HUMAN_APPROVED 的 D01～D08。  
> 不包含 D09/D10 未批准设计。  
> Implementation = NOT_AUTHORIZED。

---

## F6-D01 — UI Design Governance Foundation

- Design Source / Material / Evidence / UDC / Foundation / Rule / Design Package / UI_SPEC 边界已冻结。
- No-image path 为一等公民。
- UDC 是用户设计约束，不是 UI_SPEC。
- Shared Foundation = project-specific confirmed shared Design WHAT。
- Design Package = page/component-specific Design Target。
- AnyDesign = Provider/Skill，不是 Authority。
- Canonical governed truth 在文件；SQLite 后续为 derived index/map。
- Architecture Freeze ≠ Implementation Authorization。

---

## F6-D02 — Rule / Implementation Knowledge Governance

- UI Design Rule System 与 Frontend Rule System 分离。
- Rule resolution 不靠 priority number。
- 必须显式关系：COMPOSE / SPECIALIZE / DEPEND_ON / ALTERNATIVE / OVERRIDE / EXCLUDE / CONFLICT。
- 未解析关系不得由执行 AI 猜。
- Module 可拆分/合并/迁移/版本化。
- Profile 只选择/绑定，不复制 Rule Body。
- Effective Design/Implementation Context 为 task-scoped derived context。
- Design→Implementation Semantic Bridge 已冻结。
- Latest ≠ Current Effective。
- Learning deferred。

---

## F6-D03 — Design Source / Scene / Semantic / Design Truth

- Design Source 是 Material 的角色，不是第二真源。
- Raw Scene / Normalized Scene / Semantic Tree 都不是最终 Design Truth。
- Geometry ≠ fixed CSS。
- FACT / INFERENCE / RECOMMENDATION / UNKNOWN 分离。
- Static source 不脑补行为、响应式、业务语义。
- Existing UI/Code = Current Reality Evidence。
- Reference Design 默认不是 Target。
- Design Truth Model 属于 Design Package。
- Provider/Normalizer/Interpreter 可替换。

---

## F6-D04 — Visual Property / Token / Shared Foundation

- Observed Property / Local Value / Token Candidate / Governed Token / Resolution / Foundation 分离。
- 不是所有视觉值都 Token 化。
- Repetition ≠ Authority。
- Token 需要 stable meaning / scope / identity。
- Taxonomy 不写死。
- Foundation > Token。
- 一个 shared fact 一个 canonical owner。
- Scope 决定 owner。
- Theme/State/Device 用 contextual resolution。
- Alias 可解析、可追踪、无环。
- No last-file-wins。
- DTCG 是 adapter/compatibility。
- CSS vars/theme = reality evidence。
- Shared change 进入 impact，不静默更新历史 UI_SPEC。
- No autonomous token learning/promotion。

---

## F6-D05 — Behavior / State / Interaction

- UI State / Data State / Business State / Runtime State 分开。
- Static source 只证明可见状态。
- State Evidence != State Definition。
- State vocabulary 可扩展。
- Interaction 可表达 Trigger/Target/Condition/Action/Transition 等。
- UI Interaction 不拥有 Product Business Logic。
- Component type 不自动推业务动作。
- Hover 等受 Applicability。
- Responsive 必须有证据。
- Transition != Motion。
- UNKNOWN 合法。
- Low-risk micro-behavior 可 bounded autonomy。
- Behavior Model 属于 Design Package。
- Existing UI behavior = Current Reality Evidence。

---

## F6-D06 — Data / UI Data Semantics / Fixture

- Display Value / Evidence / Slot / Field Semantic / Binding / Fixture / Business Contract 分开。
- 设计数据默认是 demo/display evidence。
- UI Slot 不决定 API。
- Field Semantic 不成为 Domain Model。
- Binding Requirement 是桥梁。
- 不发明 API/DB/Product Capability。
- Fixture deterministic / reproducible。
- Data Scenario 与 UI State 分开。
- Formatter/Fallback/Overflow 不成为业务规则。
- UI View Model 不成为第二 Domain Truth。
- Partial binding 合法。
- DATA_COVERAGE_GAP 显式。
- No autonomous schema creation。

---

## F6-D07 — Design Package / UI_SPEC / Effective UI Contract

```text
Design Package = 具体设计目标
UI_SPEC = 已批准 UI Construction Contract
Effective UI Contract = Task/Batch execution snapshot
```

- PRD owns Product/Business Truth。
- Business-affecting UI Change 必须回 Product Governance。
- PRD 更新可使 UI_SPEC stale/review。
- Design revision 不自动更新 UI_SPEC。
- Design Version 与 UI_SPEC Version 分开。
- Approved != Current Effective。
- Active Batch 不追 latest。
- New UI → NEWER_UI_AVAILABLE。
- Coverage 可局部。
- Design Acceptance != UI Contract Approval。
- UI_SPEC ready != Implementation Authorization。
- Coding consumes current effective PRD + UI_SPEC + rules + technical context。

---

## F6-D08 — Implementation Guidance / IR / Pack

```text
Implementation Semantic Need
≠ Guidance
≠ IR
≠ Pack
≠ Adapter Output
```

- Guidance = task-specific HOW。
- IR = framework-neutral machine-readable HOW。
- Pack = derived task-scoped construction pack。
- Pack != UI_SPEC。
- Scene/Design/Implementation/Framework 分层。
- Geometry != fixed sizing。
- Parent-driven sizing。
- Layout relationships > screenshot coordinates。
- Absolute 只用于真实 positioning semantics。
- Flex/Grid 是 implementation decision。
- Origin/Reason/Trace 必须保留。
- Behavior/Data/Token 用 refs。
- Semantic Component != Framework Component。
- Existing code/components = reuse evidence。
- Responsive 输出 transformation。
- No invented mobile behavior。
- Alternatives != Deviations。
- Deviation 显式治理。
- Adapter limitation → feasibility issue。
- Implementation revision 与 UI_SPEC revision 分离。
- Compiler 不重新 resolve authority。
- Adapter 只做技术栈翻译。
- No autonomous implementation learning/promotion。

---

## 全局 Architecture Quality Gate

后续定稿必须检查：

```text
Flexibility
Responsibility Clarity
Extensibility
Performance / Scope
Semantic Separation
Low-friction Reliability
Rule Compatibility
Explicit Resolution
Authority Clarity
No Competing Truth
No Silent Override
No AI Guess-Wins
No Premature Learning
No Speculative Complexity
Future Migration Path
```

核心体验：

```text
用户表达意图，Banyan 承担治理成本。
```

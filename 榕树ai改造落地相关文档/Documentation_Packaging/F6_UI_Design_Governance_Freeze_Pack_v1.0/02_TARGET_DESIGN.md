# F6 UI Design Governance — Target Design

## 0. Target

F6 定义 Banyan 的 UI / Design Governance（界面与设计治理）：

> 从多种设计/规则/产品物资进入，到设计证据解释、视觉/状态/数据语义形成、Design Package 与 UI_SPEC 批准、Implementation Guidance / IR / Pack 生成，再到运行结果验证、受治理修复和设计—代码同步的完整架构边界。

F6 的目标不是让用户承担更多流程，而是：

> **规则能自动判断的事情自动完成；真正影响 Authority、Canonical Truth、高风险边界或无法唯一解析的冲突才打扰人。**

---

## 1. End-to-End Architecture

```text
Material / User Intent / PRD / Existing UI / Design Source
                         ↓
                 D01 Material Intake
                         ↓
         Registration / Reconciliation / Routing
                         ↓
            ┌────────────┴────────────┐
            ↓                         ↓
     Product Semantics           Design / Rule Input
          → F5                        ↓
                                 D02 Rules
                              Profile / Index
                              Context Resolution
                                      ↓
                                 D03 Design Source
                              Raw / Normalized Scene
                               Semantic Interpretation
                                      ↓
                             Structured Design Evidence
                                      ↓
          ┌───────────────┬───────────┼───────────────┐
          ↓               ↓           ↓               ↓
         D04             D05         D06          D01 UDC
 Visual/Token/Foundation Behavior  UI Data Semantic User Design Constraint
          └───────────────┴───────────┴───────────────┘
                                      ↓
                                 D07 Design Package
                                      ↓
                              Draft UI Contract
                                      ↓
                                  UI Governance
                                      ↓
                                     UI_SPEC
                                      ↓
                            Effective UI Contract
                                      ↓
                         D08 Implementation Semantic Need
                                      ↓
                            Implementation Guidance
                                      ↓
                              Implementation IR
                                      ↓
                            Implementation Pack
                                      ↓
                              Framework Adapter
                                      ↓
                         React / Vue / Other Runtime
                                      ↓
                               Current Reality
                                      ↓
                            D09 Conformance Validation
                                      ↓
                        Difference / Drift / Regression
                                      ↓
                               Validation Result
                                      ↓
                             D10 Governed Repair
                                      ↓
                            Necessary Revalidation
                                      ↓
                                  D10 CLOSED
```

---

## 2. Core Design Principles

### 2.1 Flexibility

Core freezes stable contracts, not concrete frameworks or hard-coded module trees.

Allowed:

- Module composition；
- Rule composition；
- Profile composition；
- Scope-local overrides；
- Provider replacement；
- Adapter replacement；
- versioned evolution；
- split / merge / supersession；
- project-local rules；
- future extension without Core rewrite。

### 2.2 Clear Responsibility

F6 keeps the following concepts separate:

```text
Fact
Evidence
Rule
Authority
Inference
Context
Effective State
Implementation
Validation Result
Repair Result
```

No downstream result automatically becomes upstream Authority.

### 2.3 Targeted Loading

Default resolution path:

```text
Scope
→ Profile
→ Module Index
→ Rule Association Index
→ Targeted Canonical Read
→ Resolver
→ Minimum Sufficient Context
```

Not:

```text
load all docs
load all rules
load all history
ask human again
```

### 2.4 Governed Automation

```text
Deterministic Work
→ Automatic

Policy-resolvable Work
→ Automatic

Authority Conflict
→ Governance / Human

High-Risk Gate
→ Governance / Human

Canonical Truth Change
→ Existing Change / Decision Governance

Unresolvable Ambiguity
→ Governance / Human
```

Formal:

```text
Governed
!=
Manual Every Time

Automatic
!=
Ungoverned
```

### 2.5 Current AI Learning Boundary

Current F6 does not implement:

- autonomous long-term rule learning；
- autonomous permanent summarization；
- autonomous framework optimization；
- autonomous rule promotion；
- autonomous Authority creation。

Future learning capability may produce Candidate / Recommendation through extension points, but must reuse current Stable ID / Version / Authority / Change / Apply contracts.

---

## 3. D01 — Material Intake and Design Input Governance

### Purpose

D01 makes diverse inputs enter a unified governance path without immediately becoming truth.

Inputs may include:

- PRD / approved change；
- user natural-language design constraints；
- design image / screenshot / Figma / 墨刀 / prototype；
- existing page；
- frontend standard / design guideline；
- historical material；
- current project evidence。

### Contract

```text
Material
→ Register
→ Classify
→ Reconcile
→ Route
```

Outputs route to semantic Owners:

- Product semantic → F5 / PRD；
- User Design Constraint → F6 design input；
- design evidence → D03；
- rule candidate → D02；
- technical/current-code evidence → implementation context；
- unresolved valuable item → Carry-Forward / governance buffer。

Rules:

```text
Material
!=
Authority

Material
!=
Canonical Truth

AI Inference
!=
Human Constraint

UNKNOWN
must remain UNKNOWN
```

Gap / blocker should be localized; one local uncertainty must not freeze unrelated batch scope.

---

## 4. D02 — Rule, Profile, Index and Context Governance

### 4.1 Rule Systems

F6 keeps at least two governed systems separate:

```text
UI Design Rule System
Frontend Development Rule System
```

They may be semantically related, but do not copy rule bodies or create hidden inheritance.

### 4.2 Module / Rule Entry

```text
Rule System
├── Rule Module
│   ├── Rule Entry
│   └── Rule Entry
└── Rule Module
```

Module represents a stable minimum coherent knowledge responsibility boundary.

One Rule Entry != one Module.

Module names are not hard-coded by Core.

### 4.3 Rule Resolution Dimensions

A rule's effect cannot be reduced to a single priority number.

Resolve at least:

```text
Strength
Authority
Scope
Applicability
Version / Freshness
Override Policy
Rule Relation
```

Rule relation may include:

```text
COMPOSE
SPECIALIZE
DEPENDENCY
ALTERNATIVE
OVERRIDE
EXCLUDE
CONFLICT
```

Unknown relation:

```text
UNRESOLVED_RELATION
→ Autonomy NOT ELIGIBLE
```

### 4.4 Profile

Profile declares project/task adoption and bindings.

Profile:

- references Modules / Rule Sets；
- limits Scope / applicability；
- may reference legitimate override；
- does not copy canonical rule body；
- does not create new priority by ordering；
- does not silently auto-upgrade to latest shared version。

### 4.5 Index

```text
Index Match
!=
Rule Applicability
!=
Rule Effectiveness
```

Index finds candidates.

Resolver decides current applicability/effectiveness.

Index miss:

```text
INDEX_MISS
!=
RULE_NOT_EXIST
```

### 4.6 Context

F6 defines two separate contexts:

```text
Effective Design Context
Effective Implementation Context
```

They are:

```text
Derived
Rebuildable
Task-scoped
Minimum Sufficient
```

They are not new Product / UI / Rule truth.

Compiler assembles resolved inputs; Compiler must not recreate Authority/priority logic.

---

## 5. D03 — Design Evidence Interpretation

### Layers

```text
Design Material
→ Design Source Registration
→ Provider Interpretation
→ Raw Scene
→ Normalized Scene
→ Semantic Tree
→ Structured Design Evidence
→ Design Truth contribution
```

Not all tasks require every Scene layer.

Provider may be:

- image parser；
- Figma adapter；
- 墨刀 adapter；
- browser/runtime adapter；
- future provider。

Core consumes normalized contracts, not provider-specific structures.

Formal:

```text
Design Source
!=
Design Truth

Provider Output
!=
Design Authority

Existing UI
!=
Design Truth
```

Evidence must preserve source, provenance, freshness, confidence and unknowns.

---

## 6. D04 — Visual Property, Token and Shared Foundation

A measured property is not automatically a token.

```text
Observed Color / Radius / Spacing
→ Visual Property Evidence
→ semantic reconciliation
→ Governed Token candidate
→ approved token within Scope
```

Tokenization requires stable design meaning + governed reuse value + explicit Scope.

Shared Foundation:

- owns shared design WHAT；
- may include shared tokens / typography / visual semantics / common design basis；
- is not CSS；
- is not Ant Design Theme config；
- is not a framework runtime object。

Scope may be:

```text
Page
Application
Product Area
Project Shared
```

Core does not require one global token namespace.

---

## 7. D05 — Behavior, State and Interaction

Formal separation:

```text
State Evidence
State Definition
Interaction Evidence
Interaction Definition
Transition / Motion
Behavior Model
Product Business Logic
```

Static image can prove a visible state but not its business entry condition.

Button can prove interaction affordance but not automatically:

```text
click → submitOrder()
```

Behavior Model may reference Product semantics, but does not create business capability or business state meaning.

---

## 8. D06 — UI Data Semantics and Fixture

Design examples:

```text
¥39.90
上传中 72%
brand.png
张三
```

default to Evidence / Fixture unless authoritative product/data evidence says otherwise.

F6 models:

```text
Data Evidence
→ UI Slot / UI Field Semantic
→ Binding Requirement
→ Upstream Source Reconciliation
→ UI Data Binding Model
→ Deterministic Fixture
```

Formal:

```text
UI Data Semantic
!=
Business Data Truth

Fixture
!=
Production Data

Design Example Value
!=
Required Business Value
```

---

## 9. D07 — Design Package and UI Contract

### 9.1 Design Package

Design Package is the concrete design target package for a page/region/component/task.

It can reference:

- structure/layout design；
- visual properties；
- Shared Foundation；
- tokens；
- state/interaction model；
- UI data semantics；
- User Design Constraints；
- evidence/provenance；
- unknown/conflict/deviation。

### 9.2 UI_SPEC

UI_SPEC is the approved UI construction contract.

```text
Design Package
→ Draft UI Contract
→ Governance / Approval
→ UI_SPEC
```

Formal:

```text
Design Package
!=
UI_SPEC

PRD
!=
UI_SPEC
```

PRD owns Product WHAT.

UI_SPEC owns approved UI WHAT.

### 9.3 Effective UI Contract

Task/Batch resolves a current effective UI snapshot.

```text
Latest
!=
Current Effective

Approved
!=
Current Effective
```

New design evidence does not silently replace a bound Effective UI Contract.

---

## 10. D08 — Implementation Guidance, IR and Pack

Implementation begins from semantic need, not raw screenshot geometry.

```text
Effective UI Contract
+ Effective Frontend Rules
+ Technical Context
+ Current Code Evidence
↓
Implementation Semantic Need
↓
Implementation Guidance
↓
Implementation IR
↓
Implementation Pack
↓
Framework Adapter
```

Formal:

```text
UI_SPEC owns WHAT
Implementation owns HOW

Geometry
!=
CSS

Implementation Guidance
!=
UI Truth

Implementation Pack
!=
UI_SPEC

Framework Adapter
!=
Design Authority
```

Examples:

- fixed measured x/y does not automatically imply `position:absolute`；
- repeated cards may be implemented with Grid/Flex when semantics allow；
- width/height may be intrinsic/responsive rather than fixed when the contract does not require fixed geometry；
- AntD / Element Plus APIs belong to adapters/technical rules, not Core IR.

---

## 11. D09 — UI Conformance Validation

### 11.1 Session Boundary

Full UI conformance session is explicit and bounded.

Its explicit trigger is a specialized D09 gate, not a global Banyan automation requirement.

### 11.2 Target

Default applicable target:

```text
Current Effective UI Contract
```

Potential status:

```text
CURRENT
STALE
REVIEW_REQUIRED
SUPERSEDED
CONFLICTED
UNKNOWN
```

Formal:

```text
Latest
!=
Current Effective

Existing Reality
!=
Design Truth
```

### 11.3 Scope / Evidence / Coverage

Scope may be composed from:

```text
Application
Page
Region
Component
State
Interaction
Viewport / Device
Data Scenario
```

Formal:

```text
Explicit Scope
>
AI Inferred Scope

Unobserved
!=
PASS

Partial PASS
!=
Whole Scope PASS
```

### 11.4 Difference / Drift

```text
Difference
=
Target != Actual
```

But:

```text
Difference
!=
Drift
```

Classifications may include visual / structural / layout / state / interaction / responsive / data-presentation / accessibility.

Keep distinct:

```text
LEGAL_ALTERNATIVE
EXPECTED_VARIATION
APPROVED_DEVIATION
ACCEPTABLE_DIFFERENCE
DRIFT
```

### 11.5 Regression

Protected Functional Baseline can include:

- API integration；
- routing；
- permission；
- business logic/state；
- data contract；
- persistence；
- upload/delete/pagination/query；
- accepted interactions。

Regression Scope:

```text
Impact-driven
Minimum Sufficient
```

Not always full regression, and not only changed DOM.

### 11.6 Result

Validation Result is structured Evidence.

```text
Validation Result
!=
UI_SPEC
!=
Design Package
!=
PRD
```

D09 ends:

```text
Final Report
→ SESSION CLOSED
```

D09 does not grant repair permission.

---

## 12. D10 — Governed Correction and Repair

### 12.1 Authority

D09 finding only makes an Issue eligible for D10 review.

```text
Eligible
!=
Authorized
```

Authorization may come from applicable:

```text
Explicit Human Authorization
OR
Pre-Approved Repair Policy
```

but Policy cannot be inferred by AI.

Authorization must be bounded by Issue / Scope / Mutation Target / Allowed Action / Exclusions / Validity / Context.

### 12.2 Scope

```text
Requested Repair Scope
Authorized Mutation Scope
Effective Mutation Scope
```

Formal:

```text
Requested Scope
!=
Authorized Scope

Effective Mutation Scope
⊆
Authorized Mutation Scope

Not Explicitly Forbidden
!=
Authorized

Impact Scope
!=
Authorized Mutation Scope

Necessary
!=
Authorized
```

### 12.3 Repair Plan

Repair follows Minimum Sufficient Repair.

No:

- opportunistic refactor；
- unrelated cleanup；
- broad unrequested normalization；
- changing Design Truth just because code is easier to keep。

### 12.4 Mutation

Mutation requires:

```text
Valid Authorization
+
Valid Effective Mutation Scope
+
Valid Repair Plan
```

Auto Repair is policy/authority driven:

```text
Low Risk
!=
Auto Repair Permission
```

### 12.5 Revalidation

After repair:

```text
Repair Objective
+
Required Regression Checks
→ Repair Success
```

D10 revalidation is local/impact-driven and does not automatically reopen D09.

### 12.6 Retry

Automatic retry must have finite Retry Budget and stop conditions.

```text
Retry Allowed
!=
Retry Until Success
```

### 12.7 Escalation

Escalation:

```text
→ SUSPENDED
```

After governance resolution, Resolver determines:

```text
RESUME_ALLOWED
or
FORK_NEW_REPAIR_INSTANCE
```

Material authority/scope/target/objective change requires a new execution instance with lineage.

### 12.8 Effective State and Authority

Do not model `Implementation = AUTHORIZED / NOT_AUTHORIZED` as permanent manually edited Core truth.

Resolve:

```text
Authority Fact
+
Rule
+
Context
+
Gate
+
Profile
+
Revision
↓
Resolver
↓
Effective State
```

Formal:

```text
Effective State
!=
Authority Fact

State Derivation
!=
Authority Creation

AI May Derive State
!=
AI May Invent Authority
```

---

## 13. Formal Owner Matrix

| Owner | Responsibility |
|---|---|
| D01 | Material Intake / Registration / Reconciliation / Routing |
| D02 | Rules / Modules / Profiles / Index semantics / Resolution / Effective Context contracts |
| D03 | Design Source / Scene / Semantic Design Evidence |
| D04 | Visual Property / Token / Shared Foundation |
| D05 | UI State / Interaction / Behavior |
| D06 | UI Data Semantic / Fixture |
| D07 | Design Package / UI_SPEC / Effective UI Contract |
| D08 | Implementation Guidance / IR / Pack |
| D09 | Target/Actual Validation / Difference / Drift / Regression / Report |
| D10 | Repair Authorization / Mutation / Revalidation / Closure |

Formal:

```text
Earlier Broad Reference
!=
Later Specialized Authority
```

---

## 14. Current Effective / Derived / Canonical Model

```text
Canonical / Governed Source
        ↓
Profile / Binding
        ↓
Index Discovery
        ↓
Resolver
        ↓
Effective Rule Set / Effective Context / Effective State
        ↓
Task Execution / Validation
```

Rules:

```text
Index
= find

Resolver
= resolve

Compiler
= assemble

Effective View
= current derived result

Canonical Source
= authoritative meaning
```

Derived objects do not become canonical because they are frequently consumed.

---

## 15. Stage Boundary

F6 freezes architecture semantics for UI Design Governance.

F6 intentionally does not freeze:

- exact physical directory；
- exact YAML / JSON schema；
- exact field names / enums；
- SQLite DDL / index；
- vector/embedding implementation；
- exact provider SDK；
- exact framework adapter API；
- exact CLI / WebUI；
- exact migration / rollback algorithm；
- actual project source-code changes；
- AI Learning implementation。

Those belong to Implementation Freeze or F7～F12 owner stages.

---

## 16. Final Architecture Statement

F6 final architecture can be summarized as:

> **Banyan 将各种设计、规则、产品与现有实现材料先作为可追踪输入，通过 Scope / Profile / Index 精准解析，严格区分 Evidence、Rule、Authority、Inference、Effective State 和 Implementation；Design Source 经可替换 Provider 解释形成结构化设计证据，视觉、交互、数据语义分别治理后汇入 Design Package，经 UI Governance 形成 UI_SPEC 与 Current Effective UI Contract；实现层只负责 HOW，通过框架无关 IR 与 Adapter 落地；D09 只验证，D10 只在有效 Authority 和 Scope 下受治理修复。确定性工作自动完成，真正 Authority 冲突、高风险 Gate 或 Canonical Truth 变化才升级人工治理。当前不实现 AI 自主学习，只保留不推翻 Core 的扩展边界。**

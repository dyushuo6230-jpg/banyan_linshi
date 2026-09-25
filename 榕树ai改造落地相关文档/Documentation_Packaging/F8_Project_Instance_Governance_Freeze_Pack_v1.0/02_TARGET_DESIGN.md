# F8 Project Instance Governance — Target Design

## 0. Target

F8 定义 Banyan 的 Project Instance 架构：

> 一个项目如何被稳定识别、映射到真实 Source、组合 Profile、绑定 Provider、约束 Version、解析 Feature / Gate、接入 Existing / New Project、跟随项目现实变化，并向 Runtime 输出当前任务所需的最小充分 Project Context。

目标不是建立一个万能“项目配置中心”，而是：

```text
Stable Identity
+
Explicit Bindings
+
Scoped Effective Resolution
+
Targeted Reconciliation
+
Clear Owner Boundaries
```

同时满足：

> **可靠自动路由 × 最小人工决策治理**

---

## 1. End-to-End Architecture

```text
Project / Intent / Existing Reality
              ↓
           F8-D01
Project Identity / Project Instance Boundary
              ↓
           F8-D02
Source Role / Mapping / Location Binding
              ↓
           F8-D03
Profile Instance / Overlay / Project Fact Resolution
              ↓
           F8-D04
Provider Binding / Eligibility / Selection / Fallback
              ↓
           F8-D05
Version Pin / Compatibility / Effective Version
              ↓
           F8-D06
Feature Activation / Gate / Effective Instance State
              ↓
           F8-D07
Existing Adoption / New Initialization
              ↓
           F8-D08
Observation / Drift / Reconciliation / Refresh
              ↓
           F8-D09
Project Instance Evolution Boundary
              ↓
           F8-D10
Task-scoped Runtime Handoff
              ↓
              F10
Runtime Permission / Execution
```

该图表示职责依赖，不表示固定 Runtime Call Order。

---

## 2. Core Semantic Separations

```text
Project Identity
!= Project Instance

Project Instance
!= .banyan Directory

Source Role
!= Path / Location

Mapping
!= Canonical Truth

Binding
!= Effective Binding

Profile Definition
!= Project Profile Instance

Project Profile Instance
!= Authority

Overlay
!= Authority Override

Project Fact
!= Product / Design / Engineering Truth

Capability
!= Provider

Provider Binding
!= Runtime Permission

Health
!= Capability

Fallback
!= Retry

Stable Identity
!= Version

Version
!= Revision

Version Pin
!= Effective Version

Latest
!= Current Effective

Feature Definition
!= Feature Activation Binding

Feature Activation Binding
!= Effective Feature Activation

Gate Definition
!= Gate Result

Gate PASS
!= Authority

Observation
!= Canonical Project Instance Truth

Drift
!= Conflict
!= Error
!= Change Case

Refresh
!= Canonical Rewrite

Shadow / Pilot
!= Mandatory Lifecycle

Pilot Success
!= Final Activation

Runtime Handoff
!= Canonical Truth Copy

Runtime ALLOW
!= Project Instance Semantic Decision
```

---

## 3. Project Identity / Project Instance Model

Project Identity 表达“这个项目是谁”。

Project Instance 表达“这个项目当前如何使用 Banyan”。

Project Instance 可以承载或引用：

```text
project identity
source mappings
location bindings
profile instance
project overlays
project facts
provider bindings
version pins
feature activation bindings
runtime/index/trace/generated locations
migration lineage references
```

但 Project Instance 不吞并：

```text
Product Truth
Design Truth
Engineering Standards Truth
Decision Authority
Apply Authorization
Runtime Permission
Legacy Retirement Authority
```

---

## 4. Binding Model

Binding 是 F8 的核心结构之一，但不同领域的 Binding 仍由各自 Owner 管理。

```text
Source Binding
Profile Binding
Provider Binding
Version Pin / Binding Constraint
Feature Activation Binding
```

Binding 应保持：

```text
stable identity
scope awareness
authority/reference separation
version/freshness applicability
explicit conflict handling
traceable lineage
```

Binding 变化不自动创造新的 Project Instance Identity。

Durable protected mutation 进入 F7。

---

## 5. Effective Resolution

F8 不把所有状态写成静态 bool。

Effective Result 应由必要的：

```text
Canonical Facts
Bindings
Profile
Scope
Context
Authority
Applicability
Version / Compatibility
Boundary
Gate
Freshness Evidence
```

解析得到。

正式：

```text
Definition / Binding
!= Effective Result

State Derivation
!= Authority Creation
```

同一 Semantic Fact + 同一 Applicable Scope 应唯一解析到一个 Current Effective Result。

---

## 6. Existing / New Project

### Existing Project
默认：

```text
PRESERVE_IN_PLACE
```

Banyan 适应项目，而不是强迫项目搬家。

```text
Inspect minimum sufficient reality
→ Resolve Project Identity
→ Build Source Mapping
→ Bind Profile / Provider / Version / Feature
→ Preserve UNKNOWN
→ Form Project Instance
```

### New Project
可由 Banyan 建立 Project Identity / Project Instance，并提供可选推荐模板，但：

```text
Recommended Template
!= Mandatory Layout
```

Existing / New 最终进入同一 Project Instance semantic model。

---

## 7. Reconciliation Model

项目可以自然变化。

F8-D08 负责：

```text
Observe
→ Compare
→ Classify
→ Resolve owner
→ Reconcile
→ Refresh derived state
```

但：

```text
Observation
!= Truth

Drift Detection
!= Mutation Authorization

Refresh
!= Canonical Rewrite
```

确定性 reconciliation 自动完成。

只有真正无法由 Rule / Boundary / Authority / Evidence 唯一解决的 Judgment Gap 才进入 Human Decision。

---

## 8. Evolution Model

Project Instance 建立后持续演进。

D09 不建立第二套 Revision / History / Apply 系统。

```text
Project Instance Fact evolution
→ domain owner resolves semantics
→ F7 owns durable governed mutation
```

Shadow / Pilot 只在风险和验证需求需要时使用。

```text
simple deterministic change
→ shortest governed path

complex / high-impact change
→ optional Shadow / Pilot
```

---

## 9. Runtime Handoff Model

F8 向 F10 交付：

```text
Task / Action Scoped
Minimum Sufficient
Derived
Rebuildable
Project Instance Resolution Result
```

可能包含：

```text
Project ref
Scope
Effective Bindings
Applicable Profile
Effective Provider
Effective Version
Feature / Gate state
Boundary refs
Authority / Evidence refs
UNKNOWN / BLOCKED
```

但：

```text
Runtime Handoff
!= second Project Instance truth
```

Runtime 发现 stale / mismatch 时：

```text
F10 detects
→ evidence / re-resolution
→ D08 / F9 / domain owner
→ F7 if durable mutation required
→ new context
→ F10 resumes
```

---

## 10. Performance Model

F8 默认采用：

```text
Task
→ Scope
→ Profile
→ Index
→ Minimum Sufficient Context
→ Targeted Canonical Read
```

不默认：

```text
full project scan
full rule load
full context replay
repeated user confirmation
```

Dynamic Scope 是解析与性能能力，不是 Project Identity、Authority 或 Canonical Truth。

---

## 11. Final Owner Architecture

```text
D01 Identity
D02 Source / Location
D03 Profile / Project Fact
D04 Provider
D05 Version
D06 Feature / Gate / Effective State
D07 Adoption / Initialization
D08 Reality Reconciliation
D09 Project Instance Evolution Boundary
D10 Runtime Handoff / Stage Closeout

F7 Revision / History / Canonical Apply
F9 Index / Search / Freshness / Impact
F10 Runtime Permission / Execution
F11 Control Plane UX
F12 Legacy Migration / Retirement
```

---

## 12. Stage17 Compatibility

Current `.banyan`：

```text
PILOT_SHADOW
SHADOW_VALIDATED
final_activation = false
canonical_replacement = false
canonical_write = BLOCKED
```

因此 F8 Target Design 不把现有 Pilot 自动提升为正式 Canonical Replacement。

---

## 13. Global Design Requirements

F8 最终架构满足：

```text
Flexible
- no forced project layout
- no mandatory Shadow/Pilot lifecycle

Structured
- owner / object / state / truth / authority boundaries explicit

Extensible
- source endpoint, provider, version model, feature types remain extensible

Fast
- Scope / Profile / Index targeted resolution

Logical
- facts / rules / implementation / evidence / authority / state separated

Convenient but reliable
- deterministic work auto
- only genuine judgment gaps interrupt humans

Compatible and unambiguous
- final owner map explicit
- stale future-owner references closed by F8-FREEZE-CLOSURE-01

No premature AI Learning complexity
- no self-learning / self-policy-promotion system introduced
```

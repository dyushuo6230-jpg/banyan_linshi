# F8 Project Instance Governance — Final Reconciliation

## 0. Pack Identity

- Pack: `F8_Project_Instance_Governance_Freeze_Pack_v1.0`
- Stage: `F8 — Project Instance / Binding / Profile Instance / Provider Selection / Version Pin / Project Reconciliation`
- Status: `ARCHITECTURE_FREEZE_PASS`
- Stage Closure: `PASS`
- Frozen decisions:
  - `F8-PRE-VAR-01`
  - `F8-D01` ～ `F8-D10`
  - `F8-FREEZE-CLOSURE-01`
- Cross-stage dependencies:
  - `CROSS-STAGE-BOUNDARY-01`
  - `CROSS-STAGE-GOVERNANCE-02`
  - `CROSS-STAGE-DECISION-02`
- Pack grants Implementation Authority: `false`
- Pack grants RP2 Authority: `false`
- Pack grants Authority Cutover: `false`
- Pack grants Final Activation Authority: `false`
- Pack grants Canonical Replacement Authority: `false`
- Pack grants Legacy Retirement Authority: `false`

> 本 Pack 是 F8 的最终 Architecture Freeze（架构冻结）阶段包。
> 它定义 Project Instance 层的最终架构合同、Owner 边界、跨阶段交接和收口结果。
> 它不是 Implementation Freeze，也不因为自身存在而授权真实项目写入、Final Activation、Canonical Replacement 或 Legacy Retirement。

---

## 1. F8 为什么存在

F8 解决 Banyan 中“当前项目如何被框架稳定、准确、可扩展地理解和使用”的问题。

核心链路：

```text
Project Identity
→ Project Instance
→ Source / Location Binding
→ Project Profile / Project Facts
→ Provider Binding / Selection
→ Version Pin / Compatibility
→ Feature Activation / Gate / Effective State
→ Existing / New Project Adoption
→ Reality Observation / Drift / Reconciliation
→ Project Instance Evolution
→ Runtime Handoff
```

F8 不把项目强制改造成 Banyan 的固定目录结构，也不把所有项目事实塞进一个万能变量文件。

F8 的目标是：

> **可靠自动路由 × 最小人工决策治理**

Banyan 应优先自己判断：

```text
这是什么？
属于哪个 Project / Project Instance？
Source 在哪里？
适用什么 Profile？
应该使用哪个 Provider？
哪个 Version 当前有效？
哪些 Feature / Gate 生效？
项目现实是否发生 Drift？
是否需要重新解析？
是否真的需要 Human Decision？
```

---

## 2. Four-Source Reconciliation

F8 使用四类源进行对账：

### A. Old Human Discussions
恢复长期确认的使用体验与治理要求，例如：

- Existing Project 默认 `PRESERVE_IN_PLACE`；
- 不强制统一业务目录；
- 项目事实、产品事实、设计事实、实现现实不能混为一体；
- 确定性工作尽量自动完成；
- 只有真正判断缺口才占用人的注意力。

### B. Legacy v3.1
通过 `F8-PRE-VAR-01` 对 44 个项目变量进行逐项无损对账。

结果：

```text
Legacy Variables = 44
Mapped = 44
Unmapped = 0
Silently Dropped = 0
Competing Writable Truth Introduced = 0
Legacy Bool Authority Bypass Allowed = 0
Critical UNKNOWN Silent Default Allowed = 0
Deprecated Without Rationale = 0
```

### C. Accepted Refactor / Historical Stage Evidence
重点继承：

- Historical Stage 04 Project Instance / Source Mapping / Profile；
- Stage17 `.banyan` Pilot / Shadow 事实；
- Runtime / Index / Trace / Generated / Migration 位置与语义分离；
- single writable truth；
- Preserve-in-Place；
- no forced relayout；
- Pilot success does not equal Final Activation。

### D. Current Implementation Reality
当前代码、`.banyan` Pilot、Provider loader、Runtime status 等只作为 Implementation Reality / Evidence。

正式：

```text
Current Implementation Reality
!= Final Architecture Authority
```

---

## 3. Approved F8 Decision Set

### F8-PRE-VAR-01 — Legacy v3.1 Project Variables No-Loss Reconciliation
冻结：

- 44/44 Legacy 项目变量全部有明确去向；
- 允许 RETAIN / STRUCTURALIZED / MOVED_TO_OWNER / DERIVED / SUPERSEDED / DEPRECATED；
- 不允许 Silent Drop；
- 不允许旧 bool 绕过 Authority / Boundary / Gate / Apply Authorization / Runtime Permission；
- 不允许重新建立“大一统 variables.yaml”；
- Domain Semantic Variables 必须交给真实 Owner。

### F8-D01 — Project Identity × Project Instance × Instance Boundary
冻结：

- `Project Identity != Project Instance`；
- stable identity 不等于项目名、路径、Git、Provider 或 Editor；
- Project Instance 是项目如何使用 Banyan 的受治理结构，不是 Product / Design / Code / Requirement Truth；
- Project Instance 逻辑对象不等于 `.banyan` 目录；
- Effective Project Instance 是派生结果，不是简单 `enabled=true`；
- Critical UNKNOWN 不得静默默认；
- Existing Project 接入默认 Preserve-in-Place；
- `.banyan` 存在不等于 Final Activation。

### F8-D02 — Project Source Mapping × Canonical Binding × Location Binding
冻结：

- `Source Role != Path / File / URL / Endpoint`；
- Role 与 Binding / Mapping / Location 分离；
- 一个 Role 可有 0..N Binding；
- 多 Source 不等于多 Truth；
- `Binding != Effective Binding`；
- 多个竞争 Canonical 候选未解析时必须阻断，不使用 Last/Latest Wins；
- writable/capability 不等于 Apply Authorization；
- `Mapping Miss != Source Absent`；
- Protected Binding durable mutation → F7；
- Source Endpoint 保持可扩展，不限文件路径。

### F8-D03 — Project Profile Instance × Overlay × Project Fact × Variable Resolution
冻结：

- `Profile Definition != Project Profile Instance`；
- Project Profile Instance 不是 Authority，也不是 Domain Truth；
- Profile 采用 reference/composition，不复制 canonical rule body；
- ordering 不等于 priority；
- Overlay 只表达项目差异，不是 Authority Override；
- Project Fact 只承载项目级事实，不吞 Product / Design / Engineering Truth；
- Detected Reality 不等于 Architecture Decision；
- Critical UNKNOWN 不得静默默认；
- Contributor/Git identity 不等于 Authentication / Permission / Authority。

### F8-D04 — Provider Selection × Provider Binding × Capability × Health × Fallback
冻结：

- `Capability != Provider`；
- `Provider != Skill`；
- Core 不硬编码商业 Provider / Model / Editor；
- Provider Binding 绑定 Project Instance + Port/Capability Requirement + Scope + Provider Ref；
- capability declaration 只是 Evidence，不自动形成 Eligibility；
- Health 与 Capability 分离；
- Fallback 必须预治理且语义兼容；
- Retry != Fallback；
- temporary runtime reselection 不等于 durable rebinding；
- Selected Provider 不获得 Product / Design / Apply / Runtime Authority；
- Configuration/Credential 不等于 Authority。

### F8-D05 — Version Pin × Compatibility × Effective Version Resolution
冻结：

- `Stable Identity != Version`；
- `Version != Revision`；
- Version Pin 是 scope-aware Binding Constraint；
- `Latest != Current Effective`；
- Compatibility 是多维的，Technical Compatibility 不等于 Semantic Compatibility；
- Upgrade Policy 必须显式；
- 已治理、兼容且唯一可解的升级可以自动；
- durable Pin change → F7；
- `Compatible != Authorized`；
- `Pin != Feature Activation`；
- Installed Version 不等于 Version Authority。

### F8-D06 — Feature Activation × Effective Instance State × Gate Resolution
冻结：

- `Feature Definition != Feature Activation Binding`；
- `Feature Activation Binding != Effective Feature Activation`；
- Activation 不退化为全局 bool；
- Critical UNKNOWN 不得静默激活；
- Capability / Provider Availability / Invocation / Runtime Permission / Authority / Apply Authorization 分离；
- Dependency 不自动等于 activation；
- Gate Definition != Gate Result；
- Gate PASS 不授予 Authority；
- `PILOT_CONNECTED != FINAL_ACTIVATED`；
- `SHADOW_VALIDATED != FINAL_ACTIVATED`；
- `Instance Active != Canonical Replacement`；
- Validation PASS 不自动 Final Activate；
- Effective State 是 derived / rebuildable，不是第二可写真源。

### F8-D07 — Existing Project Adoption × New Project Initialization × Preserve-in-Place
冻结：

- `Existing Adoption != New Initialization`；
- Existing Project 默认 `PRESERVE_IN_PLACE`；
- Project Layout != Project Identity；
- multi-root 合法；
- Adoption != Relayout / Migration / Authority Creation；
- Minimum Sufficient Discovery，非默认全项目扫描；
- Adoption 可在显式 UNKNOWN 下渐进进行；
- New Project 可用推荐模板，但模板不是唯一合法布局；
- Existing / New 最终进入同一 Project Instance semantic model；
- `.banyan-refactor Exists != Canonical Project Instance`；
- `.banyan Exists != Final Activation`；
- Project Source Relayout != Instance Cutover；
- Copy / Shadow != Canonical Truth。

### F8-D08 — Project Reconciliation × Binding Drift × Instance Refresh
冻结：

- F8 Project Reconcile != F7 Change Reconcile != F12 Legacy Reconcile；
- Current Observation != Canonical Project Instance Truth；
- Difference != Material Drift；
- Drift != Conflict != Error != Change Case；
- `Stale != Drift`；
- `Mapping Miss != Source Deleted`；
- `Path Change != Source Identity Change`；
- `Drift Detected != Human Decision Required`；
- `Detection != Mutation Authorization`；
- `Refresh != Canonical Rewrite`；
- local drift 不导致 global invalidation；
- D08 消费 F9 Freshness / Impact Evidence；
- Deterministic reconciliation 自动完成；
- Reconciliation PASS != Final Activation。

### F8-D09 — Project Instance Evolution × Optional Validation × Effective Result Boundary
最终冻结（精简版）：

- ordinary Project Instance change 不自动创造新的 Project Instance Identity；
- Project Instance 内部 Stable ID / Revision / History / Supersession / Canonical Apply 统一复用 F7；
- Shadow / Pilot 是可选验证方式，不是固定生命周期；
- 同一 Semantic Fact + 同一 Applicable Scope → 唯一 Current Effective Result；
- `Latest / Validation PASS / AI Recommendation / Model Confidence / Pilot Success != Current Effective`；
- D09 不覆盖 D02～D06 领域语义；
- Reality Reconciliation → D08；
- Index / Freshness / Impact → F9；
- Runtime Permission / Execution → F10；
- Legacy Migration / Retirement → F12；
- Stage17 `.banyan` 仍是 `PILOT_SHADOW / SHADOW_VALIDATED`；
- D09 approval 不授予 Final Activation / Canonical Replacement / Legacy Retirement。

### F8-D10 — Project Instance Runtime Handoff × Stage Closeout Boundary
最终冻结（精简版）：

- Runtime Handoff 提供 Task/Action scoped、Minimum Sufficient、Derived、Rebuildable 的 Project Instance Context；
- `Runtime Handoff != Canonical Truth Copy`；
- Runtime Observation / Result / ALLOW 不创造 Project Instance Truth / Binding Authority / Semantic Decision；
- Runtime Context stale 时回到对应 Owner 重新解析，而不是 Runtime Guess；
- Rebinding 不作为独立 Governance Domain；
- History / Revision / Supersession / Canonical Apply → F7；
- Index / Search / Freshness / Impact → F9；
- Runtime Permission / Execution → F10；
- Control Plane UX → F11；
- Legacy Migration / Retirement → F12；
- D10 不创建 Runtime Handoff Registry / Rebinding Registry / Project Instance History Registry 等新 Core 对象。

### F8-FREEZE-CLOSURE-01 — Final Owner Remap × Stale Reference Supersession
冻结：

- D01 / D06 / D07 / D08 中早期对未来 D09 / D10 的 Owner 预告保留为历史原文；
- 旧 `D09 = Canonical Cutover Owner` 标签失效；
- 旧 `D10 = Project History / Rebinding Owner` 标签失效；
- 最终：
  - D09 = Project Instance Evolution Boundary；
  - D10 = Runtime Handoff + F8 Stage Closeout；
  - History / Revision / Supersession / Canonical Apply → F7；
  - Runtime Permission / Execution → F10；
  - Legacy Migration / Retirement → F12；
- Closure 只纠正旧 Future-Owner Reference，不重开 D01～D08 主体语义。

---

## 4. Final Owner Map

```text
Project / Project Instance Identity
→ F8-D01

Source Mapping / Location Binding
→ F8-D02

Profile Instance / Overlay / Project Fact
→ F8-D03

Provider Selection / Provider Binding
→ F8-D04

Version Pin / Compatibility / Effective Version
→ F8-D05

Feature Activation / Gate / General Effective State
→ F8-D06

Existing / New Project Adoption
→ F8-D07

Reality Observation / Drift / Project Reconciliation
→ F8-D08

Project Instance Evolution Boundary
→ F8-D09

Runtime Handoff / F8 Stage Closeout
→ F8-D10

Stable ID / Revision / History / Supersession / Canonical Apply
→ F7

Index / Search / Freshness / Impact Evidence
→ F9

Runtime Permission / Provider Runtime / Actual Execution
→ F10

Control Plane UX / Governance Interaction
→ F11

Legacy Reconciliation / Migration / Retirement
→ F12
```

---

## 5. Cross-Stage Governance Compatibility

F8 与跨阶段冻结保持一致：

### Boundary
```text
Boundary != Permission
Boundary != Canonical Truth
Boundary != Runtime Authorization
State Derivation != Authority Creation
```

### Reliable Routing
```text
Change != Human Decision Required
Candidate != Human Decision Required
Risk Detected != Human Decision Required
AI Uncertainty != Ask Human Immediately
```

### Informed Decision
已有治理可唯一 ALLOW / BLOCK / ROUTE / DEFER / AUTO 时不拉起完整 Human Decision。
只有真实 Judgment Gap、Authority-sensitive unresolved choice、正式 Boundary change 等才进入 Human Governance。

---

## 6. Current Stage17 Reality Reconciliation

当前 `.banyan` 仍保持：

```text
mode = PILOT_SHADOW
status = SHADOW_VALIDATED
final_activation = false
formal_migration_complete = false
canonical_replacement = false
canonical_write = BLOCKED
protected_business_write = BLOCKED
```

正式：

```text
Pilot Success
!= Final Activation

.banyan Exists
!= Canonical Replacement

F8 Architecture Freeze PASS
!= Runtime Activation
```

`.banyan-refactor` 被视为 Refactor / Bootstrap / Construction / Historical Evidence，不是与 `.banyan` 竞争的第二个 Canonical Project Instance。

---

## 7. Final No-Loss / Conflict Audit

```text
Unmapped Legacy Variable = 0
Silently Dropped Legacy Variable = 0
Competing Writable Truth = 0
Duplicate Project Instance Authority = 0
Duplicate Revision Governance = 0
Duplicate Rebinding Governance = 0
Runtime Permission Promoted To Semantic Authority = 0
Index Promoted To Canonical Truth = 0
Evidence Promoted To Authority = 0
Critical UNKNOWN Silent Default = 0
Implicit Last/Latest Winner Path = 0
Blocking F8 Architecture Conflict = 0
Owner Ambiguity = 0
Cross-stage Boundary Leakage = 0
Implementation Leakage = 0
Final Activation Leakage = 0
```

---

## 8. Final Stage Result

```text
F8 Architecture Freeze = PASS
```

但：

```text
Implementation = NOT AUTHORIZED
RP2 = NOT AUTHORIZED
Authority Cutover = NOT AUTHORIZED
Final Activation = NOT AUTHORIZED
Canonical Replacement = NOT AUTHORIZED
Legacy Retirement = NOT AUTHORIZED
```

F8 到此完成 Architecture Freeze，并向 F9 提供稳定上游。

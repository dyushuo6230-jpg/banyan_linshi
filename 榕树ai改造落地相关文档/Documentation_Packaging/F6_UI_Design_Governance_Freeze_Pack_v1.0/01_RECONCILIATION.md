# F6 UI Design Governance — Final Reconciliation

## 0. Pack Identity

- Pack: `F6_UI_Design_Governance_Freeze_Pack_v1.0`
- Stage: `F6 — UI_SPEC / Design Truth / Visual Governance`
- Status: `ARCHITECTURE_FREEZE_PASS`
- Stage Closure: `PASS`
- Human Decisions: `F6-D01～D10` + `F6-STAGE-C01～C06` = `HUMAN_APPROVED`
- Pack grants Implementation Authority: `false`
- Pack grants RP2 Authority: `false`
- Pack grants Final Activation Authority: `false`

> 本文件是 F6 最终 Reconciliation（对账）、No-Loss（无损）、Conflict/Gap（冲突/缺口）与 Cross-Stage Obligation（跨阶段义务）的阶段冻结记录。  
> 它是 Architecture Freeze（架构冻结），不是 Implementation Freeze（实现冻结），也不因为自身存在而产生真实项目修改权限。

---

## 1. F6 为什么存在

F6 的目的不是重新设计一个独立 UI 工具，而是补齐 Banyan 既有设计/前端链中的长期漏洞，使以下概念不再混在一起：

```text
Design Source
Design Evidence
Design Truth
Design Package
UI_SPEC
Effective UI Contract
Implementation Guidance
Implementation IR
Implementation Pack
Current Implementation Reality
Validation Result
Repair Result
```

F6 重点解决历史上容易出现的问题：

- 设计图 / 截图 / Figma / 墨刀 / AnyDesign 输出被直接当作正式 UI 真相；
- 设计测量值被机械翻译成固定 CSS；
- Design Package、UI_SPEC、Implementation Pack 职责混淆；
- UI 示例数据被误当业务数据；
- 静态图被 AI 脑补成交互或业务状态；
- Rule / Profile / Index / Context 全量加载，导致上下文膨胀和规则误判；
- 当前代码反向污染 Design Truth；
- 验证发现差异后自动进入无限修复循环；
- “低风险”被误解释为“自动获得修改权”；
- 状态被当作人工维护的死变量，而不是由 Rule / Authority / Context 派生；
- 规则关系、覆盖关系、Owner 关系不明确，执行时才让 AI 临场解释。

F6 通过 D01～D10 将以上问题拆成独立 Owner，并形成可组合、可版本化、可替换、可迁移的 Architecture Contract。

---

## 2. Reconciliation Method Normalization

### 2.1 Historical Four-Source Reconciliation

F6 阶段最终统一：

```text
Four-Source Reconciliation
=
Historical Reference Discovery
```

其用途是发现：

- 以前聊过什么；
- Legacy 有什么设计；
- Accepted Refactor / Freeze 有什么；
- Current Framework Reality 当前实现了什么；
- 有没有历史方案值得参考；
- 有没有不能无损丢失的高价值语义。

它不是自动 Authority Priority（权威优先级），也不能因为某个旧方案存在就自动成为当前目标架构。

正式冻结：

```text
Historical Evidence
!=
Current Authority

Historical Existence
!=
Current Effective
```

### 2.2 Material Reconciliation

D01 / D02 中的 Material Reconciliation（物资对账）是当前输入处理机制，负责：

```text
register
classify
deduplicate
extract
normalize
identify delta
identify conflict
identify gap
route to owner
```

但：

```text
Material Reconciliation
!=
Authority Creation
```

最终 Authority 仍由当前适用的 Human Decision、Frozen Contract、Rule、Policy、Workflow/Governance 等正式来源决定。

---

## 3. Approved F6 Decision Set

### F6-D01 — Design Input × Material Reconciliation × Design Package Input Contract

冻结：

- Unified Material Intake（统一物资入口）；
- Material registration / batch / provenance；
- reconciliation-first，而不是拿到材料直接生成终稿；
- Product semantics → PRD；
- explicit UI intent → User Design Constraint；
- design-related material → Design Evidence / Design Package input；
- Shared Foundation + Page Package 支持多页面公共/局部设计；
- 确定内容自动处理，真正不能可靠解析的冲突进入治理；
- Fact / Human Constraint / Inference / UNKNOWN 分离；
- SQLite / Index 只作为可重建查询层，不成为正式语义真源；
- Gap / Blocker localized（局部化），Carry-Forward 无损传递。

### F6-D02 — Rule / Implementation Knowledge Governance

D02-01～D02-10 + FC-01～FC-06 冻结：

- Frontend Rule System 与 UI Design Rule System 独立治理；
- `Module → Rule Entry → Index → Profile → Effective Rule Set / Context`；
- Rule Strength / Authority / Scope / Applicability / Override / Conflict 分离；
- Module / Rule Stable ID、Version、Split、Merge、Supersession、Impact；
- Material → Rule Candidate → Reconciliation，禁止第二条 Rule Formation Path；
- Module Index / Rule Association Index 只负责“找”，不负责“判”；
- Profile 负责组合，不复制 Rule Body，不创造 Rule Priority；
- Effective Design Context / Effective Implementation Context 为 Task-scoped Derived View；
- Minimum Sufficient Context，禁止全量规则常规加载；
- Index miss != Rule not exist；
- Latest != Current Effective；
- Rule Relationship UNKNOWN 时不得使用 Autonomy 猜；
- Bounded Autonomous Resolution 只处理“已知合法 Alternative 如何选择”；
- 当前不实现 AI Autonomous Learning / Autonomous Rule Promotion / Autonomous Framework Optimization。

### F6-D03 — Design Source × Scene × Semantic Tree × Design Truth

冻结：

- Material 先于 Design Source；
- Design Source / Screenshot / Prototype / Provider output = Evidence，不自动获得 Design Authority；
- Raw Scene / Normalized Scene / Semantic Tree 是可重建解释层；
- Scene 不是所有设计任务的强制必经路径；
- Provider / Interpreter / Normalizer 可替换；
- Design Truth 必须保持 provenance / confidence / freshness / unknown；
- Current Code / Existing UI 可作为 Reality Evidence，但不是 Design Truth；
- Design Package 持有具体 Design Target；
- UI_SPEC Approval 才形成批准后的 UI Contract。

### F6-D04 — Visual Property × Design Token × Shared Foundation

冻结：

- Visual Property 首先是 Evidence；
- 只有具有稳定设计意义、明确 Scope、受治理复用价值的视觉语义才能成为 Governed Design Token；
- Token Scope 不固定为“全局”，允许 Page / Application / Project Shared Foundation；
- Shared Foundation 是共享设计 WHAT，不是 CSS/Framework 实现；
- Context / Authority / Override / Version 共同决定 Token/Shared Foundation 的当前适用；
- CSS Variable / Ant Design Token / Tailwind / Figma Variable 只是实现/Provider 映射，不拥有 Design Authority。

### F6-D05 — Behavior × State × Interaction Evidence

冻结：

```text
Visible State
!=
Behavior
!=
Business State Transition
```

并明确：

- 静态图只证明可见状态，不自动证明进入条件；
- Button identity 不自动证明业务 click action；
- Interaction Evidence / Interaction Definition / Behavior Model 分离；
- Behavior Model 不拥有 Product Business Logic；
- Motion/transition 语义与具体动画实现分离；
- Provider / Prototype Adapter / Interaction Interpreter 可替换；
- 当前不实现 AI Autonomous Behavior Learning。

### F6-D06 — Data Evidence × UI Data Semantics × Demo Fixture

冻结：

- 设计中的具体值默认是 Evidence / Fixture，不是 Business Fact；
- UI Slot / Field Semantic 表达页面“需要理解什么数据”；
- UI Data Semantic != Business/API/Data Contract；
- Binding Requirement 必须与 PRD / API / Current Reality 对账；
- Demo Fixture 必须稳定、可重复、可覆盖必要场景；
- Fixture 不得冒充生产数据；
- OpenAPI / GraphQL / TypeScript / Go struct / DB model 等物理绑定留给后续实现 Owner。

### F6-D07 — Design Package × UI_SPEC Governance

冻结以下对象：

```text
Design Source
Design Package
Draft UI Contract
UI_SPEC
Effective UI Contract
```

其中：

- Design Package = concrete design target；
- UI_SPEC = approved UI construction contract；
- Effective UI Contract = Task/Batch 当前锁定的有效 UI contract snapshot；
- Design Package != UI_SPEC；
- UI_SPEC != Implementation Pack；
- PRD 保持 Product Authority；
- Latest != Current Effective；
- Design/Source 变化触发 freshness/review，不静默覆盖 Current Effective UI Contract；
- Approved != Current Effective。

### F6-D08 — Implementation Guidance × Implementation IR × Implementation Pack

冻结：

```text
Implementation Semantic Need
Implementation Guidance
Implementation IR
Implementation Pack
Framework Adapter Output
```

并明确：

- UI_SPEC owns WHAT；
- Implementation owns HOW；
- Geometry != CSS；
- Design measurement != fixed CSS；
- Implementation Guidance != UI Truth；
- Implementation Pack != UI_SPEC；
- Implementation IR framework-neutral；
- Framework Adapter 不拥有 Design Authority；
- Core 不绑定 React / Vue / AntD / Element Plus / Tailwind；
- Flex / Grid / spacing 等布局表达属于实现策略，不由截图坐标机械决定。

### F6-D09 — UI Conformance Validation × Design Drift × Interaction Regression

D09 G01～G06 + closure 冻结：

- Full UI Conformance Session 使用显式专项触发；
- Target Resolution 必须唯一可解释；`Latest != Current Effective`；
- Existing Reality != Design Truth；
- Validation Scope / Coverage 必须显式；
- Unobserved != PASS；
- Partial PASS != Whole Scope PASS；
- Observation != Target Authority；
- Evidence insufficient != AI Guess；
- Difference != Drift；
- Pixel Diff != Visual Correctness；
- Legal Alternative / Expected Variation / Approved Deviation / Acceptable Difference 分离；
- Protected Functional Baseline 独立于视觉 Protected Baseline；
- Regression Scope = impact-driven minimum sufficient；
- Risk != Authority；
- Finding != Repair Instruction；
- D09 Handoff != Mutation Authorization；
- D09 Final Report → SESSION CLOSED；
- D10 necessary local revalidation != reopen previous D09 session。

### F6-D10 — Governed Correction × Mutation Authority × Repair Governance

D10 G01～G06 + Closure C01～C05 冻结：

- Eligible for D10 Review != Authorized to Modify；
- Authorization 是 bounded capability；
- Requested Scope != Authorized Scope；
- Effective Mutation Scope ⊆ Authorized Mutation Scope；
- Not Explicitly Forbidden != Authorized；
- Impact Scope != Authorized Mutation Scope；
- Necessary != Authorized；
- Repair Plan != Mutation Authority；
- Minimum Sufficient Repair != Minimum Possible Repair；
- Implementation Repair Authority != Canonical Truth Mutation Authority；
- Low Risk != Auto Repair Permission；
- Auto Repair 必须来自适用 Policy / Authority；
- Repair 后必须 Necessary Local Revalidation；
- Repair Success = Repair Objective Satisfied + Required Regression Checks Passed；
- New Issue != Current Mutation Authority；
- Retry Allowed != Retry Until Success；
- Synchronization != Change Either Side Freely；
- Repair Result != Canonical Truth；
- Effective State != Authority Fact；
- State Derivation != Authority Creation；
- AI may derive State, but may not invent Authority；
- Escalation → Suspend First；
- Material Boundary Change → Fork New Repair Execution Instance。

---

## 4. F6 Stage Closure Normalization — C01～C06

### C01 — Historical Status Is Snapshot, Not Permanent Core Variable

早期原稿中的：

```text
Status = HUMAN_REVIEW
Implementation = NOT_AUTHORIZED
```

属于当时审批/施工状态快照。

后续 Human Approval 和 Stage Closure 决定当前架构状态。

`Implementation = NOT_AUTHORIZED` 不得被未来实现成一个需要人工维护的永久 Core Boolean。

真实执行状态应按：

```text
Scope + Profile + Rule + Authority + Context + Gate + Revision
→ Resolver
→ Effective Execution Authorization State
```

派生。

### C02 — Formal Owner Matrix

阶段 Owner：

```text
D01 → Material Intake / Reconciliation / Routing
D02 → Rule / Profile / Index / Resolution / Effective Context
D03 → Design Source / Scene / Semantic Evidence
D04 → Visual Property / Token / Shared Foundation
D05 → UI State / Interaction / Behavior
D06 → UI Data Semantic / Fixture Boundary
D07 → Design Package / UI_SPEC / Effective UI Contract
D08 → Implementation Guidance / IR / Pack
D09 → Validation / Drift / Regression Judgment
D10 → Governed Repair / Mutation / Revalidation / Closure
```

正式冻结：

```text
Earlier Broad Reference
!=
Later Specialized Authority
```

### C03 — Historical Reconciliation vs Current Material Reconciliation

```text
Four-Source Reconciliation
=
Historical Reference Discovery Only

Material Reconciliation
=
Current Input Reconciliation

Neither
=
Automatic Authority Resolution
```

### C04 — Governed Does Not Mean Manual Every Time

正式冻结：

```text
Governed
!=
Manual Every Time

Automatic
!=
Ungoverned
```

Existing Authority + Deterministic Rule + Resolved Scope + Satisfied Gate 时，应自动执行确定性工作。

Human / Governance 主要用于：

- Authority Change；
- Authority Conflict；
- unresolved ambiguity；
- High-Risk Gate；
- Canonical Truth Change；
- Rule explicitly requiring Human Decision。

### C05 — D09 Explicit Trigger Is Specialized, Not Global

D09 的固定口令只属于 Full UI Conformance Session 的专项治理入口。

```text
D09 Explicit Trigger
=
Specialized Full-Session Gate

D09 Explicit Trigger
!=
Global Automation Pattern
```

D10 必要局部复验不因此要求重新启动 D09。

### C06 — Derived View / Effective State Never Becomes Second Truth

统一冻结：

```text
Index → find
Resolver → resolve
Compiler → assemble
Effective State / Effective Context → express current derived result
Canonical Source → own authoritative meaning
```

Derived / Effective / Index / Result 对象不会因为频繁被消费而自动升级为 Canonical Authority。

---

## 5. F6 No-Loss Matrix

| Semantic Obligation | Frozen Owner |
|---|---|
| Unified material intake / reconciliation / routing | D01 |
| User Design Constraint / design input separation | D01 |
| Frontend/UI Design Rule governance | D02 |
| Rule module / entry / stable identity / version | D02 |
| Profile / Index / minimum sufficient context | D02 |
| Design Source / Raw/Normalized/Semantic evidence | D03 |
| Visual Property / Token / Shared Foundation | D04 |
| State / Interaction / Behavior | D05 |
| UI data semantics / fixture | D06 |
| Design Package / UI_SPEC / Effective UI Contract | D07 |
| Implementation Guidance / IR / Pack | D08 |
| Validation target / scope / evidence / coverage | D09 |
| Difference / Drift / Legal Alternative / Deviation | D09 |
| Protected functional regression | D09 |
| Validation result / report / handoff | D09 |
| Repair authorization / scope / plan / mutation | D10 |
| Auto-repair / retry / escalation / closure | D10 |
| Effective state / authority resolution | D10 Closure + Stage C01/C04/C06 |
| Historical vs material reconciliation normalization | Stage C03 |
| Cross-D owner normalization | Stage C02 |
| D09 trigger specialization | Stage C05 |

Result: `F6_NO_LOSS_CHECK = PASS`

---

## 6. Conflict Resolution Register

### C-F6-01 — Design Source vs Design Authority
- Status: `RESOLVED`
- Resolution: Design Source / Provider output / Screenshot = Evidence; no automatic Design Authority.

### C-F6-02 — Design Package vs UI_SPEC
- Status: `RESOLVED`
- Resolution: Design Package owns concrete design target; UI_SPEC owns approved construction contract.

### C-F6-03 — UI_SPEC vs Implementation Pack
- Status: `RESOLVED`
- Resolution: UI_SPEC = WHAT; Implementation Pack = HOW.

### C-F6-04 — Geometry vs CSS
- Status: `RESOLVED`
- Resolution: Design geometry/measurement does not mechanically select implementation strategy.

### C-F6-05 — Visible UI State vs Business Behavior
- Status: `RESOLVED`
- Resolution: D05 separates visual state evidence, interaction semantics and product business behavior.

### C-F6-06 — UI Data vs Business/API Truth
- Status: `RESOLVED`
- Resolution: D06 UI data semantics describe UI need; business/API/data authority remains upstream.

### C-F6-07 — Index Match vs Rule Effectiveness
- Status: `RESOLVED`
- Resolution: Index only discovers; Resolver evaluates Authority/Scope/Applicability/Version/Override.

### C-F6-08 — Autonomy vs Rule Authority
- Status: `RESOLVED`
- Resolution: Autonomy may choose among already legal alternatives; it may not resolve unknown authority relationships by guessing.

### C-F6-09 — Current Code vs Design Truth
- Status: `RESOLVED`
- Resolution: Current code/UI = reality evidence, not Design Truth.

### C-F6-10 — Validation vs Repair
- Status: `RESOLVED`
- Resolution: D09 judges and reports; D10 owns governed repair.

### C-F6-11 — Risk vs Mutation Authority
- Status: `RESOLVED`
- Resolution: Risk describes governance/change risk; it never creates mutation permission.

### C-F6-12 — Architecture Approval vs Runtime Authorization
- Status: `RESOLVED`
- Resolution: Freeze Pack does not itself grant project mutation authority; Effective State is resolved later.

### C-F6-13 — Governed vs Manual Every Time
- Status: `RESOLVED`
- Resolution: deterministic policy-resolvable work should automate; only genuine authority/conflict/high-risk cases escalate.

### C-F6-14 — Historical Four-Source Reconciliation vs Authority Ranking
- Status: `RESOLVED`
- Resolution: historical source review discovers old designs/evidence; current authority is resolved by current governed sources.

Blocking unresolved F6 conflict count: `0`

---

## 7. Gap Routing Result

Remaining implementation or owner-stage details are explicitly routed:

- **F7** — governed Change / Canonical Apply / rollback / reference-safe mutation / promotion apply.
- **F8** — Project Instance / `.banyan` / Profile & Binding / provider selection / version pin / project reconcile.
- **F9** — Index / Context retrieval / SQLite / FTS / Embedding / Dependency Graph / Fingerprint / Cache / Freshness engine / impact query / rebuild.
- **F10** — Runtime permission / authorization validation / provider / adapter / execution / retry / pause / resume enforcement.
- **F11** — UI / Control Plane / Rule/Profile/Impact/Decision management UX.
- **F12** — Legacy reconciliation / compatibility / migration / retirement gates.
- **Future Capability** — AI Autonomous Learning / autonomous framework optimization; current stage only reserves extension boundaries.

`F6_UNROUTED_ARCHITECTURE_GAP = 0`

---

## 8. Cross-Stage Obligations

### F7
- Canonical artifact change must not be performed by D10 repair authority.
- Rule/Design/Profile promotion or canonical mutation requires governed Change / Apply semantics.
- Preserve history / reference integrity / rollback / supersession.

### F8
- Project Profile / Binding / Provider selection consumes F6 contracts.
- Shared updates must not silently change Project Current Effective binding.
- UNKNOWN authority must not be inferred into a project binding.

### F9
- Index / cache / embedding / memory / context projection remain derived and rebuildable.
- Must support scope/profile/index targeted loading.
- Must support freshness, impact, provenance and localized invalidation.
- Must not become second UI / Rule truth.

### F10
- Runtime permission cannot manufacture Design/Product Authority.
- Resolver / execution must consume applicable F6 Authorization/Scope/Policy contracts.
- Automatic execution remains governed and bounded.

### F11
- Control Plane must expose current effective state, source/trace/conflicts without implying that UI clicks alone create Authority.
- Human intervention should remain low-friction and be reserved for genuine decision/gate cases.

### F12
- Legacy F6-related design/rule artifacts cannot be deleted merely because new contracts exist.
- Retirement requires compatibility/no-loss/migration/authority gates.

---

## 9. Final Reconciliation Result

```text
F6 Final Reconciliation                 = PASS
F6 No-Loss Check                        = PASS
F6 Cross-Decision Ownership             = PASS
F6 Conflict Review                      = PASS
F6 Gap Routing Review                   = PASS
F6 Cross-Stage Obligation               = PASS
F6 Flexibility / Extensibility          = PASS
F6 Scope→Profile→Index Targeted Loading = PASS
F6 Authority / State Separation         = PASS
F6 Deterministic Automation             = PASS
F6 AI Learning Boundary                 = PASS
Unresolved Blocking F6 Core Decision    = 0
```

F6 可正式进入 Architecture Freeze Pack 状态。

# F5 PRD Governance — Target Design

## 0. Target

F5 定义 Banyan 的 **Product Semantic Governance（产品语义治理）**：从用户自然语言 Intent 进入，到 Requirement / Product Definition 的形成、Gap/Decision/Approval、Change/CR、Trace、Version/Baseline、AI Modification Boundary，再到向 F7 交付 Product Definition Delta 与 Apply obligations。

F5 的目标不是让用户承担治理操作，而是：

> **用户表达意图，Banyan 承担治理成本；人的注意力只用于真正需要人决定的事情。**

---

## 1. Core Product Model

### Requirement

Requirement 是稳定、可寻址、可追踪的 Product Semantic Entity（产品语义实体）。

- Requirement != PRD。
- Requirement 不要求“一条需求一个文件”。
- Requirement 粒度遵循 minimum coherent product semantic boundary。
- Stable ID 不依赖文件路径、编辑动作、projection regeneration 或普通 revision。

### PRD / Product Definition

PRD / Product Definition 是 ProjectArtifact 级的 Canonical Product Definition Aggregate。

```text
Product Definition
  ├─ Requirement A
  ├─ Requirement B
  ├─ Approved Semantics
  ├─ Working Assumptions
  ├─ Deferred Uncertainties
  └─ Open Decisions
```

这些内容可以 co-locate（共处），但不因此拥有相同 Authority。

同一 semantic fact 只能有一个 Canonical Write Target；SQLite、Index、Meeting Pack、OpenSpec workspace、UI_SPEC、Code、Test、AI Memory 不得形成 competing Product Truth。

---

## 2. Reconciliation-first Product Definition Pipeline

F5 主流程：

```text
INTENT_INTAKE
→ SCOPE_RESOLUTION
→ CURRENT_STATE_RECONCILIATION
→ REQUIREMENT_SEMANTIC_ANALYSIS
→ GAP_DECISION_ROUTING
→ PRODUCT_DEFINITION_DELTA
→ COMMUNICATION_ROUTING
→ REVIEW_APPROVAL_READINESS
→ CANONICAL_APPLY_HANDOFF
→ POST_APPLY / POST_DEVELOPMENT_RECONCILIATION
```

### Rules

1. New Product Intent 先与 minimum sufficient authoritative evidence 对账，不 generation-first。
2. 基于 semantic unit 做分析，不只做 textual diff。
3. 默认产生 smallest valid Product Definition Delta，不重写 unaffected semantics。
4. 输入可分类为 ADD / MODIFY / KEEP / RETIRE / NO_CHANGE / CONFLICT / IMPLEMENTATION_GAP / DOCUMENTATION_GAP / DECISION_REQUIRED / DEFERRABLE_UNCERTAINTY。
5. F5 形成 Product Definition Delta + affected scope，交给 F7 处理 governed Change / Canonical Apply。

---

## 3. Requirement Gap & Progressive Closure

逻辑 Gap classes：

```text
SAFE_AUTO_COMPLETE
WORKING_ASSUMPTION
DECISION_REQUIRED
DEFERRABLE_UNCERTAINTY
BLOCKING_GAP
```

- `SAFE_AUTO_COMPLETE`: authoritative semantics 已足够且不创造新 business meaning。
- `WORKING_ASSUMPTION`: explicit / scoped / reversible / low-risk / non-approved。
- `DECISION_REQUIRED`: alternatives materially affect semantics / acceptance / authority / risk / downstream contracts。
- `DEFERRABLE_UNCERTAINTY`: 当前 scope 无实质威胁，可延期。
- `BLOCKING_GAP`: 默认 localized，只阻塞 affected scope。

Authority / Safety / Security / Critical Money / Irreversible Data / Core External Contract 不得为了速度降级为 provisional assumption。

Requirement Completeness != Development Readiness。

Development completion 也不自动关闭 Requirement uncertainty；必须支持 Post-Development Requirement Reconciliation。

---

## 4. Lifecycle / Readiness / Approval / Baseline

以下维度独立：

```text
Stable Identity
Revision / Version
Requirement Maturity
PRD Lifecycle
Approval
Development Readiness
Development Entry Authorization
Baseline
Current Effective
Freshness
Applicability
Supersession
History
```

PRD lifecycle 至少包含：

```text
Draft → In Review → Approved → Baselined
```

并保留 supersession / archive 等语义。

关键规则：

```text
Latest != Current Effective
Approved != Baselined
Lifecycle Status != Freshness
Baseline != Copy of Truth
```

Draft / Candidate revision 可与旧 Current Effective revision 共存。

---

## 5. Human Decision & Low-friction Governance

必须区分：

```text
User Intent
Human Decision
Approval Evidence
Development Readiness
Development Entry Authorization
Authority
Canonical Apply
```

Clear natural-language statement 在满足 Authority / Policy、scope 明确且无关键歧义时，可以直接成为 Decision / Approval Evidence。

不因 Candidate → Draft → Approved → Baselined 的 lifecycle advancing 重复确认同一 semantic decision。

低风险、解释充分的问题争取一次清晰交互完成；high-impact / irreversible / authority-sensitive 决策可升级 stronger confirmation。

Silence / cancellation / AI recommendation / inference / ambiguous preference 不构成自动确认。

---

## 6. Shape Before Build

当用户明确表达“先别开发 / 先盘需求 / 代码先别动”等，形成 conceptual `IMPLEMENTATION HOLD`。

Hold 期间允许：

- inspection / reconciliation
- gap/conflict analysis
- option comparison
- Human Decisions
- assumption/deferred capture
- impact analysis
- development-ready baseline candidate

Hold 期间禁止：

- business code mutation
- formal DB mutation
- formal API contract mutation
- Canonical Apply
- actual implementation

Development Readiness = READY 可以与 Development Entry = HOLD 共存。

---

## 7. Requirement Evolution / Change / CR

必须区分：

```text
New Requirement
Requirement Delta
Change
CR
Decision
Canonical Apply
```

- Initial shaping 中的新 Requirement 不自动需要 CR。
- Approved/Baselined Requirement 的 confirmed semantic modification 进入 formal Change；适用时生成 durable CR。
- Change Workspace = operational/governance workspace，不是 Product Truth。
- CR = previously approved Product Semantics 的 governed change record，不是所有 task 的通用容器。
- Pure implementation fix 通常不需要 CR，除非 Product Semantics 也改变。
- 已实现但未写回 Canonical Product Definition 的 confirmed semantic change = Canonical Reconciliation Debt。
- Canonical Reconciliation Debt 默认阻塞 affected scope 的 governance closeout / release / baselining，而不是全局阻塞。

F5 owns product-semantic evolution rules；F7 owns Change Workspace execution / Canonical Apply / rollback / reference-safe mutation。

---

## 8. Trace / Test / UI / Engineering Linkage

Requirement 是 stable Product Semantic Anchor。

Trace 应连接 upstream provenance 与 downstream engineering artifacts，但不得创造第二 Product Truth。

- Source Evidence 不自动授予 Product Authority。
- Material Human Decision 改变 Requirement semantics 时必须链接 Decision Evidence。
- Acceptance Intent / Acceptance Criteria / Test Artifact / Test Execution Evidence 是不同概念。
- UI_SPEC / Architecture / API / Data / Test / Batch / Implementation linkage 按 applicability。
- `NOT_APPLICABLE` != `REQUIRED_BUT_MISSING`。
- Bidirectional navigation != duplicate canonical write。
- Requirement change 触发 scoped downstream impact evaluation。
- Development Ready trace gate 与 Governance Closeout trace gate 分离。

Ownership split：

- F5 — Requirement-side linkage obligations / readiness semantics
- F6 — detailed PRD↔UI_SPEC/Design linkage
- F7 — Change / Decision / Apply reference-safe mutation
- F9 — physical Trace Graph / Index / reverse query / freshness / Evidence indexing
- F10 — Runtime enforcement / tool execution

---

## 9. Adaptive Meeting / Review Communication

Meeting Pack 是 optional、adaptive 的 human-facing derived projection。

- small/local changes 默认不问、不生成。
- communication value 由 complexity / impact / cross-role scope / unresolved decisions / comparison / collaboration needs 决定。
- Discussion Pack 用于 semantics still evolving。
- Final Review Pack 用于 semantics sufficiently settled for implementation coordination。
- Meeting conclusion 如果改变 Product Semantics，必须回到 Requirement / Change / Decision / Canonical Apply。
- upstream materially changed 后 Meeting Pack 必须 stale / regenerate。

OpenSpec：

```text
Banyan Core
→ Provider-neutral Change Workspace Contract
→ OpenSpec Adapter / Provider
```

OpenSpec 可承载 proposal / delta / impact / discussion / decision refs / design-task planning / review / archive，但不是 Core、Product Truth、Decision Authority。

---

## 10. D10 — AI Modification Boundary & Product Governance Authority

### 10.1 AI has no intrinsic Product Authority

AI Agent / Model / Provider / Skill / Role / Editor / Adapter / Runtime Client / Tool 本身不自动获得：

- Product Semantic Decision Authority
- Product Approval Authority
- Canonical Apply Authorization

但在有效 Human/Governed Authority、Apply Authorization 和 Runtime Permission 满足时，AI/Runtime 可以作为 Authorized Executor 执行已经批准的变化。

```text
AI Assistance != AI Authority
AI Execution != AI Self-Authorization
```

### 10.2 Four conceptual modification bands

1. **Deterministic Non-Semantic Automation** — 分类、ID、Trace、refs、provenance、format、freshness marker、derived projection、deterministic bookkeeping。
2. **Governed Non-Canonical Semantic Writing** — Candidate、Recommendation、Working Assumption、Deferred、Open Question、Open Decision、possible delta、impact draft。
3. **Authority-Required Product Semantic Decision / Approval** — AI 可分析/解释/比较/推荐，但不能把自己的输出升级成 Human Decision / Approved Product Meaning。
4. **Governed Canonical Apply Execution** — Decision / Approval / Apply Authorization / Runtime Permission 满足后，AI/Runtime 可作为 executor 自动应用。

这些是 Architecture concepts，不在 F5 冻结成 exact runtime enum。

### 10.3 Product Semantic Mutation Test

如果一个动作创造、改变、删除、扩大、缩小或重新解释 Product Behavior、Business Rule、Acceptance Intent、Rights/Obligations、Money/Settlement、Permission/Data Scope、Lifecycle/State Meaning、Data Ownership、Core External Contract 或 User-visible Product Behavior，则属于 Product Semantic Mutation。

不得把它伪装成 formatting / metadata / documentation cleanup / code sync 来绕过 Authority。

### 10.4 Clear Natural Language

Explicit bounded Natural Language 在 Authority / Policy 满足、无关键 ambiguity/conflict、无 stronger gate 时，可直接形成 Human Decision / Approval Evidence。

Silence / cancellation / AI recommendation / inference / ambiguous preference 不得自动构成确认。

### 10.5 No free-edit of Approved / Baselined / Current Effective semantics

Material changes must follow：

```text
Reconcile
→ Product Definition Delta
→ Change/CR when required
→ Decision / Approval
→ Canonical Apply
```

非语义 deterministic maintenance 不应被人为升级成大型 Product Decision。

### 10.6 Candidate / Assumption / Deferred may be recorded automatically

Non-canonical semantics 可自动记录，但必须保留 identity/state/provenance/scope/applicability/revisit semantics。

```text
Co-location != Equal Authority
```

### 10.7 Evidence may challenge Truth, not seize Authority

Code / Test / UI / Design / Runtime / Telemetry / Meeting Pack / Implementation 可以产生 Conflict / Gap / Drift / Candidate / Change Candidate / Reconciliation Trigger，但不能 silent redefine Product Truth。

```text
Reality may challenge Product Truth.
Reality may not silently redefine Product Truth.
```

### 10.8 Five distinct authority/enforcement concepts

1. Source Authority — 哪里是真源。
2. Product Semantic Decision Authority — 谁有资格决定产品应该是什么。
3. Product Approval Authority — 谁有资格批准某 scope/revision。
4. Canonical Apply Authorization — 这一次正式写入是否被授权。
5. Runtime Execution Permission — 当前执行者/上下文是否允许执行动作。

它们不得折叠成一个模糊 `permission=true`。

---

## 11. F5 / F7 / F10 Boundary

```text
Human / Governed Product Authority
          ↓
F5 — Product Semantic Governance
          ↓
F7 — Governed Change / Canonical Apply
          ↓
F10 — Runtime Permission / Enforcement / Execution
```

- F5 决定“什么属于 Product Meaning / 是否需要 Decision / Approval / Delta”。
- F7 决定“如何安全 promotion / apply / supersede / rollback / reconcile”。
- F10 决定“当前动作能不能被运行时执行”。

F7 不创造 Product Decision；F10 `ALLOW` 不创造 Product Authority。

---

## 12. Core Invariants

```text
AI Assistance != AI Authority
AI Execution != AI Self-Authorization
AI Recommendation != Human Decision
Candidate != Approved
Working Assumption != Approved Product Rule
Permission to Write != Authority to Decide
Role != Permission != Authority
Approval != Canonical Apply Authorization
Runtime ALLOW != Product Decision
Evidence != Authority
Co-location != Equal Authority
Latest != Current Effective
Approved != Baselined
Lifecycle Status != Freshness
One semantic fact != multiple competing Canonical Write Targets
Reality may challenge Product Truth but may not silently redefine it
```

---

## 13. Deferred to Implementation Freeze / Later Stages

F5 intentionally does **not** freeze：

- exact YAML / JSON schema
- exact enum names
- exact L0-L4 runtime mapping
- exact SQLite tables / DDL
- exact PRD physical directory / decomposition
- exact version syntax / SemVer policy
- exact AuthorizationRecord fields
- exact Canonical Apply API / Runtime API endpoint / CLI
- exact WebUI page / button / dialog
- exact RBAC / ABAC implementation
- exact Git branch / commit mechanics
- exact transaction / rollback implementation
- exact OpenSpec physical representation
- concrete CON-002 authority winner

These are not gaps in F5 Architecture Freeze; they are explicitly deferred owners.

# F5 PRD Governance — Final Reconciliation

## 0. Pack Identity

- Pack: `F5_PRD_Governance_Freeze_Pack_v1.0`
- Stage: `F5 — PRD Generation & Governance`
- Status: `ARCHITECTURE_FREEZE_PASS`
- Human Decisions: `F5-G01~G03`, `F5-D01~D10`, `CROSS-STAGE-DECISION-01`, `CROSS-STAGE-COMM-01`, `CROSS-STAGE-GOVERNANCE-01` = `HUMAN_APPROVED`
- Implementation Authorized: `false`
- RP2 Authorized: `false`
- Authority Cutover: `NOT_AUTHORIZED`
- Full Legacy Migration: `NOT_AUTHORIZED`
- Legacy Retirement/Delete: `NOT_AUTHORIZED`
- Final Activation: `NOT_AUTHORIZED`

> 本文件是 F5 最终四源对账、No-Loss、Conflict/Gap 和 Cross-Stage Obligation 的冻结记录。它不是 Implementation Freeze，也不授权施工。

---

## 1. Reconciliation Method

F5 采用四源对账：

1. **SOURCE-A — Human Decisions / confirmed communication**
2. **SOURCE-B — Legacy v3.1.15**
3. **SOURCE-C — Accepted Refactor / Stage / R0 / R1 / RP1 Evidence**
4. **SOURCE-D — Current Framework Reality**

修订优先级：

```text
仍有效的 Human Decision / Confirmation
→ Current Frozen Contract
→ Historical confirmed requirement not yet frozen
→ Legacy No-Loss
→ Accepted Refactor / R0 / R1 / RP1 Evidence
→ Current Framework Reality Check
→ Conflict / Gap / Supersession Judgment
→ New Proposal
```

Current Framework Reality 只用于说明“现在实际实现了什么”，不能反向决定目标架构必须等同当前实现。

---

## 2. SOURCE-A — Human-approved F5 Semantic Set

### 2.1 Global F5 Principles

- `F5-G01` — Low-Friction Governed Product Experience
- `F5-G02` — Progressive Requirement Closure
- `F5-G03` — User-Controlled Requirement Shaping Before Development

### 2.2 Product Governance Decisions

- `F5-D01` — Requirement 是稳定 Product Semantic Unit；PRD / Product Definition 是 Canonical Product Definition Aggregate。
- `F5-D02` — Requirement Maturity、PRD Lifecycle、Development Readiness、Closure 为独立维度。
- `F5-D03` — Gap 分类、Decision Routing、Provisional Progression 分离治理。
- `F5-D04` — User Intent、Human Decision、Approval、Development Entry、Authority、Canonical Apply 分离。
- `F5-D05` — Requirement 可寻址但不要求独立文件；Product Definition 持有 Canonical Product Semantics。
- `F5-D06` — PRD Generation 必须 reconciliation-first、incremental，并使用 adaptive communication routing。
- `F5-D07` — New Requirement、Requirement Delta、Change、CR、Decision、Canonical Apply 是不同语义。
- `F5-D08` — Requirement Trace 是 progressive、applicability-driven linkage，不创造第二 Product Truth。
- `F5-D09` — Stable Identity / Revision / Lifecycle / Approval / Baseline / Freshness / Applicability / Supersession / History 分离。
- `F5-D10` — AI Modification Boundary & Product Governance Authority。

### 2.3 Cross-stage Decisions

- `CROSS-STAGE-DECISION-01` — Adaptive Informed Decision Protocol。
- `CROSS-STAGE-COMM-01` — Adaptive Meeting & Review Communication。
- `CROSS-STAGE-GOVERNANCE-01` — Revision Authority & Reconciliation Precedence。

---

## 3. SOURCE-B — Legacy v3.1.15 No-Loss Result

以下 Legacy 高价值语义被保留：

- Confirmed / Current / Candidate / Inference / Pending/Unknown 必须区分。
- PRD 承担产品业务目标、规则、流程、验收的唯一产品真源职责。
- UI / Design / Implementation / Test 不得静默改变业务规则。
- Requirement 必须可追溯到来源、Decision、Design、Batch、Test 等适用下游。
- 未经有效 Human / Authority，不得将 Recommendation 或推断包装成已批准结论。
- 已建立 Baseline 的 Product Semantics 通过 governed Change 演进，旧历史不得静默覆盖。
- Batch/Post-development reconciliation 语义保留。

### Superseded Legacy Interaction Ritual

Legacy v3.1.3 的固定：

```text
Explain → First Selection → Impact Replay → Second Confirmation → Controlled Apply
```

作为“所有普通 Decision 的统一强制交互仪式”被 `CROSS-STAGE-DECISION-01` 的 Adaptive Informed Decision Protocol 取代。

但以下安全语义继续保留：

```text
Silence != Confirmation
Cancellation != Confirmation
AI Recommendation != Human Decision
Ambiguous Preference != Final Decision
High-impact / irreversible / authority-sensitive decisions may require stronger confirmation
```

Result: `LEGACY_NO_LOSS = PASS`

---

## 4. SOURCE-C — Accepted Refactor / R0 / R1 / Stage Reconciliation

F5 保留并重新归位了以下 Accepted Refactor 语义：

- Change Workspace 不是 Product Truth。
- Provider Workspace 不是 Product Truth。
- OpenSpec 是 first/reference Change Workspace Provider，不是 Banyan Core、Product Truth 或 Decision Authority。
- Meeting Pack 是 human-facing derived projection，不是 Product Truth。
- Trace / Evidence 不授予 Authority。
- Role / Git Identity / Editor / Provider / Commit Plan 不自动授予 Authorization。
- Canonical / Protected Write 必须具有独立 Authority / Decision / Authorization / rollback / validation 边界。
- Current Project mutation 与“Framework 已具备执行能力”严格区分。

R1 No-Loss 既有审计结果继续作为重要 evidence：

```text
LEGACY_HIGH_VALUE_CAPABILITY_UNMAPPED = 0
ACCEPTED_REFACTOR_ADDITION_UNMAPPED = 0
SILENT_SEMANTIC_DROP = 0
UNTRACEABLE_ARTIFACT = 0
UNAUTHORIZED_NEW_SEMANTIC = 0
```

Result: `ACCEPTED_REFACTOR_PRESERVATION = PASS`

---

## 5. SOURCE-D — Current Framework Reality

Current Framework Reality 与 F5 Target Architecture 不冲突，但两者不能混为一谈。

当前 Reality 至少包括：

- Runtime API / Policy Compiler / Permission Evaluator / Generic Adapter / Semantic Commit Planner / guarded executor 已存在。
- Current project execution 仍受 fail-closed / dry-run / bounded mutation 限制。
- Canonical Apply 与完整 Change lifecycle 仍无完整 current executable API。
- `.banyan` 仍是 Pilot / Shadow context；Final Activation 未授权。
- Role != Permission != Git Identity != Authentication 的边界已经在现有文档/验收中保持。

因此：

```text
FROZEN_CONTRACT != IMPLEMENTED
```

F5 Freeze 不能被描述成 Current Framework 已经完整实现 F5。

Result: `CURRENT_REALITY_CONFLICT = NONE_BLOCKING`

---

## 6. F5 No-Loss Matrix

| Semantic Obligation | Frozen Owner |
|---|---|
| 新输入先与当前状态对账 | D01 / D06 |
| Requirement 稳定身份与语义粒度 | D01 / D05 |
| PRD / Product Definition 真源 | D01 / D05 |
| Gap / Assumption / Deferred | G02 / D03 |
| Draft / Review / Approved / Baselined | D02 / D04 / D09 |
| Readiness 与 Approval / Entry 分离 | G02 / G03 / D02 / D04 |
| Human Decision / Authority | D04 / D10 / CROSS-STAGE-DECISION-01 |
| Change / CR | D07 |
| Canonical Apply 产品侧义务 | D04 / D05 / D07 / D10 → F7 |
| Trace / Test / UI / Code linkage | D08 |
| Version / Effective / Baseline / Freshness | D09 |
| AI 修改边界 | D10 |
| Code/UI/Design reverse influence | D08 / D10 |
| Meeting / Review Communication | D06 / CROSS-STAGE-COMM-01 |
| OpenSpec provider-neutral positioning | D06 / D07 / CROSS-STAGE-COMM-01 |
| Post-development reconciliation | G02 / D06 / D07 |
| Low-friction Natural Language governance | G01 / D04 / D10 / CROSS-STAGE-DECISION-01 |

Result: `F5_NO_LOSS_CHECK = PASS`

---

## 7. Conflict Resolution Register

### C-F5-01 — Fixed Double Confirmation vs Adaptive Decision
- Status: `RESOLVED`
- Resolution: 固定交互形式被 supersede；安全语义保留。

### C-F5-02 — OpenSpec vs Product Truth
- Status: `RESOLVED`
- Resolution: OpenSpec = provider/workspace；不得成为 Product Truth / Decision Authority。

### C-F5-03 — Meeting Pack vs Product Truth
- Status: `RESOLVED`
- Resolution: Meeting Pack = derived human-facing projection。

### C-F5-04 — Code/UI/Test/Design vs PRD Authority
- Status: `RESOLVED`
- Resolution: downstream reality/evidence may challenge Product Truth, but may not silently redefine it。

### C-F5-05 — Role vs Permission / Authority
- Status: `RESOLVED`
- Resolution: Role / RoleAssignment 不自动授予 Permission / Source Authority / Product Decision Authority。

### C-F5-06 — Approval vs Canonical Apply
- Status: `RESOLVED`
- Resolution: Approved Requirement 不自动授权 Canonical Apply。

### C-F5-07 — Latest vs Current Effective
- Status: `RESOLVED`
- Resolution: Latest != Current Effective；Approved != Baselined；Freshness independent。

### C-F5-08 — AI Write Capability vs Product Authority
- Status: `RESOLVED`
- Resolution: AI 可自动整理/起草/执行已授权变更，但不得 self-authorize Product Meaning。

Blocking unresolved F5 conflict count: `0`

---

## 8. Gap Routing Result

剩余 Gap 已明确路由到后续阶段，不再视为 F5 未完成 Architecture Decision：

- **F6** — UI_SPEC / Design Truth / Visual Governance / detailed PRD↔UI impact。
- **F7** — Change Workspace mechanics / Canonical Apply / rollback / reference-safe mutation / supersession mechanics。
- **F8** — Project Instance / Authority-Binding / Overlay / Provider & Source mapping instance mechanics。
- **F9** — Index / Context / Memory / Evidence / Freshness / reverse query / rebuild。
- **F10** — Runtime Permission / Authorization Validation / Write Guard / Provider / Adapter / Execution。
- **F11** — WebUI / guided review / approval UX / control plane interaction。
- **F12** — Legacy compatibility / reconciliation / migration / retirement gates。

`CON-002 = TYPED_BLOCKED_HUMAN_PROJECT_AUTHORITY` 继续作为 carried blocker；它是具体 Project Authority 绑定问题，不是 F5 Product Semantic Architecture 未定义问题。

Result: `F5_UNROUTED_ARCHITECTURE_GAP = 0`

---

## 9. Cross-Stage Obligations

### F6 obligations
- UI_SPEC 不得成为第二 Product Truth。
- Design / screenshot / prototype = Evidence / Design Source。
- Product Semantic changes 必须通过 Product Change；不得用 UI silent override PRD。
- Relevant Product changes 触发 scoped UI freshness / review impact。

### F7 obligations
- F7 不得发明 Product Decision。
- Change Workspace 不是 Product Truth。
- Approved != Apply Authorization。
- Canonical Apply 必须消费有效 Decision / Approval / Apply Authorization。
- Same semantic fact must not gain competing Canonical Write Targets。
- 必须保留 history / supersession / reference integrity / rollback / reconciliation。

### F8 obligations
- Project Instance 可绑定 authority/source/provider/overlay，但不得重新定义 F5 已冻结 Authority 语义。
- UNKNOWN authority 不得由推断自动补齐。

### F9 obligations
- Trace / Index / Evidence / Memory / Summary / Cache != Product Authority / Product Truth。
- 必须支持 stable identity / provenance / impact / freshness / history query。

### F10 obligations
- Permission to Write != Authority to Decide。
- AI Role / Editor / Git Identity / Provider 不自动产生 Product Authorization。
- Runtime ALLOW != Product Decision。
- Protected write 必须尊重 F5 / F7 semantic preconditions。

### F11 obligations
- UI click != Authority。
- Natural-language confirmation 必须保持 scope / semantics / authority evidence。
- 普通 Decision 保持 low-friction；high-impact decision 支持 stronger confirmation。

### F12 obligations
- Legacy 不得因新架构存在而直接删除。
- Retirement 必须经过 compatibility / no-loss / migration / authority gates。

---

## 10. Final Reconciliation Result

```text
F5 Final Reconciliation       = PASS
F5 No-Loss Check              = PASS
F5 Conflict Review            = PASS
F5 Gap Routing Review         = PASS
F5 Cross-Stage Obligation     = PASS
Unresolved Blocking F5 Core Decision = 0
```

F5 可进入 Architecture Freeze Pack 状态。

# Stage 05 → Stage 06 Gate Review v1.0

> Review Basis：Stage 05 Acceptance Report、VALIDATION_RESULTS、NEXT_STAGE_HANDOFF、CON001_RESOLUTION_RECORD  
> Stage 05 Run：`stage05-20260920T144623Z`  
> Review Result：**PASS_FOR_STAGE06_DESIGN_WITH_INHERITED_BLOCKERS**  
> Stage 06 Execution：**NOT_STARTED / NOT_AUTHORIZED**

---

## 1. 最终结论

```text
Stage 05 = COMPLETED
Stage 05 Acceptance = PASS_WORKFLOW_AND_SEMANTIC_COMMIT_POLICY_FREEZE
Stage 06 Entry Gate = PASS_FOR_STAGE06_DESIGN_WITH_INHERITED_BLOCKERS
Stage 06 Execution = NOT_STARTED
```

Stage 05 已冻结 Adaptive Workflow、五级决策、Human Confirmation、Semantic Commit Workflow / Policy，并完成 CON-001 的分层契约化解决。

Stage 06 可以进入：

```text
Change Workspace Provider
OpenSpec Integration
Canonical Apply / Promotion / Reconciliation
```

设计阶段。

---

## 2. Stage 05 已冻结成果

```text
Adaptive Workflow
LIGHT / STANDARD / FULL Work Modes
L0 ～ L4 Decision Levels
Human Confirmation / Escalation
CON-001 = RESOLVED_BY_LAYERED_CONTRACT
Semantic Commit Workflow
READY / INCOMPLETE / UNRELATED / LOCAL_ONLY / SECRET_RISK
Semantic Grouping / Hunk Planning
Commit Message Policy
Git Identity Policy
Commit Authorization Boundary
Leftover Reporting
```

Stage 05 没有执行任何 Git Commit，也没有实现 Runtime Executor。

---

## 3. CON-001 状态

CON-001 已从未建模冲突转为：

```text
Generic Core = Decision Semantics
Project Overlay = Pacing / Project Parameters
Safety Floor = Non-overridable
```

当前项目：

```text
decision_batch_max = 5
high_impact_batch_max = 1
```

只属于 Project Overlay，不进入 Generic Core。

Stage 06 必须消费这套 Decision Contract，
不能重新把项目参数写进 Core。

---

## 4. Stage 06 正式职责

Stage 06 的核心问题：

```text
“变更讨论、Draft、并行方案、OpenSpec Change、Canonical 文档之间如何安全流动？”
```

必须设计并冻结：

```text
Change Workspace abstraction
Change Workspace Provider Port
OpenSpec Provider binding contract
Change identity / lifecycle
Draft / Parallel Draft lifecycle
Proposal / Spec Delta / Task / Design relationships
Canonical Apply Contract
Draft Promotion Contract
Batch Reconciliation Contract
Conflict / Divergence handling
Reference Integrity during apply
No-loss apply semantics
Apply preview / dry-run contract
Apply authorization boundary
Rollback / recovery semantics
Provider-neutral workspace model
```

---

## 5. 关键能力来源

Stage 03 已冻结的重要能力契约：

```text
banyan.contract.change_application.v1
banyan.contract.draft_promotion.v1
banyan.contract.batch_reconciliation.v1
banyan.contract.reference_integrity.v1
banyan.contract.artifact_status_and_identity.v1
banyan.contract.evidence_trace.v1
```

Stage 05 冻结的 Workflow / Decision Contract 负责：

```text
什么时候可以继续
什么时候要确认
什么时候 BLOCK
```

Stage 06 不得重复定义这些语义。

---

## 6. Change Workspace 不等于 OpenSpec

必须保持：

```text
Change Workspace = Banyan Generic Abstraction
OpenSpec = Provider Candidate / Provider Binding
```

未来可以有：

```text
OpenSpec
Generic Filesystem Workspace
Other Change Provider
```

Core 不得直接依赖 OpenSpec 的具体目录名称和文件格式。

---

## 7. Canonical Apply 原则

Apply 必须是显式动作。

禁止：

```text
讨论稿自动成为 Canonical
Draft 直接覆盖 PRD
Provider Workspace 自己修改 Canonical
未验证引用直接删除旧 Artifact
Apply 后双写真源
```

必须：

```text
Preview
Impact
Reference Check
Decision Gate
Authorization
Apply Plan
Apply
Validation
Evidence
Reconciliation
```

Stage 06 当前只冻结流程和 Provider 合同，不执行真实 Legacy Apply。

---

## 8. Parallel Draft / Reconciliation

Stage 06 必须保留现有高价值能力：

```text
Parallel Draft
Draft Promotion
36A / 类似收口语义
Batch Reconciliation
```

允许多个候选方案存在。

禁止：

```text
AI 私自合并冲突
用最后修改时间自动选 winner
用 provider-specific 状态替代 Banyan semantic status
```

冲突时使用 Stage 05 Decision Mechanism。

---

## 9. Canonical Truth 边界

必须区分：

```text
DISCUSSION
DRAFT
CHANGE_WORKSPACE
PROPOSED
APPROVED_FOR_APPLY
CANONICAL
DERIVED
HISTORICAL
```

Provider Workspace 不是 Canonical Truth。

Canonical Truth 的实际物理来源由：

```text
Source Role
Source Mapping
Project Instance
```

决定。

---

## 10. CON-002

继续继承：

```text
CON-002 = OPEN
Owner Stage = 12
```

Stage 06 可以设计 freshness / divergence 表达，
但不得代替 Stage 12 裁决项目 source freshness 策略。

---

## 11. Low-Token 原则

默认读取：

```text
本 Gate Review
Stage 06 Low-Token Input Index
Stage 05 NEXT_STAGE_HANDOFF
Stage 05 Workflow / Decision contracts
Stage 03 change/draft/reconciliation/reference contracts
Stage 04 Project Instance / Source Mapping / Provider Binding schema
Stage 01/02 只按 CAP-CHANGE / CAP-PARALLEL / CAP-RECONCILE 定点回读
```

禁止：

```text
重新扫描 Repository
重建 Asset Inventory
重跑 Git 历史
重新分析所有 35 Capability
```

---

## 12. 继承风险

继续：

```text
R03-PURITY
R03-SOURCE
CON-002
R03-COST
R03-SECRET
R03-LOCAL
```

13 Secret：

```text
SECRET_METADATA_ONLY
PARTIAL_APPROVED
```

---

## 13. Gate Decision

```text
Stage 05 → Stage 06 = PASS_FOR_STAGE06_DESIGN_WITH_INHERITED_BLOCKERS
Stage 06 Pack Generation = ALLOWED
Stage 06 Execution = NOT YET AUTHORIZED
```

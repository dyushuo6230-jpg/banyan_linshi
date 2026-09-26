# AUDIT-PATCH-010 — Reconciliation Precedence × Authority Validation × Canonical Transition Boundary

> Patch ID: `AUDIT-PATCH-010`  
> Source Candidate: `B2-PATCH-05`  
> Status: `HUMAN_APPROVED`  
> Classification: `DEFECT / P1`  
> Scope: Pre-F9 F1～F8 Architecture Integrity & Optimization Review — Audit Batch 2  
> Primary Affected Stages: `F5 / F6 / F7 / F8 / F9 / F10 / F11`  
> Implementation Authorization: `NO`

---

## 1. Problem（问题）

F5 的 `CROSS-STAGE-GOVERNANCE-01 — Revision Authority & Reconciliation Precedence` 已冻结：

```text
Still-valid Human Decision / Confirmation
→ Current Frozen Contract
→ Historical Confirmed Requirement
→ Legacy No-Loss
→ Accepted Evidence
→ Current Reality
```

原意是：旧文档 / Legacy / Current Code 不得反向覆盖已经明确确认的人类意图。

但“Human Decision outranks Frozen Contract”如果被字面实现为“Human Decision 立即替换 Canonical Truth”，会绕过 Authority、Governed Change、Apply Authorization、Canonical Acceptance。

因此必须收窄为 **Reconciliation / Target-Intent Precedence**，而不是 Mutation / Runtime Authority Priority。

---

## 2. Two Different Precedence Models

### Reconciliation Precedence

回答：

> 多份材料冲突时，哪份更能代表已经确认的目标意图？

正确顺序仍保留：

```text
Valid Human Decision / Confirmation
→ Current Frozen Contract
→ Historical Confirmed Requirement
→ Legacy No-Loss
→ Accepted Evidence
→ Current Reality
```

### Authority / Canonical Transition

回答：

> 谁有资格决定？该决定是否已正式成为 Canonical Truth？

需要独立消费：

- Authority；
- Scope；
- Semantic Domain；
- Policy / Applicability；
- Gate；
- Approval；
- Apply Authorization；
- Canonical Apply；
- Validation / Canonical Acceptance。

正式：

```text
Reconciliation Precedence != Authority Precedence
Reconciliation Source Priority != Mutation Authorization
```

---

## 3. Human Statement / Decision / Mutation Boundary

```text
Human Statement != Human Decision
Human Decision != Authorized Semantic Mutation
```

只有：

```text
clear decision
+ applicable authority
+ valid scope
+ valid semantic domain
+ applicable policy
+ no unresolved blocking conflict
```

才形成 Valid Human Decision Evidence，并进入高优先级 Reconciliation。

因此顺序为：

```text
Human Statement
↓
Decision Semantic Resolution
↓
Effective Authority Resolution
↓
Valid Human Decision
↓
Reconciliation Precedence
```

---

## 4. Target Semantic vs Current Canonical

Reconciliation 的结果可以明确：

```text
Current Canonical = A
Target Semantic = B
Semantic Delta = A → B
```

正式冻结：

```text
Target Semantic != Current Canonical Semantic
Reconciliation Result != Current Effective Transition
Human Decision Evidence != Immediate Canonical Replacement
```

这允许 Banyan 同时知道“现在正式是什么”和“已经决定目标要变成什么”，而不发生静默覆盖。

---

## 5. Governed Canonical Transition

目标链：

```text
Valid Human Decision
↓
Reconciliation
↓
Target Semantic Resolution
↓
Semantic Delta
↓
Governed Change
↓
Applicable Approval
↓
Apply Authorization
↓
Canonical Apply
↓
Post-mutation Validation / Reconciliation
↓
Canonical Acceptance
↓
Current Effective Transition
```

具体变化是否需要所有步骤由 Applicability / Gate 决定；本 Patch 不要求普通低风险任务走固定重仪式。

正式：

```text
Reconciliation != Canonical Apply
Reconciliation Engine != Mutation Authority
```

---

## 6. Protected but Evolvable Canonical Truth

```text
Canonical Truth
is protected but evolvable
through governed change
```

Frozen / Canonical 不是永远不能改；合法新 Human Decision 也不是立即覆盖旧真相。

正确模型：

```text
Current Canonical Baseline
+ Valid Governed Delta
→ New Canonical Revision
```

---

## 7. Supersession Boundary

合法新 Decision 可以明确 supersede 旧 Decision，但：

```text
Decision Supersession
!= Canonical Apply Completed
```

同时：

```text
Decision History != Canonical Revision History
```

Decision 更新不允许原地改写历史 Canonical Revision。

---

## 8. Authority / Scope / Hard Governance Boundary

Human Decision 的 Reconciliation Precedence 不能超出：

- Valid Authority Envelope；
- Valid Scope；
- Valid Semantic Domain；
- Hard Governance Invariant；
- Override / Exception eligibility；
- Apply Authorization；
- Runtime Permission。

正式：

```text
Human Decision does not bypass Hard Governance
Higher Reconciliation Precedence != Scope Expansion Authorization
Higher Reconciliation Precedence != Override Authority
Reconciliation Precedence != Exception Eligibility
```

---

## 9. Latest / Evidence / Reality Boundary

继续保持：

```text
Latest != Current Effective
Latest != Highest Reconciliation Precedence
Evidence != Authority
Current Reality != Final Architecture Authority
```

最新一句话可能只是 question / idea / clarification / invalid-authority statement，因此不能因为“最新”自动升为最高对账来源。

Current Code / UI / Runtime 可以 challenge / detect drift / produce evidence，但不能静默重定义目标语义。

---

## 10. Pre-Apply Impact Analysis

Target Intent 尚未成为 Canonical Truth 时，仍可以做：

```text
planning / impact / evidence work
```

例如预先分析“如果退款 7 天改 15 天会影响哪些 UI / API / Test / Batch”。

但：

```text
Potential Impact != Current Effective Invalidation
```

除非适用 Gate 明确要求提前 HOLD。

---

## 11. Cross-Patch Integration

- `AUDIT-PATCH-007`：Gate 是否适用 / 是否需要人；
- `AUDIT-PATCH-008`：正式上游变化后的 downstream re-resolution；
- `AUDIT-PATCH-009`：谁拥有适用 Authority；
- 本 Patch：合法 Human Decision 在对账层如何形成 Target Delta，又如何与 Current Canonical Transition 分离。

因此：

```text
Statement
→ Authority Validation
→ Valid Decision
→ Reconciliation
→ Target Delta
→ Governed Canonical Transition
```

成为统一合同。

---

## 12. Stage Owner Boundary

- F5 — Product Intent / Human Decision / Product Authority / Reconciliation-first Product Definition；
- F6 — UI / Design reconciliation / target design delta / UI_SPEC governance；
- F7 — Governed Change / Apply Authorization / Canonical Apply / Acceptance / Revision / Supersession；
- F8 — Project / Scope / Authority applicability context；
- F9 — history / decision trace / impact / retrieval index，不能成为 reconciliation authority；
- F10 — Runtime Permission / execution enforcement；
- F11 — 展示 Current Canonical / Target Semantic / Delta / Apply State 的 governance UX。

---

## 13. No-Loss / Supersession

保留 `CROSS-STAGE-GOVERNANCE-01` 的核心价值：

- Current implementation reality 不能反压已确认 intent；
- Legacy 不能覆盖更新的合法确认；
- conflicting decisions 必须显式 reconcile / supersede；
- no silent overwrite。

只 supersede 以下宽泛错误解释：

```text
Human Decision outranks Frozen Contract
therefore Human Decision immediately becomes effective truth
```

正确解释：

```text
Valid Human Decision outranks older conflicting frozen semantics
for reconciliation / target-intent resolution;
it does not itself perform canonical mutation.
```

---

## 14. Banyan-wide Invariants

```text
Reconciliation Precedence != Authority Precedence
Reconciliation Source Priority != Mutation Authorization
Human Statement != Human Decision
Human Decision != Authorized Semantic Mutation
Human Decision Evidence != Immediate Canonical Replacement
Target Semantic != Current Canonical Semantic
Reconciliation Result != Current Effective Transition
Reconciliation != Canonical Apply
Decision Supersession != Canonical Apply Completed
Valid Human Decision does not bypass Authority Envelope
Valid Human Decision does not bypass Hard Governance Invariant
Higher Reconciliation Precedence != Scope Expansion Authorization
Canonical Truth is protected but evolvable through governed change
```

---

## 15. Forbidden Interpretations

禁止：

1. 人说的话永远比正式合同高；
2. Human Statement 自动等于合法 Decision；
3. 新 Human Decision 自动修改 PRD / UI_SPEC / Policy；
4. Human Decision 绕过 Authority / Scope / Domain / Hard Governance；
5. Human Decision 自动授予 Apply Authorization / Runtime Permission；
6. Reconciliation Result 自动成为 Current Effective；
7. Target Semantic 自动等于 Canonical Truth；
8. Decision Supersession 自动完成 Canonical Apply；
9. Latest Message 自动最高优先；
10. Current Code / Evidence 反向获得 Decision Authority；
11. Reconciliation Engine 直接修改 Canonical Truth；
12. Frozen Contract 永远不可演进；
13. 本 Patch 要求所有变化人工审批；
14. 本 Patch 授权 Implementation。

---

## 16. Integration Target / Version Impact

未来整合时，应精确解释 F5 `CROSS-STAGE-GOVERNANCE-01` 为 Reconciliation Evidence / Target-Intent Precedence，并补充 F6/F7/F8/F9/F10/F11 的消费边界。

F1～F8 v1.0 不直接修改。

---

## 17. Human Decision

`B2-PATCH-05 HUMAN_APPROVED` 已完成：

```text
AUDIT-PATCH-010 = HUMAN_APPROVED
```

---

## Current Authorization Boundary（当前授权边界）

本 Patch 只属于 Audit Patch Layer（审计补丁层）。即使 `HUMAN_APPROVED`，仍然：

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
```

F1～F8 v1.0 继续保持 Original Frozen Baseline（原始冻结基线），直到整个 Pre-F9 Audit 完成、形成 F1～F8 v1.1 Candidate、完成 No-Loss Reconciliation / Final Audit 并再次获得明确批准。

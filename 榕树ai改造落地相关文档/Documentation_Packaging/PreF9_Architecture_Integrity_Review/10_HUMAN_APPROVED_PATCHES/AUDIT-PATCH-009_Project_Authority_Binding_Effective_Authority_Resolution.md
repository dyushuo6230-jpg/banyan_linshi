# AUDIT-PATCH-009 — Project Authority Binding × Effective Authority Resolution × Governed Override / Exception Eligibility

> Patch ID: `AUDIT-PATCH-009`  
> Source Candidate: `B2-PATCH-04`  
> Status: `HUMAN_APPROVED`  
> Classification: `GAP / P1`  
> Scope: Pre-F9 F1～F8 Architecture Integrity & Optimization Review — Audit Batch 2  
> Carried Blocker: `CON-002 — TYPED_BLOCKED_HUMAN_PROJECT_AUTHORITY`  
> Primary Affected Stages: `F5 / F6 / F7 / F8 / F9 / F10 / F11`  
> Implementation Authorization: `NO`

---

## 1. Problem（问题）

F5 已经区分 Source Authority、Product Semantic Decision Authority、Product Approval Authority、Canonical Apply Authorization、Runtime Execution Permission；F7/F8 也已经明确 Role / Identity / Overlay / Runtime ALLOW 不创造 Authority。

真正遗留的 `CON-002` 是：

> 在具体 Project、Scope、Semantic Domain、Decision / Action Type 下，谁拥有哪种 Authority，以及多个 Authority / Override / Exception 出现时如何解析。

旧名 `CON002_CONCRETE_AUTHORITY_WINNER` 过于狭窄，因为合法治理有时不是“选一个赢家”，而是 Single Authority、Delegated Authority、Compound Authority 或 unresolved conflict。

因此正式采用：

```text
Effective Authority Resolution
```

---

## 2. Core Contract（核心合同）

```text
Authority Fact / Binding
= Governed Input

Effective Authority
= Derived Resolution Result
```

因此：

```text
Effective Authority != Second Authority Truth
Effective Authority Resolution != Authority Creation
```

Authority 不得退化为：

```text
user_id = X
authority = true
```

而必须是 Scoped Authority（范围化权威）。

---

## 3. Project Authority Binding Semantic Model

Architecture 层至少能够表达：

- Authority Principal；
- Project / Project Instance；
- Authority Kind；
- Semantic Domain；
- Scope；
- Decision / Action Class；
- Applicability；
- Boundary / Constraint；
- Override / Exception Capability；
- Validity；
- Revision / Supersession / Revocation；
- Provenance / Evidence。

本 Patch 不冻结 exact YAML / DB / SQLite / RBAC / ABAC / API representation。

---

## 4. Identity / Role Boundary

正式冻结：

```text
Identity != Authority
Authentication != Authority
Git Identity != Authority
Editor Identity != Authority
RoleAssignment != Authority Binding
```

RoleAssignment 表达 Responsibility / Participation；Authority Binding 表达受治理的 Decision / Approval / Exception / Override Authority。

例如 `Software Implementation` Role 不自动获得 Product Semantic Decision Authority；`Engineering Standards Steward` 不自动获得 Standard Adoption / Exception / Canonical Apply Authority。

---

## 5. Authority Kind / Domain / Scope

继续保持：

```text
Decision Authority
!= Approval Authority
!= Apply Authorization
!= Runtime Permission
```

并新增：

```text
Authority in Domain A != Authority in Domain B
Authority for Scope A != Authority for Scope B
More Specific Scope != Higher Authority
Project Local != Automatic Override
```

Authority 必须根据 Project / Domain / Scope / Decision Type / Policy / Validity 解析。

---

## 6. Authority Envelope（权威包络）

正式引入 Architecture Concept：

```text
Authority Envelope
=
Principal
× Authority Kind
× Semantic Domain
× Scope
× Decision / Action Class
× Constraints
× Validity
```

它回答：

> 当前 Principal 在什么条件下，可以做什么类型的治理决定。

并且：

```text
Authority Envelope != Runtime Permission
```

---

## 7. Governed Override / Exception

正式冻结：

```text
Override Scope ⊆ Valid Authority Envelope
Override != Priority Number
Override != File Ordering
Override != Latest Wins
Project Local != Automatic Override
```

Exception 必须经过：

```text
Applicable Rule / Standard
→ Exception Eligibility
→ Required Exception Authority
→ Scope / Boundary
→ Approved Exception
```

并保持：

```text
Convenience != Exception Authority
Implementation Necessity != Exception Authority
Low Risk != Exception Authority
Exception Approval != Authority Expansion
```

普通 Project Override / Exception 不能绕过 Hard Governance Invariant。

---

## 8. Multiple / Compound / Delegated Authority

正式：

```text
Multiple Authorities != Authority Conflict
```

某动作可以要求：

```text
Authority A AND Authority B
```

例如 Product Approval + Security / Privacy Approval，这叫 Compound Authority Requirement，不需要挑一个 winner。

支持 bounded Delegation：

```text
A delegates B
within Scope X / Decision Type Y / Validity Z
```

但：

```text
Delegation != Unlimited Authority Transfer
```

---

## 9. Authority Conflict

真正 Authority Conflict 应至少满足：

```text
Same Semantic Subject
+ Same Applicable Scope
+ Same Authority / Decision Kind
+ Multiple Valid Authority Decisions
+ Mutually Incompatible
+ no Policy / Delegation / Supersession / Precedence resolves it
```

此时：

```text
AUTHORITY_CONFLICT → Human Governance
```

禁止：

- Last Write Wins；
- Latest Message Wins；
- More Specific Scope Automatically Wins；
- Local Project Rule Automatically Wins；
- Highest Numeric Priority Wins；
- AI Recommendation / Model Confidence Wins。

---

## 10. Revision / Supersession / Revocation

Authority Binding 自身必须支持：

```text
Stable Identity
Revision
Validity
Supersession
Revocation
History
```

并保持：

```text
Authority Revoked != Authority History Deleted
Current Authority != Historical Validity
```

某人后来失去 Authority，不会自动让其过去在有效 Authority 下产生的合法决定变成“历史未授权”。

---

## 11. Low-friction Natural Language

正式保持：

```text
Clear Bounded Natural Language
+ Valid Effective Authority
+ Clear Scope
+ No Blocking Conflict
+ No Stronger Gate
→ may directly form Decision / Approval Evidence
```

内部严格解析 Authority，不等于外部每次都重复询问。

只有 Authority missing / conflict、Scope ambiguity、Override eligibility unresolved、compound authority incomplete 等真实 Judgment Gap 才进入 REVIEW_REQUIRED。

UNKNOWN Authority 必须保持 UNKNOWN，不得由 AI 猜测补齐。

---

## 12. Stage Owner Boundary

- F5 — Product Authority semantics / Product Decision / Approval semantics；
- F6 — UI / Design Authority semantics；
- F7 — Governed Change / Decision-Approval-Apply consumption / Canonical Apply；
- F8 — **Project Authority Binding Mechanics**；
- F9 — Authority-related index / query / freshness；Index != Authority；
- F10 — Runtime identity / authorization validation / execution enforcement；Runtime ALLOW != Authority Creation；
- F11 — Human-facing Authority / Conflict UX；UI Click != Authority。

不新增 GlobalAuthorityCenter / AuthorityDefinitionService / DecisionWinnerEngine。

---

## 13. CON-002 Closure

本 Patch 获得 `HUMAN_APPROVED` 后，在 Architecture Audit Layer 正式将：

```text
CON-002
TYPED_BLOCKED_HUMAN_PROJECT_AUTHORITY
```

更新为：

```text
CON-002 = ARCHITECTURALLY_RESOLVED
```

架构答案：

```text
Project Authority Binding
+ Authority Envelope
+ Effective Authority Resolution
+ Governed Conflict / Override / Exception Resolution
```

F5 v1.0 原始 `CON002_CONCRETE_AUTHORITY_WINNER` 继续保留历史原文，不直接修改。

Identity Provider、RBAC / ABAC、SQLite Schema、YAML Schema、API、WebUI、Runtime implementation 仍属于后续 Owner Stage，不再属于 Architecture Gap。

---

## 14. Banyan-wide Invariants

```text
RoleAssignment != Authority Binding
Authority in Domain A != Authority in Domain B
More Specific Scope != Higher Authority
Project Local != Automatic Override
Later Decision != Automatic Winner
Multiple Authorities != Authority Conflict
Effective Authority Resolution != Authority Creation
Override Scope ⊆ Valid Authority Envelope
Exception Approval != Authority Expansion
Unknown Authority != Inferred Authority
```

---

## 15. No-Loss / Compatibility

保留 F5/F6/F7/F8 的全部 Authority / Truth / Scope / Runtime separation，只补齐具体 Project Authority Binding 与 Effective Authority Resolution。

与 `AUDIT-PATCH-007` Adaptive Gate Governance 和 `AUDIT-PATCH-008` Re-resolution Routing 兼容：前者决定何时需要 Authority Gate，后者可能发现“需要重新决定”，本 Patch 决定“谁有资格决定”。

---

## 16. Forbidden Interpretations

禁止：

1. 当前登录用户默认有 Authority；
2. Human Statement 自动拥有所有 Domain Authority；
3. RoleAssignment = Authority；
4. Scope 更具体就自动胜出；
5. Project-local 自动覆盖 shared rule；
6. Later Decision 自动胜出；
7. Priority number 决定 Authority；
8. 多 Authority 必须选一个 winner；
9. Override / Exception 超出 Authority Envelope；
10. Runtime Permission 创造 Semantic Authority；
11. SQLite / Index 成为 Authority Truth；
12. Authority Revocation 重写历史合法性；
13. AI 猜测 UNKNOWN Authority；
14. 新建 Global Authority Center；
15. 本 Patch 授权 Implementation。

---

## 17. Integration Target / Version Impact

未来整合目标主要为 F5 authority references、F8 Project Authority Binding mechanics、F7/F10 consumption boundary，并向 F9/F11 提供索引 / UX 合同。

Exact physical representation deferred。

F1～F8 v1.0 保持原文。

---

## 18. Human Decision

`B2-PATCH-04 HUMAN_APPROVED` 已完成：

```text
AUDIT-PATCH-009 = HUMAN_APPROVED
CON-002 = ARCHITECTURALLY_RESOLVED
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

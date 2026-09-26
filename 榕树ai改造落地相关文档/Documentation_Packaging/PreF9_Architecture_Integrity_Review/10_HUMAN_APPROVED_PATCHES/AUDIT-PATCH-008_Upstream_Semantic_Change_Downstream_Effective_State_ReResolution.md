# AUDIT-PATCH-008 — Upstream Semantic Change × Downstream Effective State Invalidation × Re-resolution Routing

> Patch ID: `AUDIT-PATCH-008`  
> Source Candidate: `B2-PATCH-03`  
> Status: `HUMAN_APPROVED`  
> Classification: `GAP / P1`  
> Scope: Pre-F9 F1～F8 Architecture Integrity & Optimization Review — Audit Batch 2  
> Primary Affected Stages: `F5 / F6 / F7 / F8 / F9 / F10`  
> Implementation Authorization: `NO`

---

## 1. Problem（问题）

F5 已要求 Requirement Change 触发 scoped downstream impact evaluation；F6 已有 Current Effective UI Contract 的 `CURRENT / STALE / REVIEW_REQUIRED / SUPERSEDED / CONFLICTED / UNKNOWN`；F7 已有 Freshness / Impact / `STALE != INVALID`；F8 / F10 已有 runtime stale / mismatch → re-resolution feedback。

缺口是：

> Banyan 尚未形成一个统一的跨阶段合同，明确 Authoritative Upstream Semantic Change（权威上游语义变化）如何使真正依赖它的 downstream Derived / Effective State（下游派生 / 当前有效状态）进入 freshness / impact / re-resolution 判断，同时又不让上游 Owner 越权改写下游语义。

---

## 2. Target Contract（目标合同）

正式冻结：

```text
Authoritative Upstream Change
may invalidate dependent downstream
Derived / Effective State
```

同时：

```text
Upstream Change
!= Automatic Downstream Semantic Rewrite
```

正确链路：

```text
Authoritative Change
↓
Semantic Delta
↓
Affected Scope Resolution
↓
Dependency / Applicability Resolution
↓
Impact / Freshness Evidence
↓
Dependent State Re-evaluation
↓
Domain-owner Re-resolution
↓
New Effective State
```

---

## 3. Impact Detection Before Invalidation

不是任何 Revision 变化都会让全部下游 STALE。

必须判断：

- Semantic Delta；
- real dependency；
- Scope；
- Applicability；
- Current Effective provenance。

因此：

```text
Upstream Revision Changed != Invalidate All Downstream
Reference Exists != Material Impact Exists
Indexed Relation != Confirmed Semantic Impact
```

非语义 format / wording / metadata 变化不得默认引发全链失效。

---

## 4. Current Effective Freshness Contract

```text
Current Effective
```

不是 `Last Selected Forever`。

它必须保持：

```text
dependency-aware
applicability-aware
freshness-aware
scope-aware
```

同时：

```text
Any Upstream Change != Automatic Downstream Stale
```

只有 Relevant Semantic Dependency Changed 才要求重新判断。

---

## 5. Stale Semantics

正式提升：

```text
STALE != INVALID
STALE != DELETED
STALE != HISTORICALLY_INVALID
```

失效的是“当前有效资格”，不是历史事实。

旧 UI_SPEC / Binding / Effective Result 仍可以保留为历史批准制品、审计证据和过去执行解释依据。

```text
Invalidate Current Effectiveness
!= Delete Historical Artifact
```

---

## 6. Automatic Re-resolution

如果新的 Current Effective 结果可以由：

- Rule；
- Policy；
- Binding；
- Scope；
- Version；
- Authority；
- Applicability；

唯一确定，则允许：

```text
STALE
→ Automatic Re-resolution
→ New Effective Result
```

默认不打扰用户。

但：

```text
Auto Re-resolution != Auto Reauthorization
```

重新解析发现需要新增 DB / API / Scope / high-risk mutation 时，仍必须走对应 Gate。

---

## 7. Scope Boundary

正式冻结：

```text
Impact Discovery
!= Scope Expansion Authorization
```

当前任务只授权 `tenant-admin`，但 impact query 发现 `platform-admin` 也可能受影响时，可以产生 Impact Evidence，却不能自动把 `platform-admin` 纳入 mutation scope。

---

## 8. Domain-owner Routing

```text
Downstream Re-resolution
must route to the owning semantic domain
```

典型 Owner：

- F5 — Product semantic delta / requirement-side impact obligation；
- F6 — UI / Design re-interpretation / UI_SPEC current effective；
- F7 — durable semantic mutation / Canonical Apply；
- F8 — ProjectInstance / Binding / Profile / Provider / Version re-resolution；
- F9 — Index / Freshness / Impact / Evidence discovery；
- F10 — consume current context, pause affected execution on stale / mismatch, resume after re-resolution。

F9：

```text
Impact / Freshness Evidence
!= Semantic Authority
```

---

## 9. SQLite / Index Boundary

F9 / SQLite 未来可以高速索引：

- Stable ID / location；
- dependency / reverse reference；
- scope / applicability；
- revision / version；
- freshness；
- potential impact；
- owner stage；
- effective-result provenance。

但：

```text
SQLite Index != Canonical Truth
Relation Index != Semantic Authority
Impact Query != Mutation Authority
```

正确性能路径：

```text
Stable ID
→ Relation Index
→ Candidate Impact Set
→ Targeted Canonical Read
→ Resolver
```

不是默认全仓扫描或全局 cascade refresh。

---

## 10. Batch Auto-continuation Interaction

继承 `AUDIT-PATCH-007`：大型工作在合法 Batch Authorization Envelope 内可以自动连续执行。

如果执行期间出现 materially authoritative upstream change，必须重新判断未执行 Batch 的关键假设。

```text
Approved Batch Plan != Immutable Forever
```

确定性、不扩 Scope、不改变批准语义 / Authorization Envelope 的 re-plan 可自动完成；否则进入 HOLD / REVIEW_REQUIRED。

```text
Automatic Re-plan != Automatic Reauthorization
```

---

## 11. Historical Reproducibility

Effective State Transition 必须可追踪：

- 当时依赖什么 Revision；
- 使用什么 Binding / Version；
- 为什么成为 Current Effective；
- 后来为什么 STALE / SUPERSEDED。

历史对象不得因为当前失效被原地删除或重写。

---

## 12. Banyan-wide Invariants

```text
Upstream Change != Automatic Downstream Rewrite
Indexed Relation != Confirmed Semantic Impact
Impact Evidence != Mutation Authority
Stale != Invalid != Deleted
Current Effective must remain dependency/applicability/freshness/scope aware
Auto Re-resolution != Auto Reauthorization
Impact Discovery != Scope Expansion Authorization
Automatic Re-plan != Automatic Reauthorization
Detection Direction != Authority Direction
```

---

## 13. No-Loss / Compatibility

保留：

- F5 Requirement change → scoped downstream impact；
- F6 Effective UI Contract 状态模型；
- F7 STALE != INVALID / AUTO_REBASE != AUTO_REAUTHORIZE；
- F8 / F10 stale / mismatch feedback；
- F2 SQLite/index noncanonical；
- `AUDIT-PATCH-007` 的 bounded automatic continuation。

本 Patch 补上 upstream → downstream 主动 re-evaluation 的统一合同。

---

## 14. Forbidden Interpretations

禁止：

1. 上游一改就自动改写所有下游；
2. Revision 一变化就全项目 STALE；
3. Index relation 存在就证明必然有语义影响；
4. F9 / SQLite 获得 Domain Authority；
5. STALE 表示历史应删除；
6. Re-resolution 自动扩大 Scope；
7. Re-resolution 自动获得新的 Authorization；
8. Runtime mismatch 直接修改上游 Canonical Truth；
9. 局部 Requirement 变化默认全仓扫描；
10. 新建 Global Impact Authority Center。

---

## 15. Integration Target / Version Impact

未来整合目标：F5 / F6 / F7 / F8 的 freshness / impact / effective-state handoff，并向 F9 / F10 提供明确消费合同。

Exact runtime enum、SQLite schema、impact engine implementation 均延期到后续 Owner Stage。

F1～F8 v1.0 保持原文不变。

---

## 16. Human Decision

`B2-PATCH-03 HUMAN_APPROVED` 已完成：

```text
AUDIT-PATCH-008 = HUMAN_APPROVED
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

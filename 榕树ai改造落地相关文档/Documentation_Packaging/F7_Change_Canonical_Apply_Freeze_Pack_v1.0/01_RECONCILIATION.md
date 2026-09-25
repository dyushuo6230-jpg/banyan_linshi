# F7 Change / Canonical Apply — Final Reconciliation

## 0. Pack Identity

- Pack: `F7_Change_Canonical_Apply_Freeze_Pack_v1.0`
- Stage: `F7 — Change / Decision / Canonical Apply`
- Status: `ARCHITECTURE_FREEZE_PASS`
- Stage Closure: `PASS`
- Human Decisions: `F7-D01～D10` + `F7-FREEZE-CLOSURE-01` = `HUMAN_APPROVED / FROZEN`
- Cross-Stage Dependencies: `CROSS-STAGE-BOUNDARY-01`, `CROSS-STAGE-GOVERNANCE-02`, `CROSS-STAGE-DECISION-02`
- Pack grants Implementation Authority: `false`
- Pack grants RP2 Authority: `false`
- Pack grants Authority Cutover: `false`
- Pack grants Final Activation Authority: `false`

> 本文件是 F7 最终 Reconciliation / No-Loss / Conflict & Gap / Cross-Stage Handoff 的阶段冻结记录。
> 它是 Architecture Freeze，不是 Implementation Freeze，不因为自身存在而产生真实 Canonical Apply 或项目 Mutation 权限。

---

## 1. F7 为什么存在

F7 解决 Banyan 中“变化如何从非正式工作内容安全地成为正式 Canonical State”的治理问题。

它把以下概念正式拆开：

```text
Change Identity
Change Case
Change Workspace
Base State
Semantic Delta
Draft
Candidate
Working Revision
Human Decision
Approval
Apply Authorization
Apply Scope
Expected Base
Write Set
Apply Plan
Freshness
Divergence
Conflict
Impact
Reference Integrity
Canonical Apply
Apply Attempt
Atomicity
Technical Recovery
Stable ID
Canonical Revision
Supersession
Concurrent Change
Stale Draft
Semantic Rollback
Apply Result
Change Result
History
Closeout
Archive
```

F7 的目的不是制造更多人工确认，而是：

> **可靠自动路由 × 最小人工决策治理。**

能由 Rule / Boundary / Authority / Evidence 唯一解析的工作自动完成；只有真正需要 Human Judgment 的事项才进入知情决策。

---

## 2. Historical Four-Source Reconciliation

F7 使用四类历史源进行盘点：

### A. Old Human Discussions
用于恢复历史意图、已有约束、曾确认的使用体验和治理需求。

### B. Legacy v3.1
重点继承：
- 变更稿不是第二条正式写入路径；
- Approved / Baselined 内容不能被静默覆盖；
- 同主题修订升版本，历史保留；
- 已占用 ID 不得改挂另一主题；
- 被引用正式规则不得删除或整篇换题；
- 写入前检索引用；
- Draft 恢复保留 Draft，不删除历史；
- CURRENT_BASELINE 与 HISTORICAL_REFERENCE 分离。

### C. Accepted Refactor / Stage Evidence
重点继承：
- Change Workspace Provider-neutral；
- OpenSpec 只是第一个参考 Provider；
- Apply Preview / Impact / Reference / Authorization / Freshness / Checkpoint 必须分离；
- Last Write Wins / Latest File Wins 禁止；
- Canonical Apply 是受控事务语义；
- Protected Write 需要 Authorization / Freshness / Checkpoint / Audit；
- Trace / Audit 不授予 Authority。

### D. Current Framework Reality
当前已有：
- RuntimeAPI / PermissionEvaluator；
- CommitPlanner / CommitExecutor；
- Append-only Trace；
- Dry-run current-project execution；
- isolated fixture execution；
- per-commit-group checkpoint/recovery。

当前未完整实现：
- F7 Change Workspace Core；
- whole-plan Canonical Apply atomicity；
- Stable Semantic Entity / Revision registry；
- Reference-safe mutation transaction；
- Semantic Rollback；
- Change Closeout aggregation。

因此 Current Code 只能作为 Implementation Reality Evidence，不能反向定义 F7 Architecture。

---

## 3. Approved F7 Decision Set

### F7-D01 — Change Identity × Change Case × Change Workspace
冻结：
- Change Case 是受治理语义变化，不等于文件、Git、PR、OpenSpec、聊天；
- Stable Banyan Change ID 独立于 Provider / Path / Git；
- 一个 Change Case 对应一个 Logical Change Workspace；
- Workspace 不是 Canonical Truth；
- OpenSpec 是可替换 Provider；
- Change Registration 可以自动，但 Registration != Decision / Approval / Apply Authorization；
- duplicate / similarity 不允许静默 merge identity。

### F7-D02 — Base State × Reconciliation × Change Delta
冻结：
- Base State 与 Current State 分离；
- 多 Target 独立 Base Binding；
- ABSENT / UNKNOWN / UNRESOLVED 分离；
- changes_temp 只能进入 F7 Intake/Reconciliation，不是旁路；
- Semantic Delta != Text Diff；
- ADD / MODIFY / RETIRE / KEEP / NO_CHANGE / UNRESOLVED 作为开放语义；
- Not Mentioned != Delete；
- Boundary Crossing 是显式 reconciliation 结果；
- Gap Discovery != Permission To Invent Authority。

### F7-D03 — Draft × Candidate × Working Revision
冻结：
- Draft 非 Canonical、可修改；
- Candidate 是同 Change Intent 下的有意义方案；
- Working Revision 是 Candidate 的语义演进快照；
- Draft 不能静默扩 Change Scope；
- AI 可自动生成/改进 Draft，但 Draft Generation != Decision；
- AI 可推荐 Candidate，但 Recommendation != Human Decision；
- Rejected / Superseded Candidate 保留历史；
- Selected Candidate != Canonical Truth / Apply Authorization。

### F7-D04 — Decision × Approval × Apply Authorization
冻结：
```text
Decision != Approval != Apply Authorization != Runtime Permission
```
并明确：
- Governance Routing first；
- Clear natural language 可在 Authority/Scope/Gate 满足时成为 Evidence；
- silence / cancellation / AI recommendation / ambiguous preference 不能充当确认；
- Role / Provider / Editor / Git identity 不授予 Authority；
- Apply Authorization 可来自显式授权或受治理 Policy；
- High Risk != Automatic Human Confirmation；
- F7 消费全局 Informed Decision Protocol，不自造另一套。

### F7-D05 — Apply Scope × Expected Base × Write Set × Apply Plan
冻结：
```text
Change Scope != Apply Scope != Authorization Scope
Change Base State != Apply Expected Base
Semantic Delta != Write Set != Impact Set
Apply Plan != Apply Authorization != Canonical Apply
```
并明确：
- Expected Base 按 Target 绑定；
- CREATE 的 Expected Base 可为 ABSENT；
- Hidden Write 禁止；
- Apply Plan Provider-neutral；
- Authorization 可绑定 bounded envelope 或具体 Plan Revision；
- Partial Apply 只允许满足 Minimum Coherent Apply Boundary；
- D-number != Runtime fixed sequence。

### F7-D06 — Freshness × Conflict × Impact × Reference Check
冻结：
```text
Freshness != mtime
Divergence != Conflict
Divergence != Human Decision Required
UNKNOWN != NO_IMPACT
UNKNOWN != Ask Human Immediately
POTENTIAL != DIRECT
```
并明确：
- deterministic reconciliation 默认自动；
- unresolved semantic auto-merge 禁止；
- Last / Latest Wins 禁止；
- Governance Freshness 与 Content Freshness 分离；
- Conflict 必须路由 Owner；
- Reference Check 发现义务，完整 Reference Mutation 由 D08；
- Auto Replan != Auto Reauthorize。

### F7-D07 — Canonical Apply × Atomicity × Partial Failure Recovery
冻结：
```text
Canonical Apply != File Write != Git Commit != DB Transaction
Apply Plan != Apply Attempt
Mutation Completed != Canonical Apply Succeeded
Physical Mutation != Canonical Acceptance
Technical Recovery != Semantic Rollback
```
并明确：
- Final Pre-Mutation Guard；
- Checkpoint before reversible protected mutation；
- one Apply Plan 默认一个 Semantic Atomicity Boundary；
- Provider capability 必须满足 Atomicity Requirement；
- Actual Mutation Set 必须匹配 Resolved Write Set；
- Post-Mutation Validation / Reconciliation 是 Apply 成功的一部分；
- Retry 形成新 Attempt，有限且受治理。

### F7-D08 — Stable ID × Revision × Reference Integrity × Supersession
冻结：
```text
Stable ID != Revision
Path / Provider Change != Subject Change
Stable ID Reuse = FORBIDDEN
Latest Revision != Current Effective Revision
Revision Lineage != Supersession
Superseded != Deleted
Reference != Authority
Historical Reference != Broken Reference
```
并明确：
- Stable ID 标识 Semantic Subject；
- Subject Change → New Stable ID；
- Working Revision != Canonical Revision；
- Semantic Reference 与 Revision-Pinned Reference 分离；
- Reference Migration 是语义操作，不是字符串替换；
- Reference Mutation 必须进入 D05 Write Set；
- Derived Index / SQLite / Trace Graph 不拥有 Reference Truth。

### F7-D09 — Concurrent Change × Stale Draft × Reconciliation
冻结：
```text
Concurrent Change != Conflict
Stale != Invalid
Stale != Human Decision Required
Reconciliation != Semantic Merge
Auto Rebase != Auto Reauthorize
Multiple Candidates != Automatic Informed Decision
Provider Lock != Governance Authority
```
并明确：
- 并发不靠全局串行化解决；
- deterministic rebase 默认自动；
- unresolved semantic merge 禁止；
- Parallel Draft / Candidate 合法存在；
- Canonical Acceptance 后相关未完成 Plan 重新评估；
- Partial Conflict 默认只阻塞 interaction scope；
- Provider lock 只能协调执行，不能决定语义 winner。

### F7-D10 — Rollback × Recovery × History × Apply Result × Closeout
冻结：
```text
Technical Recovery != Semantic Rollback != Compensating Change != Data Restoration
Semantic Rollback != Restore Old Bytes
Rollback != History Erasure
Apply Attempt Result != Apply Result != Change Result
Executor Success != Canonical Apply Accepted
Canonical Apply Accepted != Whole Change Closed
Closed != Archived
Archive != Delete
```
并明确：
- Semantic Rollback 是 Governed Canonical Transition；
- rollback target 必须重新做 freshness / reference / impact / authority validation；
- NO_CHANGE / REJECTED / CANCELLED / SUPERSEDED 均可合法 Close；
- Closeout 按 Required Obligations 判断；
- History 保留事件演进，不只保留最终 Snapshot；
- 不可逆 Effect 只能显式记录 residual effect / compensation。

---

## 4. Stage Freeze Closure

`F7-FREEZE-CLOSURE-01` 冻结 12 条收口锁：

```text
FC-01  D-number != Runtime Call Order
FC-02  F9 Freshness/Impact Evidence != F7 Apply Governance
FC-03  F8 Project Reconcile != F7 Change Reconcile
FC-04  F7 Canonical Apply Governance != F10 Runtime Execution
FC-05  Execution Rollback Policy != Semantic Rollback Decision Authority
FC-06  Post-Close Semantic Rollback → New Change Case
FC-07  Pre-Close rollback may remain in same Change only for same unfinished obligation
FC-08  Reactivate Prior Revision != Rewrite Revision History
FC-09  Current Effective transition must remain traceable
FC-10  F7 state/results remain derived from governed facts
FC-11  Cross-plan / cross-target coordination must be declared before execution
FC-12  Cross-stage Owner Matrix is authoritative for handoff
```

---

## 5. Cross-Stage Frozen Dependencies

F7 依赖但不拥有：

### CROSS-STAGE-BOUNDARY-01
- Boundary Definition 与 Effective Boundary 分离；
- Boundary Crossing != Permission；
- Design Space Boundary != Authority；
- F7 是边界需要合法改变时的 governed channel 之一，不拥有所有 Boundary。

### CROSS-STAGE-GOVERNANCE-02
- Reliable Autonomous Routing × Minimal Human Decision Governance；
- AI Uncertainty != Ask Human Immediately；
- Model Confidence != Authority；
- High Risk != Automatic Human Interruption；
- deterministic governed work 默认自动。

### CROSS-STAGE-DECISION-02
- Informed Decision 是 Banyan-wide Human Governance Protocol；
- Governance Resolution first；
- 用户明确要求知情决策时必须拉起；
- Informed Decision invocation != Authority / Approval / Apply Authorization。

---

## 6. Cross-Stage Owner Matrix

```text
F5  = Product Meaning Authority
F6  = UI / Design Truth Authority
F7  = Governed Change + Canonical Apply Governance
F8  = Project Instance / Binding / Project Reconcile
F9  = Index / Search / Freshness Evidence / Impact Query
F10 = Runtime Permission / Provider Adapter / Execution Enforcement
F11 = WebUI / Control Plane / Governance UX
F12 = Legacy Reconciliation / Migration / Retirement Program
```

Capability / Evidence / Runtime Provider 不因“能查、能执行、能写”而获得 Semantic Authority。

---

## 7. No-Loss / Conflict / Gap Audit

```text
Unmapped F7 Decision = 0
Unmapped Closure Lock = 0
Competing Change Truth = 0
Competing Canonical Apply Authority = 0
Runtime Permission promoted to Semantic Authority = 0
Reference Truth promoted from Index/SQLite = 0
Hidden Write allowed path = 0
Last/Latest Wins path = 0
Silent semantic auto-merge path = 0
Unbounded retry path = 0
Closed Change ID reuse path = 0
Rollback history erasure path = 0
Blocking F7 Architecture Conflict = 0
```

---

## 8. Final Stage Conclusion

```text
F7-D01～D10 = HUMAN_APPROVED / FROZEN
F7-FREEZE-CLOSURE-01 = HUMAN_APPROVED / FROZEN

F7 Stage Architecture Freeze = PASS

Implementation = NOT AUTHORIZED
RP2 = NOT AUTHORIZED
Authority Cutover = NOT AUTHORIZED
Final Activation = NOT AUTHORIZED
```

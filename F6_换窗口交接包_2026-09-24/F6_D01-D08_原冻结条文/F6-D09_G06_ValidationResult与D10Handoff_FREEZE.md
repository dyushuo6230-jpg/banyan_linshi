# F6-D09 — G06 Validation Result × Report × D10 Handoff 冻结条文

- **Stage**: F6
- **Decision**: F6-D09
- **Group**: 06
- **Status**: HUMAN_APPROVED
- **Freeze Status**: Architecture Freeze PASS
- **Type**: UI Conformance / Validation Result & Handoff Governance
- **Date**: 2026-09-24

## 1. Validation Result 必须是结构化结果

D09 最终输出不得只有：

```text
PASS
```

Validation Result 至少应能够关联：

- Session ID
- Target Ref
- Target Version / Freshness
- Scope
- Coverage
- Actual Evidence Refs
- Findings
- Difference / Drift Classification
- Regression Findings
- Risk
- Affected Scope
- Unresolved Items
- Provider Trace
- Decision Refs
- Session Status

这样后续的：

- D10；
- Human Decision；
- Audit；
- Revalidation；

才能明确：

> 某个 Validation Result 是在什么 Target、Scope、Coverage、Evidence 与风险条件下成立。

---

## 2. Validation Result 是 Evidence，不是新的 Canonical Truth

正式冻结：

```text
Validation Result
!=
UI_SPEC

Validation Result
!=
Design Package

Validation Result
!=
PRD

Validation Result
!=
Canonical Product Truth
```

D09 可以发现：

- Current Implementation 与 Target 冲突；
- Target 可能已经过期；
- Design Source 存在冲突；
- Protected Functional Baseline 可能过期；
- Evidence 不足；
- Scope / Coverage 不完整。

但只能输出：

```text
Evidence
Gap
Conflict
Review Required
```

不得自动：

```text
Validation Result
→ Rewrite UI_SPEC
```

也不得自动修改：

- Design Package
- PRD
- Canonical Product Truth
- Frozen Contract

Validation Result 可以触发治理，但不能替代治理。

---

## 3. Session Result 与单个 Issue Result 必须分离

一轮 Session 中，每个 Issue 可以拥有独立结果。

例如：

```text
D09-ISSUE-001 = PASS
D09-ISSUE-002 = LEGAL_ALTERNATIVE
D09-ISSUE-003 = DRIFT
D09-ISSUE-004 = UNKNOWN
D09-ISSUE-005 = PERMISSION_REGRESSION
```

不得因为多数 Issue 没有问题，就自动把整个 Session 判定为 PASS。

Session Result 必须综合：

- Coverage
- Unresolved Items
- Blocked Scope
- Regression Result
- Target Readiness
- Evidence Sufficiency

Session Status 的治理语义至少应支持：

```text
PASS
PARTIAL_PASS
FAIL
BLOCKED
NOT_READY
UNKNOWN
COMPLETED_WITH_UNRESOLVED
```

具体物理 Enum 可留待 Implementation Freeze 再确定，但这些语义边界必须保留。

---

## 4. D09 报告必须区分 Finding 与 Repair Instruction

D09 可以输出：

- Finding
- Classification
- Evidence
- Risk
- Affected Scope
- Governance Route

例如可以说明：

```text
该 Issue 需要进入 D10 Review
```

但不得因为发现 Drift 或 Regression，就在 D09 中自动产生：

- 修改授权；
- Repair Instruction；
- 自动修复指令；
- 文件修改清单；
- 代码重写方案；
- 共享组件修改许可。

正式冻结：

```text
Finding
!=
Repair Instruction
```

并继续遵守：

```text
Risk
!=
Authority
```

---

## 5. D09 → D10 必须按具体 Issue / Scope 交接

D09 Handoff 必须：

```text
Issue-bound
Scope-bound
Evidence-bound
Risk-aware
```

例如：

```text
D09-ISSUE-001 = R1 Visual Drift
D09-ISSUE-002 = Legal Alternative
D09-ISSUE-003 = R2 Shared Component Risk
D09-ISSUE-004 = R3 Permission Regression
```

则可以形成：

```text
Eligible for D10 Review:
001
003
004

No Repair Needed:
002
```

不得直接形成：

```text
“把这一轮发现的问题全部修掉”
```

即使某 Issue 被交给 D10：

```text
Eligible for D10 Review
!=
Authorized to Modify
```

D10 仍必须依据自己的修改边界、授权规则和治理条件继续判断。

D09 Handoff 本身不产生 Mutation Authority。

---

## 6. Session 必须明确结束，不得自动进入 Repair 或下一轮

一轮 D09 Session 的完整闭环：

```text
启动UI一致性校准会话
↓
Target Resolution
↓
Scope Resolution
↓
Actual Evidence
↓
Difference / Drift Classification
↓
Regression Validation
↓
Validation Result
↓
Final Report
↓
SESSION CLOSED
```

在 Final Report 输出并完成 Session Closure 后：

```text
不得自动进入 D10 Repair
不得自动修改代码
不得自动开启下一轮 Session
```

如需修复：

```text
D09 Report
↓
User / Governance Decision
↓
D10
```

如需再次校准，则必须重新满足 G01 的显式启动条件，并再次使用固定关键词：

> **启动UI 一致性校准会话**

正式闭环：

```text
Explicit Start
→ Bounded Validation
→ Explicit Result
→ Explicit Stop
```

禁止：

```text
Start
→ Inspect
→ Repair
→ Inspect
→ Repair
→ 无限循环
```

---

## 7. G06 正式收口链

```text
D09 Findings
↓
Issue-level Result
↓
Session-level Result
↓
Final Validation Report
↓
Issue / Scope / Evidence / Risk Handoff
↓
SESSION CLOSED
↓
等待新的明确 Governance / Human Decision
```

---

## 8. 核心冻结边界

G06 正式冻结：

```text
Validation Result
!=
Canonical Truth

Session Result
!=
Single Issue Result

Finding
!=
Repair Instruction

D09 Handoff
!=
Mutation Authorization

Eligible for D10 Review
!=
Authorized to Modify

Final Report
→
SESSION CLOSED
```

---

## 9. 冻结结论

本组正式冻结：

1. Validation Result 必须结构化；
2. Validation Result 必须记录其 Target、Scope、Coverage、Evidence、Finding、Risk 与 Trace；
3. Validation Result 是 Evidence，不是新的 Canonical Truth；
4. Validation Result 不得自动改写 UI_SPEC、Design Package 或 PRD；
5. Session Result 与单个 Issue Result 必须分离；
6. Session Result 必须综合 Coverage、Unresolved、Blocked Scope、Regression、Target Readiness 与 Evidence Sufficiency；
7. D09 Finding 与 Repair Instruction 必须分离；
8. Risk 不产生修改 Authority；
9. D09 → D10 Handoff 必须绑定具体 Issue、Scope、Evidence 与 Risk；
10. Eligible for D10 Review 不等于 Authorized to Modify；
11. D09 Handoff 不产生 Mutation Authority；
12. Final Report 输出后 Session 必须明确关闭；
13. D09 不得自动进入 D10 Repair；
14. D09 不得自动修改代码；
15. D09 不得自动开启下一轮 Session；
16. 新一轮 UI 一致性校准必须重新满足 G01 的固定口令启动条件。

---

**HUMAN_APPROVED — 2026-09-24**

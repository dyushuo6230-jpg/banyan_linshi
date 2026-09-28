# F9-D05 — Context Recovery

**中文名称：上下文恢复**

---

## 0. 文档身份

| 项目 | 内容 |
|---|---|
| Stage | F9 — Index / Projection / Cache Architecture |
| Decision | F9-D05 |
| 名称 | Context Recovery |
| 中文名称 | 上下文恢复 |
| 当前状态 | `HUMAN_APPROVED` |
| 精确批准语句 | `F9-D05 HUMAN_APPROVED` |
| 前置批准 | `F9-G01 HUMAN_APPROVED` |
| 前置批准 | `F9-D01 HUMAN_APPROVED` |
| 前置批准 | `F9-D02 HUMAN_APPROVED` |
| 前置批准 | `F9-D03 HUMAN_APPROVED` |
| 前置批准 | `F9-D04 HUMAN_APPROVED` |
| 上游正式架构基线 | F1～F8 v1.1 Architecture Freeze Baseline |
| Implementation | `NOT_AUTHORIZED` |
| RP2 | `NOT_AUTHORIZED` |
| Authority Cutover | `NOT_AUTHORIZED` |
| Canonical Replacement | `NOT_AUTHORIZED` |
| Final Activation | `NOT_AUTHORIZED` |
| Legacy Retirement | `NOT_AUTHORIZED` |
| SQLite Physical Schema | `NOT_FROZEN` |

---

## 1. 决策目标

F9-D05 解决：

> 当当前任务需要的 Context Package（上下文包）丢失、不完整、过期、被清理、跨 Session / Window（会话 / 窗口）继续、跨 Role / Consumer（角色 / 消费者）交接，或 Material Context（实质上下文）无法直接取得时，F9 如何在不创造新 Truth、不扩大 Scope、不篡改 Authority 的前提下，恢复足以继续当前任务的最小充分上下文。

D05 恢复的是：

```text
Task-scoped Context View
```

不是：

```text
Canonical Truth
Domain Truth
Authority
Permission
Governance Winner
```

正式冻结：

```text
Context Missing
!= Truth Missing

Context Recovery
!= Canonical Truth Recovery

Recovered Context
!= New Canonical Source
```

---

## 2. Minimum Sufficient Recovery

D05正式采用：

## Minimum Sufficient Recovery
**最小充分恢复**

即：

> 只恢复当前 Task / Query 安全继续所需的最小实质上下文，不要求重新加载全部历史、全部旧聊天或全部旧 Context Package。

正式冻结：

```text
Recovery Complete
!= Full History Reloaded

Recovery Complete
!= Previous Package Fully Reproduced
```

恢复同样继承 D04：

```text
Stop When Materially Sufficient
```

---

## 3. Recovery 与 AI Memory 分离

模型记忆、会话回忆、AI Summary 可以辅助：

- Navigation；
- Candidate Discovery；
- Source Re-location；
- Recovery Hint。

但不能单独形成 Governed Recovery Result。

正式冻结：

```text
Context Recovery
!= AI Memory Recall

Model Memory
!= Governed Recovery Evidence

Conversation Recall
!= Canonical Source
```

---

## 4. Recovery 场景

D05至少覆盖以下逻辑恢复场景：

- Context Package Lost；
- Partial Context Loss；
- Context Item Missing；
- Cache Eviction；
- Session / Window Change；
- Consumer / Role Handoff；
- Source Relocation；
- Material Context Stale；
- Source Temporarily Unavailable；
- Previous Context Snapshot Recovery；
- Continuation Resume。

具体物理 enum 不冻结。

---

## 5. Recovery 分层

D05采用分层恢复思想：

```text
Valid Context Snapshot Reuse
↓
Context Item Rehydration
↓
Local Repair
↓
Derived Layer Rebuild
↓
Governed Source Recovery
↓
Context Reconstruction
↓
D03 Re-resolution
```

原则：

> 能局部恢复就不重建整包；能重建 Context 就不重新解析整个 Query；只有 Material Resolution Basis 真正变化时才回 D03。

正式冻结：

## Minimum Necessary Recovery Escalation
**最小必要恢复升级**

---

## 6. Recovery != Re-resolution

若以下 Material Resolution Basis 未变化：

- Project；
- Scope；
- Profile；
- Temporal；
- Domain Role；
- Protection；
- Query Purpose；

则属于 Context Recovery。

若其中实质变化，则必须返回 D03。

正式冻结：

```text
Recovery
!= Query Re-resolution

Missing Context
→ Recovery

Changed Material Resolution Basis
→ D03 Re-resolution
```

---

## 7. Recovery Anchor

D05引入逻辑：

## Recovery Anchor
**恢复锚点**

用于在 Context Package 不存在时重新定位当前任务。

Recovery Anchor 可包含：

- Program / Project Identity；
- Stage Identity；
- Task / Query Reference；
- Subject Stable ID；
- Scope Reference；
- Profile Reference；
- Temporal Mode；
- Source Role；
- Source Locator；
- Revision / Version / Effective Reference；
- Protection Basis；
- Provenance；
- Previous Coverage；
- Approved Decision References；
- Critical Guards。

具体 Schema 不冻结。

正式冻结：

```text
Recovery Anchor
!= Canonical Truth Copy

Recovery Anchor
!= Eternal Continuation State
```

---

## 8. Identity-anchored Recovery

恢复应优先依赖稳定语义身份，而不是单一 Path、文件名或相似度。

正式冻结：

```text
Path Change
!= Subject Identity Change

Locator Missing
!= Subject Missing

Similarity Match
!= Recovery Identity
```

Stable ID 恢复仍必须结合：

```text
Scope
Temporal / Revision
Profile / Applicability
```

不能只凭 ID 忽略 Current / Historical 差异。

---

## 9. Recovery Source Strategy

恢复来源的可用性由以下共同决定：

```text
Query Purpose
Domain Role
Source Role
Scope
Temporal
Authority Basis
Freshness
Protection
```

不采用：

```text
Latest File Wins
Search Rank Wins
Similarity Wins
Occurrence Count Wins
```

作为万能恢复规则。

---

## 10. Recovery Source 逻辑角色

恢复来源逻辑上至少区分：

### Governed / Effective Source
用于恢复正式适用语义。

### Validated Derived Evidence
例如 Validated Projection、Validated Snapshot、Validated Index View，用于加速恢复。

### Recovery / Navigation Evidence
例如 Handover、Checkpoint、Manifest、Context Semantic Envelope，用于定位和连续工作恢复。

### Weak Discovery Evidence
例如 AI Summary、Conversation Recall、Model Memory、Semantic Candidate，仅用于候选发现。

具体 enum 不冻结。

正式冻结：

```text
Weak Recovery Evidence
must not gain stronger semantic authority
```

---

## 11. Handover / Continuation Artifact 边界

Handover、Checkpoint、Start Prompt、Manifest 等可以帮助：

- 恢复 Stage；
- 恢复当前 Decision；
- 恢复 Next Step；
- 恢复 Source References；
- 恢复 Guards；
- 恢复 Package Coverage。

但：

```text
Handover Artifact
!= Frozen Decision Authority

Handover
!= Canonical Replacement

Handover Convenience
!= Governance Authority
```

如果 Handover 与正式 HUMAN_APPROVED / Frozen Source 冲突，必须以适用正式来源为准。

---

## 12. Approval State 不得被 Recovery 升级

正式冻结：

```text
Discussion
!= HUMAN_APPROVED

Handover Summary
!= HUMAN_APPROVED Evidence

Recovery Summary
!= Replacement Canonical Decision
```

如果恢复材料声称某 Decision 已批准，但找不到适用 HUMAN_APPROVED 依据，则 Approval State 必须保持：

```text
UNVERIFIED / UNRESOLVED
```

而不能自动升级。

---

## 13. Progressive Recovery

D05采用：

## Progressive Recovery
**渐进式恢复**

恢复可从：

```text
Recovery Anchor
↓
Checkpoint / Metadata
↓
Approved Decision Reference
↓
Relevant Material Section
↓
Governed Source
```

逐级深入。

正式冻结：

```text
Recovery Expansion
must be material-need-driven
and bounded
```

---

## 14. Recovery Scope 不得静默扩大

正式冻结：

```text
Recovery Failure
!= Scope Expansion Authorization

Cross-scope Discovery
!= Primary Recovery Success
```

如果 Project A 的恢复失败，Project B 的类似资料只能作为 Exploratory Evidence，不能冒充 Project A 的恢复结果。

---

## 15. Previous Context Snapshot 的定位

Previous Context Snapshot 可以作为：

- Recovery Accelerator；
- Comparison Basis；
- Fallback Evidence；
- Previous Coverage Evidence；
- Frontier Reference。

但：

```text
Previous Context Snapshot
!= Current Truth

Last Known Snapshot
!= Current Authoritative Truth
```

---

## 16. Degraded Recovery

D05允许：

## Degraded Recovery
**降级恢复**

当正式 Source 暂时不可用，但存在可追溯的 Last Validated Snapshot / Projection / Cache 时，可在适用任务中有限继续。

必须保留：

- Recovery Basis；
- Source Role；
- Last Validated Revision / Version；
- Observed Time；
- Current Revalidation State；
- Freshness Limitation；
- Protection Basis；
- Degradation Basis。

正式冻结：

```text
Source Unavailable
!= Cache Becomes Canonical

Degraded
!= Current Reconfirmed
```

---

## 17. Partial 与 Degraded 分离

正式冻结：

```text
Partial Recovery
!= Degraded Recovery
```

Partial 表示：

> 缺 Material Context。

Degraded 表示：

> Context 有，但 Current / Freshness / Validation 能力降低。

二者可以同时存在。

---

## 18. Degraded Continuation 的适用条件

Degraded Recovery 是否可继续，必须综合：

- Query Purpose；
- Required Authority；
- Freshness Requirement；
- Risk / Governance Consequence；
- Protection；
- Provenance；
- Claim Strength。

正式冻结：

```text
Fallback Available
!= Fallback Usable

Degraded Continuation
is purpose-relative
```

---

## 19. 必须 BLOCK 的场景

以下情形不得通过弱证据静默继续：

- 当前任务必须确认 Current Authority，但 Current Authority 无法验证；
- Governed Identity 无法可靠解析；
- Material Protection 无法验证；
- Multiple Governed Candidates 无 deterministic winner；
- Required Effective Result 不可获得；
- Recovery 需要改变 Scope / Profile / Temporal；
- Source Lineage 已断；
- 弱证据会影响高风险或不可逆动作。

原则：

> 不能把“未知”包装成“已知”。

---

## 20. Protection 必须在 Recovery 时重新应用

正式冻结：

```text
Previously Visible
!= Currently Recoverable

Previously Recoverable
!= Currently Authorized

Recovery Eligibility
is consumer-relative
```

Consumer / Role 变化后必须重新检查 Protection。

Recovery 不得利用旧 Cache / Snapshot 绕过新的访问边界。

---

## 21. Protection-aware Explainability

如果某 Protected Subject 的存在本身敏感，则 Recovery Result 也不得泄漏其存在。

正式冻结：

```text
Recovery Explainability
must be protection-aware
```

---

## 22. Recovery Material Obligations

D05恢复的目标不只是正文。

必须恢复当前任务需要的：

- Material Truth；
- Material Guard；
- Material Conflict；
- Material Unknown；
- Material Unresolved；
- Material Coverage；
- Applicability Context；
- Required Provenance。

正式冻结：

```text
Recovery
must restore material guards

Recovery
must preserve material conflict

Recovery
must preserve material unknown
```

---

## 23. Recovery Coverage

D05复用 D04 Material Coverage 思想，不建立第二套独立 Truth Model。

Recovery Completeness 按：

```text
Material Obligations
```

判断，而不是：

```text
Token Count
Byte Count
Item Count
File Count
```

正式冻结：

```text
Recovery Completeness
is obligation-based
not byte-based
```

---

## 24. Recovery Success 是 Purpose-relative

同一恢复结果：

```text
Product = recovered
Design = recovered
Code = unavailable
```

对于 Product Lookup 可能已经足够。

对于 Product / Code Consistency Analysis 则仍为 Partial。

正式冻结：

```text
Recovery Success
is purpose-relative
```

---

## 25. Recovery Reconciliation

多个恢复来源不一致时：

```text
Recovery Reconciliation
!= Majority Vote

Recovery Reconciliation
!= Latest File Wins

Recovery Reconciliation
!= Search Rank Wins
```

首先判断是否处于同一：

- Subject Identity；
- Scope；
- Temporal；
- Revision；
- Domain Role；
- Source Role；
- Profile / Applicability。

---

## 26. Different Value 不等于 Conflict

以下可能是合法差异：

```text
Tenant A != Tenant B
R5 != R6
Normative != Observed
Current != Historical
```

所以：

```text
Different Value
!= Recovery Conflict
```

只有语义坐标可比较时，才判断 Recovery Discrepancy。

---

## 27. Recovery Evidence Set

允许逻辑：

## Recovery Evidence Set
**恢复证据集合**

用于聚合一个 Material Subject 的：

- Governed Source；
- Previous Snapshot；
- Projection；
- Handover；
- Observed Evidence；
- Recovery Metadata。

但：

```text
Recovery Evidence Set
!= Canonical Truth
```

---

## 28. Governed Effective Result 优先被消费

如果上游已经解析：

```text
Current Effective Result
```

D05直接消费该结果恢复 Context。

正式冻结：

```text
Recovery Reconciliation
!= Authority Resolution
```

D05不得重新选择 Governance Winner。

---

## 29. Stale 与 Historically Invalid 分离

正式冻结：

```text
Stale For Current Use
!= Historically Invalid
```

旧 Snapshot 在生成时可能完全正确，只是今天不能继续作为 Current。

---

## 30. Derived-layer Repair

如果：

```text
Canonical Basis unchanged
+
Derived Projection / Snapshot mismatch
```

则优先视为：

```text
Derived-layer Repair Candidate
```

可以执行：

```text
invalidate
→ rebuild
→ retry
```

正式冻结：

```text
Derived Mismatch
!= Canonical Error
```

---

## 31. Material Semantic Equivalence

恢复对账不要求字节相同。

正式冻结：

```text
Text Difference
!= Semantic Change

Small Text Difference
!= Small Semantic Difference
```

恢复比较应保护 D04 已冻结的 Material Semantic Atoms：

- 数值；
- 阈值；
- MUST / MUST NOT / MAY；
- Scope；
- Temporal；
- Owner；
- Authority；
- Conflict；
- Unknown；
- Guard。

---

## 32. D05 与 D07 的边界

D05负责：

```text
detect recovery inconsistency
```

D07负责：

```text
fingerprint
change evidence
invalidation trigger
```

正式冻结：

```text
D05
!= Change Detection Engine
```

---

## 33. Recovery Difference 分类

恢复差异逻辑上至少应区分：

- Expected Temporal Difference；
- Expected Scope Difference；
- Expected Role Difference；
- Derived-layer Mismatch；
- Governed Conflict；
- Identity Ambiguity；
- Unknown Cause。

具体 enum 不冻结。

---

## 34. Cross-role Divergence 不是 Recovery Corruption

正式冻结：

```text
Cross-role Divergence
!= Recovery Corruption
```

例如：

```text
Requirement = 500
Code = 1000
```

可能是真实业务 / 实现偏差。

D05不得为了“恢复一致”而把 Code 改成 500。

---

## 35. Recovery 自动修复边界

F9可以自动：

- Stable ID relocation；
- Known Source reload；
- Context rehydration；
- Index / Projection rebuild；
- Derived Cache repair；
- Local Material Repair；
- Coverage reconstruction；
- Protection-aware projection；
- Traceable Summary regeneration；
- bounded retry。

F9不得自动：

- Guess Governed Identity；
- Choose Authority Winner；
- Override Protection；
- Change Scope；
- Change Profile Applicability；
- Promote Historical Snapshot to Current；
- Resolve Governance Conflict；
- Upgrade Approval State。

---

## 36. Evidence Count 不等于 Authority

正式冻结：

```text
Evidence Count
!= Independent Authority Count

Repeated Derived Evidence
!= Stronger Truth
```

必须通过 Lineage 识别多个 Summary / Projection 是否来自同一祖先，防止虚假多数。

---

## 37. Recovery Discrepancy Record

允许逻辑：

## Recovery Discrepancy Record
**恢复差异记录**

可记录：

- Affected Subject；
- Scope；
- Temporal；
- Evidence A / B；
- Difference Type；
- Lineage；
- Authority Basis；
- Resolution State；
- Affected Coverage。

但：

```text
Recovery Discrepancy Record
!= Canonical Conflict Truth
```

---

## 38. Branch Failure 局部化

正式冻结：

```text
Recovery Branch Failure
!= Global Recovery Failure
```

D05应输出受影响的 Material Coverage，再由 D04判断：

```text
Context Sufficient?
```

正式责任边界：

```text
D05 reports recovery coverage
D04 decides context sufficiency
```

---

## 39. Local Repair

当以下成立时优先 Local Repair：

- Query Resolution Basis 未变；
- Subject Identity 明确；
- 影响局部；
- Protection 未变；
- Lineage 清晰；
- 其他 Material Context 仍 coherent。

Local Repair 后必须重新评估：

- affected dependents；
- Conflict；
- Coverage；
- Freshness；
- Snapshot Coherence。

---

## 40. Context Reconstruction

以下情况应升级为 Context Reconstruction：

- 大量 Context Item 丢失；
- 多个 Material Branch stale；
- Lineage 大面积不明；
- Context Snapshot Coherence 已破坏；
- 原 Context Package 已无法安全局部修复。

重建应基于：

```text
valid D03 Query Plan
→ Retrieval
→ D04 Assembly
```

---

## 41. D03 Re-resolution

以下发生 Material Change 时必须返回 D03：

- Project；
- Scope；
- Profile；
- Temporal；
- Protection；
- Query Purpose；
- Domain Role。

正式冻结：

```text
Local Repair
→ Context Reconstruction
→ D03 Re-resolution
```

按影响边界逐级升级。

---

## 42. Recovery Retry 必须 Cause-aware

正式冻结：

```text
Recovery Retry
must be cause-aware
```

若 Derived Rebuild 后差异消失，可继续。

若仍然是上游 Governed Conflict：

```text
stop repeated rebuild
→ route to applicable Owner / Resolver
```

禁止无限：

```text
invalidate
rebuild
invalidate
rebuild
```

---

## 43. Snapshot Coherence

恢复后必须维持 D04 的 Snapshot Coherence。

但不要求所有 Source 时间戳完全一致。

要求的是：

> Temporal / Freshness 差异不得造成当前 Query 的 Material Semantic Ambiguity，或必须被明确标识。

---

## 44. Degradation Basis

Degraded Recovery 必须保留：

```text
why degraded
```

例如：

- Source unavailable；
- Current revalidation unavailable；
- Freshness uncertain；
- Partial lineage；
- Restricted source inaccessible。

正式冻结：

```text
Degraded State
must retain degradation basis
```

---

## 45. No Universal Recovery Score

D05不建立：

```text
Recovery Quality Score = 87
```

之类万能评分。

正式冻结：

```text
No single universal recovery quality score
```

Authority、Freshness、Coverage、Protection、Conflict 必须保持多维状态。

---

## 46. UNKNOWN 是合法恢复结果

正式冻结：

```text
Unknown Recovery Cause
!= Permission To Guess
```

当无法确定：

```text
Source changed?
or
Derived cache corrupted?
```

可以保持 UNKNOWN，并根据风险决定重建、请求 D07 Evidence 或停止。

---

## 47. Continuation State

D05引入逻辑：

## Continuation State
**连续工作状态**

用于表达：

- Program / Project；
- Stage；
- Approved Decisions；
- Current Working Decision；
- Current Working State；
- Next Step；
- Critical Guards；
- Applicable Baseline；
- Recovery Basis。

正式冻结：

```text
Continuation State
!= Governance Authority
```

---

## 48. New Session 与 Continuation

正式冻结：

```text
New Session
!= New Governance Task

Same Project
!= Same Continuation State
```

跨 Session / Window 必须恢复可验证 Continuation State。

---

## 49. Recovery Anchor / Continuation State / Context Package 三层分离

正式冻结：

```text
Recovery Anchor
↓
Continuation State
↓
Context Package
```

- Anchor：定位；
- Continuation State：恢复工作位置；
- Context Package：当前 Consumer 真正工作上下文。

---

## 50. Continuation Package

D05正式定位：

## Continuation Package
**连续工作交接包**

用于跨 Session / Consumer 提供恢复入口。

逻辑上至少应能够恢复：

- Program / Project Identity；
- Stage Identity；
- Approved Decision References；
- Current Working Decision；
- Current Working State；
- Next Step；
- Critical Guards；
- Applicable Baseline；
- Source / Repository Pointers；
- Package Coverage；
- Recovery Instructions。

具体 ZIP 结构和文件名不冻结。

正式冻结：

```text
Continuation Package
!= Canonical Replacement
```

---

## 51. Next Step 必须重新解析

正式冻结：

```text
Handover Next Step
!= Automatically Current Next Step
```

Next Step 必须结合：

```text
Current Approved State
+
Current Working State
+
Applicable Roadmap
```

重新确认。

---

## 52. 多个 Continuation Package

多个 Package 不得仅通过：

- 文件名；
- 版本号；
- 修改时间；

选择 Current。

必须依据：

- Coverage；
- Source Lineage；
- Supersession；
- Approved References；
- Generation Basis。

正式冻结：

```text
Newer Package Name
!= Governed Supersession
```

---

## 53. Superseded Package

旧 Package 可以保留用于：

- History；
- Audit；
- Recovery Debugging。

但：

```text
Superseded Package
!= Current Continuation State
```

---

## 54. Single Logical Current

正式冻结：

```text
Multiple Active Sessions
!= Multiple Current Governance States
```

同一治理链应能解析出单一 Logical Current Continuation State。

但不冻结：

- Distributed Lock；
- Database Lock；
- Lease；
- Session Token。

正式冻结：

```text
Single Logical Current
!= Frozen Physical Lock Mechanism
```

---

## 55. Checkpoint 生成时机

建议在以下 Material Event 生成新 Checkpoint：

- HUMAN_APPROVED；
- Stage Boundary；
- Material Working Topic Change；
- New-window Handoff；
- Major Recovery Boundary Change；
- 旧 Checkpoint 已会实质误导 Continuation。

不要求每一个讨论小步骤生成永久 Artifact。

---

## 56. Checkpoint 不得升级 Governance State

正式冻结：

```text
Continuation Metadata
must not upgrade Governance State
```

没有 HUMAN_APPROVED 正式依据时，不得从 Checkpoint 恢复成已批准。

---

## 57. Recovery Completion

D05正式采用：

## Recovery Completion
**恢复完成**

当以下对当前 Purpose 足够时，可判定恢复完成：

- Current Task Identity 已解析；
- Current Continuation State 已解析；
- Required Query / Scope Basis 已恢复；
- Required Approved Boundaries 已恢复；
- Material Guards 已恢复；
- Material Recovery Coverage 足够；
- Protection 已验证；
- Temporal / Current / Historical 语义清楚；
- 无阻塞当前 Purpose 的 Material Recovery Gap。

---

## 58. Recovery Complete != Context Ready

正式冻结：

```text
Recovery Complete
!= Context Ready
```

链路：

```text
D05 Recovery Complete
↓
D04 Context Assembly / Sufficiency
↓
Context Ready
```

---

## 59. Recovery Complete != Runtime Authorized

正式冻结：

```text
Recovery Complete
!= Runtime Authorized

Context Ready
!= Runtime Authorized
```

恢复成功不产生 Implementation / Mutation / Runtime Permission。

---

## 60. Recovery Completion Basis

Recovery Completion 必须可解释。

至少应能够说明：

- 恢复了哪些正式边界；
- 依据哪些 Source；
- 哪些是 Current；
- 哪些是 Degraded；
- 哪些仍 Partial；
- 为什么当前可以继续。

正式冻结：

```text
Recovery Completion
must be explainable
```

---

## 61. Safe Continuation Point

当精确工作进度无法验证时，引入：

## Safe Continuation Point
**安全继续点**

即：

> 最近一个 fully verified、non-ambiguous、governed continuation point。

正式冻结：

```text
Unknown Exact Progress
→ Recover to Safe Continuation Point
```

禁止根据 AI印象猜测“上次大概做到哪里”。

---

## 62. Package Coverage

Continuation Package 必须表达自己覆盖到哪里。

正式冻结：

```text
Package Omission
!= Governance Absence
```

包里没有某 Decision，不代表它不存在，只代表该 Package 未覆盖。

---

## 63. Manifest 与 Checksum

Manifest 用于：

```text
Package Coverage Evidence
```

但：

```text
Manifest
!= Decision Authority
```

Checksum 用于：

```text
Integrity Evidence
```

但：

```text
Integrity Evidence
!= Semantic Validity
```

---

## 64. Cross-session Semantic Envelope

跨 Session Handoff 必须继续保留 D04 已冻结的 Context Semantic Envelope 中的 Material 信息，包括：

- Scope；
- Profile；
- Temporal；
- Domain / Source Role；
- Protection；
- Coverage；
- Conflict；
- Unknown；
- Guards；
- Provenance；
- Current Working State。

---

## 65. Recovery Artifact 的生命周期

恢复完成后：

```text
Handover / Checkpoint / Recovery Artifact
```

应回到：

```text
Navigation / Bootstrapping Evidence
```

角色。

正式冻结：

```text
Recovery Artifact
is bootstrapping evidence
not permanent reasoning center
```

正常推理应重新基于：

```text
Governed Source
+
Current Context
```

---

## 66. Recovery 是 Event-driven

正式冻结：

```text
Recovery
is event-driven
not permanently active
```

典型 Trigger：

- Context Loss；
- Session Change；
- Cache Eviction；
- Consumer Handoff；
- Material Context Missing；
- Material Stale Context；
- Source Relocation；
- Continuation Resume。

没有 Recovery Trigger 时，不持续执行完整恢复流程。

---

## 67. D05 与 D04 的最终边界

D05：

```text
Recover required context inputs
```

D04：

```text
Select / assemble / evaluate context sufficiency
```

正式冻结：

```text
Recovery Success
!= Context Sufficiency by itself
```

---

## 68. D05 与 D06 的最终边界

D05向 D06提供：

- Recovery Result；
- Recovery Basis；
- Recovered Source References；
- Degraded / Partial State；
- Freshness-related Metadata；
- Unresolved Freshness Questions。

D06负责：

- Freshness Evaluation；
- Revalidation；
- Currentness 判断。

正式冻结：

```text
D05 recovers context

D06 evaluates freshness
```

---

## 69. D05 与 D08 的边界

D05只处理：

```text
Recovery-local dependency
Context-local affected dependents
```

D08处理：

```text
Global Dependency / Impact Discovery
```

正式冻结：

```text
Recovery-local Dependency
!= Global Impact Discovery
```

---

## 70. D05 与 D09 的边界

D05冻结：

- Recovery semantics；
- Recovery escalation；
- Snapshot / Cache fallback boundary；
- Local Repair / Reconstruction boundary。

D09后续冻结：

- Cache Provider；
- Storage；
- Rebuild mechanism；
- Retry implementation；
- Physical invalidation / cache behavior。

---

## 71. 自动化边界

F9 / AI 可以自动：

- Stable ID relocation；
- known source reload；
- context item rehydration；
- local derived repair；
- index / projection rebuild；
- recovery coverage reconstruction；
- protection-aware projection；
- source lineage tracing；
- discrepancy detection；
- bounded retry；
- degraded-state labeling；
- safe continuation reconstruction；
- checkpoint coverage validation。

F9 / AI 不得自动：

- Guess Governed Identity；
- Choose Governance Winner；
- Upgrade Approval State；
- Expand Scope without D03；
- Treat stale Snapshot as Current Truth；
- Override Protection；
- Promote Recovery Summary to Canonical Truth；
- Resolve unresolved Authority Conflict；
- Treat Recovery Complete as Runtime Permission。

---

## 72. 核心不变量

```text
Context Missing != Truth Missing
Context Recovery != Canonical Truth Recovery
Recovered Context != New Canonical Source
Recovery Complete != Full History Reloaded
Recovery Complete != Previous Package Fully Reproduced
Context Recovery != AI Memory Recall
Model Memory != Governed Recovery Evidence
Recovery != Query Re-resolution
Path Change != Subject Identity Change
Similarity Match != Recovery Identity
Recovery Anchor != Canonical Truth Copy
Handover Artifact != Frozen Decision Authority
Discussion != HUMAN_APPROVED
Handover Summary != HUMAN_APPROVED Evidence
Recovery Failure != Scope Expansion Authorization
Previous Context Snapshot != Current Truth
Last Known Snapshot != Current Authoritative Truth
Source Unavailable != Cache Becomes Canonical
Partial Recovery != Degraded Recovery
Fallback Available != Fallback Usable
Different Value != Recovery Conflict
Recovery Evidence Set != Canonical Truth
Recovery Reconciliation != Authority Resolution
Stale For Current Use != Historically Invalid
Derived Mismatch != Canonical Error
Text Difference != Semantic Change
Cross-role Divergence != Recovery Corruption
Evidence Count != Independent Authority Count
Recovery Branch Failure != Global Recovery Failure
Recovery-local Dependency != Global Impact Discovery
Unknown Recovery Cause != Permission To Guess
Continuation State != Governance Authority
Continuation Package != Canonical Replacement
Handover Next Step != Automatically Current Next Step
Multiple Active Sessions != Multiple Current Governance States
Recovery Complete != Context Ready
Recovery Complete != Runtime Authorized
Package Omission != Governance Absence
Manifest != Decision Authority
Integrity Evidence != Semantic Validity
```

---

## 73. Acceptance Gates

F9-D05 Architecture Freeze 只有在以下全部成立时才可 PASS：

1. Context Recovery 与 Truth Recovery 明确分离。
2. Minimum Sufficient Recovery 成立。
3. AI Memory 不作为 Governed Recovery Authority。
4. Recovery Anchor / Continuation State / Context Package 三层分离。
5. Recovery 优先基于 Stable Identity，而非 Path / Similarity。
6. Recovery 与 D03 Re-resolution 边界清楚。
7. Handover / Checkpoint 不获得 Decision Authority。
8. Recovery 不升级 Approval State。
9. Progressive Recovery 有界。
10. Recovery Scope 不得静默扩大。
11. Previous Snapshot / Cache 不成为 Current Truth。
12. Degraded 与 Partial 明确分离。
13. Degraded Continuation 为 Purpose-relative。
14. Protection 在 Recovery 时重新应用。
15. Recovery Explainability 保护敏感存在性。
16. Material Guard / Conflict / Unknown / Coverage 在 Recovery 中恢复。
17. Recovery Completeness 按 Material Obligation 判断。
18. 多来源对账不采用多数票 / Latest / Search Rank。
19. Different Value 不自动判定 Conflict。
20. Governed Effective Result 由 D05消费而非重新裁决。
21. Derived Mismatch 优先修 Derived Layer。
22. Cross-role Divergence 不被 Recovery Repair 抹平。
23. Evidence Lineage 可识别虚假多数。
24. Branch Failure 优先局部化。
25. Local Repair / Context Reconstruction / D03 Re-resolution 升级链成立。
26. Recovery Retry Cause-aware 且有界。
27. Continuation State 不成为 Governance Authority。
28. 多 Continuation Package 依据 Coverage / Lineage / Supersession 解析。
29. Multiple Sessions 不产生 Multiple Current Governance State。
30. Checkpoint 不升级 Approval State。
31. Recovery Completion 为 Purpose-relative、Obligation-based。
32. 精确进度无法恢复时回退 Safe Continuation Point。
33. Package Coverage 可解释。
34. Manifest / Checksum 语义边界清楚。
35. Recovery Artifact 恢复完成后退回 Bootstrapping Role。
36. Recovery 为 Event-driven。
37. Recovery Complete 与 Context Ready 分离。
38. Recovery Complete 与 Runtime Authorized 分离。
39. D05 未吞并 D06 Freshness Evaluation。
40. D05 未吞并 D07 Change Detection。
41. D05 未吞并 D08 Global Impact Discovery。
42. D05 未冻结 D09 Cache / Storage 物理实现。
43. Implementation、RP2、Authority Cutover、Canonical Replacement、Final Activation、Legacy Retirement 仍未授权。
44. SQLite Physical Schema 仍为 `NOT_FROZEN`。

---

## 74. Final Owner Boundary

```text
Upstream Domain Owner
→ owns semantic truth

F8
→ owns Project / Binding /
   Effective Project / Profile semantics

F9-D03
→ owns Query Resolution /
   Search-space boundary

F9-D04
→ owns Context Selection /
   Assembly /
   Coverage /
   Sufficiency

F9-D05
→ owns Context Recovery /
   Continuation Recovery /
   Recovery Escalation /
   Degraded Recovery Boundary /
   Recovery Handoff Semantics

F9-D06
→ owns Freshness Evaluation /
   Revalidation

F9-D07
→ owns Fingerprint /
   Change Detection /
   Invalidation Trigger

F9-D08
→ owns Global Dependency /
   Impact Discovery

F9-D09
→ owns Cache /
   Projection /
   Rebuild implementation behavior
```

---

## 75. Architecture Closure

F9-D05 冻结后的恢复链为：

```text
Recovery Trigger
↓
Resolve Task / Consumer
↓
Recovery Anchor
↓
Continuation State
↓
Material Recovery Obligations
↓
Recovery Source Selection
↓
Progressive Recovery
↓
Multi-source Reconciliation
↓
Local Repair
   or Context Reconstruction
   or D03 Re-resolution
↓
Protection Re-evaluation
↓
Recovery Coverage
↓
Safe Continuation Point
↓
Recovery Completion
↓
D04 Context Assembly / Sufficiency
↓
D06 Freshness Evaluation
```

---

## 76. Final Decision

F9-D05 最终确定：

> Banyan F9 的 Context Recovery 不依赖 AI 模糊记忆，也不把旧 Context Package、Cache、Handover 或 Summary 当作新的 Truth。Recovery 必须围绕稳定身份、适用 Scope、Temporal、Profile、Protection、Source Role、Authority Basis 和 Provenance 进行。

> D05采用 Minimum Sufficient Recovery，只恢复当前任务安全继续所需的实质上下文，而不要求重放全部历史或完整复制旧 Context Package。

> Recovery 与 Re-resolution 严格分离。Context 缺失、局部失效、Cache Eviction、Session Change 等进入 D05；Project、Scope、Profile、Temporal、Protection、Query Purpose 等 Material Resolution Basis 变化时必须返回 D03。

> D05允许 Validated Snapshot、Projection、Cache、Handover 等作为恢复加速器或降级证据，但 Source Unavailable 不会使 Cache 成为 Canonical Truth，Last Known Snapshot 不会自动成为 Current Authoritative Truth。

> Degraded Recovery 可以支持适用的低风险连续工作，但必须显式保留 Degradation Basis、Freshness Limitation、Validation State 和 Claim Boundary。若当前任务要求无法验证的 Current Authority、Protection 或 Governed Identity，则必须 BLOCK，而不是静默 fallback。

> Recovery Reconciliation 不采用多数票、最新文件、搜索排名或出现次数决定 Truth。不同 Scope、Temporal、Domain Role 的值不自动构成 Conflict。上游 Governed Effective Result 已明确时，D05消费该结果；若是 Derived Layer 与正式 Source 不一致，则优先修复派生层。

> D05采用 Local Repair → Context Reconstruction → D03 Re-resolution 的最小必要恢复升级链，并要求 Recovery Retry Cause-aware、有界、可解释。

> Continuation State、Recovery Anchor 和 Continuation Package 只用于可靠恢复连续工作，不获得 Governance Authority。HUMAN_APPROVED、Frozen Decision 和正式 Source 的 Authority 不得被 Handover、Checkpoint、Manifest 或 AI Summary 替代。

> 跨窗口恢复必须重新解析 Current Continuation State、Current Approved State、Critical Guards 和 Next Step。精确进度无法验证时，必须回退到 Safe Continuation Point，而不是根据 AI 印象猜测。

> Recovery Complete 只表示当前任务所需恢复输入已足够，不等于 Context Ready，更不等于 Runtime Authorized。恢复完成后由 D04重新完成 Context Assembly / Sufficiency 判断，再由 D06负责 Freshness Evaluation。

---

## 77. HUMAN_APPROVED Effect

本文件已经获得：

```text
F9-D05 HUMAN_APPROVED
```

因此：

```text
Context Recovery Boundary
= ARCHITECTURALLY_FROZEN

Recovery Anchor Boundary
= ARCHITECTURALLY_FROZEN

Continuation State Boundary
= ARCHITECTURALLY_FROZEN

Recovery Source Strategy
= ARCHITECTURALLY_FROZEN

Degraded Recovery Boundary
= ARCHITECTURALLY_FROZEN

Recovery Reconciliation Boundary
= ARCHITECTURALLY_FROZEN

Local Repair / Reconstruction / Re-resolution Boundary
= ARCHITECTURALLY_FROZEN

Cross-session Continuation Boundary
= ARCHITECTURALLY_FROZEN

Recovery Completion / Handoff Boundary
= ARCHITECTURALLY_FROZEN
```

但仍然：

```text
F9 Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

`F9-D05 HUMAN_APPROVED` 只表示 Context Recovery 架构语义冻结，不代表任何 Recovery Engine、Cache、Storage、Watcher、Session System、Database Schema、Runtime、Agent、Prompt 或代码实现获得施工授权。

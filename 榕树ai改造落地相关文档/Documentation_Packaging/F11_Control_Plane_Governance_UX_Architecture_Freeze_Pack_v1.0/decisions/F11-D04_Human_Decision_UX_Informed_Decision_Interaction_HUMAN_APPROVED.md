# F11-D04 — Human Decision UX & Informed Decision Interaction
## 人工决策体验与知情决策交互

**Stage：** F11 — Control Plane / Governance UX Architecture（控制面 / 治理交互架构）  
**Decision ID：** F11-D04  

**Upstream：**
- F11-G01 = HUMAN_APPROVED / FROZEN
- F11-D01 = HUMAN_APPROVED / FROZEN
- F11-D02 = HUMAN_APPROVED / FROZEN
- F11-D03 = HUMAN_APPROVED / FROZEN

**Status：** HUMAN_APPROVED / FROZEN

**Implementation Authorization：** NO  
**RP2 Authorization：** NO  
**Authority Cutover Authorization：** NO  
**Canonical Replacement Authorization：** NO  
**Final Activation Authorization：** NO  
**Legacy Retirement Authorization：** NO  

---

# 1. 决策目标

F11-D04 用于冻结 Banyan Control Plane 中 Human Decision（人工治理决策）的交互边界。

本 Decision 回答：

```text
什么时候真的需要人做决定？

什么时候系统应继续自动解析，而不打扰用户？

F11 如何把一个 Human Decision Requirement
转换成用户可以理解的知情决策交互？

用户至少应该看到哪些信息？

多个候选方案如何过滤为真正值得选择的 Alternative？

AI Recommendation 可以做到什么程度？

Default / Preference / Historical Choice
分别是什么？

用户明确选择以后，
为什么还不等于正式 Governed Decision？

Decision Basis 变化以后怎么办？

Stale / Superseded /
No Longer Required 如何处理？

Human Decision 完成后，
系统如何重新解析后续 Scope /
Authority / Gate / Runtime Context？

以及 F11 如何避免成为
Decision Authority / Apply Authority /
Runtime Authority。
```

---

# 2. F11 不创建 Human Decision Requirement

F11-D04 正式冻结：

```text
F11 presents Human Decision Requirement.

F11 does not invent Human Decision Requirement.
```

是否真正需要人工判断，应由：

```text
DecisionProtocol

Applicable Domain Governance

Scope / Authority / Gate rules

Workflow / Runtime governance escalation
```

等正式规则和 Owner 决定。

不得因为：

```text
AI 不确定

页面信息很多

系统暂时失败

出现多个 Candidate
```

就自动创建 Human Decision Requirement。

---

# 3. 自动解析优先

Banyan 的默认方向仍然是：

```text
Deterministic Resolution
↓
Existing Rules
↓
Recovery / Fallback
↓
Authority / Scope / Gate Resolution
↓
Governance Routing
↓
Human Decision only when
genuine unresolved judgment remains
```

该流程不是固定机械步骤。

如果规则已经明确：

```text
Human Decision Required
```

可以直接进入人工决策。

---

# 4. Operational Failure 不等于 Human Decision

正式：

```text
Operational Failure
!= Human Decision Required
```

例如：

```text
network timeout

provider transient failure

temporary service unavailable

transport interruption
```

应优先进入：

```text
retry

fallback

re-query

re-route

technical recovery
```

而不是把用户作为默认错误处理器。

---

# 5. Technical Uncertainty 不等于 Human Decision

正式：

```text
Technical Uncertainty
!= Human Decision Required
```

例如：

```text
当前 Projection 暂时未知

系统重启后关联关系尚未恢复

部分 Trace 尚未加载
```

首先进入：

```text
refresh

recover

re-resolve

inspect state / evidence / trace
```

不能要求用户猜测系统技术状态。

---

# 6. Missing Context 不自动等于 Human Input Required

Context 缺失时应优先：

```text
recover context

load required source

resolve owner

rebuild projection
```

只有该缺失内容本身必须由人类价值判断产生时，才进入 Human Decision。

正式：

```text
Missing Context
!= Human Input Required by default.
```

---

# 7. Multiple Candidates 不等于 Human Decision

系统发现多个 Candidate 时，应优先：

```text
remove invalid candidates

collapse semantically equivalent candidates

remove dominated candidates

apply existing Policy / Preference

perform deterministic routing
```

只有剩余：

```text
multiple legitimate
materially different alternatives
```

且现有规则无法唯一解析时，才形成真正 Human Decision Requirement。

因此：

```text
Multiple Candidates
!= Human Decision Required
```

---

# 8. 真正需要人工决策的典型条件

Human Decision Requirement 可以出现在：

```text
Material Scope Expansion

Unresolved Authority Conflict

Governed Exception

High-impact irreversible governance choice

Multiple legitimate materially different paths
that existing rules cannot uniquely resolve
```

这些是典型条件，不构成封闭 Enum。

---

# 9. Technical Alternative 与 Material Alternative 分离

例如：

```text
Provider A

Provider B
```

如果：

```text
Semantic Result unchanged
Scope unchanged
Authority unchanged
Governance consequence unchanged
```

则只是 Technical Alternative。

正式：

```text
Technical Alternative
!= Material Decision Alternative
```

不得仅因为技术路径不同就占用人工决策。

---

# 10. Candidate 与 Decision Alternative 分离

正式：

```text
Candidate
!= Valid Decision Alternative
```

只有经过治理解析后仍然：

```text
valid
legitimate
materially distinct
decision-relevant
```

的方案才应展示给用户。

---

# 11. Implementation Difference 不自动成为 Decision Difference

正式：

```text
Implementation Difference
without Material Governance Difference
!= Human Decision Alternative
```

不同代码结构、Provider、Adapter 或底层技术路径，如果没有改变治理意义，不应自动升级为人工选择。

---

# 12. Human Decision 的基本结构

一个 HumanDecisionInteraction 逻辑上应能够组织：

```text
Decision Requirement

Decision Subject

Decision Question

Decision Basis

Valid Alternatives

Material Differences

Consequences / Impact

Optional Recommendation

Explicit GovernanceDecisionInput
```

这是逻辑模型，不是固定 DTO 或页面布局。

---

# 13. Decision Requirement

Decision Requirement 回答：

> 为什么系统现在不能自动继续？

例如：

```text
现有批准 Scope 无法覆盖新增影响范围。

存在两个均合法、
但长期结果明显不同的方案。

当前 Authority 冲突没有既有规则可以唯一消解。
```

正式：

```text
Decision Requirement
!= Decision Question
```

---

# 14. Decision Question

Decision Question 回答：

> 现在具体需要用户决定什么？

例如：

```text
是否允许当前 Change
扩大到 shared component
以及 platform-admin？
```

Decision Requirement 和 Decision Question 不得混为一体。

---

# 15. Decision Subject

所有 Governance Decision 必须绑定清晰 Subject。

例如：

```text
Change C100

Action A17

Project Instance P3

Configuration Profile CP2
```

正式：

```text
Governance Decision
must remain Subject-bound.
```

不得只呈现：

```text
请选择 A / B
```

而不说明正在决定什么对象。

---

# 16. Decision Basis

Decision Basis 表示：

> 用户当前做出这个决策时依赖的实质事实、规则、Scope、Impact 和治理上下文。

Decision Input 必须能够解释：

```text
这个选择是针对哪一版
Material Decision Context 做出的。
```

正式：

```text
Human Decision
must remain interpretable
against the Material Decision Basis
presented to the human.
```

---

# 17. Informed Decision 不等于最大信息量

知情决策不要求一次加载所有：

```text
Trace

Repository Diff

Dependency Graph

Evidence Store

Runtime History
```

正式：

```text
Informed Decision
!= Maximum Information
```

推荐方向：

```text
Informed Decision
= Minimum Sufficient Material Context
```

即只加载做出当前治理判断所必需的实质信息。

---

# 18. 信息压缩不得损失实质差异

允许摘要和 Progressive Disclosure（渐进展开）。

但：

```text
Decision Summary
may compress detail

but must preserve Material Difference.
```

不能为了简洁隐藏：

```text
Scope Expansion

Authority impact

Irreversibility

Major downstream impact

Deferred Obligation
```

等真正影响选择的内容。

---

# 19. Decision Detail Importance 与技术信息量分离

正式：

```text
Decision Detail Importance
!= Technical Detail Volume
```

一个只有两行说明的 Scope Expansion 可能比几百行技术 Diff 更值得进入决策核心区。

---

# 20. Material Difference 逻辑维度

Decision Interaction 可按需组织以下 Material Difference：

```text
Scope Impact

Authority / Governance Impact

Semantic / Result Impact

Downstream Impact

Risk / Uncertainty

Reversibility

Deferred Obligation

Material Operational / Cost Impact
```

该集合用于指导比较，但不是每个 Decision 必须机械填满所有维度。

---

# 21. Scope Impact

当 Alternatives 的治理 Scope 存在实质差异时，应明确展示。

例如：

```text
Alternative A:
tenant-admin only

Alternative B:
shared component
+ tenant-admin
+ platform-admin
```

正式：

```text
Material Scope Difference
must be visible.
```

---

# 22. Path Count 不等于 Scope Meaning

例如：

```text
3 files → 17 files
```

只是技术数量变化。

真正需要表达的是：

```text
tenant-admin
→ shared component + platform-admin
```

因此：

```text
Path Count
!= Scope Meaning
```

---

# 23. Authority / Governance Impact

若某方案会：

```text
require broader authority

introduce new Gate

require additional governance condition
```

应明确展示。

但：

```text
Authority Impact
!= Authority Transfer by default
```

只有真正 Authority Owner 变化时才能称为 Authority Transfer。

---

# 24. Semantic / Result Impact

如果 Alternatives 会改变：

```text
business meaning

future behavior

shared rule semantics

canonical result
```

这些差异必须展示。

正式：

```text
Implementation Difference
may be hidden.

Material Semantic Difference
must not be hidden.
```

---

# 25. Downstream Impact

Downstream Impact 应支持：

```text
Summary
↓
Drill-down
```

例如第一层：

```text
platform-admin affected

3 shared modules affected

12 pages require validation
```

需要时再展开完整 Dependency / Impact 信息。

正式：

```text
Downstream Impact
should support Summary → Drill-down.
```

---

# 26. Material Impact 不能被聚合隐藏

即使存在大量 Downstream 项，也不得因为：

```text
只显示 Top N
```

而隐藏真正 Material Impact。

正式：

```text
Material Impact
must not be hidden by aggregation.
```

---

# 27. Risk 与 Reversibility 分离

Risk 表示：

> 哪些不确定性或负面后果可能发生？

Reversibility 表示：

> 选择后能否安全恢复或撤销？

正式：

```text
Risk
!= Reversibility
```

---

# 28. Risk Label 必须有治理依据

D04 不默认创建：

```text
LOW
MEDIUM
HIGH
83/100
```

等 Risk Score。

正式：

```text
Risk Label
requires governed basis.
```

若没有正式风险模型，应优先展示具体 Risk Fact / Concern。

---

# 29. Known Consequence 与 Risk 分离

例如：

```text
B 必然影响 platform-admin
```

属于：

```text
Known Consequence
```

而：

```text
B 可能增加回归风险
```

属于 Risk / Inference。

正式：

```text
Known Consequence
!= Risk

Known Impact
!= Predicted Possibility
```

---

# 30. Reversibility

当 Alternatives 可逆性存在 Material Difference 时，应明确展示。

例如：

```text
A:
remove local override to rollback

B:
requires coordinated shared-component rollback
```

正式：

```text
Material Reversibility Difference
must be visible.
```

Exact Reversibility Enum 不在 D04 冻结。

---

# 31. Deferred Obligation

当一个选择会创建、修改或解除明确 Deferred Obligation 时，该义务属于 Material Decision Consequence。

正式：

```text
Deferred Obligation
is a Material Decision Consequence
when choice creates or changes one.
```

---

# 32. Deferred Obligation 必须可执行、可追踪

不推荐模糊描述：

```text
增加技术债
```

应优先说明：

```text
未来何时需要处理

需要处理什么

由哪个 Trigger / Context 重新发现

影响哪些对象
```

正式：

```text
Deferred Obligation
must remain actionable and traceable
when known.
```

---

# 33. Immediate Consequence 与 Deferred Obligation 分离

正式：

```text
Immediate Consequence
!= Deferred Obligation
```

Human Decision UX 应允许区分：

```text
现在立即发生什么

未来因此必须承担什么义务
```

---

# 34. Cost / Effort 信息必须有 Basis

如果 Material Decision 确实与：

```text
time

cost

operational effort

validation burden
```

相关，可以展示。

但：

```text
Cost / Effort Claim
must remain Basis-backed.
```

没有可靠估算时不得伪造 ETA 或精确成本。

---

# 35. Decision Information Architecture 不等于固定 UI

Web / CLI / IDE / API 可以使用不同展示方式。

正式：

```text
Decision Information Architecture
!= Fixed UI Layout
```

D04 不冻结：

```text
Modal
Drawer
Card
Radio
Button position
Color
```

---

# 36. Core Decision View

推荐第一层优先回答：

```text
为什么现在需要你决定？

你具体在决定什么？

有哪些真正合法方案？

这些方案会造成哪些实质不同结果？

系统是否有 Recommendation？
```

---

# 37. Detail View

第二层可以包含：

```text
Scope details

Authority / Gate details

Downstream Impact

Risk basis

Reversibility

Deferred Obligations

Material operational impact
```

---

# 38. Evidence Drill-down

第三层可进入：

```text
Evidence

Trace

Provenance

Full Dependency / Impact References
```

具体 Evidence Presentation 由 F11-D06 进一步治理。

---

# 39. Recommendation 的定位

AI Recommendation 是：

> 基于当前 Decision Basis、规则和 Material Differences 给出的辅助建议。

正式：

```text
AI Recommendation
!= Human Decision
```

---

# 40. Recommendation 必须 Basis-backed

正式：

```text
AI Recommendation
must remain Basis-backed.
```

Recommendation 应能够解释：

```text
为什么推荐

基于哪些规则 / Preference / Evidence

主要收益

主要代价

主要反向证据
```

---

# 41. Recommendation 不得抹掉反向证据

正式：

```text
Recommendation
must not erase Material Countervailing Evidence.
```

例如推荐 B 时，仍需展示：

```text
B expands scope

B requires broader validation
```

等关键代价。

---

# 42. Recommendation Rationale 区分事实与推断

正式：

```text
Recommendation Rationale
must distinguish Fact from Inference.
```

不得把：

```text
“可能更易维护”
```

包装成：

```text
“维护成本一定更低”
```

---

# 43. Recommendation 可以不存在

正式：

```text
Recommendation Presence
is optional.
```

如果当前证据无法可靠推荐：

```text
No Reliable Recommendation
```

本身就是合法结果。

---

# 44. Recommendation 不等于 Default

正式：

```text
Recommendation
!= Default
```

AI 推荐 B 不表示：

```text
用户不操作时自动选择 B
```

---

# 45. Default 的定位

Default 是：

> 在没有 Human Decision Input 时，由正式治理规则预定义的系统行为。

例如：

```text
deadline passed
→ keep current state
```

如果是正式规则，则属于：

```text
Governed Default Behavior
```

而不是用户决定。

正式：

```text
Default Applied
!= Human Decision
```

---

# 46. Default Presentation 不等于 Human Decision

即使 UI 默认把某项放在第一位，也不能记录成用户选择。

正式：

```text
Default Presentation
!= Human Decision
```

---

# 47. Recommendation Highlight 不等于 Explicit Selection

UI 可以标记：

```text
Recommended
```

但：

```text
Recommendation Highlight
!= Explicit Selection
```

在用户未明确选择前：

```text
selected = NONE
```

仍然可能是正确语义。

---

# 48. Preference 的定位

Preference 是：

> 用户、项目或治理 Profile 过去明确配置并由正式 Owner 管理的可复用选择偏好。

如果 Preference 在当前场景：

```text
legally applicable

sufficiently specific

does not cross governance boundary
```

它可以参与 Automatic Resolution。

---

# 49. Applicable Preference 可以消除 Human Decision

正式：

```text
Applicable Governed Preference
may eliminate Human Decision Requirement.
```

如果规则和 Preference 已经足以唯一合法地自动决定：

> 就不要再创建 Human Decision Requirement。

---

# 50. Preference 不等于 Blanket Authorization

例如：

```text
Prefer shared component reuse
```

不能被解释为：

```text
自动批准任何 Scope Expansion
```

正式：

```text
Preference
!= Blanket Authorization
```

---

# 51. Human Decision 已经存在时 Preference 不得伪装成决定

如果 Human Decision Requirement 仍然成立，说明现有 Preference 不足以完整解决当前选择。

因此：

```text
If existing Preference can deterministically
and legitimately resolve the choice,
Human Decision should not be created.

If Human Decision still exists,
Preference must not masquerade as the Decision.
```

---

# 52. Historical Choice 的定位

Historical Choice 只是：

> 过去某个特定 Decision Basis 下发生过的选择事实。

正式：

```text
Historical Choice
!= Standing Preference
```

---

# 53. 重复历史选择也不自动生成 Preference

正式：

```text
Repeated Historical Choice
!= Preference
```

F11 不得：

```text
观察用户连续三次选 B
→ 推断以后自动 B
```

---

# 54. Historical Choice 可以用于解释

允许：

```text
Historical Choice
may inform explanation
```

例如：

> 类似 Decision D12 曾选择共享方案。

但：

```text
Historical Choice
does not become Decision Authority.
```

---

# 55. Historical Consistency Signal

系统可以提示：

> 当前选择与之前相关 Decision 不一致。

但：

```text
Historical Consistency Signal
!= Governance Prohibition
```

除非正式治理规则明确要求一致。

---

# 56. Explicit Preference Declaration

如果用户明确表达：

> 以后符合这些条件时都按 B 处理。

则可以路由至：

```text
Preference Definition / Update
```

正式：

```text
Explicit Preference Declaration
may create governed Preference
through its owning mechanism.
```

D04 不拥有完整 Preference Definition 模型。

---

# 57. Recommendation 可以引用 Preference

正式：

```text
Recommendation
may use governed Preference as Basis.
```

但应明确说明：

```text
Recommendation Basis:
Preference P17
```

不能隐藏 Preference 来源。

---

# 58. Historical Choice 不能直接驱动 Recommendation Authority

Historical Choice 可以成为辅助 Context。

但当前 Recommendation 仍必须基于：

```text
current Decision Basis

current Material Differences

current applicable rules
```

而不是：

```text
“你上次选了 B，所以这次也应该 B。”
```

---

# 59. 一键选择 Recommendation

UX 可以提供：

```text
选择推荐方案 B
```

但必须由用户明确触发。

正式：

```text
One-click Recommended Selection
may be valid UX

but must remain Explicit Human Input.
```

---

# 60. AI 不代替 Human Decision

如果 Governance Requirement 明确：

```text
Human Decision Required
```

则：

```text
AI Recommendation
!= Delegated Human Decision by default.
```

当前阶段不存在默认 AI Delegation Governance。

---

# 61. 自动可解决的选择不应伪造成 Human Decision

正式：

```text
Automatically Resolvable Choice
should remain Automatic Resolution,
not Synthetic Human Decision.
```

系统可以自动完成的，就不要：

```text
先制造 Human Decision
再让 AI 替用户点
```

---

# 62. Explicit Human Input

Human Decision 必须来自可识别的明确输入。

正式：

```text
Silence
!= Human Decision

Dismiss
!= Human Decision

Timeout
!= Human Decision

Acknowledge
!= Human Decision
```

---

# 63. Defer 不等于 Decision

用户：

```text
稍后处理
```

只表示延后 Interaction。

正式：

```text
Defer
!= Decision
```

Decision Requirement 可以继续存在。

---

# 64. 合法“不继续”必须成为明确 Alternative

如果：

```text
不继续当前 Change
```

本身是一种合法 Governance Choice，

则应作为明确 Alternative 展示。

正式：

```text
Valid Refusal / No-change Choice
must be represented as explicit Alternative
when it carries governance meaning.
```

不得使用关闭弹窗代替。

---

# 65. UI Confirmation Event 不等于 Decision Meaning

用户点击：

```text
确认
```

只是交互动作。

真正 GovernanceDecisionInput 应表达：

```text
selected Alternative

Decision Basis

Decision Subject
```

正式：

```text
UI Confirmation Event
!= Governance Decision Meaning
```

---

# 66. Decision Granularity

一个 Decision Interaction 应围绕：

```text
one coherent Material Semantic Choice
```

组织。

正式：

```text
Decision Granularity
should follow Material Semantic Choice,
not individual fields.
```

---

# 67. 不得偷偷捆绑独立治理问题

如果多个问题：

```text
Authority 不同

Scope 不同

后果不同

可独立成立
```

不应强行合并成一个：

```text
“全部确认”
```

正式：

```text
One Interaction
should not silently bundle
independent governance decisions.
```

---

# 68. Coherent Alternative 可以包含多个不可分割后果

如果方案 B 本身就是：

```text
修改 shared component
+
同步两个后台
+
扩大验证范围
```

且这些是一个不可分割的治理选择，

可以作为一个 Coherent Alternative 一次决策。

---

# 69. Batch Presentation 与 Batch Authority 分离

UI 可以展示：

```text
3 个待决事项
```

但：

```text
Batch Presentation
!= Bundled Decision Authority
```

只有 Governance Contract 明确允许时，才可以批量产生正式 Decision。

---

# 70. Decision Requirement / Interaction / Input / Record 分离

正式冻结四层：

```text
Decision Requirement
为什么必须做决定

GovernanceDecisionInteraction
怎样让人理解并选择

GovernanceDecisionInput
人明确提交了什么

Governed Decision Record
正式 Owner 接受并拥有的治理事实
```

因此：

```text
Decision Requirement
!= Decision Interaction

Decision Interaction
!= Decision Input

Decision Input
!= Governed Decision Record
```

---

# 71. Decision Interaction Lifecycle 与 Governed Decision Lifecycle 分离

正式：

```text
Decision Interaction Lifecycle
!= Governed Decision Lifecycle
```

F11 交互可以经历：

```text
Presented
Input Drafted
Submitted
Feedback shown
```

这些都不自动构成正式治理 Decision State。

---

# 72. Presented 不等于 Decided

正式：

```text
Presented
!= Acknowledged

Presented
!= Understood

Presented
!= Decided
```

F11 不能因为 Decision 页面被打开，就认为治理问题已经处理。

---

# 73. Notification / Attention 与 Decision 分离

正式：

```text
Notification Read
!= Decision Made

Attention Acknowledged
!= Decision Made
```

通知状态由 D07 进一步治理。

---

# 74. Unsubmitted Selection 不等于 Human Decision

用户在页面上暂时选中：

```text
B
```

但未正式提交 GovernanceDecisionInput，

则：

```text
Unsubmitted Selection
!= Human Decision
```

Draft 是否跨 Surface 同步留给 D08 / Implementation。

---

# 75. Decision Input 与 Owner Validation

GovernanceDecisionInput 提交后，由正式 Decision Owner 检查：

```text
Requirement 是否仍存在

Decision Basis 是否仍适用

Alternative 是否仍合法

Decision Authority 是否仍有效
```

正式：

```text
Decision Submission
!= Automatic Decision Acceptance
```

---

# 76. Decision Applicability Validation 与 Runtime Revalidation 分离

正式：

```text
Decision Applicability Validation
!= Runtime Permission Revalidation
```

D04 的 Input 交回：

```text
Decision / Domain Owner
```

D03 的 RuntimeControlIntent 交回：

```text
F10
```

Owner 不得混淆。

---

# 77. Stale Decision Input

若用户基于：

```text
DB-17
```

选择 B，

但提交时 Material Decision Basis 已变为：

```text
DB-18
```

则 Input 可以成为：

```text
Stale Decision Input
```

正式：

```text
Stale Decision Input
!= Invalid Human Judgment

Stale Decision Input
!= System Failure
```

---

# 78. Basis Revision 不自动使 Decision 失效

正式：

```text
Basis Revision
!= Automatic Decision Invalidation
```

只有发生：

```text
Material Basis Change
```

才需要重新评估 Input 是否仍适用。

---

# 79. Material Basis Change

Material Basis Change 可以包括：

```text
Alternative meaning materially changed

Scope materially changed

Major impact changed

Risk / reversibility materially changed

Authority basis materially changed

New materially distinct valid alternative appeared
```

Exact Enum 不在 D04 冻结。

正式：

```text
Material Basis Change
requires Decision Applicability Re-evaluation.
```

---

# 80. Any Context Change 不等于 Decision Invalidation

例如：

```text
new irrelevant trace entry

timestamp refresh

non-material metadata update
```

不应自动让用户重新决定。

正式：

```text
Any Context Change
!= Decision Invalidation
```

---

# 81. F11 Basis Preservation 与 Decision Validity Authority 分离

F11 负责：

```text
preserve Basis identity

show current basis

route changed basis

stop stale submission where required
```

但：

```text
F11 Basis Preservation
!= Decision Validity Authority
```

是否仍有效由对应 Decision Owner / Governance Contract 决定。

---

# 82. Superseded Decision

一个历史 Decision 可以被后续正式 Decision 取代。

正式：

```text
Superseded Decision
!= Deleted Decision

Superseded Decision
!= Never Existed
```

历史事实必须可追踪。

---

# 83. Current Effective Decision 与历史记录分离

系统需要能够区分：

```text
Historical Decisions

Current Effective Decision
```

不得通过覆盖旧记录丢失治理历史。

---

# 84. Decision Change 保留 Provenance

如果正式决策从：

```text
B → A
```

发生变化，

应通过：

```text
Revision
Superseding Decision
New Decision
```

等由 Owner 定义的正式机制处理。

正式：

```text
Decision Change
should preserve historical decision provenance.
```

Exact Revision Model 暂缓。

---

# 85. Decision Requirement 可以 No Longer Required

Human Decision Requirement 一旦创建，不意味着永久必须由人回答。

例如：

```text
原来 A / B 都合法
↓
新规则使 A 不合法
↓
只剩 B
```

此时系统可以自动解析。

正式：

```text
Decision Requirement
is not permanent once created.
```

---

# 86. No Longer Required 不等于 Synthetic Human Decision

正式：

```text
Decision No Longer Required
!= Synthetic Human Decision
```

系统确定性解析 B 时，不得记录：

```text
Human selected B
```

而应记录：

```text
Requirement resolved automatically
```

---

# 87. Decision Interaction No Longer Applicable

如果对应 Subject / Requirement 已经消失：

```text
Action cancelled

Change withdrawn

condition no longer exists
```

Interaction 可以结束。

正式：

```text
Decision Interaction No Longer Applicable
!= Human Rejection
```

---

# 88. Deferred Interaction 不等于 Requirement Resolved

用户选择：

```text
稍后处理
```

只影响 Interaction / Attention。

正式：

```text
Deferred Interaction
!= Decision Requirement Resolved
```

---

# 89. F11 可以展示 Decision Lifecycle Projection

F11 可以显示：

```text
Human Decision Required

Submitted

Under Validation

Accepted

Stale

Superseded

No Longer Required
```

等来自不同 Owner 的当前 Projection。

但：

```text
F11 may present Decision Lifecycle Projection

but does not own
Governed Decision Lifecycle Truth.
```

---

# 90. F11 不建立万能 Decision State Machine

不得通过：

```text
F11Decision.status
```

统一承担：

```text
Requirement State

Interaction State

Input State

Governed Decision State

Runtime State
```

正式：

```text
Decision Interaction Tracking
!= Governed Decision State Machine
```

---

# 91. Decision Accepted 后不得 Blind Continue

正式：

```text
Decision Acceptance
→ Downstream Re-resolution
```

而不是：

```text
Decision Acceptance
→ Blind Runtime Continue
```

---

# 92. Downstream Re-resolution

Human Decision 被接受后，根据具体 Domain 重新解析相关：

```text
Scope

Authority

Gate

Binding

Dependency

Impact

Provider Context

Runtime Context
```

只加载与当前 Decision 后果相关的 Minimum Sufficient Context。

---

# 93. Scope Decision Accepted 不等于 Runtime Continue

例如用户批准：

```text
Scope Expansion
```

只说明：

```text
新的 Scope Governance Basis 已建立
```

后续仍可能需要：

```text
Change / Apply Authorization

Project reconciliation

Impact refresh

Runtime Permission
```

正式：

```text
Scope Decision Accepted
!= Runtime Continue
```

---

# 94. Human Decision 不等于 Apply Authorization

正式继续冻结：

```text
Human Decision
!= Apply Authorization
```

Decision 可以成为后续 Apply Authorization 的依据，但不自动等于 Apply Authorization。

---

# 95. Human Decision 不等于 Runtime Permission

正式：

```text
Human Decision
!= Runtime Permission
```

即使 Governance Decision 已被接受，F10 使用点仍需 Current Runtime Revalidation。

---

# 96. Human Decision 不等于 Canonical Mutation

正式：

```text
Human Decision
!= Canonical Mutation
```

F11 不因为用户批准方案，就直接改变 Canonical Truth。

---

# 97. Decision Accepted 不等于 Downstream Execution

正式：

```text
Decision Input Capture
!= Decision Acceptance

Decision Acceptance
!= Downstream Execution
```

这三步必须保持独立。

---

# 98. Decision Accepted + Runtime Blocked 是合法组合

例如：

```text
Decision:
Scope Expansion ACCEPTED

Runtime:
BLOCKED by Safety Gate
```

完全合法。

正式：

```text
Decision Accepted
+
Runtime Blocked
is a valid state combination.
```

---

# 99. Valid Decision 不等于 Current Runtime Permission

即使 Decision 仍然有效：

```text
Valid Decision
!= Current Runtime Permission
```

Runtime Permission 仍由 F10 根据使用点事实决定。

---

# 100. Human Decision 不要求立即产生 Runtime 后果

正式：

```text
Human Decision
does not require Immediate Runtime Consequence.
```

某些 Decision 只更新：

```text
governance basis

configuration meaning

future rule selection
```

并不会立即创建 Execution Attempt。

---

# 101. Decision Success 不等于 Global Workflow Success

正式：

```text
Decision Success
!= Global Workflow Success
```

Decision、Runtime、Validation、Apply、Canonical 等继续保持不同 Authority Domain。

---

# 102. Stale 与 Unauthorized 分离

如果 Basis 变化导致 Input 失效：

```text
Stale Decision Input
```

与用户没有 Decision Authority：

```text
Unauthorized Decision Input
```

不是同一问题。

正式：

```text
Stale Decision Input
!= Unauthorized Decision Input
```

---

# 103. Concurrent Decision Submission

多个 Surface 可能针对同一 Decision Requirement 同时提交不同 Input。

例如：

```text
Web:
B

IDE:
A
```

D04 不冻结锁机制。

但正式要求：

```text
Concurrent Decision Submissions
must not silently overwrite
Governed Decision Truth.
```

---

# 104. Last Write Wins 不是治理规则

正式：

```text
Last Write Wins
!= Governance Decision Resolution
```

后续提交可能需要：

```text
No Longer Applicable

Conflict

Amendment

New Decision Requirement
```

具体由 Decision Owner 决定。

---

# 105. Decision Identity 与 Surface Identity 分离

正式：

```text
Decision Identity
!= ControlSurface Identity
```

同一个 Decision Requirement 可在 Web / IDE / CLI 被不同方式展示。

---

# 106. 跨 Surface 展示密度可以不同

正式：

```text
Decision Presentation Density
may differ by Surface.

Decision Semantics
may not diverge by Surface.
```

各 Surface 必须保持同一：

```text
Subject

Basis

valid alternatives

material differences
```

的治理含义。

---

# 107. Decision Origin Surface 不等于 Decision Authority

正式：

```text
Decision Origin Surface
!= Decision Authority
```

用户是否有权做当前决定，由正式 Identity / Scope / Authority Contract 决定，而不是因为操作发生在某个 Surface。

---

# 108. Decision Evidence Requirement

为了未来审计，Human Decision 应能够关联：

```text
Decision Requirement

Decision Subject

Decision Basis

Alternatives presented

Material Differences

Human Input

Decision Owner Resolution

Relevant Evidence / Provenance references
```

---

# 109. Decision Evidence 不应只保存最终选项

正式：

```text
Decision Evidence
should preserve Material Decision Context,
not merely final selected value.
```

不能只留下：

```text
selected = B
```

却无法知道当时 B 代表什么。

---

# 110. Decision Evidence 不等于 Decision Authority

正式：

```text
Decision Evidence
!= Decision Authority
```

Evidence 证明发生过什么，不授予谁有权决定。

---

# 111. D04 与 D06 的边界

D04 负责：

```text
Decision Evidence Requirement

Material Decision Context requirements

Evidence / Provenance references
```

D06 负责：

```text
Evidence Presentation

Trace Timeline

Provenance Navigation

Result / Evidence / Trace drill-down
```

正式：

```text
D04 owns Decision Evidence Requirement.

D06 owns rich Evidence Presentation.
```

---

# 112. D04 与 D07 的边界

D04 负责：

```text
Human Decision Interaction
```

D07 负责：

```text
when / where / how to notify

attention urgency

deduplication

reminders

inbox

delivery
```

因此：

```text
Human Decision Required
!= Specific Notification Mechanism
```

---

# 113. Decision Materiality 与 Notification Urgency 分离

一个决策很重要，不代表：

```text
必须立即全屏打断用户
```

正式：

```text
Decision Materiality
!= Notification Urgency
```

Attention Policy 留给 D07。

---

# 114. D04 与 F4 DecisionProtocol 的边界

F4 / applicable Governance Owner 负责：

```text
when Human Decision is required

what governance semantics the requirement carries

who owns Decision Authority

which choices can be automatically resolved

how Decision Resolution feeds Workflow
```

F11-D04 负责：

```text
presenting requirement

assembling Minimum Sufficient Material Context

comparing alternatives

showing optional Recommendation

collecting Explicit Human Input

preserving Decision Basis

routing Input back to Owner
```

正式：

```text
F11-D04
!= DecisionProtocolDefinition Owner.
```

---

# 115. Decision UX Owner 与 Decision Authority Owner 分离

正式：

```text
Decision UX Owner
!= Decision Authority Owner
```

F11 可以拥有交互 Contract，但不能因为拥有 UI 就获得：

```text
Product Decision Authority

Apply Authority

Runtime Authority

Canonical Mutation Authority
```

---

# 116. Decision Responsibility Flow

F11-D04 正式采用以下逻辑责任链：

```text
1. Requirement
   Applicable governance determines
   Human Decision is genuinely required

2. Assemble
   F11 obtains:
   Subject
   Basis
   Alternatives
   Material Differences
   Consequences

3. Present
   F11 provides
   Minimum Sufficient
   Informed Decision Context

4. Recommend
   Optional
   Basis-backed
   never substitutes Human Decision

5. Submit
   Human provides
   Explicit GovernanceDecisionInput

6. Validate
   Decision Owner validates:
   current Basis
   Authority
   applicability

7. Resolve
   Governed Decision becomes:
   accepted / stale /
   superseded /
   no-longer-required /
   other owner-defined outcome

8. Re-resolve
   affected downstream:
   Scope
   Authority
   Gate
   Dependency
   Runtime
   etc.

9. Reflect
   F11 presents
   authoritative current outcome
```

该模型是责任模型，不是固定 API 或 Workflow Definition。

---

# 117. F11-D04 核心不变量

正式冻结：

```text
F11 presents Human Decision Requirement
!= F11 invents Human Decision Requirement

Operational Failure
!= Human Decision Required

Technical Uncertainty
!= Human Decision Required

Missing Context
!= Human Decision Required by default

Multiple Candidates
!= Human Decision Required

Technical Alternative
!= Material Decision Alternative

Candidate
!= Valid Decision Alternative

Implementation Difference
without Material Governance Difference
!= Human Decision Alternative

Informed Decision
!= Maximum Information

Informed Decision
= Minimum Sufficient Material Context

Decision Requirement
!= Decision Question

Governance Decision
must remain Subject-bound

Decision Summary
may compress detail
but must preserve Material Difference

Decision Detail Importance
!= Technical Detail Volume

Path Count
!= Scope Meaning

Authority Impact
!= Authority Transfer by default

Material Semantic Difference
must not be hidden

Downstream Impact
should support Summary → Drill-down

Material Impact
must not be hidden by aggregation

Risk
!= Reversibility

Risk Label
requires governed basis

Known Consequence
!= Risk

Known Impact
!= Predicted Possibility

Deferred Obligation
is a Material Decision Consequence
when created or changed

Deferred Obligation
must remain actionable / traceable
when known

Immediate Consequence
!= Deferred Obligation

Cost / Effort Claim
must remain Basis-backed

Decision Information Architecture
!= Fixed UI Layout

AI Recommendation
!= Human Decision

AI Recommendation
must remain Basis-backed

Recommendation
must not erase Material Countervailing Evidence

Recommendation Rationale
must distinguish Fact from Inference

Recommendation Presence
is optional

No Reliable Recommendation
is a valid outcome

Recommendation
!= Default

Default Applied
!= Human Decision

Default Presentation
!= Human Decision

Recommendation Highlight
!= Explicit Selection

Preference
!= Blanket Authorization

Applicable Governed Preference
may eliminate Human Decision Requirement

Historical Choice
!= Standing Preference

Repeated Historical Choice
!= Preference

Historical Choice
may inform explanation
but does not become Decision Authority

Historical Consistency Signal
!= Governance Prohibition

AI Recommendation
!= Delegated Human Decision by default

Automatically Resolvable Choice
should remain Automatic Resolution,
not Synthetic Human Decision

Silence
!= Human Decision

Dismiss
!= Human Decision

Timeout
!= Human Decision

Acknowledge
!= Human Decision

Defer
!= Decision

UI Confirmation Event
!= Governance Decision Meaning

Decision Granularity
should follow Material Semantic Choice

One Interaction
should not silently bundle
independent governance decisions

Batch Presentation
!= Bundled Decision Authority

Decision Requirement
!= Decision Interaction

Decision Interaction
!= Decision Input

Decision Input
!= Governed Decision Record

Decision Interaction Lifecycle
!= Governed Decision Lifecycle

Presented
!= Decided

Notification Read
!= Decision Made

Attention Acknowledged
!= Decision Made

Unsubmitted Selection
!= Human Decision

Decision Submission
!= Automatic Decision Acceptance

Decision Applicability Validation
!= Runtime Permission Revalidation

Stale Decision Input
!= Invalid Human Judgment

Stale Decision Input
!= System Failure

Basis Revision
!= Automatic Decision Invalidation

Any Context Change
!= Decision Invalidation

Material Basis Change
requires Decision Applicability Re-evaluation

F11 Basis Preservation
!= Decision Validity Authority

Superseded Decision
!= Deleted Decision

Decision No Longer Required
!= Synthetic Human Decision

Decision Interaction No Longer Applicable
!= Human Rejection

Deferred Interaction
!= Decision Requirement Resolved

F11 may present Decision Lifecycle Projection
but does not own Governed Decision Lifecycle Truth

Decision Acceptance
→ Downstream Re-resolution

Decision Acceptance
!= Blind Runtime Continue

Scope Decision Accepted
!= Runtime Continue

Human Decision
!= Apply Authorization

Human Decision
!= Runtime Permission

Human Decision
!= Canonical Mutation

Decision Input Capture
!= Decision Acceptance

Decision Acceptance
!= Downstream Execution

Valid Decision
!= Current Runtime Permission

Human Decision
does not require Immediate Runtime Consequence

Decision Accepted
+
Runtime Blocked
is a valid state combination

Decision Success
!= Global Workflow Success

Stale Decision Input
!= Unauthorized Decision Input

Concurrent Decision Submissions
must not silently overwrite
Governed Decision Truth

Last Write Wins
!= Governance Decision Resolution

Decision Change
should preserve historical decision provenance

Decision Identity
!= ControlSurface Identity

Decision Origin Surface
!= Decision Authority

Decision Presentation Density
may differ by Surface

Decision Semantics
may not diverge by Surface

Decision Evidence
should preserve Material Decision Context,
not merely final selected value

Decision Evidence
!= Decision Authority

Human Decision Required
!= Specific Notification Mechanism

Decision Materiality
!= Notification Urgency

Decision UX Owner
!= Decision Authority Owner

F11-D04
!= DecisionProtocolDefinition Owner

Decision Feedback
should converge back to
authoritative governance/domain projections
```

---

# 118. Explicitly Forbidden Designs

F11-D04 明确禁止将以下方式提升为正式架构：

```text
AI uncertainty
= Human Decision Requirement

Any operational failure
= Ask user

Multiple candidates
= Ask user

Technical implementation difference
= Governance decision

Historical choice
= User preference

Repeated choice
= Permanent AI-learned preference

AI Recommendation
= Human Decision

Recommendation
= Default approval

Default applied
= Human selected option

Dismiss
= Reject

Timeout
= Approve default

Acknowledge
= Decision

Opening decision page
= User understood

Selected radio button
= Governed Decision

Confirm button
= Decision meaning

Human Decision
= Apply Authorization

Human Decision
= Runtime Permission

Human Decision
= Canonical Mutation

Decision Accepted
= Blind Runtime Resume

Old Decision Input
= Automatically valid after Material Basis Change

Latest write
= Current Governed Decision

F11 database status
= Governed Decision Truth

Decision history overwritten
instead of preserved

All pending decisions
= One batch authority

Decision notification
= Decision itself
```

---

# 119. Deferred

F11-D04 不冻结：

```text
Exact Decision Requirement Enum

Exact Decision Status Enum

Exact Decision Input Schema

Exact Governed Decision Schema

Exact Material Difference Enum

Exact Risk Enum

Exact Reversibility Enum

Exact Recommendation Algorithm

AI Confidence Score

Exact Preference Schema

Exact Preference Owner implementation

Exact Decision Revision Model

Exact Supersede Storage Model

Exact Concurrent Write Algorithm

Exact Batch Decision Algorithm

Exact Attention Priority

Notification Delivery

Reminder Frequency

Inbox Implementation

Evidence Storage Format

Database Tables

SQLite Physical Schema

Redis Structure

REST API

HTTP Status

WebSocket

SSE

Modal

Drawer

Page Layout

Button Style

Color System

Frontend Store

Go Struct

TypeScript Interface
```

---

# 120. Approval Effect

本稿已经明确：

```text
F11-D04 HUMAN_APPROVED
```

因此正式冻结：

```text
Human Decision Requirement boundary

Automatic-resolution-first principle

Decision Requirement / Question / Subject /
Basis separation

Minimum Sufficient Informed Decision Context

Valid Alternative filtering

Material Difference governance

Scope / Authority / Semantic /
Downstream / Risk /
Reversibility / Deferred Obligation
presentation boundaries

Recommendation boundary

Recommendation / Default /
Preference / Historical Choice separation

Explicit Human Input requirement

Decision Requirement /
Interaction / Input /
Governed Decision separation

Decision Basis applicability

Stale Decision Input semantics

Superseded Decision semantics

No Longer Required semantics

Decision Acceptance /
Apply / Runtime separation

Downstream Re-resolution principle

Concurrent Decision semantic safety

Decision Evidence requirement

Cross-surface Decision semantic consistency

D04 / F4 / D06 / D07
responsibility boundaries
```

但不代表：

```text
DecisionProtocol transferred to F11

Decision Authority transferred to F11

Apply Authorization transferred to F11

Runtime Permission transferred to F11

Canonical Mutation authorized

Exact Decision Enum frozen

Exact Risk Model frozen

Exact Recommendation Algorithm frozen

Preference system implementation frozen

Database frozen

SQLite schema frozen

UI implementation frozen

Implementation authorized

RP2 authorized

Authority Cutover authorized

Canonical Replacement authorized

Final Activation authorized

Legacy Retirement authorized
```

---

# 121. Final Frozen Decision

```text
F11-D04
— Human Decision UX &
  Informed Decision Interaction

STATUS:
HUMAN_APPROVED / FROZEN

Banyan does not turn every uncertainty
into a Human Decision.

Deterministic and governed automatic
resolution remains the default.

Human Decision is reserved for genuine
material governance choices that existing
rules cannot uniquely resolve.

F11 presents the decision;
it does not invent the requirement
or own the decision authority.

A valid Human Decision Interaction provides
Minimum Sufficient Material Context:
why a decision is required,
what is being decided,
the current Decision Basis,
valid materially distinct alternatives,
their material differences,
their consequences,
and optional Basis-backed recommendation.

Technical differences that do not create
material governance differences
do not become Human Decision Alternatives.

AI Recommendation remains optional,
Basis-backed,
and separate from Human Decision.

Recommendation,
Default,
Preference,
and Historical Choice remain distinct.

Historical behavior is not silently learned
into reusable decision authority.

Silence,
dismiss,
timeout,
acknowledgement,
and unsubmitted UI selection
are not Human Decisions.

Human Input is bound to its Decision Basis
and is validated by the actual Decision Owner.

Material Basis changes trigger
applicability re-evaluation.

Stale Decision Input is not
a failed human judgment.

Superseded decisions remain historical facts.

A Decision Requirement may disappear
when deterministic resolution becomes possible;
this is not a synthetic Human Decision.

Human Decision Acceptance does not equal
Apply Authorization,
Runtime Permission,
Canonical Mutation,
or immediate execution.

Accepted decisions cause
downstream re-resolution,
not blind continuation.

Concurrent Decision submissions
must not silently overwrite
governed decision truth.

Decision evidence preserves
the material context of the choice,
not merely the selected value.

F11 owns Governance UX interaction semantics,
not DecisionProtocol,
Decision Authority,
Apply Authority,
Runtime Authority,
or Canonical Truth.

Implementation remains NOT_AUTHORIZED.
```

---

**END OF F11-D04 HUMAN_APPROVED FREEZE**

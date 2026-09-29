# F10-D03 — Runtime Provider Resolution × Adapter Routing Boundary

**阶段：** F10 — Runtime Permission / Execution Governance Architecture  
**主题：** Runtime Provider Resolution（运行时 Provider 解析）× Adapter Routing（适配器路由）边界  
**状态：** `HUMAN_APPROVED`  
**上游依赖：**
- `F10-G01 HUMAN_APPROVED`
- `F10-D01 HUMAN_APPROVED`
- `F10-D02 HUMAN_APPROVED`

**Implementation Authorization：** `NO`

---

## 1. 决策目的

F10-D03 解决：当一个具体 Action 已经拥有合法 Execution Context，并准备进入运行时执行时，应实际使用哪个已经治理有效的 Provider，以及通过哪个满足当前执行合同的 Adapter 完成技术调用。

核心：

```text
F8 Governed Provider State
+
Current Action Requirements
+
F10 Runtime Conditions
↓
Runtime Provider Resolution
↓
Compatible Adapter Routing
↓
Concrete Execution Channel
```

`Runtime convenience != Governance bypass`

---

## 2. 核心语义分离

```text
Provider Binding
!= Runtime Provider Resolution
!= Adapter Routing
```

- Provider Binding：哪些 Provider 在什么 Project / Scope / Capability 下有治理资格。
- Runtime Provider Resolution：当前 Action 此刻实际使用哪个已合法 Provider。
- Adapter Routing：Banyan 通过什么技术通道调用该 Provider / Capability。

---

## 3. F8 Provider Governance 继续有效

F8 继续拥有：

```text
Provider Binding
Provider Eligibility
Provider Selection Governance
Fallback Governance
Version / Compatibility where applicable
Project-scoped Provider Context
```

F10-D03 不建立第二套 Provider Binding Authority。

`F10 Runtime Provider Resolution != F8 Provider Governance Replacement`

---

## 4. Effective Provider 优先消费

如果 F8 Runtime Handoff 已经提供 Effective Provider，且该 Provider 在当前使用点仍 Applicable / Eligible / Compatible / Available，则 F10 应直接消费该结果，不应无理由重新挑选 Provider。

---

## 5. Runtime Provider Resolution 的 Owner 边界

F10 拥有当前 Action 使用点上的运行时 Provider 解析与执行路由。

F10 不拥有：

```text
Provider Definition Authority
Provider Binding Authority
Durable Provider Rebinding Authority
Project-wide Provider Policy Authority
```

---

## 6. Runtime Resolution 是派生状态

```text
Runtime Provider Resolution
=
Action-scoped
Context-aware
Derived
Re-evaluable
```

因此：

`Runtime Provider Selection != Durable Provider Binding`

---

## 7. 临时选择不得改写 Project Binding

例如：

```text
Primary Provider = A
Fallback Provider = B

A temporary unavailable
→ Runtime uses B
```

不能自动解释为：

`Project Default Provider = B`

如果需要永久改变 Provider Binding：

`→ Applicable F8 / F7 governed path`

---

## 8. Provider 基础语义继续分离

```text
Capability != Provider
Provider Binding != Runtime Permission
Provider Health != Capability
Provider Availability != Eligibility
Provider Availability != Authorization
```

---

## 9. Provider Health 是运行时事实

如果 A 的 Binding / Eligibility / Capability 都有效，但 Health = TEMPORARILY_UNAVAILABLE，只说明 A 当前暂时不能执行，不意味着 Provider Binding = INVALID。

---

## 10. Runtime Unavailable != Durable Invalidity

```text
Provider Temporarily Unavailable != Provider Binding Invalid
Provider Runtime Failure != Provider Definition Invalid
Provider Timeout != Project Rebinding Required
```

---

## 11. Provider Candidate Set 边界

F10 只能从当前治理允许的候选集合或治理明确允许的 Fallback Path 中解析 Provider。

```text
F10 may select within governed candidates
F10 may not silently enlarge governed candidate set
```

---

## 12. 未治理 Provider 不得自动加入

如果当前合法候选只有 A、B，而技术上发现 C 可用，F10 不能因为 C 能完成任务就自动使用 C；必须走适用 Governance。

---

## 13. Technical Capability != Governance Eligibility

`Provider Can Do It != Provider May Do It`

技术上有能力，不代表 Eligible / Authorized / Scope-compatible / Semantically compatible。

---

## 14. Semantic Compatibility

Provider Fallback 除技术能力外，还必须满足当前 Action 的 Material Semantic Contract，包括按需的：

```text
Required capability
Required output semantics
Required tool support
Required structured behavior
Required safety boundary
Required execution guarantees
Required validation compatibility
```

具体字段不在 D03 冻结。

---

## 15. Technical Compatibility != Semantic Compatibility

两个 Provider 都能“生成代码”，不代表都适合同一个严格 Action Contract。

---

## 16. Automatic Fallback 成立条件

只有替代候选同时满足：

```text
Fallback already governed / eligible
Required Capability satisfied
Semantic Contract satisfied
Current Scope remains valid
Authorization is not enlarged
Security / data boundary is not materially changed
Required runtime gates remain satisfied
```

才可 Automatic Runtime Fallback。

---

## 17. Fallback != Retry

Retry：再次尝试相同或等价执行路径。  
Fallback：切换到另一个已经治理合法的 Provider / execution path。

---

## 18. Provider 切换的三类语义

### A. Equivalent Governed Fallback
同语义、同 Scope、同 Authorization Envelope、兼容 Capability → 可自动切换。

### B. Valid Alternative with Different Operational Characteristics
例如延迟、成本、容量不同，但治理语义和最低能力合同保持 → 可按已有治理规则自动解析。

### C. Material Semantic Provider Change
如果切换会实质改变 data boundary / security boundary / authority implication / scope / semantic capability / required guarantees / governance obligations → 不得自动 fallback，必须路由 Governance Owner。

---

## 19. Operational Difference != Material Semantic Difference

不同 Cost / Latency / Throughput 不自动等于 Material Semantic Difference。

---

## 20. Cost / Speed 优先级

不能无条件 Cheapest Wins / Fastest Wins。

必须先满足：

```text
Governance Eligibility
Authorization / Scope
Required Capability
Semantic Compatibility
Safety Requirements
Required Execution Contract
```

之后才能在剩余合法候选中依据已治理 Preference / Cost / Latency / Availability / Resource Policy 做确定性解析。

---

## 21. No Arbitrary Winner

多个 Provider 都合法但无已有规则可可靠选择时，F10 不得 invent winner。

禁止：

```text
first provider wins
latest provider wins
cheapest provider wins by default
highest model confidence wins
provider self-selects
```

---

## 22. Deterministic Candidate Resolution

如果 A eligible、B ineligible → 自动选择 A。

如果 A、B 都 eligible，且已有 Primary / Fallback 规则 → 正常自动选择 Primary。

---

## 23. Multiple Legal Candidates

如果多个候选合法，且可由 Capability fit / Explicit preference / Runtime health / Cost policy / Latency policy / Environment compatibility 唯一确定 Winner → 自动解析，不要求 Human Decision。

---

## 24. Human Decision Boundary

只有：

```text
multiple legitimate candidates
+
materially different semantic outcomes
+
existing governance cannot determine winner
```

才进入 Human Decision。

`Multiple Providers != Human Decision Required`

---

## 25. Provider 不拥有 Routing Authority

Provider 失败后只能报告结果，由 F10 根据当前治理候选集合重新解析后续路径。

`Provider != Provider Routing Authority`

---

## 26. Provider Failure 输出

Provider 可以报告 Success / Failure / Temporary Unavailability / Capability Mismatch / Required Context Missing / Runtime Constraint。

这些首先是 Runtime Evidence / State，不自动修改治理 Binding。

---

## 27. Missing Context 与 Provider Resolution

Provider 缺少信息时：

```text
Provider → Required Context Need
F10 → resolve required context per D02
→ re-evaluate provider path
```

Provider 不自行无限扫描 Project。

---

## 28. Provider Continuity

一个 Task 可以在不同 Action 中使用多个治理合法 Provider。

`Task starts with A != every future Action must use A`

除非特定 Workflow / Contract 明确要求连续性。

---

## 29. Action-sensitive Provider Resolution

不同 Action 可以根据不同 Capability Requirement 使用不同 Provider，例如 Requirement Analysis / Code Generation / Visual Analysis / Test Execution 分别由不同合法 Provider 承担。

---

## 30. Provider Resolution × D01 Runtime Permission

`Provider Eligible != Runtime ALLOW`

Provider 条件只是 D01 Permission Evaluation 的一个适用输入。

---

## 31. Provider Resolution × D02 Execution Context

Provider 只获得 D02 形成的 Action-specific Minimum Sufficient Execution Context，不默认获得 Entire Project / Entire Task History / Every Requirement / Every Secret。

---

## 32. Selected Provider 不扩大 Authority

```text
Selected Provider != Context Authority
Selected Provider != Scope Authority
Selected Provider != Authorization Authority
```

---

## 33. Adapter 定义

Provider = 谁提供能力。  
Adapter = Banyan 怎么调用这个能力。

Adapter 的定位是把已经治理确定的 Action / Capability 调用翻译为具体技术接口、协议或执行通道。

---

## 34. Adapter 是执行机制

`Adapter = Execution Mechanism / Channel`

`Adapter != Semantic Decision Maker`

---

## 35. Adapter 不拥有 Permission / Scope / Provider Selection

```text
Adapter Capability != Runtime Permission
Adapter Ready != Authorization
Adapter Successful != Authority
Adapter != Scope Authority
Adapter != Provider Selector
```

Adapter 不得自行扩大 target / scope / task semantics。

---

## 36. Provider 与 Adapter 不是一对一锁死

允许：

```text
Provider A
├── CLI Adapter
├── HTTP Adapter
├── MCP Adapter
├── SDK Adapter
└── Future Adapter
```

一个兼容 Adapter 也可服务多个 Provider。具体映射留给后续实现和 Provider Contract。

---

## 37. Adapter Routing 输入

可依据：

```text
Selected / Effective Provider
Required Capability
Execution Contract
Current Environment
Adapter Availability
Adapter Compatibility
Required Safety Guarantees
```

做确定性解析。

---

## 38. Adapter Technical Capability != Contract Compatibility

Adapter 能调用 Provider，不等于满足当前执行合同。

如果无法满足 Expected Base validation / Atomicity / Trace / Authorization propagation / Target verification 等必要保证，就不能作为适用 Adapter。

---

## 39. Adapter 自动切换

多个 Adapter 都满足同一 required execution contract 且处于同一治理边界，已有规则可唯一解析时，可 Automatic Adapter Routing。

---

## 40. Adapter 切换不得改变语义

如果 Adapter 切换会丢失 required atomicity / security / traceability / expected-base protection / permission enforcement，则不能视为等价技术切换。

---

## 41. Failure 边界

```text
Adapter Failure != Provider Invalid
Adapter Unavailable != Provider Binding Invalid
Provider Failure != Adapter Failure
```

如同 Provider 仍有其他合法 Adapter，可定向重新路由。

---

## 42. Runtime Resolution 采用约束解析思想

逻辑上：

```text
Action Requirements
+
Governed Provider State
+
Capability Requirement
+
Semantic Compatibility
+
Runtime Availability
+
Execution Context
+
Applicable Gate / Permission Conditions
+
Execution Environment
↓
Valid Runtime Routes
↓
Deterministic Selection
```

D03 不冻结具体 Rule Engine / Constraint Solver / AI Selection Model / Scoring Engine。

---

## 43. Core 保持 Provider-neutral

Banyan Core 不应把 Cursor / Codex / Claude 等商业 Provider 名称硬编码成核心治理语义。

```text
Core Governance must remain provider-neutral
```

Editor 身份本身也不等于 Authority / Authorization / Provider Eligibility。

---

## 44. Technology-neutral Core

CLI / HTTP / MCP / SDK / Filesystem / Git 都只是技术通道，不能成为 Core 架构锁死条件。

---

## 45. Runtime Route 是短生命周期派生结果

```text
Runtime Route
=
Provider
+
Adapter
+
Action-specific Execution Basis
```

属于 Derived Runtime State，不是永久 Project Binding。

运行环境变化时可 Re-resolve，只要仍未越出治理边界。

---

## 46. Runtime Route Cache

允许缓存 Runtime Route Resolution，但：

```text
Cached Route != Eternal Route
Runtime Route Cache != Provider Binding
Runtime Route Cache != Adapter Authority
Runtime Route Cache != Runtime Permission
```

---

## 47. Provider Health Refresh

Provider Health / Availability 属于易变化 Runtime Slice。

Provider Health Unknown 应优先自动检查，不直接询问用户。

`Runtime Provider Unresolved != Human Decision Required`

---

## 48. Status 不产生 Authority

```text
Provider ONLINE / HEALTHY / AVAILABLE != AUTHORIZED
Adapter Ready != Action Allowed
```

---

## 49. Data / Security Boundary

Provider 切换若导致 local→external、private environment→external service、restricted data→broader exposure 等重要数据/安全边界变化，且治理未预先允许，则属于 Material Provider Change，不得自动切换。

已治理为同等 Security / Data Boundary 的多个 Provider，可在合法集合内自动解析。

---

## 50. Capability Floor

当前 Action 可以定义 Minimum Required Capability。

低于最低能力要求的 Provider，即使更快、更便宜，也不能使用。

Provider 质量不使用“模型更聪明”之类模糊主观排序作为治理依据，而应依赖 Declared Capability / Validated Capability Evidence / Contract Compatibility / Applicable Policy。

---

## 51. Additional Validation

不同合法 Provider 如具有不同 Validation Obligation，F10 可执行相应定向验证。

`Additional Validation != Human Approval by default`

---

## 52. Current Implementation Evidence Boundary

现有 Runtime / Stage 15 中 Generic filesystem / Git CLI / process runner / binding loader / provider status surface，以及 Provider / Adapter 分层，只作为 Compatibility Evidence / Implementation Reality。

`Current Implementation != F10-D03 Architecture Authority`

现有少量实现不能反推 Future Banyan only supports these Providers。

---

## 53. Current Runtime Safety State

继续保持：

```text
Current Project Execution = DRY_RUN_ONLY where governed
Final Activation = NOT_AUTHORIZED
Canonical Write = BLOCKED where governed
```

Provider / Adapter Resolution 不解除这些限制。

---

## 54. Route Ready != Execution Authorized

```text
Runtime Provider Resolved != Runtime ALLOW
Adapter Resolved != Runtime ALLOW
Runtime Route Ready != Execution Authorized
```

必须继续遵循 D01 Permission。

Provider Healthy + Adapter Ready 不能覆盖 BLOCK / HOLD。

---

## 55. Scope / Project Boundary

```text
Provider Eligible Somewhere != Provider Eligible Everywhere
Same Provider != Shared Authorization
Previous Action Provider != Next Action Automatically Valid Provider
```

Runtime Route 必须保持当前 Action Scope 可解释。

---

## 56. No Provider / Adapter God Object

Provider 不得吞并 Context Resolution / Scope Decision / Permission / Authority / Canonical Mutation Governance。

Adapter 不得吞并 Provider Resolution / Authorization / Permission / Context Ownership / Semantic Decision / Governance Routing。

---

## 57. Normal Developer Experience

```text
Action Ready
↓
Resolve effective governed Provider
↓
Check runtime availability
↓
Resolve compatible Adapter
↓
If primary unavailable:
  auto use governed compatible fallback
↓
Continue
```

普通 Provider timeout、等价 Adapter 切换、可自动恢复路由问题不应默认打扰用户。

---

## 58. Human Attention Boundary

只有类似以下情况才需要用户或相应治理主体：

```text
Provider switch changes material semantics
Provider switch changes security / data boundary
Provider switch enlarges Scope / Authority
Multiple legitimate incompatible choices remain
New high-impact Provider authorization required
Existing governance explicitly requires human authority
```

---

## 59. Architecture / Implementation Separation

D03 不冻结：

```text
Exact Provider Interface
Exact Adapter Interface
Exact Provider Registry
Exact Adapter Registry
Exact Capability Schema
Exact Health Check Protocol
Exact Fallback Algorithm
Exact Ranking Algorithm
Exact Cost Formula
Exact Latency Formula
Exact Retry Count
Exact HTTP / CLI / MCP implementation
Exact SDK
Exact Provider credentials
Exact Provider configuration file
Exact Runtime API
Exact storage
Exact cache
```

---

## 60. AI Autonomous Boundary

自动 Provider / Adapter Routing 属于既有治理约束下的确定性运行时解析，不代表 AI 自行创造 Provider、授予 Provider Authorization、修改 Provider Policy、永久 Rebind Project 或自主学习并激活新路由规则。

---

## 61. Core Invariants

```text
Provider Binding != Runtime Provider Resolution
Runtime Provider Resolution != Adapter Routing
Runtime Provider Selection != Durable Provider Rebinding
Capability != Provider
Provider Health != Capability
Provider Available != Provider Eligible
Provider Available != Provider Authorized
Technical Compatibility != Semantic Compatibility
Fallback != Retry
Provider != Provider Routing Authority
Provider Failure != Provider Binding Invalid
Adapter = Execution Mechanism
Adapter != Semantic Decision Authority
Adapter Capability != Runtime Permission
Adapter Ready != Authorization
Adapter != Scope Authority
Adapter != Provider Selector
Adapter Technical Capability != Execution Contract Compatibility
Adapter Failure != Provider Invalid
Runtime Route != Provider Binding
Runtime Route Ready != Runtime ALLOW
More Providers != More Authority
Same Provider != Shared Authorization
Multiple Providers != Human Decision Required
Operational Difference != Material Semantic Difference
Cheapest != Automatically Preferred
Fastest != Automatically Preferred
```

---

## 62. Forbidden Interpretations

明确禁止：

1. F10 建第二套 Provider Binding Governance；
2. F10 随意加入未治理 Provider；
3. Provider 技术可用就视为合法；
4. Provider Healthy 自动等于 Authorized；
5. Primary 临时失败就永久 Rebind；
6. Runtime Fallback 自动改变 Project Binding；
7. Provider 自己决定下一个 Provider；
8. 最快/最便宜无条件获胜；
9. 多个合法 Provider 就默认询问用户；
10. 多个合法 Provider 随机选择；
11. Provider 切换改变安全/数据边界仍自动继续；
12. Provider 能生成代码就认为语义完全兼容；
13. 一个 Task 必须永久使用一个 Provider；
14. 一个 Provider 必须只有一个 Adapter；
15. Adapter 能调用 Provider 就认为满足执行合同；
16. Adapter 自己扩大 Target / Scope；
17. Adapter 自己解析 Authorization；
18. Adapter Ready 自动等于 Runtime ALLOW；
19. Adapter Failure 自动等于 Provider Binding 失效；
20. Provider Failure 自动等于 Adapter Failure；
21. Core 硬编码商业 Provider；
22. 编辑器身份自动赋予 Authority；
23. Route Cache 成为 Durable Binding；
24. Provider / Adapter Resolution 绕过 D01 BLOCK / HOLD；
25. D03 Approval 自动授权真实项目执行或解除 Dry-run / Final Activation 限制。

---

## 63. 与 F8 / D01 / D02 的关系

F8：继续负责 Provider Binding / Eligibility / Selection Governance / Fallback Governance / Version / Compatibility / Effective Project Context。

D01：决定当前 Action 是否可执行；D03 只提供 Provider / Adapter 相关运行时条件。

D02：提供 Action-specific Minimum Sufficient Execution Context；D03 不能反向吞并 Context Authority。

---

## 64. 后续边界

D03 不完整冻结：

```text
Retry
Pause
Resume
Failure Classification
Recovery
Cancel
Lifecycle state machine
```

这些进入后续 F10 Lifecycle / Recovery Decision。

---

## 65. Acceptance Meaning

用户已明确批准：

```text
F10-D03 HUMAN_APPROVED
```

因此正式成立：

```text
F8 Provider Governance remains authoritative
F10 owns action-scoped runtime provider resolution
Runtime selection does not create durable rebinding
Only governed compatible fallbacks may auto-switch
Provider health / capability / eligibility / authorization are separated
Deterministic provider selection is automatic
Human involvement only for genuine material unresolved choices
Provider cannot self-route to arbitrary providers
Adapter is an execution mechanism, not semantic authority
One provider may have multiple adapters
Adapter routing must satisfy execution contract
Core remains provider/editor neutral
Runtime route is derived and rebuildable
```

但不表示批准任何 Implementation、真实项目写入、RP2、Authority Cutover、Canonical Replacement、Final Activation 或 Legacy Retirement。

---

## 66. Approval Status

```text
F10-D03 = HUMAN_APPROVED
```

普通“好的 / 下一步 / 继续 / 按建议继续”均不代表后续 Decision 的批准。

---

**END**

# Stage 07 → Stage 08 Gate Review v1.0

> Review Basis：Stage 07 Acceptance Report、VALIDATION_RESULTS、NOLOSS_COVERAGE_REPORT、MIGRATION_BLOCKER_REGISTER、NEXT_STAGE_HANDOFF  
> Stage 07 Run：`stage07-20260920T152653Z`  
> Review Result：**PASS_FOR_STAGE08_PRD_UI_GOVERNANCE_DESIGN_WITH_TYPED_BLOCKERS**  
> Stage 08 Execution：**NOT_STARTED / NOT_AUTHORIZED**

---

## 1. Gate 结论

```text
Stage 07 = COMPLETED
Stage 07 Acceptance = PASS_NOLOSS_SHADOW_DESIGN_WITH_TYPED_BLOCKERS
Real Migration = MIGRATION_BLOCKED
Stage 08 Design Gate = PASS_FOR_STAGE08_PRD_UI_GOVERNANCE_DESIGN_WITH_TYPED_BLOCKERS
Stage 08 Execution = NOT_STARTED
```

Stage 07 的真实迁移仍被 Typed Blockers 阻塞，但这些 Blocker 不阻止 Stage 08 进行 PRD × UI_SPEC Governance 设计。

原因：

```text
Stage 08 不要求真实迁移
Stage 08 不切换 Canonical Truth
Stage 08 不创建正式 .banyan
Stage 08 只冻结治理 Contract / Projection / Approval / Version 规则
```

---

## 2. Stage 07 已验证输入

No-Loss Coverage：

```text
Capability = 35 / 35
Legacy Asset = 1026 / 1026
Canonical Artifact = 330 / 330
Derived Artifact = 95 / 95
Operational Artifact = 289 / 289
Reference Edge = 108 / 108
```

V07-01～V07-22 全部 PASS。

8 个 Hard Metrics 全部为 0。

Stage 07 未执行 Canonical Apply，未创建 `.banyan`，未修改 Legacy / Business 文件。

---

## 3. Stage 07 Typed Blockers

真实迁移继续：

```text
MIGRATION_BLOCKED
```

主要 Blocker：

```text
CON-002 = OPEN / Owner Stage 12
4 条历史文档引用缺目标 / Owner Stage 12
R03-PURITY
R03-SOURCE
R03-COST
R03-SECRET
R03-LOCAL
```

另有 2 条 Scanner Finding：

```text
REF-107
REF-108
```

已确认是正则字面量，不是真实 Reference，不应重新升级为缺失引用。

Stage 08 必须继承这些事实，不得伪造迁移 Ready。

---

## 4. Stage 08 正式职责

Stage 08 进入：

```text
PRD × UI_SPEC Governance
```

要冻结：

```text
PRD Canonical Authority Contract
UI_SPEC Role / Authority Contract
UI_SPEC Enablement Contract
Application-scoped UI Governance
PRD ↔ UI_SPEC Trace Contract
UI Design Input / Evidence Contract
UI_SPEC Draft / Review / Approval Lifecycle
Version Coupling Rules
Change Workspace Integration
UI_SPEC Update / Supersession Rules
UI Implementation Readiness Gate
UI Validation Evidence Contract
Cross-application isolation rules
No-second-truth rule
```

---

## 5. PRD / UI_SPEC 权威边界

必须保持：

```text
PRD = Product / Business Requirement Canonical Truth
UI_SPEC = Approved UI Contract / Implementation Constraint Projection
```

UI_SPEC 不能成为第二套业务需求真源。

禁止：

```text
在 UI_SPEC 中偷偷改变业务规则
通过设计图反推并覆盖 PRD
由 Implementation 结果反向改写 PRD
多个 UI_SPEC 各自维护一套相同业务规则
```

业务规则变化必须回到：

```text
Change Workspace
→ Decision
→ PRD / Canonical Apply
→ UI_SPEC refresh / re-approval
```

---

## 6. UI_SPEC 可选启用原则

继承 v3.1 已有：

```text
ENABLE_UI_SPEC_GENERATION
UI_SPEC_ENABLED_APPLICATIONS
```

Stage 08 应抽象为通用 Contract：

```text
project-level default gate
application-level activation
explicit disable
partial coverage
```

规则：

```text
未启用 UI_SPEC 的应用不能被强制走 UI_SPEC
启用名单为空时不得猜测全部启用
Partial 覆盖必须显式
```

具体变量名可以保留 Compatibility Mapping，但 Generic Core 不绑定 v3.1 字符串。

---

## 7. Application Scope

UI Governance 必须以 Application 为作用域。

同一仓库可能：

```text
多个 Web
App
Mini Program
H5
Admin
Shared UI Package
```

不能假设：

```text
一份 UI_SPEC = 全仓 UI
```

必须定义：

```text
application_id
surface_scope
shared_component_scope
design_source_scope
ui_spec_status
coverage
```

---

## 8. Design Source / UI_SPEC / Implementation

Stage 08 冻结的主链：

```text
PRD / Approved Change
↓
UI Scope
↓
Design Evidence
↓
Draft UI Contract
↓
Human / Workflow Gate
↓
Approved UI_SPEC
↓
Implementation Readiness
↓
Stage 09 Design Intelligence / later Coding
```

设计图、AnyDesign、Figma、截图、原型都是 Evidence / Design Source，不自动成为 Canonical Product Requirement。

---

## 9. Version / Freshness

必须分别跟踪：

```text
PRD version
UI_SPEC version
Design evidence version
Implementation baseline
Validation baseline
```

UI_SPEC 必须声明：

```text
derived_from_prd
derived_from_change
design_evidence_refs
coverage
freshness
supersedes
```

若 PRD 发生相关变化：

```text
UI_SPEC -> STALE / REVIEW_REQUIRED
```

不能静默视为仍有效。

最终 Source Freshness 总策略仍由 CON-002 / Stage 12 处理；Stage 08 只冻结 UI Governance 所需的局部 freshness 语义。

---

## 10. Stage 09 边界

Stage 08 不实现 AnyDesign / Design Intelligence。

Stage 08 只定义：

```text
需要什么 Design Evidence
如何进入 UI_SPEC
什么算 Approved
如何追踪
什么时候 stale
什么时候能进入 implementation
```

Stage 09 才负责：

```text
Design Intelligence
Scene / Semantic / Token / Behavior / Visual Analysis
```

---

## 11. Low-Token 原则

Stage 08 默认读取：

```text
本 Gate Review
Stage 08 Low-Token Input Index
Stage 07 Handoff / No-Loss Compatibility
Stage 06 Change / Apply contracts
Stage 05 Decision / Human Confirmation
Stage 03 CAP-PRD / CAP-UI_SCOPE / CAP-UI_CONTRACT / CAP-UI_GATE contracts
Stage 01/02 相关 UI Governance Evidence 定点读取
```

禁止：

```text
重新扫描 Repository
重新读取全部 1026 Asset 正文
重新分析 35 Capability 全集
全量读取所有设计文档
```

---

## 12. Gate Decision

```text
Stage 07 → Stage 08 = PASS_FOR_STAGE08_PRD_UI_GOVERNANCE_DESIGN_WITH_TYPED_BLOCKERS
Stage 08 Pack Generation = ALLOWED
Stage 08 Execution = NOT YET AUTHORIZED
```

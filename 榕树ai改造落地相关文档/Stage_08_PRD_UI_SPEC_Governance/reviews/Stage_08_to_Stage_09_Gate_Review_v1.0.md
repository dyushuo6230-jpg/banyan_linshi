# Stage 08 → Stage 09 Gate Review v1.0

> Review Basis：Stage 08 Acceptance Report、VALIDATION_RESULTS、STAGE08_COVERAGE_REPORT、NEXT_STAGE_HANDOFF  
> Stage 08 Run：`stage08-20260920T153936Z`  
> Review Result：**PASS_FOR_STAGE09_UI_DESIGN_INTELLIGENCE_DESIGN_WITH_INHERITED_BLOCKERS**  
> Stage 09 Execution：**NOT_STARTED / NOT_AUTHORIZED**

---

## 1. 最终结论

```text
Stage 08 = COMPLETED
Stage 08 Acceptance = PASS_UI_GOVERNANCE_CONTRACT_FREEZE_WITH_INHERITED_BLOCKERS
Stage 09 Entry Gate = PASS_FOR_STAGE09_UI_DESIGN_INTELLIGENCE_DESIGN_WITH_INHERITED_BLOCKERS
Stage 09 Execution = NOT_STARTED
```

Stage 08 已冻结 PRD × UI_SPEC 权威关系、应用级 Scope、Enablement、Design Evidence、Approval、Trace、Version/Freshness Effect 和 Implementation Readiness。

Stage 09 可以进入 UI Design Intelligence 设计。

---

## 2. Stage 08 已验证成果

```text
PRD = BUSINESS_PRODUCT_REQUIREMENT_CANONICAL_TRUTH
UI_SPEC = APPROVED_UI_CONTRACT_PROJECTION
Design Source = EVIDENCE_ONLY
Owned Outcomes = 12 / 12 frozen
V08-01..V08-20 = PASS
Hard Metrics = 7 / 7 all zero
```

未修改 Canonical PRD/UI_SPEC，未创建正式 `.banyan`，未进入 Stage 09。

---

## 3. Stage 09 正式职责

Stage 09 进入：

```text
UI Design Intelligence
```

必须设计并冻结：

```text
Design Source Intake Contract
Design Provider Port
Normalized Scene Schema
Layer / Geometry Schema
Semantic Tree Schema
Design Truth Contract
Design Token Contract
Behavior Evidence / State Contract
Data Evidence / Fixture Boundary
Confidence / Provenance Model
FACT / INFERENCE / RECOMMENDATION separation
Implementation IR input contract
Visual Validation Input Contract
Design Drift Contract
Design Package Contract
Provider-neutral AnyDesign / Figma / Image adapters
```

---

## 4. 核心原则

Stage 09 必须保持：

```text
少猜测，多结构化
Design Source = Evidence
Normalized Scene = Provider-neutral
Semantic = Inference
Implementation Suggestion = Recommendation
```

不得把：

```text
INFERENCE
RECOMMENDATION
```

伪装成：

```text
FACT
```

---

## 5. 设计源与 Provider

Generic Core 不绑定：

```text
AnyDesign
Figma
墨刀
具体视觉模型
具体 OCR/Parser
```

这些都属于 Provider。

Core 只消费统一：

```text
Normalized Scene
Design Evidence
Semantic Tree
Design Truth
Behavior/Data Evidence
```

---

## 6. Geometry / Layout 边界

设计图里观察到：

```text
width = 280
height = 180
```

只能先表达为：

```text
renderedGeometry
```

不能自动推断：

```text
CSS fixed width = 280
CSS fixed height = 180
```

固定尺寸必须有更强证据。

Stage 09 应冻结：

```text
observed geometry
layout relation
constraint evidence
sizing behavior confidence
```

---

## 7. Behavior / Interaction 边界

静态设计图无法证明：

```text
hover
selected
disabled
loading
drag
scroll
gesture
animation
API behavior
```

若无证据：

```text
UNKNOWN
```

不能猜。

已有原型/多状态设计/现码/明确 UI_SPEC 才能成为行为证据。

---

## 8. Design Truth 与 UI_SPEC

Stage 08 已冻结：

```text
UI_SPEC = Approved UI Contract Projection
```

Stage 09 输出的 Design Truth / Scene / Semantic 不能自动升级为 UI_SPEC。

链路必须：

```text
Design Intelligence Output
→ Evidence / Draft Contract Input
→ Stage 08 Approval Governance
→ Approved UI_SPEC
```

---

## 9. Stage 10 / 后续边界

Stage 09 不负责：

```text
长期 Project Guide / Knowledge Publishing
Runtime CLI
前端代码生成 Executor
Visual Repair Runtime
Control Plane UI
```

Stage 09 只冻结 Design Intelligence 的结构化中间层和 Provider 接口。

---

## 10. 继承 Blockers

真实迁移继续：

```text
MIGRATION_BLOCKED
```

保留：

```text
CON-002
4 条历史缺目标引用
R03-PURITY
R03-SOURCE
R03-COST
R03-SECRET
R03-LOCAL
```

Stage 09 不解决 CON-002。

---

## 11. Low-Token 原则

默认读取：

```text
本 Gate Review
Stage 09 Low-Token Input Index
Stage 08 Design Evidence / UI_SPEC / Readiness contracts
Stage 03 CAP-UI related contracts
Stage 01/02 UI Design capability evidence 定点读取
已登记的 UI Design Pack / Implementation / Layout Guidance 文档
```

禁止：

```text
重扫 Repository
重读所有项目文档
重做 Stage 01 Inventory
全量读取所有 UI 图片/设计资源
```

---

## 12. Gate Decision

```text
Stage 08 → Stage 09 = PASS_FOR_STAGE09_UI_DESIGN_INTELLIGENCE_DESIGN_WITH_INHERITED_BLOCKERS
Stage 09 Pack Generation = ALLOWED
Stage 09 Execution = NOT YET AUTHORIZED
```

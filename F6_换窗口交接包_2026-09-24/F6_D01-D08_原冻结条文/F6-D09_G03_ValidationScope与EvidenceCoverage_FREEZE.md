# F6-D09 — G03 Validation Scope × Actual Observation × Evidence × Coverage 冻结条文

- **Stage**: F6
- **Decision**: F6-D09
- **Group**: 03
- **Status**: HUMAN_APPROVED
- **Freeze Status**: Architecture Freeze PASS
- **Type**: UI Conformance / Validation Scope & Evidence Governance
- **Date**: 2026-09-24

## 1. Validation Scope 必须显式，禁止自动扩大

每个 UI Conformance Session 都必须明确本轮 Validation Scope。

Scope 至少允许按以下维度组合限定：

- Application
- Page
- Region
- Component
- State
- Interaction
- Viewport / Device
- Data Scenario

例如：

```text
Application = tenant-admin
Page = 素材管理
Region = 上传进度弹框
State = 上传中
Viewport = Desktop
```

则本轮只能对上述已声明范围形成正式判断。

未明确纳入当前 Session Scope 的对象，应标记为：

```text
OUT_OF_SCOPE
```

或：

```text
NOT_EVALUATED
```

不得因为其与当前对象相邻、相关或容易访问，就自动扩大到：

- 整页；
- 整个 Application；
- 相邻组件；
- 其它状态；
- 其它交互；
- 其它设备；
- 其它数据场景。

正式原则：

```text
Explicit Scope
>
AI Inferred Scope
```

并且：

```text
未明确纳入 Scope
!=
默认允许检查或处理
```

---

## 2. 未检查不得写成 PASS

Validation Result 必须严格区分：

```text
Observed / Evaluated
```

与：

```text
Unobserved / Not Evaluated
```

例如目标对象存在：

```text
Default
Selected
Hover
Loading
Empty
Error
Disabled
```

而本轮只验证：

```text
Default
Selected
```

则结果必须分别记录：

```text
Default  = PASS
Selected = PASS

Hover    = NOT_EVALUATED
Loading  = NOT_EVALUATED
Empty    = NOT_EVALUATED
Error    = NOT_EVALUATED
Disabled = NOT_EVALUATED
```

不得将局部验证结果总结为：

```text
整个页面 PASS
```

正式冻结：

```text
Partial PASS
!=
Whole Scope PASS
```

以及：

```text
Unobserved
!=
PASS
```

---

## 3. Actual Observation 必须来自可追踪 Evidence

D09 对当前实际状态的判断必须来自可追踪证据，不得依赖：

- AI 模糊记忆；
- 未验证的历史描述；
- 不可追踪的印象判断；
- 无来源的推断。

Actual Observation 可以来自：

- Rendered UI
- Screenshot
- Browser Runtime
- DOM
- Layout Observation
- Computed Geometry
- Interaction Trace
- Automated Test
- Manual Validation Evidence
- Accessibility Observation

关键 Observation 应尽可能关联：

- Source
- Environment
- Scope
- State
- Viewport / Device
- Revision / Commit
- Timestamp / Run
- Provider Trace

例如：

```text
Observed:
二级分类胶囊高度 = 46rpx

Evidence:
Browser Runtime
Page = category
State = selected
Revision = abc123
```

而不是：

```text
“我记得这里大概是 46rpx”
```

---

## 4. Observation 只表达 Actual，不产生 Target Authority

Actual Observation 只能说明：

> 当前真实观察到了什么。

例如：

```text
Observed Width = 132px
```

只能证明：

```text
Actual Width = 132px
```

不能推出：

```text
Required Width = 132px
```

同样：

```text
Observed DOM
!=
Required DOM

Observed CSS
!=
Approved Implementation Strategy

Current Component Structure
!=
Design Requirement
```

正式冻结：

```text
Observation
= Actual Evidence

Observation
!= Target Authority
```

该原则与 G02 的：

```text
Existing Reality
!=
Design Truth
```

保持一致。

---

## 5. Evidence 不足时允许 UNKNOWN，禁止 AI 补全

如果当前 Target / Evidence 没有定义某一状态、交互、响应式行为或视觉参数，则 D09 不得为了形成完整报告而自行补全。

合法状态至少包括：

```text
UNKNOWN
NOT_SPECIFIED
TARGET_COVERAGE_GAP
EVIDENCE_INSUFFICIENT
```

例如：

```text
Hover Behavior
=
NOT_SPECIFIED
```

表示当前证据不足以形成判断。

这不是 Validation Failure，而是明确的 Evidence Boundary。

D09 禁止：

- 脑补状态；
- 脑补交互；
- 脑补响应式规则；
- 脑补视觉参数；
- 脑补业务行为；
- 用常识或模型习惯替代当前治理证据。

正式原则：

```text
明确不知道
>
自信地猜
```

---

## 6. Validation Coverage 必须显式记录

一次 Validation Result 不能只有：

```text
PASS
```

还必须说明：

> 本轮到底验证了多少。

Validation Coverage 至少应支持记录：

1. Target Coverage
2. State Coverage
3. Interaction Coverage
4. Viewport / Device Coverage
5. Data Scenario Coverage
6. Evidence Coverage

例如：

```text
Target Coverage
= 一级分类 + 二级分类

State Coverage
= 默认态 + 选中态

Interaction Coverage
= 一级切换 + 二级切换

Viewport Coverage
= 390×844

Data Scenario Coverage
= 正常分类数据

Evidence Coverage
= Screenshot + Browser DOM
```

因此：

```text
PASS
```

实际必须解释为：

```text
PASS
within declared coverage
```

而不是：

```text
整个系统全部通过
```

Coverage 不完整时，允许：

```text
PARTIAL_PASS
```

但必须同时列出：

- 未覆盖对象；
- 未覆盖状态；
- 未覆盖交互；
- 未覆盖设备；
- 未覆盖数据场景；
- 未覆盖证据类型。

---

## 7. G03 完整判断链路

正式链路：

```text
Session
↓
Resolve Explicit Scope
↓
Resolve Target
↓
Collect Actual Evidence
↓
Record Observation
↓
Check Evidence Sufficiency
↓
Calculate Coverage
↓
Only evaluate covered scope
↓
PASS / PARTIAL_PASS / FAIL / UNKNOWN / NOT_EVALUATED
```

---

## 8. 核心冻结边界

G03 正式冻结以下边界：

```text
未检查
!=
PASS

Observation
!=
Design Truth

Evidence Insufficient
!=
AI Guess

Partial PASS
!=
Whole Scope PASS
```

---

## 9. 冻结结论

本组正式冻结：

1. Validation Scope 必须显式；
2. Scope 不得由 AI 自动扩大；
3. 未纳入 Scope 的对象必须标记 OUT_OF_SCOPE / NOT_EVALUATED；
4. 未检查不得写成 PASS；
5. Partial PASS 不等于 Whole Scope PASS；
6. Actual Observation 必须来自可追踪 Evidence；
7. Actual Evidence 应尽可能携带环境、状态、版本、视口和 Trace；
8. Observation 只表达 Actual，不产生 Target Authority；
9. Evidence 不足时允许 UNKNOWN / NOT_SPECIFIED / TARGET_COVERAGE_GAP / EVIDENCE_INSUFFICIENT；
10. D09 不得脑补缺失状态、交互、视觉规则、响应式规则或业务行为；
11. Validation Coverage 必须显式；
12. PASS 只能在已声明 Coverage 内成立；
13. Coverage 不完整时允许 PARTIAL_PASS，但必须明确未覆盖范围。

---

**HUMAN_APPROVED — 2026-09-24**

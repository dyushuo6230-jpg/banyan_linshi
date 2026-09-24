# F6-D09 — G04 Difference × Drift × Legal Alternative × Approved Deviation 冻结条文

- **Stage**: F6
- **Decision**: F6-D09
- **Group**: 04
- **Status**: HUMAN_APPROVED
- **Freeze Status**: Architecture Freeze PASS
- **Type**: UI Conformance / Drift Classification Governance
- **Date**: 2026-09-24

## 1. Difference 与 Drift 必须严格分开

Difference 只表示：

```text
Target
!=
Actual
```

它只表达目标与实际之间存在差异。

Difference 出现后，必须继续结合：

- Scope
- Applicability
- Tolerance
- Responsive Rule
- Dynamic Data
- Legal Alternative
- Approved Deviation
- Target Freshness
- Evidence Sufficiency

进行判断，之后才能决定是否构成 Drift。

正式冻结：

```text
Difference
!=
Drift
```

例如：

```text
设计样例中的商品名称
!=
运行时真实商品名称
```

只要数据来源、布局、截断、展示规则均符合正式 Target，则该差异可以被判定为：

```text
EXPECTED_VARIATION
```

而不是 Drift。

---

## 2. Drift 必须分类，不能只输出“有差异”

D09 的 Drift Classification 至少应支持以下类别：

```text
VISUAL_DRIFT
STRUCTURAL_DRIFT
LAYOUT_DRIFT
STATE_DRIFT
INTERACTION_DRIFT
RESPONSIVE_DRIFT
DATA_PRESENTATION_DRIFT
ACCESSIBILITY_DRIFT
```

示例：

```text
目标圆角与实际圆角不符
→ VISUAL_DRIFT
```

```text
目标要求某模块属于指定容器，
实际模块脱离该容器
→ STRUCTURAL_DRIFT
```

```text
目标要求三列布局，
实际在无合法规则支持的情况下变成两列
→ LAYOUT_DRIFT / RESPONSIVE_DRIFT
```

Core Drift Class 必须允许未来扩展，不应因本阶段冻结当前类别而阻止后续新增合法类别。

---

## 3. Pixel Diff 只能作为 Evidence，不能成为最终正确性判据

正式冻结：

```text
Pixel Diff
!=
Visual Correctness
```

实际像素结果可能受以下因素影响：

- Browser
- Rendering Engine
- Font Rasterization
- Anti-aliasing
- Device Pixel Ratio
- Operating System
- Dynamic Content
- Responsive Adaptation

因此像素差异只能作为 Evidence。

最终一致性判断必须综合：

```text
Conformance Judgment
=
Target Rule
+
Semantic Relationship
+
Evidence
+
Allowed Tolerance
```

不得形成：

```text
像素不同
→ 自动 FAIL
```

也不得形成：

```text
像素接近
→ 自动 PASS
```

因为结构、层级、状态或交互语义可能已经发生偏离。

---

## 4. Legal Alternative 不得判为 Drift

如果正式 Target 只约束结果、布局关系或设计语义，而没有规定唯一实现方式，则多个实现方案可以同时合法。

例如：

```text
目标：
三个等宽列
固定列间距
自动适配容器
```

若实现分别采用：

```text
CSS Grid
```

或：

```text
Flex
```

且都满足正式 Target，同时没有更高 Authority 要求必须采用某一种实现，则二者属于合法替代实现。

正式分类：

```text
LEGAL_ALTERNATIVE
```

而不是：

```text
DRIFT
```

同理：

```text
CSS Triangle
```

与：

```text
SVG Triangle
```

如果 Target 只规定视觉结构，没有冻结具体技术实现，则技术手段不同不能单独构成 Drift。

正式保持：

```text
Geometry
!=
CSS

Design Intent
!=
One Mandatory Implementation
```

---

## 5. Expected Variation 必须与 Drift 分开

运行时存在大量合法动态变化，例如：

- 用户名长度不同；
- 商品名称不同；
- 商品价格不同；
- 图片内容变化；
- 合法图片比例变化；
- 列表数量变化；
- 时间文本变化；
- 分页数据变化；
- 响应式合法调整。

只要这些变化仍然符合正式：

- Layout Constraint
- Visual Rule
- State Rule
- Data Presentation Rule
- Responsive Rule

就应该分类为：

```text
EXPECTED_VARIATION
```

而不是 Drift。

禁止形成：

```text
真实运行数据
!=
设计图中的示例数据
→ 自动报错
```

该规则用于减少由动态内容导致的假阳性。

---

## 6. Approved Deviation 必须被识别

如果某个差异已经经过治理并获得明确批准，应登记为可追踪 Deviation。

Deviation 至少应能够关联：

- Deviation ID
- Scope
- Expected
- Actual
- Reason
- Approval
- Validity
- Version / Revision Context

当当前实际结果符合仍然有效的 Approved Deviation 时，应分类为：

```text
APPROVED_DEVIATION
```

不得每轮重新将其报告为普通 Drift。

Approved Deviation 必须：

```text
Scope-bound
Version-aware
Validity-aware
```

正式冻结：

```text
Approved Deviation
!=
Global Rule Change
```

一个 Scope 中已批准的偏差不得自动扩展到：

- 其它页面；
- 其它组件；
- 其它状态；
- 其它应用；
- 其它版本。

当 Deviation 已过期、被取代、适用范围变化或目标发生相关变更时：

```text
Deviation Expired
→ Re-evaluate
```

---

## 7. Difference 的正式分类出口

一个 Difference 经过 D09 判断后，至少允许进入：

```text
Difference
↓
├── DRIFT
├── ACCEPTABLE_DIFFERENCE
├── LEGAL_ALTERNATIVE
├── EXPECTED_VARIATION
├── APPROVED_DEVIATION
├── UNKNOWN
└── TARGET / EVIDENCE ISSUE
```

不得将校准逻辑退化为：

```text
一样 = PASS
不一样 = FAIL
```

---

## 8. 核心冻结边界

G04 正式冻结：

```text
Difference
!=
Drift

Pixel Diff
!=
Visual Correctness

Legal Alternative
!=
Drift

Expected Variation
!=
Drift

Approved Deviation
!=
Global Rule Change
```

---

## 9. 冻结结论

本组正式冻结：

1. Difference 与 Drift 必须严格分离；
2. Difference 只能说明 Target 与 Actual 不同；
3. Drift 必须经过 Scope、Applicability、Tolerance、Variation、Alternative、Deviation、Freshness 与 Evidence 判断；
4. Drift 必须支持分类；
5. Pixel Diff 只能作为 Evidence；
6. 像素不同不得自动 FAIL；
7. 像素接近不得自动 PASS；
8. 合法替代实现不得判为 Drift；
9. 运行时合法变化应分类为 EXPECTED_VARIATION；
10. 已批准且仍有效的偏差应分类为 APPROVED_DEVIATION；
11. Approved Deviation 必须绑定 Scope、Version 与 Validity；
12. Approved Deviation 不自动升级为全局规则；
13. Difference 的最终出口必须允许 DRIFT、LEGAL_ALTERNATIVE、EXPECTED_VARIATION、APPROVED_DEVIATION、UNKNOWN 等多种状态；
14. D09 不得采用“一样=PASS，不一样=FAIL”的简化模型。

---

**HUMAN_APPROVED — 2026-09-24**

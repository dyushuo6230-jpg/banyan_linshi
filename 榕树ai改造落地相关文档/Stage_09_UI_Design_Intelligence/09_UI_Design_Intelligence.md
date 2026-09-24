# Stage 09：UI Design Intelligence

## 1. 目标

把不同设计源转换为统一、可验证、可追踪的 Design Intelligence 中间层。

主链：

```text
Design Source
→ Raw Provider Output
→ Normalized Scene
→ Semantic Tree
→ Design Truth
→ Behavior / Data Evidence
→ Design Tokens
→ Implementation IR Input
→ Visual Validation Input
```

## 2. 三类信息

必须严格区分：

```text
FACT
INFERENCE
RECOMMENDATION
```

### FACT

设计源直接支持。

### INFERENCE

语义模型推断，例如：

```text
“这组节点可能是 Sidebar”
```

### RECOMMENDATION

实现建议，例如：

```text
“建议使用 CSS Grid”
```

三者不得互相冒充。

## 3. Provider-neutral Scene

Normalized Scene 只允许通用字段：

```text
id
parent_id
type
bounds
visible
children
style
asset_ref
source_ref
confidence
provenance
```

不能出现某 Provider 专属字段作为 Core 必需字段。

## 4. Geometry

设计源观察到的像素：

```text
rendered geometry
```

不等于：

```text
fixed CSS constraint
```

必须结合：

```text
multiple states
multiple viewports
explicit design constraints
token evidence
component semantics
```

才能提升为固定实现约束。

## 5. Semantic Tree

Semantic Tree 可以描述：

```text
Page
Header
Sidebar
Toolbar
Form
Table
Card
List
Dialog
Navigation
Content Region
```

但必须带 confidence / evidence。

低置信度不得自动升级为 Design Truth。

## 6. Behavior

行为事实只能来自：

```text
prototype
explicit UI_SPEC
multi-state design
interaction spec
existing verified implementation
user-confirmed rule
```

静态图没有表达的交互保持 UNKNOWN。

## 7. Data

设计里的示例文本/数字默认：

```text
DEMO / EVIDENCE
```

不能自动当真实业务数据或 API Contract。

## 8. Design Truth

Design Truth 汇总：

```text
supported facts
accepted semantic interpretation
approved constraints
known unknowns
conflicts
```

它仍然是 UI Governance 的输入，
不是自动批准的 UI_SPEC。

## 9. Design Token

Token 必须保留来源：

```text
source token
derived token
recommended token
```

不能把视觉抽样颜色自动升级为项目 Design System Canonical Token。

## 10. Implementation IR Input

Stage 09 只冻结 Implementation IR 的输入边界：

```text
scene
semantic
design truth
behavior
data evidence
tokens
layout evidence
confidence
```

真正生成 Framework-specific code 属于后续 Runtime。

## 11. Visual Validation Input

必须能定义：

```text
viewport
state
reference evidence
comparison region
expected tolerance class
known exclusions
```

Stage 09 不执行完整视觉修复循环。

## 12. Design Drift

Drift 必须区分：

```text
SOURCE_DRIFT
UI_SPEC_DRIFT
IMPLEMENTATION_DRIFT
VALIDATION_BASELINE_DRIFT
```

不能把所有差异都叫“页面不一致”。

## 13. 完成后

Stage 10 将消费结构化 Design / UI / Governance 信息，用于 Project Guide / Knowledge Publishing。

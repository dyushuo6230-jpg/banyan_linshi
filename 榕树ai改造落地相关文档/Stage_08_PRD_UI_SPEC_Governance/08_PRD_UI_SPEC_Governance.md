# Stage 08：PRD × UI_SPEC Governance

## 1. 目标

冻结 PRD、UI_SPEC、Design Evidence、Implementation 之间的权威关系。

核心：

```text
PRD / Approved Change
→ UI Application Scope
→ Design Evidence
→ Draft UI Contract
→ Approval
→ Approved UI_SPEC
→ Implementation Ready
```

## 2. 权威边界

PRD：

```text
产品/业务需求真源
```

UI_SPEC：

```text
批准后的 UI 行为/结构/视觉约束 Contract
```

UI_SPEC 不是第二套 PRD。

## 3. Application Scope

每份 UI_SPEC 必须绑定：

```text
application_id
surface_scope
coverage
shared_component_scope
```

不能默认整仓生效。

## 4. Enablement

UI_SPEC 是可选治理能力。

必须支持：

```text
DISABLED
ENABLED
PARTIAL
```

没有明确启用时不能自动生成/要求。

## 5. Design Evidence

Design Source 可以：

```text
PNG/JPG/SVG
Figma
墨刀/原型
AnyDesign 输出
现有页面截图
Design Token
现有组件库证据
```

但它们是 Evidence。

不能直接覆盖 PRD。

## 6. Lifecycle

建议：

```text
NOT_ENABLED
DRAFT
IN_REVIEW
APPROVED
PARTIAL_APPROVED
STALE
REVIEW_REQUIRED
SUPERSEDED
BLOCKED
```

## 7. Trace

UI_SPEC 必须记录：

```text
application_id
prd_refs
change_refs
design_evidence_refs
coverage
version
status
supersedes
validation_refs
```

## 8. Change Integration

PRD / Approved Change 发生 UI-relevant change 时：

```text
Impact Analysis
→ affected UI_SPEC
→ freshness transition
→ Draft Update
→ Review
→ Approval
```

禁止只改 UI_SPEC 不改正式业务需求。

## 9. Implementation Gate

只有：

```text
UI governance enabled
required coverage satisfied
UI_SPEC approved
PRD trace valid
design evidence valid
no blocking conflict
```

才可以：

```text
IMPLEMENTATION_READY
```

## 10. Stage 09 Handoff

Stage 09 消费：

```text
Design Evidence Contract
Approved UI_SPEC Contract
Application Scope
Validation expectations
```

并实现 Design Intelligence 设计。

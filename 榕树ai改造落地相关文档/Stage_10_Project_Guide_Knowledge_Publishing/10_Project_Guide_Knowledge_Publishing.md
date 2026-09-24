# Stage 10：Project Guide / Knowledge Publishing

## 1. 目标

把项目真源、批准后的 Contract、运行证据发布成长期可读、可导航、可追踪、可刷新的 Knowledge Projection。

主链：

```text
Canonical / Approved / Operational Sources
→ Knowledge Selection
→ Projection Rule
→ Audience View
→ Published Knowledge
→ Freshness / Rebuildability / Provenance
```

## 2. 知识不等于真源

必须区分：

```text
CANONICAL
AUTHORITATIVE_REFERENCE
DERIVED_PROJECTION
OPERATIONAL
HISTORICAL
DISCUSSION
```

Project Guide / Plain Document / Meeting Pack 默认：

```text
DERIVED_PROJECTION
```

除非被明确赋予别的 Source Role。

## 3. Project Guide

Project Guide 是长期入口。

应回答：

```text
项目是什么
有哪些应用/服务
正式真源在哪里
如何开始工作
如何发起 Change
如何做 Decision
如何看 UI Governance
如何测试/交付
如何看 Progress / Handover
如何判断文档是否新鲜
```

不复制所有 Canonical 正文。

## 4. Knowledge Projection

Projection 每条必须有：

```text
projection_id
source_refs
source_versions
projection_type
audience
coverage
freshness
rebuildability
provenance
generated_at
```

## 5. Audience View

同一事实可以面向：

```text
BUSINESS
PRODUCT
DEVELOPER
TESTER
OPERATOR
NEW_CONTRIBUTOR
AI_AGENT
```

生成不同 View。

但 View 只能：

```text
filter
summarize
reorganize
link
```

不能创建独立业务真源。

## 6. Plain Document

Plain Document 的通用语义：

```text
human-readable projection
single-direction sync
not second requirement truth
not direct change authority
```

Legacy 中文目录只做 Compatibility Projection。

## 7. Freshness

Projection 状态：

```text
FRESH
STALE
REVIEW_REQUIRED
BLOCKED
UNKNOWN
```

上游相关源发生变化：

```text
Projection
→ STALE / REVIEW_REQUIRED
```

## 8. Rebuildability

分类：

```text
REBUILDABLE
PARTIALLY_REBUILDABLE
NOT_PROVEN_REBUILDABLE
HUMAN_MAINTAINED
```

`NOT_PROVEN_REBUILDABLE` 禁止自动覆盖再生成。

## 9. Progress / Worklog

必须区分：

```text
CURRENT_STATUS
WORK_LOG
HISTORICAL_STATUS
DERIVED_SUMMARY
```

旧记录不能冒充当前状态。

## 10. Handover / Context

Handover 必须记录：

```text
current scope
completed work
open work
blockers
next actions
canonical refs
operational refs
freshness
```

Handover 是工作上下文，不替代 Canonical。

## 11. Architecture Diagram

架构图可以是：

```text
Canonical Architecture Diagram
Derived Explanation Diagram
Meeting Projection Diagram
```

必须标清 Source Role。

Derived 图不能自行改变架构事实。

## 12. Discussion / Meeting Pack

Discussion / Meeting Pack：

```text
TEMPORARY / DERIVED / DISCUSSION
```

不得升级为 Canonical。

会议新决策必须进入 Change / Decision / Canonical Apply 流程。

## 13. Publish Lifecycle

建议：

```text
DRAFT
PUBLISHED
FRESH
STALE
REVIEW_REQUIRED
SUPERSEDED
ARCHIVED
BLOCKED
```

## 14. Stage 11 Handoff

Stage 10 必须向 Stage 11 明确：

```text
哪些实体需要索引
哪些字段需要检索
哪些关系需要查询
哪些内容是可重建
哪些是真源
哪些是 Projection
哪些是 Operational / Historical
```

Stage 11 才实现 SQLite / Trace / History。

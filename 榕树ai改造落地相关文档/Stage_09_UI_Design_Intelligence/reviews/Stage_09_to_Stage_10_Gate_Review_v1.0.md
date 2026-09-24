# Stage 09 → Stage 10 Gate Review v1.0

> Review Basis：Stage 09 Acceptance Report、VALIDATION_RESULTS、STAGE09_COVERAGE_REPORT、MIGRATION_BLOCKER_CARRYOVER、NEXT_STAGE_HANDOFF  
> Stage 09 Run：`stage09-20260920T155444Z`  
> Review Result：**PASS_FOR_STAGE10_KNOWLEDGE_PUBLISHING_DESIGN_WITH_INHERITED_BLOCKERS**  
> Stage 10 Execution：**NOT_STARTED / NOT_AUTHORIZED**

---

## 1. 最终结论

```text
Stage 09 = COMPLETED
Stage 09 Acceptance = PASS_DESIGN_INTELLIGENCE_CONTRACT_FREEZE_WITH_INHERITED_BLOCKERS
Stage 10 Entry Gate = PASS_FOR_STAGE10_KNOWLEDGE_PUBLISHING_DESIGN_WITH_INHERITED_BLOCKERS
Stage 10 Execution = NOT_STARTED
```

Stage 09 已冻结 Provider-neutral 的 Design Intelligence 合同，并保持：

```text
Design Source = EVIDENCE_ONLY
FACT / INFERENCE / RECOMMENDATION 分离
Provider Runtime = OFF
UI_SPEC Auto Promotion = false
```

这些成果足以进入 Stage 10 的 Project Guide / Knowledge Publishing 设计。

---

## 2. Stage 09 已验证成果

```text
Owned Outcomes = 16 / 16 frozen
Legacy UI Design Capabilities = 9 / 9 mapped
Activated Legacy Design Provider = 0
V09-01..V09-22 = PASS
Hard Metrics = 8 / 8 all zero
```

未全量分析设计图库，未生成前端代码，未创建正式 `.banyan`。

---

## 3. Stage 10 正式职责

Stage 10 进入：

```text
Project Guide / Knowledge Publishing
```

目标是把已有 Canonical / Approved / Derived 信息发布为不同读者可消费的长期知识投影。

必须设计并冻结：

```text
Knowledge Source Authority Contract
Knowledge Projection Contract
Project Guide Contract
Human-readable Projection Contract
Plain Document Compatibility Contract
Knowledge Audience / View Contract
Knowledge Map / Navigation Contract
Projection Freshness Contract
Projection Rebuildability Contract
Generated Knowledge Provenance Contract
Progress / Handover Projection Contract
Architecture Diagram Projection Contract
Discussion / Meeting Pack Contract
Knowledge Publish / Refresh / Stale Lifecycle
No-Second-Truth Rule
Knowledge Publishing Provider Port
```

---

## 4. Knowledge Projection 不是真源

必须保持：

```text
Canonical Product/Architecture/Decision = Source Truth
Project Guide / Plain Document / Meeting Pack = Projection
```

禁止：

```text
在 Guide 中新增业务规则后直接让代码照着做
在白话文档里私自修改需求
在会议包里形成第二套 Canonical
Derived projection 反向覆盖 PRD / ADR / DEC / UI_SPEC
```

任何新规则必须先进入：

```text
Change Workspace
→ Decision / Approval
→ Canonical Apply
→ Projection Refresh
```

---

## 5. Plain Document 兼容原则

参考项目现有 Plain Document 体系明确是：

```text
给人看的可读译本
不是第二套需求
不是开工依据
```

Stage 10 必须保留这种单向投影语义。

现有：

```text
doc-map
总览
功能需求
分端页面
技术设计
架构图
PLAIN_SYNC
PLAIN_SYNC_GAPS
```

可以作为 Compatibility Projection，但 Generic Core 不绑定这些固定中文目录名。

---

## 6. Project Guide

Project Guide 应成为长期“项目怎么理解 / 怎么进入 / 怎么协作 / 去哪里找真源”的入口。

它不能承担：

```text
全部 PRD
全部 ADR
全部 API
全部 UI_SPEC
```

应承担：

```text
项目概览
Canonical Source Map
Application / Service Map
How to Work
Governance / Workflow Entry
Change / Decision Entry
UI Governance Entry
Testing / Delivery Entry
Knowledge Navigation
Freshness / Version Notice
```

---

## 7. Audience / View

同一真源可以有不同知识投影：

```text
Owner / Business
Product
Developer
Tester
Operator
New Contributor
AI Agent
```

但不能为每个 Audience 复制一套独立真源。

应通过：

```text
Projection
Filter
Summarize
Link
```

实现。

---

## 8. Freshness / Stale

Stage 10 需要冻结 Knowledge Projection 的局部 Freshness 语义：

```text
FRESH
STALE
REVIEW_REQUIRED
BLOCKED
UNKNOWN
```

当上游 Canonical / UI_SPEC / Architecture / Change 发生相关变化时：

```text
Projection -> STALE / REVIEW_REQUIRED
```

全局 Source Freshness 冲突 CON-002 仍由 Stage 12 处理。

Stage 10 不抢 Stage 12 Owner。

---

## 9. Rebuildability

每个生成知识产物必须明确：

```text
REBUILDABLE
PARTIALLY_REBUILDABLE
NOT_PROVEN_REBUILDABLE
HUMAN_MAINTAINED
```

若来源或生成规则不完整：

```text
不能自动再生成覆盖旧文件
```

这与 R03-SOURCE 一致。

---

## 10. Generated Knowledge Provenance

生成内容至少记录：

```text
source refs
source versions
projection rule
generated_at
generator/tool when available
confidence
coverage
freshness
```

若作者或生成器未知：

```text
UNKNOWN
```

不得猜测。

---

## 11. Progress / Handover

Progress / Handover 是重要 Project Knowledge，但需要区分：

```text
事实状态
当前工作上下文
Derived summary
Historical record
```

禁止把旧 Progress 里的陈旧状态继续投影为“当前事实”。

Stage 10 只冻结发布/投影规则；
Stage 11/12 再接入 Index / History / Freshness。

---

## 12. Stage 11 边界

Stage 10 不实现：

```text
SQLite Index
History DB
Trace Query Runtime
Full-text Search Runtime
Knowledge Retrieval Engine
```

Stage 11 才负责：

```text
SQLite Index / Trace / History Migration
```

Stage 10 只冻结：

```text
要索引什么
哪些字段必须可查询
哪些 Knowledge Projection 可重建
哪些是 Canonical / Derived / Operational
```

---

## 13. Low-Token 原则

默认读取：

```text
本 Gate Review
Stage 10 Low-Token Input Index
Stage 09 Handoff / Design Package contracts
Stage 08 PRD/UI_SPEC Authority
Stage 07 v3.1 Governance Compatibility
Stage 03 Source Role / Artifact / Provenance
Stage 01 CAP-KNOWLEDGE / Progress / Handover / Plain Document 定点 Evidence
```

禁止：

```text
重扫整个 docs/project
重建 1026 Asset Inventory
全文重读 71+ Plain Document 规划/正文
全量读取所有 PRD / ADR / API
```

---

## 14. 继承 Blockers

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

---

## 15. Gate Decision

```text
Stage 09 → Stage 10 = PASS_FOR_STAGE10_KNOWLEDGE_PUBLISHING_DESIGN_WITH_INHERITED_BLOCKERS
Stage 10 Pack Generation = ALLOWED
Stage 10 Execution = NOT YET AUTHORIZED
```

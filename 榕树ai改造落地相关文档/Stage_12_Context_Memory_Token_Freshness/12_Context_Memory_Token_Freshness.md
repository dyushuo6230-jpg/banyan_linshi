# Stage 12：Context / Memory / Token Optimization / Freshness

## 1. 目标

让 Banyan 在不重读全仓的情况下，能稳定回答：

```text
现在什么是真的？
什么是当前的？
什么是历史的？
这个任务最少需要读什么？
哪些内容必须进一步取证？
哪些 Summary 还能相信？
```

## 2. Context 层次

```text
CANONICAL_CONTEXT
APPROVED_CONTRACT_CONTEXT
CURRENT_OPERATIONAL_CONTEXT
DERIVED_PROJECTION_CONTEXT
HISTORICAL_CONTEXT
EPHEMERAL_TASK_CONTEXT
AI_WORKING_SUMMARY
```

## 3. Context Selection

选择上下文必须考虑：

```text
authority
freshness
relevance
task scope
decision state
open blockers
provenance
token budget
```

不是只按相似度召回。

## 4. Freshness

Freshness 决策顺序：

```text
Authority
→ Explicit Version/Status
→ Supersession
→ Approved Change Lineage
→ Source Role
→ Freshness Observation
→ Conflict
→ Human Decision if required
```

mtime 只可作为 observation，不可单独决定 winner。

## 5. Memory

Memory 是：

```text
recoverable working context / preference / project semantic cache
```

不是 Canonical Truth。

每条 Memory 至少：

```text
memory_id
subject
summary
source_refs
as_of
freshness
coverage
confidence
rebuildability
```

## 6. Context Recovery

恢复优先：

```text
Canonical
Approved
Current Operational
Current Handover
Current Progress
Relevant Trace
```

历史与派生内容仅补充。

## 7. Token Budget

任务先分：

```text
MANDATORY_CONTEXT
OPTIONAL_CONTEXT
ON_DEMAND_CONTEXT
EXCLUDED_CONTEXT
```

预算不足：

```text
compact optional
reuse cache
defer low-value evidence
```

不能删 Mandatory。

## 8. Compaction

允许压缩：

```text
long prose → structured summary
large history → latest valid state + relevant transitions
large reference graph → local subgraph
large docs → IDs + relevant excerpts
```

但必须保留：

```text
authority
freshness
provenance
blockers
open decisions
unknowns
```

## 9. 四条历史引用

本阶段应给出每条的 Typed Disposition：

```text
KEEP_UNRESOLVED_HISTORICAL
DELETED_HISTORICAL_TARGET
EXTERNAL_HISTORICAL_TARGET
SUPERSEDED_REFERENCE
RESOLVED_WITH_EVIDENCE
```

不能猜。

## 10. Stage 13

Stage 13 将使用本阶段输出做：

```text
Evidence
Impact
Event
Prompt Learning
```

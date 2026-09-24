# Stage 11：SQLite Index / Trace / History Migration

## 1. 定位

Stage 11 第一次允许构建真实 SQLite 文件，但只能是：

```text
SHADOW / REBUILDABLE INDEX
```

路径仅在：

```text
.banyan-refactor/stages/11/<run_id>/shadow/banyan_index.sqlite
```

它不是最终 `.banyan` 数据库，更不是真源。

## 2. 数据层次

```text
Canonical / Approved Source
        ↓
Structured Registry / Contract
        ↓
SQLite Rebuildable Index
        ↓
Query / Context / History
```

反向写回 Canonical：

```text
FORBIDDEN
```

## 3. 最低实体

必须覆盖：

```text
Artifact
SourceRole
Projection
Guide
Reference
Version
Status
Freshness
Provenance
Change
Decision
Handover
Progress
ProviderBinding
TraceEvent
HistoryEvent
UnresolvedReference
MigrationLedger
```

## 4. Stable ID

Path 是 Locator，不是 Identity。

优先：

```text
stable_id / artifact_id / contract_id / change_id / decision_id
```

路径变化不能制造一个“新实体”。

## 5. Reference Graph

必须保留：

```text
source_id
target_id_or_unknown
relationship
status
source_locator
target_locator_or_unknown
migration_strategy
evidence_refs
```

4 条历史缺目标引用：

```text
target = UNKNOWN
status = UNRESOLVED_REFERENCE
```

不能猜。

## 6. Trace

Trace 记录事件事实：

```text
event_id
event_type
subject_id
stage
run_id
actor_identity_or_unknown
timestamp_or_unknown
inputs
outputs
decisions
changes
result
evidence
```

Trace 不能授权动作。

## 7. History

History 是状态序列，不是“最新成功状态”。

必须保留：

```text
failed
stopped
reverted
blocked
archived
superseded
```

## 8. Freshness

Stage 11 只索引：

```text
freshness_state
source_version
observed_at
conflict_state
```

不解决 CON-002。

## 9. Rebuild Pipeline

Shadow DB 必须可以被删除后重新构建：

```text
structured inputs
→ normalize
→ import
→ integrity check
→ query verification
```

不得依赖人工在 DB 里补数据。

## 10. Secret

Secret 只允许 metadata：

```text
path
classification
restriction flags
exists
```

禁止正文/hash/value。

## 11. Stage 12

Stage 12 将用：

```text
freshness queries
history queries
trace queries
projection-source queries
unresolved-reference queries
```

做 Context / Memory / Token Optimization。

# Stage 10 → Stage 11 Gate Review v1.0

> Review Basis：Stage 10 Acceptance Report、VALIDATION_RESULTS、STAGE11_INDEX_REQUIREMENTS、MIGRATION_BLOCKER_CARRYOVER、NEXT_STAGE_HANDOFF  
> Stage 10 Run：`stage10-20260920T161325Z`  
> Review Result：**PASS_FOR_STAGE11_SHADOW_INDEX_TRACE_HISTORY_WITH_INHERITED_BLOCKERS**  
> Stage 11 Execution：**NOT_STARTED / NOT_AUTHORIZED**

---

## 1. 最终结论

```text
Stage 10 = COMPLETED
Stage 10 Acceptance = PASS_KNOWLEDGE_PUBLISHING_CONTRACT_FREEZE_WITH_INHERITED_BLOCKERS
Stage 11 Entry Gate = PASS_FOR_STAGE11_SHADOW_INDEX_TRACE_HISTORY_WITH_INHERITED_BLOCKERS
Stage 11 Execution = NOT_STARTED
```

Stage 10 已冻结 Knowledge Publishing 和 Stage 11 Index Requirements。

Stage 11 可以进入：

```text
SQLite Index / Trace / History
+
Structured Migration / Rebuildability
```

但只能先在 `.banyan-refactor/stages/11/<run_id>/` 内建立 **Shadow / Rebuildable Index**，不能创建最终 `.banyan` Runtime Truth。

---

## 2. Stage 10 已验证输入

Stage 10 明确冻结 Stage 11 最低索引实体：

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
```

最低关系：

```text
projection_to_source
source_to_projection
artifact_references
change_to_affected_artifact
handover_to_canonical
guide_to_canonical_source
stale_projection_to_upstream_change
```

Stage 10 同时明确：

```text
index_is_canonical_truth = false
index_is_rebuildable_layer = true
```

Stage 11 必须保持这一点。

---

## 3. Stage 11 正式职责

Stage 11 必须设计并实际验证一个 Shadow SQLite Index / Trace / History 模型。

至少完成：

```text
SQLite Logical Schema
Stable-ID Index Model
Artifact / SourceRole Index
Reference Graph
Projection / Guide Index
Change / Decision Index
Progress / Handover History
Provider Binding Index
Trace Event Model
Import / Rebuild Pipeline
Index Migration Ledger
Unresolved Reference Registry
Query Contract
Rebuildability / Integrity Validation
Shadow SQLite Build
Shadow Query Verification
```

---

## 4. Index 不是新真源

必须：

```text
Canonical / Approved Source = Truth
SQLite = Rebuildable Index / Query Layer
Trace = Operational Evidence
History = Indexed Historical View
```

禁止：

```text
手工在 SQLite 改需求
把 SQLite 内容反向覆盖 PRD/ADR/UI_SPEC
把 Index 中的 latest row 当成 Canonical winner
用 SQLite 自动解决 CON-002
```

SQLite 丢失后必须能够从已批准的 Source / Registry / Evidence 重建。

---

## 5. Shadow Implementation Boundary

Stage 11 可以实际生成：

```text
.banyan-refactor/stages/11/<run_id>/shadow/banyan_index.sqlite
```

以及：

```text
schema.sql
migration/import manifests
query validation results
integrity checks
```

但：

```text
不是最终 .banyan/index
不是正式 Runtime DB
不是 writable product truth
```

不得创建正式 `.banyan/`。

---

## 6. Low-Token / Structured-Input-First

Stage 11 必须优先消费：

```text
Stage 10 STAGE11_INDEX_REQUIREMENTS
Stage 03 Artifact / SourceRole / Provenance / Reference schemas
Stage 04 Project Instance mappings
Stage 05 Workflow / Decision registries
Stage 06 Change Workspace contracts
Stage 07 migration matrices
Stage 08 UI governance contracts
Stage 09 design intelligence contracts
Stage 10 knowledge projection contracts
Bootstrap Register / Trace
```

禁止：

```text
重新扫描整个仓库
重新解析全部 Legacy 正文
重跑 Git 全历史
重新生成 1026 Asset Inventory
```

只有缺失结构化字段时，才按 evidence_refs 定点回读。

---

## 7. Trace Model

Trace 至少支持：

```text
event_id
event_type
subject_id
actor_identity_or_unknown
stage
run_id
timestamp_or_unknown
source_refs
input_refs
output_refs
decision_refs
change_refs
status
result
evidence_refs
```

Trace 是证据，不是授权。

---

## 8. History Model

History 必须保留真实状态：

```text
created
draft
approved
applied
reverted
failed
stopped
archived
superseded
historical
```

不得：

```text
把 stopped/failed/reverted 历史改写成 success
只保留 latest 丢掉历史
```

---

## 9. Unresolved References

Stage 07～10 继承的：

```text
4 条历史文档引用缺少目标
```

Stage 11 必须进入：

```text
UNRESOLVED_REFERENCE
```

索引表/Registry。

不得伪造目标，也不得因为目标缺失而删除引用记录。

那 2 条已确认的正则字面量保持：

```text
NOT_A_REFERENCE
```

不能重新升级成 unresolved reference。

---

## 10. CON-002

继续：

```text
CON-002 = OPEN
Owner = Stage 12
```

Stage 11 可以索引：

```text
freshness_state
source_version
observed_at
conflict_state
```

但不能裁决最终 Source Freshness winner。

Stage 12 将消费 Stage 11 的索引/历史证据解决 Freshness / Context / Memory。

---

## 11. Secret / Privacy

13 个 Secret 继续：

```text
SECRET_METADATA_ONLY
```

SQLite 中最多允许：

```text
path
classification
restriction flags
existence metadata
```

禁止：

```text
body
body hash
copied value
secret-derived summary
```

---

## 12. Stage 12 Handoff

Stage 11 必须向 Stage 12 提供：

```text
Freshness Query Surface
Context Recovery Query Surface
Historical State Query Surface
Unresolved Reference Query Surface
Projection Source Query Surface
Trace / Evidence Query Surface
Index Rebuildability Report
```

Stage 12 才处理：

```text
Context / Memory / Token Optimization
CON-002
Freshness Policy
```

---

## 13. Gate Decision

```text
Stage 10 → Stage 11 = PASS_FOR_STAGE11_SHADOW_INDEX_TRACE_HISTORY_WITH_INHERITED_BLOCKERS
Stage 11 Pack Generation = ALLOWED
Stage 11 Execution = NOT YET AUTHORIZED
```

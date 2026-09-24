# Stage 06：Change Workspace Provider / OpenSpec / Canonical Apply

## 1. 目标

建立 Provider-neutral 的 Change Workspace 模型，并把 OpenSpec 作为 Provider 接入。

核心：

```text
Discussion
→ Change Workspace
→ Draft / Parallel Draft
→ Proposal
→ Review / Decision
→ Approved for Apply
→ Canonical Apply
→ Validation
→ Reconciliation
→ Archive / Historical
```

## 2. Generic Change Workspace

Generic Core 只理解：

```text
change_id
status
artifacts
relationships
decisions
evidence
apply_state
provider_binding
```

不得依赖：

```text
openspec/changes/
proposal.md
tasks.md
design.md
specs/
```

这些属于 Provider Binding。

## 3. OpenSpec

OpenSpec 是第一类 Provider。

Stage 06 设计：

```text
Banyan semantic object
↔ OpenSpec physical artifact
```

映射。

但不修改 OpenSpec 本身。

## 4. Change Identity

Change 必须有稳定 identity：

```text
change_id
provider_change_id
project_instance_id
status
created_from
supersedes
related_task/change/batch
```

Provider Change ID 不能替代 Banyan stable ID。

## 5. Draft / Parallel Draft

允许：

```text
一个需求
→ 多个 Draft Candidate
→ 各自 Evidence / Impact
→ Decision Gate
→ 选定 / 合并 / 保留
```

AI 不自动选最后修改的 Draft。

## 6. Promotion

Draft Promotion 必须显式：

```text
PROMOTION_REQUESTED
PRECHECK
CONFLICT_CHECK
HUMAN/WORKFLOW_GATE
PROMOTED
VALIDATED
```

## 7. Canonical Apply

必须：

```text
Apply Preview
Impact Analysis
Reference Integrity
Freshness / Divergence Check
Decision Gate
Authorization
Apply Plan
Apply
Post-Validation
Evidence
Reconciliation
```

Stage 06 不执行真实 Apply。

## 8. Canonical Truth

Canonical 来源由 Source Role / Mapping 决定。

Change Workspace：

```text
不是 Canonical
```

即使 Provider 把某文件称为 “spec”，也不能自动获得 Canonical 权威。

## 9. Apply Preview

Preview 必须回答：

```text
将新增什么
将修改什么
将 supersede 什么
哪些引用受影响
哪些未决冲突
哪些 Artifact 保留
哪些 Derived 需要重建
回滚点在哪里
```

## 10. Reference Integrity

Apply 不能：

```text
删除仍被引用的 Artifact
复用旧 ID 给新主题
覆盖 UNKNOWN provenance
自动重新生成不可证明重建的产物
```

## 11. Reconciliation

Apply 后必须验证：

```text
Canonical state
Change Workspace state
Reference graph
Derived projection
Trace
```

一致性。

## 12. Archive

Archive 是状态转换，不代表删除。

Provider 可以有 archive 实现，但 Core 语义是：

```text
ACTIVE
APPLIED
RECONCILED
ARCHIVED
HISTORICAL
```

物理移动/删除属于 Provider/后续实现策略。

## 13. 完成后

Stage 07 才能使用这些 Contract 去做参考项目 v3.1 Legacy / No-Loss Migration。

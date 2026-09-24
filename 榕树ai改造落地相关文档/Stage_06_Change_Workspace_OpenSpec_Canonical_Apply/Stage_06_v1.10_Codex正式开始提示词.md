# Stage 06 v1.10 — Codex 正式开始提示词（低 Token）

这是 Stage 06 正式执行，不是重跑 Stage 01～05。

当前阶段：

```text
Stage 06 — Change Workspace Provider / OpenSpec / Canonical Apply
```

## 1. 先读最小输入

```text
榕树ai改造落地相关文档/Stage_05_Adaptive_Workflow_Decision_Semantic_Commit/reviews/Stage_05_to_Stage_06_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_05_Adaptive_Workflow_Decision_Semantic_Commit/reviews/Stage_06_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_06_Change_Workspace_OpenSpec_Canonical_Apply/
```

然后只加载低 Token 索引列出的 Stage 05 / 04 / 03 冻结输入。

## 2. 核心原则

```text
Change Workspace = Generic Banyan Abstraction
OpenSpec = Provider Binding
Provider Workspace != Canonical Truth
Canonical Apply = Explicit Controlled Action
```

## 3. 必须完成

冻结：

```text
Change Workspace Generic Contract
Change Workspace Provider Port
OpenSpec Provider Binding
Change Identity / Lifecycle
Artifact Relationship Schema
Parallel Draft Contract
Draft Promotion Contract
Canonical Apply Contract
Apply Preview / Impact Contract
Reference-safe Reconciliation
Apply Authorization Boundary
Rollback Contract
Provider-neutral Archive / History
```

## 4. 不要重新定义 Stage 05

五级决策、Human Confirmation、CON-001 和 Semantic Commit Policy 已冻结。

Stage 06 只消费这些 Policy。

CON-002 继续 OPEN，Owner Stage 12。

## 5. Canonical Apply

本阶段不得真正修改 Canonical 文档。

禁止：

```text
自动 apply
自动 archive/delete legacy workspace
修改 docs/project canonical
运行 legacy migration
```

只设计 Contract / Provider Binding。

## 6. Parallel Draft

必须支持多个候选。

禁止：

```text
last-write-wins
latest-file-wins
AI auto winner
```

冲突进入 Stage 05 Decision Gate。

## 7. Evidence-on-Demand

仅遇到：

```text
CHANGE_LIFECYCLE_AMBIGUITY
PROVIDER_BINDING_GAP
CANONICAL_APPLY_CONFLICT
REFERENCE_MIGRATION_RISK
PARALLEL_DRAFT_CONFLICT
MISSING_EVIDENCE
```

才定点回读 CAP-CHANGE / CAP-PARALLEL / CAP-RECONCILE 的旧 Evidence。

不要重扫仓库。

## 8. Secret

13 个 Secret 继续：

```text
metadata-only
PARTIAL_APPROVED
no content read/copy/hash/write/delete/move/commit
```

## 9. Validation

执行 V06-01～V06-20。

七个 hard metrics 全部必须为 0。

## 10. 写入

仅：

```text
.banyan-refactor/stages/06/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

## 11. 完成

生成：

```text
ACCEPTANCE_REPORT.md
evidence/NEXT_STAGE_HANDOFF.yaml
```

更新 Bootstrap。

完成后停止，不进入 Stage 07。

# Banyan R1 — v3.1 + Refactor Accepted Additions Artifact Migration Completion

请严格执行 Banyan R1 Artifact Migration Completion。

R0 已通过：

```text
PASS_R0_FRAMEWORK_SELF_CONTAINMENT
```

R0 已建立 Framework-owned contract authority：

```text
src/banyan/contracts/data/
```

本轮必须基于 R0 的正式 Contract / Registry / Loader / Validator 工作，不重新建立第二套真源。

---

# A. 必读输入

## A1. R0 后当前 Framework

完整审计：

```text
banyan-framework/**
```

重点：

```text
src/banyan/contracts/data/**
src/banyan/contracts/**
src/banyan/runtime/**
src/banyan/policy/**
src/banyan/providers/**
src/banyan/adapters/**
tests/**
docs/maintainer/R0_FRAMEWORK_SELF_CONTAINMENT_ACCEPTANCE_REPORT.md
docs/maintainer/FRAMEWORK_CONTRACTS.md
```

## A2. D1.5 审计结果

读取：

```text
BANYAN_IMPLEMENTATION_GAP_AUDIT.md
V3_1_ARTIFACT_MIGRATION_MATRIX.yaml
CAPABILITY_IMPLEMENTATION_MATRIX.yaml
DEFERRED_VS_MISSING_IMPLEMENTATION.md
REMEDIATION_PRIORITY_PROPOSAL.md
D1_5_ACCEPTANCE_REPORT.md
```

## A3. Legacy v3.1 原始资料

必须读取真实 Legacy v3.1 主文档/使用说明/规则，不允许只读 Stage 摘要后猜测。

重点覆盖：
- G0～G11
- PROJECT_STAGE
- TBD
- 知情决策
- PRD / UI / Batch gates
- 编号占用保护
- 新窗口恢复
- WORKLOG / HANDOVER / PROJECT_DASHBOARD / DEVELOPMENT_PROGRESS / DOCUMENT_PROGRESS
- 39A～39C 变更稿模式
- 36A Batch PRD 收口
- G9.5 / UI 分闸
- 视觉修复循环
- 不同 PRD 状态下的变更写入语义
- 自测临时桩清理
- 禁止为验收修改业务口径

如果某项在 Legacy Source 中找不到，标记 `LEGACY_SOURCE_UNVERIFIED`，不得凭记忆补。

## A4. Banyan 后续 accepted/frozen 设计

定点读取与 Artifact Migration 相关的 accepted Stage / 总纲设计：

```text
Stage 03 Artifact Contract / Schema / Registry
Stage 04 Project Instance / Source Mapping / Profile
Stage 05 Adaptive Workflow / Decision Routing / Semantic Commit
Stage 06 Change / Canonical Apply Contracts
Stage 07 Legacy No-Loss Migration
Stage 09 UI Design Intelligence boundaries
Stage 10 Project Guide / Publishing
Stage 11 Index / Trace / History contracts
Stage 12 Context / Memory / Freshness / Token Optimization
Stage 13 Evidence / Impact / Event / Prompt Learning
Stage 14 Permission / Governance / Git Safety
Stage 15 Runtime implementation
Stage 20 Final Architecture / Release
```

---

# B. Source Priority

发生冲突时按以下优先级处理：

```text
1. Current accepted implementation facts
2. R0 Framework-owned authoritative contracts
3. Stage20 final architecture/release facts
4. Earlier accepted/frozen Stage contracts
5. Legacy v3.1 source
6. Documentation projections
```

但：

```text
Current implementation
```

不能自动抹掉 accepted-but-unimplemented contract。
必须保留 implementation_status 区分。

---

# C. 本轮正式来源分类

每个迁移对象必须标记：

```text
LEGACY_MIGRATION
REFRACTOR_ADDITION
GENERALIZED
NEW_PROPOSAL
```

## C1 LEGACY_MIGRATION
从 v3.1 迁移。

允许：
- editor-neutralize
- project-neutralize
- split monolithic prompt
- add metadata/schema/registry
- add provenance/compatibility
- rename to stable generic ID

禁止：
- 改核心语义
- 删除高价值能力
- 合并后丢失 Legacy distinction

## C2 REFRACTOR_ADDITION
来自后续 Banyan 已 accepted/frozen 的新增设计。

例如但不限于：
- Capability Lifecycle State
- Workflow Family
- Workflow Atom
- Workflow Node Contract
- Branch / Merge / Loop / Pause / Resume / Retry / Skip / Replace / Invalidate / Cancel
- Workflow Re-router / Reconciliation
- Checkpoint / Resume Point
- Decision Interrupt / Partial Blocking
- Experiment Mode / Candidate Delta
- Workflow Escalation / De-escalation
- Re-route Trigger / Workflow Confidence
- Parallel Draft Promotion Contract
- Batch Canonical Reconciliation Contract
- Source Role model
- Project Instance boundary
- Capability lifecycle distinctions

只有真实 accepted/frozen source 支持时才能纳入。

## C3 GENERALIZED
可以从 Legacy / Refactor 语义抽象成通用 Banyan Artifact。

必须满足：
- source evidence exists
- semantic intent preserved
- compatibility relation maintained
- no project business meaning leaked

## C4 NEW_PROPOSAL
没有 Legacy 或 accepted/frozen source 支持的新增内容。

必须：
- 不进入正式 Registry
- 写入 `R1_NEW_PROPOSAL_REGISTER.yaml`
- 说明 rationale / benefit / risk / affected artifacts
- 标记 `HUMAN_DECISION_REQUIRED`

---

# D. Artifact 范围

必须审计并正式收敛：

```text
ROLE
POLICY
SKILL
WORKFLOW
STATE
TEMPLATE
DECISION_PROTOCOL
CONTEXT_RECOVERY
COMPATIBILITY
```

如已有 Framework-owned type registry，扩展时必须复用 R0 真源。

---

# E. Role

注意：

```text
Banyan Role != 人员职位
Banyan Role != Git Identity
Banyan Role != Permission
Banyan Role != Authentication
```

只允许迁移/正式化：
- AI Role
- Workflow Role
- Reader Role
- Review Role
- Orchestration semantic role

禁止：
- 创建前端工程师/后端工程师/高级工程师等人员职位体系
- 把 Contributor Profile 变成权限系统
- 把 Editor Client 当业务角色

如果 Legacy / accepted contract 没有独立 Role 语义，就不要为了有 `roles/` 目录硬造 Role。

---

# F. Skill

Skill 必须至少满足：
- 可复用
- 输入明确
- 输出明确
- trigger/when_to_use 明确
- validation 明确
- 单一职责
- 不只是长 Prompt 的一个段落

必须区分：
- Framework-native Skill
- Provider-backed Skill
- Project/domain Skill
- Compatibility-only behavior

不得把 35 Capability Contract 自动等同于 35 Skill。

现有 Retained skills（如 anydesign / visual-repair-loop）如果属于 Provider / external skill，应按真实 ownership 注册，不强行变成 Core-native Skill。

---

# G. Workflow

必须纳入：
- Legacy lifecycle/workflow semantics
- accepted Adaptive Workflow contracts
- Change lifecycle
- Decision flow
- Semantic Commit flow
- Parallel Draft Promotion
- Batch Canonical Reconciliation
- recovery / resume semantics

但本轮：

```text
只完成 Artifact / Contract / Registry migration
```

不实现 Workflow executor / composer / re-router runtime。

必须明确：
- FROZEN_CONTRACT_ONLY
- IMPLEMENTED_RUNTIME_FLOW
- COMPATIBILITY_ONLY
- DEFERRED_EXECUTOR

---

# H. State

必须严格区分不同状态域，不允许混成一个大 enum。

至少审计：

```text
Capability Lifecycle State
Artifact Status
Workflow State
Change State
Decision State
Runtime State
Project Instance / Pilot State
Governance / Release State
Compatibility / Migration State
```

例如 Capability Lifecycle 的：

```text
DEFINED
IMPLEMENTED
INTEGRATED
VERIFIED
RELEASED
```

如 accepted source 支持，应正式纳入。

禁止把状态“统一化”为一个全局 enum 造成语义丢失。

---

# I. Template

只迁移真实存在且跨项目可复用的：
- Decision pack
- Review pack
- Change communication
- Handover
- Guide
- other accepted artifact templates

项目业务模板不得进入 Core。

---

# J. Decision Protocol

正式迁移：
- informed decision semantics
- five-level decision routing contract
- decision interruption / partial blocking if accepted
- decision evidence requirements

但不得在 R1 实现新的 decision runtime engine。

---

# K. Context / Recovery

必须收敛：
- new-window recovery
- Handover / Worklog recovery semantics
- Project Stage recovery
- Source Role-based context lookup
- accepted Context Builder / Freshness / Memory contract references

实现状态必须真实标注：
- IMPLEMENTED
- ACCEPTED_DESIGN_ONLY
- FROZEN_CONTRACT_ONLY
- DEFERRED_RUNTIME

---

# L. Token Efficiency

强制原则：

```text
TOKEN_EFFICIENCY_MUST_NOT_REDUCE_GOVERNANCE_FIDELITY
```

对每个 Artifact 应支持或声明：

```yaml
context_requirements:
  required_sources: [...]
  optional_sources: [...]

freshness:
  verification_required_for_high_risk_use: true|false

token_strategy:
  registry_first: true
  targeted_read: true
  summary_allowed: true|false
  canonical_fallback_required: true|false
```

不要强求所有字段逐文件重复；如果已有统一 schema/contract，可用引用方式。

高风险判断必须能回读 Canonical Source，尤其：
- migration
- decision
- authorization
- compatibility
- Canonical Apply
- state transition
- release/governance transition

---

# M. 建议目录策略

不要为了 R1 再造第二套 Registry。

优先：

```text
src/banyan/contracts/data/
```

作为 Artifact contract/index authority。

如果需要 human-readable artifact definitions，可在：

```text
banyan-framework/artifacts/
```

或等价目录建立正式文件，但必须清楚说明：
- 哪个是 authority
- 哪个是 projection
- 哪个由 loader 消费

若一个 YAML registry 足以权威表达，不强制每个 Artifact 一个文件。

---

# N. 必须输出的迁移矩阵

生成：

```text
R1_ARTIFACT_MIGRATION_MATRIX.yaml
```

每项至少：

```yaml
artifact_id:
artifact_type:
origin:
legacy_source:
refactor_source:
current_framework_source:
target_authority:
target_registry:
runtime_consumer:
provider_binding:
project_binding:
implementation_status:
compatibility_status:
semantic_change:
token_context_policy:
validation:
status:
missing_layers:
```

状态建议使用：

```text
MIGRATED_AS_ARTIFACT
GENERALIZED_TO_POLICY
GENERALIZED_TO_CAPABILITY
GENERALIZED_TO_RUNTIME_API
PROVIDER_BOUND
PROJECT_OVERLAY_BOUND
COMPATIBILITY_ONLY
FROZEN_CONTRACT_ONLY
PARTIALLY_MIGRATED
MISSING_MIGRATION
SUPERSEDED_WITH_EVIDENCE
DEFERRED_RUNTIME
```

---

# O. No-Loss Gate

必须证明：

```text
LEGACY_HIGH_VALUE_CAPABILITY_UNMAPPED = 0
ACCEPTED_REFACTOR_ADDITION_UNMAPPED = 0
SILENT_SEMANTIC_DROP = 0
UNTRACEABLE_ARTIFACT = 0
UNAUTHORIZED_NEW_SEMANTIC = 0
```

如果做不到，不得 PASS。

---

# P. Tests

至少覆盖：

1. R0 contract validation 继续 PASS。
2. 所有正式 migrated artifact ID 唯一。
3. 所有 provenance 可解析。
4. Legacy mapping target 全部 resolve。
5. Refactor addition source 全部有 accepted source evidence。
6. NEW_PROPOSAL 不进入正式 registry。
7. Role != Permission != Git Identity != Auth invariant。
8. Capability != Skill invariant。
9. State domain separation invariant。
10. Token context policy 不允许 high-risk summary-only。
11. Generic purity。
12. Stage15 Runtime regression。
13. Stage18 Adapter regression。
14. Stage18.5 Bridge regression。
15. `.banyan/**`、`docs/project/**` 默认不变。

---

# Q. 禁止事项

R1 禁止：

```text
实现 Adaptive Workflow executor
实现 natural-language orchestration
实现 Canonical Apply executor
实现 collaboration-role permission engine
Final Project Instance binding
Final Activation
Governance CURRENT transition
WebUI Help Center
继续 D2/D3
删除 Legacy source
删除 .banyan-refactor
```

---

# R. 输出

至少生成：

```text
banyan-framework/docs/maintainer/R1_ARTIFACT_MIGRATION_ACCEPTANCE_REPORT.md
banyan-framework/docs/maintainer/R1_ARTIFACT_MIGRATION_MATRIX.yaml
banyan-framework/docs/maintainer/R1_NEW_PROPOSAL_REGISTER.yaml
```

如需 machine-readable authoritative artifact additions，写入 R0 已建立的 Framework-owned contract authority。

Acceptance Report 必须包含：

- Result
- Scope
- Legacy inputs actually read
- Refactor accepted additions actually read
- Artifact counts by type
- Origin counts
- New proposals count
- No-loss gates
- Token efficiency / provenance safety validation
- Runtime regression
- Files changed
- Preserved gaps
- New gaps
- Human decisions required
- Rollback
- Stop condition

结果值：

```text
PASS_R1_ARTIFACT_MIGRATION
PASS_R1_WITH_HUMAN_DECISIONS
FAIL_R1
```

如果存在会改变正式语义的 `NEW_PROPOSAL`，不能静默 PASS；必须进入 Human Decision。

---

# S. 完成后停止

完成 R1 后停止。

不得进入：
- R2 Orchestration / Workflow / Decision execution
- R3 Project Instance Complete Binding
- D2/D3
- WebUI Help
- Final Activation

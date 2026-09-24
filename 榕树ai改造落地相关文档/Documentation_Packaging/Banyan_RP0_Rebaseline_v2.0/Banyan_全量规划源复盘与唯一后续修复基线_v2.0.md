# Banyan 全量规划源复盘与唯一后续修复基线 v2.0

> **Baseline ID**：`BANYAN-UNIQUE-REMEDIATION-BASELINE-2026-09-21-V2`  
> **状态**：`FROZEN_FOR_NEXT_REMEDIATION`  
> **唯一性**：本文件与同名 YAML 是同一 Baseline 的两种投影；**YAML 为机器可读权威，本文为人类可读说明**。  
> **替代关系**：本基线正式替代此前 `Banyan_规划现状差距盘点与后续修复总蓝图_v1.0.md` 与 `Banyan_后续修复基线_v1.0.yaml` 的“当前后续施工基线”身份；旧文件仅保留历史参考。  
> **核心原则**：`TOKEN_EFFICIENCY_MUST_NOT_REDUCE_GOVERNANCE_FIDELITY`。

---

## 0. 最终结论

这次以你上传的三个压缩包为**主事实源**重新复盘后，后续施工基线冻结为：

```text
R0 = PASS，保留
R1 = PASS，保留
CURRENT Governance = v1.9.1 FINAL_FREEZE
Framework Release = v1.10-additive.1（additive supplement，不等于 CURRENT pointer）
Final Activation = NOT_AUTHORIZED
旧“R0 → R1 → 直接 R2/R3”路线取消
下一施工阶段 = RP1 Framework Artifact Materialization (Shadow)
```

当前最大的结构性差距不是 R0/R1 失败，而是：**R1 已把 43 项语义迁移完整登记进 `migration_artifacts.yaml`，但独立 `banyan-framework/artifacts/**` 物理形态尚未建立。**

为避免再次制造两个真源，本基线对之前 RP1/RP2 做一个重要精化：

```text
RP1：43/43 独立 Artifact 先做“非权威 Shadow Materialization”
     ↓ 逐项语义等价验证
RP2：一次受控 Authority Cutover
     ↓ Artifact 文件成为 Semantic Source
     ↓ Registry 退回发现/索引/验证/lineage
     ↓ Loader / CLI / Wheel / Clean-room 同步切换
```

这样不会在 RP1 与 RP2 之间出现“独立文件和 migration_artifacts.yaml 同时都声称自己是权威正文”的架构漂移。

---

# 1. 本次事实源快照

| 输入 | 角色 | 文件数 | SHA-256 |
|---|---|---:|---|
| `1.banyan(3).zip` | 当前 `.banyan/` Project Instance 快照 | 13 | `8da4f3936f1a04472b946aa17ba6158f7034607e0b601f3d9909afb0a71c2282` |
| `榕树ai改造落地相关文档(2).zip` | CURRENT / CHANGELOG / AUDIT / Stage / Packaging 主规划证据 | 637 | `adf63f9ec6da5a2110c4ee2d21fc27aa9a8bd556503d1ad1d4747315508a2b4d` |
| `banyan-framework(2).zip` | 当前 Framework 实现快照 | 132 | `0a04ca07da5598f13f2dbb2accc03918e6d94e187113be417ad4183b3a79b387` |

用户已明确：`1.banyan.zip` 对应项目根目录下的 `.banyan/`。

---

# 2. CURRENT / CHANGELOG / AUDIT / ARCHIVE 重新定性

## 2.1 CURRENT

当前上传快照中有两份 CURRENT：

1. `榕树AI多编辑器AI软件工程框架改造总纲指导方案_v1.9.1.md`
2. `榕树AI改造阶段文档生成清单_v1.9.1.md`

定位：

```text
CURRENT = 当前治理设计与 Stage 规划权威
v1.9.1 = FINAL FREEZE
```

它冻结了 Framework / Project Instance 边界、Artifact 自解释契约、Initialize / Adopt / Migrate、Adaptive Workflow、Change/Canonical Apply、Control Plane/WebUI、No-Loss、Release 等总原则。

## 2.2 CHANGELOG

上传快照中有：

`榕树AI多编辑器AI软件工程框架改造总纲指导方案_v1.10补充变更记录.md`

它增加：AI Runtime Cost Governance、AI Task Routing、Capability Contract 化、Stage 执行模式。

定位：

```text
CHANGELOG = additive delta
!= 自动把 Governance CURRENT 从 v1.9.1 切到 v1.10
```

因此当前依然保持：

```text
Governance CURRENT = v1.9.1_FINAL_FREEZE
Framework Release = v1.10-additive.1 / RELEASED_AS_ADDITIVE_SUPPLEMENT_NOT_CURRENT
```

## 2.3 AUDIT

上传快照中 AUDIT 包含冻结一致性审计结论和审计提示词。

- 审计结论用于证明 v1.9.1 已修正并可冻结；
- 审计提示词是审计流程，不是第二套架构真源。

因此：

```text
AUDIT = 验收/审计证据
!= CURRENT 的平行设计权威
```

## 2.4 ARCHIVE

本次上传的 `ARCHIVE/` 为空。

因此当前不存在需要从 ARCHIVE 恢复成新真源的文件；以后进入 ARCHIVE 的内容默认只作为历史证据，不能覆盖 CURRENT 或本基线。

---

# 3. 冲突时的权威判定顺序

必须先判断问题属于“当前事实”还是“未来规划”，不能用一条简单优先级混在一起。

### 当前到底实现了什么

```text
当前代码 / 当前 .banyan
→ 已通过 Acceptance Report
→ DOCUMENTATION_SOURCE_OF_TRUTH / Inventory
→ Stage 设计文档
→ 历史规划
```

### 未来接下来应该怎么修

```text
用户当前明确要求
→ 本唯一后续修复基线 v2.0
→ CURRENT v1.9.1 + additive CHANGELOG
→ 已通过 R0/R1 的不可丢语义
→ Stage accepted evidence
→ 旧 re-baseline / ARCHIVE 仅作历史参考
```

任何施工者都不得拿“旧实现现状”反过来否定已经明确新增的产品要求，也不得拿“新规划”反过来伪造当前已经实现。

---

# 4. 当前真实实现快照

## 4.1 R0 / R1

压缩包内 Acceptance 结果仍为：

```text
R0 = PASS_R0_FRAMEWORK_SELF_CONTAINMENT
R1 = PASS_R1_ARTIFACT_MIGRATION_COMPLETION
```

本次从上传的 Framework 当前树重新运行 Python 验证：

```text
R0 runner: 16/16 PASS
R1 runner: 22/22 PASS
```

Go Control Plane 当前环境尝试重跑时，需要下载 Go 1.24 toolchain，但当前沙箱无法访问网络，因此本次状态是：

```text
NOT_RERUN_ENVIRONMENT_BLOCKED
```

这不是测试失败，也不推翻已经存在的历史 Acceptance PASS。

## 4.2 Framework 当前状态

已确认：

```text
banyan-framework/artifacts/ = 不存在
src/banyan/contracts/data/ = 当前 Framework Contract Authority
migration_artifacts.yaml = R1 43 项权威迁移 Registry
Natural Language Orchestration = 未实现完整 E2E
Canonical Apply Executor = 未实现
init/adopt/migrate/reconcile Runtime = 未实现
Guided Setup = 未实现
WebUI = 12 个基础 Runtime 页面
/help = 未实现
```

## 4.3 `.banyan/` 当前状态

当前上传 `.banyan/` 共 13 个文件，仍明确是：

```text
PILOT_SHADOW
final_activation: false
current_project_git_execution: DRY_RUN_ONLY
canonical_write: BLOCKED
```

所以：

```text
.banyan/** != 错误施工垃圾
.banyan/** 不允许删除后重建
当前 Reference Project 后续必须走 reconcile / upgrade
```

## 4.4 Documentation 当前状态

```text
D0 = DONE
D1 = DONE
D2 = 16 个 User Guide 输出已存在，但没有正式 Acceptance，仍属 UNACCEPTED_DOCUMENTATION_OUTPUT
D3 = NOT_STARTED
/help = NOT_IMPLEMENTED
```

D2 文件暂不删除，也不得当成最终已验收用户文档；在 RP10 统一重新对齐。

---

# 5. 永久冻结的架构边界

后续任何 RP 都必须满足：

```text
ARCHITECTURE_DRIFT = 0
UNPLANNED_EQUIVALENT_SUBSTITUTION = 0
CHAT_ACCEPTED_REQUIREMENT_UNTRACKED = 0
DOCUMENTED_AS_IMPLEMENTED_BUT_NOT_IMPLEMENTED = 0
DUPLICATE_AUTHORITY = 0
UNAUTHORIZED_NEW_SEMANTIC = 0
```

并永久保持：

- `Capability != Skill`；
- `SourceRole != CollaborationRole != BanyanRole`；
- `Role != Permission != GitIdentity != Authentication`；
- State Domain 不得偷合并；
- Framework Core 不写入项目专属路径、业务规则、Provider 选择或 Secret；
- WebUI 只是同一 Runtime API 的图形客户端，不能拥有第二套 Permission / Init / Canonical / Git / Workflow Truth；
- `.banyan/` 是 Project Instance / Mapping / Runtime State 根，不复制 Core 真源；
- `.banyan-refactor/` 只保留施工/历史 Evidence 身份，不得重新成为成熟 Runtime 目录；
- Legacy v3.1 删除前必须证明迁移完整且 `runtime_dependency_on_v3_1 = 0`；
- 每个 RP 必须生成 `PLAN_CONFORMANCE_CHECK`。

---

# 6. Artifact 最终物理形态与 Authority 模型

最终目标：

```text
banyan-framework/
├── artifacts/
│   ├── roles/
│   ├── policies/
│   ├── skills/
│   ├── workflows/
│   ├── states/
│   ├── templates/
│   ├── decision-protocols/
│   ├── context-recovery/
│   └── compatibility/
├── src/banyan/contracts/
├── src/banyan/runtime/
├── policies/
├── control-plane-go/
├── frontend/
├── docs/
└── tests/
```

最终三层责任：

```text
artifacts/**
= Artifact Semantic Source

Registry / Manifest / Schema
= Discovery / Index / Validation / Reference / Lineage

Code / Policy
= Runtime Execution Authority
```

## 6.1 RP1/RP2 过渡规则

当前 `migration_artifacts.yaml` 是 R1 已验收权威，不能为了“独立文件”直接删除或静默降级。

因此：

### RP1

43 个独立文件先创建为：

```text
NON_AUTHORITATIVE_SHADOW_MATERIALIZATION
```

逐项证明与 R1 语义等价，不切换 Runtime/Registry Authority。

### RP2

在同一个受控 Cutover 中完成：

```text
43 个独立 Artifact 文件 -> Semantic Authority
migration_artifacts.yaml -> migration lineage / index / projection role
Manifest / Schema -> 新 Authority 关系
Loader / Resolver / CLI -> artifacts/**
Wheel -> 包含全部 artifacts/**
Clean-room -> list/show/validate/refs 全部通过
```

这样中间过程始终只有一个权威正文。

---

# 7. 四类项目入口正式冻结

| 入口 | 适用 | 核心行为 | 严禁 |
|---|---|---|---|
| `banyan init` | 新项目 / 无现有 Banyan | Inspect → 建 Project Instance → 安全默认 Binding → Validate | 把已有 Banyan 当新项目 |
| `banyan adopt` | 已有项目首次接入，无需迁移完整旧治理体系 | Preserve-in-place → Discover/Map → `.banyan` → 已确认 Binding | 强搬目录、重写 Canonical Source |
| `banyan migrate` | 已有项目 + 旧治理体系 | Inventory → Semantic Mapping → Compatibility → Migration Plan → Apply → Validate → Rollback | 未证明 No-Loss 就删除 Legacy |
| `banyan reconcile` | 已存在 `.banyan` | Read Instance → Diff Framework/Binding → Controlled Migration → Validate → Result | 删除 `.banyan` 后重新 init |

`upgrade` 不再作为第五类接入模式；它是：

```text
reconcile(mode = UPGRADE_FRAMEWORK)
```

这既保留原总纲已有 Project Upgrade 语义，又满足后来明确的 `init/adopt/migrate/reconcile` 四入口模型。

---

# 8. Guided WebUI 冻结要求

四类入口完成后，Runtime 返回结构化结果，并在允许时给出 Guided WebUI 入口。

至少覆盖：

```text
Project Setup
Project Identity
Framework Version
Source Mapping
Provider Binding
Workflow Binding
Skill Binding
Overlays
Variables
Git Identity Status
Validation
Migration Status
```

已有 Banyan Instance 还要显示：

```text
Re-scan
Repair
Upgrade Framework
Migration Status
Rebuild Index
Drift Check
```

禁止：

```text
WebUI 自己判断 Permission
WebUI 自己写 Canonical
WebUI 自己直接执行 Git mutation
WebUI 自己维护第二套 Init/Migrate 状态机
WebUI 回显 Secret body
```

所有动作必须：

```text
WebUI Intent
→ Runtime API
→ Permission / Workflow / Migration Runtime
→ Typed Result
→ WebUI Render
```

---

# 9. 误施工文件清理规则

你这次新增的要求正式写入全局施工标准：**每个 RP 开始都必须做误施工清理扫描。**

文件只能分为：

```text
ACCEPTED_BASELINE
PLANNED_TARGET
CONFIRMED_MISCONSTRUCTION
OBSOLETE_AFTER_MIGRATION
HISTORICAL_EVIDENCE
AMBIGUOUS
```

只有满足全部条件才允许删除：

1. 已确认是 `CONFIRMED_MISCONSTRUCTION` 或 `OBSOLETE_AFTER_MIGRATION`；
2. Runtime / Package / Registry / Reference 均无依赖；
3. 不承担 Migration Lineage / Rollback / Acceptance Evidence；
4. 位于当前 RP 允许写入范围；
5. `PLAN_CONFORMANCE_CHECK` 明确记录删除依据。

### 当前已经能确定的分类

| 路径 | 当前分类 | 处理 |
|---|---|---|
| `src/banyan/contracts/data/migration_artifacts.yaml` | R1 ACCEPTED BASELINE | 保留到 RP2 受控 Cutover，不能提前删 |
| `.banyan/**` | ACCEPTED PILOT BASELINE | 保留，未来 reconcile，不 re-init |
| `docs/user-guide/**` | UNACCEPTED OUTPUT | 暂留，RP10 复核，不现在删 |
| `.banyan-refactor/**` | HISTORICAL EVIDENCE | 不作为 Runtime Authority，但未经保留期/依赖审计不删 |
| 旧 re-baseline v1 文件 | SUPERSEDED PLANNING OUTPUT | 不再作为 Active Baseline，可留历史 |

**本次仅凭上传快照，没有任何一个当前 Framework / `.banyan` 文件能够被安全、客观地判定为“现在就该删除的误施工文件”。**

以后实际 RP 中发现具体候选，如果是否错误、是否仍有依赖存在不确定，我会按你的规则：**停止该删除动作并先问你，不自行猜。**

---

# 10. 后续唯一施工路线

```text
R0 PASS
R1 PASS
↓
RP0R  Full Planning Source Review / Re-baseline v2   [DONE]
↓
RP1   Framework Artifact Materialization (Shadow)    [NEXT]
↓
RP2   Artifact Authority Cutover / Discovery / Package
↓
RP3   Governed Orchestration Runtime
↓
RP4   Change / Draft / Canonical Apply Runtime
↓
RP5   init / adopt / migrate / reconcile Runtime
↓
RP6   Guided WebUI Setup
↓
RP7   Context / Index / Memory / Evidence / Impact Runtime
↓
RP8   Knowledge Publishing / Project Guide / Help Center
↓
RP9   Reference Project Reconcile / Legacy Retirement
↓
RP10  Documentation Re-baseline / Final Alignment
```

旧 `R0 → R1 → 直接进入旧 R2/R3` 路线继续保持：

```text
CANCELLED
```

---

# 11. 各 RP 的核心 Exit Gate

## RP1 — Shadow Materialization

```text
EXPECTED = 43
SHADOW_MATERIALIZED = 43
SEMANTIC_EQUIVALENCE_FAILURE = 0
UNAUTHORIZED_NEW_SEMANTIC = 0
DANGLING_REFERENCE_INTRODUCED = 0
R0_R1_AUTHORITY_CHANGED = 0
DOT_BANYAN_CHANGED = 0
PLAN_CONFORMANCE_CHECK = PASS
```

RP1 不进入 Loader/CLI Authority Cutover，不修改 `.banyan`。

## RP2 — Authority Cutover / Package

```text
ARTIFACT_SEMANTIC_AUTHORITY = artifacts/**
DUPLICATE_AUTHORITY = 0
MIGRATION_REGISTRY_BODY_DUPLICATION = 0
ARTIFACT_LOADER = PASS
ARTIFACT_CLI = PASS
WHEEL_INCLUDES_ARTIFACTS = PASS
CLEAN_ROOM_DISCOVERY = PASS
RUNTIME_DEPENDENCY_ON_V3_1 = 0
R0_SELF_CONTAINMENT = PASS
PLAN_CONFORMANCE_CHECK = PASS
```

## RP5 — Project Entry Runtime

```text
INIT / ADOPT / MIGRATE / RECONCILE = typed distinct modes
SAFE_AUTO_BINDING = allowed
AMBIGUOUS_OR_HIGH_IMPACT_BINDING = NEEDS_INPUT
STRUCTURED_RESULT = required
EXISTING_BANYAN_REINIT = forbidden
ROLLBACK / ACCEPTANCE = required
```

## RP6 — Guided WebUI

```text
SAME_RUNTIME_API = true
SECOND_PERMISSION_ENGINE = 0
SECOND_INIT_ENGINE = 0
SECOND_CANONICAL_TRUTH = 0
DIRECT_GIT_ENGINE = 0
EXPLANATION_CONTRACT = required
```

## RP9 — Reference Project / Legacy Retirement

```text
REFERENCE_PROJECT_RECONCILED = true
DOT_BANYAN_RECREATED = false
MISSING_MIGRATION = 0
PARTIALLY_MIGRATED = 0
LEGACY_SOURCE_UNVERIFIED = 0
RUNTIME_DEPENDENCY_ON_V3_1 = 0
ROLLBACK_REHEARSAL = PASS
```

---

# 12. 每个 RP 必须产出的统一物资

每个阶段都要生成：

```text
1. Acceptance Report
2. PLAN_CONFORMANCE_CHECK
3. Gap Delta
4. Changed Files
5. Cleanup Delta
6. Regression Result
7. New Proposals / Human Decisions
8. Rollback Plan
9. Next-stage Handoff
```

状态只允许：

```text
PASS
PASS_WITH_CARRIED_GAPS
BLOCKED
FAIL
```

---

# 13. “不确定必须问我”正式施工门禁

从本基线开始，以下不允许施工者自行决定：

```text
架构边界变化
目录/文件物理形态变化
Authority 切换
Registry / Semantic Source 归属
迁移/删除/清理安全性不确定
等价替换
高影响 Binding
Canonical Write Target
Permission Overlay
Secret/Credential 处理
Final Activation
```

处理统一为：

```text
发现不确定
→ 标记 HUMAN_DECISION_REQUIRED / NEEDS_INPUT
→ 给出事实、影响和可选方案
→ 问用户
→ 获得决定
→ 更新 Plan/Baseline Delta
→ 再施工
```

不能用“我觉得等价”“这样更方便”“功能差不多”绕开确认。

---

# 14. RP1 开工前当前唯一未冻结的物理细节

目前已经冻结了：

```text
Artifact Root = banyan-framework/artifacts/**
9 个 Category Root
43 个 R1 Artifact ID
自解释 Metadata Contract
RP1 不新增语义
```

但从现有上传证据中，**43 个文件的精确文件名规则和统一文件格式/扩展名并没有被唯一冻结**。

因此真正开始 RP1 第一次写文件前必须执行：

```text
HD-RP1-001
→ 给用户一份 43 文件 filename / format mapping 提案
→ 用户确认
→ 才创建文件
```

这条是本次根据你“施工不确定必须问我”的要求新增的明确门禁。

---

# 15. R1 43 项 Artifact 清单

### ROLE — 1
- `banyan.migration.role.source_role_model.v1`

### POLICY — 4
- `banyan.migration.policy.legacy_governance.v1`
- `banyan.migration.policy.adaptive_decision.v1`
- `banyan.migration.policy.semantic_commit.v1`
- `banyan.migration.policy.permission_governance.v1`

### SKILL — 2
- `banyan.migration.skill.anydesign.v1`
- `banyan.migration.skill.visual_repair_loop.v1`

### WORKFLOW — 10
- `banyan.migration.workflow.v3_1_governance.v1`
- `banyan.migration.workflow.adaptive.v1`
- `banyan.migration.workflow.decision.v1`
- `banyan.migration.workflow.semantic_commit.v1`
- `banyan.migration.workflow.change_lifecycle.v1`
- `banyan.migration.workflow.parallel_draft.v1`
- `banyan.migration.workflow.batch_reconciliation.v1`
- `banyan.migration.workflow.context_recovery.v1`
- `banyan.migration.workflow.knowledge_publication.v1`
- `banyan.migration.workflow.evidence_learning.v1`

### STATE — 12
- `banyan.migration.state.artifact.v1`
- `banyan.migration.state.workflow.v1`
- `banyan.migration.state.change.v1`
- `banyan.migration.state.decision.v1`
- `banyan.migration.state.runtime.v1`
- `banyan.migration.state.project_pilot.v1`
- `banyan.migration.state.governance_release.v1`
- `banyan.migration.state.compatibility_migration.v1`
- `banyan.migration.state.capability_lifecycle.v1`
- `banyan.migration.state.capability_activation.v1`
- `banyan.migration.state.project_stage.v1`
- `banyan.migration.state.delivery_batch.v1`

### TEMPLATE — 7
- `banyan.migration.template.artifact_instance.v1`
- `banyan.migration.template.informed_decision.v1`
- `banyan.migration.template.change_workspace.v1`
- `banyan.migration.template.design_package.v1`
- `banyan.migration.template.project_guide.v1`
- `banyan.migration.template.handover_recovery.v1`
- `banyan.migration.template.evidence_record.v1`

### DECISION_PROTOCOL — 2
- `banyan.migration.decision.informed_protocol.v1`
- `banyan.migration.decision.level_routing.v1`

### CONTEXT_RECOVERY — 3
- `banyan.migration.context.new_window_resume.v1`
- `banyan.migration.context.layered_selection.v1`
- `banyan.migration.context.freshness_evidence.v1`

### COMPATIBILITY — 2
- `banyan.migration.compatibility.v3_1.v1`
- `banyan.migration.compatibility.boundaries.v1`


---

# 16. 最终状态冻结

```text
BASELINE_ID = BANYAN-UNIQUE-REMEDIATION-BASELINE-2026-09-21-V2
BASELINE_STATUS = FROZEN_FOR_NEXT_REMEDIATION
SOLE_ACTIVE_REMEDIATION_BASELINE = true
R0_RESULT = PRESERVED_PASS
R1_RESULT = PRESERVED_PASS
RP0R = COMPLETE
NEXT_STAGE = RP1_FRAMEWORK_ARTIFACT_MATERIALIZATION_SHADOW
OLD_DIRECT_R2_ENTRY = CANCELLED
CURRENT_GOVERNANCE = v1.9.1_FINAL_FREEZE
FRAMEWORK_RELEASE = v1.10-additive.1_NOT_CURRENT_POINTER
FINAL_ACTIVATION = NOT_AUTHORIZED
MISCONSTRUCTION_CLEANUP_GATE = REQUIRED_EVERY_RP
UNCERTAINTY = ASK_USER_BEFORE_WRITE_OR_DELETE
```

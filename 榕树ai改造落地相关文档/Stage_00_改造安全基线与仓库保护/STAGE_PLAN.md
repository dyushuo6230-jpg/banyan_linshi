# Stage 00 — STAGE PLAN

> Pack Version：1.9.1  
> Charter：v1.9.1 FINAL_FREEZE  
> 本文件只负责调度，不复制全部专项规则。

---

# 1. 目标

建立后续 Banyan 改造可信任的安全起点：

```text
Known Repository State
+
Known Protected Scope
+
Known Discovery Coverage
+
Recoverable Checkpoint
+
Trusted Bootstrap Refactor State / Trace
```

本 Stage 不实现 Banyan Runtime。

---

# 2. Owner Capability

| Capability | Stage 00 Target |
|---|---|
| Refactor Safety Baseline | VERIFIED |
| Repository Protection | VERIFIED |
| Discovery Scope Baseline | VERIFIED |
| Checkpoint / Rollback Control | VERIFIED |
| Bootstrap Refactor State / Trace | VERIFIED |

Activation：

```text
OFF
```

这些能力服务“改造施工控制”，不是业务 Runtime 功能。

---

# 3. Entry Gate

必须：

- Repository Root 可可靠识别；
- CURRENT Charter = v1.9.1 FINAL_FREEZE；
- Stage Pack `stage_id=00 / pack_version=1.9.1`；
- `PACK_SHA256SUMS.txt` 校验通过；
- 能在 Repository 外创建系统临时目录；
- 无 unresolved Git operation/conflict。

否则：

```text
Stage 00 = BLOCKED
```

不得继续写入。

---

# 4. Work Breakdown

## W00-01 Pack / Charter Check

读取：

```text
STAGE_MANIFEST.yaml
00_改造安全基线与仓库保护.md
PRECHECK_AND_SCOPE.md
00-A_Repository_Baseline与Protected_Paths.md
00-B_Snapshot_Hash_Checkpoint与Rollback.md
EXECUTION_RUNBOOK.md
VALIDATION_AND_ROLLBACK.md
templates/*
```

确认：

```text
stage_id = 00
pack_version = 1.9.1
charter_version = 1.9.1
```

校验 `PACK_SHA256SUMS.txt`。

## W00-02 Repository 外 Pre-stage Capture

记录：

```text
repo root
branch / HEAD
status
git operation
worktree
submodule
```

此时不得创建 Repo 内 Stage 控制文件。

## W00-03 Resolve Control Root

按优先级：

```text
BANYAN_REFACTOR_CONTROL_ROOT
→ existing safe control root
→ ${REPO_ROOT}/.banyan-refactor/
```

标记：

```text
bootstrap_only = true
```

## W00-04 Repository Baseline

生成：

```text
BASELINE_MANIFEST.yaml
```

## W00-05 Discovery Scope

生成：

```text
DISCOVERY_SCOPE_BASELINE.yaml
```

## W00-06 Protected Paths

生成：

```text
PROTECTED_PATHS_MANIFEST.yaml
```

正式 `.banyan/migrations/**` 在本 Stage 仍是：

```text
CONDITIONAL_WRITE_LATER
```

## W00-07 Managed Hash Inventory

生成：

```text
FILE_HASHES.sha256
```

不得让 Stage Control Output 污染 pre-stage project baseline。

## W00-08 Dirty-state Checkpoint

根据真实状态条件生成：

```text
checkpoint/staged.patch
checkpoint/unstaged.patch
checkpoint/untracked/*
checkpoint/ignored-governed/*
```

生成：

```text
CHECKPOINT_RECORD.yaml
```

## W00-09 Bootstrap State / Trace

从模板初始化/更新：

```text
MIGRATION_REGISTER.bootstrap.yaml
BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

必须记录：

```text
future canonical path
lineage_required
dual_writable_truth_forbidden
```

## W00-10 Validation

执行 `V00-01～V00-15`。

## W00-11 Acceptance / Handoff

真实通过后生成：

```text
ACCEPTANCE_REPORT.md
```

并包含：

```text
NEXT_STAGE_HANDOFF
```

完成后停止，不进入 Stage 01。

---

# 5. Planned Artifacts

## 指导产物

- `00_改造安全基线与仓库保护.md`
- `00-A_Repository_Baseline与Protected_Paths.md`
- `00-B_Snapshot_Hash_Checkpoint与Rollback.md`
- `STAGE_MANIFEST.yaml`
- `STAGE_PLAN.md`
- `PRECHECK_AND_SCOPE.md`
- `EXECUTION_RUNBOOK.md`
- `VALIDATION_AND_ROLLBACK.md`
- `ACCEPTANCE_REPORT.template.md`

## 实际施工后

- `BASELINE_MANIFEST.yaml`
- `PROTECTED_PATHS_MANIFEST.yaml`
- `DISCOVERY_SCOPE_BASELINE.yaml`
- `CHECKPOINT_RECORD.yaml`
- `FILE_HASHES.sha256`
- `PRE_STAGE_GIT_STATUS.txt`
- `POST_STAGE_GIT_STATUS.txt`
- `MIGRATION_REGISTER.bootstrap.yaml`
- `BANYAN_REFACTOR_TRACE.bootstrap.yaml`
- `checkpoint/**`
- `evidence/**`
- `ACCEPTANCE_REPORT.md`

---

# 6. Conditional Documents

```text
EXECUTION_RUNBOOK.md = REQUIRED
MIGRATION_MAP.md = NOT_APPLICABLE
COMPATIBILITY_MATRIX.md = NOT_APPLICABLE
DATA_RECONCILIATION.md = NOT_APPLICABLE
```

Bootstrap→Canonical 是**未来状态路径迁移义务**，本 Stage 不执行正式 Migration，因此不生成空壳 `MIGRATION_MAP.md`。

---

# 7. Risk Register

| Risk | Default Handling |
|---|---|
| Dirty worktree | 不清理，先 checkpoint |
| Untracked 重要文件 | inventory + safe backup |
| Ignored but governed | discovery + checkpoint |
| Secret | metadata-only |
| Large reproducible output | excluded + reason |
| Submodule/worktree/nested repo | 记录边界，不跨仓隐式写 |
| External symlink | 不跟随 |
| Git operation | BLOCK |
| Control Root collision | BLOCK / new RUN_ID |
| Git Identity | 只读，不修改，不 commit |
| Bootstrap/Canonical 双真源 | Stage 00 不提前建 Canonical writable state |

---

# 8. Definition of Done

```text
Mandatory Actual Artifacts exist
AND
V00-01..15 PASS
AND
Checkpoint recovery coverage trustworthy
AND
Only Stage-owned writes occurred
AND
Bootstrap Register/Trace valid
AND
Future canonical lineage obligation recorded
AND
ACCEPTANCE_REPORT.md is actual
AND
NEXT_STAGE_HANDOFF complete
AND
Stage 01 Entry Gate PASS
```

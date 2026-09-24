# Stage 00 — EXECUTION RUNBOOK

> 这是 Stage 00 的具体施工顺序。  
> 任何 Step 的 Stop Condition 命中时，立即停止，不为了“完成阶段”继续。

---

# Step 00.0 — Pack / Charter / Checksum

## Read

```text
CURRENT Charter v1.9.1
CURRENT Stage Document List v1.9.1
STAGE_MANIFEST.yaml
Stage 00 全部 guidance docs
templates/*
PACK_SHA256SUMS.txt
```

## Validate

```text
stage_id = 00
pack_version = 1.9.1
charter = 1.9.1
checksum = PASS
```

## Write

```text
NONE
```

## Stop

- checksum mismatch；
- pack missing mandatory files；
- stage/version mismatch。

---

# Step 00.1 — Repository 外 Pre-stage Capture

## Inputs

当前工作目录/Repository。

## Commands

使用只读 Git 命令发现 Root/HEAD/status/worktree/submodule。

## Write

```text
BOOTSTRAP_TMP/**
```

不得写 Repo。

## Expected Evidence

```text
PRE_STAGE_GIT_STATUS.raw
repo_root.txt
head.txt
branch.txt
git_operation.txt
worktree.txt
submodule.txt
```

后续复制/规范化为 Stage Evidence 时，不改变其语义。

## Stop

Repo Root 不可信或 Git operation unresolved。

---

# Step 00.2 — Resolve RUN_ID / Control Root

## Resolve

```text
REFRACTOR_CONTROL_ROOT
STAGE_ROOT
RUN_ID
```

推荐：

```text
${REFRACTOR_CONTROL_ROOT}/stages/00/${RUN_ID}/
```

## Allowed Write

```text
REFRACTOR_CONTROL_ROOT/**
```

## Forbidden

- `.gitignore`；
- `.banyan/migrations/**`；
- business/canonical/legacy source。

## Stop

Control Root collision / ownership unclear。

---

# Step 00.3 — Repository Boundary Baseline

生成：

```text
BASELINE_MANIFEST.yaml
PRE_STAGE_GIT_STATUS.txt
```

记录：

```text
root
topology
branch
head
detached
dirty
active operation
worktrees
submodules
nested repos
sparse checkout
lfs
```

Remote URL 不默认落盘。

---

# Step 00.4 — Discovery Scope

扫描 top-level / governance / AI / docs / tools / editor roots。

生成：

```text
DISCOVERY_SCOPE_BASELINE.yaml
```

分类：

```text
SCAN
METADATA_ONLY
EXCLUDE_WITH_REASON
```

必须处理：

```text
tracked
untracked
ignored-but-governed
symlink
submodule
```

---

# Step 00.5 — Protected Paths

生成：

```text
PROTECTED_PATHS_MANIFEST.yaml
```

分类：

```text
IMMUTABLE_DURING_REFACTOR
READ_ONLY_DISCOVERY
STAGE_WRITABLE
CONDITIONAL_WRITE_LATER
SECRET_METADATA_ONLY
EXCLUDED_WITH_REASON
```

必须显式保证：

```text
whole_repo_writable = false
stage00_business_code_write_allowed = false
stage00_canonical_truth_write_allowed = false
git_identity_write_allowed = false
future_canonical_migrations_write_allowed = false
```

---

# Step 00.6 — Managed Hash Inventory

生成：

```text
FILE_HASHES.sha256
```

要求：

- SHA-256；
- relative path；
- deterministic enough for later comparison；
- Stage Control Output 不进入 Pre-stage project baseline；
- Secret 正文不进入；
- external symlink target 不进入。

可在 Evidence 中额外生成：

```text
HASH_SCOPE_REPORT.txt
```

但不是强制权威 Artifact。

---

# Step 00.7 — Dirty-state Checkpoint

若 clean：

```text
CHECKPOINT_RECORD.recovery.coverage = COMPLETE
```

并记录无需 patch。

若 dirty：

## tracked

保存 binary-capable：

```text
checkpoint/staged.patch
checkpoint/unstaged.patch
```

## untracked

对 relevant non-secret：

```text
checkpoint/untracked/**
```

## ignored-governed

对 relevant non-secret：

```text
checkpoint/ignored-governed/**
```

## Secret

只：

```text
metadata-only
USER_MANAGED_SECRET_RECOVERY
```

若无法完整恢复关键状态：

```text
BLOCK
```

生成：

```text
CHECKPOINT_RECORD.yaml
```

并 hash checkpoint artifacts。

---

# Step 00.8 — Checkpoint Integrity

检查：

```text
patch exists if needed
patch hash matches
backup exists if needed
backup hash matches
relative path mapping exists
binary coverage known
secret recovery known
```

目标：

```text
recovery.coverage = COMPLETE
```

---

# Step 00.9 — Bootstrap Register / Trace

从模板产生实际：

```text
MIGRATION_REGISTER.bootstrap.yaml
BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

必须记录：

```text
charter_version = 1.9.1
bootstrap_only = true
control_root
run_id
baseline_head
actual artifacts
validation status
rollback point
future canonical paths
lineage_required = true
dual_writable_truth_forbidden = true
```

不能同时创建第二套正式可写 `.banyan/migrations/*`。

---

# Step 00.10 — Post-stage Safety Diff

捕获：

```text
POST_STAGE_GIT_STATUS.txt
```

比较 Pre/Post。

允许：

```text
本 Stage Control Root 自身产生的预期变化
```

不允许：

```text
business files newly modified
canonical docs modified
legacy governance modified
SQL modified
editor canonical entry modified
Git Identity config modified
```

若出现：

```text
BLOCK / FAIL
```

根据来源判断，且不得用 destructive command 自动“抹掉证据”。

---

# Step 00.11 — Validation

执行：

```text
V00-01～V00-15
```

将 Evidence path 写入实际 Acceptance。

---

# Step 00.12 — Acceptance / Handoff

仅在真实 Validation 后生成：

```text
ACCEPTANCE_REPORT.md
```

不得把：

```text
ACCEPTANCE_REPORT.template.md
```

简单复制并填 `PASS`。

Acceptance 必须包含：

```text
NEXT_STAGE_HANDOFF
```

更新 Bootstrap Register / Trace 最终 Stage 00 状态。

如果 Stage 01 Entry Gate PASS：

```text
Stage 00 = COMPLETED
```

然后：

```text
STOP
```

不得自动开始 Stage 01。

---

# Rollback Points During Run

每个写入步骤前至少知道：

```text
上一已验证 Step
当前 Stage Root
当前 checkpoint record
```

Stage 00 自己出错时优先：

```text
R0 = 停止 + 保留 Evidence + 用户确认后归档/清理 Stage-owned Output
```

不要动项目业务文件。

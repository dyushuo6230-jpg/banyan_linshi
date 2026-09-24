# Stage 00 — PRECHECK AND SCOPE

> Pack Version：1.9.1  
> 原则：先只读捕获，再创建任何 Repo 内控制产物。

---

# 1. Precheck 目标

确认：

```text
我正在看哪个 Repository
当前 Git/Worktree 状态是否安全
Stage 00 扫描范围是什么
Stage 00 写入范围是什么
哪些内容必须保护
哪些内容只能 metadata-only
Control Root 放在哪里
```

这是事实发现，不是架构设计。

---

# 2. 优先自动发现，不先问用户

自动发现：

```text
Repository Root
Branch
HEAD
Detached State
Working Tree
Active Git Operation
Worktree
Submodule
Nested Repository
Sparse Checkout
LFS
Top-level Roots
AI / Docs / Tool / Editor Roots
Tracked / Untracked / Ignored State
Symlink
Potential Secret Roots
```

仅在：

```text
NEEDS_INPUT
CONFLICT
无法安全建立 Recovery
无法判断目标 Repository
```

时询问用户。

---

# 3. Repository 外 Bootstrap Capture

先创建系统临时目录，例如：

```bash
BOOTSTRAP_TMP="$(mktemp -d "${TMPDIR:-/tmp}/banyan-stage00.XXXXXX")"
```

只读捕获建议：

```bash
git rev-parse --show-toplevel
git status --porcelain=v2 --branch
git rev-parse --verify HEAD
git symbolic-ref --short -q HEAD || true
git worktree list --porcelain
git submodule status --recursive 2>/dev/null || true
```

可以按需要补充其它**只读** Git 命令。

禁止：

- 将 credential-bearing remote URL 原样写报告；
- 输出 Secret；
- 在此步骤创建 Repo 内 Control Root。

---

# 4. Git Operation Safety

检查：

```text
MERGE_HEAD
CHERRY_PICK_HEAD
REVERT_HEAD
rebase-merge
rebase-apply
unmerged entries
```

如果 unresolved：

```text
PRECHECK = BLOCKED
```

不要替用户 abort/continue。

---

# 5. Repository Topology

识别：

- single repo；
- monorepo；
- nested Git repo；
- submodule；
- linked worktree；
- sparse checkout；
- symlink。

默认：

> Stage 00 只建立边界，不跨 Repository 自动修改。

---

# 6. Control Root Resolve

解析顺序：

```text
1. $BANYAN_REFACTOR_CONTROL_ROOT
2. 已存在、确认安全的本次改造 Control Root
3. ${REPO_ROOT}/.banyan-refactor/
```

检查：

- 是否与现有业务/治理数据冲突；
- 是否已存在其它未完成 Run；
- 是否能创建唯一 `RUN_ID`；
- 是否为本 Stage owned write scope。

若冲突无法解释：

```text
BLOCK
```

Stage 00 不修改 `.gitignore`。

---

# 7. Discovery Scope

每个 root 分类：

## `SCAN`
后续 Stage 01 可读正文。

## `METADATA_ONLY`
只读路径、大小、类型、存在性等 metadata。

## `EXCLUDE_WITH_REASON`
不进入默认 Discovery，但必须记录 reason。

候选：

```text
node_modules
vendor/cache
build/dist
coverage/cache
temporary compiler output
```

---

# 8. Ignored-but-Governed

`.gitignore` 不等于“无价值”。

必须考虑：

```text
AI 临时工作区
Legacy draft
handover
local runtime/progress
generated governance
local controlled state
```

如果：

```text
ignored = true
governed = true
```

必须显式进入 Discovery / Checkpoint 决策。

---

# 9. Secret Classification

识别候选但不读正文：

```text
.env*
*.pem
*.key
credential*
secret*
token*
private key stores
cloud credentials
```

文件名只是候选信号，不代表可以读内容。

如果需要恢复但不能安全复制：

```text
USER_MANAGED_SECRET_RECOVERY
```

---

# 10. Protected Paths 初始分类

Stage 00 Precheck 应产生真实 path-level 分类候选。

至少确认：

```text
业务代码 → immutable/read-only
Canonical Docs → immutable/read-only
Legacy AI Governance → read-only discovery
SQL/Production Config → immutable
REFRACTOR_CONTROL_ROOT → stage writable
future .banyan/migrations → conditional write later
Secret → metadata-only
cache/vendor → excluded with reason
```

最终以真实 Repository 为准。

---

# 11. Hash Scope Precheck

确认：

```text
哪些普通文件 hash
哪些只 metadata
哪些 excluded
哪些大文件采用替代 integrity 策略
```

禁止：

```text
Secret 明文 hash dump
Repo 外 symlink dereference
Stage output 混入 pre-stage baseline
```

---

# 12. Dirty State Precheck

分类：

```text
staged
unstaged
renamed
deleted
binary
untracked
ignored-governed
```

判断每一类是否可安全恢复。

如果关键变化无法形成恢复覆盖：

```text
CHECKPOINT_INCOMPLETE
→ BLOCK
```

---

# 13. Git Identity

Stage 00 仅可读取 Git Identity 环境状态用于 metadata/diagnostics。

禁止：

```text
修改 user.name
修改 user.email
--author
临时覆盖 identity
创建 commit
```

Git Identity 缺失本身不阻塞纯 Stage 00 基线读取；但本 Stage 不应通过写 identity 解决任何问题。

---

# 14. Precheck 输出

至少形成：

```text
repository boundary decision
git operation decision
control root decision
discovery scope candidate
protected path candidate
secret policy
hash scope
checkpoint feasibility
stop/block decision
```

---

# 15. Precheck Gate

只有全部可解释：

```text
Repository known
Git operation safe
Control Root safe
Protected Scope classifiable
Checkpoint feasible
Secret policy safe
```

才进入 Runbook 写入步骤。

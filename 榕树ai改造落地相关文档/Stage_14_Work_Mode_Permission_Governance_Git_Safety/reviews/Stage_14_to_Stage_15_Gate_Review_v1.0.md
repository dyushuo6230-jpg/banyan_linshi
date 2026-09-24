# Stage 14 → Stage 15 Gate Review v1.0

> Review Basis：Stage 14 Acceptance Report、VALIDATION_RESULTS、STAGE15_RUNTIME_ENFORCEMENT_HANDOFF、NEXT_STAGE_HANDOFF  
> Stage 14 Run：`stage14-20260921T022241Z`  
> Review Result：**PASS_FOR_STAGE15_RUNTIME_IMPLEMENTATION_IN_ISOLATED_MODE_WITH_TYPED_BLOCKERS**  
> Stage 15 Main-Project Git Mutation：**NOT AUTHORIZED**  
> Stage 15 Runtime Implementation：**AUTHORIZED BY STAGE15 PACK WHEN USER STARTS STAGE 15**

---

## 1. 最终结论

```text
Stage 14 = COMPLETED
Stage 14 Acceptance = PASS_STAGE14_PERMISSION_GOVERNANCE_GIT_SAFETY_POLICY_FREEZE_WITH_TYPED_BLOCKERS
Stage 15 Entry Gate = PASS_FOR_STAGE15_RUNTIME_IMPLEMENTATION_IN_ISOLATED_MODE_WITH_TYPED_BLOCKERS
```

Stage 15 可以正式进入：

```text
CLI / Runtime API / Policy Compiler / Adapter
+
Runtime Enforcement
+
Semantic Commit Executor
```

但必须把“实现能力”和“对当前项目执行受保护动作”严格分开。

---

## 2. Stage 14 已验证输入

```text
Shadow Policy Cases = 14 / 14 PASS
ALLOW = 2
BLOCK = 9
NEEDS_INPUT = 2
NOT_APPLICABLE = 1
V14-01..V14-26 = PASS
Hard Metrics = 11 / 11 all zero
Git mutation = 0
```

Git metadata：

```text
branch = feature/huanpipro
HEAD = 9a52349e6bcb6ee44e3039dd87ede56e3e0a3ec7
identity name/email present = true
identity values recorded = false
staged = 0
unstaged = 0
untracked = 4
conflicted = 0
```

Stage 14 未授权任何 Commit。

---

## 3. Stage 15 的实施边界

Stage 15 允许实现：

```text
banyan-framework/
```

作为 Generic Framework Source Candidate。

本阶段授权创建/修改的 Framework Source 只能包含：

```text
generic runtime
generic policy compiler
generic adapters
generic CLI
generic tests
generic schemas
generic isolated test fixtures
```

禁止包含：

```text
当前项目名称
当前项目目录硬编码
当前项目端口
当前项目业务规则
当前项目 Git identity 值
当前项目 Secret
当前项目 PRD/UI_SPEC 内容
```

---

## 4. 正式 `.banyan/` 仍不激活

Stage 15：

```text
允许 framework source
不允许 final project instance activation
```

即：

```text
banyan-framework/ = allowed
.banyan/ = forbidden
```

Project Instance 仍通过 Stage 04 Contract / Shadow data 消费，不在本阶段建立正式运行真源。

---

## 5. Main Project Git Mutation 仍禁止

Stage 15 必须实现 Git Executor，但当前项目不自动执行：

```text
git add
git commit
git reset
git stash
git rebase
git push
```

对当前项目只有用户在未来明确发起具体 Commit Action，并且 Stage 14 Runtime Gate 返回 `ALLOW` 后才可执行。

“启动 Stage 15”只授权：

```text
实现 Executor
运行只读检查
运行 isolated fixture Git tests
```

不授权当前项目 Commit。

---

## 6. Isolated Git Fixture

为证明 Commit Executor 真能工作，Stage 15 应创建隔离 Git Fixture：

```text
.banyan-refactor/stages/15/<run_id>/fixtures/git-executor-repo/
```

允许在该 Fixture 内执行：

```text
git init
git add
git commit
git reset
git stash
```

但只用于测试。

Fixture 必须设置本地测试身份，例如：

```text
Banyan Fixture
fixture@example.invalid
```

该身份只存在 Fixture，不得写当前项目 Git config。

不得执行：

```text
network push
remote destructive action
```

---

## 7. Runtime Enforcement

Runtime 必须严格消费 Stage 14：

```text
ACTION_RISK_POLICY
PERMISSION_DECISION_SCHEMA
AUTHORIZATION_RECORD_SCHEMA
WORK_MODE_PERMISSION_MATRIX
PROTECTED_WRITE_GATE
GIT_IDENTITY_SAFETY
GIT_WORKTREE_SAFETY
SEMANTIC_COMMIT_AUTHORIZATION
GIT_OPERATION_PERMISSION_MATRIX
AUDIT_EVENT_REQUIREMENTS
```

Compiler 必须：

```text
reject unknown policy fields
preserve hard blocks
unknown/blocked -> BLOCK/NEEDS_INPUT
never weaken policy
```

---

## 8. CLI / Runtime API

必须实现机器可调用接口，而不是只做文档。

至少支持：

```text
banyan policy evaluate
banyan runtime preflight
banyan git inspect
banyan commit plan
banyan commit execute --dry-run
banyan commit execute --fixture
banyan trace emit/validate
banyan provider list
```

具体命令名可以由实现统一，但语义必须覆盖。

---

## 9. Semantic Commit Executor

执行链：

```text
Inspect
→ Classify
→ Correlate
→ Group
→ Hunk Plan
→ Validate
→ Identity Precheck
→ Permission Gate
→ Authorization Gate
→ Execute
→ Capture Actual Commit
→ Evidence / Trace
→ Leftovers
```

当前项目默认只能走到：

```text
DRY_RUN / PLAN
```

Fixture 可走完整 Commit。

---

## 10. Hunk-aware / Index Safety

Stage 15 要实现：

```text
explicit path staging
hunk/patch staging abstraction
staged set verification
index snapshot/checkpoint
post-stage diff validation
rollback on mismatch
```

禁止 Runtime 内部出现：

```text
git add .
git add -A
blind stage all
```

---

## 11. Runtime Adapters

Stage 15 只实现 Generic Adapter Contract 与至少一个 Generic Local Adapter。

允许：

```text
filesystem adapter
git CLI adapter
subprocess runner
clock/id provider abstraction
provider binding loader
```

不实现：

```text
Cursor-specific behavior
Codex-specific behavior
Claude-specific behavior
```

这些属于 Stage 17/18 Pilot / Adapter。

---

## 12. CON-002 与 Blockers

继续：

```text
CON-002 = TYPED_BLOCKED / HUMAN_PROJECT_AUTHORITY
REF-039/041/043/044 = KEEP_UNRESOLVED_HISTORICAL
R03-* inherited
```

Runtime 不得自动解除。

---

## 13. Stage 16 边界

Stage 15 不实现 Control Plane WebUI。

Stage 16 才负责：

```text
Control Plane / WebUI
Contributor / Commit Provenance UI
Runtime status / gate visualization
```

Stage 15 只暴露稳定 API/CLI/trace contract。

---

## 14. Gate Decision

```text
Stage 14 → Stage 15 = PASS_FOR_STAGE15_RUNTIME_IMPLEMENTATION_IN_ISOLATED_MODE_WITH_TYPED_BLOCKERS

Allowed:
- create/update generic banyan-framework/**
- run unit/integration tests
- run isolated Git fixture mutations
- read current project Git metadata
- run current project dry-run/preflight

Not Allowed:
- current project Git mutation
- final .banyan activation
- canonical project write
- Secret body access
- network/external destructive actions
```

# Stage 15 v1.10 — Codex 正式开始提示词（Runtime Implementation / Isolated Git Execution）

这是 Stage 15 正式执行，不是重跑 Stage 01～14。

当前阶段：

```text
Stage 15 — CLI / Runtime API / Policy Compiler / Adapter / Semantic Commit Executor
```

## 1. 最小读取

先读：

```text
榕树ai改造落地相关文档/Stage_14_Work_Mode_Permission_Governance_Git_Safety/reviews/Stage_14_to_Stage_15_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_14_Work_Mode_Permission_Governance_Git_Safety/reviews/Stage_15_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_15_Runtime_API_Compiler_Adapter_Semantic_Commit_Executor/
```

然后读取 Stage14 `STAGE15_RUNTIME_ENFORCEMENT_HANDOFF.yaml` 与相关 machine-readable policy。

## 2. 本阶段开始实现 Framework Source

允许创建：

```text
banyan-framework/**
```

但必须：

```text
Generic only
No current project literals
No current project business rules
No editor-specific lock-in
```

禁止创建正式 `.banyan/`。

## 3. 当前项目 Git 权限

非常重要：

```text
Stage15 Pack 不授权当前项目 Git mutation
```

当前项目只允许：

```text
read-only inspect
dry-run plan
preflight
```

禁止：

```text
git add
git commit
git reset
git stash
git rebase
git push
Git config write
```

## 4. Isolated Fixture

允许在：

```text
.banyan-refactor/stages/15/${RUN_ID}/fixtures/**
```

建立临时 Git repo 并做真实 commit integration tests。

Fixture local identity 可使用：

```text
Banyan Fixture
fixture@example.invalid
```

不得污染当前项目/global Git config。

禁止网络 push。

## 5. 必须实现

```text
Policy Compiler
Runtime Permission Evaluator
CLI
Filesystem Adapter
Process Runner
Git CLI Adapter
Semantic Commit Planner
Semantic Commit Executor
Hunk-aware Staging Abstraction
Index Checkpoint / Verification
Trace / Audit Emitter
Provider Binding Loader
Dry-run mode
Fixture execution mode
```

## 6. Policy Compiler

必须：

```text
reject unknown fields
preserve hard blocks
fail closed
compile deterministic policy hash
unknown/blocked -> BLOCK or NEEDS_INPUT
```

Runtime 不得比 Stage14 更宽松。

## 7. Semantic Commit

完整实现：

```text
Inspect
→ Classify
→ Correlate
→ Group
→ Hunk Plan
→ Validate
→ Identity
→ Permission
→ Authorization
→ Execute
→ Capture Commit
→ Trace
→ Leftovers
```

当前项目走到 dry-run。

Fixture 可完整 Execute。

## 8. 禁止 Blind Stage

生产代码中不得存在：

```text
git add .
git add -A
```

只能 explicit path / explicit patch / verified index mutation。

## 9. Git Identity

当前项目只读 presence。

禁止：

```text
修改 identity
--author
猜操作者
alias merge
记录不必要的 identity 值到 Stage15 evidence
```

## 10. Secret

13 Secret 继续 metadata-only。

Secret Risk 必须在 staging 前 Hard Block。

## 11. Test

必须至少有：

```text
unit tests
policy compiler negative tests
runtime gate tests
commit planner tests
fixture commit integration test
secret risk test
missing identity test
unrelated leftover test
index mismatch rollback test
dry-run no-mutation test
```

## 12. Current Project Safety Verification

Stage15 Precheck 和 Exit 都记录：

```text
HEAD
Git index hash
staged count
```

Exit 必须证明：

```text
HEAD unchanged
Git index hash unchanged
current project mutation = 0
```

## 13. Stage16 Handoff

生成稳定 API Handoff 给 Control Plane。

Stage16 不得绕过 Runtime Policy。

## 14. 完成

执行 V15-01～V15-28。

11 项 Hard Metrics 必须全部为 0。

生成：

```text
ACCEPTANCE_REPORT.md
evidence/NEXT_STAGE_HANDOFF.yaml
STAGE16_RUNTIME_API_HANDOFF.yaml
```

更新 Bootstrap。

完成后 STOP，不进入 Stage16。

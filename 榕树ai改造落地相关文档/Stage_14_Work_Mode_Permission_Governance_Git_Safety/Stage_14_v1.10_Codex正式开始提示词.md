# Stage 14 v1.10 — Codex 正式开始提示词（Policy Freeze / Shadow Evaluation）

这是 Stage 14 正式执行，不是重跑 Stage 01～13。

当前阶段：

```text
Stage 14 — Work Mode / Permission / Governance / Git Safety
```

## 1. 最小读取

先读：

```text
榕树ai改造落地相关文档/Stage_13_Evidence_Impact_Event_Prompt_Learning/reviews/Stage_13_to_Stage_14_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_13_Evidence_Impact_Event_Prompt_Learning/reviews/Stage_14_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_14_Work_Mode_Permission_Governance_Git_Safety/
```

然后按 Low Token Index 定点读取 Stage 13 / 05 / 04 / 03 / 00。

## 2. 核心原则

```text
Evidence != Authorization
Profile != Authorization
Editor != Authorization
Git Identity != Permission Role
Commit Plan != Commit Authorization
Unknown/Blocked Precondition => BLOCK or NEEDS_INPUT
```

## 3. 必须冻结

```text
Action Risk
Permission Decision
Authorization Record
Work Mode Permission Matrix
Protected Target / Write Gate
Secret Safety Gate
Freshness / Rollback Preconditions
Human Confirmation Binding
Git Identity Safety
Git Worktree Safety
Semantic Commit Authorization
Git Operation Permission Matrix
External / Irreversible Gate
Audit Event Requirements
Learning Candidate Governance Binding
Stage15 Runtime Enforcement Handoff
```

## 4. Git

Stage 14 禁止所有 Git mutation：

```text
git add
git commit
git reset
git stash
git rebase
git push
git config write
```

只允许必要的只读 metadata 检查。

## 5. Git Identity

真实身份：

```text
author.name + author.email
```

AI 禁止修改身份、使用 --author、猜操作者或自动 alias merge。

缺失/含混：

```text
BLOCK / NEEDS_INPUT
```

## 6. Semantic Commit

保持：

```text
READY
INCOMPLETE
UNRELATED
LOCAL_ONLY
SECRET_RISK
```

`SECRET_RISK` 必须 Hard Block。

禁止 blind stage-all。

## 7. Secret

13 Secret 继续 metadata-only。

Stage 14 不授予读取/Hash/复制/修改/提交权限。

## 8. CON-002

继续：

```text
TYPED_BLOCKED / HUMAN_PROJECT_AUTHORITY
```

不得自动解除。

## 9. Shadow Evaluation

可以创建 Shadow Policy Cases 并离线计算：

```text
ALLOW
BLOCK
NEEDS_INPUT
NOT_APPLICABLE
```

但不得执行这些 Action。

## 10. Validation

执行 V14-01～V14-26。

11 项 Hard Metrics 必须全部为 0。

## 11. 写入

仅：

```text
.banyan-refactor/stages/14/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

## 12. 完成

生成：

```text
ACCEPTANCE_REPORT.md
evidence/NEXT_STAGE_HANDOFF.yaml
STAGE15_RUNTIME_ENFORCEMENT_HANDOFF.yaml
```

更新 Bootstrap。

完成 Stage 14 后停止，不进入 Stage 15。

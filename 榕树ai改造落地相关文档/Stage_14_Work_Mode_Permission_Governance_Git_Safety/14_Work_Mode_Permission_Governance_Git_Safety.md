# Stage 14：Work Mode / Permission / Governance / Git Safety

## 1. 目标

把 Stage 05 的 Workflow/Decision 与 Stage 13 的 Evidence/Impact 转成可机器执行的安全策略。

核心链：

```text
Action Intent
→ Risk Classification
→ Target Protection
→ Evidence / Impact
→ Decision Level
→ Human Confirmation
→ Authorization Record
→ Safety Preconditions
→ ALLOW / BLOCK / NEEDS_INPUT
```

Stage 14 只冻结策略并做 Shadow Evaluation，不执行真实写入。

## 2. Permission Decision

输出：

```text
ALLOW
BLOCK
NEEDS_INPUT
NOT_APPLICABLE
```

每次必须解释：

```text
action
target
risk
policy
evidence
decision
authorization
preconditions
reason
```

## 3. Authorization

Authorization Record 必须：

```text
authorization_id
actor_identity_or_user
action_scope
target_scope
granted_actions
constraints
expires/validity if applicable
evidence_refs
decision_ref
```

Contributor Profile / Editor 名称不能替代 Authorization。

## 4. Work Mode

LIGHT / STANDARD / FULL 只能影响流程重量。

不能影响：

```text
Secret hard block
Git identity hard block
Protected write gate
Human confirmation requirement
Unknown blocker behavior
```

## 5. Protected Targets

Protection Class：

```text
NORMAL
CANONICAL
SECRET_METADATA
PROTECTED_CONFIG
GIT_HISTORY
EXTERNAL_SYSTEM
IRREVERSIBLE
```

## 6. Git Commit Safety

Semantic Commit：

```text
Plan != Authorization
```

未来执行前必须：

```text
worktree inspection
classification
group validation
identity precheck
secret check
leftover check
authorization
```

## 7. Git Identity

只读：

```text
user.name
user.email
```

缺失/含混：

```text
BLOCK / NEEDS_INPUT
```

绝不由 AI 修改。

## 8. Git Operation Matrix

Stage 14 冻结：

```text
status/diff/log metadata = READ_ONLY
add/hunk stage = MUTATING / Stage15
commit = MUTATING / Stage15
reset/stash/rebase = HIGH_RISK_MUTATING
push = EXTERNAL
```

Stage 14 全部只设计，不执行。

## 9. Secret

`SECRET_RISK`：

```text
HARD_BLOCK
```

13 条 Secret Path 的内容仍不能读/hash/copy/write/commit。

## 10. Learning Candidate

`EVALUATED` Learning Candidate 仍只是 Proposal。

没有：

```text
Approved Change
Decision Gate
Authorization
```

就不能修改 Prompt/Rule/Skill。

## 11. Stage 15

输出机器可执行：

```text
policy registry
permission matrix
action gate schema
commit safety gate
runtime enforcement interface
```

给 Stage 15 Compiler/Runtime/Adapter 使用。

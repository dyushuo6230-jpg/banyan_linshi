# Stage 15：Runtime API / Compiler / Adapter / Semantic Commit Executor

## 1. 目标

Stage 15 将冻结策略变成真实可运行软件。

首次允许创建：

```text
banyan-framework/
```

它是 Generic Framework Source Candidate，不是当前项目 Instance。

## 2. 推荐 Framework Source 逻辑结构

物理结构可以由实现调整，但职责必须分离：

```text
banyan-framework/
  src/banyan/
    cli/
    runtime/
    policy/
    git/
    adapters/
    trace/
    providers/
    contracts/
  tests/
  pyproject.toml or equivalent
```

不得把当前项目内容写进 Framework Source。

## 3. Policy Compiler

输入：

```text
Stage14 machine-readable policy
```

输出：

```text
compiled immutable policy model
```

必须：

```text
schema validate
reject unknown fields
preserve hard block
fail closed
version policy
hash compiled policy
```

## 4. Runtime Evaluate

输入：

```text
action
target state
work mode
evidence
impact
decision
authorization
preconditions
```

输出：

```text
risk class
permission result
reason codes
failed/missing preconditions
audit event
```

## 5. Semantic Commit Planner

Planner 必须：

```text
inspect
classify
correlate
group
plan hunks
validate
identity precheck
permission precheck
leftovers
```

Planner 不执行 Git mutation。

## 6. Executor

Executor 只有收到：

```text
permission_result = ALLOW
authorization valid
identity valid
secret check pass
staging set verified
```

才可执行。

当前项目 Stage15 Pack 不提供这种执行授权。

## 7. Dry Run

Current Project：

```text
dry-run only
```

必须输出：

```text
planned commands
planned stage set
commit groups
blocked items
leftovers
required authorization
```

但不能修改 index。

## 8. Fixture Execution

在 isolated fixture 内：

```text
real stage
real commit
capture hash
trace
leftover validation
rollback test
```

以证明 Executor 能运行。

## 9. Hunk-aware

建议通过：

```text
git diff --patch
explicit patch application to index
temporary index abstraction
```

实现。

禁止：

```text
git add .
git add -A
```

## 10. Trace

每次 Executor 都必须生成：

```text
action id
policy hash
authorization ref
identity presence state
planned group
actual staged set
actual commit hash if any
validation result
leftovers
```

## 11. Stage 16

Stage 15 向 Stage 16 提供：

```text
stable runtime API
status/preflight API
policy evaluation API
commit plan API
trace query/emission API
provider status API
```

Control Plane 只调用 API，不绕过 Runtime Policy。

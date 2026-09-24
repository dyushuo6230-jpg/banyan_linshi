# Stage 15 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_14_to_Stage_15_Gate_Review_v1.0.md`
2. Stage 14:
   - `STAGE15_RUNTIME_ENFORCEMENT_HANDOFF.yaml`
   - `POLICY_REGISTRY.yaml`
   - `ACTION_RISK_POLICY.yaml`
   - `PERMISSION_DECISION_SCHEMA.yaml`
   - `AUTHORIZATION_RECORD_SCHEMA.yaml`
   - `PROTECTED_WRITE_GATE.yaml`
   - `GIT_IDENTITY_SAFETY.yaml`
   - `GIT_WORKTREE_SAFETY.yaml`
   - `SEMANTIC_COMMIT_AUTHORIZATION.yaml`
   - `GIT_OPERATION_PERMISSION_MATRIX.yaml`
   - `AUDIT_EVENT_REQUIREMENTS.yaml`
3. Stage 05:
   - Semantic Commit Workflow / Grouping / Message Policy
4. Stage 04:
   - Provider Binding / Project Instance interfaces
5. Stage 03:
   - Contract Registry / Runtime Governance
6. Stage 11:
   - Trace / Query interface only when needed

## 2. 实现优先，不重新分析

不要重新：

```text
扫描仓库
分析 477 commits
盘 1026 assets
重做 Stage05/14 policy
```

Stage 15 应把时间花在：

```text
code
tests
compiler
runtime
CLI
Git adapter
fixture integration tests
```

## 3. Current Project Git

只允许：

```text
status
diff
diff --cached
rev-parse
symbolic-ref
config --get user.name
config --get user.email
```

禁止 mutation。

## 4. Git Fixture

完整 Git mutation 只允许：

```text
.banyan-refactor/stages/15/<run_id>/fixtures/**
```

不得设置 remote push target。

## 5. Evidence-on-Demand Triggers

```text
POLICY_COMPILATION_AMBIGUITY
RUNTIME_INTERFACE_GAP
COMMIT_PLANNER_GAP
GIT_ADAPTER_GAP
ROLLBACK_GAP
TRACE_EMISSION_GAP
TEST_FAILURE
MISSING_EVIDENCE
```

## 6. Token 主要花费对象

```text
implementation
test failure diagnosis
policy compiler
runtime evaluation
commit planner/executor
trace/evidence emission
API stability
```

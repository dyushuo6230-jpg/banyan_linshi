# Stage 16：Control Plane / WebUI / Provenance

## 1. 目标

把 Stage 15 Runtime 暴露成可观察、可解释、可预检的本地 Control Plane。

主链：

```text
WebUI
→ Control Plane API
→ Stage15 Runtime API
→ Policy Evaluation
→ Result / Evidence / Trace
→ WebUI
```

WebUI 不直接调用 Git 或修改 Canonical。

## 2. 页面 / 视图

至少：

```text
Dashboard
Runtime / Policy
Project Safety
Gate / Blockers
Preflight
Commit Plan
Dry-run Result
Trace / Audit
Provenance
Provider Bindings
Stage / Run
Activation Readiness
```

## 3. Dashboard

应显示：

```text
runtime health
compiled policy hash
current execution mode
project mutation capability
open blockers
latest stage/run
provider status
activation state
```

## 4. Project Safety

显示：

```text
Git branch / HEAD
staged/unstaged counts
conflict state
identity present/ambiguous
Secret-risk count
execution mode
```

不得默认展示 identity value。

## 5. Preflight

用户输入 Action Intent 后：

```text
UI → Runtime preflight → typed result
```

结果必须显示：

```text
ALLOW / BLOCK / NEEDS_INPUT / NOT_APPLICABLE
risk class
reason codes
failed/missing preconditions
evidence refs
```

但 Stage 16 的 current-project ALLOW 也不能转成 mutation。

## 6. Commit Plan

只展示：

```text
semantic groups
classifications
paths/hunks
validation
blocked items
leftovers
identity presence
authorization requirement
```

当前项目只有 Dry Run。

## 7. Provenance

至少展示：

```text
stable ID
source role
authority
version/status
freshness
provenance
source refs
change/decision refs
trace refs
```

UNKNOWN 显示 UNKNOWN。

## 8. Local-only

默认启动：

```text
127.0.0.1
```

不得默认 `0.0.0.0`。

## 9. Activation Readiness

Stage 16 只显示：

```text
NOT_ACTIVATED
pilot preconditions
blockers
required migration/validation
```

不得创建 `.banyan/`。

## 10. Stage 17

Stage 17 才允许在独立 Gate 下进行：

```text
Cursor Pilot
Project Instance Pilot Activation
Pilot .banyan/
```

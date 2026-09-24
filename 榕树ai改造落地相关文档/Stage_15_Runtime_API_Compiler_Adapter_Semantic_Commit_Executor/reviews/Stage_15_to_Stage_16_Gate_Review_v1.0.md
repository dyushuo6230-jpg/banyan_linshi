# Stage 15 → Stage 16 Gate Review v1.0

> Review Basis：Stage 15 Acceptance Report、VALIDATION_RESULTS、STAGE15_COVERAGE_REPORT、GIT_SAFETY_VERIFICATION、STAGE16_RUNTIME_API_HANDOFF、NEXT_STAGE_HANDOFF  
> Stage 15 Run：`stage15-20260921T031742Z`  
> Review Result：**PASS_FOR_STAGE16_CONTROL_PLANE_WEBUI_IMPLEMENTATION_WITH_RUNTIME_ENFORCEMENT**  
> Stage 16 Execution：**NOT_STARTED / NOT_AUTHORIZED**

---

## 1. 最终结论

```text
Stage 15 = COMPLETED
Stage 15 Acceptance = PASS_STAGE15_RUNTIME_IMPLEMENTATION_ISOLATED_GIT_EXECUTION
Stage 16 Entry Gate = PASS_FOR_STAGE16_CONTROL_PLANE_WEBUI_IMPLEMENTATION_WITH_RUNTIME_ENFORCEMENT
Stage 16 Execution = NOT_STARTED
```

Stage 15 已把 Stage 14 Policy Freeze 转成真实 Runtime，并完成：

```text
Policy Compiler
Permission Runtime
Runtime API / CLI
Git Adapter
Semantic Commit Planner / Executor
Trace / Audit
Isolated Git execution
Current-project dry-run safety
```

因此 Stage 16 可以进入：

```text
Control Plane / WebUI
+
Provenance / Gate / Runtime Visualization
```

---

## 2. Stage 15 已验证事实

```text
Automated Tests = 21 / 21 PASS
V15-01..V15-28 = PASS
Hard Metrics = 11 / 11 all zero
Current Project Git Mutation = 0
```

Current Project：

```text
HEAD = 9a52349e6bcb6ee44e3039dd87ede56e3e0a3ec7
Git index SHA-256 = 3d09518893a2614bcec619c71dcd2d7a8f1242ee90adb66f144683ee8c397862
staged count = 0
execution mode = DRY_RUN_ONLY
```

Stage 16 不得扩大这个授权。

---

## 3. Stage 16 正式职责

Stage 16 必须实现：

```text
Control Plane Backend
Local WebUI
Runtime Status View
Compiled Policy / Policy Hash View
Project Safety State View
Gate / Blocker View
Action Preflight UI
Semantic Commit Plan UI
Dry-run Commit Result UI
Trace / Audit View
Artifact Provenance View
Source Role / Authority View
Reference / Freshness View
Provider Binding View
Stage / Run Status View
Activation Readiness View
Stage 17 Pilot Handoff
```

---

## 4. Control Plane 必须服从 Runtime

Control Plane 只能：

```text
call Runtime API
render Runtime Result
collect explicit user input
show evidence / provenance
```

禁止：

```text
自行重写 Permission
绕过 Runtime Gate
前端直接调用 Git mutation
根据按钮点击自动视为 Authorization
```

核心原则：

```text
UI Intent != Authorization
UI Confirmation != Authorization unless bound to the formal Human Confirmation / Authorization contract
Control Plane != Policy Engine
```

---

## 5. Current Project Action Boundary

Stage 16 对当前项目继续：

```text
READ_ONLY
PREFLIGHT
PLAN
DRY_RUN
```

不得执行：

```text
git add
git commit
git reset
git stash
git rebase
git push
Canonical Apply
Protected Write
```

即使 UI 提供未来按钮，也必须：

```text
disabled / dry-run-only / capability-not-authorized
```

不得存在隐藏绕过路径。

---

## 6. WebUI 安全边界

本阶段 Control Plane 默认：

```text
LOCAL_ONLY
LOOPBACK_ONLY
NO_PUBLIC_BIND
NO_REMOTE_AUTH_ASSUMPTION
```

允许：

```text
127.0.0.1 / localhost
```

禁止默认：

```text
0.0.0.0
public exposure
remote write action
network side effects
```

如果实现 HTTP Server，必须明确显示运行模式。

---

## 7. Provenance UI

Provenance 不是装饰项。

至少要能显示：

```text
stable_id
artifact/source role
authority
version/status
freshness
provenance
source refs
related change / decision
trace/evidence refs
```

UNKNOWN 必须显示为 UNKNOWN，不能隐藏。

---

## 8. Git Identity UI

只允许显示：

```text
identity present = true/false
identity ambiguous = true/false
```

默认禁止显示/持久化：

```text
user.name
user.email
```

除非未来有明确独立需求与授权。

Identity 仍不是 Permission Role。

---

## 9. Secret UI

13 条 Secret 只允许：

```text
path
classification
restriction flags
existence metadata
```

UI 禁止提供：

```text
preview
body
hash
copy
download
diff
commit action
```

---

## 10. `.banyan/` 激活边界

Stage 16：

```text
banyan-framework/** = allowed to continue implementation
.banyan/ = NOT CREATED / NOT ACTIVATED
```

Stage 16 只实现：

```text
Activation Readiness View
Pilot Activation Preconditions
```

第一次正式项目 Pilot `.banyan/` 激活放到：

```text
Stage 17 — Cursor Pilot / Project Instance Pilot Activation
```

并且 Stage 17 仍需独立 Gate。

---

## 11. Stage 17 Handoff

Stage 16 必须向 Stage 17 提供：

```text
Control Plane API
Runtime Status Surface
Preflight Surface
Commit Plan / Dry-run Surface
Trace / Provenance Surface
Project Instance Activation Readiness
Pilot Activation Preconditions
Cursor Adapter Integration Contract
```

Stage 16 不实现 Cursor-specific Adapter。

---

## 12. Gate Decision

```text
Stage 15 → Stage 16 = PASS_FOR_STAGE16_CONTROL_PLANE_WEBUI_IMPLEMENTATION_WITH_RUNTIME_ENFORCEMENT

Allowed:
- extend generic banyan-framework/**
- implement local Control Plane backend/frontend
- run local isolated WebUI/API tests
- call current-project Runtime in read-only/dry-run mode
- render provenance / blocker / trace / plan information

Not Allowed:
- current-project Git mutation
- final or pilot .banyan activation
- canonical/protected write
- Secret body access
- public network exposure
- Stage 17 execution
```

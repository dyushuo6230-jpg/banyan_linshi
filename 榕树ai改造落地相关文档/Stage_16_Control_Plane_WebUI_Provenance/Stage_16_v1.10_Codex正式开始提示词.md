# Stage 16 v1.10 — Codex 正式开始提示词（Control Plane / WebUI / Provenance）

这是 Stage 16 正式执行，不是重跑 Stage 01～15。

当前阶段：

```text
Stage 16 — Control Plane / WebUI / Provenance
```

## 1. 最小读取

先读：

```text
榕树ai改造落地相关文档/Stage_15_Runtime_API_Compiler_Adapter_Semantic_Commit_Executor/reviews/Stage_15_to_Stage_16_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_15_Runtime_API_Compiler_Adapter_Semantic_Commit_Executor/reviews/Stage_16_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_16_Control_Plane_WebUI_Provenance/
```

然后读取 Stage15 `STAGE16_RUNTIME_API_HANDOFF.yaml` 和 Runtime API 稳定接口。

## 2. 实现位置

允许继续修改：

```text
banyan-framework/**
```

实现 generic Control Plane / WebUI。

禁止创建正式或 Pilot：

```text
.banyan/
```

## 3. 核心原则

```text
Control Plane != Policy Engine
UI Click != Authorization
Trace != Authorization
Commit Plan != Commit Execution
```

所有判断必须调用 Stage15 Runtime。

## 4. 当前项目能力

Stage16 当前项目仅：

```text
READ_ONLY
PREFLIGHT
PLAN
DRY_RUN
```

禁止任何 Git mutation / Canonical Apply / Protected Write。

## 5. Local-only

默认只能绑定：

```text
127.0.0.1 / localhost
```

禁止默认 `0.0.0.0`。

本阶段不做公网部署，也不假设已有远程认证系统。

## 6. 必须实现 UI

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

## 7. Identity / Secret

Identity UI 只显示：

```text
present / ambiguous
```

不持久化 name/email。

Secret 只 metadata-only，不得 preview/hash/body/diff/copy/download。

## 8. Provenance

必须显示：

```text
stable ID
source role
authority
version/status
freshness
provenance
source refs
related refs
```

UNKNOWN 不得隐藏。

## 9. `.banyan/`

Stage16 只做：

```text
Activation Readiness
Pilot Preconditions
```

第一次 Pilot `.banyan/` 激活明确留给：

```text
Stage17
```

Stage16 禁止 mkdir/copy/switch truth。

## 10. Test

至少：

```text
backend unit tests
API contract tests
policy bypass negative tests
local-bind tests
secret rendering negative tests
identity-value persistence negative tests
dry-run UI tests
provenance rendering tests
activation-not-executed tests
UI/browser smoke tests
```

## 11. Current Project Safety

Precheck / Exit 验证：

```text
HEAD unchanged
Git index unchanged
staged count unchanged
.banyan absent
```

## 12. 完成

执行 V16-01～V16-26。

10 项 Hard Metrics 必须全部为 0。

生成：

```text
ACCEPTANCE_REPORT.md
evidence/NEXT_STAGE_HANDOFF.yaml
STAGE17_CURSOR_PILOT_HANDOFF.yaml
ACTIVATION_READINESS_REPORT.yaml
```

更新 Bootstrap。

完成后 STOP，不进入 Stage17。

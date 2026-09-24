# Stage 18.5 v1.10 — Codex 正式开始提示词
## Ant Design Pro Simple + Go/Gin WebUI / Control Plane Architecture Migration

这是插入在 Stage 18 与 Stage 19 之间的正式 Architecture Migration Stage。

不是重跑 Stage 01～18。

当前阶段：

```text
Stage 18.5 — WebUI Ant Design Pro Simple + Go/Gin Architecture Migration
```

## 1. 先读

```text
榕树ai改造落地相关文档/Stage_18_.../reviews/Stage_18_to_Stage_18.5_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_18_.../reviews/Stage_18.5_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_18.5_WebUI_AntDesignPro_GoGin_Migration/
```

Stage18 文件夹实际名称按仓库现有路径解析，不要为匹配提示词而改名。

## 2. 先做定点 Implementation Inventory

只定位：

```text
现有 WebUI
现有 Control Plane
现有 Runtime
Stage15 stable Runtime API
Stage16 UI feature surfaces
Stage18 Adapter Gateway
```

禁止 full repo rediscovery。

## 3. 技术栈目标

前端：

```text
Ant Design Pro Simple
TypeScript
Ant Design / ProComponents
```

后端：

```text
Go
Gin
```

发布：

```text
frontend production build
→ static assets
→ SHA-256 manifest
→ go:embed
→ Go executable
```

生产运行时不依赖 Node 来提供 UI。

## 4. Ant Design Pro 基线

从 Simple / minimal 版本建立 Banyan baseline。

删除：

```text
Demo pages
Mock business services
Sample business
Unused examples
不属于 Banyan 的默认业务语义
```

不要把示例系统的用户/权限模型带入 Banyan。

## 5. 不重写 Runtime Core

本阶段默认：

```text
PRESERVE_EXISTING_STAGE15_RUNTIME
```

必须实现单一：

```text
Runtime Bridge
```

Go/Gin 调现有 Runtime API。

除非明确形成独立迁移记录并证明必要性，否则禁止为了 WebUI 改造把整个 Runtime Core 改写成 Go。

## 6. Gin 只是 Transport

禁止在 Gin Handler 重新实现：

```text
Permission
Authorization
Git Safety
Freshness winner
Secret policy
```

所有判断继续由 Runtime 返回。

## 7. Feature Equivalence

Stage16 的 12 个主要 Feature 必须逐项迁移并记录：

```text
EQUIVALENT
IMPROVED_COMPATIBLY
DEFERRED_WITH_REASON
REMOVED_BY_EXPLICIT_DECISION
```

禁止 silent loss。

## 8. `.banyan/`

Stage17 Pilot `.banyan/` 已存在。

Stage18.5：

```text
READ / VERIFY ONLY
```

禁止：

```text
重新生成
迁移
改目录
改内容
切换 truth
```

Exit 必须验证 Stage18 fingerprint 完全一致。

## 9. Adapter Regression

Cursor / Codex / Generic Editor 必须通过新 Go/Gin Control Plane 路径回归。

仍必须：

```text
single Runtime
single Permission Policy
typed failure
trace
evidence refs
UNKNOWN provenance preserved
no Git mutation
```

## 10. Local-only

默认：

```text
127.0.0.1
```

禁止默认 `0.0.0.0`。

## 11. 当前项目 Git

禁止 mutation。

Pre / Exit 验证 Git fingerprint 不变。

## 12. Test

至少覆盖：

```text
frontend build
Go tests
Gin route contract
Runtime bridge success/failure
API compatibility
SPA deep link
API 404 separation
embedded asset hashes
release UI without Node server
local-only bind
Secret negative
Permission bypass negative
12-feature equivalence
Cursor/Codex/Generic regression
Pilot .banyan integrity
Git no-mutation
```

## 13. Validation

执行：

```text
V18_5-01..V18_5-30
```

12 项 Hard Metrics 必须全部为 0。

## 14. 写入范围

允许：

```text
banyan-framework/**
.banyan-refactor/stages/18.5/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

禁止项目业务、Canonical 文档、Pilot `.banyan`、Git mutation。

## 15. 完成

生成至少：

```text
ACCEPTANCE_REPORT.md
CURRENT_IMPLEMENTATION_INVENTORY.yaml
ADR_WEBUI_CONTROL_PLANE_STACK.yaml
FRONTEND_BASELINE_MANIFEST.yaml
FEATURE_EQUIVALENCE_MATRIX.yaml
RUNTIME_BRIDGE_CONTRACT.yaml
EMBEDDED_ASSET_MANIFEST.yaml
ADAPTER_REGRESSION_REPORT.yaml
STAGE19_RC_HANDOFF.yaml
evidence/NEXT_STAGE_HANDOFF.yaml
```

完成 Stage 18.5 后 STOP。

不要进入 Stage 19。

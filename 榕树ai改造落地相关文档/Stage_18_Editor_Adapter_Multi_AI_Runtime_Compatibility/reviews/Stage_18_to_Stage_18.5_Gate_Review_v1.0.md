# Stage 18 → Stage 18.5 Gate Review v1.0

> Review Basis：Stage 18 Acceptance Report、ADAPTER_VALIDATION_RESULT、VALIDATION_RESULTS、PILOT_INTEGRITY、FINAL_VERIFICATION、NEXT_STAGE_HANDOFF  
> Stage 18 Run：`stage18-20260921T062103Z`  
> Review Result：**PASS_FOR_STAGE18_5_WEBUI_GOGIN_ARCHITECTURE_MIGRATION_WITH_PRESERVED_RUNTIME_CONTRACTS**  
> Stage 19：**DEFERRED UNTIL STAGE 18.5 ACCEPTANCE**

---

## 1. Stage 18 实际结论

```text
Stage 18 = COMPLETED
Acceptance = PASS_STAGE18_MULTI_EDITOR_ADAPTER_COMPATIBILITY
V18 = 18 / 18 PASS
Automated Tests = 11 / 11 PASS
Formal Requests = 24
Trace Events = 36
```

正式请求矩阵：

```text
OK = 18
Runtime Blocked = 3
Typed Failure = 3
```

Cursor、Codex、Generic Editor 均保持：

```text
Editor
→ Adapter
→ Control Plane
→ Runtime API
→ Permission Policy
→ Evidence Trace
```

无第二套 Runtime / Permission System。

---

## 2. 安全状态

Stage 18 实际证明：

```text
Git mutation = 0
HEAD unchanged = true
Git index unchanged = true
staged/unstaged = 0
Pilot .banyan 13 files unchanged = true
Project document migration = 0
Legacy rescan = 0
```

继承：

```text
CON-002 = TYPED_BLOCKED_HUMAN_PROJECT_AUTHORITY
FINAL_ACTIVATION = NOT_AUTHORIZED
```

---

## 3. 为什么现在插入 Stage 18.5

原 Stage 19 将执行最终技术验收 / RC。

由于最终 Control Plane 技术架构现改为：

```text
Frontend:
Ant Design Pro Simple

Backend:
Go + Gin

Distribution:
Ant Design Pro build
→ static assets
→ Go embed
→ Go Control Plane executable
```

必须先完成实现迁移，再由 Stage 19 验收最终架构。

禁止：

```text
Stage 19 先验收旧 WebUI
然后 Stage 20 再换 WebUI 技术栈
```

---

## 4. Stage 18.5 的边界

Stage 18.5 是：

```text
WebUI + Control Plane Transport / Distribution Architecture Migration
```

不是：

```text
重做 Stage 15 Runtime Core
重做 Stage 14 Permission
重做 Stage 17/18 Adapter
重新迁移 .banyan
重新扫描项目文档
```

必须保持 Stage 15/16/17/18 已验证语义。

---

## 5. 新前端架构

正式目标：

```text
Ant Design Pro Simple
React
TypeScript
Ant Design / ProComponents
```

原则：

```text
从 Simple 精简基线开始
删除 Demo / Mock / 示例业务
不复制 Ant Design Pro 示例业务语义到 Banyan
保留必要 Layout / Router / Theme / ProComponents 基础
```

UI 仍只负责：

```text
render
collect intent
show typed Runtime result
show provenance / evidence / blockers
```

UI 不是 Policy Engine。

---

## 6. 新 Go Control Plane

正式目标：

```text
Go
Gin
```

职责：

```text
HTTP transport
DTO validation
Runtime bridge
SSE/event delivery if needed
static asset serving
local-only server
health/status
```

禁止把 Permission / Git Safety 重新实现成 Gin Handler 内部规则。

Control Plane 必须继续服从单一 Runtime Contract。

---

## 7. Runtime Preservation

Stage 18.5 必须先识别当前 Stage 15 Runtime 实现边界。

默认策略：

```text
PRESERVE_EXISTING_RUNTIME
```

Go/Gin 通过一个明确 Runtime Bridge 调用现有 Runtime。

除非 Stage 18.5 独立迁移计划证明并获授权，否则：

```text
NO_RUNTIME_CORE_LANGUAGE_REWRITE
```

即本阶段不因为改 WebUI 而顺手重写整个 Runtime。

---

## 8. Frontend Embed

Release Build：

```text
Ant Design Pro Simple
→ production static build
→ deterministic asset manifest
→ Go embed
→ Gin static fallback / SPA route
```

要求：

```text
production does not require Node to serve UI
embedded assets immutable at runtime
asset hash manifest available
SPA deep-link fallback works
API routes never fall through to SPA
```

---

## 9. Local-only

Go Control Plane 默认：

```text
127.0.0.1
localhost
```

禁止默认：

```text
0.0.0.0
public exposure
remote write endpoint
```

---

## 10. `.banyan/` Pilot

Stage 18 已证明 Pilot `.banyan/` 13 文件未变化。

Stage 18.5：

```text
may read pilot instance as existing project state
must not remigrate
must not restructure
must not change writable truth
```

WebUI 技术迁移不能修改 Pilot Project Instance。

---

## 11. Adapter Compatibility

Cursor / Codex / Generic Editor 的 Adapter Contract 不变：

```text
AdapterRequest
AdapterResponse
AdapterGateway
```

Stage 18.5 必须验证新 Go/Gin Control Plane 不破坏：

```text
request transformation
typed failures
permission fail-closed
trace emission
provenance UNKNOWN preservation
dry-run boundary
```

---

## 12. Stage 19

Stage 18.5 验收通过后，Stage 19 应验收：

```text
final WebUI implementation
Go/Gin Control Plane
embedded frontend assets
existing Runtime contract preservation
all three editor adapters
Pilot .banyan integrity
Git safety
No-Loss / provenance / trace
RC readiness
```

---

## 13. Gate Decision

```text
Stage 18 → Stage 18.5 =
PASS_FOR_STAGE18_5_WEBUI_GOGIN_ARCHITECTURE_MIGRATION_WITH_PRESERVED_RUNTIME_CONTRACTS

Stage 19 Pack Generation = DEFERRED
Stage 18.5 Pack Generation = ALLOWED
Stage 18.5 Execution = NOT YET AUTHORIZED
```

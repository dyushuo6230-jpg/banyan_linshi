# 16-A Control Plane API

Control Plane API 只能组合 Stage15 Runtime API。

最低 Endpoint 语义：

```text
GET  /api/status
GET  /api/policy
GET  /api/project-safety
POST /api/preflight
POST /api/commit/plan
POST /api/commit/dry-run
GET  /api/trace
GET  /api/provenance/:id
GET  /api/providers
GET  /api/stages
GET  /api/activation-readiness
```

禁止直接暴露 mutating Git endpoint。

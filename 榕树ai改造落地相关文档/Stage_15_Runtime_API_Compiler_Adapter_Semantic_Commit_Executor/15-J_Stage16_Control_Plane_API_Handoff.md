# 15-J Stage 16 Control Plane API Handoff

Stage 16 可调用：

```text
GET runtime status
GET policy status/hash
POST preflight
POST commit plan
POST dry-run execution
GET audit/trace result
GET provider bindings/status
```

任何 mutating action 必须仍经过 Runtime Enforcement。

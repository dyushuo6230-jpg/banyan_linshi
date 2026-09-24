# 04-E：Provider Binding Schema

Stage 03 Provider Port 是通用接口。
Stage 04 Binding 只回答：

```text
这个项目的哪个实例，在什么范围，把哪个 Port 绑定到哪个 Provider。
```

字段：

```text
binding_id
port_id
provider_id
scope
configuration_ref
capability_declaration
activation_state
fallback_policy
health_policy
```

不允许在 Generic Core Schema 写死：

```text
Cursor
Codex
Claude
某个模型名
某个商业服务
```

# 04-B：Source Mapping Schema / Registry

## 逻辑模型

```text
Source Role
→ Mapping
→ Existing Physical Path(s)
```

### Mapping 必填

```text
mapping_id
role_id
path_expression
path_kind
authority
read_policy
write_policy
freshness_rule
conflict_rule
optional
evidence
```

### Path Kind

建议：

```text
FILE
DIRECTORY
GLOB
MULTI_ROOT
VIRTUAL
EXTERNAL
```

## 关键约束

同一 role 可以映射多个路径。
同一路径也可以在严格条件下承担多个 role，但必须显式声明，不能自动猜。

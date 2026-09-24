# 06-C OpenSpec Provider Binding

OpenSpec Binding 只负责：

```text
Banyan change_id ↔ OpenSpec change path/id
Banyan artifact role ↔ OpenSpec artifact
Banyan status ↔ OpenSpec lifecycle state
Banyan apply intent ↔ OpenSpec-compatible operation
```

不得让 OpenSpec provider：

```text
绕过 Banyan Decision Gate
直接修改 Canonical
自动删除 Change Workspace
```

# 11-B Stable ID / Locator

原则：

```text
identity != path
```

每条索引记录：

```text
stable_id
entity_type
logical_identity
current_locator
locator_kind
source_role
authority
```

Move/Rename 只更新 Locator，不默认生成新 Identity。

# 07-D Reference Integrity Migration

每个 Reference Edge 必须：

```text
source
target
relationship
current validity
migration strategy
post-migration validation
```

策略：

```text
KEEP
REMAP
SUPERSEDE_WITH_CHAIN
DERIVE
BLOCK
```

任何未登记引用：

```text
MIGRATION_BLOCKED
```

# 11-H Shadow SQLite Validation

必须实际：

```text
create shadow DB
import structured sample/full structured indexes
run integrity checks
run query suite
delete/rebuild test or equivalent isolated rebuild proof
compare deterministic counts
```

所有结果写入 Stage 11 Run。

禁止把 Shadow DB 移入 `.banyan/`。

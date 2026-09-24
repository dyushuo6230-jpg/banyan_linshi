# 12-B Freshness Resolution / CON-002

禁止：

```text
mtime-wins
last-write-wins
path-proximity-wins
AI confidence-wins
```

每个冲突记录：

```text
candidate source
authority
version
status
supersession
lineage
freshness observation
conflict reason
resolution
evidence
```

CON-002 只有完整证据支持时才能 `RESOLVED`；
否则 `TYPED_BLOCKED`。

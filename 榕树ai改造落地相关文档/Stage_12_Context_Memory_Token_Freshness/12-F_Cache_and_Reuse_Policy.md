# 12-F Cache / Reuse

Cache Key 至少包含：

```text
subject ids
source versions
freshness snapshot
projection rule
policy version
```

任一关键输入变化：

```text
invalidate or REVIEW_REQUIRED
```

不能只用文件路径或 mtime。

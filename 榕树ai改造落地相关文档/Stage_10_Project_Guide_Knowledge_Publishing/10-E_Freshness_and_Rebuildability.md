# 10-E Freshness / Rebuildability

Freshness：

```text
FRESH
STALE
REVIEW_REQUIRED
BLOCKED
UNKNOWN
```

Rebuildability：

```text
REBUILDABLE
PARTIALLY_REBUILDABLE
NOT_PROVEN_REBUILDABLE
HUMAN_MAINTAINED
```

Auto refresh 只允许在：

```text
REBUILDABLE + source complete + no conflict
```

时进行。

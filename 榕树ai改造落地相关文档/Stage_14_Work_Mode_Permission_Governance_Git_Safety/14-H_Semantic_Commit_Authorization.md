# 14-H Semantic Commit Authorization

Stage 05 classes：

```text
READY
INCOMPLETE
UNRELATED
LOCAL_ONLY
SECRET_RISK
```

Disposition：

```text
READY -> eligible after validation + authorization
INCOMPLETE -> HOLD/BLOCK by default
UNRELATED -> isolate
LOCAL_ONLY -> never commit
SECRET_RISK -> hard block
```

Commit Plan 不能视为 Authorization。

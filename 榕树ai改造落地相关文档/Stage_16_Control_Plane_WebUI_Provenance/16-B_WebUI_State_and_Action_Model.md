# 16-B WebUI State / Action Model

UI Action State：

```text
AVAILABLE_READ_ONLY
AVAILABLE_DRY_RUN
BLOCKED
NEEDS_INPUT
NOT_APPLICABLE
NOT_AUTHORIZED_IN_STAGE16
```

按钮状态必须来自 Runtime/Stage capability，不可由前端自己推导放宽。

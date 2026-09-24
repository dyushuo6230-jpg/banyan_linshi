# 11-E History State Model

History Event：

```text
history_id
subject_id
event_type
from_state
to_state
occurred_at
source_ref
evidence_ref
```

禁止：

```text
只保留 latest
把失败/回滚/停止归一化为 success
```

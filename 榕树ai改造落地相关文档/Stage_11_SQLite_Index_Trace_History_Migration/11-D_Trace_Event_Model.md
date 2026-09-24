# 11-D Trace Event Model

Trace Event 至少：

```text
event_id
event_type
subject_id
stage
run_id
timestamp
actor_identity
input_refs
output_refs
decision_refs
change_refs
status
result
evidence_refs
```

未知值必须显式 UNKNOWN。

Trace 只记录，不授权。

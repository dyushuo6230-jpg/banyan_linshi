# 06-I Apply Authorization / Rollback

Apply Authorization 与 Stage 05 Decision Contract 绑定。

必须：

```text
decision_level
human_confirmation_if_required
protected_write authorization
secret checks
freshness check
checkpoint
```

Rollback Contract：

```text
rollback_id
pre_apply_snapshot
affected artifacts
reverse plan
validation
result
```

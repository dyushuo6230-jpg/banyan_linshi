# 15-B Runtime API

最低接口：

```text
evaluate_action()
preflight_action()
inspect_project()
plan_commit()
execute_commit()
emit_audit()
list_provider_bindings()
```

`execute_commit()` 必须明确执行上下文：

```text
CURRENT_PROJECT_DRY_RUN
ISOLATED_FIXTURE
AUTHORIZED_PROJECT_EXECUTION
```

Stage 15 Pack 不允许第三种。

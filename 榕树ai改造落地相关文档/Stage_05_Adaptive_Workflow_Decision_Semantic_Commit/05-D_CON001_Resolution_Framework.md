# 05-D CON-001 Resolution Framework

CON-001 不应通过“固定 HIGH=1 / LOW=2”或“当前项目 max-five”二选一解决。

Stage 05 应冻结：

```text
Decision Semantics = Generic Core
Decision Parameters = Project Overlay
Safety Floor = Non-overridable
```

项目可以配置：

```text
trigger thresholds
batch size
confirmation density
governance weight
```

但不能覆盖：

```text
Secret blocker
protected write blocker
missing Git identity blocker
explicit human-only decision
```

最终 Resolution 必须基于实际 Stage 01 Evidence。

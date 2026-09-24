# 04-J：Runtime / Index / Trace / Generated Location Contract

Project Instance 内需要为这些类别预留逻辑位置：

```text
runtime
trace
index
generated
migrations
```

规则：

- Runtime：运行状态，不是业务真源。
- Trace：执行证据与关系。
- Index：可重建索引，不是新的真源。
- Generated：生成物必须带来源与状态。
- Migrations：保存迁移计划、映射和验证记录。

具体 SQLite/Runtime 实现属于后续 Stage。

# 06-F Canonical Apply Contract

Apply 是一个受控事务语义：

```text
PREVIEWED
READY_FOR_DECISION
AUTHORIZED
APPLYING
APPLIED
VALIDATED
RECONCILED
FAILED
ROLLED_BACK
```

Stage 06 不执行写入。

未来 Executor 必须消费此 Contract。

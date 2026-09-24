# 04-I：Bootstrap → Canonical Project Instance Migration Design

当前：

```text
.banyan-refactor/
```

是改造期控制根。

未来：

```text
.banyan/
```

是 Project Instance 候选。

迁移设计必须：

```text
snapshot bootstrap
record source hashes
create target in isolated mode
validate schema
validate semantic equivalence
record target hashes
switch writable truth once
mark bootstrap read-only/archive
retain rollback
```

禁止双写真源。

Stage 04 默认只设计，不执行正式切换。

# 15-G Isolated Git Fixture

Fixture 根：

```text
.banyan-refactor/stages/15/<run_id>/fixtures/
```

允许本地测试身份：

```text
Banyan Fixture
fixture@example.invalid
```

只允许 Fixture-local config。

必须测试：

```text
single group commit
multi group commit
unrelated leftover
secret risk block
missing identity block
index mismatch rollback
conflict block
dry-run no mutation
```

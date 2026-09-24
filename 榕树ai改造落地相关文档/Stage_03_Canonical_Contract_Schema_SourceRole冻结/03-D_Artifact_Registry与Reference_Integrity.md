# 03-D：Artifact Registry 与 Reference Integrity

## Artifact Identity

Artifact 必须能稳定回答：

```text
它是谁
哪个版本
什么状态
谁是真源
来自哪里
引用了谁
谁引用它
是否被替代
是否允许修改
```

## Reference Integrity

仍被引用的 Canonical Artifact：

```text
不得清空
不得整篇换题
不得把旧 ID 偷换给新主题
不得删除而不更新引用图
```

## Supersession

替代必须记录：

```text
old_artifact
new_artifact
reason
effective_version
reference_migration_status
```

本阶段冻结规则，不执行迁移。

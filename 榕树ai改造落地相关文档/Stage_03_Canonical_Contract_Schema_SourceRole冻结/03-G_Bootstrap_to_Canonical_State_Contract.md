# 03-G：Bootstrap → Canonical State Contract

## 当前状态

当前唯一可写改造状态仍是：

```text
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

## 未来迁移

正式 `.banyan` 出现时必须：

```text
bootstrap source hash + run lineage
→ canonical target write
→ target hash
→ schema validation
→ semantic reconciliation
→ bootstrap read-only archive/reference
```

## 禁止

```text
dual writable truth
复制后两边继续写
无 lineage 的覆盖
未验证就删 bootstrap
```

Stage 03 只冻结该迁移契约，不执行 `.banyan` 初始化。

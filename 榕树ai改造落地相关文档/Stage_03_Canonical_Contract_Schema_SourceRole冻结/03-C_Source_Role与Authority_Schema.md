# 03-C：Source Role 与 Authority Schema

## 第一原则

Source Role 是语义角色，不是目录名。

错误：

```text
PROJECT_FACT = docs/project/**
```

正确：

```text
PROJECT_FACT
→ semantic role
→ project mapping
→ physical path(s)
```

## 必填字段

```yaml
role_id:
semantic_purpose:
authority_level:
canonicality:
writable_policy:
freshness_rule:
conflict_rule:
provenance_required:
mapping_strategy:
```

## Authority Level

建议至少表达：

```text
CANONICAL
AUTHORITATIVE_REFERENCE
DERIVED
OPERATIONAL
HISTORICAL
EXTERNAL_EVIDENCE
```

## 冲突

同一语义多来源冲突必须：

```text
记录冲突
应用 precedence contract
不能静默覆盖
```

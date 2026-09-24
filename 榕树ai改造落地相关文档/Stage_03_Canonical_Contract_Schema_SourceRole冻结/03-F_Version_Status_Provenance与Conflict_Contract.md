# 03-F：Version / Status / Provenance / Conflict Contract

## Version

必须可区分：

```text
schema version
artifact version
contract version
runtime state version
```

## Status

不同实体使用受控枚举，不允许自由文本替代关键状态。

## Provenance

至少记录：

```text
source
created/derived by
timestamp
input refs
generation/tool metadata when available
confidence if inferred
```

不知道 AI 作者身份时：

```text
UNKNOWN
```

不得猜。

## Conflict

必须能结构化表示：

```text
conflict_id
subjects
authority candidates
freshness
precedence rule
blocking
owner
resolution status
```

CON-001 / CON-002 必须保留。

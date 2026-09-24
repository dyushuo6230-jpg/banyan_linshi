# 03-A：Canonical Contract Schema

## 目标

冻结所有 Capability Contract 的共同外壳。

## 必填字段

```yaml
contract_id:
capability_id:
version:
status:
scope:
inputs: []
outputs: []
preconditions: []
guards: []
side_effect_policy:
failure_semantics: []
authority:
evidence_lineage: []
extension_points: []
compatibility:
```

## 状态

推荐：

```text
DRAFT
FROZEN
DEPRECATED
SUPERSEDED
BLOCKED
```

Stage 03 只能将证据充分的 Contract 标成 `FROZEN`。

## 失败语义

任何 Contract 没有 failure semantics：

```text
V03 FAIL
```

因为 Banyan 必须知道“做不到时怎么停”，而不是只知道成功路径。

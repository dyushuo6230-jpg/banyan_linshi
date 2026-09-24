# 01-A：AI Asset Inventory Schema

> 本阶段使用 Bootstrap Discovery Schema。Stage 03 才冻结正式 Artifact Schema。

## 1. Inventory 粒度

一条记录对应一个**可定位的资产单元**：

- 文件；
- 目录级规则集合；
- symlinked skill；
- script/tool；
- editor rule；
- generated artifact；
- operational state；
- historical-only artifact reference。

不要把整个 `docs/` 只记一条。

## 2. 推荐字段

```yaml
asset_id:
path:
repository_relative: true

origin:
  tracked_state:
  discovered_by:
  first_seen_ref:
  historical_only: false

asset_type:
classification:
  action:
  confidence:
  reason:

content_access:
  mode: SCAN | METADATA_ONLY | EXCLUDE_WITH_REASON
  secret: false

authority:
  source_of_truth_candidate:
  canonicality:
  status_if_known:

relations:
  references: []
  referenced_by: []
  symlink_target:
  generated_from: []
  generates: []

migration:
  candidate_owner_stage:
  candidate_target:
  candidate_action:
  open_question:

evidence_refs: []
notes: []
```

## 3. `asset_type`

优先枚举：

```text
ROLE
POLICY
SKILL
WORKFLOW
STATE
PROFILE
TEMPLATE
PROJECT_FACT
TOOL
ADAPTER
CHANGE_ARTIFACT
PUBLISHING_ARTIFACT
UNCLASSIFIED
```

可以记录 `subtype`，但不得在 Stage 01 擅自扩张成新的 Core Type。

## 4. Construction / Refactor Isolation

以下必须单独标记，不进入 Legacy Inventory：

```text
UPSTREAM_REFACTOR_OPERATIONAL_EVIDENCE
REFRACTOR_CONSTRUCTION_MATERIAL
```

特别是：

```text
.banyan-refactor/**
榕树ai改造落地相关文档/**
```

## 5. Secret

Stage 00 已标记的 Secret：

```text
只记录 path / exists / classification / metadata
```

禁止把正文摘要写入 Inventory。

## 6. Hash

Inventory 可以引用 Stage 00 Hash。

当前扫描如需验证 freshness，可新增 evidence hash，但：

- 不 hash Secret 正文；
- 不让 Stage 01 结果替代 Git/Stage 00 的历史 Evidence。

## 7. Canonicality

候选：

```text
CANONICAL
DERIVED
OPERATIONAL
REFERENCE
GENERATED
LEGACY
UNKNOWN
```

Stage 01 只基于 Evidence 标注；有冲突时进入 Conflict Report。

## 8. UNCLASSIFIED

必须：

```yaml
asset_type: UNCLASSIFIED
risk:
candidate_owner_stage:
next_stage_plan:
reason_not_classified:
```

不得消失。

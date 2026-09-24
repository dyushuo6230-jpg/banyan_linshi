# 01-H：Discovery Coverage 与 Preliminary No-Loss Gate

## 1. Discovery Coverage 不是文件数

必须证明：

```text
Tracked considered
Relevant untracked considered
Governed ignored considered
AI roots considered
Docs/governance roots considered
Tools/scripts considered
Editor roots considered
Generated/Operational roots considered
Git history considered where needed
Exclusion has reason
Secret policy preserved
```

## 2. Stage 00 Evidence 复用

优先消费 Stage 00 `FILE_INVENTORY` / Discovery Scope，减少无意义重新枚举。

但 Stage 01 仍必须从真实 Repository Root 重新确认 freshness 和新增/变化项。

## 3. 三个硬指标

```text
SILENTLY_IGNORED_ASSET = 0
UNSCANNED_GOVERNANCE_ROOT_WITHOUT_REASON = 0
HIGH_RISK_UNCLASSIFIED = 0
```

## 4. Coverage Classes

```text
COVERED_CONTENT
COVERED_METADATA_ONLY
COVERED_HISTORICAL
EXCLUDED_WITH_REASON
UNCLASSIFIED_REGISTERED
BLOCKED
```

## 5. Preliminary No-Loss

### Capability

所有高价值项：

```text
candidate_owner_stage
candidate_target_capability
candidate_action
confidence
open_question
```

### Canonical Artifact

```text
candidate_source_role
keep_or_migrate
integrity_risk
```

## 6. `.banyan-refactor` 与施工资料污染防护

Coverage 可以读取：

```text
.banyan-refactor/**
榕树ai改造落地相关文档/**
```

但必须分别标记：

```text
UPSTREAM_REFACTOR_OPERATIONAL_EVIDENCE
REFRACTOR_CONSTRUCTION_MATERIAL
```

它们不进入 Legacy Asset / Legacy Capability 总量。

## 7. Exit

如果存在新的治理 Root 无法安全扫描：

```text
BLOCK
```

如果只是普通未知资产：

```text
UNCLASSIFIED + owner candidate + next-stage plan
```

不能静默忽略。

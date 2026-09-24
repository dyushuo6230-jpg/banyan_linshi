# Stage 01 — EXECUTION RUNBOOK

## Step 01.0 — Pack / Upstream Gate

读取 CURRENT Charter、Stage 01 Pack、Stage 00 Gate Review、实际 Handoff。

验证 Pack checksum。

## Step 01.1 — Freshness

只读：

```text
HEAD
status
topology
Stage 00 protected/secret metadata
```

生成：

```text
evidence/BASELINE_FRESHNESS.json
```

## Step 01.2 — Build Discovery Universe

从真实 Repository Root 建立候选集合。

来源至少：

```text
Stage 00 FILE_INVENTORY / Discovery Scope
current tracked/untracked/ignored metadata
AI/editor roots
docs/governance
tools/scripts
generated/operational roots
targeted Git history
```

先排除：

```text
UPSTREAM_REFACTOR_OPERATIONAL_EVIDENCE
REFRACTOR_CONSTRUCTION_MATERIAL
SECRET_METADATA_ONLY content
dependencies/build/cache with reason
```

## Step 01.3 — AI Asset Inventory

生成：

```text
AI_ASSET_INVENTORY.jsonl
```

必须每条有 path / type / classification / evidence。

## Step 01.4 — Legacy Classification / Core Candidate

生成：

```text
LEGACY_CLASSIFICATION_REPORT.yaml
CORE_CANDIDATE_REPORT.yaml
```

禁止把 Candidate 当 Final Architecture。

## Step 01.5 — Capability Discovery

从多个文件聚合行为：

```text
LEGACY_AI_CAPABILITY_INVENTORY.jsonl
```

高价值项必须有 Owner/Target/Action candidate。

## Step 01.6 — AI Generated Artifact

生成：

```text
AI_GENERATED_ARTIFACT_INVENTORY.jsonl
```

Canonical/Derived 分开。

## Step 01.7 — Operational Artifact

生成：

```text
OPERATIONAL_ARTIFACT_INVENTORY.jsonl
```

至少覆盖：

```text
progress
worklog
handover
dashboard
runtime state
temporary governance state
generated operational evidence
```

但 `.banyan-refactor/**` 单独标记 upstream refactor evidence，不混入 Legacy。

## Step 01.8 — Duplicate / Conflict / Gap

生成：

```text
CONFLICT_GAP_REPORT.yaml
```

不修，只报告。

## Step 01.9 — Git Identity / Commit Practice

只读 Git history/config effective identity。

生成：

```text
GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml
```

不改 identity，不 commit。

## Step 01.10 — Preliminary Capability Preservation

生成：

```text
PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX.yaml
```

## Step 01.11 — Preliminary Artifact Migration

生成：

```text
PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX.yaml
```

`DROP_WITH_APPROVAL` 只能 NOT_APPROVED candidate。

## Step 01.12 — Coverage / No-Loss

生成：

```text
DISCOVERY_COVERAGE_REPORT.yaml
```

验证：

```text
SILENTLY_IGNORED_ASSET = 0
UNSCANNED_GOVERNANCE_ROOT_WITHOUT_REASON = 0
HIGH_RISK_UNCLASSIFIED = 0
```

## Step 01.13 — Bootstrap Register / Trace

更新现有 Bootstrap files：

```text
current_stage = 01
Stage 01 actual artifacts
validation
open risks
next handoff
```

不得创建正式 `.banyan/migrations`.

## Step 01.14 — Acceptance

执行 V01-01～V01-18。

真实通过后生成：

```text
ACCEPTANCE_REPORT.md
NEXT_STAGE_HANDOFF
```

然后 STOP，不进入 Stage 02。

# 01-G：AI Asset Migration Master Map

> 这是 Preliminary Master Map，不是正式迁移执行计划。

## 1. 目的

把 Stage 01 的发现转成 Stage 02/07 可消费的“迁移候选关系”。

## 2. 三类映射

### Capability

```text
Legacy Capability
→ Candidate Owner Stage
→ Candidate Target Capability
→ Candidate Action
```

### Canonical Artifact

```text
Current Canonical Artifact
→ Candidate Source Role
→ Keep/Migrate Strategy
→ Integrity Risk
```

### Generated / Derived Artifact

```text
Generated Artifact
→ Source / Consumer
→ Rebuildability
→ Candidate Migration Action
```

## 3. 不执行

本阶段不能：

```text
移动文件
改 ID
改 Source of Truth
删除 Legacy
创建正式 Compatibility Loader
```

## 4. 对 `DROP_WITH_APPROVAL`

必须：

```text
candidate_action = DROP_WITH_APPROVAL
approval_status = NOT_APPROVED
execution_allowed = false
```

## 5. 输出

权威初版矩阵：

```text
PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX.yaml
PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX.yaml
```

Stage 02 分配 Owner/Target；Stage 07 协调 Legacy Migration；各领域 Owner Stage 实施；Stage 19 最终 No-Loss Audit。

# 01-F：AI Capability Discovery Report

## 1. 能力不是文件

一个 Capability 可能由：

```text
Prompt + Rule + Skill + Script + Doc + Human Procedure
```

共同形成。

Stage 01 必须从行为语义发现能力，而不是只数文件。

## 2. 重点 Capability Families

发现但不限定：

```text
Requirement / PRD Governance
Decision / Change
Architecture Governance
UI Governance
Implementation
Test / Acceptance
Numbering / Status / Baseline
Reference Integrity
Parallel Draft
Batch Reconciliation
Worklog / Handover / Progress
Context / Recovery
Permission / Safety
Evidence / Trace
Publishing / Guide
Commit / Git Practice
Editor Integration
```

## 3. 每个高价值 Capability

至少：

```yaml
capability_id:
name:
description:
legacy_sources:
behaviors:
inputs:
outputs:
guards:
failure_semantics:
evidence_refs:

candidate_owner_stage:
candidate_target_capability:
candidate_action:
confidence:
open_question:
```

## 4. 行为证据

优先级：

```text
实际可执行规则/脚本/Skill
+
Approved/Baselined Governance
+
真实历史使用证据
+
说明文档
```

冲突进入 01-C，不在本阶段自行裁决。

## 5. Preliminary Preservation

Capability 必须进入：

`PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX.yaml`

高价值项没有候选归宿：

```text
Stage 01 Exit Gate FAIL
```

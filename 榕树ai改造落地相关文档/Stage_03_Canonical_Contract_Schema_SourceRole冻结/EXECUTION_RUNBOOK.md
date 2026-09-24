# Stage 03 — EXECUTION RUNBOOK（低 Token）

## Step 03.0

校验 Pack、Stage 02 Handoff、sealed inputs。

## Step 03.1

读取：

```text
Gate Review
Low Token Index
NEXT_STAGE_HANDOFF
CAPABILITY_MAPPING_WORKBOOK
CONTRACT_CHAIN_DESIGN
ARCHITECTURE_DECISION_RECORDS
CONFLICT_RISK_REGISTER
AI_RUNTIME_COST_GOVERNANCE_DESIGN
```

不要读取全仓。

## Step 03.2

对 35 Capability 做 schema collision / missing semantics 检查。

只有发生冲突才按 evidence_refs 定点回读。

## Step 03.3～03.11

依次生成 Schema / Contract。

每完成一类即做局部验证，不等待最后一次性修。

## Step 03.12

生成：

```text
CONTRACT_FREEZE_REGISTER.yaml
CONTRACT_COVERAGE_REPORT.yaml
CONFLICT_CARRYOVER_REGISTER.yaml
```

## Step 03.13

执行 V03-01～V03-20。

## Step 03.14

生成真实：

```text
ACCEPTANCE_REPORT.md
evidence/NEXT_STAGE_HANDOFF.yaml
```

更新 Bootstrap Register/Trace。

STOP。不得进入 Stage 04。

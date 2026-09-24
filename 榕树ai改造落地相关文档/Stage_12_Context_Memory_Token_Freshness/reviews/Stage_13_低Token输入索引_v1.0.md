# Stage 13 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_12_to_Stage_13_Gate_Review_v1.0.md`
2. Stage 12:
   - `STAGE13_QUERY_HANDOFF.yaml`
   - `CONTEXT_SELECTION_POLICY.yaml`
   - `FRESHNESS_RESOLUTION_SCHEMA.yaml`
   - `CON002_RESOLUTION_RECORD.yaml`
   - `HISTORICAL_REFERENCE_DISPOSITION.yaml`
   - `RUNTIME_COST_CONTEXT_POLICY.yaml`
3. Stage 11:
   - Query Contract / Trace / History / Reference schemas
   - Shadow DB：只通过既有 Query Surface 定点查询
4. Stage 06:
   - Change Workspace
   - Canonical Apply / Preview / Reconciliation
5. Stage 05:
   - Decision / Human Confirmation
   - Semantic Commit Workflow / Classification
6. Stage 03:
   - Evidence Trace Contract
   - Artifact / Reference / Provenance contracts
   - AI Runtime Governance Contract

## 2. Prompt / Rule / Skill 定点策略

默认不全文读取全部 Prompt / Rule / Skill。

只在以下情况定点读取：

```text
PROMPT_OUTCOME_ATTRIBUTION_GAP
PROMPT_VERSION_UNKNOWN
RULE_CONFLICT
SKILL_BEHAVIOR_GAP
LEARNING_CANDIDATE_EVALUATION
```

读取必须有明确 `source_ref` 和目的。

## 3. Impact Query 优先

优先通过：

```text
artifact references
change affected artifacts
projection/source links
UI/PRD trace
source role
current/historical state
provider binding
```

构建局部影响图。

禁止全仓关键词搜索代替 Impact Analysis。

## 4. Event Query 优先

优先消费：

```text
trace by stage/run/subject
history transitions
decision evidence
change lineage
```

不重新解析所有操作日志。

## 5. Evidence-on-Demand Triggers

```text
EVIDENCE_SOURCE_GAP
IMPACT_EDGE_AMBIGUITY
CAUSALITY_AMBIGUITY
PROMPT_OUTCOME_ATTRIBUTION_GAP
LEARNING_CANDIDATE_CONFLICT
EVALUATION_COUNTEREXAMPLE
PROVENANCE_GAP
MISSING_EVIDENCE
```

## 6. 默认禁止

```text
repository rediscovery
full prompt corpus reload
full Git history analysis
full conversation-history mining
Stage11 DB rebuild
canonical Prompt/Rule/Skill mutation
```

## 7. Token 主要花费对象

```text
Evidence Chain
Impact Graph
Event Taxonomy
Outcome Attribution
Learning Candidate
Evaluation
Promotion Gate
Stage14 Governance Requirements
```

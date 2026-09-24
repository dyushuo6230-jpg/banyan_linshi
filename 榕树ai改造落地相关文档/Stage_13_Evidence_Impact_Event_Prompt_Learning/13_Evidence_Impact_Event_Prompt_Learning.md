# Stage 13：Evidence / Impact / Event / Prompt Learning

## 1. 目标

把 Banyan 从“有记录”提升到：

```text
能说明证据
能说明影响
能说明发生了什么
能形成可评估的改进候选
```

但不允许 Runtime 自我修改。

## 2. Evidence

Evidence 结构：

```text
evidence_id
evidence_type
subject_id
source_refs
observed_at / as_of
authority
provenance
freshness
confidence
scope
result
classification
```

分类至少：

```text
OBSERVED_FACT
DERIVED_FACT
INFERENCE
RECOMMENDATION
VALIDATION_RESULT
HUMAN_DECISION
```

## 3. Evidence Chain

支持：

```text
source
→ observation
→ validation
→ decision
→ action/result
```

每一跳都必须可追溯。

## 4. Impact

Impact 分类：

```text
DIRECT
TRANSITIVE
POTENTIAL
UNKNOWN
EXCLUDED
```

Impact Edge 必须有：

```text
basis
source_refs
confidence
scope
```

## 5. Event

Event 只描述发生了什么。

Event Class：

```text
OBSERVED_EVENT
DERIVED_EVENT
CORRELATED_EVENT
```

因果关系单独记录：

```text
CAUSAL_LINK
```

并需要证据。

## 6. Prompt Observation

记录 Prompt / Rule / Skill 的使用事实：

```text
artifact_id/version
task profile
context set
execution mode
provider binding if known
tools
human intervention
result
validation
cost telemetry
```

## 7. Outcome Attribution

成功或失败可能来自：

```text
Prompt
Context
Model capability
Tool behavior
Repository state
Human intervention
Provider availability
Task difficulty
```

默认：

```text
MULTI_FACTOR / UNKNOWN
```

禁止自动单因归因。

## 8. Learning Candidate

Learning Candidate 是：

```text
PROPOSAL
```

不是生效 Policy。

候选类型：

```text
PROMPT_CHANGE
RULE_CHANGE
SKILL_CHANGE
WORKFLOW_CHANGE
CONTEXT_POLICY_CHANGE
PROVIDER_HINT
PROJECT_OVERLAY_CHANGE
```

## 9. Evaluation

候选必须经过：

```text
baseline
candidate
test cases
counterexamples
quality result
regression result
cost result
scope
confidence
```

## 10. Promotion

只有：

```text
EVALUATED
APPROVED
CANONICAL_APPLY_AUTHORIZED
```

才可能进入后续正式变更。

Stage 13 不执行 Apply。

## 11. Project vs Core

Project-specific Candidate 默认：

```text
PROJECT_SCOPE
```

想进入 Generic Core 必须额外证明：

```text
cross-project evidence
no project literals
portable semantics
independent validation
```

## 12. Stage 14

Stage 14 消费：

```text
Evidence requirements
Impact/Risk
Event audit requirements
Learning proposal approval requirements
```

并落实 Permission / Governance。

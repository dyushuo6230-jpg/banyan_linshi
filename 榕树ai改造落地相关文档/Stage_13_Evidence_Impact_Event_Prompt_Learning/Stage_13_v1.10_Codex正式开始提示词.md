# Stage 13 v1.10 — Codex 正式开始提示词（Query First / Offline Learning）

这是 Stage 13 正式执行，不是重跑 Stage 01～12。

当前阶段：

```text
Stage 13 — Evidence / Impact / Event / Prompt Learning
```

## 1. 最小读取

先读：

```text
榕树ai改造落地相关文档/Stage_12_Context_Memory_Token_Freshness/reviews/Stage_12_to_Stage_13_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_12_Context_Memory_Token_Freshness/reviews/Stage_13_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_13_Evidence_Impact_Event_Prompt_Learning/
```

然后优先消费 Stage 12 `STAGE13_QUERY_HANDOFF.yaml` 和 Stage 11 Query Surface。

## 2. 核心边界

```text
Evidence != Authorization
Correlation != Causality
Learning Candidate != Applied Policy
Project Learning != Generic Core
```

## 3. 必须冻结

```text
Evidence Record / Chain
Impact Analysis / Graph
Decision / Change Evidence
Event Taxonomy
Causality Boundary
Prompt Observation
Outcome Attribution
Learning Candidate
Evaluation / Counterexample
Promotion Gate
Quality / Cost Telemetry
False Positive / Negative Register
Stage14 Governance Requirements
```

## 4. Prompt Learning

禁止：

```text
自动改 Prompt
自动改 Rule
自动改 Skill
Runtime 自我修改
单次成功自动升级 Core
```

Stage 13 只允许：

```text
observe
propose
evaluate
recommend promotion
```

## 5. Outcome Attribution

默认：

```text
MULTI_FACTOR / UNKNOWN
```

必须考虑 Prompt、Context、Provider、Capability、Tool、Human、Repo State、Task Difficulty。

## 6. CON-002

继续：

```text
TYPED_BLOCKED / NO_WINNER_SELECTED
```

不得通过事件频率、Prompt 历史或最近记录自动解决。

## 7. Historical References

REF-039/041/043/044 保持 `KEEP_UNRESOLVED_HISTORICAL`。

REF-107/108 保持 `NOT_A_REFERENCE`。

## 8. Secret

13 Secret 不进入 Learning Dataset / Evidence body / Prompt Candidate。

## 9. Low Token

禁止：

```text
全仓扫描
全 Prompt corpus 重读
Git history 重分析
全对话历史挖掘
Stage11 DB rebuild
```

只在 Evidence Gap 时定点读取。

## 10. Validation

执行 V13-01～V13-24。

9 项 Hard Metrics 必须全部为 0。

## 11. 写入

仅：

```text
.banyan-refactor/stages/13/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

不得修改 Canonical Prompt/Rule/Skill。

## 12. 完成

生成：

```text
ACCEPTANCE_REPORT.md
evidence/NEXT_STAGE_HANDOFF.yaml
STAGE14_GOVERNANCE_REQUIREMENTS.yaml
```

更新 Bootstrap。

Stage 13 完成后停止，不进入 Stage 14。

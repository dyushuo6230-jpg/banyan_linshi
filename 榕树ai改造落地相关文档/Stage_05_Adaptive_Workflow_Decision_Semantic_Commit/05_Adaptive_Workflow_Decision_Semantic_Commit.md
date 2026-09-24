# Stage 05：Adaptive Workflow / Decision Mechanism / Semantic Commit Policy

## 1. 本阶段目的

Stage 05 把前四阶段冻结的结构转成“Banyan 如何决定下一步、何时问人、何时阻塞、如何计划语义提交”的流程策略。

本阶段只冻结 **workflow / policy**，不实现 Git Commit Runtime。

## 2. Adaptive Workflow

Workflow Routing 输入至少：

```text
task_class
risk
scope
confidence
project_governance_mode
project_stage
authorization
cost_budget_state
change_workspace_state
```

输出：

```text
workflow_mode
required_gates
required_evidence
required_human_decisions
allowed_actions
blocked_actions
```

## 3. Governance / Work Modes

通用语义建议：

```text
LIGHT
STANDARD
FULL
```

它们只能改变流程重量，不能删除职责。

例如 LIGHT 可以减少文档数量，但不能绕过：

```text
Secret protection
Git identity safety
Human-confirmation-required decision
Reference integrity
Protected write boundary
```

## 4. 五级决策机制

冻结统一语义：

```text
L0 AUTO_SAFE
L1 AUTO_WITH_TRACE
L2 PROPOSE_AND_CONTINUE_IF_POLICY_ALLOWS
L3 HUMAN_CONFIRMATION_REQUIRED
L4 BLOCKED / OWNER_DECISION_REQUIRED
```

项目可通过 Overlay 定义触发条件，但不得降低 Core 安全底线。

## 5. Human Decision

Human Confirmation 必须结构化：

```text
decision_id
question
context
options
recommended-neutral-summary
impact
reversible
deadline_if_any
default_if_no_answer
blocking
evidence_refs
```

不得通过省 Token / LIGHT 模式跳过 L3/L4。

## 6. CON-001

Stage 05 必须将“通用知情决策规则 vs 项目 override”统一成：

```text
Core decision semantics
+
Project decision parameters
+
Non-overridable safety floor
```

如果实际 Evidence 足够，应冻结 Resolution。

若不足：

```text
TYPED_BLOCKED
```

并记录 owner / evidence needed / activation blocker。

## 7. Semantic Commit

用户命令：

```text
帮我把当前修改合理分批提交
```

定义为一条正式 Workflow：

```text
Inspect
→ Classify
→ Relate
→ Group
→ Validate Plan
→ Identity Precheck
→ Authorization Gate
→ [Future Execution]
→ Capture Commit
→ Evidence
→ Leftover Report
```

Stage 05 到 `Authorization Gate` 为止。

## 8. Change Classification

至少：

```text
READY
INCOMPLETE
UNRELATED
LOCAL_ONLY
SECRET_RISK
```

必须明确 disposition：

- READY：可进入候选提交组
- INCOMPLETE：默认不提交，除非用户显式授权且政策允许
- UNRELATED：单独隔离，不混入当前语义组
- LOCAL_ONLY：保持本地，不进入提交
- SECRET_RISK：强制阻塞

## 9. Semantic Grouping

Grouping 依据：

```text
task/change/batch
feature/fix/refactor/docs/test/config
dependency
atomicity
validation boundary
reviewability
rollback boundary
```

禁止仅按文件夹机械分组。

## 10. Hunk-aware Planning

允许规划：

```text
同一文件不同 hunk 属于不同语义组
```

但 Stage 05 只定义策略，不实际执行 hunk staging。

## 11. Commit Message Policy

定义中立格式，避免绑定特定编辑器。

至少支持：

```text
type(scope): summary
```

但具体项目可通过 Project Overlay 配置 Conventional-like 或其他格式。

Banyan Core 不强制项目必须 Conventional Commit。

## 12. Git Identity Policy

真实来源：

```text
git config user.name
git config user.email
```

未来提交执行前：

```text
身份可用 → 继续
身份缺失 → BLOCK / NEEDS_INPUT
```

AI 不：

```text
设置 user.name
设置 user.email
使用 --author
伪造 Author
```

## 13. Editor Neutral

Cursor / Codex / Claude / Generic Editor：

```text
只是 Execution Client
```

同一项目使用同一 Commit Policy。

不得：

```text
Cursor 一套
Codex 一套
Claude 一套
```

## 14. 完成条件

必须冻结：

```text
Adaptive Workflow Schema
Work Mode Contract
Decision Level Schema
Decision Escalation Contract
Human Confirmation Contract
CON-001 Resolution Record
Semantic Commit Workflow
Semantic Change Classification
Semantic Grouping Policy
Commit Message Policy
Git Identity Safety Policy
Commit Authorization Boundary
Leftover Reporting Contract
```

完成后停止。

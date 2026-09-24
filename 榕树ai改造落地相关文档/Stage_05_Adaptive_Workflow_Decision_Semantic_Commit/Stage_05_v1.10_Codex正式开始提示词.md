# Stage 05 v1.10 — Codex 正式开始提示词（低 Token）

这是 Stage 05 正式执行，不是重跑 Stage 01～04。

当前阶段：

```text
Stage 05 — Adaptive Workflow / Decision Mechanism / Semantic Commit Policy
```

## 1. 最小读取

先只读：

```text
榕树ai改造落地相关文档/Stage_04_Project_Instance_Source_Mapping_Profile/reviews/Stage_04_to_Stage_05_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_04_Project_Instance_Source_Mapping_Profile/reviews/Stage_05_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_05_Adaptive_Workflow_Decision_Semantic_Commit/
```

再读取 Low-Token Index 指定的 Stage 04 / Stage 03 输入。

## 2. 禁止重做

禁止：

```text
全仓扫描
重跑 477 Git commits 分析
重建 1026 Asset Inventory
重建 Stage02 Candidate
改写 Stage03 Frozen Contract
重做 Stage04 Project Instance
```

## 3. Stage 05 目标

完成并冻结：

```text
Adaptive Workflow Model
Governance / Work Mode Contract
Five-Level Decision Mechanism
Decision Escalation Contract
Human Confirmation Contract
CON-001 Resolution Record
Semantic Commit Workflow
Semantic Change Classification
Semantic Grouping / Hunk Policy
Commit Message Policy
Git Identity Safety Policy
Commit Authorization Boundary
Leftover Reporting Contract
```

## 4. CON-001

这是本阶段 Owner 项。

不要简单选择旧规则或当前项目 override。

目标：

```text
Generic Core = decision semantics
Project Overlay = project parameters
Safety Floor = non-overridable
```

若 Evidence 足够则 RESOLVED。
若不足则 `TYPED_BLOCKED`，记录 blocker，不得伪造解决。

CON-002 不在本阶段解决。

## 5. 五级机制

必须实现语义：

```text
L0 AUTO_SAFE
L1 AUTO_WITH_TRACE
L2 PROPOSE_AND_CONTINUE_IF_POLICY_ALLOWS
L3 HUMAN_CONFIRMATION_REQUIRED
L4 BLOCKED_OR_OWNER_DECISION_REQUIRED
```

不得通过 LIGHT 模式绕过 L3/L4。

## 6. Semantic Commit

本阶段只定义 policy/workflow。

严禁实际：

```text
git add
git commit
git reset
git stash
git rebase
git push
```

分类：

```text
READY
INCOMPLETE
UNRELATED
LOCAL_ONLY
SECRET_RISK
```

`SECRET_RISK` 必须 BLOCK。

## 7. Git Identity

实际身份：

```text
author.name + author.email
```

AI 不修改 `user.name/user.email`，不使用 `--author`，不猜物理操作者。

未来如果提交需要身份而身份缺失：

```text
BLOCK / NEEDS_INPUT
```

## 8. Editor Neutral

Cursor / Codex / Claude / Generic Editor 共用一套 Semantic Commit Policy。

Editor 只是 Execution Client。

## 9. Evidence-on-Demand

仅：

```text
DECISION_POLICY_CONFLICT
WORKFLOW_AMBIGUITY
SEMANTIC_COMMIT_POLICY_GAP
IDENTITY_POLICY_GAP
MISSING_EVIDENCE
```

才回读具体 Stage 01/02 Evidence。

## 10. Secret

13 个配置继续 metadata-only / PARTIAL_APPROVED。

## 11. Validation

执行 V05-01～V05-20。

所有硬指标必须为 0。

## 12. 写入范围

仅：

```text
.banyan-refactor/stages/05/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

## 13. 完成

生成真实：

```text
ACCEPTANCE_REPORT.md
evidence/NEXT_STAGE_HANDOFF.yaml
```

更新 Bootstrap。

Stage 05 完成后停止，不进入 Stage 06。

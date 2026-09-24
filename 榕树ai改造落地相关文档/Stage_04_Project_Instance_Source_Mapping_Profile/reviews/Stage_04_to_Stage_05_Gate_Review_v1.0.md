# Stage 04 → Stage 05 Gate Review v1.0

> Review Basis：Stage 04 Acceptance Report、VALIDATION_RESULTS、NEXT_STAGE_HANDOFF  
> Stage 04 Run：`stage04-20260920T142517Z`  
> Review Result：**PASS_FOR_STAGE05_DESIGN_WITH_INHERITED_BLOCKERS**  
> Stage 05 Execution：**NOT_STARTED / NOT_AUTHORIZED**

---

## 1. 最终结论

```text
Stage 04 = COMPLETED
Stage 04 Acceptance = PASS_PROJECT_INSTANCE_DESIGN / NOT_ACTIVATED
Stage 05 Entry Gate = PASS_FOR_STAGE05_DESIGN_WITH_INHERITED_BLOCKERS
Stage 05 Execution = NOT_STARTED
```

Stage 04 已完成 Project Instance / Source Mapping / Profile / Provider Binding 设计，且没有激活 `.banyan/`、没有移动项目目录、没有执行 Legacy Migration。

---

## 2. 已验证成果

```text
Source Roles = 9 / 9
Capability Overlay = 35 / 35
Provider Port Bindings = 35 / 35 (UNBOUND / INACTIVE)
Git Identities = 16 exact identities preserved
V04-01..V04-20 = PASS
Hard Metrics = 6 / 6 all zero
```

Project Instance 设计已覆盖：

```text
project identity
source mappings
project overlays
profiles
variables
provider bindings
feature activation
runtime/index/trace/generated/migrations locations
lineage
```

---

## 3. Stage 05 的正式职责

Stage 05 进入：

```text
Adaptive Workflow / Decision Mechanism
+
Semantic Commit Workflow / Policy Definition
```

Stage 05 负责“定义流程和策略”，不负责 Git Commit 执行实现。

必须设计：

```text
Adaptive Workflow Model
Governance Mode / Work Mode routing
Five-Level Decision Mechanism
Decision Escalation
Human Confirmation Contract
Workflow State / Transition Contract
Task / Change / Batch relationship
Semantic Commit Planning Workflow
Commit Grouping / Validation Policy
Commit Message Policy
Missing Git Identity behavior
Editor-neutral commit policy
Leftover / unrelated / secret-risk handling
```

---

## 4. Semantic Commit Owner Boundary

冻结职责：

```text
Stage 03 = Schema
Stage 05 = Workflow / Policy Definition
Stage 11 / 13 = Index / Evidence
Stage 14 / 15 = Safety + Execution Implementation
Stage 17 / 18 = Pilot
Stage 19 = Verification
Stage 20 = Release
```

因此 Stage 05 禁止直接：

```text
git add
git commit
git reset
git stash
git rebase
git push
修改 user.name / user.email
使用 --author
```

只定义行为契约。

---

## 5. Git Identity 继承规则

必须保持：

```text
author.name + author.email = Banyan contribution identity
```

AI 不：

```text
猜测物理操作者
修改 Git identity
自动 alias / merge identities
强制切换身份
```

若某个未来提交动作需要身份而当前身份不可用：

```text
BLOCK / NEEDS_INPUT
```

不得伪造 Author。

Contributor Profile 只用于显示增强，不参与授权。

---

## 6. CON-001：Stage 05 Owner

`CON-001` 是 Stage 05 的必须处理项。

Stage 05 不应简单选择“旧通用规则”或“当前项目规则”作为永久 winner。

应冻结一个可通用的 Decision Policy / Override Contract，使：

```text
Generic Core 定义 decision semantics
Project Instance 可声明项目级决策参数
Project Overlay 不能绕过 Core 安全/人工确认底线
冲突时可结构化 BLOCK / ESCALATE / NEEDS_INPUT
```

Stage 05 应使 `CON-001` 从“未建模冲突”转为“已建模、可配置、可验证的决策机制”。

是否可以标记 RESOLVED，必须由实际 Evidence 和验证结果决定，不允许预写 PASS。

`CON-002` Owner 仍为 Stage 12，本阶段只继承，不裁决。

---

## 7. 五级决策机制要求

Stage 05 必须正式化五级机制，但不得把具体项目阈值硬编码进 Generic Core。

建议语义层：

```text
L0 AUTO_SAFE
L1 AUTO_WITH_TRACE
L2 PROPOSE_AND_CONTINUE_IF_POLICY_ALLOWS
L3 HUMAN_CONFIRMATION_REQUIRED
L4 BLOCKED / OWNER_DECISION_REQUIRED
```

实际项目可以通过 Project Overlay 配置适用条件，但：

```text
不能把高风险动作降级为无确认
不能绕过 Secret / Git identity / protected write policy
```

---

## 8. Adaptive Workflow 要求

Workflow 必须基于：

```text
task type
risk
change scope
evidence confidence
project governance mode
current project stage
authorization
budget/cost governance
```

动态选择：

```text
LIGHT
STANDARD
FULL
```

或其它冻结后的抽象工作模式。

重点：

```text
流程重量自适应
职责不丢
Evidence 不丢
关键 Gate 不丢
```

不能用“轻量模式”绕过安全规则。

---

## 9. Semantic Commit Workflow 必须覆盖

用户意图：

```text
“帮我把当前修改合理分批提交”
```

未来流程定义应至少包含：

```text
inspect status/diff
identify workflow/task/change/batch
classify changes
semantic grouping
hunk-aware planning
validation per group
identity precheck
commit plan
commit execution authorization boundary
capture actual commit
evidence / trace
leftover report
```

分类至少：

```text
READY
INCOMPLETE
UNRELATED
LOCAL_ONLY
SECRET_RISK
```

Stage 05 只冻结 plan/policy，不执行 commit。

---

## 10. Low-Token 原则

Stage 05 默认读取：

```text
本 Gate Review
Stage 05 Low-Token Input Index
Stage 04 NEXT_STAGE_HANDOFF
Stage 03 Frozen Contract surfaces
Stage 04 Project Instance / Overlay / Profile / Binding design
CON-001 evidence
Stage 01 Git Identity / Commit Practice inventory（仅相关部分）
```

禁止：

```text
全仓重新扫描
重跑 477 Git commits 分析
重新盘 1026 项资产
重建 Stage 02 / 03 / 04
```

只有遇到：

```text
DECISION_POLICY_CONFLICT
WORKFLOW_AMBIGUITY
SEMANTIC_COMMIT_POLICY_GAP
IDENTITY_POLICY_GAP
MISSING_EVIDENCE
```

才定点回读。

---

## 11. 继承风险

继续继承：

```text
R03-PURITY
R03-SOURCE
CON-002
R03-COST
R03-SECRET
R03-LOCAL
```

`CON-001` 进入 Stage 05 主处理范围。

13 Secret 继续：

```text
SECRET_METADATA_ONLY
PARTIAL_APPROVED
```

---

## 12. Gate Decision

```text
Stage 04 → Stage 05 = PASS_FOR_STAGE05_DESIGN_WITH_INHERITED_BLOCKERS
Stage 05 Pack Generation = ALLOWED
Stage 05 Execution = NOT YET AUTHORIZED
```

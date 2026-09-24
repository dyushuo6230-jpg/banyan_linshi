# Stage 14 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_13_to_Stage_14_Gate_Review_v1.0.md`
2. Stage 13:
   - `STAGE14_GOVERNANCE_REQUIREMENTS.yaml`
   - `evidence/NEXT_STAGE_HANDOFF.yaml`
   - Evidence / Impact / Learning Promotion contracts
3. Stage 05:
   - Work Mode Contract
   - Decision Level Schema
   - Human Confirmation Contract
   - Semantic Commit Policy
   - Git Identity Policy
4. Stage 04:
   - Contributor Profile Schema
   - Project Overlay / Variable Resolution
5. Stage 03:
   - AI Runtime Governance Contract
   - Source Role / Authority
   - Reference / Version / Status / Provenance
6. Stage 00:
   - Secret protection metadata/policy
7. Stage 11/12:
   - Freshness/query state for protected targets when needed

## 2. Git 定点读取

Stage 14 只允许读取：

```text
git status --porcelain/v2
git diff --stat / targeted diff metadata
git diff --cached --stat
git config --get user.name
git config --get user.email
git symbolic-ref / rev-parse metadata
```

用于设计验证或 Shadow Policy Evaluation。

禁止任何 Git mutation。

## 3. Semantic Commit 定点输入

只读取当前冻结的：

```text
READY
INCOMPLETE
UNRELATED
LOCAL_ONLY
SECRET_RISK
```

分类策略与 Identity 规则。

不要重跑 477 commits 历史分析。

## 4. Evidence-on-Demand Triggers

```text
ACTION_RISK_AMBIGUITY
AUTHORIZATION_PRECONDITION_GAP
PROTECTED_TARGET_AMBIGUITY
GIT_IDENTITY_AMBIGUITY
WORKTREE_CLASSIFICATION_GAP
SECRET_RISK_AMBIGUITY
FRESHNESS_BLOCKER
ROLLBACK_PRECONDITION_GAP
MISSING_EVIDENCE
```

## 5. 默认禁止

```text
repo rediscovery
Git history full analysis
git mutation
canonical mutation
Stage15 runtime implementation
```

## 6. Token 主要花费对象

```text
Risk Classification
Permission Decision
Authorization Record
Protected Write
Git Identity
Worktree Safety
Commit Authorization
Audit Requirements
Stage15 Runtime Contract
```

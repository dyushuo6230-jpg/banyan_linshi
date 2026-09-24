# Stage 05 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_04_to_Stage_05_Gate_Review_v1.0.md`
2. Stage 04 `evidence/NEXT_STAGE_HANDOFF.yaml`
3. Stage 04:
   - `PROJECT_INSTANCE_SCHEMA.yaml`
   - `PROJECT_INSTANCE_LAYOUT_CONTRACT.yaml`
   - `SOURCE_MAPPING_SCHEMA.yaml`
   - `SOURCE_MAPPING_REGISTRY.yaml`
   - `PROJECT_OVERLAY_BINDINGS.yaml`
   - `VARIABLE_RESOLUTION_SCHEMA.yaml`
   - `PROJECT_PROFILE_SCHEMA.yaml`
   - `CONTRIBUTOR_PROFILE_SCHEMA.yaml`
   - `PROVIDER_BINDING_SCHEMA.yaml`
4. Stage 03:
   - `CAPABILITY_CONTRACT_REGISTRY.yaml`
   - `CANONICAL_CONTRACT_SCHEMA.yaml`
   - `AI_RUNTIME_GOVERNANCE_CONTRACT.yaml`
   - `VERSION_STATUS_PROVENANCE_RULES.yaml`
   - `CONFLICT_CARRYOVER_REGISTER.yaml`
5. Stage 01:
   - `GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml`
   仅读取 Semantic Commit / Git Identity 相关段落。

## 2. CON-001 定点读取

只读取支持以下问题的 Evidence：

```text
通用 IDP 规则是什么
当前项目 override 是什么
冲突具体发生在哪里
哪些底线不能被 override
```

不要把整个 Stage 01/02 Evidence 全部重新读入上下文。

## 3. 默认禁止

```text
重新扫描 Repository
重新分析 477 Git commits
重新生成 1026 Asset Inventory
重新生成 Stage 02 Candidate Mapping
重新冻结 Stage 03 Contract
重新设计 Stage 04 Project Instance
```

## 4. Evidence-on-Demand 触发器

```text
DECISION_POLICY_CONFLICT
WORKFLOW_AMBIGUITY
SEMANTIC_COMMIT_POLICY_GAP
IDENTITY_POLICY_GAP
MISSING_EVIDENCE
```

## 5. Stage 05 Token 主要花费对象

```text
Adaptive Workflow
Five-Level Decision Mechanism
Decision Escalation
Work/Governance Mode
Semantic Commit Workflow
Commit Planning / Grouping Policy
Git Identity Safety Policy
Commit Message Policy
Human Confirmation Boundary
```

而不是重新盘仓库。

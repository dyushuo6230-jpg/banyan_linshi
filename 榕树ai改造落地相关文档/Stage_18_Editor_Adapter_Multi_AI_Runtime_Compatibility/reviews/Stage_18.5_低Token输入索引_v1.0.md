# Stage 18.5 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_18_to_Stage_18.5_Gate_Review_v1.0.md`
2. Stage 18:
   - `NEXT_STAGE_HANDOFF.yaml`
   - `ADAPTER_VALIDATION_RESULT.yaml`
   - `evidence/VALIDATION_RESULTS.yaml`
   - `evidence/PILOT_INTEGRITY.yaml`
3. Stage 16:
   - Control Plane API Contract
   - WebUI State / Provenance / Project Safety Contracts
4. Stage 15:
   - Runtime API stable interface
   - CLI/runtime entrypoints only
5. Stage 14:
   - Permission / Authorization / Git safety machine contracts
6. Stage 17:
   - Pilot `.banyan` integrity/readiness records only when needed

## 2. 先做 Current Implementation Inventory

只盘点：

```text
现有 WebUI source root
现有 Control Plane source root
现有 Runtime API boundary
现有 frontend build command
现有 backend/server entrypoint
现有 UI routes/features
```

禁止 repo-wide rediscovery。

## 3. 前端迁移最小输入

只读取 Stage 16 已实现页面/功能：

```text
Dashboard
Runtime / Policy
Project Safety
Gate / Blockers
Preflight
Commit Plan
Dry-run
Trace / Audit
Provenance
Provider Bindings
Stage / Run
Activation
```

用 Feature Equivalence Matrix 迁移，不重做业务语义。

## 4. Go/Gin 最小输入

只读取：

```text
Stage15 Runtime API
Stage16 Control Plane HTTP contract
Stage18 Adapter Gateway path
```

不要重新解释 Stage 14 Policy。

## 5. Ant Design Pro Simple

使用：

```text
Simple / minimal baseline
```

删除：

```text
demo pages
mock services
sample business
unused example dependencies
```

保留：

```text
layout
routing
theme
required ProComponents
Banyan features
```

## 6. Evidence-on-Demand Triggers

```text
RUNTIME_BRIDGE_AMBIGUITY
HTTP_CONTRACT_MISMATCH
FEATURE_EQUIVALENCE_GAP
PROVENANCE_RENDERING_GAP
SPA_EMBED_ROUTING_GAP
GOGIN_LOCAL_BIND_SAFETY_GAP
ADAPTER_COMPATIBILITY_REGRESSION
PILOT_INSTANCE_INTEGRITY_GAP
TEST_FAILURE
```

## 7. 默认禁止

```text
Legacy rescan
Stage01-18 rerun
full Runtime rewrite
project document migration
.banyan restructure
Git mutation
Stage19 execution
```

## 8. Token 主要花费对象

```text
frontend feature migration
Go/Gin transport
runtime bridge
embedded build
contract tests
regression tests
feature equivalence
```

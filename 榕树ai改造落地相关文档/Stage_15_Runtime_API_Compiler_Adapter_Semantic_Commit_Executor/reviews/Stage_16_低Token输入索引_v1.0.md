# Stage 16 低 Token 输入索引 v1.0

## 1. 默认读取顺序

1. `Stage_15_to_Stage_16_Gate_Review_v1.0.md`
2. Stage 15:
   - `STAGE16_RUNTIME_API_HANDOFF.yaml`
   - Runtime API source / stable models
   - CLI / Runtime tests（只读接口相关）
3. Stage 14:
   - Permission Decision
   - Authorization Record
   - Git Identity / Worktree / Protected Write gates
4. Stage 11/12:
   - Provenance / Freshness / Query Surface（仅 UI 所需）
5. Stage 04:
   - Project Instance / Provider Binding schemas
6. Stage 03:
   - Artifact / Source Role / Reference contracts

## 2. 不重新分析 Runtime

Stage 16 不重做：

```text
Policy Compiler
Semantic Commit logic
Git safety policy
Freshness policy
```

只调用 Stage 15 Runtime API。

## 3. 当前项目读取

允许：

```text
runtime status
preflight
git inspect metadata
commit plan
dry-run execution
trace/evidence query
provider status
```

禁止 mutation。

## 4. UI 定点数据

只加载当前屏幕/当前操作需要的数据。

禁止：

```text
一次性把 1911 entities 全塞进前端
一次性加载 1740 artifacts 正文
全量加载 trace/history
```

默认分页 / query-on-demand。

## 5. Evidence-on-Demand Triggers

```text
CONTROL_PLANE_API_GAP
PROVENANCE_FIELD_GAP
RUNTIME_RESULT_RENDERING_GAP
AUTHORIZATION_UI_AMBIGUITY
SECRET_UI_EXPOSURE_RISK
LOCAL_BINDING_SAFETY_GAP
PILOT_ACTIVATION_PRECONDITION_GAP
TEST_FAILURE
```

## 6. Token 主要花费对象

```text
Control Plane API
UI state model
Provenance rendering
Gate/blocker rendering
dry-run workflow
local-only safety
Stage17 activation readiness
```

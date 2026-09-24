# 03-B：Capability Contract Registry

## 目标

把 Stage 02 的 35 项 Capability Candidate 全部纳入契约注册。

每项至少：

```text
capability_id
candidate_layer
contract_id
freeze_status
owner_stage
provider_port_required
project_overlay_required
compatibility_required
evidence_refs
open_conflicts
```

## 覆盖规则

```text
35/35 accounted
UNMAPPED_HIGH_VALUE_CAPABILITY = 0
SILENT_CAPABILITY_DROP = 0
```

若某项不能冻结：

```text
DEFERRED_WITH_OWNER
```

必须有后续阶段与激活阻塞条件。

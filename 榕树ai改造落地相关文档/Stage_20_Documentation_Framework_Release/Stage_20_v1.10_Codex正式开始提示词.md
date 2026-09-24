# Stage 20 v1.10 — Codex 正式开始提示词
## Documentation / Framework Release / Final Handoff

Stage19 已通过。现在执行 Stage20。

Stage20 是整个施工链的文档、Framework Release 和最终交接收口阶段。

它不是新功能实现阶段，也不是 Project Final Activation。

## 1. Read First

读取：

```text
Stage_19_to_Stage_20_Gate_Review_v1.0.md
Stage_20_低Token输入索引_v1.0.md
Stage_20_Documentation_Framework_Release/
```

然后优先读取 Stage19：

```text
ACCEPTANCE_REPORT.md
RC_MANIFEST.yaml
STAGE20_HANDOFF.yaml
evidence/FINAL_VERIFICATION.yaml
```

不要重新读取 Stage01-19 全量资料。

## 2. Final Architecture

文档必须准确描述：

```text
Ant Design Pro Simple
→ Go/Gin + go:embed
→ LOCAL_STDIO Bridge
→ Python Banyan Runtime Core
```

不要写成“整个 Banyan 是 Go”。

## 3. Separate Release and Activation

严格区分：

```text
Banyan Framework Release
!=
Current Project Final Activation
```

当前仍：

```text
CON-002 = TYPED_BLOCKED_HUMAN_PROJECT_AUTHORITY
FINAL_ACTIVATION = NOT_AUTHORIZED
```

禁止自动解决。

## 4. `.banyan-refactor`

正式记录：

```text
.banyan-refactor
= first-construction bootstrap workspace
= temporary
= not normal future upgrade workspace
```

未来 Framework 升级使用 Banyan 自己的 Change/Migration/Validation/Rollback 机制。

由于 Final Activation 仍 blocked：

```text
不要直接删除 .banyan-refactor
```

只生成 Retirement Plan / Archive Manifest / Preconditions。

## 5. Legacy docs

生成正式：

```text
Legacy Documentation Adoption Migration Guide
```

用于未来把 `docs/project` 等既有资料转换成 Banyan 可管理的 Artifact 语义。

本阶段：

```text
DOCUMENT ONLY
DO NOT EXECUTE MIGRATION
```

默认 preserve-in-place，不批量搬文档。

## 6. Version Governance

已有：

```text
v1.9.1 = CURRENT / FINAL_FREEZE
v1.10 = additive supplement
```

Stage20 生成 `VERSION_TRANSITION_PROPOSAL.yaml`。

没有明确 Human Approval 时：

```text
READY_FOR_HUMAN_APPROVAL
replace_current_pointer = false
```

不要静默修改 CURRENT。

## 7. Documentation Set

至少完成：

```text
Final Architecture Guide
Install / Build / Run Guide
WebUI / Control Plane Guide
Runtime / Adapter Guide
Project Instance Guide
Governance / Security Guide
Upgrade / Migration Guide
Legacy Documentation Adoption Guide
Operations / Troubleshooting Guide
Framework Release Notes
Framework Release Manifest
Bootstrap Retirement Plan
Version Transition Proposal
Final Handoff
```

## 8. Safety

禁止：

```text
project Git mutation
Pilot .banyan mutation/promotion
Secret body read/exposure
Runtime rewrite
WebUI redesign
Legacy migration execution
CON-002 winner selection
Final Activation
```

## 9. Validation

执行：

```text
V20-01..V20-24
```

10 项 Hard Metrics 全部必须为 0。

## 10. Finish

生成至少：

```text
ACCEPTANCE_REPORT.md
ACCEPTED_FINAL_STATE.yaml
FRAMEWORK_RELEASE_MANIFEST.yaml
VERSION_TRANSITION_PROPOSAL.yaml
BOOTSTRAP_RETIREMENT_PLAN.yaml
LEGACY_DOC_ADOPTION_PLAN.yaml
FINAL_HANDOFF.yaml
evidence/FINAL_VERIFICATION.yaml
```

完成后 STOP。

不要自动执行 Final Activation。

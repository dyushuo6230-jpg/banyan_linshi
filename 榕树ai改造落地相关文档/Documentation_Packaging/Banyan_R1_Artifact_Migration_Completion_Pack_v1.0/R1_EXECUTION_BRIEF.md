# R1 Execution Brief

## 1. R1 接着解决什么

R0 已解决：

```text
FRAMEWORK_RELEASE_NOT_SELF_CONTAINED
```

但 R0 明确保留：
- Legacy Artifact Migration completion
- Adaptive Workflow frozen but no executor
- Natural-language orchestration not implemented
- Canonical Apply executor absent
- Collaboration roles not Runtime-bound
- Project Instance full binding pending R3

R1 只解决“Artifact Migration Completion”。

## 2. R1 输入来源必须分级

每个正式 Artifact 的来源必须属于以下之一：

```text
LEGACY_MIGRATION
REFRACTOR_ADDITION
GENERALIZED
NEW_PROPOSAL
```

### LEGACY_MIGRATION
来自 v3.1 Legacy，语义保留后结构化迁移。

### REFRACTOR_ADDITION
来自后续总纲 / accepted Stage Contract 中已经新增并 frozen/accepted 的 Banyan 设计。

### GENERALIZED
从一个或多个已有语义抽象成 Framework 通用 Artifact，但不得改变核心语义。

### NEW_PROPOSAL
当前施工才新想到、此前无 accepted/frozen 依据的内容。

`NEW_PROPOSAL` 不得直接进入正式 Registry。
必须进入 `R1_NEW_PROPOSAL_REGISTER.yaml` 并等待 Human Decision。

## 3. R1 不是按目录凑数量

禁止：

```text
看到 roles/ 就硬造 Role
看到 skills/ 就硬拆 Skill
看到 workflow 就把每段流程都拆文件
```

必须按真实语义和 Owner 来定。

## 4. Artifact 必须可追踪

建议每个 Artifact 至少有：

```yaml
id:
type:
version:
status:
purpose:
when_to_use:
when_not_to_use:
inputs:
outputs:
dependencies:
permissions:
forbidden:
validation:
compatibility:
provenance:
implementation_status:
```

其中 provenance 至少应包含：

```yaml
origin:
source_document:
source_stage:
legacy_reference:
refactor_contract:
semantic_change:
```

如果 `semantic_change: true` 且不是已有 accepted contract 明确要求，必须 BLOCK 并转 Human Decision。

## 5. Token Efficiency 约束

R1 必须建立“省 Token 但不丢治理语义”的 Context 规则：

```text
Index / Registry first
→ targeted source read
→ canonical fallback on high-risk judgment
```

不能：

```text
summary-only migration
stage-summary-only migration
skip provenance because of token cost
```

## 6. R1 完成后应该得到什么

至少：

```text
Framework-native Artifact set
Artifact migration matrix
Legacy compatibility relation
Refactor-addition provenance
No-loss evidence
Token-safe context requirements
New proposal register
Acceptance report
```

## 7. R1 不做什么

不实现：
- Adaptive Workflow executor
- Natural-language orchestration
- Canonical Apply executor
- Collaboration Role Runtime authorization
- Final Project Instance binding
- WebUI Help Center
- Final Activation

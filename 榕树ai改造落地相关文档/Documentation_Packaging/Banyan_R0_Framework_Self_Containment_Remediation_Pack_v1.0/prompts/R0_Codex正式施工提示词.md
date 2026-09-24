# Banyan R0 — Framework Self-Containment Remediation

请严格执行 R0 Framework Self-Containment Remediation。

这是一次真正会修改 `banyan-framework/**` 的修复施工。
只解决 Framework Self-Containment（框架自包含）问题，不进入 R1/R2/R3。

---

# A. 必读输入

## A1. 当前 Framework
完整定点审计：

```text
banyan-framework/**
```

重点：
- `src/banyan/**`
- `policies/**`
- `tests/**`
- `docs/**`
- `pyproject.toml`
- `control-plane-go/**`
- `frontend/**`（只读，本轮原则上不修改）

## A2. 当前 Project Instance
只读：

```text
.banyan/**
```

用于理解 Binding 边界，但禁止把 Project Instance 内容迁入 Framework Core。

## A3. D1.5 审计产物
完整读取：

```text
榕树ai改造落地相关文档/Documentation_Packaging/Implementation_Reconciliation_Audit/
```

重点：
- `BANYAN_IMPLEMENTATION_GAP_AUDIT.md`
- `V3_1_ARTIFACT_MIGRATION_MATRIX.yaml`
- `CAPABILITY_IMPLEMENTATION_MATRIX.yaml`
- `FRAMEWORK_SELF_CONTAINMENT_AUDIT.md`
- `DEFERRED_VS_MISSING_IMPLEMENTATION.md`
- `REMEDIATION_PRIORITY_PROPOSAL.md`
- `D1_5_ACCEPTANCE_REPORT.md`

如果实际目录名不同，使用真实 D1.5 输出目录。

## A4. Stage 权威设计依据
只定点读取与 R0 直接相关的最终 accepted 文档：

```text
Stage 01  Legacy/Capability Inventory
Stage 02  Target Architecture / Boundary
Stage 03  Artifact Contract / Schema / Registry
Stage 04  Project Instance / Source Mapping / Profile
Stage 05  Workflow / Decision / Semantic Commit Contract
Stage 07  Legacy No-Loss Migration
Stage 09  UI Design Intelligence provider boundary
Stage 14  Governance / Permission / Git Safety
Stage 15  Runtime API / Compiler / Adapter implementation
Stage 18/18.5 Adapter / Control Plane architecture
Stage 19  Full Acceptance
Stage 20  Final Architecture / Framework Release / Handoff
```

Source priority：

```text
1. current accepted implementation
2. Stage20 final accepted architecture/release facts
3. earlier frozen contract referenced by Stage20
4. D1.5 audit
5. legacy proposal / v3.1 source
```

如冲突，必须按优先级处理并在报告记录。

---

# B. 本轮唯一目标

解决：

```text
FRAMEWORK_RELEASE_NOT_SELF_CONTAINED
```

使正式 `banyan-framework/` 在脱离施工目录后，仍能自解释以下内容：

```text
Capability Contracts
Artifact Contracts / Types
Source Roles
Workflow / State Contracts
Provider Port Contracts
Project Overlay / Binding Contracts
Compatibility Mapping
Version / Status / Provenance Rules
Schema Index
Framework Contract Manifest
```

---

# C. 先设计再修改

禁止一上来就创建 `roles/skills/workflows` 等目录。

先生成内部施工计划（可写临时文件到 R0 workspace 或最终验收报告草稿），回答：

1. 当前 Framework 已有哪个目录最适合作为正式 Contract 归属？
2. 哪些定义已经在 Python source 中有唯一真源，不应重复创建 YAML？
3. 哪些目前只存在于 Stage 文档，必须迁入 Framework？
4. 哪些应做 authoritative asset？
5. 哪些只应做 generated index / projection？
6. Loader / Validator 从哪里加载最合理？
7. 如何避免引入第二套 Policy / Permission 真源？

完成这个分析后再施工。

---

# D. 推荐目标结构（非强制）

可以采用类似：

```text
banyan-framework/
├── contracts/
│   ├── manifest.yaml
│   ├── capabilities.yaml
│   ├── artifacts.yaml
│   ├── source_roles.yaml
│   ├── workflows.yaml
│   ├── states.yaml
│   ├── provider_ports.yaml
│   ├── project_overlay.yaml
│   └── compatibility/
│       └── v3_1.yaml
│
├── schemas/
│   └── ...
│
├── src/banyan/contracts/
│   ├── loader.py
│   ├── validator.py
│   └── models.py
│
└── tests/
    └── ...
```

但如果现有架构有更合适的目录，优先复用。

重点是“职责和唯一真源”，不是目录名字。

---

# E. 必须迁入 Framework 的正式定义

以 Stage03/07/20 和 D1.5 为准，至少审计并处理：

## E1 Capability Contract Registry
- 35 个 `CAP-*`
- stable id
- version
- status
- purpose
- target layer
- implementation binding status
- provider / overlay requirements
- compatibility source

注意：
`FROZEN_CONTRACT` 不等于 `IMPLEMENTED`。

## E2 Artifact Contract / Type Registry
至少覆盖被 accepted 的：
- PRD
- UI_SPEC
- ADR
- DEC
- CR / Change
- Trace / Evidence
- Project Guide / Handover / Worklog 等实际 accepted artifact

不要凭 D1 文档列表擅自扩充 Runtime contract。

## E3 Source Role Registry
把 Framework-level source roles 正式化。
Project-specific path mapping 继续留在 `.banyan/`。

必须保持：

```text
Source Role != physical directory
```

## E4 Workflow / State Contract Index
R0 只把已冻结 Contract 带入 Framework，不实现 executor。

必须至少能标识：
- adaptive workflow contract
- change lifecycle contract
- decision flow contract
- semantic commit flow
- current runtime request flow（若它是实现流程，不要误当 frozen workflow artifact）

## E5 Provider Port / Binding Contract
正式纳入 Framework-level provider port schema / binding contract。
具体项目 provider binding 留在 `.banyan/providers/**`。

## E6 Project Overlay Contract
Framework 只定义 overlay schema/规则。
具体 overlay 内容留在 `.banyan/overlays/**`。

## E7 Compatibility Mapping
把属于 Framework Release 的 v3.1 compatibility mapping 从施工证据提升为正式 Framework asset。

必须能够追踪：

```text
legacy_semantic
→ target_contract
→ target_layer
→ compatibility disposition
```

R0 不负责补实现，只负责正式收容并可校验。

## E8 Version / Status / Provenance
必须统一说明并可机器读取：
- contract version
- artifact version
- framework release
- implementation status
- provenance / source evidence
- supersedes / compatibility

不得把 Governance CURRENT pointer、Framework Release、Python package version 合并成一个字段。

---

# F. Loader / Validator

R0 必须至少提供一个稳定程序入口，能够：

```text
load_framework_contracts()
validate_framework_contracts()
```

函数名可不同，但必须满足：

- 能加载 Framework-owned contract manifest；
- 能校验 ID 唯一性；
- 能校验 schema/version/status；
- 能校验 cross-reference；
- 能发现 dangling reference；
- 能校验 35 CAP-* 全部 accounted；
- 不依赖 `.banyan-refactor/**`；
- 不依赖当前 Reference Project；
- 不成为第二 Runtime permission engine。

如果已有 Stage03/15 loader/validator，可复用和提升，不重复造轮子。

---

# G. Runtime / Adapter 集成边界

本轮允许做“最小引用接入”：

```text
Runtime / CLI / validator 可以读取 Framework Contract Manifest
```

但禁止：
- 重构 Runtime；
- 实现新 Workflow executor；
- 实现 Skill executor；
- 实现 Role authorization；
- 改 Permission decision semantics；
- 改 Git behavior。

如果当前 Runtime 不需要主动消费某些 contract，保持只读 discoverability/validation 即可。

---

# H. Documentation

更新：

```text
banyan-framework/docs/maintainer/
```

或现有对应维护文档，说明：

- Contract 真源目录；
- Registry 真源；
- Schema 真源；
- Loader / Validator；
- Compatibility；
- Framework 与 `.banyan` 的边界；
- 如何新增 Contract；
- 如何验证。

可以同步修订 D0/D1 中“Framework 不 self-contained”的状态说明，但：

**不要启动 D2 正式续写，也不要把 Gap 提前标记关闭，直到 R0 验收通过。**

---

# I. Tests

至少增加自动测试覆盖：

1. Framework Contract Manifest 可加载。
2. 35 CAP-* 全部存在且 ID 唯一。
3. Contract cross-reference 无 dangling。
4. Schema/registry 可以脱离施工目录运行。
5. 不含 Reference Project 业务专有路径/名称。
6. Provider Binding contract 与 project-specific binding 分离。
7. Source Role 与 physical path 分离。
8. Compatibility mapping 可解析。
9. Framework release / governance pointer / package version 维度未混淆。
10. 原 Stage15 Runtime 测试全部不回归。
11. Stage18 Adapter regression 不回归（如测试在当前包可运行）。
12. `banyan-framework/**` 中不新增 secret。

---

# J. 禁止事项

R0 禁止：

```text
修改 .banyan/**（只读）
迁移 docs/project/**
修改业务代码
实现 Adaptive Workflow executor
实现 natural-language orchestration
实现 Canonical Apply executor
实现 collaboration runtime roles
实现 /help
Final Activation
删除 .banyan-refactor
改变 Governance CURRENT pointer
把 v1.10 自动改成 CURRENT
```

---

# K. 验收输出

生成：

```text
banyan-framework/docs/maintainer/R0_FRAMEWORK_SELF_CONTAINMENT_ACCEPTANCE_REPORT.md
```

如果 maintainer 目录实际尚不存在，可放：

```text
banyan-framework/docs/R0_FRAMEWORK_SELF_CONTAINMENT_ACCEPTANCE_REPORT.md
```

报告必须包含：

- Result
- Problem addressed
- New authoritative Framework assets
- Generated/projection assets
- Loader / Validator
- Tests
- Generic Purity check
- Self-containment test
- 35 Capability accounting result
- v3.1 compatibility status
- Runtime regression
- Files changed
- Existing gaps intentionally preserved
- New gaps
- Human decisions required
- Rollback plan
- Stop condition

建议结果值：

```text
PASS_R0_FRAMEWORK_SELF_CONTAINMENT
PASS_R0_WITH_CARRIED_GAPS
FAIL_R0
```

只有真正做到 Framework 脱离施工目录仍可解释/校验自己的正式 contract，才能 PASS。

---

# L. 完成后停止

完成 R0 后停止。

不得继续：
- R1 v3.1 Artifact Migration Completion
- R2 orchestration
- R3 Project Instance binding
- D2/D3
- WebUI Help Center

# Banyan D1.5 — v3.1 / Stage00~20 / Current Framework Implementation Reconciliation

## 本轮性质

只读审计。禁止为了让结果好看而补代码、补目录、补 Registry、补文档。

完成审计报告后停止。

## 必读输入

### 当前真实实现
- `banyan-framework/**`
- `.banyan/**`

### 文档事实底座
- `banyan-framework/docs/DOCUMENTATION_SOURCE_OF_TRUTH.yaml`
- `banyan-framework/docs/DOCUMENTATION_INVENTORY.md`
- `banyan-framework/docs/D1_FOUNDATION_ACCEPTANCE_REPORT.md`

### 改造依据
定点读取 `榕树ai改造落地相关文档/**` 中：
- Stage 01：Legacy / Capability Inventory
- Stage 02：目标架构 / Boundary
- Stage 03：Contract / Registry / Source Role
- Stage 04：Project Instance / Mapping / Profile
- Stage 05：Workflow / Decision / Semantic Commit
- Stage 06：Change / Canonical Apply
- Stage 07：v3.1 Legacy No-Loss Migration
- Stage 09：UI Design Intelligence
- Stage 10：Project Guide / Knowledge Publishing
- Stage 11：SQLite Index / Trace / History
- Stage 12：Context / Memory / Freshness / Token
- Stage 13：Evidence / Impact / Event / Prompt Learning
- Stage 14：Permission / Governance / Git Safety
- Stage 15：Runtime implementation
- Stage 18 / 18.5：Adapters / WebUI
- Stage 19：Full Acceptance
- Stage 20：Final Architecture / Release / Handoff

### Legacy v3.1
如果仓库中仍有原始 v3.1 主文档/规则，必须定点读取。
如果没有，报告 `LEGACY_V3_1_SOURCE_NOT_AVAILABLE`，不得仅凭 Stage 摘要伪造逐条映射。

## 审计问题 A：AI Artifact 迁移

逐类检查：
- ROLE
- POLICY
- SKILL
- WORKFLOW
- STATE
- TEMPLATE
- DECISION PROTOCOL
- CONTEXT / RECOVERY
- COMPATIBILITY

每项回答：
1. Legacy 来源是什么？
2. Stage 01/02 给它的目标归宿是什么？
3. Stage 03/05/07 是否冻结了 Contract？
4. 当前 Framework 中真实文件在哪里？
5. 是否有 Registry Entry？
6. 是否有 Loader / Consumer？
7. 是否有 Runtime 执行路径？
8. 是否有测试？
9. 是否只是 Documentation Reference？
10. 是否被有证据地 supersede/generalize？

状态只能从：
- IMPLEMENTED
- MIGRATED_AS_ARTIFACT
- GENERALIZED_TO_POLICY
- GENERALIZED_TO_CAPABILITY
- GENERALIZED_TO_RUNTIME_API
- PROVIDER_BOUND
- PROJECT_OVERLAY_BOUND
- COMPATIBILITY_ONLY
- FROZEN_CONTRACT_ONLY
- PARTIALLY_MIGRATED
- MISSING_MIGRATION
- SUPERSEDED_WITH_EVIDENCE
- NOT_APPLICABLE
中选择。

## 审计问题 B：35 Capability Contract

对全部 `CAP-*` 逐条建立矩阵：
- capability_id
- legacy_source
- frozen_contract
- target_layer
- current_implementation
- provider_binding
- project_overlay
- runtime_consumer
- tests
- docs
- status
- missing_layers

禁止把 “35/35 accounted” 当成 “35/35 implemented”。

## 审计问题 C：Framework 是否 Self-contained

检查发布的 `banyan-framework/` 是否自身携带或能够稳定定位：
- Capability Contract Registry
- Artifact Registry / Schema
- Source Role Registry
- Workflow contracts
- State definitions
- Role definitions
- Skill catalog / provider skill references
- Provider Port schemas
- Project Overlay schema
- Compatibility mapping
- Version/status/provenance rules

如果真实运行/文档只能依赖 `榕树ai改造落地相关文档/` 才知道这些定义，标记：
`FRAMEWORK_RELEASE_NOT_SELF_CONTAINED`.

注意：不要因此直接复制施工文档进 Core；先报告。

## 审计问题 D：后续设计但未 Runtime 化的能力

分别检查，并明确“这是遗漏”还是“Stage 本来就只负责 Contract Design”：
- SQLite Index / Query runtime
- Context selection / recovery
- Memory layers
- Freshness resolver
- Token budget / compaction
- Evidence bundle runtime
- Impact graph/runtime
- Event runtime
- Prompt learning runtime
- Project Guide publisher
- UI Design Intelligence provider execution
- Adaptive Workflow router/executor
- Natural-language orchestration
- Change / Canonical Apply executor
- Collaboration role schema
- WebUI Help Center

状态必须区分：
- ACCEPTED_DESIGN_ONLY
- INTENTIONALLY_DEFERRED
- REQUIRED_FOR_TARGET_UX
- MISSING_IMPLEMENTATION
- IMPLEMENTED

## 审计问题 E：Project Instance

检查 `.banyan/` 是否能够绑定：
- Core contracts
- Source Roles
- Workflows
- Skills / Providers
- Policies
- Profiles
- Roles
- Runtime state
- Index
- Trace
- Migration

区分 Shadow Pilot 限制与真正缺口。

## 审计问题 F：D0/D1/D2 文档一致性

检查当前 `docs/user-guide/` 是否已经被提前生成。
若 D2 尚未正式验收：
- 不删除；
- 标记 `UNACCEPTED_DOCUMENTATION_OUTPUT`;
- 不继续 D2；
- 等 Framework audit 决策后再刷新 Source of Truth。

## 输出

生成到：
`榕树ai改造落地相关文档/Documentation_Packaging/Implementation_Reconciliation_Audit/`

必须包含：
1. `BANYAN_IMPLEMENTATION_GAP_AUDIT.md`
2. `V3_1_ARTIFACT_MIGRATION_MATRIX.yaml`
3. `CAPABILITY_IMPLEMENTATION_MATRIX.yaml`
4. `FRAMEWORK_SELF_CONTAINMENT_AUDIT.md`
5. `DEFERRED_VS_MISSING_IMPLEMENTATION.md`
6. `REMEDIATION_PRIORITY_PROPOSAL.md`
7. `D1_5_ACCEPTANCE_REPORT.md`

## Priority

建议分级但不要自动施工：
- P0：会造成 Legacy 能力丢失 / Framework 无法自解释 / Release 依赖施工目录
- P1：阻断目标主体验（自然语言→Workflow→决策→施工→验证）
- P2：重要治理/runtime增强
- P3：UX / 文档增强
- P4：可选优化

## 禁止

- 不修改 `banyan-framework/**`
- 不修改 `.banyan/**`
- 不修改 `docs/project/**`
- 不修改 Git
- 不创建/删除 Role/Skill/Workflow 文件来“修复”
- 不解决 Gap
- 不进入 D2/D3
- 不做 Final Activation

完成后停止。

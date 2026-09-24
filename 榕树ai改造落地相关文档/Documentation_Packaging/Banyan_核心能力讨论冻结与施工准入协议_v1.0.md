# Banyan 核心能力讨论、冻结与施工准入协议 v1.0

> 状态：DISCUSSION_PROTOCOL_PROPOSED  
> 用途：约束 Banyan 后续所有重要架构、语义、存储、Runtime、治理与迁移工作，防止讨论跳跃、遗忘旧规则、未确认即施工。  
> 核心原则：**先盘点旧规则与当前事实 → 再讨论 → 用户确认 → 冻结产物 → 才允许施工。**

---

## 1. 永久原则

1. 不依赖聊天记忆直接设计。每个重要主题讨论前，必须重新对账既有冻结文档、已接受聊天要求、Legacy v3.1、Refactor、当前 Framework。
2. 旧规则不得静默丢失、覆盖、改名或等价替换。
3. 新方案与旧规则冲突时，必须显式列出冲突、影响、迁移方案，并等待 Human Decision。
4. 讨论中的想法不自动成为正式要求。
5. 未经用户明确确认，不得把 Proposal 升级为 Frozen Contract。
6. 未达到施工准入条件，不得生成 Cursor Implementation Prompt。
7. 重要模块必须独立讨论，禁止跨模块边讨论边施工。
8. ENGINEERING_COMPLETENESS > TOKEN_SAVING。
9. TOKEN_EFFICIENCY_MUST_NOT_REDUCE_GOVERNANCE_FIDELITY。
10. Authority、Registry、Runtime、Project Instance、Legacy、Artifact、SQLite 的边界必须显式，不得形成双真源。

---

## 2. 每个主题讨论前的强制“四源对账”

每次开始一个核心主题，我必须先完成以下四源盘点：

### SOURCE-A：历史沟通
分类为：
- `HUMAN_CONFIRMED`
- `ACCEPTED_REQUIREMENT`
- `DISCUSSION_ONLY`
- `REJECTED`
- `UNKNOWN`

只有 `HUMAN_CONFIRMED` / `ACCEPTED_REQUIREMENT` 可直接作为目标约束。
`DISCUSSION_ONLY` / `UNKNOWN` 必须重新交给用户决定。

### SOURCE-B：Legacy v3.1
识别：
- 原有能力
- 原有角色/流程/状态/文档治理
- 决策、PRD、UI、开发、测试、发布、交接等高价值语义
- 兼容/迁移要求

### SOURCE-C：Accepted Refactor / Stage Evidence
识别：
- 已冻结 Contract
- 已接受边界
- 已接受 Capability / Provider / Project Instance / Runtime / Context / Evidence 等设计
- 不能被静默推翻的历史决策

### SOURCE-D：Current Framework Reality
核实：
- 真实代码
- 真实 Artifact
- Registry / Loader / Runtime / CLI / WebUI
- `.banyan`
- 当前实现状态、测试状态、实际目录与实际依赖

---

## 3. 每个主题进入讨论前，我必须先给用户一张“讨论底稿”

固定结构：

1. `已经冻结，不能随便改`
2. `已经确认，但尚未实现`
3. `当前 Framework 已实现`
4. `Legacy / Refactor 仍需保留`
5. `存在冲突`
6. `存在缺口`
7. `本轮真正需要用户决定的事项`
8. `明确不在本轮决定的事项`

只有这张底稿完成后，才开始讨论目标方案。

---

## 4. 讨论状态机

每个核心主题统一走：

`INVENTORY`
→ `RECONCILED`
→ `PROPOSAL`
→ `HUMAN_REVIEW`
→ `HUMAN_APPROVED`
→ `FROZEN_FOR_IMPLEMENTATION`
→ `IMPLEMENTATION`
→ `VALIDATED`
→ `ACCEPTED`

禁止跳过 `HUMAN_APPROVED`。

---

## 5. Human Decision 规则

需要用户明确确认的事项至少包括：

- 核心对象定义
- Artifact 分类
- Role / Capability / Skill / Workflow 模型
- PRD 生成与治理
- UI_SPEC / Design Truth / AnyDesign / Visual Repair
- SQLite / Markdown 存储边界
- Authority / Registry / Runtime 边界
- Provider / MCP / Adapter
- Permission / Git / Semantic Commit
- Project init / adopt / migrate / reconcile
- Change / Draft / Canonical Apply
- Context / Memory / Evidence / Index
- WebUI / Control Plane
- 目录结构改变
- Schema/数据库迁移
- Canonical Source 改变
- Legacy Retirement / 删除
- 任何高影响等价替换

---

## 6. 每个核心主题讨论完成后的冻结产物

每个主题固定生成一个“小型 Freeze Pack”，避免文档爆炸：

```text
<topic>/
├── 01_RECONCILIATION.md
├── 02_TARGET_DESIGN.md
├── 03_HUMAN_DECISIONS.yaml
├── 04_FROZEN_CONTRACT.yaml
├── 05_IMPLEMENTATION_BOUNDARY.md
└── 06_ACCEPTANCE_GATES.yaml
```

### 文件职责

- `01_RECONCILIATION.md`
  - 四源盘点结果
  - 保留项、冲突、缺口、来源

- `02_TARGET_DESIGN.md`
  - 用户已理解并讨论过的目标设计
  - 运行方式、关系、边界、示例

- `03_HUMAN_DECISIONS.yaml`
  - 用户明确批准/否决的决策
  - 未决定事项保持 OPEN

- `04_FROZEN_CONTRACT.yaml`
  - 给 Runtime / Registry / Schema / Cursor 消费的机器可读合同
  - 不写施工细节以外的猜测

- `05_IMPLEMENTATION_BOUNDARY.md`
  - 本阶段允许改什么
  - 禁止改什么
  - 不能提前进入哪些未来能力

- `06_ACCEPTANCE_GATES.yaml`
  - 必须通过的测试、无损、Authority、回归、迁移与 Plan Conformance 条件

只有六份产物完整并且 `HUMAN_APPROVED=true`，才允许进入施工。

---

## 7. 施工准入判定

### READY_FOR_IMPLEMENTATION

必须同时满足：

- 四源对账完成
- 冲突已解决或明确 DEFERRED 且不阻塞
- Human Decisions 全部记录
- Target Design 已确认
- Frozen Contract 已生成
- Authority / Source of Truth 已明确
- 数据迁移与回滚边界已明确
- Acceptance Gates 已明确
- 不存在未解决的高影响 `UNKNOWN`
- `PLAN_CONFORMANCE_CHECK` 目标已定义

### NOT_READY_FOR_IMPLEMENTATION

出现任意一项即禁止施工：

- 仍在讨论核心模型
- 旧规则尚未核对
- Chat Requirement 状态不明
- 新方案会覆盖旧语义但未确认
- Schema/目录/Authority 仍有多个候选
- SQLite 真源边界未定
- PRD/UI_SPEC Canonical 边界未定
- 角色/技能/能力/Workflow 关系未定
- 高影响迁移/删除未确认

---

## 8. Banyan 后续固定讨论顺序

### Foundation Gate F0 — 已完成结果保护
- R0 / R1 / RP1
- 当前 CURRENT / Final Activation
- Protected areas
- 不重新设计已验收内容，除非新 Human Decision 明确授权

### F1 — Core Object Model
讨论：
- 一等核心对象是什么
- 什么才叫 Artifact
- Definition Artifact / Project Artifact
- Runtime Object / Binding / Infrastructure 的边界

完成后产出：
`F1_Core_Object_Model_Freeze_Pack`

### F2 — Storage & Truth Model
讨论：
- Markdown / YAML / SQLite 各自负责什么
- 哪些是 Canonical Truth
- 哪些是 Structured Truth
- 哪些是 Derived/Rebuildable Index
- 一个 DB 还是多个 DB
- Stable ID / Version / Status / Relation / History
- Migration / Backup / Rebuild

完成后产出：
`F2_Storage_Truth_Model_Freeze_Pack`

> F2 先冻结逻辑模型；物理 DDL/索引/迁移 SQL 在真正进入数据库实现前再做 Implementation Freeze。

### F3 — Definition Artifact Taxonomy
讨论：
- RoleDefinition
- CapabilityDefinition
- SkillDefinition
- WorkflowDefinition
- PolicyDefinition
- StateModelDefinition
- DecisionProtocolDefinition
- TemplateDefinition
- ProviderContractDefinition
- CompatibilitySpecDefinition
- Context Recovery 是否仍为顶级 Artifact Type

完成后产出：
`F3_Definition_Artifact_Taxonomy_Freeze_Pack`

### F4 — Role / Capability / Skill / Workflow
讨论：
- Role Taxonomy
- Capability 定义
- Skill 定义
- Workflow Node
- Role→Capability
- Skill→Capability
- Workflow→Role+Capability
- Resolver / Handoff / Validation
- 与 Permission / Provider 的边界

完成后产出：
`F4_Orchestration_Semantic_Freeze_Pack`

### F5 — PRD Generation & Governance
讨论：
- PRD 输入来源
- Requirement/Conflict/Decision
- Draft / Review / Approved / Baselined
- CR / Change
- Canonical Source
- AI 可修改边界
- 人工决策门禁
- Trace / Test / UI linkage

完成后产出：
`F5_PRD_Governance_Freeze_Pack`

### F6 — UI_SPEC / Design Truth / Visual Governance
讨论：
- Design Source
- Raw Scene
- Normalized Scene
- Semantic Tree
- Design Truth
- UI_SPEC
- Implementation Guidance / Pack
- AnyDesign
- Visual Validation
- Visual Repair Loop
- PRD ↔ UI_SPEC 边界
- 视觉变更与代码同步

完成后产出：
`F6_UI_Design_Governance_Freeze_Pack`

### F7 — Change / Decision / Canonical Apply
讨论：
- Change Workspace
- Draft
- Human Decision
- Reconcile
- Canonical Apply
- Rollback
- Reference Integrity

完成后产出：
`F7_Change_Canonical_Apply_Freeze_Pack`

### F8 — Project Instance / Bootstrap / Reconcile
讨论：
- `.banyan`
- init / adopt / migrate / reconcile
- Binding
- Provider Selection
- Overlay
- Existing Project Upgrade

完成后产出：
`F8_Project_Instance_Freeze_Pack`

### F9 — Context / Index / Memory / Evidence
讨论：
- Context Builder
- SQLite Index
- Memory
- Freshness
- Evidence
- Trace
- Impact
- Rebuild
- Query

完成后产出：
`F9_Context_Index_Evidence_Freeze_Pack`

### F10 — Runtime / Provider / Permission / Adapter
讨论：
- Provider
- MCP
- Runtime API
- Permission
- Git / Semantic Commit
- Adapter
- Execution / Retry / Pause / Resume

完成后产出：
`F10_Runtime_Execution_Freeze_Pack`

### F11 — WebUI / Help / Control Plane
讨论：
- Guided Setup
- Runtime API single source
- WebUI pages
- Help Center
- Migration Center
- Workflow Visualization

完成后产出：
`F11_WebUI_Control_Plane_Freeze_Pack`

### F12 — Legacy Reconciliation / Retirement
讨论：
- v3.1 compatibility
- Reference Project reconcile
- Zero runtime dependency
- Archive / retire / optional delete

完成后产出：
`F12_Legacy_Retirement_Freeze_Pack`

---

## 9. 两级冻结，避免过早设计

每个重要能力使用两级冻结：

### Architecture Freeze
先确定：
- 对象
- 职责
- Authority
- Source of Truth
- 关系
- 生命周期
- 外部接口
- 不变量

### Implementation Freeze
临近实际施工再确定：
- 精确目录
- 精确 Schema
- SQLite DDL
- API
- 字段
- 索引
- migration
- CLI
- tests

这样既不会忘旧规则，也不会过早把未来实现写死。

---

## 10. Cursor 施工规则

Cursor 只能拿到已经冻结的施工输入。

施工 Prompt 必须引用：
- 对应 Freeze Pack
- 当前唯一修复基线
- 上一阶段 Acceptance/Handoff
- 允许修改范围
- 黑名单
- Human Decisions
- Acceptance Gates

Cursor 不得：
- 重新设计冻结内容
- 自动补 Human Decision
- 因“更合理”而做等价替换
- 提前进入下一主题
- 删除 Legacy
- 改 Authority
- 改 `.banyan`
- 改目录/Schema 而未授权

---

## 11. 当前状态

当前阶段应保持：

- RP1：已完成并通过
- RP2 Implementation：暂不进入
- 当前优先：F1 → F2 → F3 → F4
- PRD 与 UI_SPEC：列为高优先核心讨论，分别在 F5 / F6 独立 Human Gate
- SQLite：在 F2 先冻结逻辑存储与真源边界，在 F9/实施前再冻结物理表结构与迁移
- 未讨论完成前，不生成 RP2 施工 Prompt

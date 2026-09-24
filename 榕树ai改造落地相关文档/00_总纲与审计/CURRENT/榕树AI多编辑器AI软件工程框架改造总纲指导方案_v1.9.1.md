# 榕树 AI 多编辑器 AI 软件工程框架改造总纲指导方案 v1.9.1

> 文档定位：本文件是后续全部 Banyan AI Engineering Framework 改造阶段的总纲、路线图、保护边界和闭环验收依据。  
> 当前阶段：总纲设计，不直接修改业务代码，不直接迁移正式项目数据。  
> 使用方式：后续严格按 00～20 逐阶段生成一套 **Stage Delivery Pack**；每次只生成、审查并实施当前阶段，完成 Gate 后再进入下一阶段。  
> 核心目标：打造一套**不挑编辑器、适配新项目和开发中项目、盘点快、省 Token、有持续记忆、可追踪、可验证、可迁移、可回滚**的 AI 软件制作工程。  
> 推荐框架名：**Banyan AI Engineering Framework（榕树 AI 软件工程框架）**。  
> 推荐 AI 根目录：**`.banyan/`**。  
> v1.9.1 定位：**逐阶段施工最终冻结版（Freeze Consistency Audit 修正版）**。在 v1.8 的 Stage 00～20 闭环基线上，正式冻结 Git Identity 贡献身份、可选 Contributor Profile、跨编辑器统一 Semantic Commit、Commit Provenance 与 AI 分批提交模型，并完成最后一轮阶段依赖、Handoff、Owner、文档清单与发布闭环审计。  
> 重要约束：本方案优先服从《AI 提示词改造 · 当前项目状态与 AI 使用统计说明》。

---

## v1.9.1 最终施工前冻结审计结论

v1.9.1 是开始连续生成 Stage Delivery Pack 前的最终 Freeze Consistency Audit 修正版。此次不改变 00～20 主顺序，而是修补一个此前没有完整建模的横切问题：**多人、多编辑器、Git 提交身份、AI 分批提交和 Commit Provenance**；同时再次检查阶段 Handoff、Single Owner、文档物资和 Final Release 闭环。


本次 Freeze Consistency Audit 不扩展新的功能范围，只修正以下一致性问题：

1. **Bootstrap Trace/Register 路径与最终 `.banyan/migrations` 路径的时序冲突**：Stage 00～Stage 02/04 目录冻结前允许使用 `REFRACTOR_CONTROL_ROOT` 下的 Bootstrap Register/Trace；正式 Project Instance 路径冻结后再迁入 `.banyan/migrations/`，且必须保留 lineage/hash，不允许形成两个并行真源。
2. **Semantic Commit Policy Owner 模糊**：Stage 05 正式成为 Semantic Commit Workflow + Commit Message Policy 的唯一 Owner；Stage 03 只定义 Schema，Stage 14 只定义 Safety Gate，Stage 15 只实现 CLI/API/Execution，不再重新定义 Policy。
3. **Commit 能力生命周期不够显式**：Stage 05 只推进到 `DEFINED`；Stage 14/15 才允许进入 `IMPLEMENTED / INTEGRATED`；Stage 17/18 Pilot 验证跨编辑器一致性；Stage 19 `VERIFIED`；Stage 20 `RELEASED`。
4. **Git Identity 缺失时的行为补齐**：AI 不得自行发明、修改或临时覆盖 Git Identity；当前环境无法解析有效 Git Author Identity 时，Commit Workflow 必须 `BLOCK / NEEDS_INPUT`。
5. **Dependency Matrix 用词统一**：Stage 顺序 Gate 仍然必须逐阶段 PASS；矩阵中的 `DEFINED / Schema 稳定 / Pilot 经验` 仅表示语义能力前置，不得被解释为可跳过上一 Stage Acceptance。

本次冻结结论：

1. **Git Identity 是 Banyan 默认且唯一的贡献身份标识**：以 Git Commit 的 `author.name + author.email` 作为项目内贡献身份事实；Banyan 不追踪、不推断真实物理操作者。
2. **使用别人电脑就使用该环境实际 Git Identity**：Banyan 不提示切换身份、不修改 Git `user.name/user.email`、不使用 `--author` 或其它方式替用户改身份；最终 Commit Object 中的 Author/Committer 是 Git Evidence。
3. **Contributor Profile 只是可选显示增强**：可以给某个 Git Identity 填 `display_name / status / note`；未填写时直接显示 Git `name + email`。Profile 不包含 `role_labels`、模块归属、前后端标签，也不参与权限判断。
4. **不同 Git Identity 默认就是不同贡献身份**：v1 不自动猜测两个邮箱是否属于同一个真人，不做隐式 Alias/Merge；需要精确归属时应从源头使用正确且稳定的 Git Identity。
5. **编辑器没有业务职责**：Cursor / Codex / Claude / Generic 只作为 `Execution Client` 记录。任务、模块、Change、Batch、Workflow 才描述“这次在做什么”。
6. **Banyan 的 `Role` 与人员职位彻底分离**：Role 继续表示 AI/Workflow/Reader 语义角色，不表示前端、后端、商品负责人等人员岗位；Contributor Profile 不建立固定 Role。
7. **统一 Semantic Commit Policy**：Cursor、Codex、Claude 不能各自定义 Git 提交规范；Banyan 维护一套中立 Commit Policy，各 Adapter 只负责调用。
8. **正式纳入 AI 分批提交能力**：用户可以直接要求“帮我把当前修改合理分批提交”；AI 必须读取真实 Working Tree / Diff，按语义变化而不是目录机械分组，保留无关、未完成、Local-only 修改，并逐批验证。
9. **AI 提交绝不修改 Git 身份**：提交前可读取 Git 当前解析身份，提交后以真实 Commit Object 为最终事实；Git Author 本身已经表示贡献身份，不再重复写 `Banyan-Actor`。
10. **Commit Message 与 Provenance 分层**：提交标题/正文遵循统一 Commit Contract；Workflow / Change / Batch / Task / Client 等 Git 原生不知道的上下文由 Banyan Trace/Evidence 管理，并可使用最小机器可读 Trailer 保持跨环境可重建性。
11. **Git 是文件修改历史真源，Banyan Trace 是语义关联层**：SQLite/Control Plane 不复制一套可独立修改的 Git 历史；删掉 Index 后必须能从 Git + Canonical Artifacts + 可持久化 Trace 重建。
12. **No-Loss 与身份/提交模型接轨**：Stage 01 会盘点现有 Git Identity、Commit Message 习惯、已有 AI Commit Rule/Script；Stage 02～16 各自承担唯一职责，Stage 17/18 验证跨编辑器一致，Stage 19 做最终 E2E。
13. **Handoff 再次加强**：每个实际 `ACCEPTANCE_REPORT.md` 必须包含 `NEXT_STAGE_HANDOFF`，明确下阶段可消费的真实 Artifact、Evidence、Open Risk、Rollback Point 和 Entry Gate，不再依赖“上一阶段自己去猜”。
14. **Stage Pack 版本兼容规则补齐**：已经生成的 Stage Pack 如果上位总纲升级但其 Owner Contract 未被改变，可以显式标记兼容而无需机械重做。当前已生成的 **Stage 00 v1.8 Pack 与 v1.9.1 兼容，不需要重新生成**；v1.9 新增能力从 Stage 01 开始进入施工链。
15. **修正 Stage 16 子文档清单遗漏**：Section 18 与 Section 25 重新对齐，Migration Center、Parallel Draft、No-Loss Migration UI 与新增 Contributor/Commit Provenance UI 均进入正式清单。
16. **修正“每阶段一个 Commit”的潜在误读**：阶段边界不得混提，但一个阶段可以有多个语义清晰的 Commit；Stage 00 只做安全基线/Checkpoint，不自动 Commit。
17. **最终阶段顺序不变**：Stage 19 仍只产出 `VERIFIED / RELEASE_CANDIDATE`；Stage 20 在真实实现基础上生成使用说明并通过 Documentation Drift Gate 后才 `FINAL_RELEASE`。
18. **本轮未发现需要新增 Stage 的问题**：Git Identity / Semantic Commit 属于横切能力，分别落到现有 Owner Stage，避免再制造重复架构层。

从 v1.9.1 起，00～20 的 Stage 顺序、Owner 边界、第 25 节文件名清单、Stage Handoff 与 Git Identity / Commit Governance 共同构成后续逐阶段生成文档的正式冻结基线。真实仓库发现的新事实仍必须通过 `REFRACTOR_PLAN_CHANGE` 受控回补，不能在后续 Stage 私自重新定义上游 Contract。


# 0. 本次改造最终要解决什么

当前体系已经不是“缺规则”，而是规则、文档和 AI 协作资产已经非常多。

当前真实问题更接近：

1. 两份 v3.1 主文件体积过大，新窗口反复完整加载，Token 成本高。
2. Role、Policy、Skill、Workflow、State、Template、Project Fact 混在“大型提示词”里。
3. `.cursor/` 当前承担规则入口，未来会造成编辑器绑定。
4. Skill、规则、项目事实、运行时上下文之间缺少统一注册和发现机制。
5. `docs/project` 已经积累大量正式工程知识，不能推倒重来。
6. TRACE、DEC、ADR、CR、Batch、Test、UI 等关联关系越来越多，仅靠全文扫描越来越慢。
7. AI 新窗口需要快速恢复状态，但不能另造一套与正式项目状态冲突的“AI_CONTEXT 真源”。
8. AI 开发经验、失败经验和高价值 Prompt 还没有形成系统的学习闭环。
9. 编辑器规则以后需要“一处维护，多端释放”，不能 Cursor、Codex、Claude 各维护一套。
10. UI 设计图驱动开发已经形成多份协议，需要合并职责，避免重复加载。
11. 改造期间必须保证现有项目继续可开发，不能因为治理升级破坏代码、已有文档和当前 Batch。
12. 所有新增 AI 文件必须让人和 AI 都能看懂：它是什么、何时用、谁生成、能改什么、不能改什么、如何验证和回滚。

因此本次改造不是“优化 Prompt”，而是：

> **把已经验证过的 Prompt Governance，升级成可执行、可索引、可迁移、可跨编辑器运行的 Framework Governance。**

---


# 0A. Banyan 通用性最高约束

Banyan 的目标不是为首个 Reference Project 定制一套更复杂的项目规范，而是形成可以接入不同语言、不同技术栈、不同目录、不同需求治理方式、不同编辑器的通用 AI 软件工程框架。

硬约束：

```text
Banyan Core
≠
任何具体项目的业务知识
```

Core 中禁止硬编码：

- 项目名称；
- 业务模块名称；
- 某个端/页面/角色名称；
- 项目专属 PRD / REQ / DEC 编号；
- 项目专属 API / 端口 / 域名；
- 项目专属目录结构；
- 某个业务状态机；
- 某个项目的产品规则；
- 某个项目特有的进度文件路径。

首个真实项目只允许作为：

```text
Reference Project
Migration Fixture
Compatibility Fixture
Acceptance Fixture
Experience Source
```

项目经验只有在被抽象、去业务化、验证可跨项目复用后，才允许晋升为 Banyan Core 能力。

---


# 0B. Codex 是本次改造施工执行器，不等于 Banyan Codex Adapter

后续生成的 Stage Delivery Pack 的主要使用方式是：

```text
Stage Document
↓
Codex 读取真实 Repository
↓
PRECHECK
↓
按允许范围施工
↓
Validation / Evidence
↓
Acceptance / Handoff
```

这里的 Codex 身份是：

```text
TRANSFORMATION_EXECUTOR
```

它可以在 Banyan 尚未建成时就读取仓库并按阶段文档执行改造。

而 Stage 18 要建设的：

```text
Banyan Codex Adapter
```

是 Banyan 完成后，未来项目日常使用 Codex 时的 Runtime Adapter。

两者必须严格区分：

```text
Codex 施工执行器
≠
Banyan Codex Runtime Adapter
```

因此不存在循环依赖：

```text
必须先有 Codex Adapter
→ 才能用 Codex 改 Banyan
```

这是错误理解。

Stage 00～14 尚未有完整 Banyan Governance Runtime 时，Codex 写入必须继续服从：

```text
Legacy Safety Gate
Stage Runbook Allowlist
Protected Paths
Checkpoint / Rollback
```

Stage 14 以后再逐步切换到 Banyan Governance Check。

---

# 1. 首个 Reference Project 迁移基线：本次改造必须保护的东西

## 1.1 当前 Reference Project 不是实验空仓库

当前项目已经进入真实开发阶段，并已经形成大量治理资产。

后续任何改造都必须假定：

- `docs/project/` 是正在使用的正式项目知识体系；
- 已有 PRD、DEC、ADR、CR、UI-DEC、Batch、Worklog 等不能随意改号、改主题或重写历史；
- G0～G11 已经真实执行过；
- 当前代码已经按开发批次发生实际改动；
- G9.5、AnyDesign、UI_SPEC、视觉修复循环已经有真实实践；
- `.cursor/rules/` 已经承担现有安全闸口；
- 当前系统不是“重新初始化”，而是“带历史、带状态、带开发中的项目迁移”。

## 1.2 本次改造的保护区

在没有进入专门迁移阶段前，默认禁止修改：

```text
nunu-go-api/**
go-uni-app/**
go-uni-app-online/**
go-uni-app-tob/**
deploy/sql/**
真实业务配置
已批准或已基线的 PRD / DEC / ADR / CR 正文
```

框架施工阶段如果需要验证代码，只允许：

```text
READ_ONLY
```

只有进入明确的项目开发 Batch，并满足现有代码写入门禁时，才能恢复正常业务代码修改能力。

## 1.3 `docs/project/` 不作为框架迁移试验田

原则：

> **项目真源优先保持原位，框架围绕它建立索引、Context、Trace、Evidence 和 Adapter。**

初期不大规模搬迁 `docs/project/`。

需要改变目录时，必须执行：

```text
盘点
→ 映射
→ 复制/生成新结构
→ 校验
→ 双轨读取
→ 切换
→ 回滚验证
→ 最后才考虑旧入口退役
```

禁止“先移动再修引用”。

---

# 2. 本批方案文档的归并结论

这批文件中有多组功能相似方案。总纲采用“一个规范核心 + 一个详细参考 + 一个专项职责”的方式归并，而不是把全部文件直接拼接。

---

## 2.1 软件工程总体框架

### 主干采用

《榕树 AI 软件工程框架改造初始方案》

保留其核心架构：

```text
Role
Policy
Skill
Workflow
State
Context
Evidence
Trace
Adapter
Project Instance
```

同时保留：

- Banyan Core 与 Project Instance 分离；
- `docs/project` 不被 Banyan 替代；
- 编辑器采用 Adapter；
- Markdown/YAML 与 SQLite 混合；
- 高风险决策继续由人确认；
- Evidence + Trace 形成完成证据链。

### 吸收《优化策略.md》

重点吸收：

- LIGHT / STANDARD / FULL 项目治理模式；
- 动态 Context，不建立新的长期 `AI_CONTEXT` 真源；
- Prompt Learning Loop；
- AI 工作模式；
- 机器可执行权限；
- Decision Necessity / Context / Dependency；
- SQLite 索引；
- Impact Analysis；
- 代码反向追踪；
- Governance Check；
- 专项 Profile；
- Token 优化。

### 对初始方案做一项重要升级

初始方案倾向“只逐步迁移高价值历史数据”。

本次总纲调整为：

> **不要求把历史 Markdown 改写成数据库，但要求 SQLite 索引层可以完整扫描并索引所有可识别的正式历史资产。**

也就是说：

```text
历史正文不强迁
但历史关系尽量全索引
```

这样既不破坏历史，又能实现快速查询。

---

# 3. UI 相关方案的最优归并

UI 相关文件不再并列执行，而是形成一条编译链。

## 3.1 总协议核心

采用：

**《榕树AI UI设计图驱动开发协议 v1.1》**

作为短而硬的核心协议。

原因：

- 编译链完整；
- 明确 Raw Scene / Normalized Scene / Semantic / Design Truth / Behavior / Data / Implementation；
- 明确 `Rendered Geometry ≠ CSS Fixed Size`；
- Framework-neutral；
- 有完整验收闭环。

## 3.2 详细解释和案例库

保留：

**《榕树AI UI设计图驱动开发协议 v1.0》**

但不再作为每次 AI 开发必须整份加载的主规则。

定位改为：

```text
extended-reference
```

主要提供：

- 状态枚举；
- Interaction 说明；
- Data / Fixture；
- Upload / Modal / Drag 专项；
- Visual Regression；
- 示例和详细解释。

## 3.3 UI 数据结构和目录真源

采用：

**《榕树AI UI Design Pack 数据结构与目录规范 v1.0》**

作为 UI Design Pack 的目录与职责契约：

```text
00-source
01-scene
02-semantic
03-design
04-behavior
05-data
06-implementation
07-framework
08-validation
```

特别保留：

```text
Scene = 设计事实
Implementation = 实现施工建议
Framework = 技术栈翻译
Validation = 验收
```

## 3.4 Implementation 编译规则

核心采用：

**《榕树AI Implementation 产物生成规则 v1.1》**

详细参考保留：

**《榕树AI Implementation 产物生成规则 v1.0》**

其中 v1.1 作为硬规则，重点固化：

- FACT / INFERENCE / RECOMMENDATION 分离；
- Geometry 不自动变 fixed；
- fixed / fill / intrinsic / fraction / minmax 等 Sizing；
- Parent-driven Sizing；
- Flex / Grid 判断；
- responsive transformation；
- Behavior / Data 通过引用使用；
- Framework-neutral IR。

v1.0 则作为：

```text
schema-reference
example-library
extended-generation-rules
```

## 3.5 前端布局实现规则

核心采用：

**《榕树AI前端 UI 布局开发指导 v1.1》**

详细手册保留：

**《榕树AI前端 UI 布局开发指导 v1.0》**

最终规则：

> **布局实现关系，不抄截图坐标。**

## 3.6 视觉验收与修复

采用：

**《榕树AI前端设计图驱动开发与视觉一致性治理方案 v2》**

但只抽取它最擅长的职责：

- 复杂视觉效果显式建模；
- 页面/组件修改范围控制；
- Visual Diff；
- 一轮只修可验证问题；
- 视觉组件沉淀；
- Screenshot Regression；
- 视觉修复循环。

它不再重复定义 Design Scene、Implementation IR、Sizing 等已经由前面几份规范负责的概念。

## 3.7 最终 UI 子系统

最终形成：

```text
Design Source
    ↓
Scene
    ↓
Semantic
    ↓
Design Truth
    ↓
Behavior + Data
    ↓
Frontend Layout Guidance
    ↓
Implementation IR
    ↓
Framework Adapter
    ↓
React / Vue / Other
    ↓
Visual + Interaction Validation
    ↓
Repair Loop
```

这一条链以后作为 Banyan 的：

```text
UI Design Intelligence Profile / Skills
```

按需加载，不进入所有任务的默认 Context。

---


## 3.8 PRD × UI_SPEC 页面开发协同模型

后续页面开发禁止让 Coding Agent 临时把 PRD、设计图、UI_SPEC 混在一起自行判断优先级。

固定职责：

```text
PRD
= WHAT / WHY
= 功能、角色、权限、业务流程、状态、数据语义、异常、验收

UI_SPEC
= HOW IT LOOKS / HOW IT FEELS
= 布局、视觉、组件、视觉状态、交互表现、响应式表现

Design Source / UI Design Pack
= UI_SPEC 的证据源与结构化设计输入

Technical/API/Data Contract
= HOW IT WORKS TECHNICALLY

Implementation Pack
= HOW TO IMPLEMENT THE UI RELATIONSHIP

Effective UI Contract
= 当前 Batch 真正生效的 UI 规则快照
```

页面真正进入编码时，目标输入应收敛成：

```text
Business Contract
+
Effective UI Contract
+
Implementation Pack
+
Engineering Constraints
↓
PAGE_IMPLEMENTATION_CONTEXT
↓
Coding Agent
```

### 3.8.1 冲突优先级

涉及业务目标、角色、权限、金额、状态、字段业务含义、业务流程：

```text
Approved/Baselined PRD
优先于
UI_SPEC / Design Source
```

涉及纯视觉：

```text
Approved/Baselined UI_SPEC
优先于
未批准 Design Source / 旧页面实现
```

### 3.8.2 一个根决策只确认一次

若一个决定同时影响：

```text
PRD
UI_SPEC
API
Architecture
Batch
Test
```

不得按“修改了几份文件”重复询问用户。

应该：

```text
Root Decision
↓
一次决策路由
↓
用户完成该决策所需的确认
↓
Canonical Apply
↓
分别传播到各正式真源
```

文档同步属于系统责任，不属于新的用户决策。

### 3.8.3 Batch 必须锁定版本

正在开发的 Batch 不得自动追随“latest”。

每个前端 Batch 至少锁定：

```yaml
batch:
prd_version:
effective_ui_contract:
design_revisions:
implementation_pack:
technical_baseline:
```

新 UI_SPEC 或新设计图出现时，默认只产生：

```text
NEWER_UI_AVAILABLE
```

是否让正在开发的 Batch 升级，必须先进行 Impact Analysis；存在明显返工、验收基准变化或业务变化时按相应决策档位处理。

---

## 3.9 Design Source Revision × UI_SPEC Version 双版本轴

设计图版本与 UI_SPEC 版本必须分离。

禁止：

```text
Design v5
=
UI_SPEC v5
```

正确模型：

```text
Design Revision:
D1 → D2 → D3 → D4

UI_SPEC:
1.0.0 → 1.1.0 → 1.1.1 → 2.0.0
```

设计图变化不一定导致 UI_SPEC 升级。

### 3.9.1 Design Revision

原始设计源不得静默覆盖。

至少记录：

```yaml
source_id:
revision:
checksum:
source_file:
created_at:
supersedes:
change_summary:
```

### 3.9.2 UI_SPEC 版本语义

采用 UI Governance SemVer：

```text
MAJOR
页面主结构、信息架构、继承关系或核心交互发生破坏性变化

MINOR
新增/调整状态、布局规则、响应式、组件行为，整体仍兼容

PATCH
Token、图标、小范围间距、规范错误等非结构性修订
```

版本升级必须先根据：

```text
Source Diff
→ Semantic Diff
→ Behavior Diff
→ Layout Diff
→ Token Diff
→ Asset Diff
```

判定：

```text
NO_SPEC_CHANGE
PATCH
MINOR
MAJOR
```

### 3.9.3 设计图更新分类

```text
New Design Revision
↓
Design Change Classification
├── SOURCE_ONLY
│   └── UI_SPEC 不升级
├── PURE_UI_CHANGE
│   └── UI-DEC（需要选择时）→ UI_SPEC 新 Draft
└── BUSINESS_AFFECTING_CHANGE
    └── UI-CONFLICT → CR / PRD → UI Scope → UI_SPEC
```

已经完成的历史 Batch 不反向改写；需要适配新设计时创建新的变更/批次。


# 4. 推荐的最终总体架构

Banyan 分成两层：

```text
Banyan Framework Distribution
独立版本化、发布、升级
│
├── Core
├── Schemas
├── Generic Roles / Policies / Workflows
├── Generic Skills
├── Registry Model
├── Context Engine
├── Decision / Change Engine
├── Evidence / Trace Model
├── Adapter Framework
├── CLI / Runtime API
├── Control Plane Contract
└── Templates

                ↓ version pin / install / reference

Project Instance
项目自己的 Banyan 接入实例
│
├── project.yaml
├── source mappings
├── project profiles
├── project overrides
├── local index
├── runtime
├── migrations
└── adapter outputs
```

逻辑关系：

```text
Human
  ↓
Banyan Framework Distribution
  ↓
Project Instance
  ↓
Project Canonical Sources
  ↓
AI Agent / Tools / Editors
  ↓
Docs / Code / Test / Release
  ↓
Evidence / Trace
  ↓
Learning
```

Reference Project 只验证 Framework，不拥有 Framework。

---


## 4.1 Banyan Control Plane 的正式定位

Banyan Control Plane 是 Framework 的**可选客户端与观测面**，不是新的 Source of Truth。

正确关系：

```text
Project Canonical Sources
        +
Banyan Registry
        +
Project Instance
        +
SQLite Read Model
        +
Runtime State
        ↓
Banyan Query Service
        ↓
Control Plane WebUI
```

写操作：

```text
WebUI Action / Form
↓
Banyan Command
↓
Governance Check
↓
Decision Router（需要时）
↓
Canonical Writer
↓
Reindex / Refresh
↓
WebUI
```

禁止：

```text
WebUI Local State
=
Project Truth
```

WebUI Core 不得硬编码任何 Reference Project 的业务页面、业务角色、业务模块或业务变量。

---

## 4.2 Control Plane 的建议技术形态

第一版保持轻量：

```text
banyan serve
↓
Single Process
├── Local API
├── Static SPA
├── SQLite Read Model
├── File Watcher
├── Event Stream（SSE / WebSocket）
└── Command Endpoint
```

默认运行于本地回环地址，团队远程模式后续再设计。

Control Plane 不要求引入 Redis、PostgreSQL、消息队列或微服务作为第一版前置依赖。

---

# 5. 推荐目录总结构

> 本结构是总纲推荐目标。具体安装方式、包管理方式和文件名在“目标架构与目录定稿阶段”再冻结。

### 5.1 Framework Distribution（项目外或依赖形式）

```text
banyan-framework/
├── core/
│   ├── roles/
│   ├── policies/
│   ├── workflows/
│   ├── states/
│   ├── profiles/
│   ├── templates/
│   └── schemas/
├── skills/
├── registries/
├── context/
├── decision/
├── change/
├── evidence/
├── trace/
├── adapters/
├── cli/
└── VERSION
```

### 5.2 Project Instance（项目内）

```text
repo/
├── .banyan/
│   ├── project.yaml
│   ├── framework.lock
│   ├── sources.yaml
│   ├── profiles/
│   ├── overrides/
│   ├── mappings/
│   ├── registry/
│   ├── index/
│   │   └── banyan.db
│   ├── memory/
│   ├── runtime/
│   ├── trace/
│   └── migrations/
│       └── MIGRATION_REGISTER.yaml
│
├── tools/                           # 项目可选的通用/项目 Skill 实现；通过 Registry 声明归属
├── openspec/                        # 若本项目选择 OpenSpec Provider
├── docs/                            # 项目自己的正式知识体系；目录名不由 Core 强制
├── .cursor/                         # Adapter 输出
├── .codex/                          # Adapter 输出（若需要）
├── .claude/                         # Adapter 输出（若需要）
├── AGENTS.md                        # Adapter 输出（若需要）
└── project code...
```

Framework 可以通过包、Git 依赖、二进制、安装目录或其它方式分发，具体方案后续冻结。

关键原则：

```text
Project .banyan/
不复制维护一整套 Banyan Core 真源
```

项目实例只保存“本项目如何使用 Banyan”。

---

# 6. Source Role 与 Source of Truth

Banyan Core 不硬编码某个项目必须使用 `docs/project/**`。

Core 只定义语义角色：

```text
PROJECT_FACT_SOURCE
DECISION_SOURCE
CHANGE_SOURCE
ARCHITECTURE_SOURCE
UI_SOURCE
REFERENCE_SOURCE
TOOL_SOURCE
GENERATED_SOURCE
RUNTIME_SOURCE
INDEX_SOURCE
```

Project Instance 负责把真实项目映射进去。

例如某个项目可以配置：

```yaml
sources:
  project_fact:
    - docs/project/**
  reference_only:
    - docs/temp/**
  tools:
    - tools/**
```

另一个项目完全可以是：

```yaml
sources:
  project_fact:
    - specs/**
    - architecture/**
  reference_only:
    - notes/**
```

Banyan Core 的治理语义不因此改变。

## 6.1 项目正式事实

正式事实的物理位置由 Project Instance 映射。

对当前 Reference Project，可映射到其现有正式项目文档体系；但这只是该项目配置，不是 Core 规范。

## 6.2 AI 工程规则真源

Banyan Framework Distribution 是通用规则真源：

- Role；
- Policy；
- Workflow；
- State；
- Generic Profile；
- Schema；
- Adapter Model；
- Generic Memory Pattern。

Project Instance 只维护本项目：

- Source Mapping；
- Profile；
- Override；
- Project Policy；
- Project Skill Binding；
- Migration State。

## 6.3 可执行 Skill

Skill 必须区分：

```text
GENERIC_SKILL
PROJECT_SKILL
DOMAIN_SKILL
```

只有去项目化并完成跨项目验证的 Skill 才能升级为 Generic Skill。

## 6.4 编辑器目录

```text
.cursor/**
.codex/**
.claude/**
AGENTS.md
```

定位：

> Adapter 编译/释放结果，不是通用规则真源。

## 6.5 SQLite

Project Instance 内的 SQLite 仍然只是：

> 查询索引、关系缓存、Context 加速器。

必须可由项目映射源重新构建。

---

# 7. Reference Project 的特殊映射原则

## 7.1 `docs/temp`

以下规则只属于当前 Reference Project 的 Project Instance 映射，不进入 Banyan Core。

必须保留当前机制：

```text
reference_only = true
writable = false
authoritative = false
```

允许：

- 搜索；
- 人工点名读取；
- 迁移分析时引用；
- 历史对照。

禁止：

- AI 自动修改；
- 自动把内容升级为 PRD/DEC/ADR；
- 默认参与正式 Context；
- 因为内容较新就覆盖正式真源。

可在索引里记录：

```yaml
trust_level: reference_only
write_policy: deny
auto_context: false
```

## 7.2 `docs/agreements`

这是当前 Reference Project 的项目专属目录。

当前阶段：

```text
保留原目录
不强迁
不删除
```

后续只做：

- 注册；
- 标注类型；
- 确定它与 `docs/project` 的优先级；
- 如果未来迁移，必须有映射和引用检查。

## 7.3 `tools`

当前 Reference Project 将其映射为：

> **跨编辑器通用 Skill / Tool 实现仓库。**

规则：

1. Skill 可执行源码只有一份。
2. 每个 Skill 必须有说明。
3. 每个编辑器通过 Adapter、软链、包装器或原生发现机制引用同一份。
4. 禁止为了适配编辑器复制出多套不同源码。
5. Adapter 只解决加载方式差异，不改 Skill 业务语义。

---


# 7A. Project Onboarding：初始化、接入与治理迁移必须分开

Banyan 不能把所有项目都当成“新项目初始化”。

统一分成三类顶级入口：

```text
Initialize New Project
新项目，从零建立 Project Instance

Adopt Existing Project
已有项目接入 Banyan，但没有需要迁移的旧 AI 治理体系

Migrate Existing Governance
已有项目 + 已有 AI 文档/Rules/Skills/变量/治理体系
```

其中 `Adopt Existing Project` 可以进一步包含：

```text
EXISTING_CONTINUE
保留当前项目事实，继续迭代

EXISTING_REBASE
保留代码和历史，重新建立可靠 Current Baseline

AUDIT_ONLY
只扫描，不接管、不写项目
```

## 7A.1 Project Instance Bootstrap ≠ Project Initialization

已有项目迁入 Banyan 时，仍需要创建项目接入壳：

```text
.banyan/project.yaml
.banyan/framework.lock
.banyan/sources.yaml
.banyan/profiles/
.banyan/mappings/
.banyan/index/
.banyan/runtime/
.banyan/migrations/
```

这叫：

```text
Project Instance Bootstrap
```

它不等于：

```text
重新定义项目目标
重新生成 PRD
重新跑 G0
重新确认全部变量
重写业务历史
```

## 7A.2 现有治理体系迁移

如果项目已经存在：

```text
AI Prompt
Rules
Skills
Project Variables
Progress
Decision
PRD
UI Governance
Legacy Dashboard
```

应该：

```text
Legacy Governance
→ Inventory
→ Parse
→ Classify
→ Mapping
→ Transform / Reuse
→ Compatibility Check
→ Shadow
→ Cutover
```

而不是从零生成第二套。

## 7A.3 迁移工具是一次性能力

例如：

```text
legacy-prompt-importer
cursor-rule-migrator
legacy-variable-mapper
plain-document-migrator
```

属于：

```text
MIGRATION_CAPABILITY
```

完成后状态：

```text
COMPLETED
```

日常运行默认不再加载。

---

# 7B. Legacy Variable Migration

旧变量迁移必须分类：

```text
MAPPED
DERIVED
DEFAULTED
NEEDS_INPUT
DEPRECATED
CONFLICT
```

规则：

### MAPPED

旧变量与新变量有明确映射，直接迁移，不重复询问。

### DERIVED

可从 Git、代码、文档、现有状态可靠推导，自动生成并记录证据。

### DEFAULTED

Banyan 新变量有安全且不改变业务语义的默认值，可自动采用并说明。

### NEEDS_INPUT

无法从现有资料确定，且会真实影响后续行为，才要求用户填写/确认。

### DEPRECATED

新体系不再需要，仅保留迁移记录，不继续驱动运行。

### CONFLICT

多个来源出现矛盾，必须显示来源与候选值，进入 Decision Router。

迁移过程中必须记录：

```text
旧变量
新变量
来源
迁移方式
置信度
是否需人工
冲突
验证
```

禁止把所有新变量一次性重新抛给用户填写。

---

# 7C. Migration Center

Control Plane 应提供独立 Migration Center。

至少显示：

```text
Legacy Files
Rules
Skills
Variables
Decisions
Progress Sources

Mapped
Derived
Defaulted
Needs Input
Deprecated
Conflict
```

单个变量至少展示：

```text
Variable
Target Value
Source
Migration Method
Confidence
Needs Human
Validation
```

迁移流程：

```text
READ_ONLY Scan
↓
Legacy Inventory
↓
Mapping
↓
Only NEEDS_INPUT / CONFLICT Ask Human
↓
Migration Preview
↓
Project Instance Bootstrap
↓
Generate / Map Banyan Artifacts
↓
Index
↓
Semantic Compatibility Diff
↓
Shadow Mode
↓
Cutover
↓
Legacy Compatibility / Archive
```

迁移只执行一次，但 Migration Map 永久保留用于审计和回滚。

---


# 7D. AI Capability Preservation Layer：迁的是“能力”，不只是文件

Legacy AI Governance 迁移必须同时回答两个问题：

```text
旧文件去了哪里？
旧 AI 会做的事情还会不会？
```

因此 Stage 01 不能只生成文件 Inventory，还必须发现：

```text
AI Source Capability
AI Runtime Capability
AI Collaboration Capability
AI Generated Artifact
AI Operational Artifact
AI Safety / Governance Behavior
```

至少分四类重新盘点：

### 7D.1 AI 源能力

```text
Prompt
Rule
Policy
Role
Skill
Command
Workflow
State
Template
Schema
Tool
Hook
Adapter Config
```

### 7D.2 AI 生成的正式工程产物

例如：

```text
PRD
DEC
ADR
CR
UI-DEC
Architecture
Technical Design
API / Data Contract
UI_SPEC
Batch
Test
Acceptance
Release
Trace
```

### 7D.3 AI 生成的辅助/派生产物

例如：

```text
Project Dashboard
Progress
Worklog
Handover
Plain / Guide
Design Pack
Implementation Pack
Effective UI Contract
Screenshot Diff
Visual Repair Record
Discussion / Review Pack
Context Cache
```

### 7D.4 AI 运行行为

例如：

```text
编号保护
新窗口恢复
知情决策
变更稿
Batch 收口
视觉修复
在引用保护
临时桩清理
禁止为验收改口径
权限门禁
```

这些行为即使没有一个独立文件，也必须作为 Capability 被盘点。

---

## 7D.5 AI Capability Preservation Matrix

必须维护能力级保留矩阵，逻辑字段至少包括：

```yaml
legacy_capability_id:
name:
source_locations:
legacy_behavior:
business_or_engineering_value:
migration_action:
target_capability:
owner_stage:
integration_stages:
compatibility_mode:
regression_cases:
status:
```

推荐 `migration_action`：

```text
KEEP
MAP
GENERALIZE
PROJECT_ONLY
REPLACE_EQUIVALENT
COMPATIBILITY_READ
ARCHIVE
DEPRECATE
DROP_WITH_APPROVAL
```

禁止：

```text
扫描到了能力
↓
没有归宿
↓
直接不管
```

任何有价值能力最终必须是：

```text
PRESERVED
GENERALIZED
PROJECT_ONLY
REPLACED_WITH_EQUIVALENT
ARCHIVED_WITH_REASON
DEPRECATED_WITH_APPROVAL
```

---

# 7E. AI Generated Artifact Migration Layer

AI 已经生成出来的产物必须与“AI 能力”分开迁移。

必须维护：

```text
AI_GENERATED_ARTIFACT_INVENTORY
AI_ARTIFACT_MIGRATION_MATRIX
```

每个 Artifact 至少记录：

```yaml
source_path:
artifact_type:
artifact_id:
canonical_or_derived:
current_status:
current_version:
source_hash:
references:
migration_action:
target_role:
target_location:
transform_rule:
index_policy:
compatibility_policy:
validation:
rollback:
status:
```

统一迁移动作：

```text
KEEP
MAP
TRANSFORM
REGENERATE
INDEX_ONLY
COMPATIBILITY_READ
ARCHIVE
SUPERSEDE
DEPRECATE
DROP_WITH_APPROVAL
```

其中：

```text
DROP_WITH_APPROVAL
```

不得由 Codex 自动决定。

如果 Artifact 属于 Canonical Truth，默认优先：

```text
KEEP_IN_PLACE
+
MAP
+
INDEX
```

而不是为了 Banyan 强制改目录。

---

# 7F. No-Loss Gate

Legacy Governance Cutover 前必须满足：

```text
Unmapped Valuable Capability = 0
Unmapped Canonical Artifact = 0
Unexplained Generated Artifact = 0
Unapproved Drop = 0
Failed Legacy Regression = 0
```

否则：

```text
NO_LOSS_GATE = FAIL
```

No-Loss 不要求所有旧文件永远保留原形；它要求每一个有价值能力和重要产物都有**明确归宿、转换依据和验证证据**。

---

# 7G. Codex Full Repository Rediscovery

Stage 01 在 Codex 中执行时，以真实仓库为准重新发现。

禁止把总纲目前列出的：

```text
v3.1
.cursor/rules
tools
plain
UI_SPEC
```

误认为完整清单。

Codex 必须从 Repository Root 重新盘点：

```text
AI files
AI rules
AI generated docs
AI generated manifests
runtime artifacts
progress artifacts
historical governance
scripts
tools
editor adapters
ignored-but-governed paths
Git history needed for migration
```

如果发现本总纲未预见的新 Legacy Capability：

```text
DISCOVERED_LEGACY_CAPABILITY
→ 加入 Preservation Matrix
→ 分类
→ 分配 Owner / Migration Action
→ 验证
```

而不是因为总纲没写就忽略。

---

# 7H. Parallel Draft Workspace / 变更稿模式

这是 v3.1 第 39A～39C 的高价值协作能力，必须保留，但在 Banyan Core 中去项目目录化。

通用名称：

```text
Parallel Draft Workspace
```

定位：

> **非 Canonical、可并行、可丢弃、可 Reconcile、可 Promote 的需求/变更草稿工作区。**

典型场景：

```text
同事 A
正在修改正式 PRD / 正式 Change / 开发

同事 B
同时需要盘点其它需求
↓
Parallel Draft Workspace
↓
只读 Canonical Truth
↓
写 DRAFT-* 草稿
↓
不占正式 CR / DEC / REQ 编号
↓
不修改正式 PRD / DEC / CR
↓
不修改业务代码
```

主线稳定后：

```text
Refresh Canonical Truth
↓
Rebase / Reconcile
↓
Conflict Analysis
↓
Decision（必要时）
↓
Promote
↓
Change Provider / CR
↓
Canonical Apply
```

允许状态：

```text
DRAFTING
WAITING_RECONCILE
CONFLICTED
READY_TO_PROMOTE
PROMOTING
PROMOTED
DISCARDED
```

关键硬约束：

- 它不是 Project Lifecycle Stage；
- 不修改 `Project Lifecycle`；
- 默认不能写 Canonical Truth；
- 默认不能修改业务代码；
- 草稿编号不能预占正式编号；
- Promote 前必须对最新 Canonical Truth 重新对照；
- 多个 Draft Workspace 可以并行存在；
- Promote 后仍通过正常 Change / Decision / Canonical Apply；
- 当前 Reference Project 的 `changes_temp` 只是 Legacy Mapping，不是 Core 固定目录。

Stage Owner 分工：

```text
Stage 03 → Draft Workspace Artifact Schema
Stage 05 → Runtime Workflow / Reconcile / Promote Trigger
Stage 06 → Draft → Formal Change / Canonical Apply
Stage 07 → v3.1 39A～39C Compatibility Mapping
Stage 11 → Draft Metadata Index
Stage 13 → Conflict / Promote Evidence
Stage 14 → Non-canonical Write Guard
Stage 16 → Draft Workspace / Pending Promote UI
```

---

# 7I. Batch Canonical Reconciliation：36A 能力保留

v3.1 的“开发批次结束后逐条盘点业务改动”升级为通用能力：

```text
Batch Canonical Reconciliation
```

在一个 Batch 准备 Close / Accepted 前：

```text
本批真实实现
+
本批 Decision
+
本批 Change
+
本批 Test / Acceptance
↓
Business Semantic Diff
```

分类：

```text
PURE_IMPLEMENTATION
CANONICAL_ALREADY_UPDATED
BUSINESS_CHANGE_NOT_CANONICALIZED
CONFLICT
```

规则：

- `PURE_IMPLEMENTATION` 不写入 PRD；
- 已 Canonical Apply 的变化不重复建 CR；
- 新确认的业务语义变化必须通过 Change / Canonical Apply；
- Approved/Baselined 历史不能被静默覆盖；
- Batch 不得以“代码已完成”替代 Canonical Reconciliation。

---

# 7J. Reference Integrity Policy：在引用规则保护

正式 Artifact 只要仍被有效 Source 引用：

```text
禁止删除正文
禁止清空正文
禁止整篇换成别的主题
禁止把既有 ID 改挂到新主题
```

正确处理：

```text
同主题修订
→ 新版本 / Supersede

新主题
→ 新 ID / 新 Artifact

错误换题
→ 从历史恢复旧语义
→ 新主题重新分配 ID
→ 按语义修正引用
```

禁止：

```text
全局字符串替换编号
```

Stage 03 定义 Reference Integrity Contract，Stage 11 提供引用图，Stage 14 执行 Governance Check，Stage 07 负责 Legacy Compatibility。

---

# 7K. Test Integrity：临时桩与验收口径保护

测试与验收必须证明实现符合已确认口径，不能反过来修改业务口径来“让测试通过”。

禁止：

```text
为了通过测试
→ 修改已确认业务规则
→ 修改验收口径
→ 用永久硬编码伪装成功
→ 用临时桩冒充正式实现
```

允许临时使用：

```text
stub
mock
test data
temporary bypass
```

但必须：

```text
显式标记 TEMPORARY
记录 Owner / Scope / Reason
限制影响范围
测试完成后清理
产生 Evidence
```

如果测试发现产品实现与已确认规则不一致：

```text
修实现
```

如果确实需要改变规则：

```text
Decision / Change
→ Canonical Apply
→ 再更新 Test / Acceptance
```

Stage 13 定义 Test / Evidence Integrity，Stage 14 强制 Governance，Stage 07 验证 Legacy 行为等价。

---

# 7L. WORKLOG / HANDOVER / Progress 兼容映射

旧 Operational Artifact 不直接删除。

建议语义映射：

```text
WORKLOG
→ Activity / Event / Evidence

HANDOVER
→ Session Recovery / Handover Snapshot / Active Workflow Resume

PROJECT_DASHBOARD
→ Control Plane Overview Projection

DEVELOPMENT_PROGRESS
→ Multi-dimensional Progress Read Model

DOCUMENT_PROGRESS
→ Artifact / Canonicalization Progress

旧 Batch Progress
→ Workflow / Work Item / Test / Acceptance / Closure Dimensions
```

迁移要求：

- 历史日志继续可查询；
- Handover 中有效的未完成事项不得丢失；
- 新窗口恢复不再依赖聊天记忆；
- Legacy Progress 不强制伪映射成一个百分比；
- 原进度证据和更新时间必须保留；
- 旧 Dashboard 退役前必须证明 Control Plane 能覆盖其有效信息。

---

# 8. AI 文件统一“自解释契约”

用户要求以后生成的角色、技能等 AI 文件都有注释和使用说明。

因此所有 Banyan AI Artifact 必须满足统一元数据。

推荐至少包含：

```yaml
id:
type:
version:
status:
scope:
purpose:
when_to_use:
when_not_to_use:
inputs:
outputs:
permissions:
forbidden:
dependencies:
source_of_truth:
generated_or_manual:
compatibility:
validation:
rollback:
maintenance_owner:
last_updated:
```

Markdown 文件必须有：

```text
这是什么
什么时候加载
输入是什么
输出是什么
允许做什么
禁止做什么
依赖什么
如何验证
如何回滚
谁维护
```

这里的 `maintenance_owner` 表示 Artifact/Capability 的维护归属，不表示 Git Contributor，也不表示开发者职位。人员贡献来源统一由 Git Identity / Commit Provenance 记录，禁止把两种 Owner 语义混在一起。

YAML 可使用注释。

JSON 如果不适合写行内注释：

- 必须有 `$schema`；
- 可以使用标准允许的 `$comment`；
- 同目录必须有 README；
- 不允许只放“裸 JSON”让下一位 AI 猜含义。

生成文件还必须标记：

```text
GENERATED FILE
DO NOT EDIT DIRECTLY
SOURCE: ...
REGENERATE: ...
```

---

# 9. “有记忆”不能等于建立第二套项目真源

建议把 AI Memory 分成三层。

## 9.1 Project Fact Memory

不单独复制事实。

来源必须是 Project Instance 映射的正式 Source Role，例如：

```text
PROJECT_FACT_SOURCE
DECISION_SOURCE
ARCHITECTURE_SOURCE
UI_SOURCE
CHANGE_SOURCE
```

当前 Reference Project 可以把这些角色映射到其现有目录，但这只是项目配置，不是 Banyan Core 的硬编码。

通过 Index + Context 动态取。

## 9.2 Engineering Experience Memory

存放：

- AI 常见失误；
- 返工原因；
- 工程经验；
- 哪类任务应该加载哪些 Skill；
- 哪些规则组合效果好。

推荐：

```text
.banyan/memory/lessons/
```

## 9.3 Prompt Learning Memory

形成：

```text
Prompt
→ Result
→ Review
→ Root Cause
→ Pattern
```

推荐：

```text
.banyan/memory/prompt-reviews/
.banyan/memory/patterns/
```

只有被复盘并批准/达到准入条件的经验才能提升为长期 Pattern。

避免：

> AI 把一次偶然成功直接写成永久规则。

---


# 9A. Change Workspace Provider 与 OpenSpec 参考实现

> **Banyan Core 定义 Change Workspace Provider Contract；OpenSpec 是当前首选/参考 Provider，而不是 Banyan Core 的硬依赖，也不是第二套 PRD。**

Banyan 管整个项目生命周期；Change Workspace Provider 只管理“一次变化”。当前计划以 OpenSpec 作为首个参考实现，但其它项目可替换 Provider，只要满足同一 Canonical Apply / Governance / Trace 契约。

核心关系：

```text
Banyan
├── Governance
├── Decision
├── PRD
├── UI
├── Architecture
├── Delivery
├── Change Workspace Provider
│   └── OpenSpec Adapter（参考实现）
├── Trace
├── Evidence
├── Memory
└── Adapter
```

## 9A.1 Change Provider / OpenSpec 与正式真源

禁止：

```text
OpenSpec Specs
+
Project Canonical Requirement Source
=
两套正式需求真源
```

采用：

```text
OpenSpec Change
↓
已确认 Delta
↓
Banyan Canonical Apply
↓
Project Canonical Sources
（由 Project Instance Source Mapping 决定物理位置）
├── PRD / Requirement Truth
├── DEC / CR
├── ADR
├── UI_SPEC
└── Technical Design
↓
SQLite Reindex
```

SQLite 继续只是可重建索引。

## 9A.2 OpenSpec Change 与 CR 不等价

```text
OpenSpec Change
= 工作容器
= 可以讨论、修改、取消、尚未批准

CR
= 正式治理记录
= 表示已确认变化对 Approved/Baselined 需求产生影响
```

关系：

```text
OpenSpec Change
↓
确认
↓
CR（需要时）
↓
PRD / UI_SPEC / ADR...
```

并非每个 OpenSpec Change 都必须产生 CR；纯实现修复可以只形成任务和证据。

## 9A.3 OpenSpec Reference Provider Schema

目标 Schema：

```text
banyan-change

proposal
↓
requirement-delta
↓
impact
↓
discussion-pack
↓
decision
↓
canonical-apply
↓
design
↓
tasks
↓
implementation
↓
final-review-pack
↓
archive
```

是否使用 OpenSpec 原生 `specs/` 目录作为中间 Artifact 可在实施阶段决定，但**不得让其升格成与 Project Instance 映射的正式 Requirement Source 并列的第二业务真源**。

## 9A.4 OpenSpec Apply 受 Banyan Governance 控制

OpenSpec 不拥有无条件代码写入权。

执行代码前至少验证：

```text
Change 状态
Decision 是否已完成
Canonical Apply 是否完成
Batch 是否 Ready
CODE_WRITE 是否允许
Protected Paths
P0/P1
Migration / Rollback
```

只有 Governance Check = PASS 才允许实施。

## 9A.5 Archive 不是“把 OpenSpec 变成 PRD”

归档顺序：

```text
Implementation Complete
↓
Test / Acceptance / Evidence
↓
Canonical Truth 已更新
↓
SQLite Reindex
↓
Trace Check
↓
OpenSpec Archive
```

OpenSpec 自身状态与 PRD/UI_SPEC/Batch/Release 状态必须分开。

---

# 9B. Change Communication：会议讨论与评审文档

保留并强化“会议讨论用的规范、丰富需求材料”。

它不是第二套 PRD，而是一次 Change 的**面向人的会议界面**。

## 9B.1 Discussion Pack：定需求阶段

在 Canonical Apply 前生成：

```text
discussion/
├── 00-会议一页纸.md
├── 01-现状与问题.md
├── 02-本次拟议变化.md
├── 03-典型用户场景.md
├── 04-变化前后对照.md
├── 05-影响范围.md
├── 06-方案比较.md
├── 07-待决策事项.md
└── 08-会议议程与结论记录.md
```

只把真正需要人的事项带进会议。

## 9B.2 Final Review Pack：PRD/规范确认以后

用于产品、UI、前端、后端、测试、项目负责人共同启动实施：

```text
review/
├── 00-本次变更总览.md
├── 01-业务变化前后对照.md
├── 02-用户角色与场景影响.md
├── 03-页面与UI变化.md
├── 04-权限状态数据影响.md
├── 05-技术影响范围.md
├── 06-测试验收重点.md
├── 07-发布迁移与回滚.md
├── 08-风险与剩余事项.md
└── 09-研发启动会清单.md
```

会议材料不能直接成为正式规则。

会议中新产生的结论必须：

```text
Meeting Conclusion
↓
Decision Router
↓
DEC / CR / ADR / UI-DEC
↓
Canonical Apply
↓
重新生成 Meeting/Review Pack
```

---

# 9C. Project Knowledge Publishing：长期项目说明书

现有：

```text
docs/project/plain-spec/
docs/project/plain-document/
```

不删除、不直接重建。

但后续要把其能力从：

> PRD 白话摘要

升级为：

> **Project Guide / System Handbook：面向读者的长期系统说明书。**

## 9C.1 Project Guide 与 PRD 的区别

```text
PRD
= 规范性
= 产品必须是什么
= 用于需求治理与验收

Project Guide
= 解释性
= 整个系统现在怎么工作、怎么使用、怎么理解
= 用于新人、产品、研发、测试、交接和日常查阅
```

Project Guide 不能按 REQ 编号机械重写 PRD。

## 9C.2 Reader-oriented Information Architecture

目标内容应围绕读者问题组织，例如：

```text
Project Guide
├── 00-开始阅读/
├── 01-业务怎么运行/
├── 02-各端怎么使用/
├── 03-主要能力说明/
├── 04-关键规则手册/
├── 05-系统怎么组成/
├── 06-场景流程图/
└── 07-维护与排查/
```

例如“商品管理”应该解释：

```text
商品是什么
谁会接触
从哪里进入
完整生命周期
各端分别怎么操作
上架/下架意味着什么
与订单有什么关系
常见误区
```

而不是：

```text
REQ-081 摘要
REQ-082 摘要
REQ-083 摘要
```

## 9C.3 Project Guide 来源不是只有 PRD

按主题动态组合：

```text
PRD
DEC
ADR
UI_SPEC / 页面事实
Architecture
Current Baseline Code
Acceptance
```

但任何内容都不能反写或覆盖正式真源。

## 9C.4 GUIDE_SYNC 取代简单“一对一 PRD 映射”

目标关系是多对多知识映射：

```yaml
guide: 04-关键规则手册/钱怎么算.md

sources:
  - PRD:M03
  - DEC-021
  - DEC-034
  - ARCH:settlement

update_when:
  - amount_rule_changed
  - settlement_rule_changed

ignore_when:
  - css_changed
  - menu_text_changed
```

变化流程：

```text
Canonical Truth Changed
↓
Guide Impact Analysis
↓
命中 Guide 标记 STALE
↓
只增量刷新命中的说明文档
↓
质量校验
↓
SYNCED
```

不是每次 PRD 变化都重生整套说明书。

## 9C.5 旧 plain-document 的迁移

```text
Inventory
↓
KEEP / REWRITE / MERGE / ARCHIVE / MIGRATE
↓
建立新的 Guide Map
↓
建立 GUIDE_SYNC
↓
双轨校验
↓
逐步切换
```

旧内容必须保留到迁移验收通过。

---


## 9C.6 稳定知识与迭代知识必须分离

Project Guide 只承载适合长期阅读和持续维护的系统知识。

以下内容不得长期混入 Project Guide 正文：

```text
本批暂不做
本轮临时不开
当前验收只测某项
为了本次测试的临时桩
某个 Batch 的短期绕路
待下一批删除的临时入口
当前开发会话的施工提醒
```

这些分别进入：

```text
OpenSpec / Change
Final Review Pack
Batch / Work Item
Acceptance
Evidence
Open Items
Release Notes
```

Project Guide 应回答：

```text
系统是什么
为什么这么组成
用户怎么使用
业务怎么运行
关键规则怎么理解
常见问题如何定位
```

而不是保存当前迭代的施工状态。

阶段 10 审计旧 Plain 体系时，必须额外标记：

```text
STABLE_KNOWLEDGE
ITERATION_CONTEXT
ACCEPTANCE_CONTEXT
HISTORICAL_CONTEXT
```

只有 `STABLE_KNOWLEDGE` 默认允许进入长期 Guide。

---


# 9D. Interaction Orchestrator 与五档决策机制

v3.1 的 HIGH/LOW + 全量二次确认升级为**按风险和必要性动态路由**。

核心组件：

```text
Task Router
↓
Change Necessity Engine
↓
Decision Necessity Engine
↓
Decision Risk Classifier
↓
Workflow Router
↓
Context Builder
↓
Permission Gate
↓
Impact Analyzer
```

这里表示**逻辑决策链**，不是把所有组件实现都归给 Interaction/Workflow Stage：Context Builder 的实现 Owner 是 Stage 12，Impact/Evidence Engine 是 Stage 13，Permission/Governance Runtime 是 Stage 14；Stage 05 只定义如何调用这些能力及在缺少后置实现时的 Contract/Interface。

## 9D.1 五档机制

### `AUTO`

不需要用户选择即可安全执行。

适用：

```text
已有 Approved/Baselined 规则
事实唯一
可逆
不改变业务语义
影响范围明确
```

示例：

- 按 UI_SPEC 修复实现偏差；
- 重建 SQLite；
- 重建 Adapter 输出；
- 补已有验收规则对应的测试；
- 修正明确的文档引用错误。

### `ASK_ONCE`

低风险偏好或组织选择，问一次后即可执行。

例如：

- 新 Skill 命名；
- 低风险目录命名；
- 展示顺序。

### `CONFIRM_ONCE`

改变正式规则或目录，但影响明确、可迁移、可回滚。

例如：

- 通用 Skill 从编辑器私有目录迁移到 `tools/`；
- 普通 UI 规范调整；
- 中等影响工程治理变化。

### `CONFIRM_TWICE`

真正高风险事项保留完整知情决策：

- 金额 / 支付 / 退款 / 结算；
- 权限 / 身份 / 隐私 / 安全；
- 状态机 / 数据归属 / 删除 / 迁移；
- 不兼容变更；
- PRD 核心业务规则；
- 总体架构 / 模块边界；
- Approved / Baselined / 生产风险。

### `CROSS_DOMAIN_CONFIRM`

一个根决策同时影响多个正式域：

```text
PRD
UI
Architecture
API
Data
Batch
```

用户只确认**根决策一次**；确认后由 Canonical Apply 负责向各正式真源传播。

## 9D.2 “两边都要确认”的三种情况

### 派生同步

```text
PRD 已确认
↓
UI Scope 必须同步
```

这是派生，不再问一次。

### 两个真源冲突

```text
PRD 无删除功能
Design 有删除按钮
```

进入 `CROSS_DOMAIN_CONFIRM`。

### 用户已经一次表达完整意图

例如：

> 增加批量删除功能，并按这张设计图实现。

不得再机械地分别询问“要不要改 PRD”和“要不要改 UI_SPEC”。

系统只补充隐藏风险，然后按根决策对应档位确认。

## 9D.3 已确认决策默认不重复问

Decision Index 至少记录：

```yaml
decision_id:
status:
scope:
depends_on:
invalidate_when:
```

只在依赖变化后：

```text
APPLIED → STALE
```

才重新评审。

## 9D.4 项目复杂度、任务复杂度、决策风险三维分离

项目级：

```text
LIGHT
STANDARD
FULL
```

任务级：

```text
FAST
NORMAL
CONTROLLED
```

决策级：

```text
AUTO
ASK_ONCE
CONFIRM_ONCE
CONFIRM_TWICE
CROSS_DOMAIN_CONFIRM
```

大型 FULL 项目里的一个 1px 视觉修复仍然可以走：

```text
FAST + AUTO
```

避免“项目复杂 = 每件小事都复杂”。


# 9E. Adaptive Runtime Workflow Engine

Banyan 的项目治理必须从“固定阶段驱动”升级为“任务驱动 + 运行时自适应编排”。

核心原则：

> **项目有生命周期，但任务没有固定阶段；每个任务根据当前事实、变化类型、影响范围和风险动态组装最短安全工作流。**

## 9E.1 G0～G11 的新定位

G0～G11 不删除。

它们继续用于：

- 历史兼容；
- 项目宏观生命周期；
- 老项目治理语义映射；
- Legacy v3.1 Compatibility；
- 项目状态解释。

但禁止把 G0～G11 当成每个任务都必须顺序执行的流水线。

例如项目总体处于：

```text
IMPLEMENTATION
```

同时可以运行：

```text
TASK-A → UI_VISUAL_REPAIR → FAST
TASK-B → FEATURE_CHANGE → CONTROLLED
TASK-C → TEST_FAILURE_REPAIR → FAST
TASK-D → REFACTOR → NORMAL
```

## 9E.2 Adaptive Workflow 核心链

```text
User Intent
↓
Task Classifier
↓
Context Resolver
↓
Delta Classifier
↓
Impact Analyzer
↓
Risk Classifier
↓
Decision Router
↓
Workflow Composer
↓
Permission / Governance
↓
Workflow Runtime
↓
Observe Events
↓
Re-route when needed
↓
Evidence
↓
Closure
```

这条链只表示 Runtime 的逻辑顺序，不改变 Single Owner：Stage 05 拥有 Workflow Graph / Router / Composer / Reconciliation 语义；Stage 12、13、14 分别提供 Context、Impact/Evidence、Governance 的正式实现。

用户不需要手工选择 Workflow Family、G 阶段或决策档位。

## 9E.3 Workflow Family

Banyan 不维护几十条大型固定工作流，而维护少量通用 Family。

初始 Catalog 至少覆盖：

```text
BUG_FIX
CONFORMANCE_FIX
IMPLEMENT_APPROVED
UI_VISUAL_REPAIR
UI_EXPERIMENT
UI_CHANGE
LIGHT_FEATURE_CHANGE
FEATURE_CHANGE
DECISION_INTERRUPT
CROSS_DOMAIN_CHANGE
CONTRACT_CHANGE
ARCHITECTURE_CHANGE
REFACTOR
DEPENDENCY_CHANGE
DATA_MIGRATION
TEST_FAILURE_REPAIR
HOTFIX
DOC_MAINTENANCE
KNOWLEDGE_SYNC
RELEASE
AUDIT_DISCOVERY
```

Family 表达“通常需要哪些能力”，不是固定死的步骤表。

## 9E.4 Workflow Atom

通用原子示例：

```text
DISCOVER
VERIFY_SOURCE
LOAD_CONTEXT
DIFF
IMPACT_ANALYSIS
DECIDE
CANONICAL_APPLY
PLAN
IMPLEMENT
EXPERIMENT
VISUAL_REPAIR
TEST
INTEGRATE
MIGRATE
ACCEPT
RELEASE
PUBLISH
CLOSE
```

Workflow Composer 根据任务实际需要拼接。

例如已有 Approved 规则下的普通 Bug：

```text
VERIFY_SOURCE
→ IMPLEMENT
→ TEST
→ EVIDENCE
```

而高风险业务变更可能是：

```text
IMPACT_ANALYSIS
→ DECIDE
→ CANONICAL_APPLY
→ PLAN
→ IMPLEMENT
→ TEST
→ ACCEPT
→ EVIDENCE
```

未使用的 Atom 不加载、不执行。

## 9E.5 Workflow Graph，而不是固定链

Runtime Workflow 必须支持：

```text
Branch
Merge
Loop
Pause
Resume
Retry
Skip
Replace
Invalidate
Cancel
```

因此内部使用：

```text
Workflow Graph
```

而不是只使用线性 `Step 1 → Step 2 → Step 3`。

## 9E.6 Workflow Node Contract

每个运行节点至少声明：

```yaml
id:
type:
purpose:
requires:
inputs:
produces:
completion_condition:
evidence_required:
invalidated_by:
reentry_policy:
permissions:
rollback:
```

`reentry_policy` 可包括：

```text
RESUME
RESTART
SKIP_IF_SATISFIED
REPLACE
MANUAL_REVIEW
```

Reconciliation Engine 必须根据 Contract 判断旧节点是否仍有意义，而不是因为“刚才停在第 2 步”就机械返回第 2 步。

## 9E.7 Workflow Runtime Instance

一次真实执行至少记录：

```yaml
workflow_instance:
  id:
  family:
  execution_profile:
  current_node:
  graph_version:
  state:
  affected_scope:
  active_branch:
  checkpoint:
  resume_point:
  decisions:
  change_refs:
  evidence:
  health:
```

Runtime 状态是可重建/可解释的执行态，不成为业务真源。

## 9E.8 Re-route Trigger

AI 不得无理由随意改工作流。

只有明确事件允许 Re-route，例如：

```text
NEW_FACT_DISCOVERED
CONFLICT_DETECTED
MISSING_CANONICAL_RULE
USER_INTENT_CHANGED
TEST_FAILED
VALIDATION_FAILED
DESIGN_CHANGED
DEPENDENCY_CHANGED
SECURITY_RISK_FOUND
DATA_RISK_FOUND
ASSUMPTION_INVALIDATED
SCOPE_CHANGED
```

每次 Re-route 必须记录 Trigger、原因、影响范围和 Evidence。

## 9E.9 Workflow Re-router

触发后允许：

```text
原 Workflow
↓
Pause Current Node
↓
Create Branch / Subflow
↓
Execute Branch
↓
Workflow Reconciliation
```

不得默认重跑整个 Workflow。

## 9E.10 Workflow Reconciliation Engine

Branch / Subflow 结束后必须明确选择：

```text
RESUME
RESTART_NODE
SKIP_NODE
REPLACE_NODE
INVALIDATE_DOWNSTREAM
REPLAN
ABORT
```

Reconciliation 判断依据：

```text
旧节点的前置条件是否仍成立
节点目标是否仍需要
旧输入是否失效
Branch 是否已经产生同等输出
已完成结果是否仍兼容
下游节点具体依赖哪些输出
风险和置信度
```

## 9E.11 Dependency / Invalidation Engine

变化只影响真正依赖被修改输出的节点。

例如：

```text
N2 output changed
↓
N3 depends_on N2 → INVALIDATED
N4 does_not_depend_on N2 → KEEP
```

禁止因为一个局部变化就默认从头执行全部流程。

## 9E.12 Pause / Branch / Resume

开发途中发现缺失业务规则：

```text
IMPLEMENT
↓
MISSING_CANONICAL_RULE
↓
Pause affected work
↓
DECISION_INTERRUPT
↓
Decision
↓
Canonical Apply
↓
Impact Recalculation
↓
Reconciliation
↓
Resume / Replace / Replan
```

必须记录 Resume Point。

## 9E.13 Partial Blocking

一个 Batch 中部分 Work Item 被决策或依赖阻塞时：

```text
Affected Work Item → BLOCKED_BY_DECISION
Unaffected Work Item → CONTINUE
```

只有正式 Impact Analysis（实现 Owner：Stage 13）证明整个 Batch 都受影响时，才阻塞整个 Batch。

## 9E.14 Decision Interrupt

Decision Interrupt 不等于“回到需求阶段重新开始”。

它是一条可插入的子工作流：

```text
Gap / Conflict
→ Impact
→ Decision Router
→ DEC / ADR / UI-DEC / CR（按需）
→ Canonical Apply
→ Contract Refresh
→ Reconciliation
→ Resume
```

已明确事实不得重复决策。

## 9E.15 Experiment Mode 与 Candidate Delta

可逆 UI/交互/实现探索允许：

```text
Current Workflow
↓
EXPERIMENT MODE
↓
Temporary Branch
↓
Preview / Compare
↓
Accept | Discard
```

`Discard`：

```text
Rollback temporary diff
→ Resume Parent Workflow
```

`Accept`：

```text
Candidate Delta
→ Change Classification
→ 必要时 Decision
→ Canonicalize
→ Reconcile Parent Workflow
```

Experiment 未接受前：

- 不自动修改 PRD；
- 不自动修改 UI_SPEC；
- 不升格为正式 Design Revision；
- 不创建无意义 DEC；
- 不把临时结果写成项目真源。

## 9E.16 UI Visual Repair 与正式 UI Change 分离

设计图/Effective UI Contract 没变，只是实现不像：

```text
UI_VISUAL_REPAIR
FAST
通常 AUTO
```

如果用户临时想“试试看更大、更松、另一种排列”：

```text
UI_EXPERIMENT
```

如果 Experiment 被接受且正式改变设计：

```text
UI_CHANGE
```

如果视觉调整实际改变业务行为、删除安全、权限、状态等：

```text
ESCALATE → NORMAL / CONTROLLED
```

## 9E.17 Workflow Escalation / De-escalation

Workflow 可在运行中升级或降级。

升级示例：

```text
UI_VISUAL_REPAIR
↓
Behavior Diff Detected
↓
UI_CHANGE / CROSS_DOMAIN_CHANGE
↓
FAST → CONTROLLED
```

降级示例：

```text
用户说“新增功能”
↓
扫描发现 Approved PRD 已明确，只是代码缺失
↓
FEATURE_CHANGE
→ CONFORMANCE_FIX
↓
NORMAL → FAST
```

初始分类不是永久锁定。

## 9E.18 Workflow Confidence

每次 Reconciliation / Re-route 至少标记：

```text
HIGH
MEDIUM
LOW
```

规则：

- 高置信度、低风险、可逆：允许 AUTO；
- 中等置信度：根据影响范围 ASK_ONCE / CONFIRM_ONCE；
- 低置信度或高风险：不得自动跳过/废弃关键节点，进入人工确认。

## 9E.19 Workflow Event Log

每次改变路线必须留下结构化记录：

```yaml
workflow:
trigger:
occurred_at_node:
old_plan:
inserted_branch:
changed_outputs:
reconciliation:
invalidated_nodes:
resume_point:
reason:
confidence:
decision_refs:
evidence:
```

用于 Trace、WebUI 和后续 Prompt Learning。

## 9E.20 Context 必须随 Workflow 局部变化

Re-route 后只重新组装受影响 Context：

```text
Changed Scope
+
Relevant Canonical Sources
+
New Decisions
+
Affected Contracts
```

禁止每次 Branch 都重新加载全项目文档。

## 9E.21 Control Plane 的 Workflow 可观测性

Control Plane 至少显示：

```text
Workflow Instance
Family
Execution Profile
Original Plan
Current Graph
Current Node
Active Branch
Trigger
Re-route History
Blocked Scope
Unaffected Scope
Resume Candidate
Reconciliation Result
Workflow Health
Confidence
Evidence
```

当 Workflow 改变时应明确显示：

```text
Old Route
→ Why Changed
→ Inserted Branch
→ What Was Invalidated
→ Where It Will Resume
```

而不是只显示“任务进行中”。

## 9E.22 自适应工作流的核心限制

禁止：

- AI 无 Trigger 自行无限增加步骤；
- 为了“更完整”自动升级成重流程；
- 低风险视觉修复强制创建 OpenSpec Change；
- 子流程结束后无 Reconciliation 就直接恢复旧节点；
- 高风险节点被低置信度 AI 自动 Skip；
- Branch 临时产物未经晋升就写入 Canonical Truth；
- 一个局部变化让整个 Batch 无差别重跑。

---

## 9E.23 Workflow Artifact Budget：流程越轻，产物越少

`FAST / NORMAL / CONTROLLED` 不只是执行速度标签，还决定默认治理产物预算。

### FAST

默认只产生必要的：

```text
Task / Work Item State
Code / Doc Diff
Test / Validation Evidence
Workflow Event
```

除非 Trigger 发生，否则默认不创建：

```text
OpenSpec Change
CR
DEC
ADR
新的 PRD Version
新的 UI_SPEC Version
大型 Review Pack
```

### NORMAL

如果存在 Canonical Change，才创建 Change / Delta；如果事实已明确则不创建无意义 Decision。

### CONTROLLED

对真正高风险变更要求：

```text
Formal Change
Impact
Decision
Migration / Rollback
Acceptance
Evidence
Trace
```

原则：

> **流程治理产物由风险和变化事实触发，不由“项目很复杂”触发。**

## 9E.24 Workflow Graph Revision

运行中的 Workflow Graph 每次 Re-route 不覆盖原计划。

必须保留：

```text
Graph Revision 1
→ Re-route Event
→ Graph Revision 2
→ Re-route Event
→ Graph Revision 3
```

每个 Revision 至少记录：

```yaml
revision:
parent_revision:
trigger:
changed_nodes:
added_edges:
removed_edges:
invalidated_nodes:
created_at:
```

这样 Control Plane、Trace 和事后复盘都能回答：

> 原计划是什么、为什么变、变了什么、最后实际走了哪条路径。

---


# 10. Token 优化总原则

当前大型规范不应继续每个窗口整份加载。

未来采用：

```text
Bootstrap Context
+
Task Profile
+
Relevant Policies
+
Relevant Skills
+
Relevant Project Facts
+
Relevant Trace
```

而不是：

```text
加载全部 5000+ 行规范
+
加载全部项目文档
```

Context Builder 应回答：

```text
我现在是什么任务？
属于哪个项目阶段？
需要什么 Role？
需要哪些 Policy？
需要哪些 Skill？
需要哪些 Project Fact？
需要哪些 DEC / ADR / CR？
需要哪些代码文件？
哪些内容禁止加载？
```

最终目标：

> **按任务组装 Context，而不是按目录灌满 Context。**

---

# 11. SQLite 数据迁移原则

SQLite 是本次改造中风险最高的部分之一，必须单独施工。

## 11.1 第一阶段只读建立索引

先扫描 Project Instance 已声明的 Source Role：

```text
PROJECT_FACT_SOURCE
DECISION_SOURCE
ARCHITECTURE_SOURCE
UI_SOURCE
CHANGE_SOURCE
TOOL_SOURCE metadata
.banyan Project Instance metadata
```

当前 Reference Project 的 `docs/project/**`、`tools/**` 只是这些 Source Role 的一种映射。

只写：

```text
banyan.db
```

绝不反向修改项目文件。

## 11.2 建立 Migration Manifest

每一次导入必须记录：

```text
source_path
source_hash
source_type
parsed_id
parsed_version
parsed_status
relations
parse_result
warnings
migration_version
timestamp
```

## 11.3 完整性对账

至少检查：

```text
文件数量
ID 数量
DEC 数量
ADR 数量
CR 数量
REQ 数量
Batch 数量
Worklog 数量
UI Spec 数量
Trace Edge 数量
无法解析数量
重复 ID
失效引用
孤儿引用
```

## 11.4 SQLite 不允许成为不可逆迁移

验收必须包含：

```text
删除数据库
重新 rebuild
结果一致
```

并对关键计数、ID 和关系做一致性校验。

---

# 12. 多编辑器规则释放模型

目标不是让 Banyan 理解三个编辑器，而是：

> **Banyan 维护中立规则，每个 Adapter 负责翻译。**

最终命令体验建议达到：

```bash
banyan doctor
banyan scan
banyan index build
banyan context build
banyan workflow status
banyan workflow inspect
banyan workflow resume
banyan commit plan
banyan commit batch
banyan contributors
banyan sync cursor
banyan sync codex
banyan sync claude
banyan sync all
banyan adapter check
banyan migration status
banyan rollback <migration>
```

这些只是目标接口，具体命令名在 CLI 阶段冻结。

## Adapter 必须保证

同一条 Banyan Policy：

```text
不得修改 docs/temp
```

无论释放到哪个编辑器，语义必须一致。

Adapter 只能调整：

- 文件格式；
- 入口；
- Skill 加载方式；
- Hook；
- Command；
- Context 机制；
- 工具特定能力。

不能改变：

- Policy；
- 项目事实；
- 权限；
- Gate；
- 决策语义。

多编辑器还必须遵守：

```text
Execution Client = 记录来源
!= 人员职责
!= 权限主体
!= Git Identity
```

Cursor / Codex / Claude 可以执行相同类型的任务；Banyan 不给编辑器固定“前端/后端/PRD”等职责。不同编辑器执行 Git 提交时必须使用同一套 Banyan Commit Policy，并保留实际 `client` 作为 Provenance。

---

# 12A. Git Identity、Contributor Profile、Commit Provenance 与统一 AI 提交

## 12A.1 Git Identity 是贡献身份，不追踪物理操作者

Banyan v1 采用：

```text
Git Commit Author Name + Author Email
=
Contribution Identity
```

逻辑唯一键推荐：

```text
normalized(author.name + "\0" + author.email)
→ git_identity_id
```

`git_identity_id` 只用于稳定索引；用户界面仍展示 Git 原始 `name + email`。

硬规则：

- 不追踪“现实中谁坐在电脑前”；
- 不根据操作系统账号、编辑器账号或聊天账号猜真实操作者；
- 用户使用别人电脑时，若该环境 Git Identity 是对方，Banyan 就如实把 Commit 归到该 Git Identity；
- 不提示强制切换身份；
- AI 不修改 global/local/worktree Git Identity；
- AI 不使用 `--author`、临时 `-c user.name/user.email` 等方式替用户改身份；
- 最终以 Commit Object 中实际 Author/Committer 为 Evidence。

Git `Author` 是主要贡献身份；`Committer` 同样保留为 Git Evidence，但不自动推导另一个“真实操作人”。

## 12A.2 Contributor Profile 是可选显示增强

Contributor Profile 以 Git Identity 为 Key，最小字段：

```yaml
git_identity_id:
git_name:
git_email:

profile:
  display_name: null   # optional
  status: null         # optional: ACTIVE / INACTIVE / LEFT / UNKNOWN
  note: null           # optional
```

规则：

- Profile 未配置时，直接显示 Git `name + email`；
- 不需要注册 Banyan User 才能提交；
- 不保存 `role_labels`；
- 不保存固定模块归属；
- 不保存前端/后端职位；
- `status` 只用于 WebUI 展示/筛选，不自动授权或禁用 Git 提交；
- 不自动合并多个 Git Identity 为同一个真人；
- Profile 变化不会重写历史 Commit。

## 12A.3 Role / Assignment / Client 的职责边界

必须区分：

```text
Git Identity
= 谁的 Git 贡献身份

Contributor Profile
= 可选的人类可读资料

Workflow / Task / Change / Batch / Module Context
= 这一次在做什么

Execution Client
= Cursor / Codex / Claude / Generic
```

Banyan `Role` 继续表示 AI Role、Workflow Role 或 Reader Role 等语义角色，不表示人员职位。

禁止：

```text
Cursor = 前端
Codex = 后端
Claude = PRD
Git Identity = 某个永久模块负责人
```

## 12A.4 Git 是 Commit 真源，Banyan 是语义 Provenance 层

Git 原生负责：

```text
Commit Hash
Author / Committer
Timestamp
Parent
Diff
Branch/History
```

Banyan 额外关联：

```text
Workflow
Task
Change
Batch
Module/Scope（若有）
Execution Client
Evidence / Validation
```

正确关系：

```text
Git Commit
       +
Banyan Semantic Context
       ↓
Commit Provenance
```

SQLite 只建立可重建索引，不成为第二 Git History。

## 12A.5 统一 Semantic Commit Policy

所有编辑器必须消费同一套 Commit Policy。

用户可以直接发：

```text
帮我把现在的修改合理分批提交。
```

Banyan Semantic Commit Planner 必须：

```text
读取真实 git status / diff
↓
识别当前 Workflow / Task / Change / Batch
↓
识别不同语义变化
↓
区分 READY / INCOMPLETE / UNRELATED / LOCAL_ONLY / SECRET_RISK
↓
按语义分 Commit Plan
↓
必要时按 hunk 精确 stage
↓
逐批 Validation
↓
Commit
↓
读取真实 Commit Object
↓
写 Commit Evidence / Trace
↓
报告剩余未提交内容
```

禁止把“目录相同”直接等价为“一个 Commit”，也禁止简单：

```text
git add .
git commit -m "update"
```

作为默认策略。

## 12A.6 Commit Plan 模式

统一支持语义：

```text
PLAN_ONLY
只生成分批方案，不提交

REVIEW_THEN_COMMIT
整批 Commit Plan 确认一次后执行，不逐 Commit 重复确认

AUTHORIZED_COMMIT
用户已经明确要求“帮我提交/分批提交”时，在无冲突、无 Secret 风险、无未知修改的情况下按计划执行
```

它们必须映射到既有 Decision / Governance 体系，不建立第二套确认机制。

出现以下情况必须停止或升级决策：

- Secret / Credential；
- 无法判断来源的修改；
- 明显未完成代码；
- 当前 Task 与 Working Tree 大量无关；
- Protected Path；
- 需要改写历史、force push、rebase 等高风险 Git 操作。

## 12A.7 Commit Message Contract

Banyan Core 定义中立 Commit Contract。Owner 边界固定为：

```text
Stage 01 → 盘点现有 Commit Practice
Stage 03 → 冻结 CommitPlan / CommitMessage / CommitProvenance Schema
Stage 05 → 冻结 Semantic Commit / Commit Message Policy
Stage 14 → 实现 Git Commit Safety Gate
Stage 15 → 实现 CLI / Runtime API / Adapter Execution
```

因此 **Stage 15 不得重新定义 Commit Policy**；它只能实现 Stage 05 已冻结的 Policy，并根据 Project Profile 解析该项目选择的 type/scope/trailer convention。

默认建议兼容 Conventional Commit 结构：

```text
<type>(<scope>): <summary>

<body when needed>

<trailers when available>
```

可用的最小 Banyan Trailer 候选：

```text
Banyan-Workflow:
Banyan-Task:
Banyan-Change:
Banyan-Batch:
Banyan-Client:
```

规则：

- 只有真实存在的关联才写，不填假 ID；
- 不写 `Banyan-Actor`，因为 Git Author 已经是贡献身份；
- Trailer 用于跨环境 Trace 重建，不取代 Git Commit 本身；
- 项目已有成熟 Commit Convention 时允许 Project Profile 覆盖格式，但不同编辑器仍必须使用同一项目规范。

## 12A.8 AI 分批提交安全规则

AI 必须：

- 不修改代码只为了“让 Commit 更好看”；
- 不把两个无关 Change 强行混成一个 Commit；
- 不把未完成改动标记为已完成；
- 不自动提交 Secret；
- 不默认提交未知大文件；
- 不因为用户说“全部提交”就绕过 Protected Path / Governance；
- 每个 Commit 前检查 staged diff；
- 每个 Commit 后读取真实 Commit Hash / Author / Diff Summary；
- 最后汇报“已提交什么 + 还剩什么 + 为什么没提交”。

---

# 13. AI 工作模式和机器权限

最终统一引入：

```text
READ_ONLY
PLAN_ONLY
DOC_WRITE
CODE_WRITE
REVIEW
```

每个任务必须先确定模式。

例如：

```yaml
mode: CODE_WRITE

permissions:
  read_docs: true
  write_docs: true
  read_code: true
  write_code: true

deny:
  modify_sql: true
  modify_infra: true
  git_push: true
  release: true
```

再由 Governance Check 验证：

```text
Project Stage
Batch
ALLOW_CODE_CHANGES
Protected Paths
Pending Decision
P0/P1
Baseline Protection
Editor Capability
```

身份/权限额外约束：

```text
Git Identity / Contributor Profile
= Attribution
!= Authentication
!= Authorization
```

除非未来项目显式启用独立认证/权限 Provider，`display_name / status / note` 等 Contributor Profile 字段不得改变 Governance Permission。

输出：

```text
PASS
```

或：

```text
BLOCK
```

这样以后“不要改业务代码”不仅存在于自然语言里，而是成为执行前检查项。

---

# 14. Banyan Control Plane、进度与可观测性

Control Plane 第一版建议至少包含：

```text
Overview
Change Center
Delivery
Test & Acceptance
Decision Center
Knowledge
Activity
Configuration
System
Migration Center
Contributors & Commits
```

可选后续：

```text
Design Center
Trace Graph
Impact Graph
Memory / Prompt Learning
```

每个页面必须通过 Registry / Schema / Project Profile 动态渲染，禁止把具体项目业务字段写进 WebUI Core。

`Contributors & Commits` 只展示/维护贡献身份投影：

```text
Git Identity (READ_ONLY)
Optional display_name / status / note
Commit History
Workflow / Change / Batch / Client Provenance
```

它不建立 Banyan 登录账号，不追踪物理操作者，也不允许通过 Profile 状态改写 Git 历史或绕过权限。

---

## 14.1 多轴状态与进度模型

一个 Batch / Milestone 不能只使用“一个状态 + 一个百分比”。

至少分离：

```text
Lifecycle Status
Health
Implementation Progress
Integration Progress
Test Execution Progress
Test Pass Rate
Acceptance Progress
Closure Progress
Release Readiness
Freshness
```

### 14.1.1 Lifecycle Status

示例：

```text
PLANNED
READY
IN_PROGRESS
CODE_COMPLETE
TESTING
INTEGRATING
ACCEPTANCE
READY_TO_CLOSE
CLOSED
BLOCKED
```

状态回答：

> 现在处于生命周期哪一站？

### 14.1.2 Health

示例：

```text
ON_TRACK
AT_RISK
BLOCKED
UNKNOWN
```

Health 可由：

```text
Blocker
Failed Test
Stale Decision
Missing Evidence
Dependency Failure
```

计算。

### 14.1.3 Implementation Progress

必须由 Work Breakdown + Weight + Evidence 计算。

禁止 AI 凭感觉输出百分比。

例如：

```text
Σ（Work Item Weight × Work Item Progress）
÷
Σ（Work Item Weight）
```

没有可靠 Work Breakdown：

```text
N/A
```

优于伪造精确数字。

### 14.1.4 Test Execution 与 Test Pass 必须分开

```text
Test Execution
=
Executed / Planned

Test Pass Rate
=
Passed / Executed
```

禁止合并成一个含义不清的“测试进度”。

### 14.1.5 Closure Progress

收口单独显示，例如：

```text
Code Complete
Tests Passed
Acceptance
CR Reconciled
Canonical Docs Synced
Trace Updated
Project Guide Synced
Evidence Complete
```

因此允许出现：

```text
Implementation = 100%
Closure = 60%
```

这不是冲突，而是更真实。

### 14.1.6 Progress Source

所有进度必须标明：

```text
EVIDENCE
CALCULATED
MANUAL
UNKNOWN
```

手工填写的进度不得伪装成 Evidence-based。

---

## 14.2 Activity、Event 与 Freshness

Activity 不等于 Progress。

例如：

```text
Commit Count
Changed Files
PR
AI Runs
CLI Commands
```

只能作为活动观测，不能直接换算开发完成度。

建议事件：

```text
BATCH_STARTED
WORK_ITEM_COMPLETED
SEMANTIC_COMMIT_PLANNED
GIT_COMMIT_CREATED
TEST_STARTED
TEST_PASSED
TEST_FAILED
DECISION_CREATED
DECISION_APPLIED
CHANGE_CREATED
CHANGE_CANONICAL_APPLIED
UI_SPEC_UPDATED
BLOCKER_CREATED
BLOCKER_RESOLVED
BATCH_ACCEPTED
RELEASE_CREATED
```

区分：

```text
Canonical Event
Telemetry Event
```

Event Store 不得成为新的业务真源。

所有动态卡片建议显示：

```text
Last Evidence
Last Index
Git HEAD
Context Freshness
```

避免用户把过期数据当当前状态。

---

## 14.3 WebUI 字段权限模型

所有 UI 字段必须声明以下一种：

```text
EDITABLE
CONTROLLED_EDIT
ACTION_ONLY
READ_ONLY
SECRET
```

### EDITABLE

可直接保存的项目配置，例如：

- Display Name；
- Description；
- Locale；
- Timezone；
- 非治理型标签。

### CONTROLLED_EDIT

可改，但必须显示影响并经过 Banyan Command / Decision / Governance，例如：

- Governance Mode；
- Source Mapping；
- Protected Paths；
- Framework Version；
- Capability Enablement；
- Project Override。

### ACTION_ONLY

不能直接改状态值，只能执行受控动作，例如：

- Start Batch；
- Mark Code Complete；
- Request Acceptance；
- Close Batch；
- Archive Change；
- Rebuild Index。

### READ_ONLY

系统推导或观测值，例如：

- Git Branch / HEAD；
- Implementation Progress；
- Test Pass Rate；
- Acceptance Progress；
- Closure Progress；
- Blockers；
- Evidence Count；
- Core Purity；
- Freshness。

### SECRET

只显示：

```text
Configured
Missing
Invalid
```

禁止回显密码、Token、API Key 原值。

---

## 14.4 Explanation Contract

所有：

```text
Page
Section
Card
Field
Action
Status
Metric
```

都必须具备解释元数据。

推荐至少：

```yaml
id:
label:
type:
description:
purpose:
source:
editable_mode:
allowed_values:
calculation:
how_it_changes:
impact:
does_not_mean:
security:
```

UI 上必须能通过说明入口回答：

```text
这是什么
有什么用
数据来自哪里
能不能改
怎么改变
改了影响什么
它不代表什么
```

没有 Explanation Contract 的新控件不得进入正式 Control Plane。

---

## 14.5 Project Initialization Wizard

这里的 Wizard 只属于 Control Plane **UI/Command Orchestration**；New/Existing/Migrate 的语义、Source Mapping、Project Instance Bootstrap 与 Legacy Variable Migration Contract 仍由 Stage 04 拥有，Stage 16 不重新定义。

Control Plane 对未接入 Banyan 的项目提供 Wizard：

```text
Step 1 接入方式
Step 2 READ_ONLY Project Discovery
Step 3 Source Mapping
Step 4 Project Profile
Step 5 Capability Profile
Step 6 Governance / Permission
Step 7 Init / Migration Preview
Step 8 Result / Health Report
```

第一步不得直接展示几十个变量表单。

项目扫描应识别：

```text
Git
Structure
Language
Framework
Build
Tests
CI/CD
Documentation
AI Rules
OpenSpec
Existing Governance
```

识别结果应显示：

```text
Evidence
Confidence
```

初始化前必须明确列出：

```text
Will Create
Will Modify
Will Not Touch
```

已有 Banyan Project Instance 时，不再显示“初始化”，改为：

```text
Re-scan
Repair
Upgrade Framework
Migration Status
Rebuild Index
Drift Check
```

---

# 15. 改造全过程的安全迁移与 Activation 模式

所有高风险改造统一遵循：

```text
Inventory
↓
Snapshot
↓
Hash
↓
Mapping
↓
Copy / Generate
↓
Validate
↓
Dual Read / Dual Run
↓
Cutover
↓
Observe
↓
Rollback Test
↓
Retire Legacy Entry
```

## 15.1 禁止方式

```text
直接 mv 整个目录
直接删旧规则
直接把旧 Prompt 替换成新框架
直接将 Markdown 导入 DB 后删除 Markdown
直接让 Cursor 使用未验证的新规则
直接同时切 Cursor + Codex + Claude
```

---


## 15.2 Capability Activation Mode

Capability Lifecycle 描述“能力做到了哪种成熟度”，Activation Mode 描述“它当前是否允许接管真实项目”。

统一采用：

```text
OFF
SHADOW
GUARDED
ACTIVE
```

含义：

- `OFF`：未启用；
- `SHADOW`：只观察/计算/对比，不拥有真实写入权；
- `GUARDED`：可在旧治理门禁或人工确认保护下执行有限写入；
- `ACTIVE`：已经通过对应 Gate，可作为正式运行路径。

硬约束：

- Stage 05/06 早期实现的 Workflow / Change Runtime 默认不得直接 `ACTIVE`；
- Stage 05 定义的 Semantic Commit Workflow / Policy 在 Stage 14 Safety Gate 与 Stage 15 Commit Execution 完成前不得 `ACTIVE`；
- Stage 14 Governance Check 未完成前，新写路径只能 `SHADOW` 或通过 Legacy Gate 的 `GUARDED`；
- Stage 17 Cursor Pilot 通过前，不允许把当前主力开发入口完全切到新 Adapter；
- Stage 19 确认技术上可进入 Release Candidate 的 `ACTIVE` 能力集合；Stage 20 文档/采用 Gate 通过后才发布 Final Release。

---

# 16. Capability Lifecycle、Refactor Trace 与 Core Purity

## 16.1 Capability Lifecycle State

为了避免“规范已经写完”被误认为“能力已经能运行”，所有跨阶段核心能力必须具有明确生命周期：

```text
PROPOSED
↓
DEFINED
↓
IMPLEMENTED
↓
INTEGRATED
↓
VERIFIED
↓
RELEASED
```

含义：

- `DEFINED`：Schema、Policy、接口和行为已经设计完成；
- `IMPLEMENTED`：已有实际代码/模板/CLI/生成器实现；
- `INTEGRATED`：已接入 Project Instance / Runtime / Adapter；
- `VERIFIED`：通过对应测试与 Evidence；
- `RELEASED`：通过 Stage 19 技术验收与 Stage 20 Documentation/Adoption Gate，并进入正式 Framework Version。

阶段文档必须声明自己负责把某个能力推进到哪个状态。

例如：

```text
OpenSpec Governance Gate
Stage 06 → DEFINED
Stage 14 → IMPLEMENTED / INTEGRATED
Stage 19 → VERIFIED
Stage 20 → RELEASED
```

Semantic Commit / Commit Provenance
Stage 03 → Schema DEFINED
Stage 05 → Workflow / Policy DEFINED
Stage 11/13 → Index / Evidence IMPLEMENTED
Stage 14/15 → Safety + Execution IMPLEMENTED / INTEGRATED
Stage 17/18 → Cross-editor Pilot VERIFIED
Stage 19 → VERIFIED
Stage 20 → RELEASED
```

禁止阶段 06 因为“设计完成”就宣称运行时 Gate 已落地。

---

## 16.2 全局改造追踪矩阵

最终正式 Project Instance 冻结后，框架改造状态与跨阶段能力追踪的 Canonical Path 为：

```text
.banyan/migrations/MIGRATION_REGISTER.yaml
.banyan/migrations/BANYAN_REFACTOR_TRACE.yaml
```

但 Stage 00～Stage 02/04 尚未冻结最终 Project Instance 目录时，允许在 `REFRACTOR_CONTROL_ROOT` 下使用 **Bootstrap Register / Bootstrap Trace**。目录冻结后必须执行一次受控迁移：

```text
Bootstrap Register / Trace
→ hash + lineage
→ canonical .banyan/migrations/*
→ validate
→ bootstrap copy 归档为 reference
```

禁止 Bootstrap 与正式 `.banyan/migrations/*` 同时成为可独立更新的双真源。

其职责是回答：

> 总纲中的每一个 Framework Requirement 最终由谁设计、谁实现、谁验证、证据在哪里。

建议至少记录：

```yaml
requirement_id:
description:
scope:
owner_stages:
design_artifacts:
implementation_artifacts:
validation_artifacts:
evidence:
capability_state:
activation_mode:
status:
```

阶段完成不能只看 Stage 是否 `COMPLETED`，还必须检查其负责的 Requirement 是否达到目标 Capability State。

---

## 16.3 Core Purity Gate

必须建立机器可检查的 Core Purity Gate。

扫描对象：

```text
Framework Core
Generic Schemas
Generic Skills
CLI
Generic Adapter Sources
Generic Templates
```

禁止出现未显式允许的：

```text
具体项目名
项目专属目录
业务模块名
业务页面名
项目专属角色
项目专属 API / 端口 / 域名
项目专属 PRD / DEC / REQ ID
项目专属业务状态和业务规则
```

发现后默认：

```text
CORE_PURITY = FAIL
```

允许存在的项目示例只能位于：

```text
examples/
fixtures/
reference-projects/
tests/fixtures/
```

并必须清楚标记：

```text
REFERENCE ONLY
NOT CORE POLICY
```

---


## 16.4 Cross-stage Plan Change

后续阶段如果发现上游设计、Schema、Owner 边界或阶段输出存在错误，禁止直接静默修改历史阶段文档。

必须形成逻辑上的：

```text
REFRACTOR_PLAN_CHANGE
```

实际文件名/ID Schema 在阶段 03 冻结。

至少记录：

```text
trigger_stage
affected_upstream_stage
reason
old_contract
proposed_contract
impact
migration_effect
rollback_effect
trace_updates
approval
```

处理顺序：

```text
发现问题
→ 记录 Plan Change
→ Impact Analysis
→ 更新 Owner Stage 的 Canonical Contract
→ 更新受影响 Stage Manifest / Trace
→ 必要时重新验证下游
→ 继续施工
```

这保证“允许迭代”与“不能静默漂移”同时成立。

---


# 16A. Banyan Usage Documentation Publishing Contract

最终使用说明是：

```text
Verified Framework Capability
→ Documentation Projection
```

不是：

```text
使用说明
→ 反过来定义 Framework Behavior
```

因此最终说明文档必须遵守：

1. 所有行为描述来源于 `VERIFIED` Capability；
2. Command / Field / State / Schema Reference 优先从 Registry / Schema / CLI 自动生成；
3. WebUI 字段说明复用 Explanation Contract；
4. 示例必须绑定明确 Framework Version；
5. 截图/命令/路径必须经过最终 Release Candidate 验证；
6. 使用说明发现实现与规范不一致时，不允许“以文档为准”直接改口径，必须走 `REFRACTOR_PLAN_CHANGE`；
7. Documentation Pack 自己不是业务真源，也不是 Core Policy 真源。

Stage 20 必须生成：

```text
DOCUMENTATION_SOURCE_MAP
DOCUMENTATION_COVERAGE_REPORT
DOCUMENTATION_DRIFT_REPORT
```

每篇文档至少追踪：

```yaml
doc_id:
audience:
framework_version:
capabilities:
commands:
schemas:
ui_routes:
evidence:
generated_references:
last_verified:
```

---

# 17. Stage Delivery Pack 与阶段文档治理

后续 00～20 的每个阶段，不再默认只生成“一份超级施工文档”。

统一采用：

```text
Stage
├── STAGE_MANIFEST.yaml               # 机器可读阶段契约
├── STAGE_PLAN.md
├── PRECHECK_AND_SCOPE.md
├── EXECUTION_RUNBOOK.md              # 复杂阶段必须
├── VALIDATION_AND_ROLLBACK.md
├── XX-A_专项子指导.md                # 按需
├── XX-B_专项子指导.md                # 按需
├── MIGRATION_MAP.md                  # 有迁移时必须
├── COMPATIBILITY_MATRIX.md           # 有兼容时必须
├── DATA_RECONCILIATION.md            # 有结构化数据迁移时必须
└── ACCEPTANCE_REPORT.md              # 阶段施工完成后生成
```

## 17.1 各类文档职责


### `STAGE_MANIFEST.yaml`

每个阶段必须有一个机器可读 Manifest，至少声明：

```yaml
stage_id:
title:
prerequisites:
owned_capabilities:
consumed_capabilities:
target_capability_state:
activation_mode:
required_inputs:
planned_artifacts:
conditional_artifacts:
protected_paths:
required_upstream_artifacts:
handoff_outputs:
charter_compatibility:
entry_gate:
exit_gate:
```

它回答“这个阶段需要什么、负责什么、交付什么”，但**不作为阶段实时状态真源**；实际状态仍以全局 `MIGRATION_REGISTER.yaml` 为准。

### `STAGE_PLAN.md`

阶段总调度文件，只负责：

- 阶段目标；
- 为什么现在做；
- 输入；
- 前置门禁；
- 允许/禁止范围；
- 子指导调用顺序；
- 预期产物；
- 完成条件；
- 下一阶段准入。

不得塞入所有领域细节。

### `PRECHECK_AND_SCOPE.md`

负责：

- 真实仓库盘点；
- 当前版本/Commit；
- 现有文件；
- Protected Paths；
- 可修改范围；
- 不可修改范围；
- 已发现风险；
- 本阶段实际适用性。

必须先于写入施工。

### `EXECUTION_RUNBOOK.md`

只描述**这一次施工怎么分刀执行**。

至少包含：

```text
Step
Inputs
Files To Read
Files Allowed To Write
Expected Diff
Validation
Stop Condition
Rollback Point
```

不把抽象架构原则重复抄一遍。

### `VALIDATION_AND_ROLLBACK.md`

负责：

- 正向验收；
- 数据完整性；
- 兼容性；
- 重建测试；
- 回滚命令/步骤；
- 回滚后再验证；
- 阶段是否可安全进入下一步。

### 专项子指导

一个专项只解决一个复杂问题。

例如：

```text
08-A_PRD_UI职责与冲突裁决
08-B_Design_Revision
08-C_UI_SPEC版本治理
```

专项子指导可以被其它阶段引用，但只能有一个正式维护源。

### `MIGRATION_MAP.md`

存在旧目录、旧文件、旧规则、旧 ID、旧索引迁移时强制生成。

至少记录：

```text
old_path / old_id
new_path / new_id
action
compatibility
reference_impact
validation
rollback
```

### `COMPATIBILITY_MATRIX.md`

存在多编辑器、多版本、旧新入口或不同 Schema 时强制生成。

### `DATA_RECONCILIATION.md`

涉及 SQLite、批量索引、结构化历史导入时强制生成。

### `ACCEPTANCE_REPORT.md`

由实际施工结果生成，不得提前伪造。

记录：

```text
实际修改
实际未修改
校验结果
失败项
偏差
回滚测试
Evidence
最终状态
NEXT_STAGE_HANDOFF
```

---

## 17.2 阶段文档拆分准则

满足以下任一条件时，阶段主文档必须拆专项子指导：

1. 存在独立 Schema。
2. 存在独立数据迁移。
3. 存在独立版本模型。
4. 存在独立兼容矩阵。
5. 存在独立回滚路径。
6. 存在独立验收模型。
7. 一个主题需要被多个阶段重复引用。
8. 一个主题拥有独立 Source of Truth。
9. 一个主题涉及多个工具/编辑器实现差异。
10. 单章节继续增长会导致 Codex 必须加载大量无关规则。

反之，以下内容不应为了“形式完整”机械拆文档：

- 三五条局部约束；
- 只被当前 Step 使用的一次性说明；
- 没有独立验证和复用价值的细节。

核心原则：

> **按认知边界和验证边界拆，不按章节数量拆。**

---

## 17.3 五层改造文档体系

以后整个 Banyan 改造工程固定为：

```text
L0  总纲
    榕树AI多编辑器AI软件工程框架改造总纲

L1  阶段主指导
    00～20 STAGE PLAN

L2  专项子指导
    XX-A / XX-B / XX-C ...

L3  实际施工计划
    Runbook / Migration Map / Compatibility / Validation Plan

L4  实际施工证据
    Manifest / Diff / Reconciliation / Report / Acceptance / Evidence
```

职责：

```text
L0-L2 = 应该怎么做
L3    = 这一次具体怎么施工
L4    = 实际做成了什么
```

禁止把 L4 的“实际结果”提前写进 L1/L2 当成已经完成。

---

## 17.4 阶段改造状态真源

为 Banyan 框架改造本身维护独立 Stage State Register。

最终 Canonical Path：

```text
.banyan/migrations/MIGRATION_REGISTER.yaml
```

在 Stage 00～Project Instance 路径尚未冻结期间，可以使用 `REFRACTOR_CONTROL_ROOT` 下的 Bootstrap Register；一旦正式路径冻结，必须按第 16.2 节执行 lineage-preserving migration，之后只保留一个可写真源。

它只记录**框架改造工程进度**，不替代：

```text
docs/project/progress/**
```

业务项目自身进度。

建议字段：

```yaml
stage:
status:
baseline_commit:

sub_stages:
  XX-A:
  XX-B:

planned_artifacts:
actual_artifacts:

validation:
rollback_point:
open_risks:
next_gate:
```

状态示例：

```text
NOT_STARTED
PRECHECK
READY
IN_PROGRESS
VALIDATING
BLOCKED
COMPLETED
ROLLED_BACK
```

---


## 17.5 Stage Handoff Contract

阶段完成时必须同时满足：

```text
Stage Validation PASS
+
Acceptance Report 已生成
+
MIGRATION_REGISTER 已更新
+
BANYAN_REFACTOR_TRACE 已更新
+
实际 Artifact / Evidence 已登记
+
Rollback Point 可用
+
Next Stage Entry Gate 满足
```

禁止仅因为“文件已经生成”就进入下一阶段。

每个真实 `ACCEPTANCE_REPORT.md` 必须包含：

```text
NEXT_STAGE_HANDOFF
- upstream stage / run id
- actual artifacts to consume
- evidence to trust
- unresolved risks
- protected/allowed scope changes
- rollback point
- next entry gate result
```

下游 Stage 优先消费这份 Handoff，而不是重新猜上游输出位置。

## 17.5A Stage Pack / Charter Compatibility

总纲版本提升后，不机械要求所有已生成 Stage Pack 重做。

只有以下情况才必须重生/补丁：

```text
Owner Contract 改变
Required Input / Output 改变
Gate 改变
Safety Boundary 改变
Schema / Migration Contract 改变
```

如果只是后续 Stage 新增横切能力、且当前 Stage Contract 未变化，可以记录：

```text
COMPATIBLE_WITH_NEWER_CHARTER
```

当前已生成的 `Stage_00_改造安全基线与仓库保护` v1.8 Pack 与 v1.9.1 **兼容**：v1.9 的 Git Identity / Semantic Commit 能力从 Stage 01 起进入施工链，不改变 Stage 00 的 Repository Baseline、Protected Paths、Discovery Scope、Checkpoint 与 Rollback Contract，因此不需要重新生成 Stage 00 Pack。

---

## 17.6 计划文档与执行结果严格分离

施工前可以生成：

```text
STAGE_MANIFEST
STAGE_PLAN
专项子指导
PRECHECK 模板
RUNBOOK 模板
VALIDATION / ROLLBACK 方案
```

真实施工后才允许形成：

```text
实际 Inventory
实际 Diff
实际 Reconciliation
实际 Migration Result
实际 Test Result
Evidence
ACCEPTANCE_REPORT
```

不得在施工指导里提前伪造“已完成”。

---

# 18. 00～20 总体改造阶段

后续每个阶段生成一套 Stage Delivery Pack，并且一次只实施一个阶段。

---


## 18.0 阶段施工包适用规则

所有阶段统一遵循第 17 节 Stage Delivery Pack。

施工前必须生成：

```text
STAGE_MANIFEST.yaml
STAGE_PLAN.md
PRECHECK_AND_SCOPE.md
VALIDATION_AND_ROLLBACK.md
```

真实施工完成后必须生成：

```text
ACCEPTANCE_REPORT.md
```

涉及复杂写入/迁移的阶段再根据第 25 节权威清单生成：

```text
EXECUTION_RUNBOOK.md
MIGRATION_MAP.md
COMPATIBILITY_MATRIX.md
DATA_RECONCILIATION.md
专项子指导
```

**第 25 节是 00～20 专项文档文件名的唯一权威清单。**

如果某个已列出的条件型专项经真实 Precheck 证明不适用：

```text
STAGE_MANIFEST
→ NOT_APPLICABLE
→ reason
```

不得私自删除职责、另造同义文档或生成空壳文档。

---

## 阶段 00：改造安全基线与仓库保护

建议文档：

`00_改造安全基线与仓库保护.md`

目标：

- 读取真实仓库；
- 固化 Commit、分支、目录和已有治理状态；
- 建立 Protected Paths；
- 建立全量**受管范围**文件 Hash / Inventory，并记录排除范围；
- 建立迁移前 Manifest；
- 建立可恢复 Checkpoint。

门禁：

> 未完成安全基线，不进入任何迁移。


安全基线必须同时记录 Discovery Coverage：

```text
Git tracked
相关 untracked
明确受治理的 ignored paths
AI / docs / tools / editor config roots
```

以下内容可以排除正文扫描，但必须记录排除理由：

```text
vendor
node_modules
build/dist/cache
大体积二进制
Secret / Credential 内容
```

Secret 默认只记录存在性和路径策略，不在 Inventory 中泄露原值。

---

## 阶段 01：AI 资产全量盘点与方案裁剪

建议文档：

`01_AI资产全量盘点与方案裁剪.md`

本阶段的权威专项清单见第 25 节；v1.9.1 继承并冻结 `01-I_Git_Identity与AI提交现状盘点.md`。

已知 Seed Inputs（仅用于启动发现，不代表完整清单）：

```text
v3.1 两份主文档
.cursor/rules
.cursor/skills
tools
docs/project
docs/temp
docs/agreements
plain-spec / plain-document
全部 UI 方案
OpenSpec 候选接入点
```

统一标记：

```text
KEEP
MERGE
SPLIT
REWRITE
REFERENCE
LEGACY
IGNORE
```

并归类到：

```text
ROLE
POLICY
SKILL
WORKFLOW
STATE
PROFILE
TEMPLATE
PROJECT_FACT
TOOL
ADAPTER
CHANGE_ARTIFACT
PUBLISHING_ARTIFACT
```


新增硬性盘点对象：

```text
Legacy AI Capability
AI Generated Canonical Artifact
AI Generated Derived Artifact
Operational Artifact
Legacy Governance Behavior
```

必须以 Codex 真实仓库 Full Discovery 为准，不允许只按总纲已知目录清单盘点。

Stage 01 Exit Gate 额外要求：

```text
AI Capability Discovery 完成
AI Generated Artifact Inventory 完成
Operational Artifact Inventory 完成
所有未知项进入 UNCLASSIFIED，而不是静默忽略
```


Stage 01 必须生成**初版 No-Loss Coverage**，不能等 Stage 07 才第一次做映射：

```text
PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX
PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX
DISCOVERY_COVERAGE_REPORT
```

每个高价值 Legacy Capability 至少先得到：

```text
candidate_owner_stage
candidate_target_capability
candidate_action
confidence
open_question
```

每个 Canonical Artifact 至少先得到：

```text
candidate_source_role
keep_or_migrate
integrity_risk
```

Stage 01 Exit Gate：

```text
SILENTLY_IGNORED_ASSET = 0
UNSCANNED_GOVERNANCE_ROOT_WITHOUT_REASON = 0
HIGH_RISK_UNCLASSIFIED = 0
```

普通 `UNCLASSIFIED` 可以存在，但必须登记 Owner Candidate / 下一阶段处理计划，不能消失。

同时盘点现有 Git 协作事实：

```text
历史 Git Identity（Author name + email）
Commit Message 约定与常用 type/scope
已有 Commit Hook / Script / CI Check
已有 AI Commit Rule / Prompt / Skill
是否存在自动分批提交习惯或脚本
现有 commit trailer / issue / PR 关联方式
```

Stage 01 只做 Discovery，不在此阶段冻结最终 Commit Policy。

---

## 阶段 02：Banyan 目标架构与目录正式冻结

建议文档：

`02_Banyan目标架构与目录定稿.md`

本阶段的权威专项清单见第 25 节；v1.9.1 继承并冻结 `02-G_Contribution_Identity与Commit_Provenance架构.md`。

冻结的重点不是强迫所有项目使用相同物理目录，而是冻结：

- Banyan Framework Distribution 与 Project Instance 的边界；
- Project Instance 最小目录与配置契约；
- Source Role 语义；
- Registry；
- Runtime；
- Index；
- Memory；
- Adapter；
- Migration；
- Publishing；
- Control Plane 接口边界；
- Source of Truth 优先级模型；
- 可选 Change Provider 接口（OpenSpec 只是实现之一）；
- Generic Skill 与 Project/Domain Skill 的边界。

当前 Reference Project 的：

```text
tools/
docs/
openspec/
.cursor/
```

只在本项目 Migration Mapping 中记录，不升格为所有项目必须采用的 Core 物理目录。


Stage 02 必须消费 Stage 01 的初版 Preservation / Migration Coverage。

架构冻结前必须完成：

```text
Legacy Capability
→ Core / Project / Provider / Compatibility / Retirement Candidate

Canonical Artifact
→ Source Role / Preservation Strategy
```

Architecture Coverage Gate：

```text
UNOWNED_VALUABLE_CAPABILITY = 0
CANONICAL_ARTIFACT_WITHOUT_TARGET_ROLE = 0
UNKNOWN_CORE_VS_PROJECT_BOUNDARY = 0
```

如果 Stage 01 发现总纲没有预见的新高价值能力：

```text
先纳入 Capability Ownership
→ 再冻结 Architecture
```

禁止先冻结架构、到 Stage 07 才发现 Banyan 根本没有承接位置。

本阶段同时冻结 Collaboration / Provenance 架构边界：

```text
Git Identity = Contribution Identity
Contributor Profile = Optional Projection
Execution Client = Attribution only
Workflow/Task/Change/Batch = Work Context
Git = Commit Truth
Banyan Trace = Semantic Relation
```

并明确：不建立人员职位体系、不建立编辑器业务职责体系、不把 Profile 当认证/权限系统。

---

## 阶段 03：AI Artifact 契约、Schema 与 Registry

建议文档：

`03_AI产物契约Schema与Registry.md`

本阶段的权威专项清单见第 25 节；v1.9.1 继承并冻结 `03-I_Git_Identity_Contributor_Profile与Commit_Provenance_Schema.md`。

定义：

- Role；
- Policy；
- Skill；
- Workflow；
- Workflow Family；
- Workflow Atom；
- Workflow Node Contract；
- State；
- Profile；
- Adapter；
- Memory Pattern；
- Change Artifact；
- Publishing Artifact；

的统一元数据、自解释注释、版本、依赖、权限和加载规则。

本阶段只冻结 Adaptive Workflow 所需的结构契约；真正的 Workflow Composer / Runtime / Reconciliation 在阶段 05 实现。

---

## 阶段 04：Project Instance、Source Mapping 与 Profile

建议文档：

`04_Project_Instance_Source_Mapping与Profile.md`

本阶段的权威专项清单见第 25 节；v1.9.1 继承并冻结 `04-G_Contributor_Profile与Git_Identity_Discovery.md`。

目标：

- 定义 Framework Distribution 与 Project Instance 的连接方式；
- 定义 `framework.lock` / Framework Version Pin；
- 定义 Source Role → 真实目录/系统的映射；
- 定义 Project Profile；
- 定义 Project Override；
- 定义 Generic / Domain / Project Skill 的边界；
- 当前 Reference Project 只作为第一套映射实例；
- 定义 `Initialize New Project / Adopt Existing Project / Migrate Existing Governance`；
- 定义 Project Instance Bootstrap；
- 定义 Legacy Variable Migration 分类与 Migration Map；
- 已有项目不得被错误重置为新项目。

必须证明：

```text
换一个目录结构完全不同的项目
↓
只修改 Project Instance Mapping
↓
Banyan Core 无需修改
```

本阶段负责 Project Instance 中的 Contributor Profile Registry：

- 从 Git 历史发现 Git Identity；
- 不自动创建“真人账号”；
- 未配置 Profile 的身份直接使用 Git name/email；
- Profile 仅保存 `display_name / status / note` 等可选资料；
- 不保存 `role_labels`、固定模块、前端/后端职责；
- 不自动合并多个 Git Identity；
- 最终物理文件位置由 Stage 04 冻结，不写进 Banyan Core 业务规则。

---

## 阶段 05：Adaptive Workflow Orchestrator、Interaction 与 Decision Routing

阶段主文档：

`05_Adaptive_Workflow_Orchestrator与决策路由.md`

本阶段属于**核心复杂阶段，强制拆专项子指导**：

```text
05-A_Task_Classification与Delta_Detection.md
05-B_Workflow_Atom与Workflow_Composer.md
05-C_Workflow_Family_Catalog.md
05-D_Workflow_Graph_Node_Contract与Runtime_State.md
05-E_ReRoute_Escalation_DeEscalation与Reconciliation.md
05-F_Decision_Interrupt_Pause_Resume与Partial_Blocking.md
05-G_Experiment_Mode与Candidate_Delta.md
05-H_Dependency_Invalidation与Checkpoint.md
05-I_Workflow_Governance_Confidence与Evidence.md
05-J_Adaptive_Workflow验收场景集.md
05-K_Parallel_Draft_Workspace_Runtime.md
05-L_Semantic_Commit_Planner与Batch_Commit_Workflow.md
```

核心组件：

```text
Task Classifier
Context Requirement Resolver Interface
Delta Classifier
Change Necessity Engine
Decision Necessity Engine
Decision Risk Classifier
Impact Assessment Interface
Workflow Composer
Workflow Runtime
Re-route Trigger Detector
Workflow Re-router
Workflow Reconciliation Engine
Dependency / Invalidation Engine
Checkpoint / Resume Manager
Context Provider Interface
Governance / Permission Gate Interface
```

职责边界：Stage 05 只定义 Context / Impact / Governance 的**调用接口和 Workflow 需求**；真正的 Context Builder 由 Stage 12、Impact/Evidence Engine 由 Stage 13、Governance Check Runtime 由 Stage 14 实现。Stage 05 不提前复制这些 Owner Stage 的实现。

必须冻结：

```text
AUTO
ASK_ONCE
CONFIRM_ONCE
CONFIRM_TWICE
CROSS_DOMAIN_CONFIRM
```

并定义：

```text
Project Governance:
LIGHT / STANDARD / FULL

Task Execution Profile:
FAST / NORMAL / CONTROLLED

Workflow Confidence:
HIGH / MEDIUM / LOW
```

本阶段必须证明：

- G0～G11 已降级为项目生命周期/Compatibility，不再强迫日常任务逐阶段执行；
- Workflow 可由 Atom 动态组合；
- Workflow Runtime 使用 Graph，不只支持线性 Step；
- 运行中可以 Branch / Pause / Resume / Loop / Retry / Skip / Replace；
- 子流程结束后必须 Reconcile；
- 支持 Escalation 与 De-escalation；
- 支持 Decision Interrupt 和局部 Work Item Blocking；
- 支持 Experiment Accept / Discard；
- 高风险/低置信度 Re-route 不得自动越权；
- Re-route 只重新加载受影响 Context；
- 每次重规划有 Trigger、Evidence、Trace 和 Resume Point。

`05-J` 必须至少覆盖以下验收：

```text
开发中发现缺失规则 → 插 DEC → 继续原工作
开发中 DEC 改变核心输入 → 原节点 Invalidated → Replace
一个 Batch 只有一个 Work Item 被决策阻塞 → 其它继续
UI Visual Repair → Experiment → Discard → 回原流程
UI Visual Repair → Experiment → Accept → 正式 UI Change
视觉调整检测出业务行为变化 → FAST 升 CONTROLLED
用户说新增功能 → 发现 PRD 已存在 → NORMAL 降 FAST
Test Fail → Repair Branch → 回 Test
Data Migration 发现脏数据 → Audit/Clean Branch → Reconcile
Release Preflight Fail → Repair → 回 Release
```



Stage 05 必须纳入 `Parallel Draft Workspace` 的 Runtime 行为：

```text
CREATE_DRAFT_WORKSPACE
CAPTURE_DRAFT
REFRESH_CANONICAL
RECONCILE_DRAFT
PROMOTE_DRAFT
DISCARD_DRAFT
```

并保证 Draft Workspace：

- 不改变 Project Lifecycle；
- 默认 `NON_CANONICAL`；
- 默认 `READ_ONLY` 读取正式真源；
- 不获得正式编号；
- Promote 时才进入正式 Change / Decision 路径。

Stage 05 对 Semantic Commit 的目标状态是：

```text
Workflow / Commit Message Policy = DEFINED
Activation = OFF / SHADOW
```

本阶段不得把真实 Git Commit Execution 宣称为已经正式接管；真实 Safety Gate 属于 Stage 14，CLI/API/Adapter Commit Execution 属于 Stage 15。

Stage 05 同时定义 `SEMANTIC_COMMIT` Workflow Family/Atom：

```text
Detect Working Tree
→ Semantic Diff Classification
→ Commit Group Planning
→ Risk / Secret / Protected Path Check
→ Stage Hunks / Files
→ Validate
→ Commit
→ Capture Commit Object
→ Evidence / Trace
→ Remaining Work Reconciliation
```

它必须支持“积累很多修改后让 AI 合理分批提交”的场景，并且不建立编辑器专属提交逻辑。

---

## 阶段 06：Change Workspace Provider、OpenSpec 参考集成与 Canonical Apply

建议文档：

`06_Change_Workspace_Provider_OpenSpec与Canonical_Apply.md`

明确：

- Banyan Core 定义 Change Workspace Provider Contract；
- OpenSpec 作为首个参考/首选 Provider 集成，不作为 Core 强制依赖；
- `banyan-change` 自定义 Schema；
- Proposal / Delta / Impact / Tasks；
- Change 与 CR 的职责边界；
- Canonical Apply；
- Banyan Governance Gate Interface（本阶段定义接口，阶段 14 实现运行时）；
- Archive 前置条件；
- OpenSpec 状态与 Banyan 状态分离；
- Capability State 至少推进到 `DEFINED`；
- OpenSpec 不成为第二 PRD 真源。

同时定义：

```text
Discussion Pack
Final Review Pack
```

的 Artifact 契约。


本阶段必须新增两个通用 Contract：

### Parallel Draft Promotion Contract

```text
Draft Workspace
→ Refresh latest Canonical Truth
→ Reconcile
→ Conflict / Decision
→ Formal Change
→ Canonical Apply
```

### Batch Canonical Reconciliation Contract

Batch 收口时必须判断：

```text
PURE_IMPLEMENTATION
CANONICAL_ALREADY_UPDATED
BUSINESS_CHANGE_NOT_CANONICALIZED
CONFLICT
```

只有真正的业务语义变化进入 Canonical Change；纯实现不得污染 PRD。

---

## 阶段 07：Reference Project v3.1 超级提示词拆分与兼容层

建议文档：

`07_Reference_Project_v3.1超级提示词拆分与兼容层.md`

建立：

```text
v3.1
↓
Role / Policy / Skill / Workflow / State / Template
↓
Compatibility Loader
```

必须保留：

- G0～G11 生命周期语义，但明确降级为项目宏观生命周期 / Legacy Compatibility，不再作为每个 Task 的固定流水线；
- 知情决策核心安全原则；
- 编号保护；
- PRD / UI / Batch 门禁；
- 新窗口恢复；
- 已有项目续做能力。


Stage 07 不能只做结构拆分，必须执行 **Legacy Capability Preservation**。

至少逐项覆盖：

```text
v3.1 第 1～52 节
所有 A/B/C 补充节
各版本新增能力
所有独立手续
所有可选会话模式
所有安全保护规则
所有新窗口/交接/进度机制
```

必须明确验证并迁移：

```text
39A～39C 变更稿模式
36A Batch PRD 收口
编号占用保护
在引用规则保护
自测临时桩清理
禁止为验收修改业务口径
WORKLOG
HANDOVER
PROJECT_DASHBOARD
DEVELOPMENT_PROGRESS
DOCUMENT_PROGRESS
新窗口恢复
知情决策
G9.5 / UI 分闸
视觉修复循环
不同 PRD 状态下的变更写入语义
```

必须输出并建立持续更新责任：

```text
AI_CAPABILITY_PRESERVATION_MATRIX
AI_ARTIFACT_MIGRATION_MATRIX
LEGACY_BEHAVIOR_REGRESSION_MATRIX
```

Stage 07 负责把 Legacy 能力/产物**完整映射到目标 Owner/Action/Compatibility**，但不抢占后续领域 Stage 的具体迁移 Owner。例如 UI 历史产物由 Stage 09、Plain/Guide 由 Stage 10、历史索引由 Stage 11、Cursor 入口由 Stage 17 实施；这些 Stage 完成后必须回写全局 Migration Matrix。

Gate：

```text
UNMAPPED_VALUABLE_CAPABILITY > 0
→ FAIL

UNMAPPED_CANONICAL_ARTIFACT > 0
→ FAIL
```


职责边界：

> Stage 07 的任务是**执行、验证和收口 Reference Project 的 Legacy Migration**，不是第一次发现旧能力。

如果 Stage 07 又发现 Stage 01 漏掉的高价值能力：

```text
DISCOVERED_LATE_LEGACY_CAPABILITY
→ REFRACTOR_PLAN_CHANGE
→ 回补 Stage 01 Coverage
→ 回到对应 Owner Stage 补 Contract
→ 重验受影响 Stage
→ 再继续 Stage 07
```

不得为了赶迁移在 Stage 07 私自发明临时 Core 规则。

---

## 阶段 08：PRD × UI_SPEC 协同与 UI 版本治理

建议文档：

`08_PRD与UI_SPEC协同及UI版本治理.md`

冻结：

```text
PRD = Business Truth
UI_SPEC = UI Truth
Design Source = Evidence
Implementation Pack = UI施工图
Effective UI Contract = Batch UI Snapshot
```

完成：

- 页面 Coding Context；
- PRD/UI 冲突规则；
- 根决策一次确认；
- Design Revision；
- UI_SPEC SemVer；
- Design Diff Classification；
- Batch Version Lock；
- NEWER_UI_AVAILABLE；
- UI Contract 冻结和升级。

---

## 阶段 09：UI Design Intelligence 子系统整合

建议文档：

`09_UI_Design_Intelligence子系统整合.md`

整合：

```text
Core Protocol
Design Pack Schema
Layout Guidance
Implementation Compiler
Framework Adapter
Validation / Repair Loop
```

通过 Skill Registry 统一注册 UI Intelligence 工具。当前 Reference Project 的现有 `tools/anydesign`、`visual-repair-loop` 仅作为首批迁移对象，不成为 Core 固定路径。

保留现有历史 UI 产物兼容读取。

---

## 阶段 10：Project Knowledge Publishing 与 Reference Project Guide 迁移

阶段主文档：

`10_Project_Guide与知识发布体系改造.md`

本阶段属于**复杂阶段，强制生成专项子指导**。

### 强制审计输入

必须读取并逐条审计现有：

```text
白话文档生成方案.md
白话文档总体编写规划.md
分端页面相关文档编写方案.md
功能需求相关文档编写方案.md
技术设计相关文档编写方案.md
架构图相关文档编写方案.md
总览相关文档编写方案.md
plain-document文档地图编写说明.md
```

以及真实：

```text
docs/project/plain-spec/**
docs/project/plain-document/**
docs/project/progress/PLAIN_SYNC.yaml
docs/project/progress/PLAIN_SYNC_GAPS.md
```

每份旧规则/旧内容至少标记：

```text
KEEP
GENERALIZE
PROJECT_PROFILE
REWRITE
SUPERSEDE
MIGRATE
ARCHIVE
```

### 10-A：现有 Plain 体系审计与问题报告

文档：

`10-A_现有Plain体系审计与问题报告.md`

重点判断：

- 哪些规则已经成熟，应直接保留；
- 哪些规则只适用于当前 Reference Project；
- 哪些规则导致“PRD 白话摘要化”；
- 哪些固定目录/固定篇数已经限制 Reader-oriented 说明书；
- 哪些同步规则值得进入 Banyan Core；
- 哪些内容必须保留历史兼容。

### 10-B：Project Guide 信息架构设计

文档：

`10-B_Project_Guide信息架构设计.md`

从：

```text
按 PRD Module / 固定目录填格子
```

转为：

```text
Reader-oriented
Question-oriented
Scenario-oriented
Role-oriented
```

定义：

```text
Orientation
Concept Guide
How It Works
Role Guide
Application Guide
Rule Handbook
Technical Explanation
Troubleshooting
Architecture View
```

等文章类型。

### 10-C：Project Guide 编写规范

文档：

`10-C_Project_Guide编写规范.md`

统一：

- 写作目标；
- 读者；
- 信息密度；
- 白话程度；
- 事实与解释分离；
- 当前态/目标态；
- 禁止写成 PRD 摘要；
- 禁止把编号堆进正文；
- 跨文章去重；
- 图文协同；
- 长度与章节策略。

### 10-D：文章类型与模板规范

文档：

`10-D_Project_Guide文章类型与模板规范.md`

不同文章不得都套同一模板。

例如：

```text
How It Works
≠
Application Guide
≠
Rule Handbook
≠
Troubleshooting
```

每一种 Article Type 定义：

- 适用场景；
- 来源；
- 推荐骨架；
- 禁止内容；
- 示例；
- 验收标准。

### 10-E：GUIDE_SYNC 与来源图谱设计

文档：

`10-E_GUIDE_SYNC与来源图谱设计.md`

把旧：

```text
PRD File → Plain File
```

升级为：

```text
Canonical Facts
        ↓
Topic / Concept / Scenario
        ↓
One or More Guide Articles
```

支持多对多来源：

```yaml
guide:
sources:
update_when:
ignore_when:
last_synced:
source_hashes:
status:
```

本阶段先定义反向 Impact Query Interface 与 Canonical Relation Model；SQLite 加速实现留到阶段 11。

### 10-F：旧 Plain 文档迁移映射

文档：

`10-F_旧Plain文档迁移映射.md`

对现有 71 份规划及已经落地内容执行：

```text
KEEP
REWRITE
MERGE
SPLIT
RENAME
MIGRATE
ARCHIVE
```

必须保留旧路径映射、引用关系和回滚方式。

迁移验收前不得删除旧 `plain-spec/plain-document`。

### 10-G：Project Guide 质量验收规范

文档：

`10-G_Project_Guide质量验收规范.md`

验证至少包括：

- 是否像说明书，而不是 PRD 摘要；
- 新人是否能按阅读路径理解系统；
- 是否能回答“系统怎么工作/怎么使用”；
- 是否重复大量正式需求；
- 是否混入未确认事实；
- 是否存在跨篇矛盾；
- 是否正确反映当前已落地事实；
- 图是否真正提升理解；
- 是否只刷新受影响内容。

### 10-H：迁移回滚与旧体系退役方案

文档：

`10-H_Project_Guide迁移回滚与旧体系退役方案.md`

定义：

```text
旧体系继续可读
↓
新体系 Shadow
↓
Guide 对比验证
↓
增量同步验证
↓
Cutover
↓
观察期
↓
旧生成入口 Deprecated
```

旧内容是否最终移动目录，在真实迁移阶段决定，不在总纲提前强制。

### 阶段 10 最终目标

职责边界：Stage 10 的 Project Guide 是**项目本身的说明书/系统手册**；Stage 20 的 Usage Documentation 是**Banyan Framework 的使用说明**。两者不得复用同一真源或相互替代。

把现有：

```text
plain-spec
plain-document
PLAIN_SYNC
```

从“PRD 白话摘要机制”升级为：

```text
Project Guide / System Handbook
Project Guide Authoring Standard
Article Type Templates
Guide Map
GUIDE_SYNC
Guide Impact Analysis
Stale Detection
Incremental Regeneration
Quality Validation
```

旧资产必须保护性迁移。


---

## 阶段 11：SQLite 索引、Trace 与历史数据安全迁移

建议文档：

`11_SQLite索引Trace与历史数据迁移.md`

完成：

- Schema；
- Full Scan；
- ID Index；
- Decision Dependency；
- Change / PRD / UI / Batch Relations；
- GUIDE_SYNC / Publishing Relations；
- Code Trace；
- Rebuild；
- Integrity Check。

原则：

> Markdown/YAML/正式项目文件是真源；SQLite 必须可删除、可重建。

Git / Commit Provenance 额外要求：

```text
Git Commit Object
→ GitIdentity
→ Workflow / Task / Change / Batch / Client relations
→ Artifact / Code relations
```

SQLite 中的 Contributor / Commit 关系必须可从 Git + 持久化 Banyan Trace/Trailer 重建；SQLite 不成为第二 Git History。

---

## 阶段 12：动态 Context、记忆与 Token 优化

建议文档：

`12_动态Context记忆与Token优化.md`

实现：

```text
Task Detection
→ Profile
→ Role
→ Policy
→ Skill
→ Project Fact
→ Change Context
→ Trace
→ Runtime Context
```

目标：

- 不完整加载 5000+ 行大提示词；
- 新窗口快速恢复；
- Context 可解释；
- 不产生第二项目真源。


本阶段必须定义 Legacy HANDOVER → Session Recovery 的兼容：

```text
旧 Handover 中的未完成事项
→ Active Task / Workflow Resume Point
→ Pending Decision / Blocker / Next Action
```

不得因为新 Context Runtime 上线而丢失旧交接信息。

---

## 阶段 13：Evidence、Impact 与 Prompt Learning 闭环

建议文档：

`13_EvidenceImpact与Prompt学习闭环.md`

形成：

```text
Change
→ Canonical Truth
→ Implementation
→ Test
→ Acceptance
→ Evidence
→ Trace
→ Prompt Review
→ Lesson
→ Pattern
```

并支持：

- Impact Analysis；
- Code → Batch → Requirement 反向追踪；
- AI 完成声明证据化；
- Prompt 经验受控沉淀；
- Workflow Event / Re-route / Reconciliation / Resume Evidence；
- Workflow 失败模式进入 Prompt Learning，而不是直接升级为永久规则。


本阶段同时负责：

```text
WORKLOG → Activity / Event / Evidence
Test Integrity
Temporary Stub Evidence
Legacy Behavior Regression Evidence
```

临时桩必须有生命周期证据；测试通过不能建立在篡改业务口径基础上。

Commit Evidence 至少能够记录/索引：

```text
commit_hash
author_name / author_email
committer_name / committer_email
workflow/task/change/batch（存在时）
client
validation evidence
semantic commit plan id（若有）
```

不得用 Contributor Profile 覆盖 Git 原始 Author Evidence。

---

## 阶段 14：AI 工作模式、权限与 Governance Check

建议文档：

`14_AI工作模式权限与Governance_Check.md`

本阶段的权威专项清单见第 25 节；v1.9.1 继承并冻结 `14-I_Git_Commit_Governance与Safety_Gate.md`。

机器化：

```text
READ_ONLY
PLAN_ONLY
DOC_WRITE
CODE_WRITE
REVIEW
```

并验证：

```text
Project Stage
Batch
ALLOW_CODE_CHANGES
Protected Paths
Pending Decision
Change Status
Canonical Apply Status
P0/P1
Baseline Protection
Editor Capability
```


Governance Check 新增硬规则：

```text
Reference Integrity Check
Draft Workspace Canonical Write Guard
Temporary Stub / Bypass Guard
Acceptance Semantics Integrity Check
Unapproved Drop Guard
```

任何 `DROP_WITH_APPROVAL` 没有批准记录时必须 FAIL。

Git Commit Governance 必须额外检查：

```text
Commit Scope 是否属于当前允许写范围
Secret / Credential 是否被 stage
Protected Path 是否被 stage
Working Tree 中是否存在无法解释的混杂修改
Commit Plan 是否把无关 Change 混提
AI 是否尝试修改 Git Identity
高风险历史改写 / force push / rebase 是否升级 Gate
```

Profile `status` 不参与这些权限判断。

---

## 阶段 15：Banyan CLI、Runtime API、规则编译器与 Adapter Framework

建议文档：

`15_Banyan_CLI_Runtime_API规则编译器与Adapter框架.md`

本阶段的权威专项清单见第 25 节；v1.9.1 继承并冻结 `15-I_Banyan_Commit_CLI与统一提交策略.md`。

建立：

```text
Canonical Rule
↓
Compiler
↓
Adapter
↓
Editor-specific Output
```

目标命令：

```bash
banyan doctor
banyan scan
banyan change
banyan index build
banyan context build
banyan workflow status
banyan workflow inspect
banyan workflow resume
banyan sync cursor
banyan sync codex
banyan sync claude
banyan sync all
banyan migration status
banyan rollback
```

命令最终名称以实施阶段冻结为准。

Stage 15 正式实现统一 Commit CLI / Runtime API / Execution：

- 所有 Adapter 调用同一 Commit API；
- 消费 Stage 03 Schema、Stage 05 Semantic Commit / Message Policy、Stage 14 Safety Gate；
- 读取当前 Git Identity，但不修改；
- 当前 Git Identity 无法解析时 `BLOCK / NEEDS_INPUT`，不得自动补身份；
- 支持 Semantic Commit Plan、批量提交、剩余修改报告；
- Commit Message Convention 可由 Project Profile 覆盖，但不能按编辑器分叉；
- Commit 完成后读取真实 Commit Object 并写 Evidence；
- 本阶段只冻结**具体命令/API 形态和 Policy 的执行映射**，不得重新定义 Stage 05 已冻结的 grouping / message / confirmation 语义。

---

## 阶段 16：Banyan Control Plane / WebUI

阶段主文档：

`16_Banyan_Control_Plane与动态工程看板.md`

本阶段属于**复杂阶段，强制拆专项子指导**：

```text
16-A_Project_Entry_UI与Wizard_Flow.md
16-B_Project_Discovery_Source_Mapping与Legacy_Migration_UI.md
16-C_Control_Plane信息架构.md
16-D_WebUI字段权限与Explanation_Contract.md
16-E_Multi_Dimensional_Progress_Model.md
16-F_Event_Activity_Freshness_Model.md
16-G_Control_Plane_Command与Governance集成.md
16-H_WebUI安全权限与Secrets.md
16-I_Control_Plane验收与回滚.md
16-J_Runtime_Workflow可视化与ReRoute时间线.md
16-K_Migration_Center_UI与变量迁移视图.md
16-L_Parallel_Draft_Workspace_UI.md
16-M_Capability_Artifact_NoLoss_Migration_UI.md
16-N_Contributor_Commit_Provenance_UI.md
```

必须实现/验证：

- WebUI 不成为第二真源；
- 初始化、已有项目接入、已有治理迁移三条入口；
- Migration Center；
- 多轴进度；
- Status / Health / Freshness；
- Field Permission Model；
- Explanation Contract；
- Event / Activity；
- Project / Framework / Runtime 三层视图；
- 所有写操作通过 Command + Governance；
- Secrets 不回显；
- 已有 Project Instance 不重复初始化；
- Control Plane 可完全关闭，不影响 CLI / Framework 正常运行；
- 能观察 Workflow Graph、Active Branch、Re-route Trigger、Reconciliation、Resume Point 和 Workflow Health；
- Experiment / Decision Interrupt / Partial Blocking 在 UI 中可解释。


Control Plane 必须增加：

```text
Draft Workspaces
Pending Reconcile
Pending Promote
Legacy Capability Migration Coverage
AI Artifact Migration Coverage
No-Loss Status
Legacy Worklog / Handover / Progress Compatibility
Contributor Git Identities
Optional Contributor Profiles
Semantic Commit Plans / Commit Provenance
```

用户必须能看见“哪些能力/产物尚未映射”，而不是只看阶段完成百分比。

Contributor UI 规则：Git Identity 只读；`display_name/status/note` 可选编辑；不提供固定 Role/Module 职责编辑器；Client 只用于活动/来源筛选。

---

## 阶段 17：Reference Project Cursor 零回退迁移（首个 Adapter Pilot）

建议文档：

`17_Cursor零回退迁移.md`

顺序：

```text
现有 .cursor 盘点
↓
新 Adapter 输出
↓
语义对比
↓
Shadow Mode
↓
真实开发任务验证
↓
Cutover
```

未通过前不删除当前 Cursor Rules。

Cursor Pilot 还必须验证：Cursor 调用统一 Semantic Commit Policy 时，不改变当前 Git Identity；Commit Message、Trailer、Evidence 与 Core Contract 一致。

---

## 阶段 18：Codex、Claude 与 Generic Adapter

建议文档：

`18_CodexClaude与GenericAdapter适配.md`

只解决工具差异，不建立第二套 Policy。

建立 Adapter Compatibility Matrix，并验证同一任务在不同工具中的：

- 权限；
- Gate；
- Context；
- Skill；
- Decision；
- Change；
- Git Identity attribution；
- Semantic Commit grouping / message contract；
- Commit Provenance；

语义一致。

不同编辑器不得通过 Adapter 私自添加各自的提交格式、人员 Role 或身份切换逻辑。

---

## 阶段 19：全链路技术验收、回滚演练、Legacy 收口与 Release Candidate

建议文档：

`19_全链路技术验收回滚Legacy收口与Release_Candidate.md`

本阶段的权威专项清单见第 25 节；v1.9.1 继承并冻结 `19-N_Contribution_Identity与Commit_Provenance_Acceptance.md`。

必须验证：

### 已有项目

```text
续做
Change
Decision
PRD / UI
Meeting Pack
Project Guide
Batch
Code
Test
Acceptance
Release
```

### 新项目

```text
Bootstrap
Assessment
Governance Mode
Context
Change
Batch
Code
Test
```

### Core Purity

```text
Framework Core
→ Core Purity Scan
→ 不得包含 Reference Project 业务知识
```

### 跨项目移植

至少准备：

```text
Fixture A：已有项目
Fixture B：全新最小项目
Fixture C：与首个 Reference Project 不同技术栈的项目（推荐）
```

Banyan Core 不修改，只通过 Project Instance Mapping 完成接入。

### 多编辑器

```text
Cursor
Codex
Claude
Generic
```

### 重建

```text
删除 SQLite → rebuild
删除编辑器输出 → sync
删除 Runtime Context → rebuild
新会话 → restore
```

### 回滚

任一迁移阶段失败必须能恢复到阶段开始前可继续开发的状态。

全部通过后才允许：

- `.cursor` 手工规则降级为生成物；
- v3.1 大提示词降级为 Compatibility / Legacy Reference；
- Legacy 进入 `RETIREMENT_READY / DEPRECATED`，但默认不得做不可逆物理删除；
- 生成经过技术验收的 Banyan Release Candidate；
- 输出跨项目 Bootstrap 包。


### AI Capability No-Loss

必须验证：

```text
Legacy Capability Inventory
→ Preservation Matrix
→ Banyan Target Capability
→ Regression Evidence
```

全部闭环。

### AI Artifact Migration No-Loss

必须验证：

```text
AI Generated Artifact Inventory
→ Migration Matrix
→ Target / Action
→ Integrity / Rebuild / Compatibility Evidence
```

全部闭环。

Final Gate：

```text
UNMAPPED_VALUABLE_CAPABILITY = 0
UNMAPPED_CANONICAL_ARTIFACT = 0
UNEXPLAINED_GENERATED_ARTIFACT = 0
UNAPPROVED_DROP = 0
FAILED_LEGACY_REGRESSION = 0
FAILED_COMMIT_PROVENANCE_ACCEPTANCE = 0
```

否则禁止 Legacy `RETIREMENT_READY` / Release Candidate。

### Contribution Identity / Commit Provenance E2E

必须验证：

```text
Git Identity A + Cursor → Commit → Trace
Git Identity B + Codex  → Commit → Trace
同一 Git Identity + 不同 Client → 仍归同一贡献身份
未配置 Contributor Profile → 仍可正常 Commit / 查询
配置 Profile → 历史 Commit 只改变显示，不改变 Git Evidence
删除 SQLite → Contributor / Commit Index 可重建
AI 分批提交 → 无关/未完成修改仍留在 Working Tree
```

不得要求追踪实际物理操作者。


---

## 阶段 20：Banyan 使用说明体系、采用指南与 Final Release

阶段主文档：

`20_榕树AI使用说明体系与Final_Release.md`

本阶段的权威专项清单见第 25 节；v1.9.1 继承并冻结 `20-O_Git提交_贡献身份与AI分批提交指南.md`。

前置条件：

```text
Stage 19 Technical Acceptance = PASS
Release Candidate = VERIFIED
```

本阶段不再设计新的 Framework Behavior，只完成：

```text
Verified Capability
→ User / Admin / Operations / Extender Documentation
→ Documentation Consistency Validation
→ Final Release
```

目标读者分层：

```text
普通项目使用者
项目负责人 / 管理员
AI / 开发执行者
迁移负责人
框架扩展开发者
```

必须生成：

```text
Quick Start
New / Existing Project Onboarding
Adaptive Workflow Daily Guide
Change / Decision / Parallel Draft Guide
PRD × UI / Design Guide
Project Guide / Context / Memory / Progress / Control Plane Guide
Multi-editor Guide
Admin / Permission / Variables / Secrets Guide
CLI / Runtime API / WebUI Reference
Migration / Upgrade / Rollback / Troubleshooting Guide
Artifact / State / Schema Glossary
Extension Provider / Skill / Adapter Guide
Best Practices / Recipes / FAQ
Git Identity / Multi-contributor / AI Semantic Commit Guide
Documentation Consistency & Release Report
```

硬规则：

- 使用说明不能定义 Core 没有的行为；
- 命令、字段、状态、Schema Reference 优先自动生成；
- 所有文档绑定 Framework Version；
- Quick Start 必须在全新项目 Fixture 实测；
- Existing Project Guide 必须在迁移 Fixture 实测；
- Multi-editor Guide 必须使用 Stage 17/18 的真实验证结果；
- WebUI 操作说明必须使用 Stage 16 实际字段权限与 Explanation Contract；
- 文档发现实现问题时走 `REFRACTOR_PLAN_CHANGE`，不能在说明文档中私自修正规则；
- 如果 Plan Change 改变 Runtime / Schema / Adapter 行为，必须重新通过受影响 Gate 和 Stage 19 Technical Acceptance；
- Legacy 默认以 Deprecated / Archived 保留；任何不可逆 `DROP_WITH_APPROVAL` 仍需要单独批准，不因为 Final Release 自动删除。

Stage 20 Exit Gate：

```text
PUBLIC_CAPABILITY_WITHOUT_DOC = 0
DOCUMENTED_NONEXISTENT_CAPABILITY = 0
STALE_COMMAND_REFERENCE = 0
STALE_SCHEMA_REFERENCE = 0
UNVERIFIED_QUICKSTART_STEP = 0
DOCUMENTATION_DRIFT = 0
```

全部通过后：

```text
Framework Capability = RELEASED
Documentation Pack = RELEASED
Banyan Framework = FINAL_RELEASE
```


---

# 19. 各阶段统一施工模板

以后每一个阶段文档必须包含：

```text
1. 阶段目标
2. 为什么现在做
3. 输入
4. 真实仓库预检
5. 允许修改范围
6. 禁止修改范围
7. 迁移对象
8. 施工步骤
9. 新目录/新文件
10. 文件说明和注释要求
11. 数据迁移
12. 兼容策略
13. 校验
14. 回滚
15. 风险
16. 人工决策点
17. 完成证据
18. 阶段验收条件
19. 下一阶段准入条件
```

Codex 每阶段必须：

```text
先盘点
→ 出预检结果
→ 再施工
→ 再验证
```

不能：

```text
读完阶段文档后直接大面积改仓库
```

---

# 20. 全过程必须遵守的全局约束

## 20.1 不通过“删除旧体系”获得整洁

整洁必须通过：

```text
分类
迁移
索引
生成
兼容
```

获得。

## 20.2 不允许有两个正式真源

例如：

错误：

```text
Canonical DEC Source
+
SQLite 里另有一份可单独修改的 DEC 副本
```

正确：

```text
Canonical Decision Source
↓
SQLite Index / Read Model
```

## 20.3 不允许 Adapter 漂移

Cursor Adapter、Codex Adapter、Claude Adapter 不能各自加入业务规则。

## 20.4 不把项目业务塞进 Banyan Core

例如：

```text
源品 API 必须 8035
```

属于：

```text
Project Policy
```

不是：

```text
Banyan Core Policy
```

## 20.5 不把所有历史都默认塞给 AI

历史可以被索引，但 Context 按需加载。

## 20.6 不为了省 Token 删除必要证据

Token 优化是：

```text
更准确地选择内容
```

不是：

```text
删掉来源、决策、验收
```

## 20.7 SQLite 迁移必须可验证

必须有：

- 源文件；
- Hash；
- 解析结果；
- 失败列表；
- 重复列表；
- 关系统计；
- Rebuild 测试。

## 20.8 AI Memory 必须有来源

长期 Pattern 必须能知道：

```text
来自哪次任务
出现什么问题
如何验证有效
什么时候适用
什么时候不适用
```

## 20.9 所有自动生成文件都必须可再生

任何 Adapter / Context / Index 生成物都要记录：

```text
Source
Generator
Version
Command
Generated At
```

## 20.10 不跨 Stage 混合提交

每个阶段必须有独立 Checkpoint；需要 Git Commit 时，不能把多个 Stage 的改造混进同一个 Commit。

一个 Stage **可以有多个语义 Commit**，并应通过 Semantic Commit Planner 保持：

```text
阶段边界清楚
每个 Commit 语义清楚
差异可审查
可以单阶段回滚
```

Stage 00 只建立 Safety Baseline / Checkpoint，默认不自动 Commit。

## 20.11 Git Identity 只表示贡献身份

```text
Git Author name + email
= Contribution Identity
```

不追踪、不推断真实物理操作者，不自动合并多个 Identity。

## 20.12 Contributor Profile 不得变成权限/职责系统

Profile 只允许作为可选显示增强；不得通过 `role_labels`、模块标签、在职状态等隐式控制 Governance。

## 20.13 所有编辑器统一 Git Commit Policy

Cursor / Codex / Claude / Generic 不允许各自维护提交规范。AI 提交必须读取并使用当前 Git Identity，不自动修改身份，并按 Semantic Commit Plan 保留无关/未完成修改。

---

# 21. 全局闭环验收标准

整个改造只有满足以下条件才叫“完成”。

## 21.0 通用性闭环

必须证明：

- Banyan Core 不依赖任何 Reference Project 的业务事实；
- 换项目目录后只修改 Project Instance Mapping；
- Generic Skill 与 Project Skill 能明确区分；
- Project Override 不会反向污染 Framework Distribution；
- Core Purity Gate 可机器执行；
- 至少一个非 Reference Project Fixture 能完成初始化、Context、Change、执行与验收。

## 21.0A Control Plane 闭环

必须证明：

- Control Plane 完全关闭后 CLI / Framework 仍可正常工作；
- WebUI 只展示/操作 Canonical Source、Read Model 和 Runtime，不持有第二套业务真源；
- 所有可编辑字段均有明确编辑模式；
- 所有状态变更都通过 Action，不允许直接伪造状态值；
- 所有 Metric 有来源、计算和 Freshness；
- 所有 UI 元素都有 Explanation Contract；
- 进度支持多轴展示，不用单百分比掩盖开发/测试/验收/收口差异；
- Manual Progress 与 Evidence-based Progress 可区分；
- Secret 不回显；
- WebUI Command 无法绕过 Governance Check。

## 21.0B Project Onboarding / Migration 闭环

必须证明：

- 新项目可从零初始化；
- 已有项目可只接入而不重写历史；
- 已有治理体系可执行一次 Legacy Governance Migration；
- 旧变量能按 MAPPED / DERIVED / DEFAULTED / NEEDS_INPUT / DEPRECATED / CONFLICT 分类；
- 已确定变量不会被重复询问；
- 只有 NEEDS_INPUT / CONFLICT 才要求人工；
- Migration Preview 可列出 Will Create / Modify / Not Touch；
- Shadow / Cutover / Rollback 可执行；
- 迁移后旧 Governance 仍可追溯；
- 已存在 Project Instance 时不会重复初始化。

## 21.1 数据闭环

- Project Instance 映射的正式 Canonical Sources 没有丢失；当前 Reference Project 还需额外验证其既有 `docs/project` 资产完整；
- 原 DEC / ADR / CR / REQ ID 不被改挂；
- SQLite 索引计数和源文件一致；
- 无法解析项全部有报告；
- Migration Register 完整；
- 旧资料仍可追溯。

## 21.2 规则闭环

- AI 规则只有一个 Canonical Source；
- Editor Adapter 不拥有第二套业务规则；
- 规则修改后可以一条命令同步全部编辑器；
- 生成结果可检查漂移。

## 21.3 Context 闭环

- 新会话无需完整加载全部 5000+ 行规则；
- 能自动确定需要的 Role / Policy / Skill；
- 能恢复 Project Stage / Batch / Pending Decisions；
- 能说明 Context 来自哪些真源。

## 21.4 记忆闭环

- AI 工程经验可以沉淀；
- 项目事实不复制成第二真源；
- Prompt Review 能形成 Pattern；
- Pattern 有适用范围和来源。

## 21.5 权限闭环

- READ_ONLY 任务无法被误当 CODE_WRITE；
- `docs/temp` 无法被 AI 自动修改；
- Protected Path 被 Governance Check 拦截；
- 没有 Ready Batch 时不能误入代码施工。

## 21.6 UI 闭环

```text
Design Source
→ Design Pack
→ Implementation
→ Framework Adapter
→ Code
→ Screenshot
→ Diff
→ Repair
→ Acceptance
```

每层职责只有一处正式定义。

## 21.7 编辑器闭环

同一项目任务在：

```text
Cursor
Codex
Claude
```

中应得到一致的：

- Policy；
- Project Fact；
- Permission；
- Gate；
- Skill 语义；
- Git Identity attribution；
- Semantic Commit Policy；
- Commit Provenance。

编辑器只作为 Execution Client，不承担固定人员/业务职责。

## 21.8 重建闭环

必须能够证明：

```text
SQLite 可删可重建
Editor 输出可删可重建
Runtime Context 可删可重建
Adapter 输出可重新同步
```

## 21.9 回滚闭环

任意迁移阶段失败：

```text
rollback
```

后都应恢复到阶段开始前可继续开发的状态。

---


## 21.10 决策简便化闭环

必须证明：

- 明确事实不会被重复提问；
- 已 Applied 且依赖未变的 Decision 不会重复提问；
- AUTO 可以安全自动执行；
- ASK_ONCE 不被强制二次确认；
- CONFIRM_ONCE 只确认一次；
- CONFIRM_TWICE 只用于真正高风险；
- CROSS_DOMAIN_CONFIRM 不按文档数量重复询问；
- 一个根决策可以受控传播到 PRD / UI / API / Architecture / Batch。

## 21.11 OpenSpec 闭环

必须证明：

```text
Change
→ Discussion
→ Decision
→ Canonical Apply
→ PRD/UI/ADR
→ SQLite
→ Batch
→ Apply
→ Evidence
→ Review Pack
→ Archive
```

且：

- OpenSpec 不成为第二 PRD 真源；
- OpenSpec Archive 不覆盖正式真源；
- Change 可以取消而不污染正式文档；
- 纯实现 Fix 不被强制创建 CR。

## 21.12 PRD × UI 闭环

必须证明：

- PRD 与 UI_SPEC 职责明确；
- Design Revision 与 UI_SPEC Version 分离；
- Batch 锁定 Effective UI Contract；
- 新设计图不会静默改变进行中的 Batch；
- 纯 UI 与业务变化能自动分类；
- PRD/UI 冲突进入跨域决策。

## 21.13 Meeting / Review Pack 闭环

必须证明：

- Discussion Pack 真正服务“会前理解和待决策事项”；
- Final Review Pack 真正服务“实施启动与跨角色理解”；
- 会议文档不是业务真源；
- 会议产生的新决定必须回到 Decision + Canonical Apply；
- 已确认事实不会因为 Meeting Pack 重写而漂移。

## 21.14 Project Guide 闭环

必须证明：

- Guide 是整体说明书，不是 PRD 摘要；
- 文档组织面向读者，不按 REQ 机械展开；
- GUIDE_SYNC 支持多对多来源；
- 只有真正受影响的 Guide 标记 STALE；
- 旧 plain-document 迁移有对照、有保留、有回滚；
- Guide 不能反写 PRD/ADR/UI_SPEC。


## 21.15 Adaptive Workflow 闭环

必须证明：

- Project Lifecycle 与 Task Workflow 已分离；
- G0～G11 不再强迫 FAST Task 走重流程；
- Workflow Family 不等于固定 Step 模板；
- Workflow Atom 可按需组合；
- Runtime Workflow 支持 Graph、Branch、Loop、Pause、Resume、Retry、Skip、Replace、Invalidate 和 Cancel；
- Re-route 只有明确 Trigger 才发生；
- Branch 结束后必有 Reconciliation；
- Reconciliation 可输出 `RESUME / RESTART_NODE / SKIP_NODE / REPLACE_NODE / INVALIDATE_DOWNSTREAM / REPLAN / ABORT`；
- 节点是否继续由 Node Contract、依赖、输出和失效规则判断，不按旧步骤号机械返回；
- Decision Interrupt 可以局部阻塞并在 Canonical Apply 后恢复；
- Partial Blocking 不会无故冻结整个 Batch；
- Experiment 未接受前不会污染 Canonical Truth；
- UI Visual Repair 与正式 UI Change 能正确分流；
- Workflow 可以 Escalate / De-escalate；
- 高风险或低置信度 Re-route 会进入决策机制；
- Dependency / Invalidation 只让真正受影响的下游节点失效；
- Re-route 后只重建相关 Context；
- Workflow Event / Re-route / Resume / Evidence 可被 Trace 和 Control Plane 查询；
- 新会话可从 Checkpoint / Resume Point 恢复活动 Workflow。

## 21.16 跨阶段 Requirement Trace 闭环

必须证明：

```text
Framework Requirement
→ Owner Stage
→ Design Artifact
→ Implementation Artifact
→ Validation
→ Evidence
→ Capability State
```

均可在 `BANYAN_REFACTOR_TRACE` 中反查。

Stage `COMPLETED` 不能替代 Requirement `VERIFIED`。

## 21.17 Stage Delivery Pack 闭环

必须证明：

- 每个阶段都有独立 Precheck；
- 阶段主文档没有退化为新的超级 Prompt；
- 专项子指导只处理一个明确复杂域；
- Runbook 的每一步都有允许写入范围；
- 有迁移的阶段有 Migration Map；
- 有兼容差异的阶段有 Compatibility Matrix；
- 有数据迁移的阶段有 Reconciliation；
- 实际完成情况写入 Acceptance Report，而不是回写成计划事实；
- 每个阶段都有可用 Rollback Point；
- MIGRATION_REGISTER 能准确恢复“当前改造做到哪一步”。


## 21.18 阶段衔接闭环

必须证明：

- 每个 Stage 的 Prerequisite 都来自已完成上游；
- 下游不得依赖未定义 Schema / Provider / Gate；
- Owner Stage 唯一；
- 后阶段发现上游问题时走 `REFRACTOR_PLAN_CHANGE`；
- 阶段交棒包含实际 Artifact / Evidence / Rollback / Next Gate；
- 不存在“Stage 已完成但关键 Capability 仍无 Owner”的孤儿能力。

## 21.19 Activation 闭环

必须证明：

- `IMPLEMENTED` 不自动等于 `ACTIVE`；
- Shadow 能输出与旧体系的语义差异；
- Guarded Write 有明确旧/新 Gate 保护；
- Cutover 前存在可执行回滚；
- Release 后所有 ACTIVE 能力都能追溯到 VERIFIED Evidence。

---


## 21.20 Legacy Capability Preservation 闭环

必须证明：

- Codex 对真实仓库执行了 Full Repository Rediscovery；
- v3.1 有价值能力逐项进入 Preservation Matrix；
- Parallel Draft Workspace 被保留并行为回归；
- 36A Batch Canonical Reconciliation 被保留；
- 编号占用和 Reference Integrity 被保留；
- Test Integrity / Temporary Stub Cleanup 被保留；
- WORKLOG / HANDOVER / Progress 有明确新语义；
- `UNMAPPED_VALUABLE_CAPABILITY = 0`。

## 21.21 AI Generated Artifact Migration 闭环

必须证明：

- AI 生成的 Canonical / Derived / Operational Artifact 均被盘点；
- 每一项都有明确 Migration Action；
- Canonical Artifact 不因 Banyan 改造被静默搬迁或重写；
- Derived Artifact 可重建或有兼容入口；
- Archive / Deprecate / Drop 都有理由与证据；
- `UNMAPPED_CANONICAL_ARTIFACT = 0`；
- `UNAPPROVED_DROP = 0`。

## 21.22 Legacy Behavior Regression 闭环

必须证明旧能力迁移后的行为，而不仅是文件存在：

```text
旧场景输入
→ Banyan 新能力执行
→ 语义结果
→ Safety / Permission
→ Evidence
```

与旧能力的有效语义保持等价或有批准后的明确升级差异。

---



## 21.23 Contribution Identity / Semantic Commit / Provenance 闭环

必须证明：

- Git Identity 以 Commit Author `name + email` 为贡献身份事实；
- Banyan 不要求记录真实物理操作者；
- 使用别人电脑/环境时不会提示或自动切换 Git Identity；
- Contributor Profile 未配置时系统仍完整可用；
- Profile 只包含可选显示资料，不含固定 Role/Module 权限；
- Profile `status` 不参与 Governance Authorization；
- 同一 Git Identity 在 Cursor/Codex/Claude 中产生的 Commit 可归到同一 Contributor；
- 不同 Git Identity 默认保持独立，不被系统猜测合并；
- AI 执行 Commit 时不修改 Git 配置或 Author；
- “帮我分批提交”可以按语义拆分 Working Tree，并保留无关/未完成/Local-only 修改；
- Commit Message Policy 在多编辑器间一致；
- Commit → Workflow / Task / Change / Batch / Client 关系可以 Trace；
- 删除 SQLite 后 Commit/Contributor 索引可从 Git + 持久化 Trace 重建；
- Git Author Evidence 不会被 WebUI Profile 覆盖或改写。

---


## 21.24 Usage Documentation / Adoption 闭环

必须证明：

- 所有对外公开 Capability 都有对应说明或 Reference；
- Quick Start 在干净新项目上可按文档完成；
- Existing Project Migration Guide 在迁移 Fixture 上可按文档完成；
- Adaptive Workflow、Decision、Change、Parallel Draft 有真实操作示例；
- CLI / Runtime API / Schema / State Reference 与最终 Release Candidate 一致；
- Control Plane 的字段、权限、状态说明与 Explanation Contract 一致；
- Cursor / Codex / Claude 使用说明与真实 Adapter Capability 一致；
- Git Identity / Contributor Profile / AI 分批提交说明与 Stage 03～19 的真实实现一致；
- Documentation Source Map 可以反查 Capability / Schema / Command / Evidence；
- 使用说明不成为新的 Policy / Canonical Truth；
- Git Identity / Contributor Profile / Semantic Commit / Commit Provenance 使用说明与实际行为一致；
- `DOCUMENTATION_DRIFT = 0`。

只有本节通过后，Framework 才从：

```text
VERIFIED / RELEASE_CANDIDATE
```

进入：

```text
RELEASED / FINAL_RELEASE
```

---


# 22. 后续阶段按真实环境冻结的实施细节

这些问题不会阻塞当前总纲，但在相应阶段必须由真实仓库盘点后再定。

1. `docs/agreements` 在项目真源优先级中的准确位置。
2. `visual-repair-loop` 最终是否迁入 `tools/` 作为通用 Skill。
3. `.banyan/index/banyan.db` 是否提交 Git，还是统一本地重建。
4. Prompt 原文保留到什么粒度，避免无意义膨胀。
5. Memory Pattern 的人工批准门槛。
6. LIGHT / STANDARD / FULL 的自动评估指标。
7. 各编辑器当前版本的实际规则入口、Skill/Command/Hook 支持能力。
8. Adapter 输出是否使用软链、生成文件或混合方式。
9. Legacy v3.1 最终保留完整副本还是保留兼容入口 + Archive。
10. 是否将 Banyan CLI 做成 Python 包、独立二进制或项目脚本。
11. OpenSpec 最终采用的版本、CLI/API 接入方式与项目级 Schema 能力。
12. `banyan-change` 中各 Artifact 的最终文件名、必选/可选关系。
13. Discussion Pack / Final Review Pack 是否提交 Git，及归档保存周期。
14. Project Guide 最终是否沿用 `plain-document/` 物理目录，还是迁移到新目录；迁移前不得删除旧目录。
15. GUIDE_SYNC 最终采用 YAML、SQLite 派生关系还是双层表示。
16. UI_SPEC Governance SemVer 的自动升级判定阈值与人工覆盖规则。
17. `CROSS_DOMAIN_CONFIRM` 的根决策聚合算法和传播边界。
18. 哪些 AUTO 操作允许立即写文件，哪些仅允许生成建议后自动应用。
19. Banyan Framework Distribution 最终采用包、Git 依赖、二进制、安装目录还是混合分发。
20. Project Instance 如何声明/锁定 Framework Version。
21. Core Purity Gate 的项目特有词汇发现机制与允许清单。
22. Cross-Project Fixture 的最小标准与发布门槛。
23. Control Plane 首版前端技术栈与打包方式。
24. Runtime API 采用本地 HTTP、Unix Socket 或其它 IPC 方式。
25. Event Stream 首版使用 SSE 还是 WebSocket。
26. Progress Manual Override 是否默认允许，若允许其审批级别与过期策略。
27. Migration Center 对第三方旧治理体系的插件化 Importer Contract。
28. WebUI 远程访问是否进入 v1，还是只支持 Local-first。
29. Control Plane 的认证方式、只读模式和多人协作模式。
30. Initialization / Migration Report 的长期保存位置与保留周期。
31. Workflow Graph 的持久化采用 YAML/JSON、SQLite 派生状态还是混合方式。
32. Workflow Atom 的最小稳定 Schema 与版本兼容规则。
33. Workflow Family Catalog 的 v1 最小集合，避免过度分类。
34. Re-route Trigger 的默认白名单及项目扩展方式。
35. Workflow Confidence 的自动阈值和人工覆盖规则。
36. 哪些 Reconciliation Action 可 AUTO，哪些必须进入 Decision Router。
37. Experiment 临时分支采用 Git worktree、patch、内存 diff 还是项目适配方式。
38. 并行 Workflow / 并行 Branch 的 v1 支持范围及锁冲突策略。
39. Partial Blocking 与 Batch/Work Item 状态的最终 Schema。
40. Workflow Event Log 的保留周期、压缩与 Trace 关系。
41. Nested Branch / Subflow 的最大深度与循环保护策略。
42. Workflow Graph Revision 的持久化和压缩策略。
43. FAST / NORMAL / CONTROLLED 的 Artifact Budget 默认值与项目覆盖规则。
44. Parallel Draft Workspace 首版物理存储采用文件、Git ignored workspace、独立 worktree 还是混合方式。
45. Draft Workspace 并发命名、锁和 Reconcile 冲突策略。
46. AI Capability Preservation Matrix 最终 YAML Schema 与自动发现置信度规则。
47. AI Artifact Migration Matrix 对 Generated / Derived / Canonical Artifact 的默认策略。
48. Legacy Behavior Regression 的自动化测试格式与人工验收边界。
49. WORKLOG / HANDOVER 历史保留期限及是否全部索引。
50. Temporary Stub / Bypass 的最大存活时间和自动告警策略。
51. 最终用户文档的物理发布位置（Framework 包内 docs、独立站点、项目模板或组合方式）。
52. CLI / Runtime API / Schema Reference 自动生成器的具体技术实现。
53. WebUI 截图文档是否由自动 Screenshot Pipeline 生成。
54. 用户说明是否提供中英双语；v1 默认以中文为主，语言包后续决定。
55. Documentation Version 是否与 Framework Version 完全同号或允许独立 Patch。
56. Stage 15 最终采用的 Commit type/scope 词表，以及是否默认完全兼容 Conventional Commits。
57. Banyan Commit Trailer 的最小必选集合和项目覆盖规则。
58. Contributor Profile 的最终物理存储位置与 `status` 枚举是否允许项目扩展。
59. Stage 01 对历史 Commit Message 风格采用全历史统计还是代表性窗口分析。
60. Semantic Commit Planner 首版对 hunk-level staging、rename/binary/submodule change 的支持边界。

原则：

> **这些选择应在对应阶段结合真实仓库和真实编辑器能力确认，而不是现在拍脑袋冻结。**

---


## 22.1 当前不再需要用户提前准备的事项

以下内容应由对应阶段 Precheck 从真实仓库或工具环境发现，不要求用户现在重复整理：

- 目录树、文件数量、Git 分支/Commit；
- 现有 Rules / Skills / Prompt；
- 已有 PRD / DEC / ADR / CR / UI / Batch / Progress；
- 技术栈、构建系统、测试框架；
- Source Mapping 候选；
- 已确定旧变量；
- Cursor / Codex / Claude 的实际入口与当前能力（进入 Adapter 阶段时现场验证）。

只有以下情况才询问用户：

```text
NEEDS_INPUT
CONFLICT
高风险业务/数据/安全决策
真实工具能力无法自动确认
多个可行方案需要用户选择
```

---


# 23. 阶段依赖、Single Owner 与实施顺序

## 23.0 顺序 Gate 与语义依赖必须同时满足

本计划默认严格按：

```text
00 → 01 → ... → 20
```

执行。因此每个 Stage 的**直接前一阶段 Acceptance / NEXT_STAGE_HANDOFF**始终是硬 Entry Gate。

下面 Dependency Matrix 的“关键前置”只列出该 Stage 语义上必须消费的主要 Capability，不表示可以跳过中间阶段。

正确关系：

```text
Sequential Gate
+
Semantic Capability Prerequisites
+
NEXT_STAGE_HANDOFF
=
Stage Entry Ready
```

## 23.1 Stage Dependency Matrix

| Stage | 关键前置能力（仍受顺序 Gate 约束） | 唯一 Owner 职责 | 关键输出 | 主要消费者 |
|---|---|---|---|---|
| 00 | 无 | 改造安全基线 | Snapshot / Protected Paths / Discovery Scope / Checkpoint | 01～20 |
| 01 | 00 PASS | 全仓资产、能力、AI 生成产物、Git Identity/Commit Practice 发现与初版 No-Loss Coverage | Inventory / Capability Discovery / Artifact Inventory / Git Commit Practice Inventory / Preliminary Preservation & Migration Coverage | 02～20 |
| 02 | 01 PASS | Framework / Project 架构边界、Capability Coverage、Contribution/Provenance 架构 | Distribution / Project Instance / Source Role / Owner-Target Coverage / Git Identity-Provenance Boundary | 03～20 |
| 03 | 02 PASS | Artifact / Schema / Registry / Contribution Identity Contract | 通用 Schema / Registry / GitIdentity / ContributorProfile / CommitPlan / CommitProvenance Schema | 04～20 |
| 04 | 03 PASS | Project Instance / Source Mapping / Onboarding / Contributor Profile Registry | Instance / Profile / Source Mapping / Legacy Variable Migration / Git Identity Discovery | 05～20 |
| 05 | 04 PASS | Adaptive Workflow / Decision / Semantic Commit Workflow 语义 | Workflow Atom/Graph/Composer/Reconcile / 五档决策 / Draft Runtime / Semantic Commit Plan | 06、12～20 |
| 06 | 05 PASS | Change Workspace Provider / Canonical Apply | Provider Contract / OpenSpec Reference / Change-CR Mapping / Draft Promotion / Batch Reconciliation | 07～20 |
| 07 | 06 PASS；所需 Change/Canonical Apply Capability ≥ DEFINED；Legacy 可读 | Reference Project Legacy Migration / No-Loss Execution | v3.1 Preservation / Artifact Migration / Regression / Compatibility Loader | 08～20 |
| 08 | 03/05/06 PASS | PRD × UI_SPEC Governance | UI Truth Boundary / Version Axis / Effective UI Contract | 09、13、16、17、20 |
| 09 | 08 PASS | UI Design Intelligence | Design Pack / Implementation IR / Visual Validation | 13、16、17、20 |
| 10 | 09 PASS；语义依赖 04/06 已通过 | Project Knowledge Publishing | Guide Standard / GUIDE_SYNC / Legacy Plain Migration | 11、13、16、20 |
| 11 | 10 PASS；03/04/06/10 所需 Schema/Relation Contract 稳定 | Index / Trace / Historical Relations / Commit Provenance Index | SQLite Index / Trace Graph / Git Commit-Contributor Relations / Rebuild | 12～20 |
| 12 | 11 PASS；语义依赖 05 Workflow Contract | Context / Memory / Token | Context Builder / Session Restore / Memory Promotion | 13～20 |
| 13 | 12 PASS；语义依赖 05/11 | Evidence / Impact / Event / Learning / Commit Evidence | Evidence / Impact / Event / Test Integrity / Commit Evidence / Prompt Learning | 14～20 |
| 14 | 13 PASS；语义依赖 05/06 | Permission / Governance / Git Commit Safety Runtime | Work Mode / Governance Check / Write Guard / Integrity Gates / Commit Safety Gate | 15～20 |
| 15 | 14 PASS；语义依赖 03/05/11/12 | CLI / Runtime API / Compiler / Adapter Framework / Unified Commit Execution | CLI / API / Compiler / Adapter SDK / Semantic Commit CLI / Distribution | 16～20 |
| 16 | 15 PASS；语义依赖 11～14 | Control Plane | WebUI / Migration Center / Contributor & Commit Provenance / Workflow Visualization | 17～20 |
| 17 | 16 PASS；Pilot 语义依赖 07/14/15 | Reference Project Cursor Pilot | Shadow / Semantic Equivalence / Cursor Commit Policy Evidence / Cutover | 18～20 |
| 18 | 17 PASS；语义依赖 15 + Cursor Pilot Evidence | Codex / Claude / Generic Runtime Adapter | Multi-editor Compatibility / Commit Attribution Equivalence / Drift / Rebuild | 19～20 |
| 19 | 00～18 Gate 完整 | Technical Final Acceptance / Release Candidate | Core Purity / Portability / E2E / Rollback / No-Loss / Commit Provenance Acceptance / Release Candidate | 20 |
| 20 | 19 PASS | Usage Documentation / Adoption / Final Release | Documentation Pack / Git & AI Commit Guide / Reference / Drift Report / Final Release | Framework Users |

## 23.2 Single Owner Matrix

以下概念只能由一个 Stage 定义其 Canonical Contract：

| 概念 | Owner Stage | 其它阶段允许做什么 |
|---|---:|---|
| Framework / Project Boundary | 02 | 引用、验证，不重新定义 |
| Artifact / Registry Schema | 03 | 实现、扩展受控字段，不另造并行 Schema |
| Project Instance / Source Mapping | 04 | 读取、更新实例数据 |
| Adaptive Workflow / Decision Routing | 05 | 调用、提供事件/证据 |
| Change Provider / Canonical Apply | 06 | 调用 Provider、产生 Delta |
| Legacy v3.1 Compatibility | 07 | 仅 Reference Project 消费 |
| PRD × UI Governance | 08 | UI 工具和 Coding Context 消费 |
| UI Design Intelligence | 09 | Adapter / Control Plane 展示 |
| Project Guide / GUIDE_SYNC | 10 | Index、Impact、Control Plane 消费 |
| Index / Trace | 11 | Context / Impact / WebUI 查询 |
| Context / Memory | 12 | Agent / Adapter / Runtime 消费 |
| Evidence / Impact / Event | 13 | Governance / Dashboard / Learning 消费 |
| Permission / Governance Check | 14 | CLI / UI / Adapter 调用，不绕过 |
| CLI / Runtime API / Adapter Framework | 15 | Control Plane / Editor Adapter 实现 |
| Control Plane Contract | 16 | UI 实现，不定义业务事实 |
| Cursor Pilot Mapping | 17 | 不进入 Core |
| Other Editor Mapping | 18 | 不建立新 Policy |
| Parallel Draft Workspace Runtime | 05 | 06 Promote、07 Legacy Mapping、16 展示 |
| Batch Canonical Reconciliation | 06 | 05 触发、07 Legacy Mapping、13/14 验证 |
| Reference Integrity Contract | 03 | 11 建引用图、14 执行、07 Legacy Mapping |
| Test / Evidence Integrity | 13 | 14 强制、07 Legacy Regression |
| Reference Project Legacy Preservation / Compatibility Coordination | 07 | 01 发现、02 分配 Owner、03 提供 Schema；各领域 Owner Stage 实施具体迁移，19 做 No-Loss Audit |
| AI Artifact Migration Matrix Coordination | 07 | 01 建初版、02 Target Role 覆盖；09/10/11/17 等按领域实施并回写矩阵，19 最终审计 |
| Contribution Identity / Commit Provenance Schema | 03 | 02 冻结架构边界；04/11/13/15/16 实例化或消费 |
| Contributor Profile Registry | 04 | 16 展示/编辑可选资料；不得被 14 当权限源 |
| Semantic Commit Workflow / Commit Message Policy | 05 | 03 提供 Schema；13 记录 Evidence；14 执行 Gate；15 只实现 CLI/API/Execution，不重新定义 Policy |
| Commit Provenance Index | 11 | 从 Git + Trace 重建；16 查询，不成为第二 Git History |
| Commit Evidence / Contribution Event | 13 | 11 索引、14/19 验证 |
| Git Commit Safety Gate | 14 | 15/Adapter 调用，不修改 Git Identity |
| Unified Commit CLI / Execution | 15 | 17/18 各 Adapter 复用，不各自定义提交规范 |
| Contributor / Commit Provenance UI | 16 | 只做 Projection/可选 Profile 编辑，不改 Git Evidence |
| Technical Release Candidate Gate | 19 | 只验收技术实现，不重新定义上游能力 |
| Usage Documentation / Adoption | 20 | 从 VERIFIED 能力生成说明，不反向定义行为 |
| Final Release Gate | 20 | 文档一致性通过后发布最终版本 |

## 23.3 阶段回流规则

正常路径：

```text
Upstream Contract
→ Downstream Consume
→ Validate
```

如果下游发现上游 Contract 有缺陷：

```text
发现缺陷
→ REFRACTOR_PLAN_CHANGE
→ Impact Analysis
→ 回到 Owner Stage 修 Canonical Contract
→ 更新 Trace / Manifest
→ 仅重新验证受影响下游
→ Resume
```

禁止：

```text
Stage 15 发现问题
→ 直接在 CLI 内发明一个新的 Workflow 规则
```

这能从机制上避免重复设计和规则漂移。

## 23.4 施工顺序

```text
00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09
→ 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17 → 18 → 19 → 20
```

可以并行的是**只读调研与准备工作**；正式 Canonical Contract 和 Cutover 按 Gate 顺序推进。

---

# 24. 最终目标形态

最终不是：

```text
一份更大的 Prompt
```

也不是：

```text
Cursor Rules 2.0
```

而是：

```text
Usage Documentation / Reference
          ↓
        Human
          ↓
        Banyan
  ├── Project Assessment
  ├── Task Classifier / Workflow Composer
  ├── Change Necessity
  ├── Workflow Runtime / Re-router / Reconciliation
  ├── Decision Router
  ├── Change Workspace Provider
  ├── Canonical Apply
  ├── Context
  ├── Role
  ├── Policy
  ├── Skill
  ├── Workflow
  ├── State
  ├── Profile
  ├── Permission
  ├── PRD × UI Contract
  ├── Change Communication
  ├── Project Knowledge Publishing
  ├── Trace
  ├── Evidence
  ├── Memory
  └── Adapter
          ↓
       AI Agent
  ↓
Project
  ↓
Docs / Code / Test / Release
  ↓
Evidence / Trace / Learning
  ↓
下一次任务更快、更稳、更省 Token
```

最终要达到：

> **一份 AI 工程规则源，多个编辑器 Adapter；一套项目正式真源，SQLite 负责高速索引；一次真实开发经验可以沉淀成下一次可复用能力；已有项目可以安全迁入，新项目可以快速初始化；最终用户能够通过与 Framework Version 同步的使用说明体系正确操作 Banyan。**

---


# 25. 后续必须生成的阶段文档与物资清单

本节是后续逐阶段生成文档的**唯一权威文件名清单**。如果某个“条件型”文档经 Precheck 证明不适用，应在 `STAGE_MANIFEST.yaml` 标记 `NOT_APPLICABLE + reason`，而不是生成空文件。

## 25.1 每个阶段统一拥有的 Common Pack

除明确 `NOT_APPLICABLE` 外，每阶段统一包含：

```text
STAGE_MANIFEST.yaml
STAGE_PLAN.md
PRECHECK_AND_SCOPE.md
VALIDATION_AND_ROLLBACK.md
ACCEPTANCE_REPORT.md        # 真实施工完成后生成
```

涉及写入、迁移或多步骤执行时再强制：

```text
EXECUTION_RUNBOOK.md
MIGRATION_MAP.md
COMPATIBILITY_MATRIX.md
DATA_RECONCILIATION.md
```

`ACCEPTANCE_REPORT.md` 不在施工前预填“通过”。

### 25.1A 条件型施工物资默认适用矩阵

以下是默认要求；真实 Precheck 可以用 `NOT_APPLICABLE + reason` 收口，但不能静默省略。

| Stage | Runbook | Migration Map | Compatibility Matrix | Data Reconciliation |
|---|---|---|---|---|
| 00 | 必须 | N/A | N/A | N/A |
| 01 | 必须 | N/A | N/A | N/A |
| 02 | 条件 | N/A | N/A | N/A |
| 03 | 条件 | N/A | 条件 | N/A |
| 04 | 必须 | 必须 | 条件 | 条件 |
| 05 | 必须 | N/A | N/A | N/A |
| 06 | 必须 | 条件 | 必须 | N/A |
| 07 | 必须 | 必须 | 必须 | 条件 |
| 08 | 必须 | 条件 | 必须 | N/A |
| 09 | 必须 | 必须 | 必须 | 条件 |
| 10 | 必须 | 必须 | 必须 | 条件 |
| 11 | 必须 | 必须 | 必须 | 必须 |
| 12 | 必须 | 条件 | 必须 | 条件 |
| 13 | 必须 | N/A | 条件 | 条件 |
| 14 | 必须 | N/A | 必须 | N/A |
| 15 | 必须 | 条件 | 必须 | N/A |
| 16 | 必须 | 条件 | 必须 | 条件 |
| 17 | 必须 | 必须 | 必须 | 条件 |
| 18 | 必须 | 条件 | 必须 | 条件 |
| 19 | 必须 | 条件 | 必须 | 必须 |
| 20 | 必须 | N/A | 必须 | N/A |

说明：这里的 `Data Reconciliation` 只在有结构化导入/索引/历史数据重建时真正生成；“条件”不意味着可忽略，而是由该 Stage Precheck 明确决定。

## 25.2 全改造工程只维护一份的跨阶段物资

```text
MIGRATION_REGISTER.yaml
BANYAN_REFACTOR_TRACE.yaml
AI_CAPABILITY_PRESERVATION_MATRIX.yaml
AI_ARTIFACT_MIGRATION_MATRIX.yaml
LEGACY_BEHAVIOR_REGRESSION_MATRIX.yaml
DOCUMENTATION_SOURCE_MAP.yaml        # Stage 20 生成/维护
REFRACTOR_PLAN_CHANGE/*              # 实际命名由 Stage 03 冻结
```

路径说明：

- Stage 00～正式 Project Instance 路径冻结前，`MIGRATION_REGISTER / BANYAN_REFACTOR_TRACE` 可以存在于 `REFRACTOR_CONTROL_ROOT` 的 Bootstrap 位置；
- 正式 `.banyan/migrations/` 路径冻结后必须迁移并校验 lineage/hash；
- 迁移完成后不得保留两个可写真源。

最终阶段额外形成：

```text
CORE_PURITY_REPORT
CROSS_PROJECT_PORTABILITY_REPORT
CROSS_EDITOR_EQUIVALENCE_REPORT
FINAL_ROLLBACK_REHEARSAL_REPORT
TECHNICAL_RELEASE_CANDIDATE_REPORT
FINAL_RELEASE_REPORT
```

## 25.3 Stage 00：安全基线

阶段主文档：

```text
00_改造安全基线与仓库保护.md
```

专项：

```text
00-A_Repository_Baseline与Protected_Paths.md
00-B_Snapshot_Hash_Checkpoint与Rollback.md
```

执行后物资：

```text
BASELINE_MANIFEST
PROTECTED_PATHS_MANIFEST
CHECKPOINT_RECORD
DISCOVERY_SCOPE_BASELINE
```

> 兼容说明：已生成的 Stage 00 v1.8 Delivery Pack 与 v1.9.1 Contract 兼容，不需要重新生成；执行时以上位总纲 v1.9.1 为准，并在 Acceptance Report 记录兼容版本。

## 25.4 Stage 01：资产盘点

```text
01_AI资产全量盘点与方案裁剪.md
01-A_AI_Asset_Inventory_Schema.md
01-B_Legacy_Classification与Core_Candidate_Mapping.md
01-C_Duplicate_Conflict_Gap_Report.md
01-D_Reference_Project与Generic_Core边界审计.md
01-E_AI_Generated_Artifact_Inventory.md
01-F_AI_Capability_Discovery_Report.md
01-G_AI_Asset_Migration_Master_Map.md
01-H_Discovery_Coverage与NoLoss_Preliminary_Gate.md
01-I_Git_Identity与AI提交现状盘点.md
```

执行后物资：

```text
AI_ASSET_INVENTORY
LEGACY_CLASSIFICATION_REPORT
CORE_CANDIDATE_REPORT
CONFLICT_GAP_REPORT
LEGACY_AI_CAPABILITY_INVENTORY
AI_GENERATED_ARTIFACT_INVENTORY
OPERATIONAL_ARTIFACT_INVENTORY
DISCOVERY_COVERAGE_REPORT
PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX
PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX
GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY
```

## 25.5 Stage 02：目标架构

```text
02_Banyan目标架构与目录定稿.md
02-A_Framework_Distribution与Project_Instance边界.md
02-B_Target_Layout与Package_Strategy.md
02-C_Source_Role与Truth_Model.md
02-D_Capability_Ownership与Dependency_Map.md
02-E_Extension_Provider_Interface.md
02-F_Legacy_Capability_Architecture_Coverage_Gate.md
02-G_Contribution_Identity与Commit_Provenance架构.md
```

## 25.6 Stage 03：Artifact / Schema / Registry

```text
03_AI产物契约Schema与Registry.md
03-A_Artifact_Metadata_Schema.md
03-B_Registry_Schema与Discovery.md
03-C_Version_Dependency_Compatibility.md
03-D_Generated_Artifact_Contract.md
03-E_Validation_Error与Explanation_Schema.md
03-F_Refactor_Plan_Change_Schema.md
03-G_Legacy_Capability与Artifact_Migration_Schema.md
03-H_Parallel_Draft_Workspace与Reference_Integrity_Schema.md
03-I_Git_Identity_Contributor_Profile与Commit_Provenance_Schema.md
```

## 25.7 Stage 04：Project Instance / Onboarding / Migration

```text
04_Project_Instance_Source_Mapping与Profile.md
04-A_Project_Instance_Schema.md
04-B_Source_Mapping与Project_Profile.md
04-C_Project_Onboarding与Discovery.md
04-D_Legacy_Variable_Migration.md
04-E_Migration_Importer_Contract.md
04-F_Framework_Version_Lock与Upgrade.md
04-G_Contributor_Profile与Git_Identity_Discovery.md
```

## 25.8 Stage 05：Adaptive Workflow / Decision

```text
05_Adaptive_Workflow_Orchestrator与决策路由.md
05-A_Task_Classification与Delta_Detection.md
05-B_Workflow_Atom与Workflow_Composer.md
05-C_Workflow_Family_Catalog.md
05-D_Workflow_Graph_Node_Contract与Runtime_State.md
05-E_ReRoute_Escalation_DeEscalation与Reconciliation.md
05-F_Decision_Interrupt_Pause_Resume与Partial_Blocking.md
05-G_Experiment_Mode与Candidate_Delta.md
05-H_Dependency_Invalidation与Checkpoint.md
05-I_Workflow_Governance_Confidence与Evidence.md
05-J_Adaptive_Workflow验收场景集.md
05-K_Parallel_Draft_Workspace_Runtime.md
05-L_Semantic_Commit_Planner与Batch_Commit_Workflow.md
```

## 25.9 Stage 06：Change Provider / OpenSpec / Canonical Apply

```text
06_Change_Workspace_Provider_OpenSpec与Canonical_Apply.md
06-A_Change_Workspace_Provider_Contract.md
06-B_OpenSpec_Reference_Integration.md
06-C_Change_Necessity与Change_CR_Mapping.md
06-D_Canonical_Apply_Contract.md
06-E_Discussion_Pack_Contract.md
06-F_Final_Review_Pack_Contract.md
06-G_Change_Cancel_Archive与History.md
06-H_Change_Governance_Integration.md
06-I_Parallel_Draft_Promotion_Contract.md
06-J_Batch_Canonical_Reconciliation.md
```

## 25.10 Stage 07：Reference Project v3.1 Compatibility

```text
07_Reference_Project_v3.1超级提示词拆分与兼容层.md
07-A_v3.1_Inventory与Semantic_Mapping.md
07-B_Role_Policy_Skill_Workflow_State_Split.md
07-C_Legacy_Compatibility_Loader.md
07-D_Numbering_Status_Baseline_Compatibility.md
07-E_Shadow_Semantic_Equivalence.md
07-F_Legacy_Retirement与Rollback.md
07-G_v3.1功能能力完整保留矩阵.md
07-H_v3.1_Legacy_Feature_Regression_Cases.md
07-I_Parallel_Draft_Workspace迁移.md
07-J_Worklog_Handover_Progress兼容迁移.md
07-K_Legacy_Safety_Policies兼容映射.md
07-L_AI_Generated_Artifact迁移矩阵.md
```

## 25.11 Stage 08：PRD × UI_SPEC Governance

```text
08_PRD与UI_SPEC协同及UI版本治理.md
08-A_PRD_UI职责与冲突裁决.md
08-B_Design_Revision管理规范.md
08-C_UI_SPEC版本治理规范.md
08-D_Effective_UI_Contract生成规则.md
08-E_Batch版本冻结与升级规则.md
08-F_UI_Change_Classification.md
08-G_UI版本治理验收与回滚.md
```

## 25.12 Stage 09：UI Design Intelligence

```text
09_UI_Design_Intelligence子系统整合.md
09-A_UI_Protocol归并与职责矩阵.md
09-B_UI_Design_Pack_Schema.md
09-C_Frontend_Layout_Guidance_Standard.md
09-D_Implementation_IR与Compiler.md
09-E_UI_Framework_Adapter_Contract.md
09-F_Visual_Validation与Repair_Loop.md
09-G_Historical_UI_Artifact_Compatibility.md
09-H_UI_Intelligence_Acceptance.md
```

## 25.13 Stage 10：Project Guide / Knowledge Publishing

```text
10_Project_Guide与知识发布体系改造.md
10-A_现有Plain体系审计与问题报告.md
10-B_Project_Guide信息架构设计.md
10-C_Project_Guide编写规范.md
10-D_Project_Guide文章类型与模板规范.md
10-E_GUIDE_SYNC与来源图谱设计.md
10-F_旧Plain文档迁移映射.md
10-G_Project_Guide质量验收规范.md
10-H_Project_Guide迁移回滚与旧体系退役方案.md
```

## 25.14 Stage 11：SQLite / Trace / Historical Migration

```text
11_SQLite索引Trace与历史数据迁移.md
11-A_Index_Schema与Source_Parsers.md
11-B_Trace_Graph与Relationship_Model.md
11-C_Historical_Import与Migration_Manifest.md
11-D_Code_Trace与Reverse_Query.md
11-E_GUIDE_SYNC与Impact_Index.md
11-F_Rebuild与Integrity_Check.md
11-G_Data_Reconciliation.md
11-H_Index_Migration_Rollback.md
```

## 25.15 Stage 12：Context / Memory / Token

```text
12_动态Context记忆与Token优化.md
12-A_Context_Builder与Context_Plan.md
12-B_Context_Policy与Token_Budget.md
12-C_Runtime_Context与Session_Recovery.md
12-D_Memory_Tiers与Promotion.md
12-E_Project_Fact_Retrieval.md
12-F_Context_Explainability与Freshness.md
12-G_Context_Quality_Acceptance.md
12-H_Legacy_Handover与Session_Recovery兼容.md
```

## 25.16 Stage 13：Evidence / Impact / Event / Learning

```text
13_EvidenceImpact与Prompt学习闭环.md
13-A_Evidence_Model.md
13-B_Impact_Analysis_Engine.md
13-C_Event_Activity_Model.md
13-D_Prompt_Learning与Review.md
13-E_Lesson_Pattern_Promotion.md
13-F_Completion_Claim与Evidence_Gate.md
13-G_Evidence_Trace_Audit_Integration.md
13-H_Test_Integrity与Temporary_Stub_Governance.md
13-I_Legacy_Worklog_Event_Evidence_Mapping.md
```

## 25.17 Stage 14：Permission / Governance

```text
14_AI工作模式权限与Governance_Check.md
14-A_Work_Mode与Permission_Model.md
14-B_Governance_Check_Engine.md
14-C_Protected_Path与Write_Guard.md
14-D_Decision_Change_Gate_Integration.md
14-E_High_Risk_Operation_Policy.md
14-F_Governance_Audit与Evidence.md
14-G_Governance_Acceptance_Cases.md
14-H_Reference_Integrity与Legacy_Safety_Gates.md
14-I_Git_Commit_Governance与Safety_Gate.md
```

## 25.18 Stage 15：CLI / Runtime API / Compiler / Adapter Framework

```text
15_Banyan_CLI_Runtime_API规则编译器与Adapter框架.md
15-A_CLI_Command_Model.md
15-B_Runtime_API_Contract.md
15-C_Rule_Compiler.md
15-D_Adapter_Framework.md
15-E_Generated_Output_Drift_Check.md
15-F_Provider_Capability_Interface.md
15-G_Framework_Distribution与Versioning.md
15-H_CLI_Runtime_Acceptance.md
15-I_Banyan_Commit_CLI与统一提交策略.md
```

## 25.19 Stage 16：Control Plane / WebUI

```text
16_Banyan_Control_Plane与动态工程看板.md
16-A_Project_Entry_UI与Wizard_Flow.md
16-B_Project_Discovery_Source_Mapping与Legacy_Migration_UI.md
16-C_Control_Plane信息架构.md
16-D_WebUI字段权限与Explanation_Contract.md
16-E_Multi_Dimensional_Progress_Model.md
16-F_Event_Activity_Freshness_Model.md
16-G_Control_Plane_Command与Governance集成.md
16-H_WebUI安全权限与Secrets.md
16-I_Control_Plane验收与回滚.md
16-J_Runtime_Workflow可视化与ReRoute时间线.md
16-K_Migration_Center_UI与变量迁移视图.md
16-L_Parallel_Draft_Workspace_UI.md
16-M_Capability_Artifact_NoLoss_Migration_UI.md
16-N_Contributor_Commit_Provenance_UI.md
```

## 25.20 Stage 17：Reference Project Cursor Pilot

```text
17_Cursor零回退迁移.md
17-A_Current_Cursor_Inventory.md
17-B_Cursor_Adapter_Mapping.md
17-C_Rule_Semantic_Equivalence.md
17-D_Cursor_Shadow_Mode.md
17-E_Real_Task_Pilot.md
17-F_Cursor_Cutover与Rollback.md
17-G_Cursor_Acceptance.md
```

## 25.21 Stage 18：Codex / Claude / Generic Adapter

```text
18_CodexClaude与GenericAdapter适配.md
18-A_Codex_Adapter.md
18-B_Claude_Adapter.md
18-C_Generic_Adapter.md
18-D_Adapter_Capability_Compatibility_Matrix.md
18-E_Cross_Editor_Semantic_Equivalence.md
18-F_Adapter_Drift与Rebuild.md
18-G_Multi_Editor_Acceptance.md
```

## 25.22 Stage 19：Technical Final Acceptance / Release Candidate

```text
19_全链路技术验收回滚Legacy收口与Release_Candidate.md
19-A_Final_Requirement_Trace_Audit.md
19-B_Core_Purity_Audit.md
19-C_Existing_Project_E2E.md
19-D_New_Project_E2E.md
19-E_Cross_Project_Portability.md
19-F_Multi_Editor_E2E.md
19-G_Rebuild与Disaster_Recovery.md
19-H_Rollback_Rehearsal.md
19-I_Legacy_Retirement_Readiness.md
19-J_Release_Candidate与Bootstrap_Pack.md
19-K_AI_Capability_No_Loss_Audit.md
19-L_AI_Generated_Artifact_Migration_Audit.md
19-M_Legacy_Behavior_Regression_Final_Report.md
19-N_Contribution_Identity与Commit_Provenance_Acceptance.md
```


## 25.23 Stage 20：Usage Documentation / Adoption / Final Release

```text
20_榕树AI使用说明体系与Final_Release.md
20-A_快速开始与核心概念.md
20-B_新项目初始化与已有项目接入迁移.md
20-C_日常开发与Adaptive_Workflow使用指南.md
20-D_需求变更_Decision_Change与Parallel_Draft指南.md
20-E_PRD_UI_SPEC_设计图与视觉修复指南.md
20-F_Project_Guide_Context_Memory_Progress与Control_Plane指南.md
20-G_多编辑器_Cursor_Codex_Claude_Generic使用指南.md
20-H_管理员配置_变量_权限_安全与Secrets指南.md
20-I_CLI_Runtime_API_WebUI命令与操作参考.md
20-J_迁移_升级_回滚_灾难恢复与故障排查.md
20-K_Artifact_状态_Schema与概念词典.md
20-L_Extension_Provider_Skill_Adapter开发指南.md
20-M_典型场景_最佳实践与FAQ.md
20-N_使用说明一致性_Drift与Final_Release验收.md
20-O_Git提交_贡献身份与AI分批提交指南.md
```

执行后物资：

```text
DOCUMENTATION_SOURCE_MAP
DOCUMENTATION_COVERAGE_REPORT
DOCUMENTATION_DRIFT_REPORT
BANYAN_USAGE_DOCUMENTATION_PACK
FINAL_RELEASE_REPORT
```

## 25.24 后续你需要主动提供什么

当前进入 Stage 00 前，**不需要再人工制作新的项目说明文档**。

默认由 Codex / Banyan 在真实仓库 Precheck 中读取已有：

```text
Git / Git History / Git Identity / Commit Convention
Code
Current Governance Docs
Rules / Skills / Prompts / Commands / Hooks
PRD / DEC / ADR / CR
UI Assets / UI Specs / Design Packs / Visual Records
Plain / Guide Assets
Progress / Worklog / Handover / Dashboard
AI Generated Canonical / Derived / Operational Artifacts
Tests / Build / CI
```

只有阶段现场产生：

```text
NEEDS_INPUT
CONFLICT
无法自动验证的外部约束
必须由你选择的方案
```

时才让你决策。

因此接下来你的主要动作就是：

> **一次只让我生成一个阶段的 Stage Delivery Pack。**

---

# 26. 本总纲之后的逐阶段执行规则

当前只完成：

```text
总纲
```

不直接实施任何阶段。

你后续点名某一个阶段后，只生成该阶段的 Stage Delivery Pack；完成审查与实施验收后，再生成下一阶段。

建议严格按：

```text
00 → 01 → 02 → ... → 20
```

推进。

所有 Stage Gate 原则上都不得静默跳过。若某阶段能力经 Precheck 证明对当前发布目标 `NOT_APPLICABLE`，必须在 Stage Manifest 和 Migration Register 中记录理由。

已生成 Stage Pack 若来自较早 Charter，但上位总纲明确判定 `COMPATIBLE_WITH_NEWER_CHARTER`，可以继续执行；必须在 Acceptance Report 记录所依据的 Charter 与 Compatibility Note。

其中绝对不可跳过的安全/闭环 Gate：

- 00 安全基线；
- 01 全量盘点；
- 02 Framework / Project Boundary；
- 03 Artifact Contract；
- 04 Project Instance / Source Mapping；
- 05 Workflow / Decision Contract；
- 06 Change / Canonical Apply Contract；
- 11 Index / Trace Rebuild；
- 14 Governance Runtime；
- 15 CLI / Runtime API / Adapter Framework；
- 17 首个真实编辑器 Pilot；
- 19 Core Purity、Portability、Rollback、No-Loss 与 Technical Final Acceptance；
- 20 Usage Documentation 一致性与 Final Release。

Stage 16 Control Plane 对 Framework Runtime 是可选客户端，但因为本次目标版本已经明确纳入 WebUI，所以本次改造计划按必做阶段实施；未来其它项目可关闭它。

Stage 20 的用户文档对 Framework Runtime 不是运行时依赖，但对本次 `FINAL_RELEASE` 是必过发布 Gate。

允许某些阶段先完成 `DEFINED` 而不立即完成 `IMPLEMENTED`，但必须在 `BANYAN_REFACTOR_TRACE` 中记录目标 Capability State，禁止把“设计完成”误记成“运行时已经落地”。


---

# 27. 总纲结论

本次改造采用以下总原则：

1. **当前 Reference Project 保留既有 `docs/`；Banyan Core 不要求所有项目必须使用 `docs/` 目录，正式知识位置由 Source Mapping 决定。**
2. **项目内 `.banyan/` 作为 Banyan Project Instance / Runtime / Mapping 根目录；Banyan Framework Distribution 独立版本化，不由项目内 `.banyan/` 复制维护一套 Core 真源。**
3. **Banyan Core 只依赖 Project Canonical Source Role；当前 Reference Project 的 `docs/project` 继续作为其项目正式知识真源，不推倒重来。**
4. **当前 Reference Project 的 `docs/temp` 继续按 Project Mapping 保留为只读参考袋；该物理目录不是 Core 强制约定。**
5. **当前 Reference Project 的 `docs/agreements` 保留，后续仅做注册和优先级定义；其它项目可使用不同 Source Mapping。**
6. **当前 Reference Project 的 `tools/` 继续作为 Skill 实现映射来源；其它项目可使用不同 Tool Source，Generic Skill 真源归属于 Framework Distribution / Registry。**
7. **`.cursor` / `.codex` / `.claude` 最终均降级为 Adapter 输出。**
8. **SQLite 只作为可重建索引，不成为第二项目真源。**
9. **v3.1 不直接删除，而是拆分后通过 Compatibility Layer 平滑迁移。**
10. **现有 G0～G11、知情决策、编号保护、UI 门禁等已经验证过的能力先保留语义，再优化实现。**
11. **UI 方案按 Core Protocol + Design Pack + Layout + Implementation + Adapter + Validation 重新分工，去掉重复定义。**
12. **新增 AI Artifact 全部必须自解释、可发现、可版本化、可验证、可回滚。**
13. **通过 Context Builder、Index、Profile、Registry 降低 Token，而不是删除必要治理证据。**
14. **通过 Prompt Learning、Evidence 和 Memory 让 AI 能积累经验，但不能篡改项目事实。**
15. **通过 Governance Check 和机器权限保证改造过程及未来 AI 开发都不会随意越权。**
16. **整个迁移采用旁路建设、双轨验证、逐阶段切换，任何阶段都必须可以回滚。**
17. **Cursor 作为首个真实 Pilot，验证成功后再扩展 Codex、Claude 和其他编辑器。**
18. **最终必须同时通过“已有项目继续开发”“新项目初始化”“多编辑器一致”“数据可重建”“迁移可回滚”五类验收，才算真正闭环。**


19. **正式纳入五档决策机制：`AUTO / ASK_ONCE / CONFIRM_ONCE / CONFIRM_TWICE / CROSS_DOMAIN_CONFIRM`，不再让所有低风险事项机械执行二次确认。**
20. **正式纳入 Adaptive Workflow Orchestrator：先判断任务、Delta、Change/Decision 必要性和风险，再由 Composer 组装最短安全 Workflow，并允许运行时 Re-route / Reconcile。**
21. **正式纳入 Provider-neutral Change Workspace Contract，并以 OpenSpec 作为首个参考实现；OpenSpec Change 经过 Canonical Apply 后才进入 PRD/UI_SPEC/ADR 等正式真源。**
22. **为 OpenSpec 参考 Provider 定义 Banyan 兼容 Schema，并把 Discussion Pack 与 Final Review Pack 作为可生成的会议/评审 Artifact；Core 只依赖 Provider Contract。**
23. **Meeting Pack 只负责帮助人讨论和理解，会议结论必须回到 Decision + Canonical Apply，禁止会议文档成为第二真源。**
24. **正式纳入 PRD × UI_SPEC 协同模型：PRD 管业务，UI_SPEC 管视觉与交互表现，Effective UI Contract 冻结当前 Batch 真正使用的 UI 版本。**
25. **正式纳入 Design Revision 与 UI_SPEC Version 双版本轴，设计图更新先 Diff/Classification，再决定是否升级 UI_SPEC。**
26. **正式纳入 Batch Version Lock；正在开发的 Batch 不自动追随最新设计图或最新 UI_SPEC。**
27. **正式把 `plain-document` 能力升级为 Project Guide / System Handbook，而不是“另一份 PRD 白话摘要”。**
28. **正式纳入 Project Knowledge Publishing、Guide Map、GUIDE_SYNC、Stale Detection 和增量更新机制。**
29. **Project Guide 从 PRD/DEC/ADR/UI_SPEC/Architecture/Current Baseline 等正式事实按主题组装，但永远不能反写正式真源。**
30. **保留现有 `plain-spec/plain-document` 资产，先分类迁移、双轨验证，再决定最终物理目录，不直接删除重建。**
31. **最终用户体验以“用户只描述要干什么”为目标，G 阶段、OpenSpec Artifact、决策档位、Context 和 Adapter 由 Banyan 内部路由。**


32. **正式采用 Stage Delivery Pack：阶段主指导只负责调度，专项规则、Runbook、迁移、兼容、验收和实际报告分层管理。**
33. **正式采用阶段文档拆分准则：按 Schema、迁移、版本、回滚、验收和复用边界拆，不按“想写得更细”机械拆。**
34. **阶段 10 的 8 份现有 Plain 编写方案是强制审计输入，不能绕过它们直接重新设计 Project Guide。**
35. **阶段 10 固定拆为 10-A～10-H，覆盖旧体系审计、信息架构、写作规范、文章模板、GUIDE_SYNC、迁移映射、质量验收、回滚退役。**
36. **禁止生成新的“超级阶段文档”；复杂阶段必须通过专项子指导与按需 Context 控制复杂度。**
37. **Banyan 改造工程自身的阶段状态最终统一进入 `.banyan/migrations/MIGRATION_REGISTER.yaml`；Stage 00～路径冻结前允许 Bootstrap Register/Trace，正式迁入后只保留一个可写真源，并与业务项目进度彻底分离。**


38. **Banyan Framework Distribution 与任何 Project Instance 分离版本化；项目不得复制并手工维护一套 Core 真源。**
39. **Banyan Core 只认识通用 Source Role，具体目录由 Project Instance 映射，`docs/project` 不是 Core 的硬编码目录。**
40. **首个真实项目只作为 Reference/Migration/Acceptance Fixture，项目经验必须去业务化并通过跨项目验证后才允许进入 Core。**
41. **所有跨阶段能力采用 `DEFINED / IMPLEMENTED / INTEGRATED / VERIFIED / RELEASED` 生命周期，禁止用“文档完成”冒充“能力落地”。**
42. **新增全局 `BANYAN_REFACTOR_TRACE`，保证总纲要求到设计、实现、验证、Evidence 的跨阶段可追踪性。**
43. **最终技术验收必须通过 Core Purity Gate 和非 Reference Project 的 Cross-Project Portability Test；最终发布还必须通过 Stage 20 Documentation Gate。**


44. **正式纳入 Banyan Control Plane：它是 Framework 的可选观测/配置/控制客户端，不拥有第二套项目真源。**
45. **正式区分 New Project Initialization、Existing Project Adoption、Existing Governance Migration，已有治理项目不得重新从零初始化。**
46. **已有治理迁移只做一次 Project Instance Bootstrap + Legacy Governance Migration；已经确定的变量优先映射/推导，不重复询问。**
47. **Legacy Variable 统一采用 MAPPED / DERIVED / DEFAULTED / NEEDS_INPUT / DEPRECATED / CONFLICT 分类。**
48. **正式采用多轴进度：Implementation / Integration / Test Execution / Test Pass / Acceptance / Closure / Release Readiness 分开表达。**
49. **所有进度必须声明 Progress Source，禁止 AI 主观估算后伪装成 Evidence-based。**
50. **正式采用 Status / Health / Freshness 三维状态模型，并把 Activity 与 Progress 分离。**
51. **正式采用 WebUI 字段权限五类模型：EDITABLE / CONTROLLED_EDIT / ACTION_ONLY / READ_ONLY / SECRET。**
52. **正式采用 Explanation Contract；所有 WebUI 页面、卡片、字段、状态、指标、动作都必须能解释用途、来源、修改权限和影响。**
53. **正式纳入 Event / Activity Model，但 Event Store 只服务观测和追踪，不成为业务事实真源。**
54. **Control Plane 作为独立阶段 16；Cursor、Codex/Claude、技术终验和使用说明发布依次为 17/18/19/20。**


55. **正式把 G0～G11 从“每个任务的固定阶段流水线”降级为项目宏观生命周期与 Legacy Compatibility；日常任务由 Adaptive Workflow Runtime 编排。**
56. **正式采用 Workflow Family + Atom + Composer；以最短安全路径替代固定重流程。**
57. **正式采用有状态 Workflow Graph，支持 Branch / Merge / Loop / Pause / Resume / Retry / Skip / Replace / Invalidate / Cancel。**
58. **正式采用 Workflow Re-router + Reconciliation Engine；执行中出现新事实后可局部重规划，并决定 Resume / Restart / Skip / Replace / Invalidate / Replan / Abort。**
59. **正式采用 Workflow Node Contract、Dependency / Invalidation Engine、Checkpoint / Resume Point，禁止仅按步骤号机械恢复。**
60. **正式采用 Decision Interrupt 与 Partial Blocking；开发中新增 DEC 不要求整个 Batch 或整个生命周期从头再跑。**
61. **正式采用 Experiment Mode / Candidate Delta；临时 UI/实现探索可以 Accept/Discard，未接受前不得污染 Canonical Truth。**
62. **正式采用 Workflow Escalation / De-escalation；初始分类错误可以在 Evidence 支持下升级或降级。**
63. **正式采用 Re-route Trigger 与 Workflow Confidence，禁止 AI 无理由无限重规划。**
64. **正式把 Workflow Runtime、Active Branch、Re-route、Reconciliation、Resume Point 纳入 Control Plane 可观测性。**
65. **Project Guide 正式区分稳定知识与迭代上下文；短期 Batch/验收/临时桩信息不再长期混入说明书。**
66. **Project Fact Memory、Canonical Apply 和验收统一通过 Source Role 访问项目正式真源，避免继续硬编码 `docs/project/**`。**

> **v1.9.1 施工基线原则：每个能力只有一个 Owner；每个阶段只有在 Evidence、Trace、Rollback 与 Next Gate 同时闭环后才允许交棒；所有 Legacy AI 能力和 AI 生成产物必须经过 Preservation / Migration / Regression / No-Loss Audit 后，才允许旧体系退役。**

67. **正式纳入 Parallel Draft Workspace，保留 v3.1 变更稿模式的并行需求盘点价值，同时从 Core 中移除 `changes_temp` 等项目路径硬编码。**
68. **正式纳入 AI Capability Preservation Matrix，迁移对象从“文件”提升为“能力 + 行为”。**
69. **正式纳入 AI Artifact Migration Matrix，所有 AI 生成产物必须明确 KEEP / MAP / TRANSFORM / REGENERATE / INDEX_ONLY / COMPATIBILITY_READ / ARCHIVE / SUPERSEDE / DEPRECATE / DROP_WITH_APPROVAL。**
70. **正式保留 36A 的价值语义并升级为 Batch Canonical Reconciliation；纯实现不污染 PRD，真实业务变化必须 Canonicalize。**
71. **正式纳入 Reference Integrity Policy，仍被有效引用的正式规则不得删除、清空、换题或改挂 ID。**
72. **正式纳入 Test Integrity 与 Temporary Stub Governance，禁止为了通过验收改业务口径，临时桩必须可追踪并清理。**
73. **正式保留 WORKLOG / HANDOVER / Progress 的有效语义并映射到 Event/Evidence、Session Recovery、Multi-dimensional Progress 与 Control Plane。**
74. **Stage 19 正式增加 AI Capability No-Loss、AI Generated Artifact Migration Audit 和 Legacy Behavior Regression Final Report，并只产出 VERIFIED Release Candidate。**
75. **Codex Stage 01 必须重新从真实 Repository Root 全量盘点，不得把总纲已知名单当作完整事实。**


76. **正式区分 Codex Transformation Executor 与 Banyan Codex Runtime Adapter；Codex 可以从 Stage 00 开始施工，Stage 18 才建设未来运行时 Adapter。**
77. **No-Loss Coverage 正式左移到 Stage 01/02；所有高价值 Legacy Capability 在架构冻结前必须有 Candidate Owner / Target。**
78. **Stage 19 改为 Technical Final Acceptance / Release Candidate；Stage 20 才完成 Usage Documentation / Adoption / Final Release。**
79. **正式加入 Banyan Usage Documentation Publishing Contract；用户说明是 VERIFIED Capability 的 Projection，不得反向定义 Framework Behavior。**
80. **最终 Release 必须拥有 Documentation Source Map / Coverage / Drift Report，并保证 Public Capability 无文档遗漏、文档无虚构能力。**

81. **正式采用 Git Identity 作为 Banyan 唯一贡献身份：Commit Author `name + email` 是身份事实，Banyan 不追踪实际物理操作者。**
82. **Contributor Profile 仅为可选显示增强，只保留 display_name / status / note 等轻量信息；不建立 role_labels、固定模块、前后端岗位或人员权限体系。**
83. **Cursor / Codex / Claude / Generic 只记录为 Execution Client，不分配业务职责；所有编辑器使用同一 Git Identity / Commit Provenance / Semantic Commit Contract。**
84. **AI 执行 Git Commit 时必须使用当前环境实际 Git Identity，不修改 Git 配置、不替用户切换 Author；最终以 Commit Object 为 Evidence。**
85. **正式纳入 Semantic Commit Planner：允许用户积累大量改动后让 AI 按语义自动分批提交，并保留无关、未完成、Local-only 与风险修改。**
86. **Git 是 Commit History 真源，Banyan Trace/SQLite 只建立 Workflow / Change / Batch / Client 等语义关联和可重建索引，不建立第二套 Git 历史。**
87. **每个实际 Acceptance Report 必须交付 NEXT_STAGE_HANDOFF；下游 Stage 消费明确 Artifact/Evidence/Gate，不再靠猜测衔接。**
88. **已生成的 Stage 00 v1.8 Delivery Pack 与 v1.9.1 兼容，不因本次身份/Commit 横切能力补强而重新生成。**

> **最终原则：不推倒已验证的工程资产；把它们拆成更小、更明确、更可执行的能力，再通过统一 Registry、Workflow、Context、Index、Governance、CLI、Control Plane 和 Adapter 组织起来。**

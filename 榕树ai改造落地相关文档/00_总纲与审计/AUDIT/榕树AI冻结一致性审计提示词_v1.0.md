# 榕树 AI Freeze Consistency Audit 审计提示词 v1.0

> 用途：在逐阶段生成 Stage Delivery Pack 之前，对 Banyan 总纲与阶段文档清单做最后一次“冻结一致性审计”。  
> 核心原则：**只找冲突、遗漏、重复、依赖错误、Owner 漂移、旧概念残留和文件清单不一致；不主动扩张功能范围。**

---

## 审计任务

请对以下两份文档执行 Freeze Consistency Audit：

```text
榕树AI多编辑器AI软件工程框架改造总纲指导方案_<CURRENT_VERSION>.md
榕树AI改造阶段文档生成清单_<CURRENT_VERSION>.md
```

本次审计不是重新设计 Banyan，不允许因为“还能做得更复杂”就增加新 Stage、新子系统或新功能。

只有发现：

```text
结构冲突
阶段无法衔接
Owner 冲突
循环依赖
关键能力无 Owner
文档清单遗漏
旧规则残留造成语义冲突
Release / Handoff / Rollback 无法闭环
```

时才允许提出修正。

---

# 一、版本与文件完整性审计

检查：

1. 两份文档版本号是否一致。
2. 当前版本引用是否存在旧版本残留。
3. 旧版本引用是否属于明确的兼容/历史说明。
4. Stage 00～20 是否全部存在且各出现一次。
5. 第 25 节是否为唯一权威文件名清单。
6. 独立《阶段文档生成清单》是否与总纲第 25 节完全一致。
7. 是否存在重复文件名。
8. Stage 子文档 A/B/C... 是否存在意外缺号。
9. Section 18 的 Stage 主文档名是否与 Section 25 相同。
10. 是否仍存在已经废弃的旧文件名。

输出：

```text
VERSION_CONSISTENCY
STAGE_COVERAGE
FILE_LIST_MATCH
DUPLICATE_FILES
STALE_FILE_NAMES
```

---

# 二、Stage Dependency 审计

逐个检查 Stage 00～20：

```text
Stage N
→ Required Previous Gate
→ Required Capability / Schema / Evidence
→ Output
→ Next Consumer
```

必须确认：

1. Sequential Gate 始终按 00 → 20 推进。
2. 后 Stage 不得要求未来 Stage 才会定义的能力。
3. 不得出现循环依赖。
4. “Capability ≥ DEFINED”“Schema Stable”“Pilot Evidence”等语义前置，不得被误写成允许跳过上一 Stage Acceptance。
5. 下阶段可以通过 `NEXT_STAGE_HANDOFF` 精确获得所需 Artifact / Evidence。
6. Stage 19 只能进入 Release Candidate。
7. Stage 20 才能 Final Release。

输出：

```text
DEPENDENCY_GRAPH = PASS / FAIL
FORWARD_DEPENDENCY = 0
CYCLE = 0
AMBIGUOUS_ENTRY_GATE = ...
```

---

# 三、Single Owner 审计

对所有核心 Capability 建表：

```text
Capability
Canonical Owner Stage
Definition Stage
Implementation Stage
Integration Stage
Verification Stage
Release Stage
```

重点检查：

```text
Framework / Project Boundary
Artifact / Registry Schema
Project Instance
Workflow / Decision
Change / Canonical Apply
Legacy Compatibility
PRD × UI
UI Intelligence
Project Guide
Index / Trace
Context / Memory
Evidence / Impact / Event
Governance
CLI / Runtime API / Adapter
Control Plane
Git Identity
Contributor Profile
Semantic Commit
Commit Message Policy
Commit Provenance
Git Commit Safety
Commit CLI / Execution
Usage Documentation
Final Release
```

规则：

- 一个 Canonical Contract 只能有一个 Owner。
- 后续 Stage 只能消费、实现、验证，不得重新定义。
- 如果实现阶段必须改变 Owner Contract，只能走 `REFRACTOR_PLAN_CHANGE`。

输出：

```text
UNOWNED_CAPABILITY = 0
DUPLICATE_OWNER = 0
OWNER_DRIFT = 0
```

---

# 四、Git Identity / Contributor / Commit 模型审计

必须逐条验证当前冻结语义：

```text
Git Commit Author name + email
= Contribution Identity
```

并确认：

1. Banyan 不追踪现实物理操作者。
2. 使用别人电脑时，使用该环境实际 Git Identity。
3. AI 不切换、不修改、不猜测 Git Identity。
4. Git Identity 缺失时，AI 不发明身份，必须 BLOCK / NEEDS_INPUT。
5. Contributor Profile 仅为可选显示增强。
6. Profile 只允许轻量字段，例如 display_name / status / note。
7. 不存在 role_labels / 固定模块 / 前后端职位 / 人员权限体系。
8. Profile status 不参与 Governance Authorization。
9. 不自动合并多个 Git Identity。
10. Cursor / Codex / Claude / Generic 只是 Execution Client。
11. 编辑器不承担业务职责。
12. Git 是 Commit History 真源。
13. SQLite/Trace 不建立第二套可独立修改的 Git History。
14. Commit Author 与 Contributor Profile 显示增强不会互相覆盖。
15. Semantic Commit Policy 只有一个 Owner。
16. Adapter 不得各自定义 Commit Message。
17. “帮我分批提交”必须按语义拆分，而不是按目录机械拆分。
18. 未完成、无关、Local-only、Secret-risk 修改能够留在 Working Tree。

输出：

```text
IDENTITY_MODEL = PASS / FAIL
PROFILE_MODEL = PASS / FAIL
COMMIT_POLICY_OWNER = ...
COMMIT_PROVENANCE = PASS / FAIL
```

---

# 五、Capability Lifecycle / Activation 审计

检查核心跨阶段能力是否区分：

```text
PROPOSED
DEFINED
IMPLEMENTED
INTEGRATED
VERIFIED
RELEASED
```

以及：

```text
OFF
SHADOW
GUARDED
ACTIVE
```

重点验证 Semantic Commit：

```text
Stage 03 → Schema DEFINED
Stage 05 → Workflow / Policy DEFINED
Stage 11/13 → Index / Evidence IMPLEMENTED
Stage 14/15 → Safety + Execution IMPLEMENTED / INTEGRATED
Stage 17/18 → Cross-editor Pilot VERIFIED
Stage 19 → VERIFIED
Stage 20 → RELEASED
```

Stage 05 不得因为定义了 Commit Workflow 就提前获得正式 Git 写入接管权。

---

# 六、Stage Handoff 审计

每个 Stage 必须满足：

```text
Validation PASS
+
Acceptance Report
+
MIGRATION_REGISTER
+
BANYAN_REFACTOR_TRACE
+
Actual Artifacts
+
Evidence
+
Rollback Point
+
NEXT_STAGE_HANDOFF
+
Next Entry Gate
```

检查 `NEXT_STAGE_HANDOFF` 是否至少包括：

```text
upstream stage / run id
actual artifacts to consume
evidence to trust
unresolved risks
protected / allowed scope changes
rollback point
next entry gate result
```

禁止下阶段重新猜上阶段输出位置。

---

# 七、Bootstrap → Canonical Path 审计

特别检查 Stage 00 时序：

Stage 00 执行时 Stage 02/04 尚未冻结正式 Banyan Project Instance 路径，因此：

```text
Bootstrap Register / Trace
```

与最终：

```text
.banyan/migrations/MIGRATION_REGISTER.yaml
.banyan/migrations/BANYAN_REFACTOR_TRACE.yaml
```

必须有明确迁移规则。

要求：

```text
Bootstrap
→ hash / lineage
→ canonical path
→ validate
→ bootstrap archive/reference only
```

最终不得存在两个可写真源。

---

# 八、No-Loss / Legacy 审计

检查：

```text
Stage 01 Discovery
→ Stage 02 Owner/Target
→ Stage 03 Schema
→ Stage 07 Legacy Migration
→ Stage 19 No-Loss Final Audit
```

必须满足：

```text
UNMAPPED_VALUABLE_CAPABILITY = 0
UNMAPPED_CANONICAL_ARTIFACT = 0
UNEXPLAINED_GENERATED_ARTIFACT = 0
UNAPPROVED_DROP = 0
FAILED_LEGACY_REGRESSION = 0
```

不得让 Stage 07 成为第一次发现 Legacy Capability 的地方。

---

# 九、重复设计审计

重点检查以下边界：

```text
Stage 04 Onboarding Contract
vs
Stage 16 Wizard UI

Stage 05 Context/Impact/Governance Interface
vs
Stage 12/13/14 Runtime Owner

Stage 10 Project Guide
vs
Stage 20 Banyan Usage Documentation

Stage 15 Adapter Framework
vs
Stage 17/18 Editor Adapter

Stage 19 Release Candidate
vs
Stage 20 Final Release

Git / Commit History
vs
Banyan Trace / SQLite
```

发现重复定义必须保留唯一 Owner，其他阶段改成消费/展示/验证。

---

# 十、阶段文档物资审计

检查每阶段 Common Pack：

```text
STAGE_MANIFEST.yaml
STAGE_PLAN.md
PRECHECK_AND_SCOPE.md
VALIDATION_AND_ROLLBACK.md
ACCEPTANCE_REPORT.md
```

条件型：

```text
EXECUTION_RUNBOOK.md
MIGRATION_MAP.md
COMPATIBILITY_MATRIX.md
DATA_RECONCILIATION.md
```

检查：

1. 条件矩阵是否明确。
2. N/A 是否允许用 `NOT_APPLICABLE + reason` 收口。
3. 不允许生成空壳文档。
4. 实际结果不能提前写进计划文档。
5. Acceptance Report 只能在真实施工后产生。

---

# 十一、最终输出格式

最终必须输出：

```text
FREEZE AUDIT RESULT
PASS
PASS_WITH_FIXES
FAIL
```

然后分四类：

## A. Blocking Issues
会导致施工链错误，必须修。

## B. Consistency Fixes
不改变架构，只修 Owner、Gate、路径、生命周期、命名或引用。

## C. Verified Pass Items
列出已经确认没问题的核心项。

## D. Freeze Decision
只能选择：

- FINAL_FREEZE
- FIX_AND_REAUDIT
- ARCHITECTURE_REOPEN_REQUIRED

如果只是文字、Owner、Path、Gate 表达问题：

```text
当前版本 → Patch Version
例如 v1.9 → v1.9.1
```

不得因为小修正重新开启架构设计。

---

# 十二、审计纪律

禁止：

- 因为“未来可能有用”增加新功能；
- 因为“看起来更完整”新增 Stage；
- 重新设计已通过审计的子系统；
- 把项目业务事实写入 Banyan Core；
- 用一般经验替换文档已经冻结的明确决策；
- 为了追求理论完美导致无法开始施工。

最终目标：

> **确认这套计划现在能安全进入逐 Stage 施工，而不是继续无限设计。**

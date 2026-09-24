# Stage 08 v1.10 — Codex 正式开始提示词（低 Token）

这是 Stage 08 正式执行，不是重跑 Stage 01～07。

阶段：

```text
Stage 08 — PRD × UI_SPEC Governance
```

## 最小读取

先读：

```text
榕树ai改造落地相关文档/Stage_07_Reference_Project_v3.1_Legacy_NoLoss_Migration/reviews/Stage_07_to_Stage_08_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_07_Reference_Project_v3.1_Legacy_NoLoss_Migration/reviews/Stage_08_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_08_PRD_UI_SPEC_Governance/
```

然后按 Low Token Index 定点读取。

## 关键边界

```text
PRD = Business/Product Requirement Canonical Truth
UI_SPEC = Approved UI Contract / Projection
Design Source = Evidence
```

UI_SPEC 不能成为第二套 PRD。

## 必须冻结

```text
PRD Authority
UI_SPEC Authority
Application Scope
UI_SPEC Enablement
Design Evidence
UI_SPEC Lifecycle / Approval
PRD ↔ UI Trace
Version / Freshness Effect
Change Integration
Implementation Readiness
Validation Evidence
v3.1 UI Compatibility
```

## Legacy v3.1

必须保留：

```text
ENABLE_UI_SPEC_GENERATION
UI_SPEC_ENABLED_APPLICATIONS
G9.5
Partial Coverage
Draft / Approval
Design materials
Visual repair loop
```

的语义，但 Generic Core 不硬编码 Legacy 变量名。

## Stage07 Blockers

真实迁移仍：

```text
MIGRATION_BLOCKED
```

不要伪造 Ready。

CON-002 与 4 条缺目标历史引用继续保持开放。

## Stage09 边界

本阶段不实现 AnyDesign / Design Intelligence / Visual Runtime。

## 禁止

```text
重新扫描仓库
重读全部设计文档
修改 Canonical PRD/UI_SPEC
执行真实 Migration / Apply
创建正式 .banyan
进入 Stage 09
```

## Validation

执行 V08-01～V08-20，7 项 Hard Metrics 必须全为 0。

## 写入

仅：

```text
.banyan-refactor/stages/08/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

完成后 Acceptance + Handoff，停止。

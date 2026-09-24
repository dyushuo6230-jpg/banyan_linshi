# Stage 09 v1.10 — Codex 正式开始提示词（低 Token）

这是 Stage 09 正式执行，不是重跑 Stage 01～08。

当前阶段：

```text
Stage 09 — UI Design Intelligence
```

## 1. 最小读取

先读：

```text
榕树ai改造落地相关文档/Stage_08_PRD_UI_SPEC_Governance/reviews/Stage_08_to_Stage_09_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_08_PRD_UI_SPEC_Governance/reviews/Stage_09_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_09_UI_Design_Intelligence/
```

然后按低 Token 索引定点读取。

## 2. 核心原则

```text
Design Source = EVIDENCE_ONLY
Normalized Scene = Provider-neutral
Semantic = INFERENCE unless directly supported
Implementation Advice = RECOMMENDATION
```

严禁把 INFERENCE / RECOMMENDATION 写成 FACT。

## 3. 必须冻结

```text
Design Source Intake
Design Provider Port
Normalized Scene
Geometry
Semantic Tree
Design Truth
Design Tokens
Behavior Evidence
Data Evidence
Confidence / Provenance
FACT / INFERENCE / RECOMMENDATION
Implementation IR Input
Visual Validation Input
Design Drift
Legacy Compatibility
```

## 4. Geometry

设计图像素尺寸默认只是 observed/rendered geometry。

不得自动变成 fixed CSS width/height。

## 5. Behavior

静态图无法证明 Hover / Selected / Disabled / Loading / Drag / Gesture / Animation。

无证据时：

```text
UNKNOWN
```

## 6. UI_SPEC

Stage 09 Design Intelligence 输出不得自动升级为 Approved UI_SPEC。

必须继续经过 Stage 08 Governance。

## 7. Provider

AnyDesign / Figma / 图片解析 / 原型工具都只作为 Provider。

Generic Core 不绑定具体 Provider。

## 8. Inherited Blockers

真实迁移继续 `MIGRATION_BLOCKED`。

CON-002 / 四条历史缺目标引用 / R03 风险继续保留。

## 9. 禁止

```text
全仓扫描
全量分析设计图库
重做 Stage 08 Governance
修改 Canonical PRD/UI_SPEC
生成真实前端代码
创建正式 .banyan
进入 Stage 10
```

## 10. Validation

执行 V09-01～V09-22。

8 个 Hard Metrics 必须全部为 0。

## 11. 写入

仅：

```text
.banyan-refactor/stages/09/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

完成 Acceptance + Handoff 后停止。

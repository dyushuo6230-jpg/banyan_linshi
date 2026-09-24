# R0 Framework Self-Containment Remediation — 执行总则

## 1. 背景

D1.5 已识别：

```text
FRAMEWORK_RELEASE_NOT_SELF_CONTAINED
```

当前 Framework 的若干正式定义仍主要存在于施工阶段材料中，例如：

- Capability Contract Registry
- Artifact Contract / Schema / Registry
- Source Role Registry
- Workflow / State Contract
- Provider Port Schema
- Project Overlay Schema
- v3.1 Compatibility Mapping
- Version / Status / Provenance rules

如果 Framework 发布包离开 `.banyan-refactor/` 或 Stage 施工文档后无法自解释，则不满足最终可维护、可迁移、可复用目标。

## 2. R0 目标

把“属于 Framework 的最终正式定义”收敛到 `banyan-framework/` 内部，并做到：

```text
Self-contained
Discoverable
Versioned
Validated
Loadable / referenceable
Tested
Documented
Reproducible
```

## 3. R0 不解决什么

本轮不要求：
- 把所有 frozen Capability 都实现成 Runtime Skill；
- 建完整 Role runtime engine；
- 建 Adaptive Workflow executor；
- 建 Canonical Apply executor；
- 建多人 Collaboration Runtime Role；
- 建 WebUI Help Center；
- 做 Final Activation。

这些属于 R1/R2/R3 或后续阶段。

## 4. 设计原则

### 4.1 不复制施工目录

施工证据只能作为 Source Evidence。
最终 Framework Asset 必须是经过归并、去项目化、去临时化后的正式定义。

### 4.2 Generic Purity

`banyan-framework/` 不得出现当前业务项目专有名称、业务规则、项目路径硬编码。

### 4.3 一项正式定义只有一个权威归属

例如：

```text
Capability Contract Registry
```

不能同时在：
- Stage03 文档
- D0 inventory
- Runtime source
- 新 registry 文件

四处都各自成为事实真源。

必须明确 authoritative source，其余为 projection / generated reference / documentation。

### 4.4 兼容当前架构

当前 Runtime Core 仍为 Python。
Go/Gin 仍只是 Web Host / Control Plane bridge。
R0 不重构 Runtime Core 语言，不引入第二套 Permission Engine。

### 4.5 保留 Legacy 语义

v3.1 的兼容映射如果属于 Framework Release 必须正式进入 Framework。
但 R0 不要求现在完成所有 Legacy Artifact 的 Runtime 化。

## 5. R0 产物类别

至少应有：

```text
Framework Contract Manifest
Capability Contract Registry
Artifact Type / Contract Registry
Source Role Registry
Provider Port / Binding Contract
Workflow / State Contract Index
Compatibility Manifest
Schema Index
Version / Status / Provenance Definitions
Loader / Validator entrypoint
Tests
Maintainer Reference
```

具体文件名和目录由 Codex根据当前 Stage20 架构决定，但必须在验收报告中解释。

## 6. 验收核心问题

R0 完成后，假设只拿：

```text
banyan-framework/
```

不拿：

```text
.banyan-refactor/
榕树ai改造落地相关文档/
```

是否仍然能够回答：

```text
Banyan 有哪些正式 contract？
有哪些 capability？
有哪些 artifact type？
有哪些 source role？
有哪些 workflow/state contract？
有哪些 provider port？
v3.1 compatibility 如何映射？
这些定义的版本和状态是什么？
怎样校验？
Runtime / Adapter / Project Instance 应从哪里引用？
```

如果不能，R0 不通过。

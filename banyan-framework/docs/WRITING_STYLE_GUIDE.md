# Banyan Documentation Writing Style Guide

本指南约束 Banyan 用户文档和 Reference 的写法。事实以 [DOCUMENTATION_SOURCE_OF_TRUTH.yaml](DOCUMENTATION_SOURCE_OF_TRUTH.yaml) 为准；本指南不能创造新能力或新 Runtime enum。

## 1. 面向读者

- User Guide 与 Scenario 使用小白表达：先说用户要做什么，再解释必要术语和边界。
- Reference 使用精确表达：给出所属对象、实际值、状态、限制和事实来源。
- Maintainer 文档说明架构与维护责任，不把内部组件包装成用户功能。

## 2. 英文术语第一次出现

第一次出现采用：`English（推荐中文：一句普通开发者能理解的解释）`。

推荐写法：

- Canonical（权威正式来源：发生冲突时可作为正式事实依据的来源）
- Provenance（来源沿革：说明内容从哪里来、经过什么处理）
- Evidence（证据：支持判断、状态或结果的可核验材料）
- Trace（追踪记录：按事件保存动作、结果和关联证据）
- Gate（门禁：条件不满足时阻止进入下一步的检查点）
- Preflight（执行前预检：正式动作前检查权限、风险、前置条件和证据）

缩写第一次出现时展开英文全称并给中文，例如 `PRD（Product Requirements Document，产品需求文档）`。中英文说明统一使用中文全角括号 `（ ）`；代码、路径、枚举和值使用反引号。

## 3. 实现状态标签

使用 [IMPLEMENTATION_STATUS_REFERENCE.md](reference/IMPLEMENTATION_STATUS_REFERENCE.md) 定义的文档展示标签：

- `IMPLEMENTED`：当前实现源码中存在并可按已声明边界调用。
- `FROZEN_CONTRACT`：合同已冻结，不能推导为执行器已经存在。
- `PILOT`：受控试点，尚未正式激活或替代 Canonical truth。
- `PLANNED`：规划内容，尚未交付。
- `NOT_IMPLEMENTED`：明确不存在所述实现。
- `BLOCKED`：因授权、证据、治理决策或安全条件不能继续。

这些标签只用于文档展示，不是新增 Runtime enum。写状态时同时给出对象和上下文，例如“Adaptive Workflow：`FROZEN_CONTRACT`，executor：`NOT_IMPLEMENTED`”。

## 4. 事实措辞

- 已实现：写“当前实现提供……”并说明安全边界。
- 已冻结：写“合同已冻结；当前执行实现状态为……”。不得简写成“已支持”。
- 规划：写“计划在 D7 建设”，不得写“可在 `/help` 查看”。
- Pilot：写“`.banyan` 是 Shadow Pilot，未成为正式项目真相”。
- Blocked：写明阻塞对象和原因，例如“Final Activation 为 `NOT_AUTHORIZED`”。

禁止把目标体验写成当前实现。尤其不得声称：Adaptive Workflow 已自动路由全部任务、自然语言编辑器已完整编排研发流程、Canonical Apply 可由 Runtime 执行、`/help` 已上线、Framework Release 已激活 `.banyan`。

## 5. 示例与真实枚举

示例代码使用明确标题“示例”，并注明示例值是否真实。占位符使用 `<...>`，不能伪装成 accepted value。

真实枚举必须从 [STATUS_AND_ENUM_REFERENCE.md](reference/STATUS_AND_ENUM_REFERENCE.md) 或 D0 YAML 复制，并保留所属 schema / context。不同状态机里的 `BLOCKED` 不能合并解释。解释性标签不得写成 Runtime 返回值。

## 6. 权限与角色

始终保持：`Role != Permission != Git Identity != Authentication`。

`ALLOW` 是 Permission Result，不代表动作已执行。WebUI confirmation、Adapter request、Trace、Commit Plan、Role 和 Git Identity 都不单独构成 Authorization（授权：允许特定主体在特定范围执行特定动作的有效依据）。

Implementation Owner、Draft Contributor、Reviewer 只能标为 Documentation Collaboration Role；Human Project Authority 是治理概念，不是 Runtime role enum。

## 7. 文档类型与标记

文档类型使用 [KEY_DOCUMENT_TYPES_REFERENCE.md](reference/KEY_DOCUMENT_TYPES_REFERENCE.md) 的清单。`TBD` 是 unresolved value marker，不是文档类型。`RFC` 与 `TBC` 可解释通用工程含义，但必须注明 Banyan 当前没有独立 frozen schema / enum。

PRD 是产品/业务需求 Canonical truth。UI_SPEC 仅在批准后、且只在声明的应用范围内作为 UI contract projection。Design Source 是 Evidence，不能建立第二份业务真相。

## 8. 版本写法

必须分开写：Framework Release `v1.10-additive.1`、Governance CURRENT pointer `v1.9.1`、Python package / Runtime `0.1.0`。禁止用其中一个代替全部版本状态。

## 9. 链接与阶段

只链接真实存在的文件。提到尚未生成的内容时写“（D2/D3/D4/D5 后续生成）”，不创建看似可用的假链接。D0 的 9 个 `DOC-GAP-CANDIDATE` 必须保留原 ID。

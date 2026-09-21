# Banyan 如何陪你完成一次开发

> 关键术语：Workflow（工作流：按规则组织任务步骤）；Adapter（适配器：转换不同入口的请求格式）；Authorization（授权：允许特定范围动作的有效依据）；Trace（追踪记录：记录动作、结果和证据关系）。

## 这篇解决什么问题

用一条容易记住的用户旅程说明开发全过程中，你和 Banyan 各自要做什么。

## 什么时候需要看

任务不止一步，涉及需求理解、证据、决策、修改、验证和交付时。

## 核心概念

Documentation Target User Journey（文档目标用户旅程）是：

`Understand（理解需求） → Collect（收集物资和证据） → Plan（规划） → Decide（决策） → Execute（施工） → Validate（验证） → Deliver（交付）`

它是组织使用方式的目标旅程，不是当前 Runtime（运行时核心：执行权限判断和受控动作）已经实现的自动状态机。

## 推荐操作方式

### Understand（理解需求）

说明目标、范围、约束和验收结果。让 Banyan 复述理解，及时纠正歧义。

### Collect（收集）

提供需求文档、错误日志、截图、相关代码和已有 Decision。缺少关键 Evidence 时先补证据。

### Plan（规划）

要求列出影响范围、文件、步骤、验证方法、风险和明确不做的内容。

### Decide（决策）

遇到多个合理方案、Authority 冲突或高风险动作时，由合适的人作出明确决定。

### Execute（施工）

授权已审阅范围内的修改。出现新边界或新风险时重新回到 Plan / Decide。

### Validate（验证）

运行与变化相称的测试和静态检查，对照验收条件，并保留失败或 leftover。

### Deliver（交付）

总结变化、验证结果、限制和提交计划。当前项目 Runtime 只提供 commit dry-run。

## 自然语言示例

> 按 Understand、Collect、Plan 三步先处理，不要改代码。把已知事实、缺少材料、候选方案和需要我决定的问题分开列出。

## 当前实现状态

当前实现覆盖部分 Runtime request flow，包括 Adapter、Control Plane、Runtime API、Policy 和 Evidence Trace。Adaptive Workflow contract 已冻结，但完整自动 router / executor 未实现。

## 常见误区

- 七步旅程不是七个当前 Runtime enum。
- 人作出 Decision 后，仍不等于所有执行动作自动获 Authorization。
- Deliver 不代表必须提交；可以只交付计划和 dry-run 结果。

## 相关 Reference

- [工作流参考](../reference/WORKFLOW_REFERENCE.md)
- [角色参考](../reference/ROLE_REFERENCE.md)
- [关键文档类型参考](../reference/KEY_DOCUMENT_TYPES_REFERENCE.md)

# Skill, Capability Contract and Provider Reference

## 三个不同概念

Skill（技能说明包）是可由 AI 编辑器加载的任务说明，通常以 `SKILL.md` 表达。Capability Contract（能力合同）定义某类能力的输入、输出、前置条件、guard、failure semantics 和扩展点。Provider capability（提供方能力）是某个具体工具或实现通过 port / binding 提供的行为。

三者不能混用：Skill 存在不证明 Capability 已进入 Core；Capability Contract 冻结不证明 Provider 已选择；Provider 可运行也不证明它已获激活、拥有 Authority 或能绕过 Runtime Policy。

## 当前 Skill 事实

- Framework-native Skills：`none`。`banyan-framework` 内没有 Framework-native `SKILL.md`。
- `anydesign`：真源为 `tools/anydesign/SKILL.md`；`.cursor/skills/anydesign` 是符号链接。状态为 provider-owned / preserved in place，不属于 Banyan Core。
- `visual-repair-loop`：位于 `.cursor/skills/visual-repair-loop/SKILL.md`。状态为 compatibility layer / preserved in place，不属于 Banyan Core。

这两个 Skill 都不能被描述为 Framework-native Skill catalog。

## 35 个 Capability Contract 索引

注册表总状态是 `FROZEN_CONTRACTS_IMPLEMENTATION_UNBOUND`。所有项目均为 `implementation_frozen=false`、`provider_selected=false`。以下标题与清单是 Capability Contract，不是“35 个 Skill”。

### Frozen Core Contracts

- `CAP-AUTH`：工作范围与授权
- `CAP-PROFILE`：项目变量与接入模式
- `CAP-INTAKE`：来源投放与冻结
- `CAP-PRD`：PRD 生命周期与评审
- `CAP-IDP`：知情决策协议
- `CAP-ARCH`：架构和模块边界参与门禁
- `CAP-SCHEMA`：文档状态与编号
- `CAP-IDREF`：编号占用与在引用规则保护
- `CAP-TRACE`：全链路追踪
- `CAP-CHANGE`：变更与版本路由
- `CAP-PARALLEL`：Parallel Draft 临时袋
- `CAP-RECONCILE`：36A 批次正式口径收口
- `CAP-TEST`：自测桩与验收口径完整性
- `CAP-PROGRESS`：证据驱动多轴进度
- `CAP-HANDOVER`：工作日志与接管
- `CAP-CONTEXT`：新窗口续做
- `CAP-UI_SCOPE`：UI 逻辑范围与应用分闸
- `CAP-UI_CONTRACT`：分层 UI 合并与批次契约
- `CAP-UI_GATE`：素材→Draft→批准→点名换皮
- `CAP-VISUAL`：独立视觉修复循环
- `CAP-PUBLISH`：白话知识发布

### Compatibility Contracts

- `CAP-EDITOR`：Cursor 入口与项目覆盖
- `CAP-COMMIT`：既有提交校验与授权
- `CAP-MERGE`：旧协作合码指导

### Project Overlay Contracts

- `CAP-PORT`：项目端口绑定
- `CAP-SQL`：增量 SQL 交付习惯

### Provider Port Contracts

- `CAP-DESIGN`：AnyDesign 全量与单元素模式
- `CAP-CSS`：CSS 变量提取与摘要
- `CAP-CAPTURE`：页面截图与计算样式采集
- `CAP-COLORS`：图像主色提取
- `CAP-A11Y`：对比度检查
- `CAP-LINT`：设计文档结构校验
- `CAP-TOKENS`：设计令牌生成
- `CAP-DRIFT`：令牌与线上设计漂移比较
- `CAP-EXPORT`：设计交付包导出

## 如何写实现状态

正确写法：“`CAP-CHANGE` 的 Capability Contract 为 `FROZEN_CONTRACT`；完整 Change executor 尚未因此成为 `IMPLEMENTED`。”

错误写法：“Banyan 已安装 35 个 Skill”或“35 个 Capability 已全部实现”。

当前实际编辑器 Adapter 和 Runtime action surface 见[工作流参考](WORKFLOW_REFERENCE.md)。状态标签见[实现状态参考](IMPLEMENTATION_STATUS_REFERENCE.md)。

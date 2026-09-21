# Banyan Documentation

这里是 Banyan 正式说明文档的入口。Banyan 的当前主入口是 Codex / Cursor 自然语言编辑器，WebUI 是辅助观察与受限操作入口，CLI 是高级、调试和自动化入口。

当前编辑器 Adapter（适配器：把不同编辑器请求转换成统一格式的组件）只支持一组受限 action surface。完整自然语言自动 Workflow（工作流：按规则组织任务步骤的过程）编排尚未在 Banyan Framework 内实现，不能把“用自然语言提出需求”理解为 Runtime 已能自动完成整个研发流程。

## 按角色开始

### 普通开发者

先看[从这里开始](user-guide/00_从这里开始.md)，再按任务进入 [5 分钟快速开始](user-guide/01_5分钟快速开始.md)或[完整 User Guide](DOCUMENTATION_MAP.md#user-guide已完成)。Scenario Cookbook 将在 D3 生成。

遇到术语时查[中英双语术语表](reference/GLOSSARY_BILINGUAL.md)，需要判断某项能力是否真的可用时查[实现状态参考](reference/IMPLEMENTATION_STATUS_REFERENCE.md)。

### 项目负责人

先读[角色参考](reference/ROLE_REFERENCE.md)、[关键文档类型参考](reference/KEY_DOCUMENT_TYPES_REFERENCE.md)和[工作流参考](reference/WORKFLOW_REFERENCE.md)。这些页面明确区分治理角色、文档协作角色、权限和冻结合同。

`.banyan` 当前是 Shadow Pilot（影子试点：只作受控投影、尚未成为正式项目真相），Final Activation（最终激活：把 Project Instance 正式启用的独立治理动作）尚未授权。

### 高级 / 自动化用户

查阅[关键 ID 与变量](reference/KEY_IDS_AND_VARIABLES_REFERENCE.md)、[状态与枚举](reference/STATUS_AND_ENUM_REFERENCE.md)、[Skill 与 Capability](reference/SKILL_REFERENCE.md)及[工作流参考](reference/WORKFLOW_REFERENCE.md)。CLI、HTTP API 和 WebUI 的完整 Reference 将在 D4 生成。

当前项目 Git 执行边界为 `DRY_RUN_ONLY`。Permission Result（权限判定结果）中的 `ALLOW` 不等于动作已执行。

### Banyan 维护者

先从机器可读的 [Documentation Source of Truth](DOCUMENTATION_SOURCE_OF_TRUTH.yaml) 和人工盘点 [Documentation Inventory](DOCUMENTATION_INVENTORY.md)核对事实，再使用[写作风格指南](WRITING_STYLE_GUIDE.md)。架构、构建、运行、治理和升级维护正文将在 D5 生成。

## 当前版本维度

- Framework Release：`v1.10-additive.1`，`RELEASED_AS_ADDITIVE_SUPPLEMENT_NOT_CURRENT`。
- Governance CURRENT pointer：`v1.9.1`，`CURRENT_FINAL_FREEZE`。
- Python package / Runtime version：`0.1.0`。

这三个值描述不同对象，不能合并成一个“Banyan 当前版本”。Framework Release 也不等于 Project Final Activation。

## D1 已提供

- [文档地图](DOCUMENTATION_MAP.md)
- [写作风格指南](WRITING_STYLE_GUIDE.md)
- [中英双语术语表](reference/GLOSSARY_BILINGUAL.md)
- [实现状态参考](reference/IMPLEMENTATION_STATUS_REFERENCE.md)
- [关键文档类型参考](reference/KEY_DOCUMENT_TYPES_REFERENCE.md)
- [关键 ID 与变量参考](reference/KEY_IDS_AND_VARIABLES_REFERENCE.md)
- [状态与枚举参考](reference/STATUS_AND_ENUM_REFERENCE.md)
- [角色参考](reference/ROLE_REFERENCE.md)
- [Skill 与 Capability 参考](reference/SKILL_REFERENCE.md)
- [工作流参考](reference/WORKFLOW_REFERENCE.md)

## D2 User Guide 已提供

- [00 从这里开始](user-guide/00_从这里开始.md)
- [01 5 分钟快速开始](user-guide/01_5分钟快速开始.md)
- [02 Banyan 如何陪你完成一次开发](user-guide/02_Banyan如何陪你完成一次开发.md)
- [03 在 Codex / Cursor 中使用 Banyan](user-guide/03_在Codex_Cursor中使用Banyan.md)
- [04 如何向 Banyan 描述需求](user-guide/04_如何向Banyan描述需求.md)
- [05 物资、证据、决策是什么](user-guide/05_物资_证据_决策是什么.md)
- [06 Banyan 如何自动选择工作流](user-guide/06_Banyan如何自动选择工作流.md)
- [07 WebUI 使用手册](user-guide/07_WebUI使用手册.md)
- [08 CLI 使用入门](user-guide/08_CLI使用入门.md)
- [09 Change 与 Decision 使用说明](user-guide/09_Change与Decision使用说明.md)
- [10 Git 与语义化分批提交](user-guide/10_Git与语义化分批提交.md)
- [11 多人研发与变更稿协作](user-guide/11_多人研发与变更稿协作.md)
- [12 Project Instance 与项目接入](user-guide/12_Project_Instance与项目接入.md)
- [13 文档、Source Mapping 与知识管理](user-guide/13_文档_Source_Mapping与知识管理.md)
- [14 权限、Gate 与安全](user-guide/14_权限_Gate与安全.md)
- [15 FAQ](user-guide/15_FAQ.md)

WebUI `/help` 尚未实现。D1 文档通过仓库文件访问，不代表 Help Center 已上线。

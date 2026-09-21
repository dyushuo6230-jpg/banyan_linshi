# Banyan Documentation Map

本文说明 Banyan 文档体系各区域的用途与建设阶段。当前完成的是 D0 事实底座、D1 文档地基和 D2 User Guide。

## 当前可用

### 事实底座

- [DOCUMENTATION_SOURCE_OF_TRUTH.yaml](DOCUMENTATION_SOURCE_OF_TRUTH.yaml)：机器可读事实清单，是后续文档的首要内容依据。
- [DOCUMENTATION_INVENTORY.md](DOCUMENTATION_INVENTORY.md)：D0 人工盘点，解释实际实现、冻结合同、Pilot 和 Gap。

### 文档地基

- [README.md](README.md)：按用户角色导航。
- [WRITING_STYLE_GUIDE.md](WRITING_STYLE_GUIDE.md)：术语、状态、措辞和示例规则。
- [reference/GLOSSARY_BILINGUAL.md](reference/GLOSSARY_BILINGUAL.md)：中英双语术语。
- [reference/IMPLEMENTATION_STATUS_REFERENCE.md](reference/IMPLEMENTATION_STATUS_REFERENCE.md)：文档展示状态标签。
- [reference/KEY_DOCUMENT_TYPES_REFERENCE.md](reference/KEY_DOCUMENT_TYPES_REFERENCE.md)：文档类型与标记的边界。
- [reference/KEY_IDS_AND_VARIABLES_REFERENCE.md](reference/KEY_IDS_AND_VARIABLES_REFERENCE.md)：稳定 ID、版本字段、环境变量和项目变量。
- [reference/STATUS_AND_ENUM_REFERENCE.md](reference/STATUS_AND_ENUM_REFERENCE.md)：按 schema / context 分组的实际枚举。
- [reference/ROLE_REFERENCE.md](reference/ROLE_REFERENCE.md)：Source、Governance、Contributor Profile 与 Documentation Collaboration Role。
- [reference/SKILL_REFERENCE.md](reference/SKILL_REFERENCE.md)：Skill、Capability Contract、Provider capability 的区别。
- [reference/WORKFLOW_REFERENCE.md](reference/WORKFLOW_REFERENCE.md)：已实现流程与冻结工作流合同的区别。

## User Guide（已完成）

`user-guide/` 面向普通开发者，用小白表达回答“怎样开始、怎样说需求、怎样理解结果和安全边界”。

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

## 后续文档区域

### `scenarios/`（D3 后续生成）

面向具体任务的 Scenario Cookbook（场景手册：按真实任务给出输入、步骤、判断和边界），例如规划但不改代码、修复 Bug、多人协作和接入旧项目。D1 不创建场景正文。

### `reference/`

面向查阅的精确规则。D1 已建立术语、状态、类型、ID、角色、Skill 和 Workflow 的基础 Reference；CLI、WebUI、Project Instance、Decision Level、Source Role 等专题将在 D4 补齐。尚未生成的 D4 页面不在此创建假链接。

### `maintainer/`（D5 后续生成）

面向 Banyan 维护者，覆盖架构、安装构建运行、Runtime/Adapter、Project Instance、治理安全、升级迁移和故障排查。D1 不创建维护正文。

## 后续阶段

- D2：User Guide，已完成。
- D3：Scenario Cookbook。
- D4：完整 Reference Manual。
- D5：Maintainer Packaging。
- D6：Documentation-driven Gap Check。
- D7：WebUI Help Center；当前 `/help` 为 `NOT_IMPLEMENTED`。
- D8：最终文档验收。

`Understand → Collect → Plan → Decide → Execute → Validate → Deliver` 是 Documentation Target User Journey（文档目标用户旅程），不是当前 Runtime 已实现的完整自动状态机。

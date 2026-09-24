# Banyan Documentation Packaging 总指挥文档 v1.0

> 适用范围：Stage 20 完成后的 Banyan 用户文档体系建设
> 性质：Documentation Packaging / User Manual Pass
> 不是 Stage 21，不修改 Banyan Core，不自动改变当前 Framework Version Pointer，不执行 Project Final Activation。

## 1. 总目标

把已经验收通过的 Banyan Framework，整理成一套真正可供团队日常使用的正式文档体系：

```text
自然语言编辑器（Codex / Cursor）
        ↓
User Guide / Scenario Cookbook
        ↓
WebUI Help Center
        ↓
Reference Manual
        ↓
Maintainer Manual
```

最终文档统一进入：

```text
banyan-framework/docs/
```

Stage 00～20 施工证据继续留在原施工档案目录，不迁入 Framework Docs。

## 2. 已冻结的文档原则

### 2.1 使用入口

```text
主入口：自然语言编辑器（Codex / Cursor）
辅助入口：WebUI
高级入口：CLI
```

### 2.2 文档风格

```text
user-guide / scenarios = 小白教程风格
reference = 简洁、精确、可查
maintainer = 工程维护和架构文档
```

### 2.3 英文术语规则

第一次出现必须带中文解释：

```text
Preflight（执行前预检：在正式执行动作前检查权限、风险、前置条件和所需证据）
Canonical（权威正式来源：发生冲突时可作为正式事实依据的来源）
```

### 2.4 必须覆盖的 Banyan 基础语言

```text
PRD / ADR / DEC / UI_SPEC / TBD / TBC / RFC
Artifact / Canonical / Derived / Stable ID / Source Role
Authority / Version / Status / Freshness / Provenance
Evidence / Trace / Role / Skill / Workflow / Decision Level
Permission Result / Risk Class / Execution Mode / Provider
Overlay / Project Instance / Change / Draft Change Package / Canonical Apply
```

## 3. 最终文档目录

```text
banyan-framework/docs/
├── README.md
├── DOCUMENTATION_MAP.md
├── WRITING_STYLE_GUIDE.md
├── DOCUMENTATION_SOURCE_OF_TRUTH.yaml
├── user-guide/
├── scenarios/
├── reference/
└── maintainer/
```

### user-guide

```text
00_从这里开始.md
01_5分钟快速开始.md
02_Banyan如何陪你完成一次开发.md
03_在Codex_Cursor中使用Banyan.md
04_如何向Banyan描述需求.md
05_物资_证据_决策是什么.md
06_Banyan如何自动选择工作流.md
07_WebUI使用手册.md
08_CLI使用入门.md
09_Change与Decision使用说明.md
10_Git与语义化分批提交.md
11_多人研发与变更稿协作.md
12_Project_Instance与项目接入.md
13_文档_Source_Mapping与知识管理.md
14_权限_Gate与安全.md
15_FAQ.md
```

### scenarios

```text
01_开发一个全新需求.md
02_只让Banyan规划_不要修改代码.md
03_Banyan规划_我决策_再施工.md
04_修改已有功能.md
05_修复一个Bug.md
06_排查复杂问题.md
07_检查当前修改是否完整.md
08_让Banyan合理分批提交.md
09_接手别人开发到一半的需求.md
10_前后端数据库联合需求.md
11_PRD或UI_SPEC发生变化.md
12_多人按模块并行开发.md
13_多人按独立需求并行开发.md
14_一人施工_其他人变更稿盘点.md
15_变更稿释放到正式文档.md
16_两个Change碰到同一模块.md
17_多人同时涉及同一个Canonical文档.md
18_旧项目第一次接入Banyan.md
19_旧docs_project文档接入Banyan.md
20_Banyan自身升级.md
```

### reference

```text
GLOSSARY_BILINGUAL.md
KEY_DOCUMENT_TYPES_REFERENCE.md
KEY_IDS_AND_VARIABLES_REFERENCE.md
STATUS_AND_ENUM_REFERENCE.md
ROLE_REFERENCE.md
SKILL_REFERENCE.md
WORKFLOW_REFERENCE.md
WORKFLOW_STATE_MACHINE_REFERENCE.md
DECISION_LEVEL_REFERENCE.md
SOURCE_ROLE_REFERENCE.md
ARTIFACT_REFERENCE.md
COLLABORATION_ROLE_AND_STATE_REFERENCE.md
CLI_REFERENCE.md
WEBUI_PAGE_REFERENCE.md
NATURAL_LANGUAGE_PROMPT_REFERENCE.md
DIRECTORY_REFERENCE.md
PROJECT_INSTANCE_REFERENCE.md
```

### maintainer

```text
ARCHITECTURE.md
INSTALL_BUILD_RUN.md
WEBUI_CONTROL_PLANE.md
RUNTIME_ADAPTER.md
PROJECT_INSTANCE.md
GOVERNANCE_SECURITY.md
UPGRADE_MIGRATION.md
LEGACY_DOC_ADOPTION.md
TROUBLESHOOTING.md
RELEASE_MAINTENANCE.md
CONTRIBUTING_TO_BANYAN.md
```

## 4. 核心用户旅程

```text
Understand（理解需求）
→ Collect（收集物资和证据）
→ Plan（影响分析与规划）
→ Decide（需要开发者做决策）
→ Execute（施工）
→ Validate（验证）
→ Deliver（交付、提交、正式文档释放）
```

目标体验：

```text
用户先说需求
→ Banyan 自动安排 Workflow
→ 缺材料时索取材料
→ 缺证据时索取证据
→ 需要决策时停止让开发者决定
→ 确认后施工
→ 完成后验证并交付
```

## 5. 多人研发模式

默认推荐：

```text
按模块隔离
按目录隔离
按独立需求隔离
按 Change 隔离
```

关键角色：

```text
Implementation Owner（主要施工负责人）
Draft Contributor（变更稿贡献者）
Reviewer（评审者）
Project Authority（项目权威决策人）
```

注意：

```text
Role != Permission
Role != Git Identity
Role != Authentication
```

重点协作链：

```text
Draft Change Package
→ Pull Latest Code
→ Reconcile（重新对账）
→ Review
→ Human Decision
→ Canonical Apply（正式真相应用）
→ Archive Draft
```

## 6. Documentation Source of Truth

正式写正文前必须生成：

```text
DOCUMENTATION_SOURCE_OF_TRUTH.yaml
```

至少记录：

```text
实际 CLI
实际 WebUI 页面
实际 Runtime API
实际 Adapter
实际 Skill / Capability
实际 Workflow
实际 Role
实际 Status / Enum
实际 ID / Variable
实际 Directory
实际 Project Instance schema
实际 Git / Permission semantics
```

规则：

```text
文档不能描述实际 Framework 没有的能力。
```

如用户期望与实现不同：

```text
DOC-GAP → 文档修正 或 Enhancement Proposal
```

## 7. 施工阶段

```text
D0 Source of Truth
D1 文档地基
D2 User Guide
D3 Scenario Cookbook
D4 Reference Manual
D5 Maintainer Packaging
D6 Documentation-driven Gap Check
D7 WebUI Help Center
D8 Final Documentation Acceptance
```

## 8. WebUI Help Center

作为单独的 Documentation UX Enhancement，不修改 Python Runtime Core。

入口：

```text
Ant Design Pro Header
→ 使用说明 / Help
→ 新 Tab
→ /help
```

页面：

```text
左侧：Markdown 文件树
中间：Markdown 正文
右侧：Sticky 文档标题目录
```

数据源：

```text
banyan-framework/docs/
```

建议：

```text
Ant Design Tree
Ant Design Anchor
react-markdown
remark-gfm
rehype sanitize
代码高亮
```

Go/Gin 提供本地 Docs API 或 embedded docs。

## 9. 用户需要参与的点

仅以下情况需要人工意见：

```text
1. 团队角色正式命名有歧义
2. 多人协作流程存在多个可选方案
3. 某个 Workflow 默认行为需要产品决策
4. 文档想描述的能力当前 Framework 不存在
5. 是否批准新增 Enhancement
6. 是否接受某些术语的中文正式译名
```

其余由 Documentation Workstream 推进。

## 10. 禁止事项

默认禁止：

```text
修改 Python Runtime Core
修改 Permission / Policy
修改 Git Safety
重构 Project Instance
迁移 docs/project
Final Activation
删除 .banyan-refactor
改变 CURRENT version pointer
```

WebUI Help Center 仅允许修改：

```text
banyan-framework/frontend/**
banyan-framework/control-plane-go/**
banyan-framework/docs/**
```

## 11. 完成标准

```text
普通开发者：看 User Guide / Scenario 就能使用
高级用户：查 Reference 就能知道准确规则
维护者：看 Maintainer 就能维护 Banyan
WebUI：点击“使用说明”即可浏览本地完整文档
自然语言编辑器：用户不需要记 CLI，也能按 Banyan Workflow 工作
```

# Banyan Documentation Packaging — D1 文档地基施工说明 v1.0

## 目标

D1 只建设 Banyan 正式说明文档的语言地基和导航地基，不进入大规模 User Guide / Scenario 正文，不修改 Banyan Core。

D0 已完成并作为唯一事实底座：

```text
banyan-framework/docs/DOCUMENTATION_SOURCE_OF_TRUTH.yaml
banyan-framework/docs/DOCUMENTATION_INVENTORY.md
```

所有 D1 内容必须从 D0 事实出发。不得把规划、冻结合同、用户期望写成已实现能力。

## D1 输出

在 `banyan-framework/docs/` 生成：

```text
README.md
DOCUMENTATION_MAP.md
WRITING_STYLE_GUIDE.md

reference/
├── GLOSSARY_BILINGUAL.md
├── IMPLEMENTATION_STATUS_REFERENCE.md
├── KEY_DOCUMENT_TYPES_REFERENCE.md
├── KEY_IDS_AND_VARIABLES_REFERENCE.md
├── STATUS_AND_ENUM_REFERENCE.md
├── ROLE_REFERENCE.md
├── SKILL_REFERENCE.md
└── WORKFLOW_REFERENCE.md
```

## 必须坚持的事实边界

1. 35 个 `CAP-*` 是 Capability Contract，不是 35 个已安装 Skill。
2. Framework-native Skill 当前为空；实际保留 Skill 是 `anydesign` 与 `visual-repair-loop`，且不属于 Banyan Core。
3. `banyan.workflow.adaptive.v1` 为 `FROZEN_POLICY_NOT_IMPLEMENTED`。
4. `Understand → Collect → Plan → Decide → Execute → Validate → Deliver` 是目标用户旅程，不得写成当前 Runtime 已完整自动编排。
5. 当前 Editor Adapter 仅支持受限动作面，不等于完整自然语言需求编排。
6. Canonical Apply 有冻结合同，但当前 Runtime / Control Plane 没有执行 API。
7. `/help` 尚未实现。
8. `Human Project Authority` 是当前真实治理概念，但不是 Runtime role enum。
9. `Implementation Owner / Draft Contributor / Reviewer` 是文档协作角色，不得描述为 Runtime 授权角色。
10. `RFC`、`TBC` 当前缺少独立冻结定义；可以解释普通工程含义，但必须明确 Banyan 当前未冻结独立 schema/enum。
11. Framework Release、Governance CURRENT pointer、Python package/runtime version 是三个不同版本维度。
12. `.banyan` 仍是 Shadow Pilot；Framework Release 不等于 Project Final Activation。

## 英文术语规则

第一次出现必须写：

```text
英文（推荐中文名：一句面向普通开发者的解释）
```

例如：

```text
Preflight（执行前预检：正式执行动作之前检查权限、风险、前置条件和证据）
Canonical（权威正式来源：冲突时可作为正式事实依据的来源）
```

不能只堆英文名词。

## 实现状态标签

D1 新增统一的说明文档状态语义：

```text
IMPLEMENTED
FROZEN_CONTRACT
PILOT
PLANNED
NOT_IMPLEMENTED
BLOCKED
```

这些是“文档展示标签”，不是擅自新增 Runtime enum。

必须在 `IMPLEMENTATION_STATUS_REFERENCE.md` 中解释：
- 标签的中文意思
- 如何映射 D0 中的实际状态
- 为什么 `FROZEN_CONTRACT != IMPLEMENTED`
- 为什么 `ALLOW != EXECUTED`
- 为什么 `RELEASED != PROJECT_ACTIVATED`

## D1 不做

```text
不修改 Runtime / Policy / Permission / Git
不修改 .banyan
不迁移 docs/project
不实现 /help
不创建大量 user-guide / scenarios
不解决 9 个 DOC-GAP-CANDIDATE
不改变 version pointer
不执行 Final Activation
```

## 完成后停止

D1 完成后输出：
- 文件清单
- 每个文件的主要内容摘要
- D0 事实引用检查结果
- 新增术语中存在歧义、需要 Human Decision 的清单
- 未解决 DOC-GAP-CANDIDATE 清单

然后停止，等待 D1 验收。

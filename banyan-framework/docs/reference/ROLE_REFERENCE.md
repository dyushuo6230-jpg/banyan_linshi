# Role Reference

Role 必须连同所属 context 使用。全局不变量是：

`Role != Permission != Git Identity != Authentication`

角色描述职责或来源地位；Permission 是 Runtime 判定；Git Identity 是提交身份元数据；Authentication 是身份验证。任何一个都不能自动替代另外三个。

## 1. Source Role

Source Role（来源角色）描述 Artifact 在事实判断中的作用，不是人员角色。9 个 frozen roles 是：

- `DECISION_CHANGE_HISTORY`：决策与变更历史；evidentiary，不能静默替代当前 Canonical truth。
- `DERIVED_PROJECTION`：派生投影；source hashes/versions 匹配时才 fresh。
- `OPERATIONAL_HISTORY`：运行历史；低权威证据，不能单独授权当前真相。
- `PROJECT_CANONICAL_DOCUMENT`：项目正式文档；scope 内 primary authority，peer 含混会阻塞。
- `PROJECT_GUIDE_DERIVED`：项目指南派生物；输入引用一致时才 fresh。
- `REQUIREMENT_SOURCE`：需求来源；在声明 scope 内 primary。
- `TECHNICAL_CONTRACT_SOURCE`：技术合同来源；scope 冲突为 blocked。
- `UI_DESIGN_DERIVED`：UI 设计派生物；UI_SPEC source 优先，除非有批准决策。
- `UI_SPEC_SOURCE`：UI_SPEC 来源；产品/技术冲突需要 decision evidence。

状态：`FROZEN_CONTRACT`。Source Role 不授予任何人 Permission。

## 2. Governance Role

`Human Project Authority`（项目人类权威决策方）是当前真实治理概念，用于解决 `CON-002`、批准 version transition，并参与 Final Activation 的独立治理决定。

它不是 Runtime role enum。文档不能把它写成 API 可设置的角色字段，也不能假定某个 Git author、Editor profile 或 Reviewer 自动拥有这项 Authority。

状态：治理概念已被 accepted evidence 使用；Runtime enum 为 `NOT_IMPLEMENTED`。

## 3. Project Instance Contributor Profile

`.banyan/profiles/contributor.yaml` 当前是 Shadow Pilot profile：

- `state: UNKNOWN`
- `identity_values_persisted: false`
- `permission_role: NONE`
- `authorization_source: false`

因此 Contributor Profile 当前既不保存身份值，也不是 Authorization source。状态：`PILOT`。

## 4. Documentation Collaboration Role

以下名称只用于文档描述团队协作职责：

- `Implementation Owner`（主要施工负责人）：协调某项实现工作与交付证据。
- `Draft Contributor`（变更稿贡献者）：在隔离范围内贡献草稿材料。
- `Reviewer`（评审者）：检查提议、证据、影响和边界。

这些是 Documentation Collaboration Role（文档协作角色），不是当前 Runtime role enum，不自动授予 Permission、Authorization、Git Identity 或 Authentication。

Documentation Packaging 总指挥文档还使用 `Project Authority` 名称，而 accepted evidence 使用 `Human Project Authority`。正式中文与二者是否同义需要 Human Decision；在决定前保留各自 context，不合并成 Runtime enum。

## 使用规则

写“某角色可以执行”时，必须另行引用有效 Permission Result 和 Authorization。写“某人提交了代码”时，也不能仅凭 Git Identity 推断其治理 Authority。

参见[术语表](GLOSSARY_BILINGUAL.md)和[状态与枚举参考](STATUS_AND_ENUM_REFERENCE.md)。

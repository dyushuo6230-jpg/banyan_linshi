# Key Document Types Reference

本页区分 Banyan 已有证据支持的文档/Artifact 类型、尚未独立冻结的常见术语，以及根本不是文档类型的标记。状态标签见[实现状态参考](IMPLEMENTATION_STATUS_REFERENCE.md)。

## 已有合同或实际文件证据的类型

- `PRD`：Product Requirements Document（产品需求文档）。产品/业务需求的 Canonical truth；`FROZEN_CONTRACT`。
- `UI_SPEC`：User Interface Specification（界面规格）。批准后且限定 application scope 的 UI contract projection；`FROZEN_CONTRACT`。
- `DEC`：Decision Record（决策记录）。承载有效决策、理由、影响和确认关系。
- `ADR`：Architecture Decision Record（架构决策记录）。记录架构选择及理由；accepted Stage evidence 中存在实际 ADR。
- `CR`：Change Request（变更请求）。在决策和 Change contract 中出现的变更请求类型。
- `UI-DEC`：User Interface Decision（界面决策记录）。用于 UI 范围中的明确决策与冲突收口。
- `Change`：变更对象。具有 Banyan `change_id`、Provider ID、状态和关联关系；lifecycle 为 `FROZEN_CONTRACT`。
- `Draft Change Package`：变更草稿包。供预览、对账、评审和决策的临时变更材料；不会自动晋升为正式来源。
- `Evidence`：证据记录。支持判断、状态或结果的可核验材料；不能单独授权。
- `Trace`：追踪记录。当前有 `IMPLEMENTED` JSONL audit surface；不能单独授权。
- `Project Guide`：项目指南。由 accepted sources 派生的知识投影，需保留 lineage 和 freshness。
- `Handover`：交接记录。保存可恢复上下文、状态、blocker 和后续动作。
- `Worklog`：工作日志。现有项目文档中存在，用于记录过程；过程记录不会自动成为当前权威真相。

## PRD、UI_SPEC 与 Design Source 的边界

PRD 是产品/业务需求 Canonical truth。UI_SPEC 只有在批准后、且仅在声明的应用/表面范围内，才是 UI contract projection。它不能创造第二份业务真相。

Design Source（设计来源，如截图、原型、Figma 或设计素材）是 Evidence。它可以支持 UI_SPEC，但未经有效流程不会自动成为已批准 UI_SPEC，也不能覆盖 PRD。

## 常见但当前 Banyan 未独立冻结

- `RFC`：Request for Comments（征求意见稿）。可以使用普通工程含义，但 D0 未发现独立 frozen Banyan artifact schema。
- `TBC`：To Be Confirmed（待确认）。可以作为普通说明词，但 D0 未发现独立 frozen Banyan enum。

文档使用这两个词时必须附上上述限制，不能将其添加到 Runtime enum。

## 不是文档类型

- `TBD`：To Be Determined（待确定），是 unresolved value marker。它表示值或结论仍未知，不能被静默默认，也不是 Artifact 类型。

参见[术语表](GLOSSARY_BILINGUAL.md)和[状态与枚举参考](STATUS_AND_ENUM_REFERENCE.md)。

# 文档、Source Mapping（来源映射）与知识管理

> 关键术语：Evidence（证据：支持判断的可核验材料）。

## 这篇解决什么问题

说明怎样判断哪份文档是正式来源、哪些是派生内容，以及接入 Banyan 时为什么不需要搬迁现有 `docs/project`。

## 什么时候需要看

多份 PRD、UI_SPEC、ADR、DEC、生成文档或历史记录出现冲突时。

## 核心概念

Canonical（权威正式来源：冲突时可作为正式事实依据的来源）不是“最新文件”的同义词。Derived（派生内容：根据正式来源整理或计算的结果）必须保留 Provenance（来源沿革：内容从哪里来、何时生成）与 Freshness（时效状态：是否仍与有效来源一致）。

Source Mapping（来源映射：把现有来源映射到 Source Role 和目标用途）允许文档 preserve in place（保持原位）。

- PRD：产品/业务需求 Canonical truth。
- UI_SPEC：批准后且限定应用范围的 UI contract projection，不能建立第二份业务真相。
- ADR：架构决策记录。
- DEC：通用决策记录。
- Design Source：Evidence，不自动成为 UI_SPEC 或 PRD。

## 推荐操作方式

1. 先确定 Artifact 的 Stable ID、类型、版本、状态和 Source Role。
2. 记录 Authority、Freshness、Provenance 和 source refs。
3. 冲突时按 scope 与有效决策处理；不靠 mtime 或文件名排序选赢家。
4. 生成 Project Guide、索引或摘要时保留输入引用，使其可以重建。
5. 接入旧文档时使用 Source Mapping；`docs/project` 保持原位，不物理迁移。

## 自然语言示例

> 对这三份需求文档做 Source Mapping。列出各自 Source Role、Authority、Version、Status、Freshness 和 Provenance；有冲突时标记 BLOCKED，不根据文件更新时间选赢家。

## 当前实现状态

Artifact、Source Role、Provenance、PRD/UI_SPEC Authority 与知识投影主要是 frozen contracts。Control Plane 已有受限 Provenance 查询面。`.banyan` mapping 当前是 reference-only Pilot，`docs/project` 为 `PRESERVE_IN_PLACE_NOT_MIGRATED`。

## 常见误区

- generated / index / summary 不是 Canonical truth。
- Git 历史和旧 Worklog 是 Evidence，不自动决定当前 Authority。
- Approved UI_SPEC 只对声明 scope 有效。
- `UNKNOWN` 不能由模型信心替换成确定事实。

## 相关 Reference

- [关键文档类型参考](../reference/KEY_DOCUMENT_TYPES_REFERENCE.md)
- [术语表](../reference/GLOSSARY_BILINGUAL.md)
- [状态与枚举参考](../reference/STATUS_AND_ENUM_REFERENCE.md)

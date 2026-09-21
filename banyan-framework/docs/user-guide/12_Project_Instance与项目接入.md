# Project Instance（项目实例）与项目接入

> 关键术语：Authorization（授权：允许特定范围动作的有效依据）；Gate（门禁：条件不足时阻止下一步）。

## 这篇解决什么问题

解释通用 Banyan 怎样与具体项目连接，以及为什么当前 `.banyan` 仍不能当作正式项目真相。

## 什么时候需要看

旧项目第一次接入、看到 `.banyan` 目录，或准备讨论 Final Activation 时。

## 核心概念

Project Instance（项目实例：把通用 Banyan 与具体项目的来源、变量和 Provider 连接起来的状态集合）包含：

- Source Mapping（来源映射：记录已有来源与目标角色的引用关系）。
- Overlay（项目覆盖层：绑定项目约定，但不能削弱 Core safety floor）。
- Profile（配置档案：描述项目或贡献者状态，不自动授予权限）。
- Provider Binding（能力提供方绑定：把 port 与具体 Provider 连接起来）。
- Shadow Pilot（影子试点：验证结构和连接，但不替代 Canonical truth）。
- Final Activation（最终激活：经过独立治理决定后正式启用 Project Instance）。

## 推荐操作方式

1. 保持现有项目结构与 Canonical source 原位。
2. 用 Source Mapping 引用来源，不为接入而搬迁 `docs/project`。
3. 未知变量保留 `UNKNOWN`；关键未知阻塞依赖动作。
4. Overlay 只表达项目差异，不复制 Core Policy。
5. Provider Binding 只声明连接和能力，不把 Provider 变成 Authority。
6. Pilot 验证通过后，仍需 Human Project Authority、Gate、checkpoint、rollback readiness 和独立 Authorization 才能 Final Activation。

## 自然语言示例

> 只读盘点这个项目接入 Banyan 所需的 Source Mapping、Overlay、Profile 和 Provider Binding。保持现有目录原位，不创建或修改 `.banyan`，不要执行 Final Activation。

## 当前实现状态

`.banyan` 有 13 个 Stage 17 Pilot 文件，Stage 20 总状态为 `PROJECT_INSTANCE_SHADOW_PILOT`。`canonical_truth=false`、`canonical_replacement=false`、`docs_project_migration=NOT_PERFORMED`、`git_mutation=NOT_AUTHORIZED`。Final Activation 为 `NOT_AUTHORIZED`，`CON-002` 仍被 Human Project Authority 阻塞。

## 常见误区

- `.banyan` 存在不等于已经激活。
- Framework Release 不等于 Project Instance Final Activation。
- generated / index 内容不是 Canonical truth。
- Provider Binding 不授予 Provider Git mutation 或 Canonical write 权限。

## 相关 Reference

- [术语表](../reference/GLOSSARY_BILINGUAL.md)
- [关键 ID 与变量参考](../reference/KEY_IDS_AND_VARIABLES_REFERENCE.md)
- [角色参考](../reference/ROLE_REFERENCE.md)

# WebUI（网页控制界面）使用手册

> 关键术语：Authorization（授权：允许特定范围动作的有效依据）；Gate（门禁：条件不足时阻止下一步）；Final Activation（最终激活：正式启用 Project Instance 的独立治理动作）；Provenance（来源沿革：内容从哪里来、经过什么处理）；Permission（权限判定：Runtime 根据 Policy 给出的结论）。

## 这篇解决什么问题

说明当前 WebUI 的 12 个真实页面、能查看或提交什么，以及它不具备哪些权限。

## 什么时候需要看

希望用浏览器查看 Runtime、Policy、项目安全、Trace 或 dry-run 结果时。

## 核心概念

WebUI（网页控制界面：本地展示 Runtime typed result 并提交受限请求）由 Ant Design Pro Simple 构建，静态资源嵌入 Go/Gin Control Plane（控制面：本地转发请求到 Python Runtime）。它只允许 loopback 访问，不授予 Authorization。

## 推荐操作方式

当前实际页面恰好 12 个：

1. `/dashboard`：Runtime status。
2. `/runtime-policy`：Policy status。
3. `/project-safety`：分支、HEAD、变更数量和 identity 是否齐全，不展示 identity 值。
4. `/gate-blockers`：从 status 查看 Gate / blocker 摘要。
5. `/preflight`：提交执行前预检意图。
6. `/commit-plan`：生成语义提交计划。
7. `/dry-run-result`：查看提交 dry-run 结果。
8. `/trace-audit`：分页查看 Trace / Audit。
9. `/provenance`：按 Stable ID 查看 Provenance。
10. `/provider-bindings`：查看 Provider binding。
11. `/stage-run`：分页查看 Stage / Run。
12. `/activation-readiness`：查看激活准备度与 blocker；不执行激活。

把 WebUI 返回值当成 Runtime 结果阅读。需要写入或治理动作时，仍要满足相应 Permission、Authorization 和 Gate。

## 自然语言示例

> 请帮我解释 WebUI `/activation-readiness` 返回的 blockers，只做事实解读，不执行激活。

## 当前实现状态

以上 12 个页面与对应 HTTP API 已实现。`/help` Help Center 尚未实现，是 D7 Documentation UX Enhancement。WebUI 当前项目 Git mutation 为 `DISABLED`。

## 常见误区

- 页面中的 Intent note 或点击按钮不构成 Authorization。
- `/commit-plan` 不会提交代码；`/dry-run-result` 不创建 commit。
- `/activation-readiness` 只报告准备度，不执行 Final Activation。
- 当前没有 `/help`，不要把未来页面当作已上线入口。

## 相关 Reference

- [实现状态参考](../reference/IMPLEMENTATION_STATUS_REFERENCE.md)
- [状态与枚举参考](../reference/STATUS_AND_ENUM_REFERENCE.md)
- [术语表](../reference/GLOSSARY_BILINGUAL.md)

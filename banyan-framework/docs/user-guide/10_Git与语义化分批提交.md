# Git 与语义化分批提交

> 关键术语：Authorization（授权：允许特定范围动作的有效依据）；Decision（决策：对选项作出的明确选择）；Gate（门禁：条件不足时阻止下一步）；Permission（权限判定：Runtime 根据 Policy 给出的结论）；Trace（追踪记录：动作和结果的审计记录）。

## 这篇解决什么问题

把混在工作树里的改动按含义分组，避免把未完成、无关、本地专用或敏感文件误提交。

## 什么时候需要看

准备交付、需要 commit plan，或工作树中同时存在多类改动时。

## 核心概念

Semantic Commit（语义化提交：按变更含义而非文件出现顺序分组的提交）使用 5 个真实分类：

- `READY`：范围内完整变化，已完成所需验证且无 blocker；可成为语义分组候选。
- `INCOMPLETE`：实现、依赖、验证或 Decision 不完整；默认保留。
- `UNRELATED`：不属于当前任务；隔离并报告。
- `LOCAL_ONLY`：机器本地、bootstrap-only 或明确不可提交内容；永不提交。
- `SECRET_RISK`：凭证、疑似敏感配置或未确认泄露；硬阻塞，绝不自动 stage / commit。

## 推荐操作方式

1. 先检查变更路径、staged/unstaged/untracked/conflicted 数量。
2. 对每个路径明确分类；未分类路径在当前 planner 中默认 `INCOMPLETE`。
3. 只把 `READY` 按语义分组，写与实际内容一致的 message。
4. 报告所有 leftovers；`SECRET_RISK` 必须先处理风险。
5. 检查 Git Identity 是否存在，但 AI 不猜操作者、不根据历史作者补值，也不修改 `--author`。
6. 使用显式路径或 hunk plan；不要盲目运行 `git add .`、`git add -A` 或 `git add --all`。
7. 当前项目只查看 commit dry-run；不要声称已创建 commit。

## 自然语言示例

> 检查当前改动并按 READY、INCOMPLETE、UNRELATED、LOCAL_ONLY、SECRET_RISK 分类。只生成语义分组和 leftovers，不 stage、不 commit，不修改 Git identity。

## 当前实现状态

Git inspect、deterministic commit plan 和 current-project dry-run 已实现。真实 commit execution 只允许显式 isolated fixture root，并需要 identity、Authorization、secret check、精确 staged set、Trace 和 rollback。网络 Git 操作被禁用。

## 常见误区

- Commit Plan 不是 Authorization。
- Git Identity 不是 Permission，也不证明 Human Project Authority。
- `READY` 仍需 validation、identity 和 Authorization 才具备提交资格。
- dry-run 返回 `ALLOW` 也不会创建 commit。

## 相关 Reference

- [状态与枚举参考](../reference/STATUS_AND_ENUM_REFERENCE.md)
- [权限、Gate 与安全](14_权限_Gate与安全.md)
- [工作流参考](../reference/WORKFLOW_REFERENCE.md)

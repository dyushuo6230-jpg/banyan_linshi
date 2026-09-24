# 01-I：Git Identity 与 AI 提交现状盘点

> 本阶段只发现，不定义最终 Commit Policy。

## 1. Identity 事实

冻结语义：

```text
Git Commit Author name + email
= Banyan Contribution Identity
```

Stage 01 不追踪真实物理操作者。

## 2. 要盘点什么

### Git Identity

- 当前可解析 Git identity（只读）；
- 历史 Author `name + email`；
- 历史 Committer 差异；
- identity 数量与活跃时间；
- 不自动 Alias/Merge。

### Commit Message

统计：

- 常见 subject 格式；
- type/scope；
- 中英文；
- issue/PR reference；
- trailers；
- merge/revert patterns。

### Commit Enforcement

发现：

```text
commit-msg hook
pre-commit hook
lint rule
CI check
release tooling
changelog tooling
```

### AI Commit

发现：

```text
Cursor/Codex/Claude rules
Prompt
Skill
Script
Command
“分批提交”相关脚本/习惯
```

## 3. 统计范围

Stage 01 可根据 Repository 规模决定：

```text
全历史
或
全历史 metadata + 代表性 message sampling
```

但必须记录：

```text
analysis_window
commit_count
coverage_reason
limitations
```

不得伪称“全历史”却只分析最近少量 commit。

## 4. 禁止动作

Stage 01 不：

- 修改 `user.name/user.email`；
- 生成 Contributor Profile；
- 合并多个 identity；
- 定义 role_labels；
- 冻结 Conventional Commit；
- 冻结 Trailer；
- 自动 commit；
- 执行 Semantic Commit Planner。

## 5. 输出

`GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml`

供 Stage 02/03/04/05/15 使用。

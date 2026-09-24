# 00-A：Repository Baseline 与 Protected Paths

> Charter：v1.9.1 FINAL_FREEZE  
> Owner：Stage 00  
> 本文只定义“安全边界与保护分类”，不执行迁移。

---

# 1. 目的

把“当前仓库”从模糊概念变成可验证边界：

```text
Repository 到底在哪
哪些 Root 属于当前 Repository
是否存在 Worktree / Submodule / Nested Repo
当前 Git 状态是什么
哪些范围后续需要扫描
哪些范围当前绝不能写
Stage 00 自己允许写到哪里
```

---

# 2. Repository Baseline 最小模型

至少：

```yaml
repository:
  root:
  topology:
  branch:
  head:
  detached:
  upstream_present:
  dirty:
  git_operation:
  worktrees:
  submodules:
  nested_repositories:
  sparse_checkout:
  lfs:
```

Remote：

```text
默认只记录 remote name / presence
```

不要把可能包含 credential 的完整 URL 直接写进 Evidence。

---

# 3. Working Tree State

至少区分：

```text
STAGED
UNSTAGED
UNTRACKED
IGNORED_GOVERNED
DELETED
RENAMED
UNMERGED
BINARY_CHANGED
```

规则：

```text
UNMERGED > 0
→ BLOCK
```

Dirty 本身不等于失败；关键是 Recovery Coverage 是否可信。

---

# 4. Repository Topology

必须识别：

```text
SINGLE_REPO
MONOREPO
NESTED_REPOSITORIES
LINKED_WORKTREE
SUBMODULES
SPARSE_CHECKOUT
OTHER
```

Stage 00：

- 可以发现边界；
- 可以记录；
- 不隐式跨 repo 写；
- 不把 nested repo 内容错误纳入父 repo 的可写范围。

---

# 5. Protected Path Classes

## 5.1 `IMMUTABLE_DURING_REFACTOR`

在没有对应 Owner Stage / Gate 明确放行前不可写。

典型：

```text
业务源代码
SQL / migration
生产配置
正式 Canonical Project Docs
Approved / Baselined Artifacts
发布/部署关键脚本
```

## 5.2 `READ_ONLY_DISCOVERY`

允许读取用于 Stage 01/后续盘点，但 Stage 00 不写。

典型：

```text
Legacy prompts
Legacy rules
Legacy skills
historical governance docs
UI governance assets
reference materials
```

## 5.3 `STAGE_WRITABLE`

Stage 00 默认只允许：

```text
REFRACTOR_CONTROL_ROOT
```

以及 Repository 外的临时捕获目录。

## 5.4 `CONDITIONAL_WRITE_LATER`

未来 Owner Stage 可能写，但当前不能。

必须包含：

```text
future .banyan Project Instance
.banyan/migrations/*
generated adapter outputs
future index/runtime outputs
```

## 5.5 `SECRET_METADATA_ONLY`

只允许：

```text
exists
path
classification
recovery_mode
```

禁止正文读取/复制。

## 5.6 `EXCLUDED_WITH_REASON`

表示不进入默认正文 Discovery，例如：

```text
node_modules
vendor/cache
build/dist/cache
large reproducible outputs
```

但：

> `EXCLUDED_WITH_REASON` 不代表 Stage 00 可以修改或删除它。

---

# 6. Classification Precedence

同一 Path 命中多个规则：

```text
SECRET_METADATA_ONLY
>
IMMUTABLE_DURING_REFACTOR
>
READ_ONLY_DISCOVERY
>
CONDITIONAL_WRITE_LATER
>
STAGE_WRITABLE
>
EXCLUDED_WITH_REASON
```

Secret 的内容访问约束永远最高优先级。

---

# 7. Discovery Scope ≠ Protected Paths

一个 Path 可以：

```yaml
discovery_mode: SCAN
write: false
```

这不是冲突。

例如：

```text
Canonical PRD
Legacy AI Rules
Business Code
```

后续为了 No-Loss 可以读取，但 Stage 00 不可写。

---

# 8. 自动分类依据

执行器可以参考：

- Git tracked state；
- top-level roots；
- README / AGENTS / editor rules；
- AI / prompts / rules / skills / tools；
- docs / governance；
- package/module roots；
- SQL / migrations；
- production/deploy config；
- formal artifact metadata；
- ignored roots；
- symlink / submodule / worktree；
- v1.9.1 Seed Facts。

但最终 Manifest：

> **必须使用真实路径，不得只写抽象类别。**

---

# 9. Git Identity 不属于 Protected Path 业务模型

Stage 00 不修改：

```text
git config user.name
git config user.email
commit author
```

Git identity 只作为环境事实读取；真正 Semantic Commit / Provenance 能力从后续 Stage 建设。

---

# 10. Bootstrap Control Root 特殊规则

`REFRACTOR_CONTROL_ROOT` 是 Stage 00 的唯一 Repo 内默认写入区。

如果默认候选：

```text
${REPO_ROOT}/.banyan-refactor/
```

则必须：

```text
bootstrap_only = true
```

正式：

```text
.banyan/migrations/**
```

此时仍应：

```text
CONDITIONAL_WRITE_LATER
```

不得把它提前设为 `STAGE_WRITABLE`。

---

# 11. 不允许的做法

禁止：

```yaml
writable:
  - "**"
```

禁止因为：

```text
“后面 Stage 会迁”
```

就提前解保护。

禁止因为：

```text
ignored
generated
temporary
```

就默认认为没有治理价值。

Generated Artifact 也可能是后续 No-Loss Audit 输入。

---

# 12. Manifest 最小字段

见：

```text
templates/PROTECTED_PATHS_MANIFEST.template.yaml
```

每条至少：

```yaml
path:
class:
read:
write:
delete:
discovery_mode:
reason:
owner_stage:
source:
```

---

# 13. Stage 01 消费规则

Stage 01：

- 按 `SCAN` 读取正文；
- `METADATA_ONLY` 不读取正文；
- `EXCLUDE_WITH_REASON` 不扫描，除非 Plan Change；
- 不得因为盘点方便突破 Protected Paths；
- 发现分类缺陷时记录问题并按后续 `REFRACTOR_PLAN_CHANGE` 规则受控处理，不能静默改上游规则后继续。

---

# 14. 验收标准

合格不是“保护越多越好”，而是：

```text
真实重要资产有保护
+
Stage 00 没拿到不必要写权限
+
Stage 01 能完成只读 Discovery
+
Secret 不泄露
+
未来 Owner Stage 可以受控解锁
+
Bootstrap / Canonical 边界明确
```

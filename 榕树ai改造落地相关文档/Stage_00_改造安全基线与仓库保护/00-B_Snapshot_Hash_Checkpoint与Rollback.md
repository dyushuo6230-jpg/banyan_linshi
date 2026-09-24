# 00-B：Snapshot、Hash、Checkpoint 与 Rollback

> Charter：v1.9.1 FINAL_FREEZE  
> Owner：Stage 00  
> Stage 00 建立恢复能力，但不做破坏性恢复演练。

---

# 1. 四个概念必须分开

## Snapshot
记录某个时间点的 Repository 状态描述。

## Hash Baseline
证明受管文件后续是否发生变化。

## Checkpoint
保存足够恢复信息，保护当前未提交工作。

## Rollback
真正执行恢复动作。

Stage 00 建立前三者和 Rollback 方法，**默认不执行第四者**。

---

# 2. Snapshot 最少内容

```text
Repository Root
Branch
HEAD
Detached State
Git Status
Active Git Operation
Worktree
Submodule / Nested Repo
Sparse Checkout / LFS
Discovery Scope
Protected Paths
Control Root
RUN_ID
Timestamp
```

Snapshot 不要求复制整个 Repository。

---

# 3. Hash Baseline

默认：

```text
SHA-256
```

记录：

```text
relative_path
hash
size
kind
tracked_state
protection_class
discovery_mode
```

无法 Hash：

```text
METADATA_ONLY
+
reason
```

禁止伪造 hash。

---

# 4. Hash Scope

优先覆盖：

- tracked regular files；
- relevant untracked governance/project files；
- ignored-but-governed non-secret files；
- AI / docs / scripts / tools / editor config；
- 后续 No-Loss Audit 需要的源 Artifact。

可排除：

- node_modules；
- vendor cache；
- build/dist/cache；
- Secret 正文；
- repo 外 symlink target；
- 超大、可再生、无治理价值二进制。

每个排除都要有 reason。

---

# 5. Pre-stage Baseline 污染防护

必须：

```text
先在 Repo 外捕获 PRE_STAGE_GIT_STATUS
↓
再创建 REFRACTOR_CONTROL_ROOT
```

否则 Stage 00 自己新建的：

```text
.banyan-refactor/
```

可能污染“改造前”的工作区事实。

Pre-stage Hash Scope 也必须区分：

```text
PROJECT_BASELINE_SCOPE
vs
STAGE_CONTROL_OUTPUT
```

Stage 自身产物不能被当成“原项目已有资产”。

---

# 6. Dirty Tracked Checkpoint

需要保存：

```text
staged.patch
unstaged.patch
```

要求：

- binary-capable；
- 能表达 rename/delete；
- patch 自身 SHA-256；
- 记录生成命令/方式；
- 不自动 apply/reverse。

---

# 7. Relevant Untracked Checkpoint

只有：

```text
filename + hash
```

不足以恢复。

必须：

```text
Inventory
+
Backup / Archive
+
Archive Hash
+
Relative Path Preservation
```

但 Secret 例外：

```text
USER_MANAGED_SECRET_RECOVERY
```

不得进普通 archive。

---

# 8. Ignored-but-Governed

`ignored != disposable`

如果属于：

```text
Legacy Draft
AI Runtime State
Handover
Generated Governance
Local Governance State
```

且后续迁移有价值，则：

```text
Discovery
+
Checkpoint / Recovery Strategy
```

不能因为 `.gitignore` 静默漏掉。

---

# 9. Secret Recovery

Stage 00 不创建 Secret Vault。

允许：

```text
path
exists
classification
recovery_mode
```

禁止：

```text
原值读取
报告回显
普通 archive
普通 hash manifest 明文内容
```

如果当前未提交 Secret 变化是恢复完整性的关键，但没有安全恢复方式：

```text
NEEDS_INPUT / BLOCK
```

---

# 10. Checkpoint Coverage

枚举：

```text
COMPLETE
PARTIAL_APPROVED
INCOMPLETE
```

默认 Exit Gate：

```text
COMPLETE
```

`PARTIAL_APPROVED`：

- 必须用户明确批准；
- 必须在 Acceptance 中写出遗漏与后果；
- 不得描述为无风险。

`INCOMPLETE`：

```text
BLOCK
```

---

# 11. Rollback Levels

```text
R0
撤销/归档 Stage 自己创建的 Control Artifact

R1
撤销后续 Stage 的局部生成物

R2
恢复 tracked working tree checkpoint

R3
恢复 untracked / governed ignored checkpoint

R4
恢复 initial baseline HEAD + initial dirty state
```

R2～R4 风险较高。

真正执行前：

```text
Restore Plan
→ Compare Current State
→ Detect Post-baseline User Work
→ Human Confirmation where required
→ Minimal Restore
→ Revalidate
```

---

# 12. 为什么不自动 stash

`git stash` 可能：

- 漏 ignored；
- 改变用户当前状态；
- 在 worktree/submodule 场景产生歧义；
- stash pop/drop 产生额外风险。

所以 Stage 00：

> 使用独立 checkpoint artifact，不自动 stash。

---

# 13. 为什么不自动 commit/tag

Stage 00 默认：

```text
NO COMMIT
NO TAG
NO PUSH
```

原因：

- 安全基线不应该替用户制造业务历史；
- v1.9.1 的 Semantic Commit Runtime 尚未建设；
- Stage 00 只读 Git Identity，不修改身份。

---

# 14. Bootstrap Register / Trace 也要可迁移

Bootstrap 状态文件不是最终物理真源，但必须可验证迁移。

Stage 00 记录：

```yaml
bootstrap:
  control_root:
  register_path:
  trace_path:
  register_sha256:
  trace_sha256:
  future_canonical_paths:
  lineage_required: true
  dual_writable_truth_forbidden: true
```

未来正式迁移必须保留：

```text
source hash
source run id
migration timestamp
target hash
validation evidence
```

Stage 00 本身不执行这次未来迁移。

---

# 15. Recovery Validation

Stage 00 不在真实工作区做破坏性恢复演练。

只验证：

```text
Checkpoint Artifact 存在
Artifact Hash 可验证
Coverage 完整
Relative Path 可恢复
Secret Recovery 明确
Restore Instructions 明确
```

完整 Disaster Recovery / Rollback Rehearsal 属于后续 Final Acceptance。

---

# 16. 实际输出

```text
BASELINE_MANIFEST.yaml
FILE_HASHES.sha256
CHECKPOINT_RECORD.yaml
checkpoint/**
evidence/**
MIGRATION_REGISTER.bootstrap.yaml
BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

模板只定义结构，不表示已执行。

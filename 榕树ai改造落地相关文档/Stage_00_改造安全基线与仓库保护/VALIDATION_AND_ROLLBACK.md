# Stage 00 — VALIDATION AND ROLLBACK

> Pack Version：1.9.1  
> 目标：证明“改造起点可信、受保护、可恢复”，不是证明 Banyan Runtime 已经可用。

---

# 1. Mandatory Validation Matrix

| ID | Check | PASS Condition |
|---|---|---|
| V00-01 | Repository Boundary | Repo Root 明确；worktree/submodule/nested repo 无未解释边界 |
| V00-02 | Git State | branch/HEAD/detached/status 已记录 |
| V00-03 | Git Operation | 无 unresolved merge/rebase/cherry-pick/revert/unmerged |
| V00-04 | Discovery Coverage | SCAN/METADATA_ONLY/EXCLUDE_WITH_REASON 全有依据 |
| V00-05 | Governed Ignored | ignored-but-governed 没被静默漏掉 |
| V00-06 | Protected Paths | business/canonical/legacy/future canonical path 未被 Stage 00 误设 writable |
| V00-07 | Secret Safety | 无 Secret 原值读取、报告回显或普通 checkpoint 复制 |
| V00-08 | Hash Coverage | Managed Scope 有完整 integrity 记录；排除有理由 |
| V00-09 | Dirty Checkpoint | 重要 Dirty 状态可恢复；coverage 满足 Exit Gate |
| V00-10 | Binary Changes | tracked binary 变化的 checkpoint/recovery 方式明确 |
| V00-11 | Untracked | relevant untracked 有 inventory + safe backup/recovery |
| V00-12 | Stage Write Scope | Pre/Post 只有预期 Stage-owned writes，无项目越界写 |
| V00-13 | Manifest Parse | YAML/文本产物可解析；引用路径存在或合理声明未来路径 |
| V00-14 | Bootstrap Trace/Register | Bootstrap 状态已登记；future canonical path / lineage / single-writable-truth 规则完整 |
| V00-15 | Handoff | Acceptance 含完整 NEXT_STAGE_HANDOFF，Stage 01 inputs/gate 明确 |

任一 Critical FAIL：

```text
Stage 00 != COMPLETED
Stage 01 = NOT_ALLOWED
```

---

# 2. Pre/Post Safety Diff

比较：

```text
PRE_STAGE_GIT_STATUS.txt
POST_STAGE_GIT_STATUS.txt
```

允许：

```text
预期 REFRACTOR_CONTROL_ROOT Stage-owned Output
```

不允许：

```text
业务代码新增 modified/deleted/renamed
Canonical Docs 被改
Legacy Rules/Prompt/Skill 正文被改
SQL/Production Config 被改
现有 editor canonical entry 被改
Git Identity 配置被改
正式 .banyan/migrations 被提前创建为 writable truth
```

发现异常：

```text
STOP
→ preserve evidence
→ classify source
→ do not enter Stage 01
```

不要用 destructive Git 命令自动擦掉异常。

---

# 3. Checkpoint Completeness

## Clean Worktree

```text
HEAD known
status known clean
recovery.coverage = COMPLETE
```

## Dirty Tracked

```text
staged patch if needed
unstaged patch if needed
binary-capable
artifact sha256
relative path semantics preserved
```

## Relevant Untracked

```text
inventory
backup/archive
backup sha256
```

## Ignored-but-Governed

同样要求恢复覆盖。

## Secret

```text
metadata-only
USER_MANAGED_SECRET_RECOVERY
```

若关键恢复依赖 Secret 正文而无安全路径：

```text
BLOCK
```

---

# 4. Hash Validation

验证：

- algorithm = SHA-256；
- Stage output 未混入 pre-stage project baseline；
- external symlink 未被 dereference；
- excluded root 有 reason；
- metadata-only 有 reason；
- Secret entry 不含 value/content；
- path 表达可用于后续 Stage 重验。

---

# 5. Bootstrap State Validation

实际 Bootstrap Register / Trace 必须声明：

```text
bootstrap_only = true
control_root
run_id
charter_version = 1.9.1
future canonical paths
lineage_required = true
dual_writable_truth_forbidden = true
```

并且当前不存在：

```text
Bootstrap writable truth
+
Canonical .banyan/migrations writable truth
```

并行更新。

---

# 6. Rollback 的两种语义

## 6.1 Rollback Stage 00 自己

Stage 00 正常只写 Control Root。

优先：

```text
停止后续 Stage
保留 Evidence
生成 cleanup/archival plan
经用户确认后归档/清理 Stage-owned Output
```

不动业务文件。

## 6.2 未来 Stage 使用 Stage 00 Checkpoint

真正：

```text
git restore
patch apply/reverse
恢复 untracked
删除后续输出
```

属于恢复动作，不由 Stage 00 自动执行。

执行前：

```text
Restore Plan
→ compare current state
→ detect newer user work
→ approval where needed
→ minimal restore
→ validate
```

---

# 7. 禁止的默认 Rollback

禁止默认自动：

```bash
git reset --hard
git clean -fd
git clean -fdx
git checkout -- .
git restore .
```

这些可能破坏用户工作。

---

# 8. Rollback Point Record

至少：

```text
rollback_point_id
baseline_head
working_tree_state_hash / equivalent snapshot identifier
checkpoint_artifacts
checkpoint_artifact_hashes
created_at
recovery_coverage
bootstrap_register_hash
bootstrap_trace_hash
```

---

# 9. Exit Decision

## PASS

```text
V00-01..15 PASS
AND
actual artifacts complete
AND
recovery trustworthy
AND
no unexpected write
AND
bootstrap state/trace trustworthy
AND
Acceptance actual
AND
NEXT_STAGE_HANDOFF complete
AND
Stage 01 Entry Gate PASS
```

## BLOCKED

存在可解决但尚未解决的风险：

```text
Stage 00 = BLOCKED
Stage 01 = NOT_ALLOWED
```

## FAIL

例如：

- Stage 00 自己越界修改；
- checkpoint 不可信；
- Secret 泄露风险；
- evidence 被污染/伪造；
- Bootstrap/Canonical 双真源出现。

则：

```text
Stage 00 = FAIL
立即停止
```

---

# 10. Acceptance 要求

真实 `ACCEPTANCE_REPORT.md` 至少：

- execution identity；
- actual artifacts + hashes；
- repository baseline；
- discovery coverage；
- protected path summary；
- hash coverage；
- checkpoint coverage；
- secret handling；
- V00-01～15；
- actual modified files；
- protected important files confirmed untouched；
- open risks；
- rollback point；
- Bootstrap Register / Trace；
- `NEXT_STAGE_HANDOFF`；
- Stage 01 Entry Gate。

禁止：

```text
template 直接改名
+
没有 Evidence
+
写 PASS
```

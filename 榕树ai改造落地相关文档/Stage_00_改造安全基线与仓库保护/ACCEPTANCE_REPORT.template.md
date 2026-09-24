# Stage 00 — ACCEPTANCE REPORT TEMPLATE

> **模板，不是实际 Acceptance Report。**  
> 真实执行完成后必须新建 `ACCEPTANCE_REPORT.md` 并引用真实 Evidence。  
> 禁止预填 PASS，禁止仅复制本模板改名。

---

# 1. Execution Identity

- Stage: `00`
- Pack Version: `1.9.1`
- Charter Version: `1.9.1`
- Run ID:
- Repository Root:
- Baseline HEAD:
- Branch:
- Started At:
- Finished At:
- Executor:

---

# 2. Result

```text
NOT_EXECUTED / PASS / BLOCKED / FAIL
```

Reason:

---

# 3. Actual Artifacts

| Artifact | Actual Path | SHA-256 / Integrity Ref | Result |
|---|---|---|---|
| BASELINE_MANIFEST.yaml | | | |
| PROTECTED_PATHS_MANIFEST.yaml | | | |
| DISCOVERY_SCOPE_BASELINE.yaml | | | |
| CHECKPOINT_RECORD.yaml | | | |
| FILE_HASHES.sha256 | | | |
| PRE_STAGE_GIT_STATUS.txt | | | |
| POST_STAGE_GIT_STATUS.txt | | | |
| MIGRATION_REGISTER.bootstrap.yaml | | | |
| BANYAN_REFACTOR_TRACE.bootstrap.yaml | | | |

Conditional checkpoint/evidence:

| Artifact | Path | Hash | Why Needed |
|---|---|---|---|

---

# 4. Repository Baseline

- Topology:
- Branch:
- HEAD:
- Detached:
- Dirty Before:
- Dirty After:
- Active Git Operation:
- Worktrees:
- Submodules:
- Nested Repositories:
- Sparse Checkout:
- LFS:

---

# 5. Discovery Coverage

- SCAN roots:
- METADATA_ONLY roots:
- EXCLUDE_WITH_REASON roots:
- Governed ignored roots:
- Unexplained exclusion count:
- Silently ignored governed root count:

---

# 6. Protected Paths

| Class | Count | Representative Paths | Notes |
|---|---:|---|---|
| IMMUTABLE_DURING_REFACTOR | | | |
| READ_ONLY_DISCOVERY | | | |
| STAGE_WRITABLE | | | |
| CONDITIONAL_WRITE_LATER | | | |
| SECRET_METADATA_ONLY | | | |
| EXCLUDED_WITH_REASON | | | |

Assertions:

```text
whole_repo_writable = false
stage00_business_code_write_allowed = false
stage00_canonical_truth_write_allowed = false
git_identity_write_allowed = false
future_canonical_migrations_write_allowed = false
```

---

# 7. Hash Coverage

- Algorithm:
- Managed entries:
- Hashed:
- Metadata-only:
- Excluded:
- Unexplained:
- External symlink dereferenced: `false / true`
- Stage control output mixed into pre-stage baseline: `false / true`

---

# 8. Checkpoint

- Recovery Coverage: `COMPLETE / PARTIAL_APPROVED / INCOMPLETE`
- Staged Patch:
- Unstaged Patch:
- Binary Coverage:
- Untracked Backup:
- Ignored-but-Governed Backup:
- Secret Recovery Mode:
- Checkpoint Integrity Result:

---

# 9. Validation

| ID | Result | Evidence | Notes |
|---|---|---|---|
| V00-01 | | | |
| V00-02 | | | |
| V00-03 | | | |
| V00-04 | | | |
| V00-05 | | | |
| V00-06 | | | |
| V00-07 | | | |
| V00-08 | | | |
| V00-09 | | | |
| V00-10 | | | |
| V00-11 | | | |
| V00-12 | | | |
| V00-13 | | | |
| V00-14 | | | |
| V00-15 | | | |

---

# 10. Actual Modified Files

列出 Stage 00 **实际写过** 的全部文件/目录。

```text
...
```

---

# 11. Important Protected Areas Confirmed Untouched

```text
...
```

---

# 12. Open Risks / Blockers

```text
NONE
```

或逐项列出：

- ID:
- Severity:
- Description:
- Impact:
- Required action:

---

# 13. Rollback Point

- ID:
- Baseline HEAD:
- Recovery Coverage:
- Checkpoint Location:
- Checkpoint Hashes:
- Validation:
- Destructive Auto Restore Allowed: `false`

---

# 14. Bootstrap State / Trace

- REFRACTOR_CONTROL_ROOT:
- Bootstrap Register:
- Bootstrap Trace:
- Bootstrap-only: `true`
- Future Canonical Paths:
  - `.banyan/migrations/MIGRATION_REGISTER.yaml`
  - `.banyan/migrations/BANYAN_REFACTOR_TRACE.yaml`
- Lineage Required: `true`
- Dual Writable Truth Forbidden: `true`
- Bootstrap Hashes:
- Future Migration Obligation Recorded: `true / false`

---

# 15. NEXT_STAGE_HANDOFF

## 15.1 Upstream

- Stage: `00`
- Run ID:
- Acceptance Result:

## 15.2 Actual Artifacts Stage 01 Must Consume

```text
...
```

## 15.3 Evidence Stage 01 Can Trust

```text
...
```

## 15.4 Unresolved Risks

```text
NONE
```

或逐项列出。

## 15.5 Protected / Allowed Scope Changes

```text
...
```

## 15.6 Rollback Point

- ID:
- Location:

## 15.7 Stage 01 Entry Gate

```text
PASS / FAIL
```

Reason:

---

# 16. Final Declaration

只有真实 Evidence 支持时才能填写：

```text
Stage 00 = COMPLETED
Stage 01 = ALLOWED
```

否则必须保持：

```text
BLOCKED / FAIL / NOT_ALLOWED
```

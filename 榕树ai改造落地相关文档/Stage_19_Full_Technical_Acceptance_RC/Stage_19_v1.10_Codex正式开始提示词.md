# Stage 19 v1.10 — Codex 正式开始提示词
## Full Technical Acceptance / Release Candidate

Stage18.5 已通过；现在执行 Stage19。

这不是实现新功能，也不是重跑 Stage01～18。

## 1. 读取

先读：

```text
Stage_18.5_to_Stage_19_Gate_Review_v1.0.md
Stage_19_低Token输入索引_v1.0.md
Stage_19_Full_Technical_Acceptance_RC/
```

然后按低 Token 索引读取各 Stage 的 Acceptance / Coverage / Handoff。

## 2. Evidence-first

不要 full rediscovery。

每个 Stage19 acceptance claim 必须绑定证据。

只有发生：

```text
claim/evidence mismatch
hash mismatch
contract drift
regression
```

才做定点源码/项目验证。

## 3. Final Architecture

必须按实际最终架构验收：

```text
Ant Design Pro Simple
→ Go/Gin + go:embed
→ LOCAL_STDIO Runtime Bridge
→ Stage15 Python Banyan Runtime Core
```

不要把 Go 错判为 Runtime Core。

## 4. Critical Revalidation

必须重新执行关键回归：

```text
policy compile fail-closed
permission hard blocks
semantic commit safety
Git no-mutation
Go/Gin transport-only
Runtime Bridge fail-closed
WebUI 12-feature equivalence
embedded assets
Cursor/Codex/Generic adapters
Pilot .banyan integrity
Trace / provenance
```

## 5. Purity

对 `banyan-framework/**` 做 generic purity 验证。

禁止当前项目：

```text
business literals
hardcoded project paths
project ports
identity values
secret values
project-specific authority semantics
```

Project-specific fixture/evidence必须与 generic source 明确隔离。

## 6. No-Loss / Index

优先使用既有 coverage/rebuild evidence。

不要重扫所有 Legacy，除非证据出现冲突。

## 7. Blockers

保持：

```text
CON-002 = TYPED_BLOCKED_HUMAN_PROJECT_AUTHORITY
FINAL_ACTIVATION = NOT_AUTHORIZED
```

Stage19 不替 Human Project Authority 做 winner decision。

## 8. RC

生成 RC manifest，执行 documented release builds / tests / smoke。

RC ≠ Final Activation。

## 9. Mutation

禁止：

```text
current-project Git mutation
project canonical write
Pilot .banyan migration
secret body access
silent acceptance repair
```

如果发现缺陷，记录 FAIL/BLOCKED/typed remediation，不要为了让验收 PASS 偷偷修。

## 10. Validation

执行：

```text
V19-01..V19-32
```

16 项 Hard Metrics 必须为 0。

## 11. Completion

生成至少：

```text
ACCEPTANCE_REPORT.md
STAGE19_EVIDENCE_REGISTRY.yaml
RC_MANIFEST.yaml
STAGE20_HANDOFF.yaml
evidence/STAGE19_COVERAGE_REPORT.yaml
evidence/FINAL_VERIFICATION.yaml
evidence/NEXT_STAGE_HANDOFF.yaml
```

完成 Stage19 后 STOP。

不要进入 Stage20。

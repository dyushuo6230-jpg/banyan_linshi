# Stage 12 v1.10 — Codex 正式开始提示词（Query First / Low Token）

这是 Stage 12 正式执行，不是重跑 Stage 01～11。

当前阶段：

```text
Stage 12 — Context / Memory / Token Optimization / Freshness
```

## 1. 最小读取

先读：

```text
榕树ai改造落地相关文档/Stage_11_SQLite_Index_Trace_History_Migration/reviews/Stage_11_to_Stage_12_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_11_SQLite_Index_Trace_History_Migration/reviews/Stage_12_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_12_Context_Memory_Token_Freshness/
```

然后优先使用 Stage 11 `STAGE12_QUERY_SURFACE.yaml` 和 Shadow SQLite 查询。

## 2. Query First

禁止重新扫描仓库。

优先：

```text
query
→ structured evidence
→ targeted source read only if needed
```

## 3. CON-002

这是本阶段 Owner 项。

禁止：

```text
mtime wins
latest file wins
AI guess
```

按：

```text
Authority
Version/Status
Supersession
Approved Change Lineage
Source Role
Freshness Observation
Conflict
Human Decision
```

分析。

Evidence 足够才 RESOLVED，否则 TYPED_BLOCKED。

## 4. Context / Memory

Memory / Summary 不是 Canonical Truth。

必须带：

```text
source_refs
as_of
freshness
coverage
confidence
```

## 5. Token Budget

必须保护 Mandatory Context。

不得为了省 Token 丢：

```text
authority
freshness
blockers
decision state
unknowns
```

## 6. 4 Historical References

仅 exact-locator / exact-history 定点验证。

允许保持：

```text
KEEP_UNRESOLVED_HISTORICAL
```

禁止猜目标或改历史文档。

REF-107 / REF-108 保持 NOT_A_REFERENCE。

## 7. Secret

13 个 Secret 继续 metadata-only。

禁止正文进入 Context / Summary / Memory。

## 8. Runtime Cost

只冻结抽象 policy，不写厂商/模型名/价格/固定百分比。

## 9. Validation

执行 V12-01～V12-24，9 项 Hard Metrics 必须为 0。

## 10. 写入

仅：

```text
.banyan-refactor/stages/12/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

不得修改 Stage11 DB 作为 Canonical Truth。

## 11. 完成

生成：

```text
ACCEPTANCE_REPORT.md
evidence/NEXT_STAGE_HANDOFF.yaml
CON002_RESOLUTION_RECORD.yaml
HISTORICAL_REFERENCE_DISPOSITION.yaml
STAGE13_QUERY_HANDOFF.yaml
```

更新 Bootstrap。

Stage 12 完成后停止，不进入 Stage 13。

# Stage 03 — PRECHECK AND SCOPE

## 必须确认

```text
Stage 02 Run = stage02-20260920T131746Z
Acceptance = PASS_CANDIDATE_DESIGN
Entry Gate = PASS_FOR_CONTRACT_DESIGN
```

## 默认输入

先读 Gate Review 与低 Token 索引。

然后只读 Stage 02 必需契约输入。

## Freshness

只检查：

```text
HEAD
tracked changes
Stage 02 sealed artifacts
Bootstrap Register/Trace
13 Secret path metadata
```

不重新扫描全仓。

## Drift 分类

```text
NO_DRIFT
SAFE_CONTRACT_INPUT_DRIFT
CONTRACT_INVALIDATING_DRIFT
PROTECTED_SCOPE_DRIFT
```

后两者 BLOCK。

## 写入

仅：

```text
.banyan-refactor/stages/03/${RUN_ID}/**
两份 Bootstrap
```

## Secret

继续只允许元数据。

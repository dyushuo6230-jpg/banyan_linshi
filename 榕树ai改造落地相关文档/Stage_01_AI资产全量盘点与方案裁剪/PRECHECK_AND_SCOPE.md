# Stage 01 — PRECHECK AND SCOPE

## 1. 先确认 Stage 00 Handoff

必须找到真实 Accepted Run，而不是猜路径。

确认：

```text
Stage 00 = COMPLETED
Stage 01 Entry Gate = PASS
Recovery = PARTIAL_APPROVED
R00-SECRET-001 = USER_ACCEPTED
```

## 2. Freshness Check

比较当前：

```text
HEAD
git status
protected roots
13 secret path metadata
```

与 Stage 00。

分类：

```text
NO_DRIFT
SAFE_DISCOVERY_DRIFT
PROTECTED_SCOPE_DRIFT
BASELINE_INVALIDATING_DRIFT
```

后两类视风险 BLOCK。

## 3. Stage 01 Scope

### 可读正文

仅在 Stage 00 Discovery/Protected policy 允许时：

- tracked governance；
- AI rules/prompts/skills；
- docs；
- tools/scripts；
- editor roots；
- generated/operational assets；
- Git metadata/history。

### metadata-only

13 个 Secret 以及其它 Stage 00 Secret candidates。

### 不作为 Legacy

```text
.banyan-refactor/**
榕树ai改造落地相关文档/**
```

## 4. 写入范围

仅：

```text
REFRACTOR_CONTROL_ROOT/stages/01/${RUN_ID}/**
Bootstrap Register
Bootstrap Trace
```

## 5. Existing Layout

Stage 01 不：

```text
move
rename
merge directories
create project-sources/
create banyan-framework/
create .banyan/
```

## 6. Precheck PASS

只有：

```text
upstream handoff trustworthy
secret policy intact
protected scope trustworthy
control root writable
repository root known
```

才开始 Full Discovery。

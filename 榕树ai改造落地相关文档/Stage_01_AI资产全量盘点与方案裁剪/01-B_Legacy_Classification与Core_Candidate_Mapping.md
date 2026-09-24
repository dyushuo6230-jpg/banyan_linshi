# 01-B：Legacy Classification 与 Core Candidate Mapping

## 1. 目标

把发现到的 Legacy 资产/能力从“文件堆”转换成可供 Stage 02 使用的候选架构输入。

## 2. Legacy 处置标签

资产级：

```text
KEEP
MERGE
SPLIT
REWRITE
REFERENCE
LEGACY
IGNORE
```

能力级候选动作：

```text
KEEP
MAP
GENERALIZE
PROJECT_ONLY
REPLACE_EQUIVALENT
COMPATIBILITY_READ
ARCHIVE
DEPRECATE
DROP_WITH_APPROVAL
```

Artifact 级候选动作：

```text
KEEP
MAP
TRANSFORM
REGENERATE
INDEX_ONLY
COMPATIBILITY_READ
ARCHIVE
SUPERSEDE
DEPRECATE
DROP_WITH_APPROVAL
```

这些全是候选，不执行。

## 3. Core Candidate 五分法

```text
GENERIC_CORE_CANDIDATE
PROJECT_ONLY_CANDIDATE
PROVIDER_CANDIDATE
COMPATIBILITY_CANDIDATE
RETIREMENT_CANDIDATE
```

## 4. Core Candidate 判定证据

至少检查：

- 是否含项目名；
- 是否含业务模块；
- 是否硬编码目录；
- 是否硬编码端口/URL/ID/状态；
- 是否依赖特定编辑器；
- 是否能抽象为通用语义；
- 是否有跨项目证据；
- 是否已有更通用等价能力。

Stage 01 不能因为“看起来通用”就直接进入 Core。

## 5. Existing Project Layout

任何 Candidate 不得以“统一目录”为通用性证明。

例如：

```text
docs/project/**
tools/**
.cursor/**
```

只能作为当前 Reference Project Mapping 候选，不得升格为 Core 固定路径。

## 6. 输出

`LEGACY_CLASSIFICATION_REPORT.yaml` 与 `CORE_CANDIDATE_REPORT.yaml`。

每个候选都需要：

```text
evidence
confidence
open_question
candidate_owner_stage
```

Stage 02 才完成 Architecture Coverage。

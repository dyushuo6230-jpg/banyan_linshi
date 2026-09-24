# 01-E：AI Generated Artifact Inventory

## 1. 为什么单独盘点

迁移不能只搬 Prompt/Rule，也必须解释 AI 已经生成过的结果。

必须区分：

```text
AI Generated Canonical Artifact
AI Generated Derived Artifact
Operational Artifact
```

Operational Artifact 另在专门 Inventory 中登记。

## 2. Canonical Artifact

如果某 AI 生成文件已经被正式治理接受：

```text
不能因为“AI 生成”就当临时文件
```

默认候选：

```text
KEEP_IN_PLACE + MAP + INDEX
```

Stage 01 至少记录：

```text
candidate_source_role
keep_or_migrate
integrity_risk
```

## 3. Derived Artifact

例如：

- generated summary；
- implementation pack；
- design pack；
- adapter output；
- report；
- buildable projection。

需要记录：

```text
source
rebuildability
freshness
consumer
migration candidate action
```

## 4. Artifact Actions

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

`DROP_WITH_APPROVAL` 仅候选。

## 5. Reference Integrity

仍被引用的正式 Artifact：

```text
不能删正文
不能清空
不能整篇换题
不能把旧 ID 挂给新主题
```

Stage 01 只发现引用关系，最终 Reference Integrity Contract 属于 Stage 03。

## 6. 输出

`AI_GENERATED_ARTIFACT_INVENTORY.jsonl`
与 Preliminary Artifact Migration Matrix。

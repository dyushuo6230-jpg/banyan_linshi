# 10-L Stage 11 Index Requirements

Stage 11 需要索引的最低实体：

```text
Artifact
Source Role
Projection
Guide
Reference
Version
Status
Freshness
Provenance
Change
Decision
Handover
Progress
Provider Binding
```

最低查询关系：

```text
projection -> source
source -> projections
artifact -> references
change -> affected artifacts
handover -> canonical refs
guide item -> canonical source
stale projection -> upstream changes
```

Index 是可重建层，不是真源。

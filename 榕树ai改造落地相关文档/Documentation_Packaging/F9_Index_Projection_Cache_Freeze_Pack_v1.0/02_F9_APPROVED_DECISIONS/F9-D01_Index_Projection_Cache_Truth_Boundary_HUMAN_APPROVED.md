# F9-D01 — Index / Projection / Cache Truth Boundary

Status: `HUMAN_APPROVED`

Approval statement:

`F9-D01 HUMAN_APPROVED`

## Frozen purpose

F9 为速度需要 Index（索引）、Projection（派生投影）、Cache（缓存），但这些能力必须始终属于派生层，不能演变为第二套 Canonical Truth（正式权威事实）。

## Derived layer

```text
Index
Projection
Cache

∈ Derived / Rebuildable Layer
```

冻结：

```text
Index != Canonical Truth
Projection != Canonical Truth
Cache != Canonical Truth
```

## Rebuild basis

派生层只能从：

```text
Authoritative Source
或
Applicable Governed Effective Result
```

重建。

冻结：

```text
Rebuild != Re-resolution
```

## Navigation vs governance

可靠 Index 可以直接支持 Navigation Claim（导航结论）。

Governance Claim（治理结论）不能仅靠 Index 独立产生。

## Content copies in Index

Index 可以保存：

```text
标题
摘要
关键词
规范化搜索文本
局部正文
Embedding
```

用于检索。

但：

```text
Copied Content in Index
!= New Authority
```

## Lineage / Provenance

重要派生结果必须能够追溯：

```text
Source / Basis
Scope
Revision / Version
Applicable Effective Result
Projection Chain
Freshness
Provenance
```

## Write-back boundary

```text
Derived Result
!= Canonical Write Instruction

Derived Mismatch
!= Canonical Error
```

派生层不一致时，默认修复派生层，不反写正式源。

## F9-owned freshness / invalidation / rebuild

F9 可以对自己拥有的：

```text
Index Entry
Cache
Context Snapshot
Dependency Projection
Search Projection
Impact Projection
```

自动：

```text
Freshness Evaluation
→ Invalidate
→ Rebuild
```

但是：

```text
Invalidate F9-owned Derived Data
!= Invalidate Domain Semantic Object
```

## Controlled fallback

正式 Source 暂不可达时，允许受控使用：

```text
Cache
Projection
Previous Validated Snapshot
```

作为 Fallback Evidence。

但：

```text
Source Unavailable
!= Cache Becomes Canonical

Last Known Projection
!= Current Authoritative Truth
```

是否可继续取决于：

```text
Task Purpose
Required Authority
Freshness Requirement
Risk / Governance Consequence
```

## Scoped invalidation

默认采用 Scoped Invalidation（局部失效）。

同时：

```text
Incomplete Dependency Coverage
!= No Other Dependency

Index Miss
!= No Dependency
```

## Backend / Provider independence

未来可以使用：

```text
Memory
File
SQLite
Redis
Graph Store
Vector Store
Search Engine
```

但：

```text
Provider Change
!= Semantic Change

Logical Index Contract
!= Physical Storage Schema
```

当前继续：

```text
SQLite Physical Schema = NOT_FROZEN
```

## Search / similarity boundary

```text
Search Similarity != Semantic Equivalence
Search Rank != Governance Priority
Index Order != Winner
Latest != Winner
File Order != Winner
```

## Fingerprint boundary

```text
Fingerprint Changed
!= Semantic Meaning Changed
```

Fingerprint 只是 Change Detection Evidence（变化检测证据）。

## Retry boundary

```text
Auto Rebuild
!= Unbounded Retry
```

## Authorization remains unchanged

```text
F9 Implementation = NOT_AUTHORIZED
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

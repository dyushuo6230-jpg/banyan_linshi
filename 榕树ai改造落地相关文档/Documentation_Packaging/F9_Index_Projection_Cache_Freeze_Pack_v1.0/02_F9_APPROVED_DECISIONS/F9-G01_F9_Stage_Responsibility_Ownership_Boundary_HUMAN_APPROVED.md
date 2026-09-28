# F9-G01 — F9 Stage Responsibility / Ownership / Boundary

Status: `HUMAN_APPROVED`

Approval statement:

`F9-G01 HUMAN_APPROVED`

## Frozen purpose

F9 是 Banyan 的：

**上下文解析、信息导航、索引检索、新鲜度证据与影响发现阶段。**

它负责快速发现、定向检索、任务上下文组装、新鲜度证据、影响发现，以及 F9 自己派生层的缓存和重建。

它不成为第二套 Canonical Truth（正式权威事实），也不获得 F5 / F6 / F7 / F8 / F10 的领域 Authority。

## Owned responsibility

```text
Index
Retrieval / Search
Context Selection & Assembly
Context Recovery
Freshness Evidence
Impact Discovery
Cache / Derived Projection / Rebuild
```

## Context boundary

```text
F1
= Context Semantic Boundary

F8
= Project-effective Context Facts

F9
= Task-scoped Context Resolution & Assembly
```

## Freshness boundary

```text
Freshness Evidence
!= Domain Semantic Validity
```

F9 可以判断和重建自己拥有的派生层。

F9 不能把“Source 变化”直接等同于“其他领域对象正式失效”。

## Impact boundary

```text
Change
↓
Dependency / Reference Discovery
↓
Potential Impact Set
↓
Impact Evidence
↓
Domain Owner Re-resolution
```

冻结：

```text
Potential Impact
!= Effective Invalidity
```

## Automatic routing

确定性问题优先自动处理：

```text
Index Miss
→ 回源 / 扩 Scope / 局部重建

Cache Stale
→ 自动失效 / 重建

Context Snapshot 过期
→ 局部刷新
```

真正无法由现有规则和 Domain Owner 唯一解析的治理问题，才进入 Human Decision。

F9 不是 Human Decision Center。

## Core inequalities

```text
Index != Canonical Truth
Index Match != Effective Binding
Index Miss != Semantic Absence
Cache != Canonical Truth
Context Snapshot != Current Eternal Truth
AI Summary != Canonical Truth
Freshness Evidence != Domain Semantic Validity
Potential Impact != Effective Invalidity
Index Edge != Canonical Dependency
Search Match != Governed Relation
Derived Mismatch != Canonical Mutation Authorization
Context Ready != Runtime Authorized
F9 Evidence != Runtime Permission
Freshness Capability Owner != Global Semantic Validity Authority
Detection Direction != Authority Direction
Later Stage != Higher Authority
```

## AI learning boundary

```text
AI Autonomous Learning = NOT_CURRENT_CAPABILITY
AI Autonomous Optimization = NOT_CURRENT_CAPABILITY
AI Autonomous Canonical Promotion = FORBIDDEN
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

# AUDIT-PATCH-011 — Product / Design Typed Semantic Linkage × Impact Applicability

> Formal Audit Patch ID: `AUDIT-PATCH-011`  
> Source Finding: `B3-CHAIN-01`  
> Source Approval ID: `B3-PATCH-01`  
> Status: `HUMAN_APPROVED`  
> Audit Batch: `Audit Batch 3 — Product / Design / Change Chain`  
> Classification: `GAP`  
> Severity: `P1`  
> Primary Affected Stages: `F5 / F6 / F7 / F9`  
> Implementation Authorization: `NO`

---

## 1. Problem（问题）

F5 已经明确：

- Requirement 是稳定、可寻址的 Product Semantic Anchor（产品语义锚点）；
- Requirement 变化需要进行下游影响判断；
- F5 拥有 Product Meaning（产品含义）；
- UI_SPEC 不是 Product Truth（产品真相）。

F6 已经明确：

- `PRD != UI_SPEC`；
- `Design Package != UI_SPEC`；
- Design Package 经 UI Governance（界面治理）形成 UI_SPEC；
- UI_SPEC 存在 Current Effective（当前有效）解析；
- F6 拥有 UI / Design Truth（界面与设计真相）。

AUDIT-PATCH-008 已经明确：

```text
Authoritative Upstream Change
→ Impact / Freshness / Applicability
→ Downstream Domain-owner Re-resolution
```

但原有跨阶段合同没有完整定义：

1. Requirement / Product Semantic 与 Design Package / UI_SPEC 之间以什么语义关系连接；
2. 哪些关系必须记录；
3. 哪些纯视觉细节不需要建立 Product Trace；
4. Product Change 如何判断是否真正影响 UI；
5. UI Change 如何判断是否已经跨越 Product Semantic Boundary；
6. Requirement / UI Contract 拆分、合并、替代后的关系如何保持历史可追踪；
7. F5 / F6 / F7 / F9 在该链中的责任边界。

因此存在跨阶段语义连接缺口。

---

## 2. Existing Contract（已有合同）

继续保留：

```text
Product Truth
!= UI Truth
!= Implementation Reality

PRD != UI_SPEC
Design Package != UI_SPEC
UI_SPEC != Implementation Pack
Current Code != Product / Design Truth
```

F7 继续拥有：

- Governed Change（受治理变更）；
- Canonical Apply（正式规范应用）；
- Revision（修订）；
- Supersession（替代）；
- Reference-safe Mutation（引用安全修改）；
- Rollback Governance（回滚治理）。

F9 未来继续拥有：

- Index（索引）；
- Search（搜索）；
- Reverse Reference（反向引用）；
- Freshness（新鲜度）；
- Impact Query（影响查询）；
- Provenance Retrieval（来源检索）。

但：

```text
F9 != Product / Design Semantic Authority
```

---

## 3. Target Contract（目标合同）

正式引入逻辑上的：

```text
ProductDesignSemanticLink
```

用于表达：

> 一个稳定的 Product Semantic Subject（产品语义对象）与一个稳定的 Design / UI Semantic Anchor（设计 / UI 语义锚点）之间，存在什么类型、什么范围、基于什么依据的语义关系。

它是逻辑架构概念。

本 Patch 不要求：

- 新增 F1 顶级对象；
- 一条关系一个文件；
- 当前阶段冻结数据库表；
- 当前阶段冻结 JSON / YAML Schema；
- 当前阶段冻结 SQLite DDL。

---

## 4. Minimum Sufficient Semantic Linkage（最小充分语义关联）

正式冻结：

```text
UI Element
!= Must Have Requirement Link
```

禁止把所有 `button / div / spacing / color / radius / token / ordinary layout node`
都强制挂 Requirement ID。

只有真正携带 Product Meaning（产品含义）、Product Constraint（产品约束）、Product Action（产品动作）、Product State（产品状态）或 Acceptance Intent（验收意图）的设计语义边界，才需要建立 Product ↔ Design/UI 关联。

目标：

```text
Minimum Sufficient Semantic Linkage
```

即：关联足够支持追踪、影响判断和重新解析，但不能把 UI 每个细节都变成产品治理对象。

---

## 5. UI Semantic Anchor（UI 语义锚点）

Product Link 默认不直接指向任意 DOM / CSS / 像素。

F6 应提供最小一致的 UI Semantic Anchor，例如：

```text
MaterialUploadFlow
UploadProgressState
MoveMaterialDialog
DeleteMaterialAction
RefundAction
OrderCancellationState
PermissionControlledAction
```

UI Semantic Anchor 表达一个稳定、有业务或交互意义的 UI 范围。

它不等于：

```text
DOM ID
CSS selector
absolute x/y coordinate
framework component instance
```

---

## 6. Core Typed Relations（核心类型化关系）

第一版冻结五种核心语义关系。

### 6.1 REALIZES（承载 / 实现）
某个 UI Flow / UI Capability 承载一个已经存在的产品能力。

### 6.2 REPRESENTS（呈现 / 表达）
UI 状态、区域或信息用于表现某个产品状态或产品语义。

### 6.3 INVOKES（触发）
某个 UI 交互触发一个已经存在的产品动作。UI 交互不能因为存在而反向创造 Product Capability。

### 6.4 CONSTRAINED_BY（受约束）
UI 行为、可见性、可用性或交互受到某个产品规则、权限或状态约束。

### 6.5 ACCEPTANCE_COVERS（覆盖验收意图）
一个 UI Semantic Scope（界面语义范围）负责覆盖某个产品 Acceptance Intent（验收意图）。

---

## 7. Relation Set Extensibility（关系类型可扩展）

上述五类为第一版 Core Relation Set（核心关系集合）。

```text
Core Relation Set
is extensible
```

不得解释为 Banyan 未来永远只能存在这五种关系。

新增关系类型必须：

- 语义清晰；
- 不与现有关系重复；
- 有稳定适用场景；
- 有明确 Owner；
- 不创造新的 Authority；
- 不破坏历史 Trace。

---

## 8. Mandatory Link Boundary（必须建立关联的边界）

原则上应建立 Product ↔ Design/UI Semantic Link 的场景：

1. Product Capability → UI Flow；
2. Product Action → UI Interaction；
3. Permission / Business Rule → UI Visibility / Availability；
4. Business State → UI State；
5. Product Data Semantic → UI Data Semantic；
6. Material Acceptance Intent → UI Semantic Scope。

---

## 9. Non-required Link Boundary（不强制关联的边界）

普通圆角、阴影、常规间距、纯装饰图形、普通 token、无产品语义的布局节点、框架组件选择、CSS/Grid/Flex 实现方式默认不要求 Product Link，除非它们在具体 Scope 下实际承载 Product Meaning。

---

## 10. Logical Link Contract（逻辑关联合同）

一条具有治理意义的 Link 至少应能表达：

```text
Source
Target
Relation Type
Scope
Applicability
Revision Basis
Provenance
```

- Source：产品侧稳定语义对象；
- Target：F6 的稳定 UI Semantic Anchor；
- Relation Type：关系含义；
- Scope：关系在哪个范围成立；
- Applicability：当前条件下是否适用；
- Revision Basis：当前判断基于哪些有效修订；
- Provenance：为什么认为这条关系成立，以及其证据来源。

未来可以增加 Dependency Semantic Domain、Current Effective Provenance、Supersession State、Resolution Evidence、Confidence，但本 Patch 不冻结物理字段。

---

## 11. Scope != Applicability

```text
Scope != Applicability
```

Scope 回答“这条关系理论上属于哪里”；Applicability 回答“在当前 Project / Context / State / Version 下，这条关系现在是否真正适用”。

关系存在，不等于当前一定生效。

---

## 12. Revision / Freshness（修订与新鲜度）

Link 应绑定稳定 Semantic Subject，并保留形成当前关系判断时的 Revision Basis。

```text
Stable ID != Revision
Revision Changed != Link Automatically Deleted
```

Revision 更新后，应重新判断 relation 是否仍有效、是否 stale、是否需要 re-resolution、是否 superseded，而不是简单删除后重建全部关系。

逻辑状态可表达 CURRENT / STALE / REVIEW_REQUIRED / SUPERSEDED / UNKNOWN 等，但 exact runtime enum 延期。

```text
STALE != INVALID
STALE != DELETED
```

---

## 13. Provenance（来源依据）

Link 不能只记录 `A → B`，还必须保留足以解释“为什么系统认为 A 与 B 有这种关系”的依据。

但：

```text
Provenance != Authority
Provenance != Duplicate Product Truth
```

---

## 14. Requirement Change != Automatic UI Change

```text
Requirement Change != Automatic UI Change
```

Product Revision 变化后必须先判断：

```text
Semantic Delta
→ Dependency
→ Scope
→ Applicability
→ Material Impact
```

只有真正受到影响的 UI Semantic Scope 才进入 F6 Re-resolution（F6 重新解析）。

---

## 15. Product Change Affecting UI → F6 Re-resolution

```text
Product Change Affecting UI
→ F6 UI / Design Re-resolution
```

但：

```text
F5 != Direct UI_SPEC Mutation Authority
```

F5 不能因为 Product Truth 改变，直接重写 UI_SPEC。

---

## 16. UI Change != Automatic Product Change

```text
UI Change != Automatic Product Change
```

至少区分：

- Design-only Change（纯设计变化）：留在 F6；
- Product-reflecting Change（产品反映修正）：原则上仍留在 F6；
- Product-boundary-crossing Change（跨产品边界变化）：路由回 F5。

如果 UI Proposal 创造新能力、新权限、改变权利义务、资金规则、业务状态意义、用户可执行行为或既有 Product Acceptance Intent：

```text
Design Proposal
crosses Product Semantic Boundary
→ F5 Product Governance
```

---

## 17. Design Approval != Product Approval

```text
Design Approval != Product Semantic Approval
Product Approval != UI_SPEC Mutation
```

F6 的 UI Approval 不能合法化未经 F5 决定的新产品能力；Product Decision 也不能越过 F6 直接修改 UI Truth。

---

## 18. Link != Authority / Trace Link != Duplicate Truth

```text
Semantic Link != Authority
Trace Link != Duplicate Semantic Truth
```

Link 表达关系，不自动授予 Product Decision Authority、UI Design Authority、Canonical Apply Authorization 或 Runtime Permission。

Link 应引用稳定 Semantic Subject，而不是复制 PRD / UI_SPEC 正文。

---

## 19. Split / Merge / Supersession / Retire

Requirement 或 UI Semantic Anchor 拆分后，不允许把旧关系无脑复制到所有新对象。

```text
Old Subject
↓
Semantic Partition
↓
New Subject A / B / C
↓
Relation Re-resolution
```

能够唯一确定的关系自动迁移；存在实质语义歧义时进入 Human Governance。

Merge（合并）不等于简单拼接全部 Link，必须去重、判断 Scope、关系含义、历史来源与 Applicability。

```text
Superseded != Deleted
Retired != Historical Erasure
```

历史关系必须继续能够解释某一历史 UI_SPEC 当时依据什么 Product Revision，不得把所有历史引用静默重定向到最新对象。

---

## 20. Durable Relation Identity（持久关系身份）

长期存在、可引用、可修订、可追踪的 Relation 可以拥有稳定关系身份。

```text
Temporary Candidate Relation
!= Must Have Durable Stable ID
```

只有需要长期治理生命周期的 Relation 才需要正式稳定身份。

---

## 21. Link Coverage（关系覆盖状态）

Legacy / Historical Material（旧资料 / 历史资料）不得因为没有现成 Relation 就被判定为“确定没有关系”。

至少必须区分：

```text
KNOWN_NO_RELATION
INCOMPLETE_LINK_COVERAGE
INSUFFICIENT_EVIDENCE
```

```text
Index Miss
!= No Impact
when Link Coverage is incomplete
```

---

## 22. Owner Boundary（责任边界）

### F5
负责 Requirement Stable Semantic Anchor、Product Meaning、Product Semantic Delta、Requirement-side Impact Obligation、Product Semantic Boundary Judgment。

### F6
负责 detailed Product ↔ Design/UI typed linkage、UI Semantic Anchor、UI Applicability、Design Impact Classification、Design Package / UI_SPEC Re-resolution，以及跨 Product Boundary 的检测与路由。

### F7
负责 Governed Change、Canonical Apply、Durable Relation Mutation、Reference-safe Mutation、Revision、History、Supersession、Rollback Governance。

### F9
未来负责 Relation Index、Reverse Reference、Candidate Impact Query、Freshness Evidence、Provenance Retrieval、Search / Retrieval、Index Rebuild。

但：

```text
F9 != Semantic Owner
F9 != Product Authority
F9 != UI Authority
F9 != Mutation Authority
```

---

## 23. SQLite / Relation Index Boundary

未来性能路径允许：

```text
Requirement Stable ID
↓
SQLite / Relation Index
↓
Candidate Design / UI Impact Set
↓
Targeted Canonical Read
↓
Semantic Resolver
```

但：

```text
SQLite != Canonical Truth
SQLite != Authority
Indexed Relation != Confirmed Material Impact
Impact Query != Mutation Authorization
```

Index 必须保持：

```text
NON_CANONICAL
REBUILDABLE
```

Exact SQLite DDL 留给 F9 / Storage Owner Stage。

---

## 24. Automatic Resolution / Human Governance

默认允许自动完成：

- relation candidate discovery；
- deterministic relation refresh；
- deterministic split / merge mapping；
- freshness calculation；
- impact candidate narrowing；
- provenance assembly；
- relation index rebuild；
- uniquely resolvable re-resolution。

```text
AUTOMATIC != UNGOVERNED
```

只有真正存在 unresolved material semantic choice、Product Semantic Boundary 不明确、Authority conflict、Scope expansion、unresolved semantic split/merge、high-risk/hard governance gate、multiple incompatible valid interpretations 时才占用人工。

```text
GOVERNED != MANUAL_EVERY_TIME
```

---

## 25. Banyan-wide Invariants（全局不变量）

```text
Requirement Change != Automatic UI Change
UI Change != Automatic Product Change

Semantic Link != Authority
Semantic Link != Canonical Truth
Semantic Link != Confirmed Material Impact
Semantic Link != Mutation Authorization

Trace Link != Duplicate Product Truth

Design Approval != Product Semantic Approval
Product Approval != UI_SPEC Mutation

Product Change Affecting UI → F6 Re-resolution
Design Change Crossing Product Boundary → F5 Resolution

Detection Direction != Authority Direction

Indexed Relation != Canonical Relation
Indexed Relation != Confirmed Semantic Impact
Index Miss != No Impact when Link Coverage is incomplete

Freshness != Authority
Stale != Invalid != Deleted

Supersession != Universal Retarget
Superseded != Deleted
Retired != Historical Erasure
Revision Lineage != Supersession
Stable ID != Revision

Historical Trace must remain reproducible
Current Code != Product / Design Truth

Automatic != Ungoverned
Governed != Manual Every Time
```

---

## 26. No-Loss / Compatibility

本 Patch 保留并扩展：

- F5 Requirement Stable Anchor、Product Truth、Requirement Impact Obligation；
- F6 PRD != UI_SPEC、Design Package != UI_SPEC、Effective UI Contract、Design Truth Ownership；
- F7 Stable ID / Revision / Reference / Supersession / Canonical Apply / History；
- AUDIT-PATCH-008 Upstream Change → scoped downstream impact / freshness / re-resolution。

本 Patch 只补齐 Product Semantic 与 Design/UI Semantic 之间缺失的最小充分类型化语义连接。

兼容策略：

- 不要求重编号既有 Requirement Stable ID；
- 不要求重建现有 UI_SPEC Stable Identity；
- 不要求一次性补齐所有历史 Relation；
- 不把所有 UI Element 变成 Requirement Child；
- 不复制 Product Truth 到 UI Relation；
- 不把 Design Truth 复制回 PRD；
- 允许 Scope-based progressive coverage、Change-triggered coverage、Active-surface coverage。

---

## 27. Forbidden Interpretations（禁止解释）

禁止：

1. 每个 DOM / Button 都必须挂 Requirement ID；
2. Product Requirement 一改就自动修改 UI；
3. UI 一改就自动修改 PRD；
4. UI Approval 可以创造 Product Capability；
5. Product Approval 可以直接改 UI_SPEC；
6. Semantic Link 等于 Authority；
7. Link Body 复制整份 Product Rule；
8. Indexed Relation 等于 Canonical Relation；
9. SQLite 成为 Product / UI Truth；
10. Index Miss 自动解释为 No Impact；
11. Revision Change 自动删除全部 Link；
12. Requirement Split 后把旧 Link 无脑复制给所有新 Requirement；
13. Supersession 自动重定向所有历史引用；
14. Historical Trace 因 Current Effective 变化被重写；
15. AI 根据 Model Confidence 自创 Relation Authority；
16. 本 Patch 授权真实 Implementation。

---

## 28. Downstream Impact / Deferred

未来整合主要影响：

- F5 Product Trace / Requirement Impact obligations；
- F6 Product ↔ Design linkage / UI applicability；
- F7 relation-safe mutation / revision / history；
- F9 relation index / reverse query / freshness / impact query。

F10 可消费 re-resolved Current Effective Context，但不拥有关系语义。

以下延期：

- exact physical file format；
- exact JSON / YAML schema；
- exact SQLite DDL；
- relation physical table；
- graph physical schema；
- Stable ID physical syntax；
- exact revision numbering；
- runtime enum；
- storage location；
- API / CLI / WebUI；
- migration tooling；
- autonomous AI learning。

---

## 29. Patch Result

本 Patch 正式补齐：

```text
Product Semantic Anchor
↔
Design / UI Semantic Anchor
```

之间的 Typed Semantic Linkage（类型化语义关联）、Impact Applicability（影响适用性）、Boundary Routing（边界路由）、Revision / Freshness、Split / Merge / Supersession、Owner Responsibility、Index / Authority Boundary、Automatic / Human Governance Boundary。

```text
B3-CHAIN-01
= ARCHITECTURALLY_RESOLVED
```

---

## 30. Human Decision

用户已明确：

```text
B3-PATCH-01 HUMAN_APPROVED
```

因此：

```text
AUDIT-PATCH-011
= HUMAN_APPROVED
```

---

## 31. Current Authorization Boundary（当前授权边界）

即使本 Patch 已 HUMAN_APPROVED：

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

F1～F8 v1.0 继续作为 Original Frozen Baseline（原始冻结基线），不得因为本 Patch 被直接覆盖。

只有整个 Pre-F9 Audit 完成后：

```text
All HUMAN_APPROVED Audit Patches
↓
F1～F8 v1.1 Candidate
↓
No-Loss Reconciliation
↓
Final Audit
↓
Explicit Human Approval
```

才允许形成新的 Consolidated Freeze Baseline（整合冻结基线）。

# AUDIT-PATCH-006 — Engineering Standard Canonical Truth × Project Current Effective Resolution Boundary

> Patch ID: `AUDIT-PATCH-006`  
> Source Candidate: `B2-PATCH-01`  
> Status: `HUMAN_APPROVED`  
> Classification: `DEFECT / P1`  
> Scope: Pre-F9 F1～F8 Architecture Integrity & Optimization Review — Audit Batch 2  
> Primary Affected Stages: `F2 / F4 / F6 / F8`  
> Implementation Authorization: `NO`

---

## 1. Problem（问题）

Batch 1 的 `AUDIT-PATCH-004` 曾保留一条表述：

```text
Current Project Effective Engineering Standards
= ProjectArtifact Canonical Semantic Truth
```

该表述会让同一工程规范语义同时出现：

```text
Canonical Engineering Standard Body
+
Project Current Effective Engineering Standards
```

两个可被理解为 Canonical Truth（规范真相）的写入目标，违反 F2：

```text
One Semantic Fact → One Canonical Write Target
```

因此需要修正 Canonical Standard Semantics（规范正文）与 Project Current Effective Result（项目当前有效结果）的边界。

---

## 2. Target Contract（目标合同）

正式冻结：

```text
Canonical Engineering Standard Semantics
= Canonical Semantic Truth

Project Adoption / Binding / Version Pin / Approved Local Facts
= Governed Inputs

Project Current Effective Engineering Standards Set
= Derived Resolution Result
```

也即：

```text
Current Effective != Second Canonical Truth
Resolution != Authority Creation
Persisted / Cached Effective Result != Canonical Truth
```

Project Current Effective Result 可以为了审计、恢复、查询、性能被持久化、缓存或快照化，但其语义仍然是 Derived / Rebuildable（派生 / 可重建），不能因此升级为第二规范真相。

---

## 3. Resolution Inputs（解析输入）

项目当前有效工程规范可以由以下受治理输入共同解析：

- Canonical Engineering Standard body / revision；
- Project adoption / standard adoption binding；
- Configuration Profile / Project Profile Instance；
- Version Pin / Constraint；
- Scope / Applicability；
- Approved project-local override / exception；
- Authority / Policy；
- Freshness / compatibility evidence。

这些输入拥有各自 Owner，不因参与解析就被复制进一个新的“项目规范真相”。

---

## 4. Shared Standard Boundary（共享规范边界）

正式保持：

```text
Shared Engineering Standard
!= Global Mandatory Standard
!= Project Current Effective Standard
!= Forced Latest
```

项目是否采用共享规范，必须通过适用的 Profile / Binding / Version Pin / Policy / Authority 解析。

允许受治理的 project-local override / exception，但其存在：

```text
!= Rewrite Shared Canonical Standard Body
```

---

## 5. Owner Boundary（Owner 边界）

- Canonical Engineering Standard Semantics：由其正式 Engineering Standard Owner 管理；
- Project adoption / binding / pin / project facts：由 F8 及对应 Domain Owner 管理；
- Durable protected mutation / Canonical Apply：进入 F7；
- Index / freshness / impact / retrieval：F9；
- Runtime consumption / execution：F10。

F9 / SQLite 可以索引当前有效结果及其 provenance，但：

```text
Index != Canonical Truth
```

---

## 6. No-Loss / Supersession（无损 / 替代）

`AUDIT-PATCH-004` 除“Project Current Effective Engineering Standards 属于 ProjectArtifact Canonical Semantic Truth”这一点外，其余 Rule / Policy / Module / Engineering Standard 语义继续保留。

被替代的旧解释：

```text
Project Current Effective Engineering Standards
= Canonical Semantic Truth
```

正式替换为：

```text
Project Current Effective Engineering Standards
= Derived Resolution Result
```

历史 v1.0 / Batch 1 文件保持原文，不直接覆写；本 Patch 在 Audit Patch Layer 中拥有后续解释权。

---

## 7. Compatibility（兼容性）

本 Patch 与以下已冻结原则一致：

- F2 — one semantic fact one canonical write target；
- F6 — Current Effective / Derived / Canonical separation；
- AUDIT-PATCH-003 — Latest != Current Effective；
- AUDIT-PATCH-004 — Engineering Standard != Policy；
- F8 — Binding != Effective Binding；State Derivation != Authority Creation。

---

## 8. Forbidden Interpretations（禁止解释）

禁止：

1. 为项目当前有效工程规范创建第二套 Canonical Truth；
2. 将 Effective Result 的缓存 / SQLite 行解释为正式规范正文；
3. Shared Latest 自动升级所有项目；
4. Project Adoption 复制所有共享规范正文成为新正式真相；
5. Resolution Result 创造 Authority；
6. Project-local Exception 静默改写 Shared Canonical Standard；
7. 因本 Patch 进入 Storage / SQLite / Runtime Implementation。

---

## 9. Integration Target / Version Impact

未来整合目标主要为：

- F2 Storage & Truth Model v1.1 Candidate；
- F4 Orchestration Semantic v1.1 Candidate；
- F6 UI / Rule Resolution clarification；
- F8 Project Instance / Binding clarification；
- `AUDIT-PATCH-004` 对应条款的 supersession note。

本 Patch 不直接修改 F1～F8 v1.0。

---

## 10. Human Decision

`B2-PATCH-01 HUMAN_APPROVED` 已明确完成，因此本文件状态为：

```text
AUDIT-PATCH-006 = HUMAN_APPROVED
```

---

## Current Authorization Boundary（当前授权边界）

本 Patch 只属于 Audit Patch Layer（审计补丁层）。即使 `HUMAN_APPROVED`，仍然：

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
```

F1～F8 v1.0 继续保持 Original Frozen Baseline（原始冻结基线），直到整个 Pre-F9 Audit 完成、形成 F1～F8 v1.1 Candidate、完成 No-Loss Reconciliation / Final Audit 并再次获得明确批准。

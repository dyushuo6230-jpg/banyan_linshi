# Final Clarifications & Optimizations

## 1. Final Clarifications

### CLARIFICATION-21 — Lifecycle Completion Is Domain-local

```text
Completion in one lifecycle
!= completion in another lifecycle

Recovery Complete != Action Complete
Action Complete != Task Complete
Notification Delivered != Attention Complete
Attention Complete != Obligation Resolved
Obligation Resolved != Implementation Complete
Implementation Complete != Final Activation
Session Closed != Runtime Closed
Superseded != Deleted
```

### CLARIFICATION-22 — Logical Object Does Not Automatically Require F1 Promotion

```text
Stable Domain Logical Object
!= F1 Top-level Object automatically

Stable Domain Logical Object
!= DefinitionArtifact automatically

Persisted Domain Record
!= Canonical Truth automatically
```

### CLARIFICATION-23 — Every Material UX Signal Must Be Basis-traceable

所有会影响人判断或受保护动作的 Material UX Signal，必须能追溯其当前 Basis。

典型包括：

```text
Can Retry
Can Apply
Success
Failure
BLOCKED
Decision Required
Current
Approved
Authorized
Evidence Strong
Attention Required
```

### CLARIFICATION-24 — Safe Degradation Must Reduce Capability, Not Governance Fidelity

Safe Degradation 可以降低：

```text
detail
coverage
automation
available action
confidence
presentation richness
```

但不得降低：

```text
Authority requirement
Scope requirement
Freshness requirement
Gate requirement
Deferred Guard
Point-of-use validation
Material semantic qualifiers
```

## 2. Final Optimizations

以下属于未来工程/治理解释层的优化产物，不是新的 Architecture Patch：

```text
OPTIMIZATION-06
GLOBAL_OWNER_TRUTH_AUTHORITY_MATRIX

OPTIMIZATION-07
GLOBAL_HANDOFF_DEPENDENCY_REVALIDATION_MATRIX

OPTIMIZATION-08
GLOBAL_LIFECYCLE_COMPLETION_MATRIX

OPTIMIZATION-09
REVERSE_PROVENANCE_ROOT_MAP

OPTIMIZATION-10
MATERIAL_UX_SIGNAL_BASIS_MATRIX

OPTIMIZATION-11
DEGRADATION_FALLBACK_SAFETY_MATRIX
```

## 3. 使用原则

这些 Matrix / Map 用于：

- F12 工程映射；
- 实现前检查；
- Architecture Conformance Validation；
- UI / API / Runtime 边界设计；
- 新会话快速恢复上下文。

它们不改变原 Owner、Authority、Truth 或 Frozen Decision。

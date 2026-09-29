# F11 Deferred Obligation Register

## A. IMPLEMENTATION_DEFERRED — OPEN_NON_BLOCKING

包括但不限于：

```text
Exact API / DTO / Enum
Exact DB / SQLite / Redis physical model
Exact persistence / cache strategy
Exact WebSocket / SSE / Polling
Exact Session Store
Exact Notification Store
Exact Visibility Rule DSL
Exact Redaction / Abstraction implementation
Exact Sync protocol
Exact UI layout
Exact Architecture Conformance validation implementation
Exact deployment/service topology
```

这些内容在进入对应 Implementation Scope 时解析。

## B. FUTURE_EXTENSION_DEFERRED — OPEN_NON_BLOCKING

包括：

```text
Future new Surface semantics
Future new governance capabilities
AI autonomous learning / self-optimization
```

当前未授权。

## C. PACKAGING_OBLIGATION — OPEN_NON_BLOCKING

F11 Final Freeze Pack、Git-ready archive、Stage Summary、Next-window / next-stage handoff。

本次归档将其中主要交付物物化，但 Packaging Gap 仍不等于 Architecture Gap。

## Required metadata for future material Deferred

```text
What
Why Deferred
Future Trigger
Expected Owner / Phase
Frozen Semantics to preserve
```

## Invariants

```text
Deferred != Missing Architecture by default
Deferred Obligation != Implementation Backlog
Implementation Deferred != Architecture Extension Deferred
Every Deferred Obligation must remain discoverable until resolved or formally retired
Blocking Architecture Gap = 0 != Deferred Obligation = 0
```

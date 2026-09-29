# F10 Final Owner Map

```text
F4
Owner: Workflow / Orchestration Semantics
Includes: Workflow Graph, Branch/Merge, Retry/Pause/Resume/Skip/Replace, Workflow-level Join/Handoff/Escalation

F5
Owner: Product / Requirement Semantics

F6
Owner: Design Semantics

F7
Owner: Governed Change / Apply
Includes: Apply Authorization, Apply Scope, Expected Base, Apply Plan, Semantic Atomicity, F7 Apply Attempt, Canonical Acceptance, Semantic Rollback, Change Closeout

F8
Owner: Project Instance / Binding / Project Reality
Includes: Project identity/instance, Provider Binding governance, Version/Feature/Gate, Project reconciliation, task-scoped project runtime handoff

F9
Owner: Index / Retrieval / Freshness / Dependency / Context Recovery
Includes: Index/Search, Context selection/recovery, Freshness, Dependency/Impact discovery, Provenance

F10
Owner: Runtime Permission / Execution Governance
Includes: Runtime Permission, runtime provider resolution, adapter routing, execution attempt lifecycle, runtime failure/recovery coordination, runtime result/trace, cross-action scheduling

F11
Owner: Control Plane / Governance UX
Includes: observation UX, control-intent submission, human-decision presentation
```

Guards:

```text
Owner Map != Runtime Call Order
Owner Map != Authority Ranking
Later Stage != Higher Authority
Handoff Direction != Authority Direction
```

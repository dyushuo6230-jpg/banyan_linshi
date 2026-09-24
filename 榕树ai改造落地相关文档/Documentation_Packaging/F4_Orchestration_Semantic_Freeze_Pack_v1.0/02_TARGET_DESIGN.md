# 02_TARGET_DESIGN.md

Status: `HUMAN_APPROVED`  
Architecture Freeze: `PASS`

## 1. Goal-oriented orchestration

```text
Goal / Desired Outcome
→ Intent / Scope / Constraints
→ Workflow Family Selection / Composition
→ Minimum Valid Workflow Graph
→ Responsibility Resolution
→ Functional Role Resolution
→ Capability Requirements
→ Execution Path Resolution
   ├─ direct authorized capability path
   └─ Skill path (optional / pinned / required only when constrained)
→ Provider / Binding Resolution
→ Runtime Execution
→ Validation
→ Evidence / Trace
→ Reconcile / Continue / Re-route / Escalate
```

## 2. Role

RoleDefinition planes: SOURCE / FUNCTIONAL / PARTICIPATION_GOVERNANCE.

Functional Role = stable, reusable, semantically coherent task-function responsibility cluster. It may receive Handoff, own major outcome responsibility for one or more executable Workflow Nodes, use Capabilities and Skills, and operate under Policy / Standards / Permission / Decision / Validation constraints. It is not a person, job, department, Git identity, execution client, provider, framework, technology, single capability, permission or source authority.

`RoleDefinition != RoleAssignment`.

Core Functional Role baseline:
1. Requirement & Product Definition
2. Architecture & Solution Planning
3. Software Implementation
4. Verification & Validation
5. Change Reconciliation
6. Engineering Standards Steward
7. UI / Design Intelligence
8. Engineering Knowledge & Continuity

Workflow decides order, parallelism, repetition, re-entry, skipping, replacement, handoff and reconciliation. RoleDefinition does not contain a fixed capability pipeline.

## 3. Capability

Capability answers “what ability is required”; it does not answer who is responsible, which method must be used, which provider executes or who has permission.

Functional Capability Family baseline:
- Requirement & Product Definition
- Architecture, Technical Design & Solution Planning
- Software Implementation
- Verification & Validation
- Change & Reconciliation
- Engineering Standards Stewardship
- UI / Design Intelligence
- Knowledge & Engineering Continuity
- Delivery Planning & Release Readiness

Capability gaps are typed and localized. No approximate substitution or technology masquerading as Capability.

## 4. Skill

SkillDefinition = stable reusable optional execution method implementing one or more capabilities.

Skill is method-centric, reusable, validated, constrained and independently describable. It is not Capability, Role, Workflow, provider alias, project fact, Permission or Authority.

Default Skill resolution is automatic. User / Workflow / Contract may Pin, Exclude or Require. Missing Skill does not automatically block; blocking occurs only when skill-based execution is explicitly required/pinned or no other authorized, reliable, constraint-compliant, validation-capable path exists.

## 5. Workflow

WorkflowDefinition = governed Goal-oriented Workflow Graph, not a fixed Role/Capability/Skill sequence.

Logical layers:
1. Adaptive Orchestration Kernel
2. Goal-Oriented Workflow Families
3. Reusable Cross-Cutting Subworkflows

Workflow Family baseline:
- Requirement & Product Definition
- Architecture & Technical Design
- Software Implementation & Repair
- Verification & Validation
- Change & Reconciliation
- UI / Design Intelligence
- Engineering Standards Maintenance
- Knowledge & Continuity
- Delivery & Release Readiness

A Family is a semantic/use family, not a guarantee of exactly one physical workflow file or definition.

Logical node categories:
- Functional Node
- Control Node
- Decision / Governance Interrupt Node
- Validation / Reconciliation Node

Graph semantics include Branch, Merge, Pause, Resume, Loop, Retry, Skip, Replace, Invalidate, Partial Blocking, Checkpoint, Reconcile, Escalation and De-escalation.

Quality guardrails:
1. Minimum Valid Graph
2. Progressive Resolution
3. Reuse Before Recompute
4. Localized Invalidation
5. Progressive Disclosure UX
6. Reliability Floor

Normative rule: Runtime MUST prefer the smallest valid execution graph and the smallest necessary resolution scope.

## 6. Workflow Atom closure

Workflow Atom is a composition concept, not a new DefinitionArtifact. Legacy atom value routes to one of: Workflow Node semantic fragment; reusable WorkflowDefinition/Subworkflow; SkillDefinition; graph Control Semantics. No `AtomDefinition` or independent Atom taxonomy is added.

## 7. Resolution

Resolution is separate from Execution and produces an Execution Plan. Conceptual order:

```text
Goal / Context / Constraints
→ Responsibility Resolution
→ Functional Role / Assignment
→ Capability Requirements
→ Execution Path Candidates
   ├─ direct capability path
   └─ Skill path
→ Provider Candidate
→ Binding
→ Permission / Governance Check
→ Executable Plan
```

Skill remains optional. Provider cannot redefine semantic requirements. Re-resolution is localized.

## 8. Handoff

Handoff is a typed transition contract, not necessarily a dedicated node. It can carry result/output refs, canonical/context refs, evidence refs, decision state, blockers, unknowns, downstream required inputs and validation state. Complex handoff work may become a Functional Node.

## 9. Validation

Keep separate: Invocation Success / Node Success / Workflow Success / Goal Success. Skill validation does not replace Node or Goal validation.

## 10. Policy / Standard / Permission boundaries

Policy = mandatory / forbidden governance constraint semantics.

Engineering Standard is a distinct governed engineering semantic domain. Current-project Effective Engineering Standards belong to ProjectArtifact Canonical Semantic Truth. Framework / organization / external standards may be reusable sources or packs, but do not automatically become project truth. ProjectInstance / Binding stores applicability, scope, selection and references, not duplicated standard bodies. Engineering Standards Steward has no automatic Canonical Apply Authority. No `StandardDefinition` is added in F4.

Role, Skill, Provider and Workflow do not grant Permission or Authority. Permission / Authorization runtime remains F10-owned.

## 11. Context / Evidence / Learning boundaries

Context is not Truth. Evidence is not Authority. AI summary / memory / cache is NON_CANONICAL. Learning may generate governed proposals but may not self-modify Framework definitions.

## 12. Legacy transformation

Legacy values are routed by semantic purpose, not filename/folder. Transformation actions may include KEEP, GENERALIZE, SPLIT, MERGE, RECLASSIFY, COMPATIBILITY_ONLY and RETIRE_WITH_APPROVAL. One Legacy source may split into multiple Banyan objects. Migration execution must not invent missing architecture.

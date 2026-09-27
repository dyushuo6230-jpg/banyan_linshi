# 02_TARGET_DESIGN.md

> **Candidate status:** `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW`. v1.0 approval/freeze statements below are retained as historical source-contract evidence; this v1.1 text is not a new freeze or implementation authorization.


Source v1.0 Status: `HUMAN_APPROVED`
Source v1.0 Architecture Freeze: `PASS`
Current Candidate: `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW`

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


### Candidate integration — role assignment

`RoleAssignment` is F1 Assignment family: responsibility + subject + scope + lifetime. A Workflow/Node's RoleRequirement and a resolved responsible role are different from Assignment, and none grants authority or permission. Generic `RoleBinding` is retired in the target semantics; historical occurrences require semantic mapping.
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


### Candidate integration — execution constraints

`SkillRequirement`, `SkillPin` and `SkillExclude` are execution constraints; SkillEligibility and SkillResolution are contextual results; SkillInvocation is an execution fact. Generic `SkillBinding` is retired. A temporary resolved method does not mutate a durable binding.
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


### Candidate integration — workflow choice and adaptive gate

Banyan may compose governed WorkflowDefinitions, subworkflows and control semantics into task candidates, but cannot invent a new canonical WorkflowDefinition at runtime. Filter candidates by authority, scope, policy, gates and reliability before comparison. Collapse equivalent and dominated candidates. One legal route or a deterministic equivalence resolves automatically. For multiple valid materially different routes, scoped preference is `AUTO` or `ASK_WHEN_MULTIPLE_VALID`; task override > project preference > user default is preference resolution, not authority priority. ASK uses the existing informed-decision protocol with scope, impact, validation, risk, maintenance and material differences; AI recommendation is not the decision. AUTO never silently expands scope. Choice preference is independent of FAST/NORMAL/CONTROLLED execution governance mode; selected workflow is not product decision, approval, apply authorization or runtime permission.

Gate applicability and need for human interaction are separate. Deterministic gates resolve automatically; HOLD survives until its authorized release condition, while REVIEW_REQUIRED marks a genuine unresolved governance choice. Applicable BLOCKED, STALE and UNKNOWN results cannot be treated as PASS. A valid bounded upstream authorization can continue across ordinary lifecycle stages without duplicate confirmation.
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


### Candidate integration — dependencies and effective state

Resolution reads governed Definition/Assignment/Binding/Policy/Authority facts and produces scoped, contextual, rebuildable results, never new authority. A hard dependency exists only if target A cannot legally resolve without target B. Build the active, minimum sufficient graph by scope/context; distinguish a Workflow loop from a resolver dependency cycle. Cycle diagnosis and deterministic convergence are automatic where possible; terminate nonconvergent or oscillating cases as typed UNKNOWN/BLOCKED/CONFLICTED/UNRESOLVED rather than loop forever or let scheduler order pick a winner. Human informed choice is reserved for multiple legitimate material semantic outcomes, not missing evidence or technical failure.
## 8. Handoff

Handoff is a typed transition contract, not necessarily a dedicated node. It can carry result/output refs, canonical/context refs, evidence refs, decision state, blockers, unknowns, downstream required inputs and validation state. Complex handoff work may become a Functional Node.


### Candidate integration — handoff integrity

A material handoff preserves the qualifiers needed for its purpose: source owner, consumer, subject, scope/context, typed result, authority and resolution basis, revision/version, freshness/applicability, state/gate/decision qualifiers, blockers, unknowns, holds, provenance, deferred guards and downstream obligations where applicable. Minimum sufficient context can omit irrelevant data, not governing qualifiers. Handoff acceptance is not perpetual validity: at point of use, validate relevant basis and context; mismatch routes to owner re-resolution and does not give the consumer mutation authority. Missing required qualifier never means PASS. Future F9 supplies evidence and F10 consumes under its own runtime permission boundary.
## 9. Validation

Keep separate: Invocation Success / Node Success / Workflow Success / Goal Success. Skill validation does not replace Node or Goal validation.


### Candidate integration — operational failure

Classify error, attempt failure, validation failure, dependency failure, drift, semantic conflict and governance block before routing. Retry is bounded repetition of the same authorized objective; fallback requires a pre-governed semantically compatible path; technical recovery is not semantic rollback. Failed revalidation does not automatically require human choice; route affected scope to the responsible owner and keep independent work available.

Operational error and failure are scoped to their attempt, invocation, node, workflow or goal. Automatic recovery is eligible only if deterministic, within the existing authorization envelope, preserving evidence/history and without new semantic intent, scope expansion or gate bypass. Governed exceptions carry scope, authority and validity; expiry triggers owner re-resolution rather than being treated as an operational error.
## 10. Policy / Standard / Permission boundaries

Policy = mandatory / forbidden governance constraint semantics.

Engineering Standard is a distinct governed engineering semantic domain. Current-project Effective Engineering Standards are a scoped, derived, rebuildable resolution result, not a second ProjectArtifact Canonical Semantic Truth. Framework / organization / external standards may be reusable sources or packs, but do not automatically become project truth. ProjectInstance / Binding stores applicability, scope, selection and references, not duplicated standard bodies. Engineering Standards Steward has no automatic Canonical Apply Authority. No `StandardDefinition` is added in F4.

Role, Skill, Provider and Workflow do not grant Permission or Authority. Permission / Authorization runtime remains F10-owned.

## 11. Context / Evidence / Learning boundaries

Context is not Truth. Evidence is not Authority. AI summary / memory / cache is NON_CANONICAL. Learning may generate governed proposals but may not self-modify Framework definitions.

## 12. Legacy transformation

Legacy values are routed by semantic purpose, not filename/folder. Transformation actions may include KEEP, GENERALIZE, SPLIT, MERGE, RECLASSIFY, COMPATIBILITY_ONLY and RETIRE_WITH_APPROVAL. One Legacy source may split into multiple Banyan objects. Migration execution must not invent missing architecture.

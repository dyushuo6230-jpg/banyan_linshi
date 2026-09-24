# F4 Orchestration Semantic Freeze Pack v1.0
## 01_RECONCILIATION.md

Status: `ARCHITECTURE_FREEZE_PASS`  
Implementation Authorized: `false`  
RP2 Implementation Authorized: `false`  
Final Activation: `NOT_AUTHORIZED`

## Purpose

This file reconciles four required sources for F4: historical Human Decisions, Legacy v3.1 semantics, accepted R0/R1/RP1 evidence, and current Banyan Framework reality.

F4 freezes Role / Capability / Skill / Workflow semantics and their boundaries with Policy, State, Decision, Provider, Standards, Context, Evidence, Binding, Permission and Validation. It does **not** authorize implementation, Authority Cutover, Legacy retirement, `.banyan` re-initialization, or Final Activation.

## Upstream frozen contracts

### F1
- First-class objects remain Artifact, ProjectInstance, Binding, RuntimeExecution, Context, EvidenceTrace, Infrastructure.
- DefinitionArtifact / ProjectArtifact separation remains.
- WorkflowDefinition != WorkflowRun; SkillDefinition != invocation; StateModelDefinition != runtime State; DecisionProtocolDefinition != DecisionSession.
- EvidenceTrace is non-Artifact granular evidence; EvidencePackage is a ProjectArtifact aggregate.

### F2
- No single total-truth DB.
- Same semantic fact has one Canonical Write Target.
- Definition / Project Artifacts default to governed files as Canonical Semantic Truth.
- SQLite remains Derived / Rebuildable / Query Layer.
- Runtime operational truth cannot override Artifact Semantic Truth.
- Latest/freshest does not decide Authority.
- AI summaries, memory and caches are NON_CANONICAL.

### F3
Exactly ten DefinitionArtifact types remain frozen: RoleDefinition, CapabilityDefinition, SkillDefinition, WorkflowDefinition, PolicyDefinition, StateModelDefinition, DecisionProtocolDefinition, TemplateDefinition, ProviderContractDefinition, CompatibilitySpecDefinition. F4 adds no new type.

## Legacy / R1 preservation

R1 preserved 43 migrated artifacts across Role, Policy, Skill, Workflow, State, Template, Decision Protocol, Context Recovery and Compatibility. F4 preserves these invariants:

- Capability != Skill
- Role != Permission != Git Identity != Authentication
- Source Role != Collaboration Role != Banyan Functional Role
- State domains remain separate
- no 35-Capability-to-35-Skill promotion

Legacy/planning material is a value/evidence source, not a target schema. Migration is semantic transformation, not direct copy.

## Current reality

Architecture is ahead of implementation. Current reality still includes gaps in full Workflow execution, natural-language orchestration, collaboration-role runtime, full ProjectInstance binding, Canonical Apply execution, Context/Evidence/Learning runtime and Final Activation. Therefore F4 PASS must never be represented as runtime completion.

## Resolved F4 conflicts

- Skill is optional by default.
- `NO_ELIGIBLE_SKILL` alone does not automatically block.
- Functional Role is a stable responsibility cluster, not a person/tool/provider/technology/task-step.
- Workflow is a goal-oriented graph, not a fixed Role/Skill sequence.
- Workflow Atom is a composition concept, not a DefinitionArtifact.
- Engineering Standard is a distinct governed semantic domain; F4 does not add StandardDefinition.
- Provider cannot redefine Role/Capability/Skill semantics.
- Evidence does not grant Authority.
- Learning does not self-modify Framework definitions.
- G0-G11 is Project Lifecycle / Compatibility, not a mandatory daily execution pipeline.

## Deferred with explicit owners

Deferred without blocking F4: final Capability catalog, final domain Skill catalogs, detailed Participation/Governance Role catalog, detailed Policy/State/Decision/Template/Provider architecture, Standards physical model, ProjectInstance binding implementation, Permission runtime, Context/Evidence/Learning implementation, physical directories, schemas, DB DDL, Runtime API, adapters and migration execution.

## CROSS-STAGE-GATE-01

Before Full Legacy Semantic Migration / Authority Cutover / Canonical Rewrite / Legacy Retirement / Final Binding Activation, these domains must reach Architecture Freeze or an explicitly approved equivalent owner-stage gate: Role, Capability, Skill, Workflow, Policy, State Model, Decision Protocol, Template / Output Contract, Provider Contract, Engineering Standard, Context, Evidence / Trace, Binding / Assignment, Permission / Authority, Validation / Acceptance, Compatibility / Migration.

Required zero conditions:
- `UNROUTED_HIGH_VALUE_SEMANTIC = 0`
- `SEMANTIC_OWNER_GAP = 0`
- `UNRESOLVED_HIGH_IMPACT_TYPE_MAPPING = 0`
- `SILENT_SEMANTIC_DROP = 0`

Before that gate passes, discovery, inventory, semantic audit, migration mapping, compatibility analysis, shadow projection and dry-run are allowed. Full semantic migration and truth cutover are not.

## Result

`PASS_F4_ORCHESTRATION_SEMANTIC_ARCHITECTURE_FREEZE`

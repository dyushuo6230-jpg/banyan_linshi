# F1 Core Object Model — Target Design v1.0

> Status: HUMAN_APPROVED

## 1. Top-level model

```text
Banyan Core Object Model
│
├── Artifact
│   ├── DefinitionArtifact
│   └── ProjectArtifact
│
├── ProjectInstance
├── Binding
├── RuntimeExecution
├── Context
├── EvidenceTrace
└── Infrastructure
```

## 2. First-class object != Artifact

A Banyan object may be first-class because it has stable identity, schema, lifecycle, references, provenance or runtime semantics. That alone does not make it an Artifact.

Artifact is reserved for governed reusable definition semantics or governed formal project engineering semantics.

## 3. Artifact

### DefinitionArtifact
Framework-level reusable definitions.

Candidate subtypes, not yet frozen until F3:
- RoleDefinition
- CapabilityDefinition
- SkillDefinition
- WorkflowDefinition
- PolicyDefinition
- StateModelDefinition
- DecisionProtocolDefinition
- TemplateDefinition
- ProviderContractDefinition
- CompatibilitySpecDefinition

### ProjectArtifact
Formal project engineering outputs/truths.

Candidate subtypes for later freeze:
- PRD
- UI_SPEC
- ADR
- DEC
- CHANGE / CR
- TechnicalDesign
- TestSpec
- EvidencePackage
- Handover
- Worklog

## 4. ProjectInstance

Represents how one concrete project participates in Banyan:
- project identity
- Framework version pin
- source mappings
- project variables
- provider selection
- overlay bindings
- runtime/index/trace locations
- migration state

`ProjectInstance != Artifact`.

## 5. Binding

Represents concrete associations such as:
- RoleBinding
- SkillBinding
- ProviderBinding
- SourceMapping
- OverlayBinding

`Binding != Artifact`.

## 6. RuntimeExecution

Represents concrete execution instances:
- Task
- WorkflowRun
- StepRun
- DecisionSession
- Checkpoint
- ProviderInvocation

Permanent rule:

```text
WorkflowDefinition != WorkflowRun
StateModelDefinition != Runtime State
SkillDefinition != Skill Invocation
DecisionProtocolDefinition != DecisionSession
```

## 7. Context

Represents working context assembled for a task/run. Detailed Context/Memory/Freshness design belongs to F9.

## 8. EvidenceTrace

Fine-grained factual evidence:
- EvidenceRecord
- TraceEvent
- ValidationResult
- TestEvidence
- CommitEvidence
- ProvenanceRecord

Rules:
- EvidenceTrace is a first-class family
- it is not automatically a ProjectArtifact
- it proves facts; it does not grant authority
- latest trace/event does not automatically become Canonical Truth

## 9. EvidencePackage

`EvidencePackage` is a ProjectArtifact.

It formally aggregates many evidence records, validations, decisions, changes and source references for:
- acceptance
- review
- release
- archival
- long-term traceability

```text
many EvidenceTrace records
        ↓
formal aggregation
        ↓
EvidencePackage : ProjectArtifact
```

## 10. Infrastructure

Examples:
- Registry
- Loader
- Manifest
- Schema Registry
- SQLite Index
- Reference Graph
- Cache

These support discovery/loading/validation/querying and are not semantic Artifacts.

```text
Registry != Artifact
Loader != Artifact
SQLite Index != Artifact
Reference Graph != Artifact
```

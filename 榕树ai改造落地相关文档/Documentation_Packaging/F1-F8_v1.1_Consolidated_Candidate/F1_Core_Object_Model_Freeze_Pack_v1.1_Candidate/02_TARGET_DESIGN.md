# F1 Core Object Model — Target Design v1.0

> **Candidate status:** `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW`. v1.0 approval/freeze statements below are retained as historical source-contract evidence; this v1.1 text is not a new freeze or implementation authorization.


> Source v1.0 status: HUMAN_APPROVED; current v1.1 Candidate status: AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW

## 1. Top-level model

```text
Banyan Core Object Model
│
├── Artifact
│   ├── DefinitionArtifact
│   └── ProjectArtifact
│
├── ProjectInstance
├── Assignment
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

DefinitionArtifact type ownership is F3; its candidate taxonomy currently includes:
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
- ConfigurationProfileDefinition

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


### Candidate integration — identity and responsibility

Stable ID identifies the same semantic subject across path, provider and ordinary physical changes. Revision identifies an accepted semantic change to that subject; Version identifies an explicitly governed release target and is not required for every object or every revision. `Latest != Current Effective`; current effectiveness is resolved for scope and context from governed inputs.

Version is a governed release coordinate, not its Version Scheme or SemVer; Revision is not a patch version. A published exact Version must remain bound to its published Release Target, either one exact Revision or a coherent immutable release set. The same exact Version may not silently point to different content later. Governance-relevant `Latest` must name its ordering domain (for example Latest Revision, Latest Canonical Revision, Latest Published Version, Latest Compatible Version or Latest Observed State); these are distinct and none alone is Current Effective. Physical version strings, numbering algorithms and SemVer policy remain deferred.

`Assignment` is a separate first-class object family: subject + responsibility + scope + lifetime. A RoleAssignment may be project, task or run scoped and may be explicit or resolved. It allocates responsibility; it grants neither authority nor runtime permission. It is distinct from Definition, Binding and RuntimeExecution.
## 5. Binding

Represents concrete associations such as:
- ProviderBinding
- SourceMapping
- OverlayBinding

`Binding != Artifact`.


### Candidate integration — relation and resolution boundary

Binding is a durable, governed adoption / association / constraint relation with explicit purpose, scope and applicability. Valid relation-purpose families include Source, Configuration Profile, Provider, Version Pin/Constraint, Feature Activation and Standard Adoption. Domain and scope qualify a relation; they do not create technology-specific binding classes. A binding record is neither its current effective result nor authority.

The generic `RoleBinding` and `SkillBinding` examples are retired in the target architecture. Historical uses map by meaning: responsibility → RoleAssignment; required role → RoleRequirement; resolved role → Responsibility Resolution; required/pinned/excluded skill → execution constraint; eligible/selected skill → Skill Resolution; actual invocation → RuntimeExecution. Legacy terms remain readable until separately governed migration.

Multiple applicable bindings are resolved against a semantic target, not by file order or latest timestamp. Composition, alternative, fallback, override, constraint and mutual exclusion have distinct meanings. Resolution results are derived, rebuildable, scoped and traceable; temporary selection never creates durable rebinding. A typed state result must retain subject, domain, dimension, value, scope/context, basis/provenance and owner; the same label in different domains is not the same state.
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


### Candidate integration — evidence and exception boundaries

Evidence, index, trace and context can support impact discovery and state/authority resolution, but cannot become authority or canonical truth by projection. Operational failure evidence and a governed exception are separate: only an eligible, scoped, authorized exception changes how a rule applies. Error, failed attempt and final failure must identify their own subject and domain.
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

### Candidate integration — exhaustive approved-clause closure

Typed state keeps subject, domain, dimension, value, scope, context, basis, provenance, and owner. The same label in another domain is not the same state. Shared minimum meanings: STALE suspends current reliance and keeps history; UNKNOWN is insufficient evidence and is not false or absent; BLOCKED stops the affected protected action; CONFLICTED is a real incompatibility and is not a cycle, drift, divergence, error, or unknown; REVIEW_REQUIRED is an unresolved governance choice; HOLD waits for an authorized release and is not REVIEW_REQUIRED and not BLOCKED; SUPERSEDED is replaced and is not deleted. UNRESOLVED is a required resolution without a valid result and is not CONFLICTED. Adaptive gate states PASS, BLOCKED, HOLD, REVIEW_REQUIRED, UNRESOLVED, and STALE stay expressible and distinct. Event != State. Exception != State. Error != Conflict. State projection != state copy != authority transfer. Handoff state != receiving-domain state. State consumer != state owner. Governed state fact != derived effective state. Derived state != canonical truth. A cross-domain state change is not a direct downstream transition; the path is impact, then STALE or another typed non-current state, then owner re-resolution. Current effective != lifecycle != freshness. A new current value does not rewrite history. A snapshot is not authority. A local state block is not a global project block. Index miss != state absent. Legacy status that cannot be determined stays UNKNOWN or UNRESOLVED. AI guess != state-domain resolution.

A bare exception label is semantically ambiguous. Error != failure. A failed attempt != the final operation failure. Unbounded retry is forbidden. Retry allowed != retry until success. Warning != BLOCKED. A violation is not by itself a governed exception and is not by itself an operational error. Silent governed exception is forbidden. Silent durable rebinding is forbidden. GlobalExceptionManager, UniversalFailureEngine, and UniversalRecoveryEngine are forbidden. A downstream consumer may resolve UNKNOWN, BLOCKED, STALE, or UNAFFECTED. Failure propagation != state copy. Technical recovery != reconciliation != re-resolution. Failure handling order is a domain contract and is not governance precedence. Degraded != unrestricted success. Detection direction != authority direction. An index or trace that detects a condition does not gain authority to rewrite the upstream canonical fact.

Handoff integrity: GlobalHandoffAuthority and UniversalHandoffResolver are forbidden. Handoff composition != state-domain merge and != authority merge. Multiple authority references are not a combined authority. The same payload with a different handoff purpose is not the same authorization. Context compression != governance compression. Handoff projection != semantic downgrade. Upstream STALE cannot silently become CURRENT. BLOCKED and HOLD cannot disappear during handoff projection. Handoff accepted != basis valid forever. Point-of-use revalidation != full re-resolution and != recomputing the whole architecture every time. Missing required qualifier != PASS. Later consumer != higher authority. Handoff order != authority priority. Authority reference != authority transfer. Authority reference exists != authority still applicable. Decision evidence != apply authorization != runtime permission. Freshness evidence != authority. Handoff integrity != full evidence duplication. Effective resolution context != canonical truth. Index != handoff authority. Trace != handoff authority. Scope projection may narrow and must not silently enlarge. Revalidation failure != human decision required. Current effective handoff != eternal effective truth.

F1 closure: a resolution result is derived, rebuildable, scope-aware, task-aware when a task context applies, and traceable. Resolution Result != Canonical Truth. Latest != Current Effective. Resolution does not write a durable canonical binding. Generic skill-binding rebirth names SkillRequirementBinding, SkillPinBinding, and SkillExcludeBinding are forbidden; those meanings stay execution constraints. Default-allow or recommend maps to Configuration Profile, Policy, or Execution Constraint, not to a new binding family. Legacy read order is Legacy Term, then Semantic Identification, then No-Loss Mapping, then New Explicit Semantic. Index Match != Effective Assignment and Index Match != Effective Binding. UniversalResolver is forbidden. UniversalBindingResolver is forbidden. F1 owns the Assignment and Binding families and the global boundary; it does not own domain resolution results.

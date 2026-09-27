# 02_TARGET_DESIGN.md

> **Candidate status:** `AWAITING_FINAL_CONSOLIDATED_FREEZE_REVIEW`. v1.0 approval/freeze statements below are retained as historical source-contract evidence; this v1.1 text is not a new freeze or implementation authorization.


# F3 — Target DefinitionArtifact Taxonomy

```text
DefinitionArtifact
├── RoleDefinition
├── CapabilityDefinition
├── SkillDefinition
├── WorkflowDefinition
├── PolicyDefinition
├── StateModelDefinition
├── DecisionProtocolDefinition
├── TemplateDefinition
├── ProviderContractDefinition
├── CompatibilitySpecDefinition
└── ConfigurationProfileDefinition
```

Each logical DefinitionArtifact has:
- exactly one Primary Type,
- zero or more Domains,
- zero or more Tags,
- zero or more typed Relations.

## Type semantics

`RoleDefinition` — defines semantic responsibility/role boundaries; not a person, job title, Git identity, permission, authentication, or Project Authority.

`CapabilityDefinition` — defines what capability is required.

`SkillDefinition` — defines a concrete executable method/method contract; tools/providers/models may implement or support a Skill but are not automatically Skills.

`WorkflowDefinition` — defines reusable control-flow semantics; not `WorkflowRun`, `StepRun`, or `Checkpoint`.

`PolicyDefinition` — defines rules, constraints, prohibitions, safety floors, and governance semantics; not a runtime evaluator.

`StateModelDefinition` — defines an independent state domain, its states, meanings, and transition/constraint model; not a current state value.

`DecisionProtocolDefinition` — defines governed decision interaction/routing semantics; not a `DecisionSession` or Human Decision record.

`TemplateDefinition` — defines reusable creation scaffolding. `Template != Schema != Instance`.

`ProviderContractDefinition` — defines the contract/port a provider implementation must satisfy; not ProviderBinding or project provider selection.

`CompatibilitySpecDefinition` — defines compatibility and semantic mappings; not MigrationRun, MigrationState, adapter code, or test results.


### Candidate integration — profile, rules and state semantics

`ConfigurationProfileDefinition` is the eleventh primary type: a reusable governed composition with typed component references, scope/applicability, version/compatibility and explicit override references. It is distinct from ProfileBinding (adoption), ProjectProfileInstance (project facts), and the derived effective profile result. Profile composition uses typed relations, without implicit file-order priority or forced latest upgrade. Project-local differences remain project-local unless a separately governed shared change is warranted.

Banyan maintains derived references, indexes, freshness, impact and change candidates under governance. Canonical profile mutation goes through F7; maintenance confers no autonomous semantic authority. A Rule Entry may be constraint, applicability, resolution, override, validation, transformation or guidance; entries and modules can be owned/referenced by PolicyDefinitions and Rule Systems without creating a `RuleDefinition` top type. An Engineering Standard Pack is a governed standard composition, not a Configuration Profile and not a new `StandardDefinition`. `StateModelDefinition` specifies a state domain, never a runtime/current state fact. `DecisionProtocolDefinition` supplies informed choice; workflow preference does not add a top-level definition type.
## Single Primary Type

Forbidden:
```yaml
type:
  - WorkflowDefinition
  - PolicyDefinition
```

Required pattern:
```yaml
type: WorkflowDefinition
domain:
  - ContextRecovery
governed_by:
  - <PolicyDefinition ID>
requires:
  - <CapabilityDefinition ID>
```

## Closed-but-Extensible

The eleven types are closed by default. New feature/domain/provider names do not create new top-level types. Any new type requires a versioned F3 Change Proposal, proof existing types cannot express it without semantic loss, impact analysis, migration impact, and Human Decision.


### Candidate integration — type-change and reference guard

The approved eleventh type is an explicit taxonomy change, not permission for unbounded type growth. Further types still require no-loss proof, impact/migration analysis, a versioned proposal and human decision. Stable ID, accepted Revision, optional Version and scope-aware Current Effective remain separate. Exact schema, enum, loader and migration mechanics are deferred; no current RP2 or authority cutover follows from this taxonomy.
## Context Recovery

```text
ContextRecovery = Domain / Capability Area
```

Current R1/RP1 `CONTEXT_RECOVERY` artifacts remain untouched in F3. Exact long-term mapping is deferred to F9.

## Infrastructure boundary

`Schema / Registry / Manifest / Schema Index / Loader / Validator` are infrastructure/discovery/validation concerns by default, not DefinitionArtifact Types.

## Out of scope

F3 does not freeze Role kinds, Role→Capability mapping, Skill Resolver, Workflow Node schema, Permission model, Provider selection, ProjectInstance bindings, physical artifact directories, Loader/Registry implementation, F9 Context mapping, or RP2 authority cutover.

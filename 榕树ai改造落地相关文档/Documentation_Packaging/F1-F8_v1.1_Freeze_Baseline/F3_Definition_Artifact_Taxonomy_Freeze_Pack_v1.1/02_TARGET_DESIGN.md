# 02_TARGET_DESIGN.md

> **Freeze status:** `FROZEN_ARCHITECTURE_CONTRACT`. Human approval, architecture freeze, and this v1.1 freeze baseline are established. v1.0 approval/freeze statements below remain historical source-contract evidence. This freeze does not authorize implementation.


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

Banyan maintains derived references, indexes, freshness, impact and change candidates under governance. Canonical profile mutation goes through F7; maintenance confers no autonomous semantic authority. A Rule Entry is the minimum stable, addressable governed rule semantic unit and may be constraint, applicability, resolution, override, validation, transformation or guidance. One Rule Entry has exactly one Canonical Primary Rule Module, which fixes its primary knowledge responsibility, canonical write target and maintenance owner. PolicyDefinitions, other Modules, Engineering Standard Packs and Rule Systems may consume it through reference, tag, domain, index association or typed relation; they do not acquire Rule Entry canonical ownership or copy its rule body. This does not create a `RuleDefinition` top type.

A Rule Module is the minimum coherent knowledge responsibility, organization, loading and maintenance boundary. A PolicyDefinition organizes one or more Rule Entries around a minimum coherent governance purpose; neither a tiny-rule-per-Policy explosion nor an everything-Policy is the target. PolicyDefinition, Rule Module, Rule System and Engineering Standard remain distinct. An Engineering Standard Pack is a governed standard composition, not a Configuration Profile and not a new `StandardDefinition`; a project's current effective standard set remains a derived result, not second canonical standard truth. `StateModelDefinition` specifies a state domain, never a runtime/current state fact. `DecisionProtocolDefinition` supplies informed choice; workflow preference does not add a top-level definition type.
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

### Candidate integration — exhaustive approved-clause closure

Typed state keeps subject, domain, dimension, value, scope, context, basis, provenance, and owner. The same label in another domain is not the same state. Shared minimum meanings: STALE suspends current reliance and keeps history; UNKNOWN is insufficient evidence and is not false or absent; BLOCKED stops the affected protected action; CONFLICTED is a real incompatibility and is not a cycle, drift, divergence, error, or unknown; REVIEW_REQUIRED is an unresolved governance choice; HOLD waits for an authorized release and is not REVIEW_REQUIRED and not BLOCKED; SUPERSEDED is replaced and is not deleted. UNRESOLVED is a required resolution without a valid result and is not CONFLICTED. Adaptive gate states PASS, BLOCKED, HOLD, REVIEW_REQUIRED, UNRESOLVED, and STALE stay expressible and distinct. Event != State. Exception != State. Error != Conflict. State projection != state copy != authority transfer. Handoff state != receiving-domain state. State consumer != state owner. Governed state fact != derived effective state. Derived state != canonical truth. A cross-domain state change is not a direct downstream transition; the path is impact, then STALE or another typed non-current state, then owner re-resolution. Current effective != lifecycle != freshness. A new current value does not rewrite history. A snapshot is not authority. A local state block is not a global project block. Index miss != state absent. Legacy status that cannot be determined stays UNKNOWN or UNRESOLVED. AI guess != state-domain resolution.

A bare exception label is semantically ambiguous. Error != failure. A failed attempt != the final operation failure. Unbounded retry is forbidden. Retry allowed != retry until success. Warning != BLOCKED. A violation is not by itself a governed exception and is not by itself an operational error. Silent governed exception is forbidden. Silent durable rebinding is forbidden. GlobalExceptionManager, UniversalFailureEngine, and UniversalRecoveryEngine are forbidden. A downstream consumer may resolve UNKNOWN, BLOCKED, STALE, or UNAFFECTED. Failure propagation != state copy. Technical recovery != reconciliation != re-resolution. Failure handling order is a domain contract and is not governance precedence. Degraded != unrestricted success. Detection direction != authority direction. An index or trace that detects a condition does not gain authority to rewrite the upstream canonical fact.

Handoff integrity: GlobalHandoffAuthority and UniversalHandoffResolver are forbidden. Handoff composition != state-domain merge and != authority merge. Multiple authority references are not a combined authority. The same payload with a different handoff purpose is not the same authorization. Context compression != governance compression. Handoff projection != semantic downgrade. Upstream STALE cannot silently become CURRENT. BLOCKED and HOLD cannot disappear during handoff projection. Handoff accepted != basis valid forever. Point-of-use revalidation != full re-resolution and != recomputing the whole architecture every time. Missing required qualifier != PASS. Later consumer != higher authority. Handoff order != authority priority. Authority reference != authority transfer. Authority reference exists != authority still applicable. Decision evidence != apply authorization != runtime permission. Freshness evidence != authority. Handoff integrity != full evidence duplication. Effective resolution context != canonical truth. Index != handoff authority. Trace != handoff authority. Scope projection may narrow and must not silently enlarge. Revalidation failure != human decision required. Current effective handoff != eternal effective truth.

F3 closure: the current taxonomy has eleven top-level types, including ConfigurationProfileDefinition. Historical ten-type decisions stay under source_baseline. ConfigurationProfileDefinition != Manifest, PolicyDefinition, TemplateDefinition, WorkflowDefinition, CompatibilitySpecDefinition, and ProjectArtifact. It may carry composition purpose, applicability envelope, typed references, scope, version, and override references. It must not be the canonical owner of a path, provider selection, secret, credential, runtime permission, or live state, and it is not a project configuration dump. Domain and tag express technology differences; FrontendProfileDefinition, BackendProfileDefinition, and other technology-named profile types are forbidden. The effective chain is definition, then ProfileBinding, then ProjectProfileInstance, then overlay, project fact, and variable resolution. Profile resolution does not create authority and does not alter referenced canonical truth. A new Rule or Module does not automatically change every related profile. Maintenance has three layers: derived upkeep that must not change canonical meaning; change-candidate preparation that is not a canonical change; canonical mutation through F7, which is neither always human nor always automatic. The user owns why and whether; Banyan owns what relates, what is affected, and what applies now. This patch set adds no RuleDefinition, StandardDefinition, ModuleDefinition, or GateDefinition. StateModelDefinition is not a runtime state. F3 classifies definition artifacts; it does not own operational recovery or a global exception engine.

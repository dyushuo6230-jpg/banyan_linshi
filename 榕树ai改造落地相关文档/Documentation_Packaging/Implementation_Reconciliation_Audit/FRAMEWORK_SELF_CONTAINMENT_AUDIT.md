# Framework Self-Containment Audit

## Verdict

`FRAMEWORK_RELEASE_NOT_SELF_CONTAINED`

The bounded Runtime and Control Plane can run from `banyan-framework/`, but the released Framework cannot independently locate and interpret the complete governance and capability model it claims. Authoritative definitions remain under the temporary `.banyan-refactor/stages/**` construction tree. Documentation summaries inside the Framework do not replace machine-readable registries, schemas, loaders, and consumers.

## Required surfaces

### Capability Contract Registry

- Result: `EXTERNAL_ONLY`.
- Authoritative source: `.banyan-refactor/stages/03/stage03-20260920T135702Z/CAPABILITY_CONTRACT_REGISTRY.yaml`.
- Framework state: D0/D1 describe 35 contracts, but no registry is shipped or loaded.
- Runtime consequence: the Runtime cannot enumerate or validate all 35 contracts.

### Artifact Registry / Schema

- Result: `EXTERNAL_ONLY`.
- Authoritative source: Stage 03 Artifact Registry artifacts.
- Framework state: provenance fields are rendered by the Control Plane; there is no Artifact Registry implementation or schema loader.
- Runtime consequence: stable IDs, lifecycle, authority, references, and supersession are not enforced as one artifact model.

### Source Role Registry

- Result: `EXTERNAL_ONLY`.
- Authoritative source: `.banyan-refactor/stages/03/stage03-20260920T135702Z/SOURCE_ROLE_REGISTRY.yaml`.
- Framework state: documentation and provenance display mention source roles; no registry is shipped.
- Runtime consequence: authority resolution cannot be reproduced from the Framework alone.

### Workflow contracts

- Result: `EXTERNAL_ONLY`.
- Authoritative sources: Stage 05 `ADAPTIVE_WORKFLOW_SCHEMA.yaml` and `WORKFLOW_STATE_TRANSITION_SCHEMA.yaml`.
- Framework state: workflow reference documentation exists; no router, executor, registry, or loader exists.
- Runtime consequence: target workflows cannot be selected or advanced by the Runtime.

### State definitions

- Result: `PARTIAL`.
- Framework state: action permission enums, Runtime status, and Pilot state exist.
- External dependency: complete artifact, workflow, Change, decision, freshness, index, and migration states remain in Stage contracts.
- Runtime consequence: the release cannot validate the whole lifecycle vocabulary.

### Role definitions

- Result: `DOCUMENTATION_ONLY`.
- Framework state: `docs/reference/ROLE_REFERENCE.md` describes roles.
- Missing: Runtime enum, binding schema, registry, authority resolver, and tests for the four collaboration roles.

### Skill catalog / provider skill references

- Result: `EXTERNAL_COMPATIBILITY_ONLY`.
- Framework state: `docs/reference/SKILL_REFERENCE.md` is descriptive.
- External assets: `.cursor/skills/visual-repair-loop/SKILL.md` and `tools/anydesign/SKILL.md`.
- Missing: Framework-native skill catalog, stable provider-skill references, loader, and Runtime consumer.

### Provider Port schemas

- Result: `EXTERNAL_ONLY_WITH_NARROW_BINDING_LOADER`.
- Framework state: `ProviderBindingLoader` validates declarative binding fields; `.banyan` binds only Cursor Pilot and Runtime permission.
- External dependency: general Provider Port schemas and Stage 09 Design ports live in construction evidence.
- Runtime consequence: the loader cannot prove that an arbitrary binding implements a frozen port contract.

### Project Overlay schema

- Result: `EXTERNAL_ONLY_WITH_SHADOW_INSTANCE`.
- Framework state: `.banyan/overlays/bindings.yaml` exists with an empty binding list.
- Authoritative schema: Stage 03/04 construction evidence.
- Runtime consequence: no complete overlay validation or resolution path exists in the release.

### Compatibility mapping

- Result: `EXTERNAL_ONLY_WITH_IMPLEMENTED_EDITOR_SUBSET`.
- Framework state: editor adapters are implemented and tested.
- External dependency: Stage 07 `V31_GOVERNANCE_COMPATIBILITY_MAP.yaml` and Legacy disposition matrices.
- Runtime consequence: the release cannot independently answer how the rest of v3.1 semantics map to current contracts.

### Version / status / provenance rules

- Result: `PARTIAL_DOCUMENTATION_AND_CODE`.
- Framework state: D0/D1 list version dimensions and Control Plane provenance fields; current code preserves unknown values.
- External dependency: authoritative Stage 03 `VERSION_STATUS_PROVENANCE_RULES.yaml`.
- Runtime consequence: the full rule set cannot be validated without the construction tree.

## Release-package evidence

Stage 20's package contains the binary, source archive, Web assets, and 11 release guides. Its package manifest does not include the Stage 03–14 authoritative registries and schemas listed above. Stage 20 simultaneously classifies `.banyan-refactor` as `TEMPORARY_BOOTSTRAP / READY_TO_ARCHIVE_AFTER_FINAL_ACTIVATION`. This creates a lifecycle conflict: the semantic source needed to interpret the release is outside the release and scheduled for eventual retirement.

## Scope of the verdict

The verdict does not mean that the existing Runtime binary cannot start or that Stage 19/20 acceptance is invalid for its tested scope. It means the Framework release is not self-contained as the durable source of truth for the broader v3.1-to-Banyan contract system.

No files were copied into Core during this audit. Packaging or runtime remediation requires a later governed decision.

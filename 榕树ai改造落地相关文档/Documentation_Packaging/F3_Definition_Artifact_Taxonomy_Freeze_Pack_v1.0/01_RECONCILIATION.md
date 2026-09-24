# 01_RECONCILIATION.md

# F3 — Definition Artifact Taxonomy Reconciliation

## Final status

```text
F3_ARCHITECTURE_FREEZE = PASS
DECISIONS = F3-D01..F3-D16
HUMAN_APPROVED = 16/16
TOP_LEVEL_DEFINITION_TYPES = 10

CODE_IMPLEMENTATION_AUTHORIZED = false
RP2_IMPLEMENTATION_AUTHORIZED = false
ARTIFACT_RECLASSIFICATION_AUTHORIZED = false
R1_RP1_AUTHORITY_CUTOVER_AUTHORIZED = false
```

## Four-source basis

F3 reconciles:
- historical human-confirmed Banyan design,
- Legacy v3.1 semantics,
- accepted Refactor/Stage evidence,
- current Framework reality including R0/R1/RP1.

Protected upstream facts:
- `Capability != Skill`
- `Source Role != Collaboration Role != Banyan Role`
- `Role != Permission != GitIdentity != Authentication`
- State domains remain separate.
- `Provider Contract != Provider Binding`
- Definition objects remain separate from Runtime instances.

Current R1/RP1 migration categories remain accepted:
`ROLE / POLICY / SKILL / WORKFLOW / STATE / TEMPLATE / DECISION_PROTOCOL / CONTEXT_RECOVERY / COMPATIBILITY`.

F3 does not retroactively rewrite them.

## Main result

F3 separates:

```text
Type     = what kind of definition is this?
Domain   = what area does it serve?
Relation = how does it connect to other governed objects?
```

Long-term target taxonomy:

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
└── CompatibilitySpecDefinition
```

`Context Recovery` is a Domain/Capability Area, not a permanent top-level type.

R1/RP1 migration shape may differ from long-term taxonomy. Any future transformation must preserve semantic no-loss, Stable ID/lineage, references, compatibility, rollback/recovery boundaries, and controlled authority cutover.

Final audit:

```text
HARD_CONFLICT = 0
TYPE_OVERLAP_BLOCKER = 0
MISSING_REQUIRED_TYPE = 0
DUPLICATE_PRIMARY_TYPE = 0
R1_SEMANTIC_LOSS = 0
RP1_UNAUTHORIZED_RECLASSIFICATION = 0
F1_MODEL_CONFLICT = 0
F2_AUTHORITY_CONFLICT = 0
PREMATURE_IMPLEMENTATION_DECISION = 0
```

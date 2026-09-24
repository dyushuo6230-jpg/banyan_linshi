# Stage 07 Precheck

确认：

```text
Stage06 = PASS_CHANGE_WORKSPACE_AND_CANONICAL_APPLY_CONTRACT_FREEZE
Stage07 Gate = PASS_FOR_STAGE07_REFERENCE_MIGRATION_DESIGN_WITH_INHERITED_BLOCKERS
```

只校验：

```text
Stage06 sealed outputs
Stage01 inventory seals
Stage03/04/05 contracts needed for mapping
HEAD / tracked / staged / conflicts
Bootstrap
13 Secret metadata existence
```

禁止重新 Discovery。

# 20-H Legacy Documentation Adoption Migration

This guide documents a post-release operation; Stage20 does not execute it.

Recommended flow:

```text
DISCOVER
→ CLASSIFY
→ SOURCE ROLE
→ STABLE ID
→ AUTHORITY
→ VERSION / STATUS
→ PROVENANCE
→ REFERENCES
→ SHADOW IMPORT
→ VALIDATE
→ ACTIVATE SEMANTIC ADOPTION
→ OPTIONAL PHYSICAL MIGRATION
```

Default:

```text
docs/project canonical content = PRESERVE_IN_PLACE
Banyan registers/maps/indexes it
generated projections may live in .banyan/generated/
physical relocation requires explicit migration
```

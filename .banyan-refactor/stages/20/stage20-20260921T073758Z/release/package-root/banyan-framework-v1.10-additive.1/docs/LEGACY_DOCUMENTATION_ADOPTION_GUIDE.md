# Legacy Documentation Adoption Guide

This is a future post-release procedure. Stage 20 does not execute it. Existing documentation, including `docs/project`, remains preserve-in-place.

Use this sequence:

1. Discover candidate documents without moving them.
2. Classify canonical, operational, historical, generated and sensitive roles.
3. Assign a Source Role and stable ID.
4. Record authority, version, status, freshness and conflict state.
5. Capture provenance and source references without reading prohibited Secret bodies.
6. Build and validate the reference graph; keep missing historical targets unresolved.
7. Create a shadow import or mapping into Banyan Artifact semantics.
8. Validate counts, hashes, references, no-loss coverage and rollback readiness.
9. Obtain explicit authorization for semantic adoption.
10. Consider physical relocation only as a separate optional migration.

Semantic adoption means Banyan can map, query, validate and trace a document while it stays at its existing path. Generated projections may live under `.banyan/generated/`. Canonical physical relocation requires its own impact review, source/target mapping, reference repair plan, checkpoint, authorization and rollback validation.

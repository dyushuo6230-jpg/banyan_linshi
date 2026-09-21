# Project Instance Guide

`.banyan/` holds project-scoped Banyan state. The current instance is `PROJECT_INSTANCE_SHADOW_PILOT`; it has not replaced project canonical sources and is not finally activated.

- `instance/` describes the Project Instance identity and state.
- `mappings/` maps existing sources to Banyan semantics.
- `overlays/` contains project-specific binding overlays without changing generic Core.
- `profiles/` contains project/contributor metadata; profiles do not grant authorization.
- `providers/` records provider bindings and activation state.
- `runtime/` records runtime status, not canonical truth.
- `trace/` stores audit lineage; trace does not authorize.
- `index/` stores derived lookup metadata and is not canonical truth.
- `generated/` contains derived projections.
- `migrations/` contains migration and rollback records.
- `pilot.yaml` declares the Pilot boundary.

Canonical sources remain in place by default. Mappings and indexes may point to them. Generated and indexed state must be rebuildable from accepted sources. Promotion from Pilot requires explicit Human Project Authority, satisfied safety gates, a checkpoint, rollback readiness and a separate activation decision.

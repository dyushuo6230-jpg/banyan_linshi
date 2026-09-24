# Stage 18.5 Validation

| ID | Check | PASS |
|---|---|---|
| V18_5-01 | Upstream | Stage18 seal valid |
| V18_5-02 | Scope | no Legacy/full rediscovery |
| V18_5-03 | Inventory | current implementation boundary recorded |
| V18_5-04 | ADR | target stack frozen |
| V18_5-05 | Frontend Baseline | Ant Design Pro Simple / demos removed |
| V18_5-06 | Feature Matrix | every Stage16 feature dispositioned |
| V18_5-07 | Feature Equivalence | no silent feature loss |
| V18_5-08 | Gin Boundary | transport only |
| V18_5-09 | Permission | no second engine |
| V18_5-10 | Runtime Bridge | single existing Runtime path |
| V18_5-11 | Bridge Failure | typed / fail closed |
| V18_5-12 | API Contract | compatibility tests pass |
| V18_5-13 | SPA | deep-link fallback valid |
| V18_5-14 | API Routing | API 404 not SPA fallback |
| V18_5-15 | Static Build | production build passes |
| V18_5-16 | Asset Manifest | hashes generated/verified |
| V18_5-17 | Embed | static UI embedded in Go binary |
| V18_5-18 | Runtime Node | Node not required to serve release UI |
| V18_5-19 | Local Bind | loopback default |
| V18_5-20 | Public Bind | no default public path |
| V18_5-21 | Secret | no body/render/API exposure |
| V18_5-22 | Identity | no unnecessary value persistence |
| V18_5-23 | Provenance | authority/freshness/UNKNOWN preserved |
| V18_5-24 | Adapter Regression | Cursor/Codex/Generic pass |
| V18_5-25 | Trace | continuity preserved |
| V18_5-26 | Git | no current-project mutation |
| V18_5-27 | Pilot `.banyan` | fingerprint unchanged |
| V18_5-28 | Runtime Core | no unauthorized full rewrite |
| V18_5-29 | Stage19 Handoff | RC evidence complete |
| V18_5-30 | Stop | Stage19 not started |

Hard Metrics:

```text
FEATURE_LOST_WITHOUT_TYPED_DISPOSITION = 0
CONTROL_PLANE_CONTRACT_BREAK_WITHOUT_ADAPTER = 0
SECOND_PERMISSION_ENGINE_CREATED = 0
GIN_HANDLER_POLICY_REIMPLEMENTATION = 0
UI_AUTHORIZATION_BYPASS_PATH = 0
CURRENT_PROJECT_GIT_MUTATION = 0
PILOT_DOT_BANYAN_MUTATION = 0
SECRET_BODY_RENDER_OR_API_PATH = 0
PUBLIC_BIND_DEFAULT_PATH = 0
RELEASE_REQUIRES_NODE_TO_SERVE_UI = 0
EMBEDDED_ASSET_WITHOUT_HASH_MANIFEST = 0
ADAPTER_COMPATIBILITY_REGRESSION = 0
```

Rollback：

```text
Frontend migration and Go/Gin implementation remain isolated in framework source changes.
If equivalence / bridge / adapter validation fails, restore previous Stage18-valid Control Plane implementation and leave Stage19 blocked.
Do not touch Pilot .banyan or project docs during rollback.
```

# WebUI and Control Plane Guide

The WebUI uses Ant Design Pro Simple, TypeScript, Ant Design and ProComponents. The production build is embedded in the Go/Gin host. Gin defaults to `127.0.0.1`, applies body and time limits, recovers panics, keeps `/api/**` and `/events/**` out of SPA fallback, and invokes one `LOCAL_STDIO` bridge.

The 12 accepted feature surfaces are Dashboard, Runtime / Policy, Project Safety, Gate / Blockers, Preflight, Commit Plan, Dry-run Result, Trace / Audit, Provenance, Provider Bindings, Stage / Run and Activation Readiness.

The corresponding API surfaces are status, policy, project safety, preflight, commit plan, commit dry-run, trace, provenance, providers, stages and activation readiness. `/api/adapters/:kind` carries Cursor, Codex and Generic Editor requests through the same bridge.

The UI renders typed Runtime results and blockers. A click, form submission or displayed success message is never authorization. Commit plans are proposals, dry-run results are not commits, and activation readiness does not activate a Project Instance.

Static assets are immutable at runtime and verified through SHA-256 manifests. Deep links return the SPA; unknown API routes return JSON 404 rather than `index.html`.

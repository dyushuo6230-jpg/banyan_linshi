# Banyan Final Architecture Guide

## Components

`banyan-framework/` is reusable framework software. `.banyan/` is one project's Project Instance. `.banyan-refactor/` is the temporary first-construction workspace and is not part of the normal runtime or future upgrade path.

The accepted runtime flow is:

```text
Editor / Ant Design Pro Simple WebUI
→ Cursor, Codex, Generic Adapter / Go Gin transport
→ LOCAL_STDIO Runtime Bridge
→ Python Banyan Runtime Core
→ Permission Policy / Git Safety / Trace / Index / Providers
```

The WebUI production assets are compiled at build time and embedded into the Go host with `go:embed`. Go serves HTTP and static assets; it is not the Banyan Runtime Core. The Python Runtime remains the sole policy and domain-decision implementation.

## Authority boundaries

Editors and the WebUI submit intent. Adapters translate request shapes. Gin validates transport DTOs and maps typed responses. None of these layers grants authorization, selects a freshness winner, changes canonical truth, or performs direct Git mutation. Runtime decisions depend on explicit authority, version/status, freshness, evidence, authorization and safety preconditions.

Evidence, profiles, Git identity, UI confirmation, trace records and commit plans are inputs; none is authorization by itself. Unknown or conflicting authority remains typed and visible.

## State separation

Canonical project sources remain authoritative unless an explicit governed transition says otherwise. Generated views, caches, indexes and runtime status are derived. The current `.banyan/` is a validated Pilot/Shadow Project Instance and is not final activation.

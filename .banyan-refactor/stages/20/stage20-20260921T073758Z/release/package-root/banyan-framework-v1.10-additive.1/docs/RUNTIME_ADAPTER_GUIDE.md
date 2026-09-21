# Runtime and Adapter Guide

The Runtime Core is Python. `banyan.runtime.api.RuntimeAPI` owns policy evaluation, preflight, project inspection, semantic commit planning/execution gates, audit trace and provider-binding access. The compiler is strict: unknown fields, missing hard blocks, enum drift and weakened safety rules fail closed.

Semantic Commit separates planning from authorization. Execution requires explicit paths or hunks, identity presence, matching authorization, Secret checks, exact staged-set verification and trace capture. Blind `git add .`/`git add -A`, network Git operations, Secret-risk staging and global identity writes are blocked.

The Go `ProcessBridge` sends typed JSON over local stdin/stdout to `python3 -m banyan.control_plane.bridge`. It uses an argument vector without shell interpolation, a request deadline and typed fail-closed errors. It does not contain a fallback Runtime or Permission engine.

Cursor, Codex and Generic Editor adapters normalize editor-native request fields into one `AdapterRequest` and return one `AdapterResponse`. Adapters own no policy, canonical truth, identity changes, Secret access or direct Git mutation. Their verified path is Adapter → Gin → Runtime Bridge → Control Plane Service → Runtime → Permission → Trace.

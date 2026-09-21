# Operations and Troubleshooting Guide

Start with `/api/status`, `/api/policy` and `/api/project-safety`. Confirm the process listens on `127.0.0.1`, the Python environment can import `banyan`, the policy path exists and the trace path is writable.

- `RUNTIME_BRIDGE_FAILURE`: verify `PYTHONPATH`, Python/PyYAML installation, repository/policy arguments and the ten-second bridge deadline. Do not add fallback policy logic to Gin.
- `INVALID_REQUEST`: compare the request DTO with the route/adapter contract; do not coerce unknown fields into accepted values.
- `BLOCK` or `NEEDS_INPUT`: inspect reason codes, missing authorization, identity presence, freshness, Secret risk and rollback state. Do not bypass the Runtime.
- UI deep link failure: confirm embedded `index.html` and asset hashes; API paths must still return JSON.
- Asset mismatch: rebuild with `npm ci && npm run build`, regenerate the manifest and rebuild Go; do not edit `dist` manually.
- Trace failure: stop mutating workflows, preserve the invalid trace, repair the evidence pipeline and rerun validation.
- Pilot mismatch: stop, compare the 13-file manifest and use the Pilot rollback plan. Never regenerate the instance silently.

Back up evidence before any recovery. RC acceptance, UI availability and a healthy Runtime do not authorize Final Activation.

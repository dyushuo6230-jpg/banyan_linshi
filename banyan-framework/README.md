# Banyan Framework

Generic, editor-neutral policy compilation, runtime permission evaluation, adapters, audit tracing, and semantic commit execution.

The runtime is fail-closed. Current-project execution defaults to dry-run. Mutating Git execution is accepted only for repositories inside an explicitly configured isolated fixture root.

The Stage 16 Control Plane exposes that runtime through a loopback-only HTTP API and local WebUI. It has no current-project mutation, canonical apply, public bind, Secret body rendering, or activation endpoint. Start it with `banyan-control-plane --repository PATH --policy POLICY.yaml`; the default address is `127.0.0.1:8765`.

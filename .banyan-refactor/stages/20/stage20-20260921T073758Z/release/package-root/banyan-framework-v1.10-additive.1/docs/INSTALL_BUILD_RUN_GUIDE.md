# Install, Build and Run Guide

## Prerequisite profiles

A prebuilt web host can serve its embedded UI without Node. Runtime-connected operation still requires Python 3.9 or newer, PyYAML, the Banyan Python sources and a project policy. Developer builds additionally require Go 1.24 or newer and Node/npm compatible with the lockfile.

There is no separate viewer-only server mode in this release. The Go host requires `--repository` and `--policy`; API calls invoke the Python Runtime through `LOCAL_STDIO`.

## Install the Python Runtime

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e <release-root>/banyan-framework
```

## Reproducible developer build

```sh
cd <release-root>/banyan-framework/frontend
npm ci
npm run build
npm audit --audit-level=high

cd ../control-plane-go
go test ./...
go build -trimpath -buildvcs=false -o bin/banyan-control ./cmd/banyan-control
```

The frontend build writes immutable assets and `asset-manifest.json` into `control-plane-go/internal/webassets/dist`. `go build` embeds those files. Node is a build-time dependency and is not used to serve the release UI.

## Run locally

```sh
export PYTHONPATH=<release-root>/banyan-framework/src
<release-root>/bin/banyan-control   --repository <project-root>   --policy <release-root>/banyan-framework/policies/default-policy.yaml   --trace <local-state-root>/banyan-trace.jsonl   --host 127.0.0.1   --port 8765
```

Open `http://127.0.0.1:8765/`. Public bind addresses are rejected. Use a writable, non-secret local trace path. The current project remains read-only/preflight/plan/dry-run unless Runtime authorization explicitly permits a different scope.

## Verify

Check `/api/status`, then `/api/policy` and `/api/project-safety`. A healthy status does not authorize activation or Git mutation.

# Stage 18.5 Acceptance Report

## Status

`PASS_STAGE18_5_ANT_DESIGN_PRO_GOGIN_ARCHITECTURE_MIGRATION`

Run: `stage18_5-20260921T064132Z`. Stage 19 was not started or authorized.

## Stage18 Seal

Stage 18 acceptance, adapter validation, validation results, and Pilot integrity were consumed through the Stage 18.5 low-token index. The entry gate was `PASS_FOR_STAGE18_5_WEBUI_GOGIN_ARCHITECTURE_MIGRATION_WITH_PRESERVED_RUNTIME_CONTRACTS`.

## Current Implementation Inventory

The targeted inventory is recorded in `CURRENT_IMPLEMENTATION_INVENTORY.yaml`. The previous UI was vanilla HTML/JS, the previous HTTP transport was Python, and the preserved Runtime remains `banyan.runtime.api.RuntimeAPI` in Python. No repository-wide rediscovery or Legacy scan was performed.

## Architecture ADR

The accepted stack is Ant Design Pro Simple with TypeScript, Ant Design and ProComponents; Go/Gin is the loopback-only transport. A single typed `LOCAL_STDIO` bridge invokes the existing Stage 15 Runtime. Gin contains no Permission, Authorization, Git Safety, freshness-winner, or Secret policy implementation.

## Ant Design Pro Simple Baseline

The frontend retains ProLayout, routing, theme, required ProComponents, typed API access, and the Banyan feature surfaces. Demo pages, mock business services, sample account/permission models, and example business semantics are absent. The locked dependency tree reports zero known npm vulnerabilities at acceptance.

## Feature Equivalence

All 12 Stage 16 surfaces are dispositioned `EQUIVALENT`: Dashboard, Runtime / Policy, Project Safety, Gate / Blockers, Preflight, Commit Plan, Dry-run Result, Trace / Audit, Provenance, Provider Bindings, Stage / Run, and Activation Readiness. Silent loss count is zero.

## Go/Gin Control Plane

The Go server validates DTOs, applies request/body/time limits, invokes the Runtime Bridge, maps typed results, serves embedded assets, and provides SPA fallback. `/api/**` and `/events/**` never fall through to the SPA. Default bind is `127.0.0.1`; public bind defaults are rejected.

## Runtime Bridge

`Go ProcessBridge -> python3 -m banyan.control_plane.bridge -> ControlPlaneService -> RuntimeAPI` is the only Runtime path. Failure is typed and fail-closed. No fallback policy engine or Runtime Core rewrite was introduced.

## Embedded Frontend Distribution

The TypeScript production build produced three immutable files with SHA-256 entries. `go:embed` includes them in `banyan-control`; the release binary served the UI, deep links, and API without a Node server.

## Local-only / Security

Loopback-only binding, body/header/read/write/idle timeouts, Gin recovery, typed bridge errors, and argument-vector child process invocation were verified. Secret bodies are neither returned nor rendered. Identity values are not persisted. The UI grants no authorization.

## API / UI Tests

Frontend production build, zero-vulnerability npm audit, Go tests, route compatibility, SPA deep links, API 404 separation, asset hashes, embedded release serving, Runtime bridge success/failure, and local bind rules passed.

## Adapter Regression

Cursor, Codex, and Generic Editor requests traversed Gin, the single Runtime Bridge, Control Plane Service, Runtime API, Permission Policy, and Evidence Trace. A `git_mutation` request was blocked for all three; evidence refs were preserved and no action executed.

## Trace / Provenance Regression

Trace continuity, non-authorizing trace semantics, typed failure, evidence refs, and visible `UNKNOWN` authority/freshness passed. No UNKNOWN value was synthesized.

## Current Project Git Integrity

HEAD and `.git/index` hashes match Precheck. Staged and unstaged tracked counts remain zero. Git mutation count is zero.

## Pilot `.banyan` Integrity

The 13 Stage 17 Pilot files match the Precheck hashes. No file was added, removed, migrated, regenerated, restructured, or selected as a new truth source.

## CON-002 Carry-over

`CON-002 = TYPED_BLOCKED_HUMAN_PROJECT_AUTHORITY`. Final activation remains `NOT_AUTHORIZED`.

## V18_5-01..V18_5-30

All 30 validations passed. The machine-readable result is `evidence/STAGE18_5_COVERAGE_REPORT.yaml`.

## Hard Metrics

All 12 Hard Metrics are zero, including feature loss, second permission engine, Gin policy reimplementation, UI authorization bypass, Git/Pilot mutation, Secret exposure, public bind default, Node runtime serving, unhashed assets, and adapter regression.

## Actual Writes

Writes are limited to `banyan-framework/**`, this Stage 18.5 run directory, and the two bootstrap registers. Project business code, Canonical documents, and `.banyan/` were not modified.

## Bootstrap

The migration register and requirement trace record Stage 18.5 as completed with Runtime/Permission/Adapter contracts preserved.

## Stage19 RC Handoff

`STAGE19_RC_HANDOFF.yaml` and `evidence/NEXT_STAGE_HANDOFF.yaml` contain the RC evidence set. Stage 19 execution is explicitly false.

## Stage19 Entry Gate

`READY_FOR_INDEPENDENT_RC_REVIEW_WITH_BLOCKERS`; execution is not authorized. Stage 18.5 stops here.

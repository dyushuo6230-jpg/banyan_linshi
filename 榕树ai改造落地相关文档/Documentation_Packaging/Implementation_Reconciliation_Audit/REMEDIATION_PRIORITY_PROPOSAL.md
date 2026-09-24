# Remediation Priority Proposal

This is a proposal only. D1.5 did not authorize or perform any remediation.

## P0 — Preserve semantics and make the release self-explaining

### P0-1 Package durable authoritative definitions

- Gap: `IR-AUDIT-GAP-001`.
- Desired result: a released Framework can locate its Capability Contract Registry, Artifact/Source Role registries, workflow/state rules, Provider Port and Project Overlay schemas, compatibility mappings, and version/status/provenance rules without a temporary construction tree.
- Acceptance evidence: release manifest entries, stable hashes, schema validation, and a clean-room lookup test using only the release plus an explicitly separate Project Instance.
- Guard: choose packaging and authority semantics through governance; do not bulk-copy construction output into Core.

### P0-2 Close the v3.1 artifact migration chain

- Gap: `IR-AUDIT-GAP-002`.
- Desired result: every ROLE, POLICY, SKILL, WORKFLOW, STATE, TEMPLATE, DECISION, CONTEXT, and COMPATIBILITY category has a durable disposition with registry entry, loader/consumer, runtime or explicit non-runtime status, tests, and supersession proof where applicable.
- Acceptance evidence: an implementation-aware migration matrix with no category depending only on preserve-in-place evidence.
- Guard: retain Legacy authority and references until verified migration or evidence-backed supersession.

## P1 — Enable the primary developer journey

### P1-1 Implement the governed orchestration spine

- Gaps: `IR-AUDIT-GAP-003`, `DOC-GAP-CANDIDATE-002`, `DOC-GAP-CANDIDATE-003`, `DOC-GAP-CANDIDATE-005`.
- Desired result: natural-language intake can select an Adaptive Workflow, request informed decisions, create a controlled Change, apply approved canonical changes, run validation, and report evidence.
- Acceptance evidence: end-to-end tests across Cursor, Codex, and Generic Editor using the same Runtime policy and typed state transitions.
- Required safety: planning must remain distinct from authorization; apply must be scoped, reversible, traced, and blocked on unknown authority/freshness.

### P1-2 Define and bind collaboration roles

- Gap: `IR-AUDIT-GAP-007`.
- Desired result: stable role enum and Project Instance bindings for Implementation Owner, Draft Contributor, Reviewer, and Project Authority.
- Acceptance evidence: schema validation, authority resolution tests, missing/ambiguous binding failures, and no implicit privilege escalation.

### P1-3 Complete Project Instance binding

- Gap: `IR-AUDIT-GAP-004`.
- Desired result: `.banyan` can stably reference released Core contracts, Source Roles, Workflows, Skills/Providers, Policies, Profiles, Roles, Runtime state, Index, Trace, and Migration without embedding project secrets or replacing canonical truth.
- Acceptance evidence: validation against the self-contained release and a separately governed Final Activation decision.
- Blocker retained: `CON-002` requires Human Project Authority.

## P2 — Add governance and intelligence runtimes

### P2-1 Promote the shadow index into a supported runtime boundary

- Gap: `IR-AUDIT-GAP-005`.
- Desired result: rebuildable SQLite/index/query service with stable IDs, freshness, provenance, reference integrity, and explicit non-canonical authority.
- Acceptance evidence: deterministic rebuild, stale/unknown handling, bounded query tests, and Project Instance binding.

### P2-2 Implement context, memory, freshness, and compaction

- Gap: `IR-AUDIT-GAP-005`.
- Desired result: recoverable context that preserves decisions, blockers, safety constraints, authority, provenance, and unknowns under token budgets.
- Acceptance evidence: recovery and compaction tests proving that mandatory context and uncertainty survive.

### P2-3 Implement evidence, impact, event, and learning services

- Gap: `IR-AUDIT-GAP-005`.
- Desired result: evidence bundles, typed impact graphs, event classification, and proposal-only learning with explicit approval before policy/prompt changes.
- Acceptance evidence: provenance and causal-safety tests; learning remains `auto_apply=false` unless separately governed.

### P2-4 Bind Design Intelligence providers

- Gap: `IR-AUDIT-GAP-006`.
- Desired result: Stage 09 ports have validated provider adapters and Runtime consumers for the nine Design capabilities.
- Acceptance evidence: provider conformance, provenance/confidence preservation, failure isolation, and no direct promotion of visual evidence to canonical UI truth.

### P2-5 Implement Project Guide publishing

- Gap: `IR-AUDIT-GAP-005`.
- Desired result: governed one-way projections with source links, freshness, conflict accounting, audience views, and rebuildability rules.
- Acceptance evidence: publisher tests and a rule that generated knowledge cannot silently become canonical authority.

## P3 — Complete user-facing guidance and acceptance

### P3-1 Add WebUI Help Center

- Gap: `IR-AUDIT-GAP-008`.
- Desired result: `/help` explains current actions and limitations from accepted Source of Truth data.
- Acceptance evidence: route/API/UI tests and no claims beyond implemented capabilities.

### P3-2 Resolve D2 acceptance state after implementation decisions

- Gap: `IR-AUDIT-GAP-009`.
- Desired result: review the existing 16 User Guide files against the post-audit implementation baseline, correct any overclaims, and produce the formal D2 acceptance report.
- Acceptance evidence: link validation, fact checks, explicit gap preservation, and accepted navigation.
- Guard: D1.5 does not perform this work.

## P4 — Optional improvements

- Generate machine-readable coverage dashboards from the accepted implementation matrix.
- Add release conformance checks that reject documentation references to temporary construction paths.
- Add per-capability maturity metadata separating contract, artifact, provider, overlay, runtime, test, and documentation layers.

## Proposed sequence

1. Decide the durable authority/package model for frozen definitions.
2. Make the Framework self-contained and re-run no-loss reconciliation.
3. Define roles and complete Project Instance bindings.
4. Implement the orchestration spine.
5. Add index/context/evidence/design/publishing runtimes in independently reviewable increments.
6. Refresh and formally accept D2 documentation.
7. Consider Final Activation only through its separate governed gate.

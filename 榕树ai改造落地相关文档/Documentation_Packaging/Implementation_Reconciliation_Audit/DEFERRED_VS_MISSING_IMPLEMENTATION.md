# Deferred vs Missing Implementation

## Classification rule

- `ACCEPTED_DESIGN_ONLY`: the owning Stage explicitly accepted a contract or design and did not claim a Framework runtime.
- `INTENTIONALLY_DEFERRED`: evidence explicitly assigns implementation to a later step or keeps it inactive by design.
- `REQUIRED_FOR_TARGET_UX`: absent from the current release and needed for the intended primary developer journey.
- `MISSING_IMPLEMENTATION`: expected current surface has no implementation and is not merely a design-stage deliverable.
- `IMPLEMENTED`: a current Framework execution path and relevant tests exist.

These labels describe the current release consequence while preserving the acceptance scope of each Stage.

## Findings

### SQLite Index / Query runtime — `INTENTIONALLY_DEFERRED`

Stage 11 built and validated a shadow, rebuildable SQLite index and query model, explicitly `NOT_FINAL_RUNTIME_DB`. `.banyan/index/manifest.yaml` is only a Pilot file allowlist. No SQLite database, query service, or Runtime API method ships in `banyan-framework/`.

### Context selection / recovery — `ACCEPTED_DESIGN_ONLY`

Stage 12 froze layered selection and recovery contracts. No Framework selector, recovery service, Runtime method, or test implements them.

### Memory layers — `ACCEPTED_DESIGN_ONLY`

Stage 12 defines non-canonical memory with provenance, freshness, coverage, and confidence. No Framework memory store or retrieval consumer exists.

### Freshness resolver — `ACCEPTED_DESIGN_ONLY`

Freshness is a documented/provenance field and a frozen Stage 12 contract. The current Runtime does not calculate or resolve freshness.

### Token budget / compaction — `ACCEPTED_DESIGN_ONLY`

Stage 12 froze budget and compaction behavior. No budget manager, compactor, cache reuse service, or Runtime endpoint exists.

### Evidence bundle runtime — `ACCEPTED_DESIGN_ONLY`

Stage 13 froze evidence semantics. Current trace events are narrower: they validate append-only audit records and cannot assemble governed evidence bundles.

### Impact graph/runtime — `ACCEPTED_DESIGN_ONLY`

Stage 13 distinguishes direct, transitive, potential, unknown, and excluded impact. No graph builder, evaluator, query surface, or tests ship in the Framework.

### Event runtime — `ACCEPTED_DESIGN_ONLY`

Stage 13 defines observed, derived, and correlated events. Current trace events do not implement the full event model or causal constraints.

### Prompt learning runtime — `INTENTIONALLY_DEFERRED`

Stage 13 evaluated proposals offline with `auto_apply=false` and changed no Prompt, Rule, Skill, Core policy, or Runtime. No learning executor exists.

### Project Guide publisher — `ACCEPTED_DESIGN_ONLY`

Stage 10 froze knowledge publishing contracts and explicitly executed no publisher or index runtime. The current User Guide files are authored documentation, not output from a governed Project Guide publisher.

### UI Design Intelligence provider execution — `MISSING_IMPLEMENTATION`

Stage 09 appropriately accepted contract design only, but the present Framework still lacks the AnyDesign/Figma adapter, provider binding, visual runtime, and Design package execution path. Legacy AnyDesign scripts remain outside the Framework.

### Adaptive Workflow router/executor — `REQUIRED_FOR_TARGET_UX`

Stage 05 froze `banyan.workflow.adaptive.v1`; its result stopped at `READY_FOR_EXECUTOR_OR_BLOCKED`. No current Runtime router or executor consumes task, risk, project state, and authorization to advance a workflow.

### Natural-language orchestration — `REQUIRED_FOR_TARGET_UX`

Current editor adapters accept typed operations such as `preflight`, `commit_plan`, and `trace`. They do not turn an ordinary developer request into a complete governed workflow. This is necessary for the intended “describe work and let Banyan guide it” experience.

### Change / Canonical Apply executor — `REQUIRED_FOR_TARGET_UX`

Stage 06 intentionally designed contracts without provider implementation. The present release has no Change workspace or Canonical Apply API; `.banyan/overlays/bindings.yaml` keeps canonical apply disabled.

### Collaboration role schema — `REQUIRED_FOR_TARGET_UX`

Role names exist in documentation, but there is no Runtime enum/binding schema for Implementation Owner, Draft Contributor, Reviewer, and Project Authority. Reliable routing, approvals, and responsibility resolution need this binding.

### WebUI Help Center — `MISSING_IMPLEMENTATION`

The accepted WebUI has 12 routes and no `/help`. D0 and D1 already record this as `DOC-GAP-CANDIDATE-001`.

## Current implemented reference points

The audited deferred/missing list contains no fully implemented item. Related foundations are implemented: permission preflight, Git inspection, semantic commit planning and bounded execution, trace emission/query, provider-binding loading, editor adapters, Control Plane, and the 12 current WebUI views. Those foundations do not by themselves implement the capabilities above.

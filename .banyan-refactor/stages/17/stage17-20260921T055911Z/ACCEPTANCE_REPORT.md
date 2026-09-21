# Stage 17 Acceptance Report

## Status

`PASS_STAGE17_CURSOR_PROJECT_INSTANCE_PILOT`

## Scope and Sequence

Stage 17 consumed the existing Stage 16 handoff, Activation Readiness, Control Plane contract, Stage 15 Runtime policy, Stage 14 permission contracts, and Stage 04 Project Instance schema. It did not rescan the full project or repeat Stage 01–16 analysis.

The required order was preserved: Runtime Preflight → Checkpoint → Shadow Instance → Cursor Adapter Validation → Pilot `.banyan/` Creation → Validation → Activation Review.

## Cursor Adapter and Runtime Chain

Implemented `CursorPilotAdapter` as an adapter only. It owns no policy, permission, canonical truth, project write, or Git mutation capability. The verified chain is Cursor Adapter → Control Plane → Runtime API → Permission Policy → Evidence Trace.

Runtime preflight returned `ALLOW`, L3, `executed=false`, while preserving `CURRENT_PROJECT_DRY_RUN_ONLY`. The actual Pilot scope was independently bound to the explicit Stage 17 Gate and `USER-STAGE17-PILOT-REQUEST`; a UI click, trace, profile, Git identity, or commit plan was not treated as authorization.

## `.banyan/` Creation and Pilot Result

`.banyan/` was created for the first time. It contains 13 allowlisted Pilot/Shadow files across instance, mapping, overlay, profile, provider, runtime, trace, index, generated, and migration/rollback surfaces. The installed files match the validated Shadow byte-for-byte by SHA-256.

The Pilot succeeded and is active only as `PROJECT_INSTANCE_SHADOW_PILOT`. It is not final activation, does not represent completed migration, does not replace canonical truth, and does not replace the existing project directory.

## Existing Project, Secret, Identity, and Unknown Safety

Existing Project Layout remains `PRESERVE_IN_PLACE`. `docs/` metadata is unchanged, `project/` remains absent, no Legacy file was deleted, and no business or canonical file was overwritten. No Secret body was read or copied. Git identity values were neither persisted nor modified. `CON-002` remains `TYPED_BLOCKED_HUMAN_PROJECT_AUTHORITY`; UNKNOWN authority, freshness, and variable states remain explicit.

## Git Safety and Rollback

HEAD remains `9a52349e6bcb6ee44e3039dd87ede56e3e0a3ec7`, index SHA-256 remains `3d09518893a2614bcec619c71dcd2d7a8f1242ee90adb66f144683ee8c397862`, and staged, unstaged, and conflict counts remain zero. No Git mutation occurred.

Rollback is ready. A 13-file rollback was successfully simulated on a control-root replica. The actual plan removes only manifest-matched Pilot files and empty Pilot directories, then verifies `.banyan/` absence and the checkpoint Git fingerprints. No Git reset, Legacy restore, or docs restore is required.

## Validation and Stop Gate

All 10 automated Stage 17 tests passed. V17-01 through V17-28 passed. `ACTIVATION_RESULT.yaml` and `NEXT_STAGE_HANDOFF.yaml` are complete. Stage 18 was not started and is not authorized.

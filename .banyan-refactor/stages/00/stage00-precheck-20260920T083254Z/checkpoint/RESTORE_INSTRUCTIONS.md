# Stage 00 restore instructions

Purpose: recover baseline non-secret project state. Owner: Stage 00. This file authorizes no restore.

1. Stop dependent stages and compare then-current Git HEAD/index/status and file hashes against this baseline. Preserve newer user work first.
2. Baseline HEAD is recorded in BASELINE_MANIFEST.yaml. Original index/working tree have no tracked changes; no staged/unstaged patches are necessary. Use minimal path-specific Git recovery only after an approved restore plan; never reset/clean the whole repository.
3. Verify checkpoint archive hashes using CHECKPOINT_RECORD.yaml. Inspect members before extracting selected non-secret paths. Relative paths are repository-relative. Never overwrite newer files blindly.
4. Restore untracked.tar and ignored-governed.tar selectively when required. The untracked archive also preserves user-supplied construction documents; it does not designate them as historical development state.
5. The 13 USER_ACCEPTED_PRESERVE_IN_PLACE environment configs have NO Banyan content backup. Never read, hash, copy, edit, delete, move, rename or stage them. Losing these files cannot be repaired from this checkpoint. The user explicitly accepts this risk. Other potential secrets are not covered by this waiver.
6. Re-validate hashes, index/status and metadata-only protection after any permitted restore. This Stage only verified archive integrity; it did not restore real files.
7. To undo Stage 00 itself, first preserve evidence and request an archival/cleanup decision scoped solely to .banyan-refactor. Do not touch original project files. No automatic cleanup is authorized.

# Governance and Security Guide

Runtime permission results are `ALLOW`, `BLOCK`, `NEEDS_INPUT` or `NOT_APPLICABLE`. `ALLOW` is meaningful only for the exact action, target, actor, constraints and validity bound by an authorization record. Evidence, impact analysis, plans, profiles, editor names, AI roles, Git identity and traces do not independently authorize action.

Protected writes require authority, freshness, impact review, matching authorization, a prior checkpoint, actionable rollback and Secret checks. Missing or conflicting preconditions fail closed.

Git identity is checked for name/email presence when a commit is eligible. Values are not persisted in evidence, identity grants no permission role, and Banyan does not modify identity, invent authors or use author overrides.

Secret records are metadata-only: path, classification, existence and restriction flags. Body read, hash, copy, summary, learning use, stage, commit, move and deletion require separate explicit authorization; this release grants none.

The Go host is loopback-only by default. Gin transports typed requests but owns no Permission, Authorization, Git Safety, freshness-winner or Secret policy. The current project remains dry-run-only, `CON-002` remains blocked, and Final Activation remains unauthorized.

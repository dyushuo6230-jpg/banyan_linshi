PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS entities (
  stable_id TEXT PRIMARY KEY,
  entity_type TEXT NOT NULL,
  classification TEXT NOT NULL,
  source_role TEXT,
  authority TEXT,
  current_locator TEXT,
  locator_kind TEXT,
  version TEXT,
  status TEXT,
  freshness TEXT,
  rebuildability TEXT,
  provenance_state TEXT,
  source_stage TEXT,
  source_run_id TEXT
);

CREATE TABLE IF NOT EXISTS reference_edges (
  reference_id TEXT PRIMARY KEY,
  source_id TEXT NOT NULL,
  target_id TEXT,
  relationship TEXT NOT NULL,
  reference_status TEXT NOT NULL,
  source_locator TEXT,
  target_locator TEXT,
  migration_strategy TEXT,
  evidence_ref TEXT
);

CREATE TABLE IF NOT EXISTS trace_events (
  event_id TEXT PRIMARY KEY,
  event_type TEXT NOT NULL,
  subject_id TEXT,
  stage TEXT,
  run_id TEXT,
  occurred_at TEXT,
  actor_identity TEXT,
  status TEXT,
  result TEXT,
  lineage_json TEXT NOT NULL,
  evidence_json TEXT
);

CREATE TABLE IF NOT EXISTS history_events (
  history_id TEXT PRIMARY KEY,
  subject_id TEXT NOT NULL,
  event_type TEXT NOT NULL,
  from_state TEXT,
  to_state TEXT,
  occurred_at TEXT,
  source_ref TEXT,
  evidence_ref TEXT
);

CREATE TABLE IF NOT EXISTS relations (
  relation_id TEXT PRIMARY KEY,
  relation_type TEXT NOT NULL,
  source_id TEXT NOT NULL,
  target_id TEXT,
  status TEXT,
  evidence_ref TEXT
);

CREATE TABLE IF NOT EXISTS unresolved_references (
  reference_id TEXT PRIMARY KEY,
  source_id TEXT NOT NULL,
  relationship TEXT NOT NULL,
  missing_target_locator TEXT,
  status TEXT NOT NULL DEFAULT 'UNRESOLVED_REFERENCE',
  owner_stage TEXT,
  evidence_ref TEXT
);

CREATE TABLE IF NOT EXISTS migration_ledger (
  ledger_id TEXT PRIMARY KEY,
  source_ref TEXT NOT NULL,
  source_hash TEXT,
  imported_count INTEGER,
  import_status TEXT NOT NULL,
  imported_at TEXT,
  notes TEXT
);

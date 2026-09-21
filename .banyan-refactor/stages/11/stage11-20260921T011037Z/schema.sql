PRAGMA foreign_keys = ON;
PRAGMA journal_mode = DELETE;
PRAGMA synchronous = FULL;

CREATE TABLE index_metadata (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE entities (
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
  provenance_state TEXT NOT NULL,
  source_stage TEXT,
  source_run_id TEXT
);

CREATE TABLE artifacts (
  stable_id TEXT PRIMARY KEY REFERENCES entities(stable_id),
  artifact_type TEXT NOT NULL,
  canonicality TEXT,
  approval_status TEXT,
  source_locator TEXT NOT NULL,
  content_indexed INTEGER NOT NULL DEFAULT 0 CHECK(content_indexed = 0)
);

CREATE TABLE source_roles (
  role_id TEXT PRIMARY KEY,
  authority_rule TEXT NOT NULL,
  freshness_rule TEXT NOT NULL,
  conflict_rule TEXT NOT NULL
);

CREATE TABLE artifact_versions (
  version_id TEXT PRIMARY KEY,
  artifact_id TEXT NOT NULL REFERENCES entities(stable_id),
  version TEXT NOT NULL,
  source_ref TEXT NOT NULL,
  provenance_state TEXT NOT NULL
);

CREATE TABLE artifact_status_history (
  status_event_id TEXT PRIMARY KEY,
  artifact_id TEXT NOT NULL REFERENCES entities(stable_id),
  status TEXT NOT NULL,
  observed_at TEXT NOT NULL,
  source_ref TEXT NOT NULL
);

CREATE TABLE reference_edges (
  reference_id TEXT PRIMARY KEY,
  source_id TEXT NOT NULL REFERENCES entities(stable_id),
  target_id TEXT REFERENCES entities(stable_id),
  relationship TEXT NOT NULL,
  reference_status TEXT NOT NULL CHECK(reference_status IN ('RESOLVED','UNRESOLVED_REFERENCE','NOT_A_REFERENCE','SUPERSEDED_REFERENCE','HISTORICAL_REFERENCE')),
  source_locator TEXT NOT NULL,
  target_locator TEXT,
  migration_strategy TEXT NOT NULL,
  evidence_ref TEXT NOT NULL
);

CREATE TABLE provenance (
  provenance_id TEXT PRIMARY KEY,
  subject_id TEXT NOT NULL REFERENCES entities(stable_id),
  source_refs_json TEXT NOT NULL,
  source_version TEXT NOT NULL,
  generator_or_tool TEXT NOT NULL,
  observed_at TEXT NOT NULL,
  confidence TEXT NOT NULL,
  provenance_state TEXT NOT NULL
);

CREATE TABLE projections (
  projection_id TEXT PRIMARY KEY REFERENCES entities(stable_id),
  projection_type TEXT NOT NULL,
  audience_json TEXT NOT NULL,
  coverage TEXT NOT NULL,
  freshness TEXT NOT NULL,
  rebuildability TEXT NOT NULL,
  canonical_truth INTEGER NOT NULL DEFAULT 0 CHECK(canonical_truth = 0)
);

CREATE TABLE guides (
  guide_id TEXT PRIMARY KEY REFERENCES entities(stable_id),
  canonical_source_refs_json TEXT NOT NULL,
  freshness TEXT NOT NULL,
  provenance_state TEXT NOT NULL
);

CREATE TABLE changes (
  change_id TEXT PRIMARY KEY REFERENCES entities(stable_id),
  status TEXT NOT NULL,
  evidence_json TEXT NOT NULL
);

CREATE TABLE decisions (
  decision_id TEXT PRIMARY KEY REFERENCES entities(stable_id),
  status TEXT NOT NULL,
  evidence_json TEXT NOT NULL
);

CREATE TABLE progress_records (
  progress_id TEXT PRIMARY KEY REFERENCES entities(stable_id),
  progress_type TEXT NOT NULL CHECK(progress_type IN ('CURRENT_STATUS','HISTORICAL_STATUS','WORK_LOG','DERIVED_SUMMARY')),
  as_of TEXT NOT NULL,
  evidence_refs_json TEXT NOT NULL,
  freshness TEXT NOT NULL
);

CREATE TABLE handover_records (
  handover_id TEXT PRIMARY KEY REFERENCES entities(stable_id),
  current_scope TEXT NOT NULL,
  canonical_refs_json TEXT NOT NULL,
  operational_refs_json TEXT NOT NULL,
  blockers_json TEXT NOT NULL,
  next_actions_json TEXT NOT NULL,
  as_of TEXT NOT NULL,
  freshness TEXT NOT NULL
);

CREATE TABLE provider_bindings (
  binding_id TEXT PRIMARY KEY REFERENCES entities(stable_id),
  port_id TEXT NOT NULL,
  provider_id TEXT NOT NULL,
  activation_state TEXT NOT NULL,
  fallback_policy TEXT NOT NULL,
  health_policy TEXT NOT NULL
);

CREATE TABLE trace_events (
  event_id TEXT PRIMARY KEY,
  event_type TEXT NOT NULL,
  subject_id TEXT NOT NULL,
  stage TEXT NOT NULL,
  run_id TEXT NOT NULL,
  occurred_at TEXT NOT NULL,
  actor_identity TEXT NOT NULL,
  status TEXT NOT NULL,
  result TEXT NOT NULL,
  lineage_json TEXT NOT NULL,
  evidence_json TEXT NOT NULL,
  grants_authorization INTEGER NOT NULL DEFAULT 0 CHECK(grants_authorization = 0)
);

CREATE TABLE history_events (
  history_id TEXT PRIMARY KEY,
  subject_id TEXT NOT NULL,
  event_type TEXT NOT NULL,
  from_state TEXT NOT NULL,
  to_state TEXT NOT NULL,
  occurred_at TEXT NOT NULL,
  source_ref TEXT NOT NULL,
  evidence_ref TEXT NOT NULL
);

CREATE TABLE relations (
  relation_id TEXT PRIMARY KEY,
  relation_type TEXT NOT NULL,
  source_id TEXT NOT NULL REFERENCES entities(stable_id),
  target_id TEXT REFERENCES entities(stable_id),
  status TEXT NOT NULL,
  evidence_ref TEXT NOT NULL
);

CREATE TABLE unresolved_references (
  reference_id TEXT PRIMARY KEY REFERENCES reference_edges(reference_id),
  source_id TEXT NOT NULL REFERENCES entities(stable_id),
  relationship TEXT NOT NULL,
  missing_target_locator TEXT,
  status TEXT NOT NULL CHECK(status = 'UNRESOLVED_REFERENCE'),
  owner_stage TEXT NOT NULL CHECK(owner_stage = '12'),
  evidence_ref TEXT NOT NULL,
  invented_target INTEGER NOT NULL DEFAULT 0 CHECK(invented_target = 0)
);

CREATE TABLE migration_ledger (
  ledger_id TEXT PRIMARY KEY,
  source_ref TEXT NOT NULL,
  source_hash TEXT,
  imported_count INTEGER NOT NULL,
  import_status TEXT NOT NULL,
  imported_at TEXT NOT NULL,
  notes TEXT NOT NULL
);

CREATE TABLE secret_metadata (
  secret_id TEXT PRIMARY KEY,
  path TEXT NOT NULL,
  classification TEXT NOT NULL CHECK(classification = 'SECRET_METADATA_ONLY'),
  restriction_flags TEXT NOT NULL,
  exists_metadata INTEGER NOT NULL,
  body_indexed INTEGER NOT NULL DEFAULT 0 CHECK(body_indexed = 0),
  body_hash_indexed INTEGER NOT NULL DEFAULT 0 CHECK(body_hash_indexed = 0),
  derived_value_indexed INTEGER NOT NULL DEFAULT 0 CHECK(derived_value_indexed = 0)
);

CREATE INDEX idx_entities_locator ON entities(current_locator);
CREATE INDEX idx_entities_role ON entities(source_role, authority);
CREATE INDEX idx_reference_source ON reference_edges(source_id);
CREATE INDEX idx_reference_target ON reference_edges(target_id);
CREATE INDEX idx_history_subject ON history_events(subject_id, occurred_at);
CREATE INDEX idx_trace_stage_run_subject ON trace_events(stage, run_id, subject_id);
CREATE INDEX idx_relation_source_type ON relations(source_id, relation_type);
CREATE INDEX idx_relation_target_type ON relations(target_id, relation_type);
CREATE INDEX idx_progress_type ON progress_records(progress_type, as_of);

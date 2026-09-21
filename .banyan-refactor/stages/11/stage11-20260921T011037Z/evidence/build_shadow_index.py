#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import sys
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[5]
RUN = ROOT / ".banyan-refactor/stages/11/stage11-20260921T011037Z"
SCHEMA = RUN / "schema.sql"
PRIMARY_DB = RUN / "shadow/banyan_index.sqlite"
REBUILD_DB = RUN / "rebuild/banyan_index.rebuilt.sqlite"

S01 = ROOT / ".banyan-refactor/stages/01/stage01-20260920T091426Z"
S03 = ROOT / ".banyan-refactor/stages/03/stage03-20260920T135702Z"
S04 = ROOT / ".banyan-refactor/stages/04/stage04-20260920T142517Z"
S05 = ROOT / ".banyan-refactor/stages/05/stage05-20260920T144623Z"
S06 = ROOT / ".banyan-refactor/stages/06/stage06-20260920T151243Z"
S07 = ROOT / ".banyan-refactor/stages/07/stage07-20260920T152653Z"
S08 = ROOT / ".banyan-refactor/stages/08/stage08-20260920T153936Z"
S09 = ROOT / ".banyan-refactor/stages/09/stage09-20260920T155444Z"
S10 = ROOT / ".banyan-refactor/stages/10/stage10-20260920T161325Z"
SECRET_METADATA = ROOT / ".banyan-refactor/stages/00/stage00-precheck-20260920T083254Z/evidence/SECRET_METADATA.json"

def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))

def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]

def dump_yaml(path: Path, data: Any) -> None:
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")

def stable_locator_id(locator: str) -> str:
    return "LOC-" + hashlib.sha256(locator.encode()).hexdigest()[:16]

def relation_id(kind: str, source: str, target: str | None) -> str:
    raw = f"{kind}|{source}|{target or 'UNKNOWN'}"
    return "REL-" + hashlib.sha256(raw.encode()).hexdigest()[:20]

ASSET_MATRIX = S07 / "LEGACY_ASSET_DISPOSITION_MATRIX.jsonl"
ARTIFACT_MATRIX = S07 / "LEGACY_ARTIFACT_MIGRATION_MATRIX.jsonl"
OP_MATRIX = S07 / "OPERATIONAL_PRESERVATION_MATRIX.jsonl"
CAP_MATRIX = S07 / "LEGACY_CAPABILITY_MIGRATION_MATRIX.yaml"
REF_MAP = S07 / "REFERENCE_MIGRATION_MAP.jsonl"
GEN_SOURCE = S01 / "AI_GENERATED_ARTIFACT_INVENTORY.jsonl"
OP_SOURCE = S01 / "OPERATIONAL_ARTIFACT_INVENTORY.jsonl"
ROLE_REGISTRY = S03 / "SOURCE_ROLE_REGISTRY.yaml"
PROVIDER_BINDINGS = S04 / "PROVIDER_BINDING_SCHEMA.yaml"
TRACE_BOOTSTRAP = ROOT / ".banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml"
MIGRATION_BOOTSTRAP = ROOT / ".banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml"

assets = load_jsonl(ASSET_MATRIX)
artifacts = load_jsonl(ARTIFACT_MATRIX)
operational = load_jsonl(OP_MATRIX)
capabilities = load_yaml(CAP_MATRIX)["mappings"]
references = load_jsonl(REF_MAP)
generated_source = load_jsonl(GEN_SOURCE)
operational_source = load_jsonl(OP_SOURCE)
roles = load_yaml(ROLE_REGISTRY)["roles"]
bindings = load_yaml(PROVIDER_BINDINGS)["bindings"]
trace_bootstrap = load_yaml(TRACE_BOOTSTRAP)
migration_bootstrap = load_yaml(MIGRATION_BOOTSTRAP)
secret_records = [x for x in json.loads(SECRET_METADATA.read_text(encoding="utf-8")) if x.get("recovery_mode") == "USER_ACCEPTED_PRESERVE_IN_PLACE"]
if len(secret_records) != 13:
    raise RuntimeError(f"expected 13 approved secret metadata records, found {len(secret_records)}")

generated_by_id = {x["artifact_id"]: x for x in generated_source}
generated_by_path = {x["path"]: x for x in generated_source}
operational_by_id = {x["artifact_id"]: x for x in operational_source}

source_files: list[tuple[Path, list[str], int, bool]] = [
    (ASSET_MATRIX, ["Artifact", "Locator"], len(assets), True),
    (ARTIFACT_MATRIX, ["Artifact", "Version", "Status", "Projection"], len(artifacts), True),
    (OP_MATRIX, ["Artifact", "Progress", "Handover", "History"], len(operational), True),
    (CAP_MATRIX, ["Capability"], len(capabilities), True),
    (REF_MAP, ["Reference", "UnresolvedReference"], len(references), True),
    (GEN_SOURCE, ["ProjectionSource", "Version", "Status", "Change", "Decision"], len(generated_source), True),
    (OP_SOURCE, ["Progress", "Handover", "History"], len(operational_source), True),
    (ROLE_REGISTRY, ["SourceRole"], len(roles), True),
    (PROVIDER_BINDINGS, ["ProviderBinding"], len(bindings), True),
    (TRACE_BOOTSTRAP, ["TraceEvent", "HistoryEvent"], len(trace_bootstrap.get("requirements", [])), True),
    (MIGRATION_BOOTSTRAP, ["MigrationLedger", "HistoryEvent"], len(migration_bootstrap.get("stages", {})), True),
    (SECRET_METADATA, ["SecretMetadata"], len(secret_records), False),
]

contract_files: list[Path] = []
contract_files += [S05 / x for x in ["WORKFLOW_POLICY_REGISTRY.yaml", "DECISION_POLICY_REGISTRY.yaml", "SEMANTIC_COMMIT_POLICY.yaml"]]
contract_files += sorted(p for p in S06.glob("*.yaml") if p.name != "ARTIFACT_HASHES.sha256")
contract_files += sorted(p for p in S08.glob("*.yaml") if p.name not in {"STAGE08_COVERAGE_REPORT.yaml", "MIGRATION_BLOCKER_CARRYOVER.yaml"})
contract_files += sorted(p for p in S09.glob("*.yaml") if p.name not in {"STAGE09_COVERAGE_REPORT.yaml", "MIGRATION_BLOCKER_CARRYOVER.yaml"})
contract_files += sorted(p for p in S10.glob("*.yaml") if p.name not in {"STAGE10_COVERAGE_REPORT.yaml", "MIGRATION_BLOCKER_CARRYOVER.yaml"})
for path in contract_files:
    source_files.append((path, ["Contract"], 1, True))

def role_authority(role: str | None) -> str:
    mapping = {x["role_id"]: x["authority_rule"] for x in roles}
    return mapping.get(role or "", "NON_CANONICAL_INDEX_CLASSIFICATION")

def asset_role(canonicality: str | None) -> tuple[str, str]:
    return {
        "CANONICAL": ("PROJECT_CANONICAL_DOCUMENT", "PRIMARY"),
        "REFERENCE": ("AUTHORITATIVE_REFERENCE", "REFERENCE_ONLY"),
        "DERIVED": ("DERIVED_PROJECTION", "DERIVED"),
        "OPERATIONAL": ("OPERATIONAL_HISTORY", "EVIDENTIARY_LOW"),
        "LEGACY": ("HISTORICAL", "HISTORICAL_ONLY"),
    }.get(canonicality or "", ("UNKNOWN", "UNKNOWN"))

def logical_snapshot(conn: sqlite3.Connection) -> tuple[str, dict[str, int]]:
    tables = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]
    h = hashlib.sha256()
    counts: dict[str, int] = {}
    for table in tables:
        cols = [r[1] for r in conn.execute(f'PRAGMA table_info("{table}")')]
        order = ",".join(f'"{c}"' for c in cols)
        rows = conn.execute(f'SELECT * FROM "{table}" ORDER BY {order}').fetchall()
        counts[table] = len(rows)
        h.update(json.dumps([table, cols, rows], ensure_ascii=False, separators=(",", ":"), default=str).encode())
    return h.hexdigest(), counts

def build(db_path: Path) -> dict[str, Any]:
    if db_path.exists():
        db_path.unlink()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA.read_text(encoding="utf-8"))
    conn.execute("BEGIN")

    metadata = {
        "INDEX_MODE": "SHADOW",
        "REBUILDABILITY": "REBUILDABLE",
        "CANONICAL_TRUTH": "false",
        "FINAL_RUNTIME_DB": "false",
        "CANONICAL_WRITEBACK": "FORBIDDEN",
        "TRACE_GRANTS_AUTHORIZATION": "false",
        "RUN_ID": "stage11-20260921T011037Z",
    }
    conn.executemany("INSERT INTO index_metadata(key,value) VALUES(?,?)", sorted(metadata.items()))

    seen: dict[str, tuple[Any, ...]] = {}
    def entity(stable_id: str, entity_type: str, classification: str, source_role: str, authority: str, locator: str | None, locator_kind: str, version: str, status: str, freshness: str, rebuildability: str, provenance_state: str, source_stage: str, source_run_id: str) -> None:
        row = (stable_id, entity_type, classification, source_role, authority, locator, locator_kind, version, status, freshness, rebuildability, provenance_state, source_stage, source_run_id)
        if stable_id in seen:
            if seen[stable_id] != row:
                raise RuntimeError(f"INDEX_ID_COLLISION: {stable_id}")
            return
        seen[stable_id] = row
        conn.execute("INSERT INTO entities VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)

    path_to_id: dict[str, str] = {}
    for x in sorted(assets, key=lambda v: v["asset_id"]):
        role, authority = asset_role(x.get("canonicality"))
        entity(x["asset_id"], "Artifact", x.get("canonicality") or "UNKNOWN", role, authority, x["path"], "REPOSITORY_PATH", "UNKNOWN", x.get("legacy_classification_action") or "UNKNOWN", "UNKNOWN", "NOT_PROVEN_REBUILDABLE", "INDEXED_FROM_STAGE07_MATRIX", "07", "stage07-20260920T152653Z")
        conn.execute("INSERT INTO artifacts VALUES(?,?,?,?,?,0)", (x["asset_id"], x.get("asset_type") or "UNKNOWN", x.get("canonicality") or "UNKNOWN", x.get("legacy_classification_action") or "UNKNOWN", x["path"]))
        conn.execute("INSERT INTO provenance VALUES(?,?,?,?,?,?,?,?)", (f"PROV-{x['asset_id']}", x["asset_id"], json.dumps([x["path"]]), "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "INDEXED_FROM_STAGE07_MATRIX"))
        path_to_id.setdefault(x["path"], x["asset_id"])

    for x in sorted(artifacts, key=lambda v: v["artifact_id"]):
        original = generated_by_id[x["artifact_id"]]
        role = x.get("source_role") or "UNKNOWN"
        status = original.get("approval_status") or "UNKNOWN"
        rebuildability = "NOT_PROVEN_REBUILDABLE" if "UNKNOWN" in (x.get("rebuildability") or "") else "HUMAN_MAINTAINED"
        entity(x["artifact_id"], "Artifact", x.get("artifact_class") or "UNKNOWN", role, role_authority(role), x["path"], "REPOSITORY_PATH", "UNKNOWN", status, x.get("freshness") or "UNKNOWN", rebuildability, "INDEXED_FROM_STAGE01_AND_STAGE07", "07", "stage07-20260920T152653Z")
        conn.execute("INSERT INTO artifacts VALUES(?,?,?,?,?,0)", (x["artifact_id"], x.get("artifact_class") or "UNKNOWN", x.get("artifact_class") or "UNKNOWN", status, x["path"]))
        conn.execute("INSERT INTO artifact_versions VALUES(?,?,?,?,?)", (f"VER-{x['artifact_id']}-UNKNOWN", x["artifact_id"], "UNKNOWN", x["path"], "INDEXED_FROM_STRUCTURED_RECORD"))
        conn.execute("INSERT INTO artifact_status_history VALUES(?,?,?,?,?)", (f"STATUS-{x['artifact_id']}-001", x["artifact_id"], status, "UNKNOWN", x["path"]))
        source_refs = original.get("source") or [x["path"]]
        conn.execute("INSERT INTO provenance VALUES(?,?,?,?,?,?,?,?)", (f"PROV-{x['artifact_id']}", x["artifact_id"], json.dumps(source_refs, ensure_ascii=False), "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "INDEXED_FROM_STRUCTURED_RECORD"))
        path_to_id[x["path"]] = x["artifact_id"]

    for x in sorted(operational, key=lambda v: v["artifact_id"]):
        entity(x["artifact_id"], "Artifact", "OPERATIONAL", "OPERATIONAL_HISTORY", "EVIDENTIARY_LOW", x["path"], "REPOSITORY_PATH", "UNKNOWN", "HISTORICAL", x.get("freshness") or "UNKNOWN", "HUMAN_MAINTAINED", "INDEXED_FROM_STAGE07_MATRIX", "07", "stage07-20260920T152653Z")
        conn.execute("INSERT INTO artifacts VALUES(?,?,?,?,?,0)", (x["artifact_id"], x.get("operational_type") or "UNKNOWN", "OPERATIONAL", "HISTORICAL", x["path"]))
        conn.execute("INSERT INTO provenance VALUES(?,?,?,?,?,?,?,?)", (f"PROV-{x['artifact_id']}", x["artifact_id"], json.dumps([x["path"]]), "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "INDEXED_FROM_STAGE07_MATRIX"))
        path_to_id.setdefault(x["path"], x["artifact_id"])

    for x in sorted(capabilities, key=lambda v: v["capability_id"]):
        entity(x["capability_id"], "Capability", "FROZEN_CONTRACT", "AUTHORITATIVE_REFERENCE", "FROZEN_CONTRACT", x.get("target_contract_id"), "CONTRACT_ID", "1.0.0", x["preservation_proof"].get("contract_status") or "UNKNOWN", "UNKNOWN", "HUMAN_MAINTAINED", "INDEXED_FROM_STAGE07_MATRIX", "07", "stage07-20260920T152653Z")

    for x in sorted(roles, key=lambda v: v["role_id"]):
        sid = "ROLE-" + x["role_id"]
        entity(sid, "SourceRole", "SOURCE_ROLE", x["role_id"], x["authority_rule"], rel(ROLE_REGISTRY), "REGISTRY_LOCATOR", "stage03-v1", "FROZEN", "UNKNOWN", "HUMAN_MAINTAINED", "INDEXED_FROM_STAGE03_REGISTRY", "03", "stage03-20260920T135702Z")
        conn.execute("INSERT INTO source_roles VALUES(?,?,?,?)", (x["role_id"], x["authority_rule"], x["freshness_rule"], x["conflict_rule"]))

    for x in sorted(bindings, key=lambda v: v["binding_id"]):
        sid = x["binding_id"]
        entity(sid, "ProviderBinding", "PROVIDER_BINDING", "AUTHORITATIVE_REFERENCE", "CONFIGURATION_INDEX", rel(PROVIDER_BINDINGS), "REGISTRY_LOCATOR", "stage04-v1", x["activation_state"], "UNKNOWN", "REBUILDABLE", "INDEXED_FROM_STAGE04_REGISTRY", "04", "stage04-20260920T142517Z")
        conn.execute("INSERT INTO provider_bindings VALUES(?,?,?,?,?,?)", (sid, x["port_id"], x.get("provider_id") or "UNKNOWN", x["activation_state"], x["fallback_policy"], x["health_policy"]))

    for path in sorted(contract_files):
        data = load_yaml(path) or {}
        stage_match = re.search(r"/stages/(\d{2})/([^/]+)/", str(path))
        stage = stage_match.group(1) if stage_match else "UNKNOWN"
        source_run = stage_match.group(2) if stage_match else "UNKNOWN"
        sid = f"CONTRACT-{stage}-{path.stem}"
        version = str(data.get("schema_version", "UNKNOWN")) if isinstance(data, dict) else "UNKNOWN"
        status = str(data.get("status", data.get("schema_status", data.get("contract_status", "FROZEN")))) if isinstance(data, dict) else "FROZEN"
        entity(sid, "Contract", "CONTRACT", "AUTHORITATIVE_REFERENCE", "FROZEN_CONTRACT", rel(path), "REPOSITORY_PATH", version, status, "UNKNOWN", "HUMAN_MAINTAINED", "INDEXED_FROM_FROZEN_YAML", stage, source_run)

    def locator_entity(locator: str) -> str:
        if locator in path_to_id:
            return path_to_id[locator]
        sid = stable_locator_id(locator)
        entity(sid, "Locator", "REFERENCE_LOCATOR", "AUTHORITATIVE_REFERENCE", "LOCATOR_ONLY", locator, "REPOSITORY_PATH", "UNKNOWN", "INDEXED", "UNKNOWN", "REBUILDABLE", "DERIVED_STABLE_LOCATOR_ID", "11", "stage11-20260921T011037Z")
        path_to_id[locator] = sid
        return sid

    for x in sorted(references, key=lambda v: v["edge_id"]):
        source_id = locator_entity(x["source"])
        strategy = x["migration_strategy"]
        if strategy == "KEEP":
            status = "RESOLVED"
            target_id = locator_entity(x["resolved_path"])
        elif strategy == "BLOCK":
            status = "UNRESOLVED_REFERENCE"
            target_id = None
        else:
            status = "NOT_A_REFERENCE"
            target_id = None
        evidence_ref = f"{x['source']}:{x['line']}"
        conn.execute("INSERT INTO reference_edges VALUES(?,?,?,?,?,?,?,?,?)", (x["edge_id"], source_id, target_id, "DOCUMENT_LINK", status, x["source"], None if status != "RESOLVED" else x["resolved_path"], strategy, evidence_ref))
        if status == "UNRESOLVED_REFERENCE":
            conn.execute("INSERT INTO unresolved_references VALUES(?,?,?,?,?,?,?,0)", (x["edge_id"], source_id, "DOCUMENT_LINK", x["resolved_path"] or None, status, "12", evidence_ref))

    for x in sorted(artifacts, key=lambda v: v["artifact_id"]):
        original = generated_by_id[x["artifact_id"]]
        is_projection = (x.get("source_role") or "") in {"PROJECT_GUIDE_DERIVED", "DERIVED_PROJECTION", "UI_DESIGN_DERIVED"}
        if is_projection:
            conn.execute("INSERT INTO projections VALUES(?,?,?,?,?,?,0)", (x["artifact_id"], "DERIVED_PROJECTION", json.dumps([]), "INDEXED_SCOPE", x.get("freshness") or "UNKNOWN", "NOT_PROVEN_REBUILDABLE"))
        for ref_path in sorted(set(original.get("references") or original.get("source") or [])):
            target_id = locator_entity(ref_path)
            rid = relation_id("artifact_references", x["artifact_id"], target_id)
            conn.execute("INSERT OR IGNORE INTO relations VALUES(?,?,?,?,?,?)", (rid, "artifact_references", x["artifact_id"], target_id, "INDEXED", rel(GEN_SOURCE)))
            if is_projection:
                p2s = relation_id("projection_to_source", x["artifact_id"], target_id)
                s2p = relation_id("source_to_projection", target_id, x["artifact_id"])
                conn.execute("INSERT OR IGNORE INTO relations VALUES(?,?,?,?,?,?)", (p2s, "projection_to_source", x["artifact_id"], target_id, "INDEXED", rel(GEN_SOURCE)))
                conn.execute("INSERT OR IGNORE INTO relations VALUES(?,?,?,?,?,?)", (s2p, "source_to_projection", target_id, x["artifact_id"], "INDEXED", rel(GEN_SOURCE)))
            if "/changes/" in x["path"]:
                cid = relation_id("change_to_affected_artifact", x["artifact_id"], target_id)
                conn.execute("INSERT OR IGNORE INTO relations VALUES(?,?,?,?,?,?)", (cid, "change_to_affected_artifact", x["artifact_id"], target_id, "INDEXED", rel(GEN_SOURCE)))

        name = Path(x["path"]).name
        if "/changes/" in x["path"] or re.match(r"CR-", name):
            conn.execute("INSERT INTO changes VALUES(?,?,?)", (x["artifact_id"], original.get("approval_status") or "UNKNOWN", json.dumps(original.get("evidence_refs") or [], ensure_ascii=False)))
        if "/decisions/" in x["path"] or re.match(r"(?:DEC|ADR|UI-DEC)-", name):
            conn.execute("INSERT INTO decisions VALUES(?,?,?)", (x["artifact_id"], original.get("approval_status") or "UNKNOWN", json.dumps(original.get("evidence_refs") or [], ensure_ascii=False)))
        if x["path"] in {"docs/project/AI_DOCUMENTATION_GUIDE.md", "docs/project/README.md"}:
            conn.execute("INSERT INTO guides VALUES(?,?,?,?)", (x["artifact_id"], json.dumps(original.get("references") or [], ensure_ascii=False), x.get("freshness") or "UNKNOWN", "INDEXED_FROM_STRUCTURED_RECORD"))

    for x in sorted(operational, key=lambda v: v["artifact_id"]):
        original = operational_by_id[x["artifact_id"]]
        op_type = x.get("operational_type") or "OTHER"
        if op_type in {"PROGRESS", "DASHBOARD", "WORKLOG"}:
            progress_type = "DERIVED_SUMMARY" if op_type == "DASHBOARD" else ("WORK_LOG" if op_type == "WORKLOG" else "HISTORICAL_STATUS")
            conn.execute("INSERT INTO progress_records VALUES(?,?,?,?,?)", (x["artifact_id"], progress_type, "UNKNOWN", json.dumps(original.get("evidence") or [], ensure_ascii=False), x.get("freshness") or "UNKNOWN"))
        if op_type == "HANDOVER":
            generated = generated_by_path.get(x["path"], {})
            canonical_refs = generated.get("references") or generated.get("source") or []
            conn.execute("INSERT INTO handover_records VALUES(?,?,?,?,?,?,?,?)", (x["artifact_id"], "UNKNOWN", json.dumps(canonical_refs, ensure_ascii=False), json.dumps([x["artifact_id"]]), json.dumps([]), json.dumps([]), "UNKNOWN", x.get("freshness") or "UNKNOWN"))
            for ref_path in canonical_refs:
                target_id = locator_entity(ref_path)
                rid = relation_id("handover_to_canonical", x["artifact_id"], target_id)
                conn.execute("INSERT OR IGNORE INTO relations VALUES(?,?,?,?,?,?)", (rid, "handover_to_canonical", x["artifact_id"], target_id, "INDEXED", rel(OP_SOURCE)))
        conn.execute("INSERT INTO history_events VALUES(?,?,?,?,?,?,?,?)", (f"HIST-{x['artifact_id']}", x["artifact_id"], "INDEXED_OPERATIONAL_HISTORY", "UNKNOWN", "HISTORICAL", "UNKNOWN", x["path"], rel(OP_SOURCE)))

    for req in trace_bootstrap.get("requirements", []):
        req_id = req["requirement_id"]
        owner = req.get("owner_stage") or ["UNKNOWN"]
        stage = str(owner[0])
        artifacts_out = req.get("implementation_artifacts") or req.get("design_artifacts") or []
        evidence = req.get("evidence") or []
        run_id = "UNKNOWN"
        for p in artifacts_out + evidence:
            m = re.search(r"stages/\d{2}/([^/]+)/", p)
            if m:
                run_id = m.group(1)
                break
        lineage = {"input_refs": req.get("design_artifacts") or [], "output_refs": artifacts_out, "decision_refs": [], "change_refs": [], "evidence_refs": evidence}
        conn.execute("INSERT INTO trace_events VALUES(?,?,?,?,?,?,?,?,?,?,?,0)", (f"TRACE-{req_id}", "STAGE_REQUIREMENT_SATISFIED", req_id, stage, run_id, "UNKNOWN", "UNKNOWN", req.get("status") or "UNKNOWN", req.get("capability_state") or req.get("status") or "UNKNOWN", json.dumps(lineage, ensure_ascii=False, sort_keys=True), json.dumps(evidence, ensure_ascii=False)))
        conn.execute("INSERT INTO history_events VALUES(?,?,?,?,?,?,?,?)", (f"HISTORY-{req_id}", req_id, "REQUIREMENT_STATE", "UNKNOWN", req.get("status") or "UNKNOWN", "UNKNOWN", rel(TRACE_BOOTSTRAP), evidence[0] if evidence else rel(TRACE_BOOTSTRAP)))

    blockers = load_yaml(S10 / "MIGRATION_BLOCKER_CARRYOVER.yaml")["blockers"]
    for b in blockers:
        bid = b["id"]
        conn.execute("INSERT INTO history_events VALUES(?,?,?,?,?,?,?,?)", (f"HISTORY-BLOCKER-{bid}", bid, "BLOCKER_STATE", "UNKNOWN", b["status"], "UNKNOWN", rel(S10 / "MIGRATION_BLOCKER_CARRYOVER.yaml"), rel(S10 / "MIGRATION_BLOCKER_CARRYOVER.yaml")))

    for x in sorted(secret_records, key=lambda v: v["path"]):
        sid = "SECRET-" + hashlib.sha256(x["path"].encode()).hexdigest()[:16]
        entity(sid, "SecretMetadata", "SECRET_METADATA_ONLY", "SECRET_METADATA_ONLY", "NO_CONTENT_AUTHORITY", x["path"], "REPOSITORY_PATH", "UNKNOWN", "PRESERVE_IN_PLACE", "UNKNOWN", "NOT_PROVEN_REBUILDABLE", "METADATA_ONLY", "00", "stage00-precheck-20260920T083254Z")
        conn.execute("INSERT INTO secret_metadata VALUES(?,?,?,?,1,0,0,0)", (sid, x["path"], "SECRET_METADATA_ONLY", "NO_BODY|NO_BODY_HASH|NO_DERIVED_VALUE|NO_COPY"))

    for idx, (path, entity_types, imported_count, hash_allowed) in enumerate(source_files, 1):
        conn.execute("INSERT INTO migration_ledger VALUES(?,?,?,?,?,?,?)", (f"LEDGER-{idx:03d}", rel(path), sha(path) if hash_allowed else None, imported_count, "IMPORTED", "UNKNOWN", "STRUCTURED_INPUT; secret metadata source deliberately unhashed" if not hash_allowed else "STRUCTURED_INPUT"))

    conn.commit()
    integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
    fk = conn.execute("PRAGMA foreign_key_check").fetchall()
    logical_hash, counts = logical_snapshot(conn)
    conn.close()
    return {"logical_hash": logical_hash, "counts": counts, "integrity_check": integrity, "foreign_key_violations": len(fk), "byte_sha256": sha(db_path)}

primary = build(PRIMARY_DB)
rebuilt = build(REBUILD_DB)

def scalar(db: Path, sql: str, params: tuple[Any, ...] = ()) -> Any:
    with sqlite3.connect(db) as conn:
        return conn.execute(sql, params).fetchone()[0]

integrity_checks = {
    "sqlite_integrity": primary["integrity_check"],
    "foreign_key_violations": primary["foreign_key_violations"],
    "index_mode": scalar(PRIMARY_DB, "SELECT value FROM index_metadata WHERE key='INDEX_MODE'"),
    "rebuildability": scalar(PRIMARY_DB, "SELECT value FROM index_metadata WHERE key='REBUILDABILITY'"),
    "canonical_truth": scalar(PRIMARY_DB, "SELECT value FROM index_metadata WHERE key='CANONICAL_TRUTH'"),
    "final_runtime_db": scalar(PRIMARY_DB, "SELECT value FROM index_metadata WHERE key='FINAL_RUNTIME_DB'"),
    "records_without_stable_id": scalar(PRIMARY_DB, "SELECT count(*) FROM entities WHERE stable_id IS NULL OR stable_id=''"),
    "records_without_classification": scalar(PRIMARY_DB, "SELECT count(*) FROM entities WHERE classification IS NULL OR classification=''"),
    "reference_edges": scalar(PRIMARY_DB, "SELECT count(*) FROM reference_edges"),
    "unresolved_references": scalar(PRIMARY_DB, "SELECT count(*) FROM unresolved_references"),
    "not_a_reference": scalar(PRIMARY_DB, "SELECT count(*) FROM reference_edges WHERE reference_status='NOT_A_REFERENCE'"),
    "invented_unresolved_targets": scalar(PRIMARY_DB, "SELECT count(*) FROM unresolved_references WHERE invented_target<>0"),
    "trace_without_lineage": scalar(PRIMARY_DB, "SELECT count(*) FROM trace_events WHERE lineage_json IS NULL OR lineage_json='' OR lineage_json='{}'"),
    "trace_authorization_paths": scalar(PRIMARY_DB, "SELECT count(*) FROM trace_events WHERE grants_authorization<>0"),
    "secret_metadata_records": scalar(PRIMARY_DB, "SELECT count(*) FROM secret_metadata"),
    "secret_body_or_hash_or_derived_indexed": scalar(PRIMARY_DB, "SELECT count(*) FROM secret_metadata WHERE body_indexed<>0 OR body_hash_indexed<>0 OR derived_value_indexed<>0"),
    "blocked_or_open_history_events": scalar(PRIMARY_DB, "SELECT count(*) FROM history_events WHERE upper(to_state) IN ('BLOCKED','OPEN','PARTIAL_APPROVED','UNRESOLVED_REFERENCE')"),
}
if integrity_checks["reference_edges"] != 108 or integrity_checks["unresolved_references"] != 4 or integrity_checks["not_a_reference"] != 2:
    raise RuntimeError(f"reference invariant failed: {integrity_checks}")
if integrity_checks["secret_metadata_records"] != 13 or integrity_checks["secret_body_or_hash_or_derived_indexed"] != 0:
    raise RuntimeError(f"secret invariant failed: {integrity_checks}")
if primary["logical_hash"] != rebuilt["logical_hash"] or primary["counts"] != rebuilt["counts"]:
    raise RuntimeError("isolated rebuild mismatch")

query_specs = [
    ("artifact_by_stable_id", "SELECT stable_id, classification, authority, freshness, provenance_state FROM entities WHERE stable_id=(SELECT stable_id FROM artifacts ORDER BY stable_id LIMIT 1)"),
    ("current_locator_by_stable_id", "SELECT stable_id,current_locator,authority,freshness,provenance_state FROM entities WHERE current_locator IS NOT NULL ORDER BY stable_id LIMIT 5"),
    ("incoming_references", "SELECT target_id,count(*) FROM reference_edges WHERE target_id IS NOT NULL GROUP BY target_id ORDER BY target_id LIMIT 5"),
    ("outgoing_references", "SELECT source_id,count(*) FROM reference_edges GROUP BY source_id ORDER BY source_id LIMIT 5"),
    ("unresolved_references", "SELECT reference_id,source_id,missing_target_locator,status,owner_stage FROM unresolved_references ORDER BY reference_id"),
    ("source_role_and_authority", "SELECT source_role,authority,count(*) FROM entities GROUP BY source_role,authority ORDER BY source_role,authority"),
    ("version_status_history", "SELECT artifact_id,version,status,provenance_state FROM artifact_versions JOIN artifact_status_history USING(artifact_id) ORDER BY artifact_id LIMIT 5"),
    ("change_affected_artifacts", "SELECT source_id,target_id,status FROM relations WHERE relation_type='change_to_affected_artifact' ORDER BY source_id,target_id LIMIT 10"),
    ("decision_evidence", "SELECT decision_id,status,evidence_json FROM decisions ORDER BY decision_id LIMIT 5"),
    ("projection_sources", "SELECT source_id,target_id,status FROM relations WHERE relation_type='projection_to_source' ORDER BY source_id,target_id LIMIT 10"),
    ("source_projections", "SELECT source_id,target_id,status FROM relations WHERE relation_type='source_to_projection' ORDER BY source_id,target_id LIMIT 10"),
    ("stale_projections", "SELECT projection_id,freshness,rebuildability FROM projections WHERE freshness LIKE '%STALE%' OR freshness LIKE '%REVIEW_REQUIRED%' ORDER BY projection_id"),
    ("handover_canonical_refs", "SELECT handover_id,canonical_refs_json,operational_refs_json,freshness FROM handover_records ORDER BY handover_id"),
    ("progress_current_historical", "SELECT progress_type,count(*),min(freshness) FROM progress_records GROUP BY progress_type ORDER BY progress_type"),
    ("trace_by_stage_run_subject", "SELECT stage,run_id,subject_id,status,result FROM trace_events ORDER BY stage,run_id,subject_id"),
]
query_results = []
with sqlite3.connect(PRIMARY_DB) as conn:
    for name, sql in query_specs:
        rows = conn.execute(sql).fetchall()
        query_results.append({"query": name, "status": "PASS", "row_count": len(rows), "sample": rows[:5]})
    unresolved_db = {
        row[0]: row
        for row in conn.execute(
            "SELECT reference_id,source_id,missing_target_locator,status,owner_stage FROM unresolved_references ORDER BY reference_id"
        ).fetchall()
    }

manifest = {
    "schema_version": "stage11-v1",
    "run_id": "stage11-20260921T011037Z",
    "mode": "STRUCTURED_INPUT_FIRST",
    "sources": [
        {
            "source_id": f"SRC-{i:03d}", "source_stage": re.search(r"stages/(\d{2})/", rel(path)).group(1) if re.search(r"stages/(\d{2})/", rel(path)) else "BOOTSTRAP",
            "source_ref": rel(path), "source_hash": sha(path) if hash_allowed else None,
            "entity_types": entity_types, "expected_count": count, "import_status": "IMPORTED",
            "qualification": None if hash_allowed else "SECRET_METADATA_SOURCE_UNHASHED",
        }
        for i, (path, entity_types, count, hash_allowed) in enumerate(source_files, 1)
    ],
    "body_inputs_loaded": 0,
    "git_history_reanalyzed": False,
}
dump_yaml(RUN / "INDEX_IMPORT_MANIFEST.yaml", manifest)
dump_yaml(RUN / "INDEX_MIGRATION_LEDGER.yaml", {"schema_version": "stage11-v1", "entries": [{"ledger_id": f"LEDGER-{i:03d}", "source_ref": rel(path), "source_hash": sha(path) if hash_allowed else None, "imported_count": count, "import_status": "IMPORTED", "notes": "STRUCTURED_INPUT" if hash_allowed else "SECRET_METADATA_ONLY_SOURCE_UNHASHED"} for i, (path, _, count, hash_allowed) in enumerate(source_files, 1)]})
dump_yaml(RUN / "UNRESOLVED_REFERENCE_REGISTRY.yaml", {"schema_version": "stage11-v1", "entries": [{"reference_id": x["edge_id"], "source_id": unresolved_db[x["edge_id"]][1], "relationship": "DOCUMENT_LINK", "missing_target_locator": unresolved_db[x["edge_id"]][2], "target_id": None, "status": unresolved_db[x["edge_id"]][3], "owner_stage": unresolved_db[x["edge_id"]][4], "evidence_ref": f"{x['source']}:{x['line']}"} for x in references if x["migration_strategy"] == "BLOCK"], "not_a_reference": [{"reference_id": x["edge_id"], "status": "NOT_A_REFERENCE", "reason": x["explanation"]} for x in references if x["migration_strategy"] == "IGNORE_AS_NON_REFERENCE"], "invent_target_allowed": False})
(RUN / "evidence/INTEGRITY_RESULTS.json").write_text(json.dumps(integrity_checks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(RUN / "evidence/QUERY_RESULTS.json").write_text(json.dumps({"overall": "PASS", "queries": query_results}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(RUN / "evidence/INDEX_COUNTS.json").write_text(json.dumps(primary["counts"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
dump_yaml(RUN / "REBUILDABILITY_REPORT.yaml", {"schema_version": "stage11-v1", "run_id": "stage11-20260921T011037Z", "status": "PASS", "shadow_db": rel(PRIMARY_DB), "isolated_rebuild_db": rel(REBUILD_DB), "structured_input_only": True, "manual_database_patch": False, "canonical_writeback": False, "primary_logical_hash": primary["logical_hash"], "rebuild_logical_hash": rebuilt["logical_hash"], "logical_hash_match": True, "table_counts_match": True, "primary_byte_sha256": primary["byte_sha256"], "rebuild_byte_sha256": rebuilt["byte_sha256"], "byte_hash_match": primary["byte_sha256"] == rebuilt["byte_sha256"], "integrity_check": primary["integrity_check"], "foreign_key_violations": primary["foreign_key_violations"], "rebuild_command": "python3 evidence/build_shadow_index.py"})
dump_yaml(RUN / "STAGE12_QUERY_SURFACE.yaml", {"schema_version": "stage11-v1", "surfaces": {"freshness": ["entity_freshness", "source_version_history", "conflict_state"], "context": ["current_progress", "latest_handover_with_as_of", "related_canonical_refs", "related_operational_refs"], "history": ["subject_state_history", "reverted_failed_stopped_blocked_events"], "reference": ["unresolved_references", "incoming_outgoing_edges"], "projection": ["projection_to_sources", "source_to_projections"], "trace": ["subject_trace", "run_trace"]}, "authority_fields_required": True, "freshness_fields_required": True, "provenance_fields_required": True, "con002": {"status": "OPEN", "owner_stage": "12", "resolved_in_stage11": False}, "shadow_index": {"path": rel(PRIMARY_DB), "canonical_truth": False, "rebuildable": True}})
print(json.dumps({"primary": primary, "rebuilt": rebuilt, "integrity": integrity_checks, "queries": len(query_results)}, ensure_ascii=False))

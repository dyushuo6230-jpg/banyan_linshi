#!/usr/bin/env python3
"""Stage 11 delivery-pack helper: validate the bundled SQL schema with stdlib sqlite3."""
from pathlib import Path
import sqlite3
import sys

root = Path(__file__).resolve().parents[1]
schema = (root / "templates" / "SHADOW_INDEX_SCHEMA.sql").read_text(encoding="utf-8")
conn = sqlite3.connect(":memory:")
try:
    conn.executescript(schema)
    required = {
        "entities", "reference_edges", "trace_events", "history_events",
        "relations", "unresolved_references", "migration_ledger"
    }
    actual = {r[0] for r in conn.execute(
        "select name from sqlite_master where type='table'"
    )}
    missing = sorted(required - actual)
    if missing:
        print("FAIL missing tables:", ", ".join(missing))
        sys.exit(1)
    print("PASS Stage11 shadow schema smoke-check")
finally:
    conn.close()

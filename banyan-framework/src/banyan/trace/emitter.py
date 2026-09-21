"""Append-only JSONL audit trace with a strict minimum schema."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping


REQUIRED_FIELDS = {"event_type", "action_id", "occurred_at", "result", "grants_authorization"}


class TraceValidationError(ValueError):
    pass


class TraceEmitter:
    def __init__(self, path: str | Path):
        self.path = Path(path)

    @staticmethod
    def validate(event: Mapping[str, Any]) -> None:
        missing = REQUIRED_FIELDS - set(event)
        if missing:
            raise TraceValidationError(f"missing trace fields: {sorted(missing)}")
        if event["grants_authorization"] is not False:
            raise TraceValidationError("trace records cannot grant authorization")
        if not all(isinstance(event[key], str) and event[key] for key in ("event_type", "action_id", "occurred_at", "result")):
            raise TraceValidationError("trace string fields must be non-empty")

    def emit(self, event: Mapping[str, Any]) -> None:
        self.validate(event)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(dict(event), sort_keys=True, ensure_ascii=False) + "\n")

    @classmethod
    def validate_file(cls, path: str | Path) -> int:
        count = 0
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            if line.strip():
                cls.validate(json.loads(line))
                count += 1
        return count

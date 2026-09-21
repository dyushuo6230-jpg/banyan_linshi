import json
from pathlib import Path
import tempfile
import unittest

from banyan.providers.loader import ProviderBindingLoader
from banyan.trace.emitter import TraceEmitter, TraceValidationError


def test_trace_is_append_only_and_validated():
    path = Path(tempfile.mkdtemp()) / "audit.jsonl"
    event = {"event_type": "TEST", "action_id": "a", "occurred_at": "now", "result": "ALLOW", "grants_authorization": False}
    TraceEmitter(path).emit(event)
    TraceEmitter(path).emit(event)
    assert TraceEmitter.validate_file(path) == 2
    with unittest.TestCase().assertRaises(TraceValidationError):
        TraceEmitter(path).emit({**event, "grants_authorization": True})


def test_provider_loader_is_strict():
    path = Path(tempfile.mkdtemp()) / "providers.json"
    path.write_text(json.dumps({"bindings": [{"id": "x", "provider": "local", "enabled": True}]}))
    assert ProviderBindingLoader().load(path)[0]["id"] == "x"
    path.write_text(json.dumps({"bindings": [], "extra": True}))
    with unittest.TestCase().assertRaises(ValueError):
        ProviderBindingLoader().load(path)

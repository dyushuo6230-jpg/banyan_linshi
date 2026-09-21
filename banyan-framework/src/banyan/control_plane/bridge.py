"""Typed local-stdio bridge from the Go transport to the preserved Runtime API."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

import yaml

from banyan.editor import AdapterGateway, CodexAdapter, CursorAdapter, GenericEditorAdapter
from banyan.policy import PolicyCompiler
from banyan.runtime.api import RuntimeAPI
from .service import ControlPlaneService


def _load(path: str | None, default: Any) -> Any:
    if not path:
        return default
    source = Path(path)
    if not source.exists():
        return default
    text = source.read_text(encoding="utf-8")
    return json.loads(text) if source.suffix.lower() == ".json" else yaml.safe_load(text)


def _service() -> ControlPlaneService:
    repository = os.environ["BANYAN_REPOSITORY"]
    policy_path = os.environ["BANYAN_POLICY"]
    trace_path = os.environ.get("BANYAN_TRACE")
    runtime = RuntimeAPI(PolicyCompiler().compile_file(policy_path), trace_path)
    return ControlPlaneService(
        runtime,
        repository,
        trace_path=trace_path,
        provider_path=os.environ.get("BANYAN_PROVIDERS"),
        provenance=_load(os.environ.get("BANYAN_PROVENANCE"), {}),
        stages=_load(os.environ.get("BANYAN_STAGES"), []),
    )


def dispatch(service: ControlPlaneService, operation: str, payload: dict[str, Any]) -> dict[str, Any]:
    operations = {
        "status": lambda: service.status(),
        "policy_status": lambda: service.policy_status(),
        "project_safety": lambda: service.project_safety(),
        "preflight": lambda: service.preflight(payload),
        "commit_plan": lambda: service.commit_plan(payload),
        "commit_dry_run": lambda: service.commit_dry_run(payload),
        "trace_query": lambda: service.trace(offset=int(payload.get("offset", 0)), limit=int(payload.get("limit", 50))),
        "provenance_query": lambda: service.provenance_view(str(payload.get("stable_id", "UNKNOWN"))),
        "provider_status": lambda: {"items": service.providers()},
        "stage_query": lambda: service.stages(offset=int(payload.get("offset", 0)), limit=int(payload.get("limit", 25))),
        "activation_readiness": lambda: service.activation_readiness(),
    }
    if operation == "adapter_request":
        kind = str(payload.get("adapter", ""))
        request = payload.get("request")
        if not isinstance(request, dict):
            raise ValueError("adapter request must be an object")
        adapters = {"cursor": CursorAdapter, "codex": CodexAdapter, "generic-editor": GenericEditorAdapter}
        if kind not in adapters:
            raise ValueError("unknown adapter")
        return adapters[kind](AdapterGateway(service)).handle(request).to_dict()
    if operation not in operations:
        raise ValueError("unknown bridge operation")
    return operations[operation]()


def main() -> int:
    try:
        value = json.load(sys.stdin)
        if not isinstance(value, dict) or not isinstance(value.get("payload", {}), dict):
            raise ValueError("bridge request must contain an object payload")
        result = dispatch(_service(), str(value.get("operation", "")), value.get("payload", {}))
        json.dump({"ok": True, "result": result}, sys.stdout, ensure_ascii=False, sort_keys=True)
        return 0
    except Exception as exc:  # typed boundary; no fallback implementation
        json.dump({"ok": False, "error": {"code": "RUNTIME_BRIDGE_FAILURE", "message": str(exc)}}, sys.stdout, ensure_ascii=False, sort_keys=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

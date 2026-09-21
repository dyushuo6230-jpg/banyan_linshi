"""Cursor, Codex, and generic editor request-shape adapters."""

from __future__ import annotations

from typing import Any, Mapping

from .protocol import AdapterGateway, AdapterRequest, AdapterResponse


class _BaseAdapter:
    adapter_id = "generic"
    request_id_field = "request_id"
    action_field = "action"
    payload_field = "payload"
    metadata_field = "provenance"

    def __init__(self, gateway: AdapterGateway):
        self.gateway = gateway

    def transform(self, raw: Mapping[str, Any]) -> AdapterRequest:
        allowed = {self.request_id_field, self.action_field, self.payload_field, self.metadata_field, "evidence_refs"}
        unknown = set(raw) - allowed
        if unknown:
            raise ValueError(f"unknown adapter request fields: {sorted(unknown)}")
        request_id = raw.get(self.request_id_field)
        action = raw.get(self.action_field)
        payload = raw.get(self.payload_field, {})
        metadata = raw.get(self.metadata_field, {})
        evidence = raw.get("evidence_refs", ())
        if not isinstance(request_id, str) or not request_id:
            raise ValueError("request id is required")
        if not isinstance(action, str) or not action:
            raise ValueError("action is required")
        if not isinstance(payload, dict) or not isinstance(metadata, dict):
            raise ValueError("payload and provenance must be objects")
        if not isinstance(evidence, (list, tuple)) or not all(isinstance(item, str) for item in evidence):
            raise ValueError("evidence_refs must be a string list")
        return AdapterRequest(request_id, self.adapter_id, action, dict(payload), tuple(evidence), dict(metadata))

    def handle(self, raw: Mapping[str, Any]) -> AdapterResponse:
        try:
            return self.gateway.handle(self.transform(raw))
        except (KeyError, TypeError, ValueError) as exc:
            return self.gateway.failure(self.adapter_id, "ADAPTER_REQUEST_INVALID", str(exc))

    @staticmethod
    def capabilities() -> dict[str, bool]:
        return {
            "owns_permission_policy": False,
            "owns_canonical_truth": False,
            "direct_git_mutation": False,
            "runtime_api_required": True,
        }


class CursorAdapter(_BaseAdapter):
    adapter_id = "cursor"
    action_field = "command"
    payload_field = "arguments"
    metadata_field = "context"


class CodexAdapter(_BaseAdapter):
    adapter_id = "codex"
    request_id_field = "id"
    action_field = "operation"
    payload_field = "input"
    metadata_field = "metadata"


class GenericEditorAdapter(_BaseAdapter):
    adapter_id = "generic-editor"

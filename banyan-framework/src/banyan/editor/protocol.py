"""Editor-neutral request protocol backed exclusively by the Control Plane/Runtime."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Mapping

from banyan.control_plane.service import ControlPlaneService


SUPPORTED_ACTIONS = {
    "runtime_status", "project_safety", "preflight", "commit_plan",
    "commit_dry_run", "trace", "provenance",
}
FORBIDDEN_ACTIONS = {
    "git_mutation", "commit_execute", "canonical_write", "protected_write_execute",
    "activate", "identity_write", "secret_body_read",
}


@dataclass(frozen=True)
class AdapterRequest:
    request_id: str
    adapter_id: str
    action: str
    payload: dict[str, Any] = field(default_factory=dict)
    evidence_refs: tuple[str, ...] = ()
    provenance: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class AdapterResponse:
    request_id: str
    adapter_id: str
    action: str
    status: str
    result: dict[str, Any]
    evidence_refs: tuple[str, ...]
    provenance: dict[str, Any]
    trace_recorded: bool
    permission_owned_by_adapter: bool = False
    canonical_write_owned_by_adapter: bool = False
    direct_git_mutation: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class AdapterGateway:
    """Dispatch protocol requests without duplicating Runtime permission logic."""

    def __init__(self, control_plane: ControlPlaneService):
        if control_plane.runtime.trace is None:
            raise ValueError("adapter validation requires Runtime evidence tracing")
        self.control_plane = control_plane

    def handle(self, request: AdapterRequest) -> AdapterResponse:
        try:
            if request.action in FORBIDDEN_ACTIONS or request.action not in SUPPORTED_ACTIONS:
                runtime_result = self.control_plane.preflight({
                    "action_id": request.request_id,
                    "action_type": request.action,
                    "target_id": request.payload.get("target_id", "UNKNOWN"),
                    "target_state": request.payload.get("target_state", {}),
                    "evidence_refs": request.evidence_refs,
                    "authorization_ref": request.payload.get("authorization_ref"),
                    "precondition_results": request.payload.get("precondition_results", {}),
                })
                response = self._response(
                    request,
                    "BLOCKED",
                    {"error_code": "UNSUPPORTED_OR_FORBIDDEN_ACTION", "runtime_decision": runtime_result},
                )
            else:
                result = self._dispatch(request)
                response = self._response(request, "OK", result)
            self._trace(response)
            return response
        except (KeyError, TypeError, ValueError) as exc:
            response = self._response(request, "FAILED", {"error_code": "INVALID_REQUEST", "detail": str(exc)})
            self._trace(response)
            return response
        except Exception as exc:
            response = self._response(request, "FAILED", {"error_code": "RUNTIME_FAILURE", "detail": type(exc).__name__})
            self._trace(response)
            return response

    def failure(self, adapter_id: str, error_code: str, detail: str) -> AdapterResponse:
        request = AdapterRequest("UNKNOWN", adapter_id, "INVALID")
        response = self._response(request, "FAILED", {"error_code": error_code, "detail": detail})
        self._trace(response)
        return response

    def _dispatch(self, request: AdapterRequest) -> dict[str, Any]:
        action = request.action
        if action == "runtime_status":
            return self.control_plane.status()
        if action == "project_safety":
            return self.control_plane.project_safety()
        if action == "preflight":
            return self.control_plane.preflight(request.payload)
        if action == "commit_plan":
            return self.control_plane.commit_plan(request.payload)
        if action == "commit_dry_run":
            return self.control_plane.commit_dry_run(request.payload)
        if action == "trace":
            return self.control_plane.trace(
                offset=int(request.payload.get("offset", 0)), limit=int(request.payload.get("limit", 50)),
            )
        if action == "provenance":
            return self.control_plane.provenance_view(str(request.payload["stable_id"]))
        raise ValueError("unsupported action")

    def _response(self, request: AdapterRequest, status: str, result: dict[str, Any]) -> AdapterResponse:
        provenance = {
            "stable_id": request.provenance.get("stable_id", "UNKNOWN"),
            "source_role": request.provenance.get("source_role", "UNKNOWN"),
            "authority": request.provenance.get("authority", "UNKNOWN"),
            "freshness": request.provenance.get("freshness", "UNKNOWN"),
            "source_refs": list(request.provenance.get("source_refs", ())),
        }
        return AdapterResponse(
            request.request_id, request.adapter_id, request.action, status, result,
            request.evidence_refs, provenance, True,
        )

    def _trace(self, response: AdapterResponse) -> None:
        self.control_plane.runtime.emit_audit({
            "event_type": "ADAPTER_REQUEST_COMPLETED",
            "action_id": response.request_id,
            "occurred_at": datetime.now(timezone.utc).isoformat(),
            "result": response.status,
            "grants_authorization": False,
            "adapter_id": response.adapter_id,
            "adapter_action": response.action,
            "evidence_refs": list(response.evidence_refs),
            "provenance": response.provenance,
            "permission_owned_by_adapter": False,
            "canonical_write_owned_by_adapter": False,
            "direct_git_mutation": False,
        })

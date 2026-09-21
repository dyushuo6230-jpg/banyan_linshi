"""Loopback-only HTTP adapter for the generic Control Plane service."""

from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import ipaddress
import json
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, unquote, urlparse

from .service import ControlPlaneService


DEFAULT_HOST = "127.0.0.1"
MAX_BODY_BYTES = 1_000_000
WEB_ROOT = Path(__file__).resolve().parent.parent / "web"


def validate_bind_host(host: str) -> str:
    if host == "localhost":
        return host
    try:
        if ipaddress.ip_address(host).is_loopback:
            return host
    except ValueError:
        pass
    raise ValueError("Control Plane may bind only to localhost or a loopback address")


class ControlPlaneApplication:
    def __init__(self, service: ControlPlaneService):
        self.service = service

    def dispatch(self, method: str, raw_path: str, body: dict[str, Any] | None = None) -> tuple[int, dict[str, Any]]:
        parsed = urlparse(raw_path)
        path = parsed.path
        query = parse_qs(parsed.query)
        if method == "GET" and path == "/api/status":
            return 200, self.service.status()
        if method == "GET" and path == "/api/policy":
            return 200, self.service.policy_status()
        if method == "GET" and path == "/api/project-safety":
            return 200, self.service.project_safety()
        if method == "GET" and path == "/api/trace":
            return 200, self.service.trace(offset=self._int(query, "offset", 0), limit=self._int(query, "limit", 50))
        if method == "GET" and path.startswith("/api/provenance/"):
            return 200, self.service.provenance_view(unquote(path.removeprefix("/api/provenance/")))
        if method == "GET" and path == "/api/providers":
            return 200, {"items": self.service.providers()}
        if method == "GET" and path == "/api/stages":
            return 200, self.service.stages(offset=self._int(query, "offset", 0), limit=self._int(query, "limit", 25))
        if method == "GET" and path == "/api/activation-readiness":
            return 200, self.service.activation_readiness()
        if method == "POST" and path == "/api/preflight":
            return 200, self.service.preflight(body or {})
        if method == "POST" and path == "/api/commit/plan":
            return 200, self.service.commit_plan(body or {})
        if method == "POST" and path == "/api/commit/dry-run":
            return 200, self.service.commit_dry_run(body or {})
        return 404, {"error": "NOT_FOUND"}

    @staticmethod
    def _int(query: dict[str, list[str]], key: str, default: int) -> int:
        return int(query.get(key, [str(default)])[0])


def handler_for(application: ControlPlaneApplication):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            if self.path == "/" or self.path.startswith("/assets/"):
                self._static()
            else:
                self._api("GET")

        def do_POST(self) -> None:
            self._api("POST")

        def _api(self, method: str) -> None:
            try:
                body = None
                if method == "POST":
                    length = int(self.headers.get("Content-Length", "0"))
                    if length > MAX_BODY_BYTES:
                        self._json(413, {"error": "BODY_TOO_LARGE"})
                        return
                    body = json.loads(self.rfile.read(length) or b"{}")
                    if not isinstance(body, dict):
                        raise ValueError("request body must be an object")
                status, payload = application.dispatch(method, self.path, body)
                self._json(status, payload)
            except (KeyError, TypeError, ValueError) as exc:
                self._json(400, {"error": "INVALID_REQUEST", "detail": str(exc)})

        def _static(self) -> None:
            relative = "index.html" if self.path == "/" else self.path.removeprefix("/assets/")
            target = (WEB_ROOT / relative).resolve()
            if WEB_ROOT not in target.parents or not target.is_file():
                self.send_error(404)
                return
            content_type = {".html": "text/html", ".js": "text/javascript", ".css": "text/css"}.get(target.suffix, "application/octet-stream")
            data = target.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", f"{content_type}; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def _json(self, status: int, payload: dict[str, Any]) -> None:
            data = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, format: str, *args: Any) -> None:
            return

    return Handler


def create_server(service: ControlPlaneService, host: str = DEFAULT_HOST, port: int = 0) -> ThreadingHTTPServer:
    safe_host = validate_bind_host(host)
    return ThreadingHTTPServer((safe_host, port), handler_for(ControlPlaneApplication(service)))

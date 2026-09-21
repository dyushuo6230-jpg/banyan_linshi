from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

from banyan.policy import PolicyCompiler
from banyan.runtime.api import RuntimeAPI
from .server import DEFAULT_HOST, create_server
from .service import ControlPlaneService


def _load(path: str | None, default: Any) -> Any:
    if not path:
        return default
    source = Path(path)
    text = source.read_text(encoding="utf-8")
    return json.loads(text) if source.suffix.lower() == ".json" else yaml.safe_load(text)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="banyan-control-plane")
    parser.add_argument("--repository", required=True)
    parser.add_argument("--policy", required=True)
    parser.add_argument("--trace")
    parser.add_argument("--providers")
    parser.add_argument("--provenance")
    parser.add_argument("--stages")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=8765)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    policy = PolicyCompiler().compile_file(args.policy)
    provenance_data = _load(args.provenance, {})
    stages_data = _load(args.stages, [])
    service = ControlPlaneService(
        RuntimeAPI(policy, args.trace),
        args.repository,
        trace_path=args.trace,
        provider_path=args.providers,
        provenance=provenance_data,
        stages=stages_data,
    )
    server = create_server(service, args.host, args.port)
    print(f"Banyan Control Plane: http://{args.host}:{server.server_port} (LOCAL_ONLY, DRY_RUN_ONLY)")
    server.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

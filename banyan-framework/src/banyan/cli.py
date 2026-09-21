"""Command-line surface for the generic Banyan runtime."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

from banyan.commit.planner import CommitGroup, CommitPlan
from banyan.git.adapter import GitAdapter
from banyan.policy import PolicyCompiler, default_policy
from banyan.runtime.api import RuntimeAPI
from banyan.runtime.models import ActionRequest, ExecutionScope
from banyan.trace.emitter import TraceEmitter


def _read(path: str) -> Any:
    source = Path(path)
    text = source.read_text(encoding="utf-8")
    return json.loads(text) if source.suffix.lower() == ".json" else yaml.safe_load(text)


def _compiled(path: str | None):
    compiler = PolicyCompiler()
    return compiler.compile_file(path) if path else compiler.compile(default_policy())


def _plan_from_dict(value: dict[str, Any]) -> CommitPlan:
    allowed = {"groups", "classifications", "blocked_paths", "leftovers"}
    if set(value) != allowed:
        raise ValueError("commit plan fields mismatch")
    groups = tuple(
        CommitGroup(
            group_id=item["group_id"], message=item["message"],
            paths=tuple(item["paths"]), patches=tuple(item.get("patches", ())),
            patch_paths=tuple(item.get("patch_paths", ())),
        )
        for item in value["groups"]
    )
    return CommitPlan(groups, dict(value["classifications"]), tuple(value["blocked_paths"]), tuple(value["leftovers"]))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="banyan")
    top = parser.add_subparsers(dest="domain", required=True)

    policy = top.add_parser("policy").add_subparsers(dest="command", required=True)
    for name in ("validate", "compile"):
        sub = policy.add_parser(name)
        sub.add_argument("path")
    bundle = policy.add_parser("compile-stage14")
    bundle.add_argument("path")

    runtime = top.add_parser("runtime").add_subparsers(dest="command", required=True)
    preflight = runtime.add_parser("preflight")
    preflight.add_argument("request")
    preflight.add_argument("--policy")

    git = top.add_parser("git").add_subparsers(dest="command", required=True)
    inspect = git.add_parser("inspect")
    inspect.add_argument("repository")

    commit = top.add_parser("commit").add_subparsers(dest="command", required=True)
    plan = commit.add_parser("plan")
    plan.add_argument("repository")
    plan.add_argument("--classifications", required=True)
    plan.add_argument("--groups")
    plan.add_argument("--messages")
    execute = commit.add_parser("execute")
    execute.add_argument("repository")
    execute.add_argument("--plan", required=True)
    execute.add_argument("--policy")
    execute.add_argument("--authorization-ref")
    execute.add_argument("--trace")
    mode = execute.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--fixture-root")

    trace = top.add_parser("trace").add_subparsers(dest="command", required=True)
    validate_trace = trace.add_parser("validate")
    validate_trace.add_argument("path")
    emit = trace.add_parser("emit")
    emit.add_argument("path")
    emit.add_argument("event")

    provider = top.add_parser("provider").add_subparsers(dest="command", required=True)
    listing = provider.add_parser("list")
    listing.add_argument("path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.domain == "policy":
        compiler = PolicyCompiler()
        compiled = (compiler.compile_stage14_bundle(args.path)
                    if args.command == "compile-stage14" else compiler.compile_file(args.path))
        output = {"valid": True, "policy_hash": compiled.policy_hash}
        if args.command in {"compile", "compile-stage14"}:
            output["policy"] = dict(compiled.data)
    elif args.domain == "runtime":
        data = _read(args.request)
        request = ActionRequest(
            action_id=data["action_id"], action_type=data["action_type"],
            execution_scope=ExecutionScope(data["execution_scope"]), target_id=data["target_id"],
            target_state=data.get("target_state", {}), work_mode=data.get("work_mode", "STANDARD"),
            evidence_refs=tuple(data.get("evidence_refs", ())), impact_ref=data.get("impact_ref"),
            decision_ref=data.get("decision_ref"), authorization_ref=data.get("authorization_ref"),
            precondition_results=data.get("precondition_results", {}),
        )
        output = RuntimeAPI(_compiled(args.policy)).preflight_action(request).to_dict()
    elif args.domain == "git":
        output = RuntimeAPI(_compiled(None)).inspect_project(args.repository)
    elif args.domain == "commit" and args.command == "plan":
        output = RuntimeAPI(_compiled(None)).plan_commit(
            args.repository, _read(args.classifications),
            groups=_read(args.groups) if args.groups else None,
            messages=_read(args.messages) if args.messages else None,
        )
    elif args.domain == "commit":
        adapter = GitAdapter(args.repository, fixture_root=args.fixture_root)
        output = RuntimeAPI(_compiled(args.policy), args.trace).execute_commit(
            adapter=adapter, plan=_plan_from_dict(_read(args.plan)), dry_run=args.dry_run,
            authorization_ref=args.authorization_ref,
        )
    elif args.domain == "trace" and args.command == "validate":
        output = {"valid": True, "events": TraceEmitter.validate_file(args.path)}
    elif args.domain == "trace":
        TraceEmitter(args.path).emit(_read(args.event))
        output = {"emitted": True}
    else:
        output = {"bindings": RuntimeAPI.list_provider_bindings(args.path)}
    print(json.dumps(output, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

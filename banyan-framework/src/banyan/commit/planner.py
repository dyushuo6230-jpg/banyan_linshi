"""Deterministic semantic commit planning without repository mutation."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Mapping

from banyan.git.adapter import GitAdapter


SEMANTIC_CLASSES = {"READY", "INCOMPLETE", "UNRELATED", "LOCAL_ONLY", "SECRET_RISK"}


@dataclass(frozen=True)
class CommitGroup:
    group_id: str
    message: str
    paths: tuple[str, ...]
    patches: tuple[str, ...] = ()
    patch_paths: tuple[str, ...] = ()


@dataclass(frozen=True)
class CommitPlan:
    groups: tuple[CommitGroup, ...]
    classifications: dict[str, str]
    blocked_paths: tuple[str, ...]
    leftovers: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "groups": [asdict(group) for group in self.groups],
            "classifications": dict(self.classifications),
            "blocked_paths": list(self.blocked_paths),
            "leftovers": list(self.leftovers),
        }


class CommitPlanner:
    def __init__(self, adapter: GitAdapter):
        self.adapter = adapter

    def plan(
        self,
        classifications: Mapping[str, str],
        *,
        groups: Mapping[str, str] | None = None,
        messages: Mapping[str, str] | None = None,
    ) -> CommitPlan:
        changed = self.adapter.changed_paths()
        normalized: dict[str, str] = {}
        for path in changed:
            classification = classifications.get(path, "INCOMPLETE")
            if classification not in SEMANTIC_CLASSES:
                raise ValueError(f"unknown semantic classification for {path}: {classification}")
            normalized[path] = classification

        buckets: dict[str, list[str]] = {}
        for path, classification in normalized.items():
            if classification == "READY":
                group_id = (groups or {}).get(path, "commit-1")
                buckets.setdefault(group_id, []).append(path)

        commit_groups = tuple(
            CommitGroup(
                group_id=group_id,
                message=(messages or {}).get(group_id, f"chore: apply {group_id}"),
                paths=tuple(sorted(paths)),
            )
            for group_id, paths in sorted(buckets.items())
        )
        blocked = tuple(sorted(path for path, value in normalized.items() if value == "SECRET_RISK"))
        leftovers = tuple(sorted(path for path, value in normalized.items() if value != "READY"))
        return CommitPlan(commit_groups, normalized, blocked, leftovers)

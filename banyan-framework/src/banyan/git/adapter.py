"""Scope-aware argv-only Git CLI adapter."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from banyan.adapters.process import ProcessResult, ProcessRunner


class GitScopeError(PermissionError):
    pass


class GitCommandError(RuntimeError):
    pass


READ_ONLY = {"status", "diff", "rev-parse", "symbolic-ref", "show", "log", "ls-files"}
MUTATING = {"init", "add", "commit", "reset", "stash", "rebase", "config", "apply"}
NETWORK = {"push", "fetch", "pull", "clone", "ls-remote"}


class GitAdapter:
    def __init__(
        self,
        repository: str | Path,
        *,
        fixture_root: str | Path | None = None,
        runner: ProcessRunner | None = None,
    ):
        self.repository = Path(repository).resolve()
        self.fixture_root = Path(fixture_root).resolve() if fixture_root else None
        self.runner = runner or ProcessRunner()

    @property
    def is_fixture(self) -> bool:
        return bool(
            self.fixture_root
            and (self.repository == self.fixture_root or self.fixture_root in self.repository.parents)
        )

    def run(self, args: Iterable[str], *, mutate: bool = False, input_text: str | None = None) -> ProcessResult:
        parts = tuple(args)
        if not parts:
            raise ValueError("git arguments are required")
        op = parts[0]
        if op in NETWORK:
            raise GitScopeError("network Git operations are disabled")
        if self._is_blind_stage(parts):
            raise GitScopeError("blind staging is forbidden")
        if mutate:
            if not self.is_fixture:
                raise GitScopeError("Git mutation is restricted to the isolated fixture root")
            if op not in MUTATING:
                raise GitScopeError(f"unclassified mutating Git operation: {op}")
            if op == "config" and "--global" in parts:
                raise GitScopeError("global Git configuration is forbidden")
        elif op not in READ_ONLY and op != "config":
            raise GitScopeError(f"operation requires explicit mutating scope: {op}")
        result = self.runner.run(("git", *parts), cwd=self.repository, input_text=input_text)
        if result.returncode != 0:
            raise GitCommandError(result.stderr.strip() or result.stdout.strip())
        return result

    @staticmethod
    def _is_blind_stage(parts: tuple[str, ...]) -> bool:
        return parts[:2] in {("add", "."), ("add", "-A"), ("add", "--all")}

    def inspect(self) -> dict[str, object]:
        root = self.run(("rev-parse", "--show-toplevel")).stdout.strip()
        status = self.run(("status", "--porcelain=v2", "--branch")).stdout.splitlines()
        counts = {"staged": 0, "unstaged": 0, "untracked": 0, "conflicted": 0}
        for line in status:
            if line.startswith("? "):
                counts["untracked"] += 1
            elif line.startswith("u "):
                counts["conflicted"] += 1
            elif line.startswith(("1 ", "2 ")):
                xy = line.split()[1]
                counts["staged"] += int(xy[0] != ".")
                counts["unstaged"] += int(xy[1] != ".")
        return {
            "repository_root": root,
            "head": self.run(("rev-parse", "HEAD")).stdout.strip(),
            "branch": self._branch(),
            "identity_name_present": bool(self._config_value("user.name")),
            "identity_email_present": bool(self._config_value("user.email")),
            "identity_values_recorded": False,
            **counts,
        }

    def _branch(self) -> str:
        try:
            return self.run(("symbolic-ref", "--short", "HEAD")).stdout.strip()
        except GitCommandError:
            return "DETACHED"

    def _config_value(self, key: str) -> str:
        result = self.runner.run(("git", "config", "--get", key), cwd=self.repository)
        return result.stdout.strip() if result.returncode == 0 else ""

    def changed_paths(self) -> list[str]:
        lines = self.run(("status", "--porcelain=v1", "-z")).stdout.split("\0")
        paths: list[str] = []
        for line in lines:
            if not line:
                continue
            paths.append(line[3:])
        return sorted(set(paths))

    def staged_paths(self) -> list[str]:
        raw = self.run(("diff", "--cached", "--name-only", "-z")).stdout
        return sorted(x for x in raw.split("\0") if x)

    def stage_paths(self, paths: Iterable[str]) -> None:
        values = tuple(sorted(set(paths)))
        if not values:
            raise ValueError("explicit stage path set cannot be empty")
        self.run(("add", "--", *values), mutate=True)

    def stage_patch(self, patch: str) -> None:
        if not patch.strip():
            raise ValueError("patch cannot be empty")
        self.run(("apply", "--cached", "--unidiff-zero", "-"), mutate=True, input_text=patch)

    def commit(self, message: str) -> str:
        if not message.strip():
            raise ValueError("commit message cannot be empty")
        self.run(("commit", "-m", message), mutate=True)
        return self.run(("rev-parse", "HEAD")).stdout.strip()


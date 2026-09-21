from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess
from typing import Mapping, Sequence


@dataclass(frozen=True)
class ProcessResult:
    argv: tuple[str, ...]
    returncode: int
    stdout: str
    stderr: str


class ProcessRunner:
    def run(
        self,
        argv: Sequence[str],
        *,
        cwd: str | Path,
        env: Mapping[str, str] | None = None,
        input_text: str | None = None,
        check: bool = False,
    ) -> ProcessResult:
        if not argv or not all(isinstance(x, str) and x for x in argv):
            raise ValueError("argv must be a non-empty string sequence")
        completed = subprocess.run(
            list(argv),
            cwd=Path(cwd),
            env=dict(env) if env is not None else None,
            input=input_text,
            text=True,
            capture_output=True,
            shell=False,
            check=False,
        )
        result = ProcessResult(tuple(argv), completed.returncode, completed.stdout, completed.stderr)
        if check and completed.returncode != 0:
            raise RuntimeError(f"command failed ({completed.returncode}): {result.stderr.strip()}")
        return result


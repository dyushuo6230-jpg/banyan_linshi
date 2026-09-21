from __future__ import annotations

from pathlib import Path


class FilesystemAdapter:
    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()

    def resolve(self, relative: str | Path) -> Path:
        candidate = (self.root / relative).resolve()
        if candidate != self.root and self.root not in candidate.parents:
            raise ValueError("path escapes adapter root")
        return candidate

    def read_text(self, relative: str | Path) -> str:
        return self.resolve(relative).read_text(encoding="utf-8")

    def write_text(self, relative: str | Path, value: str) -> None:
        target = self.resolve(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(value, encoding="utf-8")


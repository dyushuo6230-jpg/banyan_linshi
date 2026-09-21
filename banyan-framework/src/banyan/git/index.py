from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

from .adapter import GitAdapter


@dataclass
class IndexCheckpoint:
    path: Path
    existed: bool
    content: bytes
    digest: str

    @classmethod
    def capture(cls, adapter: GitAdapter) -> "IndexCheckpoint":
        raw_path = adapter.run(("rev-parse", "--git-path", "index")).stdout.strip()
        path = Path(raw_path)
        if not path.is_absolute():
            path = adapter.repository / path
        existed = path.exists()
        content = path.read_bytes() if existed else b""
        return cls(path, existed, content, sha256(content).hexdigest())

    def restore(self, adapter: GitAdapter) -> None:
        if not adapter.is_fixture:
            raise PermissionError("index restore is restricted to fixtures")
        if self.existed:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.write_bytes(self.content)
        elif self.path.exists():
            self.path.unlink()

    def current_digest(self) -> str:
        content = self.path.read_bytes() if self.path.exists() else b""
        return sha256(content).hexdigest()

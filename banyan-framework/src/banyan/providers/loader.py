from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


class ProviderBindingLoader:
    """Load declarative provider bindings; loading never executes providers."""

    def load(self, path: str | Path) -> list[dict[str, Any]]:
        source = Path(path)
        text = source.read_text(encoding="utf-8")
        data = json.loads(text) if source.suffix.lower() == ".json" else yaml.safe_load(text)
        if not isinstance(data, dict) or set(data) != {"bindings"} or not isinstance(data["bindings"], list):
            raise ValueError("provider binding document must contain only a bindings list")
        output: list[dict[str, Any]] = []
        for binding in data["bindings"]:
            if not isinstance(binding, dict) or set(binding) != {"id", "provider", "enabled"}:
                raise ValueError("provider binding fields must be id, provider and enabled")
            if not isinstance(binding["id"], str) or not isinstance(binding["provider"], str) or not isinstance(binding["enabled"], bool):
                raise ValueError("invalid provider binding value")
            output.append(dict(binding))
        return output

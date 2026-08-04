from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "configs" / "config.yaml"


def get_project_root() -> Path:
    return PROJECT_ROOT


def load_config(config_path: str | Path | None = None) -> dict[str, Any]:
    path = Path(config_path) if config_path is not None else DEFAULT_CONFIG_PATH
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def resolve_path(path_value: str | Path, root: str | Path | None = None) -> Path:
    base = Path(root) if root is not None else PROJECT_ROOT
    candidate = Path(path_value)
    return candidate if candidate.is_absolute() else base / candidate


def get_config_path() -> Path:
    return DEFAULT_CONFIG_PATH

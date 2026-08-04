from __future__ import annotations

from pathlib import Path
from typing import Sequence

import torch

from .models import build_model


def load_model(checkpoint_path: str | Path, *, num_classes: int, model_name: str = "baseline_cnn") -> torch.nn.Module:
    model = build_model(model_name, num_classes=num_classes)
    checkpoint = torch.load(checkpoint_path, map_location="cpu")
    state_dict = checkpoint.get("state_dict", checkpoint)
    model.load_state_dict(state_dict)
    model.eval()
    return model


@torch.no_grad()
def predict_top_k(model: torch.nn.Module, batch: torch.Tensor, class_names: Sequence[str], k: int = 3) -> list[tuple[str, float]]:
    logits = model(batch)
    probabilities = torch.softmax(logits, dim=-1)[0]
    values, indices = torch.topk(probabilities, k=min(k, probabilities.shape[0]))
    return [(class_names[int(index)], float(value)) for value, index in zip(values, indices)]

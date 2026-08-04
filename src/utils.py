from __future__ import annotations

import random
from pathlib import Path
from typing import Iterable

import numpy as np
import torch
from sklearn.metrics import f1_score, top_k_accuracy_score


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def macro_f1(y_true: Iterable[int], y_pred: Iterable[int]) -> float:
    return float(f1_score(list(y_true), list(y_pred), average="macro"))


def top3_accuracy(y_true: Iterable[int], y_prob: np.ndarray) -> float:
    return float(top_k_accuracy_score(list(y_true), y_prob, k=3, labels=list(range(y_prob.shape[1]))))


def ensure_directory(path: str | Path) -> Path:
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory

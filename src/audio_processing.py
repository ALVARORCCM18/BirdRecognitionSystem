from __future__ import annotations

from typing import Iterator

import numpy as np


def pad_or_trim_audio(audio: np.ndarray, target_length: int) -> np.ndarray:
    if audio.shape[0] >= target_length:
        return audio[:target_length]
    padding = target_length - audio.shape[0]
    return np.pad(audio, (0, padding), mode="constant")


def sliding_windows(audio: np.ndarray, window_size: int, hop_size: int) -> Iterator[np.ndarray]:
    if window_size <= 0 or hop_size <= 0:
        raise ValueError("window_size and hop_size must be positive")
    if audio.shape[0] == 0:
        yield np.zeros(window_size, dtype=audio.dtype if audio.dtype != object else np.float32)
        return
    for start in range(0, max(audio.shape[0] - window_size + 1, 1), hop_size):
        end = start + window_size
        chunk = audio[start:end]
        if chunk.shape[0] < window_size:
            chunk = pad_or_trim_audio(chunk, window_size)
        yield chunk


def simple_energy_vad(audio: np.ndarray, threshold: float = 0.01) -> np.ndarray:
    if audio.size == 0:
        return audio
    energy = np.abs(audio)
    mask = energy >= threshold
    return audio[mask] if np.any(mask) else audio

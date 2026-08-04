from __future__ import annotations

from pathlib import Path
from typing import Any

import librosa
import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset


class BirdAudioDataset(Dataset):
    def __init__(
        self,
        metadata: pd.DataFrame,
        audio_root: str | Path,
        *,
        filename_column: str = "filename",
        label_column: str = "label",
        sample_rate: int = 32000,
        n_mels: int = 128,
        transforms: Any | None = None,
    ) -> None:
        self.metadata = metadata.reset_index(drop=True)
        self.audio_root = Path(audio_root)
        self.filename_column = filename_column
        self.label_column = label_column
        self.sample_rate = sample_rate
        self.n_mels = n_mels
        self.transforms = transforms

    def __len__(self) -> int:
        return len(self.metadata)

    def _load_audio(self, path: Path) -> np.ndarray:
        audio, _ = librosa.load(path, sr=self.sample_rate, mono=True)
        return audio.astype(np.float32, copy=False)

    def _to_mel_spectrogram(self, audio: np.ndarray) -> torch.Tensor:
        mel = librosa.feature.melspectrogram(y=audio, sr=self.sample_rate, n_mels=self.n_mels)
        mel_db = librosa.power_to_db(mel, ref=np.max)
        tensor = torch.from_numpy(mel_db).unsqueeze(0).float()
        return tensor

    def __getitem__(self, index: int) -> dict[str, Any]:
        row = self.metadata.iloc[index]
        audio_path = self.audio_root / str(row[self.filename_column])
        audio = self._load_audio(audio_path)
        if self.transforms is not None:
            audio = self.transforms(audio)
        spectrogram = self._to_mel_spectrogram(audio)
        item: dict[str, Any] = {"spectrogram": spectrogram, "filename": audio_path.name}
        if self.label_column in row:
            item["label"] = row[self.label_column]
        return item

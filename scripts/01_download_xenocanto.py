import os
from pathlib import Path

from dotenv import load_dotenv
from xcapi.client import XenoCantoClient
from xcapi.downloader import Downloader
from xcapi.query import QueryBuilder


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"
OUTPUT_DIR = PROJECT_ROOT / "data" / "raw"

PILOT_SIZE = 20

load_dotenv(ENV_PATH)


def main() -> None:
    api_key = os.getenv("XENO_CANTO_API_KEY")

    if not api_key:
        raise RuntimeError(
            f"No se encontró XENO_CANTO_API_KEY en {ENV_PATH}"
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    client = XenoCantoClient(api_key=api_key)

    recordings = []

    for quality in ("A", "B"):
        query = (
            QueryBuilder()
            .group("birds")
            .country("Spain")
            .genus("Turdus")
            .species("merula")
            .quality(quality)
            .sound_type("song")
            .build()
        )

        quality_recordings = client.search(query)

        print(
            f"Calidad {quality}: "
            f"{len(quality_recordings)} grabaciones encontradas"
        )

        recordings.extend(quality_recordings)

    print(f"Total de grabaciones A/B: {len(recordings)}")

    pilot_recordings = recordings[:PILOT_SIZE]

    downloader = Downloader(output_dir=str(OUTPUT_DIR))
    downloader.save_metadata_only(pilot_recordings)

    print(
        f"Metadatos de {len(pilot_recordings)} grabaciones "
        f"guardados en {OUTPUT_DIR / 'metadata_only.csv'}"
    )


if __name__ == "__main__":
    main()
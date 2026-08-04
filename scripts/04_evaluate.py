from __future__ import annotations

from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    print(f"Proyecto detectado en: {project_root}")
    print("Implementa aquí la evaluación final y la generación de figuras.")


if __name__ == "__main__":
    main()

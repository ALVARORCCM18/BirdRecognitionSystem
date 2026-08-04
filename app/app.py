from __future__ import annotations


def build_demo() -> None:
    try:
        import gradio as gr
    except ImportError as exc:  # pragma: no cover - runtime guard for missing dependency
        raise SystemExit("Gradio no está instalado. Ejecuta pip install -r requirements.txt.") from exc

    with gr.Blocks(title="BirdRecognitionSystem") as demo:
        gr.Markdown("# BirdRecognitionSystem\nInterfaz base para predicción de aves.")
        gr.Markdown("Añade aquí carga de audio, espectrograma y top-3 de clases.")
    demo.launch()


if __name__ == "__main__":
    build_demo()

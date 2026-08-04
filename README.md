# BirdRecognitionSystem

Estructura base reproducible para un sistema de reconocimiento de aves en audio.

## Estructura

- `configs/`: configuración centralizada y reproducible.
- `data/`: audios, metadatos y splits locales no rastreados por Git.
- `src/`: código importable con utilidades, dataset, modelos e inferencia.
- `scripts/`: pasos de descarga, preprocesado, entrenamiento y evaluación.
- `notebooks/`: exploración y análisis de errores.
- `app/`: interfaz interactiva.
- `models/`: checkpoints finales.
- `reports/`: figuras y evidencias.

## Uso

1. Crear un entorno Python e instalar dependencias.
2. Ajustar `configs/config.yaml`.
3. Ejecutar los scripts desde la raíz del proyecto.

## Notas

La carpeta `data/` se reserva para datos locales descargados o generados.
Los archivos pesados de entrenamiento y las figuras de salida se excluyen del control de versiones.

## Descripción

Una red neuronal entrenada para reconocer el canto de diferentes pájaros.

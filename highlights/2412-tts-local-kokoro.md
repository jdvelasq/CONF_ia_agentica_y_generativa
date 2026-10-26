# TTS local: Kokoro-82M

- Hasta entonces, Whisper / whisper.cpp (2209-model-whisper.md) había consolidado speech-to-text local.
- La clonación de voz y speech-to-speech quedan como capacidades posteriores y distintas.
- Todo el pipeline —modelo y voicepack— se ejecuta en memoria unificada de Apple Silicon, sin llamada de red.

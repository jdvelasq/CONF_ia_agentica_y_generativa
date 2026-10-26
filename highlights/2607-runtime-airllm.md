# AirLLM: ejecutar modelos que no caben en la VRAM

- AirLLM nació en 2023 como una biblioteca de inferencia local de bajo consumo de VRAM.
- No debe leerse como “un modelo de 2,8T se vuelve usable en una GPU de 4 GB”.
- El mismo reporte mide 900 segundos de inicialización y 292 segundos por token, limitado por disco.
- Fuente primaria: release v3.1.0 de AirLLM.
- El código es open source bajo Apache-2.0.

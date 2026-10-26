# ComfyUI

- ComfyUI llevó los flujos de generación de imágenes a una interfaz visual basada en nodos.
- Permite conectar carga de modelos, prompts, muestreo y procesamiento de imágenes en un grafo editable.
- Frente a una interfaz de generación simple, expone y permite reutilizar el pipeline completo.
- La flexibilidad exige entender los modelos, nodos y dependencias del flujo.

ComfyUI es una interfaz visual basada en nodos para componer workflows de modelos generativos (Stable Diffusion y derivados, [2208-model-stable-diffusion.md](2208-model-stable-diffusion.md)), que corre localmente y permite controlar el pipeline paso a paso en vez de sólo generar una imagen con un clic. A diferencia de Draw Things —pensado para generar una imagen rápidamente—, ComfyUI sirve para controlar y componer el pipeline completo, y se extiende más allá de imagen a video, audio y 3D.

# IA generativa y agéntica — prototipo de presentación

Presentación de **tres diapositivas**, en HTML5, CSS y JavaScript nativos, sin Reveal.js ni compilación.

## Organización

- `index.html`: visor único, sin contenido de diapositivas.
- `slides.json`: índice ordenado de los archivos de diapositivas.
- `slides/001-cover.html`: portada fotográfica/abstracta con identificación opcional.
- `slides/002-statement.html`: separador narrativo gris oscuro (`#444444`).
- `slides/003-content.html`: contenido sobre blanco con encabezado casi negro (`#222222`).
- `style.css`: estilos compartidos y paleta Tableau 10.
- `slides.js`: carga y navegación.

Cada archivo de `slides/` contiene un único elemento `<section class="slide ...">` y no duplica el encabezado HTML ni los estilos. El contenido puede organizarse libremente; preguntas, ideas clave y diagramas son opcionales.

## Uso local

Como los archivos se cargan mediante `fetch`, **no basta con abrir `index.html` mediante `file://`**. Desde la raíz del repositorio ejecutar:

```sh
python3 -m http.server 8000
```

Abrir `http://localhost:8000/`. Para publicar, activar **Settings → Pages → Deploy from a branch → main → /(root)** en GitHub.

Navegación: flechas, AvPág/RePág, Inicio/Fin o botones; **F** para pantalla completa. Enlaces directos: `#1`, `#2`, `#3`.

## Añadir o reorganizar diapositivas

1. Crear un archivo HTML en `slides/` con un solo `<section class="slide ...">`.
2. Agregar su nombre en `slides.json` en la posición deseada.
3. Ajustar estilos comunes en `style.css` cuando sea necesario.

## Recursos

- Reemplazar el fondo abstracto provisional de `.cover-photo` por una fotografía propia.
- Guardar la imagen de identificación como `assets/identificacion.png`; mientras no exista, se oculta automáticamente.

Este prototipo permite validar la identidad gráfica y la arquitectura modular antes de producir la presentación completa.

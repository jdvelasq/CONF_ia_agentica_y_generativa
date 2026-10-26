# IA generativa y agéntica — prototipo de presentación

Prototipo de **tres diapositivas**, con HTML5, CSS y JavaScript nativos, sin Reveal.js ni proceso de compilación.

1. **cover** — Portada oscura con fotografía/imagen de fondo sustituible y zona de identificación inferior izquierda.
2. **statement** — Separador narrativo con fondo gris oscuro (`#444444`) y tipografía blanca grande alineada a la derecha.
3. **content** — Franja negra superior y contenido libre sobre blanco; las preguntas, ideas clave y diagramas son recursos opcionales.

## Uso

Abrir `index.html` en el navegador. Navegar con flechas, AvPág/RePág, Inicio/Fin o botones; pulsar **F** para pantalla completa. Las URL admiten `#1`, `#2`, `#3`.

Para publicar, activar **Settings → Pages → Deploy from a branch → main → /(root)** en GitHub.

## Personalización

- Cambiar colores, tipografías y composiciones en `style.css`.
- Editar textos y orden de diapositivas en `index.html`.
- Reemplazar el fondo abstracto temporal de `.cover-photo` por una fotografía de portada propia.
- Incorporar la imagen de identificación del conferencista como `assets/identificacion.png`. Hasta suministrarla, el bloque de imagen se oculta automáticamente.

Este es un **prototipo visual** para validar el estilo antes de decidir un sistema de autoría y producción de diapositivas.

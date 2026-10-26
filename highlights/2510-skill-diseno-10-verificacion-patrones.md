# Agent Skills: producción y verificación

- Una skill puede producir un artifact válido estructuralmente sin que el contenido sea semánticamente correcto.
- Desde el punto de vista de diseño, la validación no tiene que pertenecer a la misma skill que produce el artifact.
- La skill productora puede incluir verificaciones locales básicas.
- Esto mejora separación de responsabilidades, testabilidad, reutilización y trazabilidad.
- Usar un modelo diferente no garantiza por sí solo una validación independiente.

# Agent Skills: fallos y recuperación

- Una skill robusta debe definir qué hacer cuando una ejecución no cumple el contrato esperado.
- Reintentar tiene sentido cuando el fallo puede ser transitorio o corregible.
- Un fallback cambia de mecanismo cuando la ruta principal falla.
- El fallback debe preservar el contrato de salida o declarar claramente una degradación.
- Cuando el sistema no puede resolver el problema con suficiente confianza, debe escalar.

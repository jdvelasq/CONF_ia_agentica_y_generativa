# Agent Skills: descubrimiento y selección

- Este documento cubre cómo un runtime descubre y selecciona una skill entre muchas disponibles.
- La metadata mínima útil para seleccionar una skill suele incluir name.
- El runtime puede mantener en contexto sólo el catálogo liviano (nombre.
- La selección puede ser explícita (el usuario o el runtime nombra la skill).
- Esto reduce consumo de contexto, ruido de routing e interferencia entre skills.

Este documento cubre cómo un runtime descubre y selecciona una skill entre muchas disponibles, un problema que sólo aparece cuando el catálogo de skills crece más allá de un puñado.

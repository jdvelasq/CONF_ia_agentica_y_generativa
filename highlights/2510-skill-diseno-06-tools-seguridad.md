# Agent Skills: tools y seguridad

- No toda capacidad necesaria debe empaquetarse dentro de la skill.
- Si el runtime ya ofrece una capacidad estable, no conviene reimplementarla dentro de cada skill.
- Las operaciones con efectos externos deben quedar preferiblemente detrás de tools controladas por el runtime.
- Esto reduce mantenimiento y mejora consistencia.
- Una tool general puede servir a muchas skills.

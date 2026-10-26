# Claude Code Mods

- Los mods se distribuyen como plugins, pero añaden una tercera capa.
- El módulo exporta register(on, options); cada hook recibe ($, evento, next).
- Algunas funciones propias de Claude Code, entre ellas /diff y el soporte de AGENTS.md, están implementadas como mods.
- Un mod no es un hosted-agent-: no delega una tarea a un bucle de agente operado como servicio por un proveedor.

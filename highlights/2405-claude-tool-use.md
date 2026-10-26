# Claude: tool use

- MCP (2411-mcp.md) estandariza después cómo se exponen las tools entre agentes y servidores.
- Una tool se define con tres campos: name, description e input_schema (JSON Schema).
- Claude decide por sí mismo cuándo usarla y responde con un bloque tool_use.
- Claude también puede consumir tools expuestas vía MCP.
- Si Claude decide usar la tool, devuelve conceptualmente tool_use → name.

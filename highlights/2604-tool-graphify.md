# Graphify

- No es un modelo ni un harness: es una capa de indexación estructural que se instala junto a un coding agent.
- El grafo puede consultarse después sin reconstruir todo el contexto.
- Para código usa un AST vía tree-sitter: extracción determinista, sin LLM, nada sale del equipo.
- Docs, PDFs, imágenes y video sí pueden requerir un backend semántico configurado aparte.
- A diferencia del RAG vectorial, que recupera por similitud semántica.

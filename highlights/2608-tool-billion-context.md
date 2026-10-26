# Billion Context

- El proxy entiende formatos Anthropic y OpenAI y reescribe el flujo para introducir gestión explícita del contexto.
- La afirmación "billion context" no significa que el modelo adquiera una ventana física de miles de millones de tokens.
- La ventana real puede seguir siendo ~100K-200K.
- No se limita a truncar mensajes antiguos.
- El diseño intenta preservar el prefix cache evitando reescribir continuamente todo el prefijo.

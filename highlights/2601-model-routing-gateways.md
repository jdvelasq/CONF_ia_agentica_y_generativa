# Model routing y gateways: Claude Code sobre OpenRouter

- Este cambio prepara conceptos posteriores como model routers, gateways.
- El antecedente directo de la idea "capa intermedia que desacopla cliente de proveedor" es 2307-gateway-litellm.md.
- Un harness de código puede desacoplarse del proveedor y, en ciertos casos, del modelo que usa como backend.
- El caso concreto de esta nota es conectar Claude Code, a través de un endpoint compatible.
- La idea central es que harness ≠ modelo: Claude Code puede seguir siendo la interfaz, el runtime y el agente de código.

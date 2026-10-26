# TurboFieldfare

- TurboFieldfare está diseñado específicamente para Gemma 4 26B-A4B IT.
- No es un wrapper de MLX ni llama.cpp: implementa su propio runtime y kernels Metal.
- Esto explota directamente la sparsity del MoE.
- La instalación text-only ocupa aproximadamente 14,3 GB.
- El runtime reduce el working set residente, no el tamaño lógico del checkpoint.

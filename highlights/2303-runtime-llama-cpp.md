# llama.cpp

- Antes de este hito, correr un modelo de ese tamaño requería GPU y el stack completo de un framework de deep learning.
- Al ser C/C++ puro, corre en CPU, Apple Silicon (Metal), GPUs NVIDIA (CUDA) y otros backends con el mismo código base.
- La limitación es que es una herramienta de bajo nivel.
- En Apple Silicon, Metal se activa por defecto en este build.

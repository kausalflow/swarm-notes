---
created_at: '2026-03-25T21:18:00Z'
source_papers:
- '[[2603.23491-foveated-diffusion-efficient-spatially-adaptive-image-and-vi]]'
title: Extend to multiple foveation levels
---

**Background:** General frameworks for spatially adaptive generation benefit from support for varying degrees of resolution sparsification.

**Question / Future Work:** The current framework uses a spatial downsampling factor of $d=2$ (a $4\times 4$ computational gain in the periphery). Future work could explore extending the framework to support multiple levels of foveation, necessitating multi-level adaptation of phase-aligned Rotary Positional Embeddings (RoPE).
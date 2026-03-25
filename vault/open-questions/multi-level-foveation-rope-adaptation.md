---
source_papers:
- '[[2603.23491-foveated-diffusion-efficient-spatially-adaptive-image-and-vi]]'
title: Extend to Multi-Level Foveation
---

**Background:** The current framework utilizes a spatial downsampling factor of $d=2$, resulting in two resolution levels (high and low). Traditional foveated rendering systems can employ even coarser peripheral resolutions.

**Question / Future Work:** Future work should explore extending the current general framework to support multiple levels of foveation (more than two resolution levels) and adapt the phase-aligned Rotary Positional Embeddings (RoPE) mechanism to accommodate this multi-level token structure.
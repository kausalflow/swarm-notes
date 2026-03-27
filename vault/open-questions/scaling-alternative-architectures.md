---
created_at: '2026-03-27T09:10:10Z'
source_papers:
- '[[2603.25687-on-neural-scaling-laws-for-weather-emulation-through-continu]]'
title: Scaling Alternative Architectures
---

**Background:** Neural scaling laws are typically derived by training models from scratch for each point in the compute budget, which is computationally expensive. A novel approach involves using continual training with a constant learning rate followed by a cooldown period to construct IsoFLOP curves efficiently.

**Question / Future Work:** The primary limitation is the focus on a single, minimalist Transformer architecture (Swin Transformer) without domain-specific modifications. Future work should explore how neural scaling laws manifest in models incorporating geometric inductive biases, such as those based on Neural Operators (e.g., FourCastNet) or graph-based approaches (e.g., GraphCast).
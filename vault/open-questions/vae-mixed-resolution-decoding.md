---
created_at: '2026-03-25T21:18:00Z'
source_papers:
- '[[2603.23491-foveated-diffusion-efficient-spatially-adaptive-image-and-vi]]'
title: Redesign VAE for mixed-resolution tokens
---

**Background:** Diffusion models can produce occasional visual artifacts, particularly at the boundaries where different resolution features are combined during generation.

**Question / Future Work:** The blending of VAE-decoded low-resolution and high-resolution content near the foveation boundary can lead to noticeable color or discontinuity artifacts, suggesting a need to modify the autoencoder to support mixed-resolution tokens natively.
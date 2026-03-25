---
source_papers:
- '[[2603.23491-foveated-diffusion-efficient-spatially-adaptive-image-and-vi]]'
title: Redesign VAE for Mixed-Resolution Tokens
---

**Background:** Foveated generation methods introduce color or discontinuity artifacts near the boundaries where high-resolution and low-resolution decoded content is blended.

**Question / Future Work:** A promising future direction involves redesigning the Variational Autoencoder (VAE) component to directly encode and decode mixed-resolution tokens, which is hypothesized to mitigate the artifacts that arise from the current separate decoding and subsequent alpha-blending steps.
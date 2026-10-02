---
# CSL-compatible fields
title: "Generative diffusion models for spatiotemporal influenza forecasting"
author:
  - literal: "Joseph Chadi Lemaitre"
  - literal: "Justin Lessler"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2604.24913"

# Custom fields
paper_id: "2604.24913"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "generative-adversarial-network"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "influpaint"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:47:16Z"
created_at: "2026-10-02T10:47:16Z"
---

# Generative diffusion models for spatiotemporal influenza forecasting

**Authors**: Joseph Chadi Lemaitre, Justin Lessler
**Date**: 2026-09-30
**Paper ID**: [openalex:2604.24913](https://arxiv.org/abs/2604.24913)

## Summary

The paper introduces Influpaint, a generative diffusion model that adapts denoising diffusion probabilistic models for spatiotemporal influenza forecasting by treating epidemic seasons as images. By formulating forecasting as conditional inpainting from partial observations using a hybrid dataset of surveillance and simulated trajectories, the approach captures complex multimodal uncertainty and emergent trends. In evaluations including the 2023-2025 U.S. CDC FluSight challenges, Influpaint achieves forecast accuracy competitive with leading ensemble methods.

## Key Contributions

- Introduces Influpaint, adapting denoising diffusion probabilistic models for spatiotemporal infectious disease forecasting by encoding seasons as images.
- Formulates epidemic forecasting as a conditional generation (inpainting) task from partial observations, handling multimodal uncertainty.
- Demonstrates competitive forecast accuracy compared to leading ensemble methods and evaluates performance in real-time during the 2023-2025 U.S. CDC FluSight challenges.

## Limitations

Projections were somewhat overconfident in the 2024-2025 evaluation season.

## Open Questions & Future Work

- [[direct-conditional-diffusion-forecasting]]

## Key Concepts

- [[influpaint]]: A diffusion model adapted for spatiotemporal epidemic forecasting by treating influenza seasons as images and formulating forecasting as conditional inpainting.

## Archivist Review

Approved the core model concept 'Influpaint' as a distinct spatiotemporal diffusion framework and the open question regarding direct conditional diffusion training. Adhered strictly to the scarcity policy and verification rules.

### Approved Concepts
- Influpaint: It is the core model architecture and methodological novelty introduced in the paper, adapting denoising diffusion probabilistic models for spatiotemporal epidemic forecasting.

### Approved Open Questions
- Direct Conditional Diffusion Training: Transitioning from generation-time inpainting to direct conditional diffusion training is a key architectural frontier for improving task-specific predictive accuracy and reducing potential inefficiencies in spatiotemporal disease forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2604.24913)
- [PDF](https://arxiv.org/pdf/2604.24913)


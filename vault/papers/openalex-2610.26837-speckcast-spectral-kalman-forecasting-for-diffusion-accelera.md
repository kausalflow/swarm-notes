---
# CSL-compatible fields
title: "SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration"
author:
  - literal: "Javad Rajabi"
  - literal: "Hakkı Can Karaimer"
  - literal: "David B. Lindell"
  - literal: "Babak Taati"
  - literal: "Michael S. Brown"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26837"

# Custom fields
paper_id: "2610.26837"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "transformer"
  - "efficient-transformer"
  - "model-compression"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "speckcast"
  - "spectral-kalman-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:44:14Z"
created_at: "2026-10-22T09:44:14Z"
---

# SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration

**Authors**: Javad Rajabi, Hakkı Can Karaimer, David B. Lindell, Babak Taati, Michael S. Brown
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26837](https://arxiv.org/abs/2610.26837)

## Summary

Diffusion Transformers suffer from high computational overhead due to numerous sequential denoising steps, while existing caching and forecasting methods fail to account for frequency-specific and non-uniform temporal feature changes. The authors propose SpecKCast, a training-free framework that applies a 2D discrete cosine transform (DCT) to model outputs and tracks each frequency coefficient via lightweight Kalman filters along band-specific time coordinates. By triggering transformer evaluations only when forecast uncertainty exceeds a threshold, SpecKCast achieves up to a 6x speedup across image and video generation models like FLUX.1-dev, Qwen-Image, Wan2.1-14B, and HunyuanVideo with minimal memory overhead.

## Key Contributions

- Proposes SpecKCast, a training-free frequency-domain forecasting method to accelerate diffusion transformers by bypassing redundant transformer evaluations.
- Applies a 2D discrete cosine transform (DCT) and tracks each coefficient using a lightweight Kalman filter along band-specific time coordinates derived from the noise schedule.
- Demonstrates up to 6x inference speedup on state-of-the-art models like FLUX.1-dev, Qwen-Image, Wan2.1-14B, and HunyuanVideo while maintaining high generation fidelity and requiring less than 0.05 GiB of additional memory.

## Open Questions & Future Work

- [[joint-spatial-temporal-redundancy-exploitation]]

## Key Concepts

- [[speckcast]]: A training-free diffusion acceleration method that forecasts features in the frequency domain using lightweight Kalman filters tracking band-specific time coordinates.
- [[spectral-kalman-forecasting]]: A forecasting technique that tracks discrete cosine transform coefficients with Kalman filters along band-specific time coordinates to accelerate diffusion generation.

## Archivist Review

Approved overarching conceptual contributions (SpecKCast and Spectral Kalman Forecasting) and one explicit open question regarding joint spatial-temporal redundancy exploitation. Rejected specific model names (FLUX.1-dev, Qwen-Image, etc.) as they are routine backbone architectures and evaluation instances rather than reusable algorithmic vault concepts.

### Approved Concepts
- SpecKCast: It introduces spectral Kalman forecasting for accelerating diffusion models by predicting feature trajectories in the frequency domain.
- Spectral Kalman Forecasting: Combines frequency-domain transformation with Kalman filtering to handle non-uniform noise schedules and band-specific temporal variations in diffusion models.

### Approved Open Questions
- Joint Spatial-Temporal Redundancy Exploitation: Combines spatial and temporal optimization to overcome current bottlenecks in diffusion transformer acceleration, potentially unlocking significantly higher speedups.

### Rejected Candidates
- [concept] FLUX.1-dev (`flux-1-dev`) - not_reusable: Model name/benchmark instance rather than a foundational algorithmic concept.
- [concept] Qwen-Image (`qwen-image`) - not_reusable: Model name/benchmark instance rather than a foundational algorithmic concept.
- [concept] Wan2.1-14B (`wan2-1-14b`) - not_reusable: Model name/benchmark instance rather than a foundational algorithmic concept.
- [concept] HunyuanVideo (`hunyuanvideo`) - not_reusable: Model name/benchmark instance rather than a foundational algorithmic concept.

## Links

- [Abstract](https://arxiv.org/abs/2610.26837)
- [PDF](https://arxiv.org/pdf/2610.26837)


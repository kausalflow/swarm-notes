---
# CSL-compatible fields
title: "Towards Scalable One-Step Generative Modeling for Autoregressive Dynamical System Forecasting"
author:
  - literal: "Tianyue Yang"
  - literal: "Xiao Xue"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05540"

# Custom fields
paper_id: "2605.05540"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "generative-adversarial-network"
  - "autoregressive"
  - "efficient-transformer"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "melisa-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:21:47Z"
created_at: "2026-05-10T07:21:47Z"
---

# Towards Scalable One-Step Generative Modeling for Autoregressive Dynamical System Forecasting

**Authors**: Tianyue Yang, Xiao Xue
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05540](https://arxiv.org/abs/2605.05540)

## Summary

MeLISA is a latent-free autoregressive generative surrogate designed for efficient and statistically consistent forecasting of high-dimensional physical dynamics. By utilizing a blockwise stochastic transition kernel, the model performs one-step generation at inference, bypassing the computational overhead of iterative diffusion solvers or latent compression. The approach is further stabilized by a Window-Consistency MeanFlow objective and a Time Increment Consistency loss, ensuring long-term preservation of turbulent statistics like energy spectra. Evaluation on high-resolution flow benchmarks shows that MeLISA outperforms standard neural operators in both short-term accuracy and long-horizon dynamical fidelity at competitive inference speeds.

## Key Contributions

- Introduced MeLISA, a latent-free autoregressive generative surrogate that uses a blockwise stochastic transition kernel for efficient, single-step inference.
- Proposed Window-Consistency MeanFlow objective and Time Increment Consistency loss to stabilize long-horizon rollouts and preserve turbulent statistical structure.
- Demonstrated superior long-horizon statistical fidelity (energy spectra, turbulent kinetic energy) compared to neural operator baselines on 2D Kolmogorov and turbulent channel-flow benchmarks.

## Open Questions & Future Work

- [[scaling-generative-surrogates-to-3d-systems]]

## Key Concepts

- [[melisa-model]]: A latent-free autoregressive generative surrogate for spatiotemporal dynamics that uses a blockwise stochastic transition kernel for single-pass inference.

## Archivist Review

I approved MeLISA as a central conceptual contribution for its novel one-step generative autoregressive architecture and the associated consistency objectives. The open question regarding 3D scaling was approved as it represents a fundamental, non-trivial limitation for high-dimensional spatiotemporal forecasting. Routine benchmarks like Kolmogorov flow were excluded as they are standard domain datasets, not novel methodology.

### Approved Concepts
- MeLISA (MeanFlow Long-term Invariant Spatiotemporal Consistency Autoregressive Models): MeLISA introduces a latent-free, single-step generative approach for long-horizon forecasting of high-dimensional physical dynamics, offering a significant alternative to traditional neural operators and iterative diffusion models.

### Approved Open Questions
- Scaling generative surrogates to 3D: Scaling to 3D is a critical bottleneck for surrogate modeling to transition from 2D slices to reliable full-volume physical simulations.

## Links

- [Abstract](https://arxiv.org/abs/2605.05540)
- [PDF](https://arxiv.org/pdf/2605.05540)


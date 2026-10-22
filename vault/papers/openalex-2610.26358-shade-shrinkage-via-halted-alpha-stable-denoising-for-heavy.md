---
# CSL-compatible fields
title: "SHADE: Shrinkage via Halted Alpha-stable Denoising for Heavy-Tailed Probabilistic Time Series Forecasting"
author:
  - literal: "Jiahao Weng"
  - literal: "Jiyu Liu"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26358"

# Custom fields
paper_id: "2610.26358"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "probabilistic-forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "shade"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:43:19Z"
created_at: "2026-10-22T09:43:19Z"
---

# SHADE: Shrinkage via Halted Alpha-stable Denoising for Heavy-Tailed Probabilistic Time Series Forecasting

**Authors**: Jiahao Weng, Jiyu Liu
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26358](https://arxiv.org/abs/2610.26358)

## Summary

The paper introduces SHADE, an alpha-stable Lévy diffusion forecaster designed for probabilistic time series forecasting under heavy-tailed and time-varying noise. By halting denoising at a nonzero depth, SHADE uses a residual stable kernel for distribution-level shrinkage, avoiding the overconfidence typical of Gaussian diffusion models in low-SNR settings. Evaluations show substantial improvements in tail calibration and CRPS under extreme heavy-tailed noise regimes.

## Key Contributions

- Proposes SHADE, an alpha-stable Lévy diffusion forecaster that stops at a nonzero depth to provide distribution-level shrinkage via a residual stable kernel.
- Develops a scale-calibrated halt and a context-amortized halt by decomposing halting risk into smoothing bias and estimation error.
- Improves median CRPS by 21.7% and NLL significantly in extreme heavy-tailed noise regimes (alpha <= 1.3), while maintaining strong baseline performance.

## Open Questions & Future Work

- [[multivariate-multistep-joint-tail-calibration]]

## Key Concepts

- [[shade]]: An alpha-stable Lévy diffusion forecaster that uses halted denoising for robust probabilistic time series forecasting under heavy-tailed noise.

## Archivist Review

Approved the core methodological concept SHADE and the open question regarding joint tail calibration and multi-step extension, applying strict standards of novelty and reusability for the knowledge vault.

### Approved Concepts
- SHADE: Introduces a novel alpha-stable Lévy diffusion forecaster with halted denoising to address heavy-tailed noise and overconfident predictions.

### Approved Open Questions
- Multivariate and Multi-step Joint Tail Calibration: Moving beyond marginal CDF calibration to handle multivariate joint distributions and complex multi-step dependency structures is a crucial open challenge for probabilistic time-series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2610.26358)
- [PDF](https://arxiv.org/pdf/2610.26358)


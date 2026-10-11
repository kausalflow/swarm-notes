---
# CSL-compatible fields
title: "Just Weather Scoring: Efficient End-to-end Nowcasting with Distributional Diffusion"
author:
  - literal: "Jannik Wiese"
  - literal: "Johannes Schusterbauer"
  - literal: "Tommaso Martorella"
  - literal: "Björn Ommer"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.12189"

# Custom fields
paper_id: "2610.12189"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "spatiotemporal"
  - "forecasting"
  - "benchmark"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "just-weather-scoring"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-11T11:05:00Z"
created_at: "2026-10-11T11:05:00Z"
---

# Just Weather Scoring: Efficient End-to-end Nowcasting with Distributional Diffusion

**Authors**: Jannik Wiese, Johannes Schusterbauer, Tommaso Martorella, Björn Ommer
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.12189](https://arxiv.org/abs/2610.12189)

## Summary

Just Weather Scoring (JWS) is an end-to-end single-stage diffusion model for probabilistic precipitation nowcasting that operates directly in radar space to avoid lossy compression and achieve rapid few-step generation. By combining Masked Asynchronous Diffusion with a scoring-rule objective, JWS sets a new state-of-the-art on the SEVIR and MeteoNet benchmarks while achieving over 17x faster inference than existing diffusion baselines.

## Key Contributions

- Introduces Just Weather Scoring (JWS), a single-stage end-to-end diffusion model for probabilistic precipitation nowcasting operating directly in radar space.
- Combines Masked Asynchronous Diffusion with a scoring-rule objective to enable few-step generation and eliminate lossy compression uncertainty.
- Achieves state-of-the-art probabilistic forecasting performance on SEVIR and MeteoNet benchmarks while being over 17x faster at inference.

## Key Concepts

- [[just-weather-scoring]]: A single-stage, end-to-end diffusion model for probabilistic precipitation nowcasting operating directly in radar space with few-step generation.

## Archivist Review

Approved the primary core concept 'just-weather-scoring' representing the single-stage radar-space diffusion forecasting framework. Rejected the open question as generic scaling and overfitting future work. No datasets were approved since SEVIR and MeteoNet are already tracked in the vault.

### Approved Concepts
- Just Weather Scoring: Introduces a novel single-stage end-to-end diffusion framework for precipitation nowcasting operating directly in radar space.

### Rejected Candidates
- [open_question] Data Scaling and Overfitting (`data-scaling-and-overfitting-in-weather-nowcasting`) - low_impact: Generic future work on data scaling and overfitting that applies to nearly any generative model rather than a specific unresolved spatiotemporal forecasting bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.12189)
- [PDF](https://arxiv.org/pdf/2610.12189)


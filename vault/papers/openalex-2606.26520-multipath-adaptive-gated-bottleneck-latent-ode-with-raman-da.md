---
# CSL-compatible fields
title: "Multipath Adaptive Gated Bottleneck Latent ODE with Raman Data Fusion for Cell Culture Process Forecasting"
author:
  - literal: "Johnny peng"
  - literal: "Thanh Tung Khuat"
  - literal: "Ellen Otte"
  - literal: "Katarzyna Musial"
  - literal: "Bogdan Gabryś"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.26520"

# Custom fields
paper_id: "2606.26520"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
  - "state-space-model"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "gated-bottleneck-latent-ode"
  - "multi-path-jit-fine-tuning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:16:30Z"
created_at: "2026-06-28T08:16:30Z"
---

# Multipath Adaptive Gated Bottleneck Latent ODE with Raman Data Fusion for Cell Culture Process Forecasting

**Authors**: Johnny peng, Thanh Tung Khuat, Ellen Otte, Katarzyna Musial, Bogdan Gabryś
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.26520](https://arxiv.org/abs/2606.26520)

## Summary

This paper addresses the challenge of long-term bioprocess forecasting where sparse, irregular measurements and non-linear process divergence make prediction difficult. The authors introduce a GB-Latent ODE architecture for efficient feature compression under limited data and the MP-JIT-FT framework to generate multiple plausible future paths by clustering historical trajectories. By fusing high-density Raman spectroscopy data as pseudo-observations, the model significantly outperforms global Latent ODE baselines on multi-day bioreactor runs. Experiments across diverse fed-batch conditions demonstrate that this approach is particularly effective when early run dynamics are representative of future states.

## Key Contributions

- Proposes the GB-Latent ODE architecture, which improves forecast performance on sparse bioprocessing data via learnable variable-wise gating and mask-aware bottlenecks.
- Introduces MP-JIT-FT for generating multi-path forecasts by fine-tuning models on clustered historical regimes, effectively capturing process divergence.
- Demonstrates the efficacy of fusing Raman spectroscopy data via a soft-sensor, improving prediction robustess across 38 fed-batch bioreactor runs.

## Open Questions & Future Work

- [[adaptive-pseudo-observation-weighting]]
- [[automated-hyperparameter-tuning-for-jitl]]

## Key Concepts

- [[gated-bottleneck-latent-ode]]: A Latent ODE variant that utilizes learnable variable-wise gating and a mask-aware bottleneck to effectively compress sparse, high-dimensional input sequences.
- [[multi-path-jit-fine-tuning]]: A retrieval-augmented regime-switching forecasting framework that fine-tunes local models on clustered historical trajectories to generate non-deterministic multi-path predictions.

## Archivist Review

I approved the GB-Latent ODE and Multi-Path JIT fine-tuning as they represent generalizable frameworks for tackling sparse, irregular, and divergent forecasting problems. I also approved two open questions that specifically target the identified bottlenecks of soft-sensor data integration and the lack of automation in adaptive forecasting pipelines, which are significant challenges in the field. All other candidates were rejected as they were either local implementations or routine extensions.

### Approved Concepts
- Gated Bottleneck Latent ODE: It provides a systematic architecture for handling irregular, sparse time-series in low-data regimes by combining gating and bottleneck mechanisms with continuous-time dynamics.
- Multi-Path Just-In-Time Fine-Tuning: It addresses the problem of manifold divergence where identical early history can lead to non-deterministic futures, a key challenge in complex industrial process forecasting.

### Approved Open Questions
- Adaptive pseudo-observation weighting: Incorrect weighting of sensor data can bias latent dynamics and degrade predictive performance, particularly in irregular, low-data time-series scenarios.
- Automated hyperparameter tuning for JITL: Manual hyperparameter tuning limits the robustness and transferability of adaptive models to new operating regimes or diverse experimental datasets.

## Links

- [Abstract](https://arxiv.org/abs/2606.26520)
- [PDF](https://arxiv.org/pdf/2606.26520)


---
# CSL-compatible fields
title: "Liquid Latent State Dynamics for Interpretable Turbofan Degradation Modeling"
author:
  - literal: "Weizhi Nie"
  - literal: "Weijie Wang"
  - literal: "Y W Su"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.01986"

# Custom fields
paper_id: "2607.01986"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "interpretability"
  - "anomaly-detection"
architectures:
  []
datasets:
  - "C-MAPSS"
concept_slugs:
  - "liquid-latent-state-dynamics"
dataset_slugs:
  - "c-mapss"
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:52:47Z"
created_at: "2026-07-05T07:52:47Z"
---

# Liquid Latent State Dynamics for Interpretable Turbofan Degradation Modeling

**Authors**: Weizhi Nie, Weijie Wang, Y W Su
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.01986](https://arxiv.org/abs/2607.01986)

## Summary

This paper presents a liquid neural network-based latent dynamics model for turbofan engine degradation, designed to improve interpretability in prognostics. By factorizing latent states into distinct degradation and operating-condition components using specific supervision and decorrelation losses, the model achieves superior sensor forecasting accuracy on the C-MAPSS benchmark. The results indicate that while the proposed representation excels as an interpretable world model for degradation dynamics, it provides a trade-off in direct remaining-useful-life regression performance compared to standard GRU baselines.

## Key Contributions

- Proposes a liquid latent state dynamics model for turbofan degradation that disentangles health evolution from operating condition variations.
- Demonstrates that the disentangled latent representation improves sensor forecasting RMSE (0.2266) on the C-MAPSS FD001-FD004 benchmarks compared to a standard GRU baseline.
- Achieves an interpretable degradation axis with an average state-speed Spearman correlation of 0.5960, outperforming conventional black-box latent representations in health-state monitoring.

## Open Questions & Future Work

- [[improving-rul-calibration-in-latent-models]]
- [[enhancing-latent-state-disentanglement]]

## Key Concepts

- [[liquid-latent-state-dynamics]]: A latent dynamics framework using liquid neural networks to factorize and model time-series health degradation separately from operating conditions.

## Archivist Review

I approved the liquid latent state dynamics concept and the associated C-MAPSS dataset as they represent a notable contribution to interpretable prognostic modeling. The open questions were approved because they specifically address the technical trade-offs between representation learning and regression calibration, as well as the fundamental challenges of latent disentanglement in time-series dynamics. I applied a strict filter to ensure these notes remain focused on methodologies with broad applicability rather than paper-specific implementation details.

### Approved Concepts
- Liquid Latent State Dynamics: Introduces a factorized latent space architecture for time-series forecasting that specifically isolates degradation processes from operational variations.

### Approved Open Questions
- Improving RUL calibration in latent models: The performance gap in RUL regression is a primary limitation preventing the model from acting as a fully calibrated prognostic estimator rather than just an interpretable world model.
- Enhancing latent state disentanglement: Persistence of information leakage confirms the imperfection of the current disentanglement strategy, which limits the purity of the learned degradation state for interpretability.

## Datasets

- [[c-mapss]]

## Links

- [Abstract](https://arxiv.org/abs/2607.01986)
- [PDF](https://arxiv.org/pdf/2607.01986)


---
# CSL-compatible fields
title: "ATEMPO: Amortized Transfer Entropy Model Per-lag Over-Time"
author:
  - literal: "Emma Andrews"
  - literal: "Konstantinos Kontras"
  - literal: "Keane Ong"
  - literal: "Maarten De Vos"
  - literal: "Gianmarco Mengaldo"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.36536"

# Custom fields
paper_id: "2610.36536"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:05:28Z"
created_at: "2026-10-30T11:05:28Z"
---

# ATEMPO: Amortized Transfer Entropy Model Per-lag Over-Time

**Authors**: Emma Andrews, Konstantinos Kontras, Keane Ong, Maarten De Vos, Gianmarco Mengaldo
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.36536](https://arxiv.org/abs/2610.36536)

## Summary

The authors propose ATEMPO, a diffusion-based transfer entropy estimator that is amortized over source/conditioning lags and time to recover time-varying information delays without requiring multiple separate fits. By explicitly conditioning on temporal position and sampling depths during training, ATEMPO efficiently estimates the full transfer entropy surface. Experiments on synthetic benchmarks, WEATHER-5K, and brain-computer interface tasks demonstrate superior lag-detection accuracy and improved downstream forecasting performance.

## Key Contributions

- Introduces ATEMPO, a diffusion-based transfer entropy estimator amortized over source/conditioning depths and temporal position to estimate the full TE surface in a single fit.
- Achieves 0.98 lag-detection accuracy on synthetic datasets with known lags and maintains perfect accuracy across varying window lengths on time-varying lag systems.
- Reduces MSE on WEATHER-5K by 7.25% using ATEMPO-selected inputs, outperforming the 240-feature default with only 120 features.
- Improves mean R^2 by 4.1% over competing baselines across three brain-computer interface tasks by leveraging recovered delays.

## Open Questions & Future Work

- [[joint-multivariate-transfer-entropy-amortization]]

## Archivist Review

The paper introduces ATEMPO, a novel diffusion-based amortized transfer entropy estimator. While well-designed, ATEMPO itself is specific to this paper, whereas the open question regarding joint multivariate transfer entropy amortization provides a clear, high-value technical bottleneck for future research. No concepts or datasets qualified for permanent standalone vault notes under our strict selection criteria.

### Approved Open Questions
- Joint Variable and Lag Selection: Extending amortized score-based transfer entropy estimators from pairwise interactions to joint multivariate conditioning represents a crucial step toward scalable, end-to-end causal discovery and variable selection in high-dimensional dynamical systems.

### Rejected Candidates
- [concept] ATEMPO: Amortized Transfer Entropy Model Per-lag Over-Time (`atempo`) - paper_local: ATEMPO is a paper-specific model and framework implementation rather than a general foundational mechanism or architectural primitive that recurs across papers.

## Links

- [Abstract](https://arxiv.org/abs/2610.36536)
- [PDF](https://arxiv.org/pdf/2610.36536)


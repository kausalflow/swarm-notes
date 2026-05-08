---
# CSL-compatible fields
title: "Training-Free Probabilistic Time-Series Forecasting with Conformal Seasonal Pools"
author:
  - literal: "Valery Manokhin"
issued:
  date-parts:
    - [2026, 5, 5]
url: "https://arxiv.org/abs/2605.03789"

# Custom fields
paper_id: "2605.03789"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "conformal-prediction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "conformal-seasonal-pools-csp"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-08T06:27:00Z"
created_at: "2026-05-08T06:27:00Z"
---

# Training-Free Probabilistic Time-Series Forecasting with Conformal Seasonal Pools

**Authors**: Valery Manokhin
**Date**: 2026-05-05
**Paper ID**: [openalex:2605.03789](https://arxiv.org/abs/2605.03789)

## Summary

The paper introduces Conformal Seasonal Pools (CSP), a training-free probabilistic forecasting framework that produces well-calibrated prediction intervals by combining seasonal empirical data with signed residual sampling. CSP significantly improves upon the calibration of learned non-parametric models like DeepNPTS, which often fail to maintain nominal coverage in safety-critical settings. Experimental results across six major time-series benchmarks demonstrate that CSP provides superior reliability and computational efficiency without requiring any training or learned parameters.

## Key Contributions

- Introduces Conformal Seasonal Pools (CSP), a training-free method for probabilistic time-series forecasting that relies on seasonal empirical draws and signed residual sampling.
- Demonstrates that CSP-Adaptive significantly outperforms DeepNPTS across six standard benchmarks (electricity, exchange_rate, solar_energy, taxi, traffic, wikipedia) in CRPS, quantile loss, and coverage calibration.
- Achieves 500x faster CPU inference than DeepNPTS while maintaining superior prediction interval coverage, essential for high-stakes decision-critical applications.

## Open Questions & Future Work

- [[finite-sample-conformal-validity-timeseries]]

## Key Concepts

- [[conformal-seasonal-pools-csp]]: A training-free probabilistic forecasting method that generates prediction intervals by combining seasonal historical draws with signed residuals.

## Archivist Review

Approved Conformal Seasonal Pools (CSP) as a novel training-free baseline, and the open question regarding finite-sample conformal validity as a fundamental theoretical challenge in time-series forecasting. Rejected the datasets as they are common, well-established benchmarks rather than unique or proprietary findings.

### Approved Concepts
- Conformal Seasonal Pools (CSP): It provides a robust, training-free, and computationally efficient alternative to complex neural probabilistic forecasters, setting a new bar for calibration-first forecasting baselines.

### Approved Open Questions
- Finite-sample Conformal Validity: The lack of formal coverage guarantees is a primary bottleneck for deploying probabilistic time-series forecasting in high-stakes environments where calibration failure can have severe safety consequences.

### Rejected Candidates
- [dataset] electricity (`electricity`) - not_novel: Routine, generic time-series benchmark dataset used in many papers.
- [dataset] traffic (`traffic`) - not_novel: Routine, generic time-series benchmark dataset used in many papers.

## Links

- [Abstract](https://arxiv.org/abs/2605.03789)
- [PDF](https://arxiv.org/pdf/2605.03789)


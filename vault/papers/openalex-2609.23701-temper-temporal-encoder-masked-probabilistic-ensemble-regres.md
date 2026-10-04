---
# CSL-compatible fields
title: "TEMPER: Temporal Encoder-Masked Probabilistic Ensemble Regressor for Time-Series Forecasting"
author:
  - literal: "Giancarlo Vercellino"
issued:
  date-parts:
    - [2026, 10, 2]
url: "https://arxiv.org/abs/2609.23701"

# Custom fields
paper_id: "2609.23701"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "probabilistic-forecast"
  - "autoencoder"
  - "uncertainty"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:48:06Z"
created_at: "2026-10-04T10:48:06Z"
---

# TEMPER: Temporal Encoder-Masked Probabilistic Ensemble Regressor for Time-Series Forecasting

**Authors**: Giancarlo Vercellino
**Date**: 2026-10-02
**Paper ID**: [openalex:2609.23701](https://arxiv.org/abs/2609.23701)

## Summary

TEMPER is a univariate probabilistic time-series forecasting algorithm that merges a temporal autoencoder, a differentiable masked neural decision forest, continuous ranked probability score (CRPS) training, and Gaussian-mixture post-processing. Evaluated across 96 rolling-origin forecasts on complex synthetic time series, TEMPER achieves strong median absolute error and short-horizon CRPS performance while highlighting critical calibration and horizon-specific tuning needs.

## Key Contributions

- Proposes TEMPER (Temporal Encoder-Masked Probabilistic Ensemble Regressor), combining a temporal autoencoder, differentiable masked neural decision forest, CRPS training, and Gaussian-mixture post-processing for probabilistic time-series forecasting.
- Evaluates TEMPER across 96 rolling-origin forecasts on synthetic level series with trend, periodic, regime-switching, nonlinear-threshold, and heteroskedastic components at horizons t+1, t+5, t+20, and t+60.
- Demonstrates that TEMPER achieves 2.824% mean normalized CRPS, 3.635% median absolute error, and 68.8% empirical 90% interval coverage, outperforming baselines in median absolute error and short-horizon CRPS (t+1, t+5).

## Limitations

TEMPER achieves lower initial interval coverage (68.8% vs nominal 90%) requiring calibration rules or interval inflation, and naive persistence bootstrap achieves better aggregate CRPS across all horizons.

## Open Questions & Future Work

- [[calibration-and-horizon-tuning-in-probabilistic-forecasting-models]]

## Archivist Review

We reviewed the candidate concepts and open questions from the paper. Since no candidate concepts were provided and the open question is overly broad or boilerplate regarding calibration and tuning, we rejected the open question to maintain strict vault standards.

### Approved Open Questions
- Calibration and Horizon Tuning: The results identify calibration, horizon-specific tuning, and component selection as the central research priorities.

### Rejected Candidates
- [open_question] Calibration and Horizon Tuning (`calibration-and-horizon-tuning-in-probabilistic-forecasting-models`) - low_impact: The open question is a bit too broad and resembles boilerplate future work directions regarding tuning and calibration.

## Links

- [Abstract](https://arxiv.org/abs/2609.23701)
- [PDF](https://arxiv.org/pdf/2609.23701)


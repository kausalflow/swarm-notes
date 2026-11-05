---
# CSL-compatible fields
title: "Zero-shot time-series foundation models against the Khepri v1.5 baselines for 96-hour carbon-intensity forecasts in nine Nordic bidding zones: a preregistered comparison"
author:
  - literal: "Eirik Botten Nicolaysen"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.02895"

# Custom fields
paper_id: "2611.02895"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "zero-shot-learning"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-05T12:51:35Z"
created_at: "2026-11-05T12:51:35Z"
---

# Zero-shot time-series foundation models against the Khepri v1.5 baselines for 96-hour carbon-intensity forecasts in nine Nordic bidding zones: a preregistered comparison

**Authors**: Eirik Botten Nicolaysen
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.02895](https://arxiv.org/abs/2611.02895)

## Summary

This paper presents a preregistered comparative evaluation of zero-shot time-series foundation models (Timestral-5M, Timestral-209M, and Chronos-2) against established Khepri v1.5 SARIMA and GBM baselines for 96-hour hourly carbon-intensity forecasting in nine Nordic bidding zones. Utilizing timestamped proofs to ensure integrity, the study finds that zero-shot foundation models significantly outperform traditional statistical and gradient-boosting baselines in terms of MAPE on the 2025 test set, while holdout results on late 2026 data remain statistically underdetermined within the preregistered MDE.

## Key Contributions

- Evaluated zero-shot time-series foundation models (Timestral-5M, Timestral-209M, Chronos-2) against Khepri v1.5 SARIMA and GBM baselines for 96-hour carbon-intensity forecasting across nine Nordic bidding zones.
- Demonstrated that all three zero-shot models achieve lower zone-averaged MAPE than baselines on the 2025 test set (by 0.952 to 1.347 percentage points, p < 0.0001).
- Conducted a rigorously preregistered evaluation with timestamped OpenTimestamps proofs and OSF registration to ensure methodological transparency and prevent data contamination bias.

## Limitations

Holdout evaluation on 14 origins from October 2026 yielded point estimates within the preregistered minimum detectable effect (MDE), leaving them statistically underdetermined.

## Links

- [Abstract](https://arxiv.org/abs/2611.02895)
- [PDF](https://arxiv.org/pdf/2611.02895)


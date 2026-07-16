---
# CSL-compatible fields
title: "Climate-Invariant Conformal Prediction Intervals for Multi-Horizon Solar and Wind Forecasting"
author:
  - literal: "Shreedhar Gangwar"
  - literal: "Abhinav Bains"
  - literal: "Banalaxmi Brahma"
issued:
  date-parts:
    - [2026, 7, 13]
url: "https://arxiv.org/abs/2607.11470"

# Custom fields
paper_id: "2607.11470"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "conformal-prediction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "group-conditional-split-conformal-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-16T07:14:33Z"
created_at: "2026-07-16T07:14:33Z"
---

# Climate-Invariant Conformal Prediction Intervals for Multi-Horizon Solar and Wind Forecasting

**Authors**: Shreedhar Gangwar, Abhinav Bains, Banalaxmi Brahma
**Date**: 2026-07-13
**Paper ID**: [openalex:2607.11470](https://arxiv.org/abs/2607.11470)

## Summary

This paper presents a group-conditional split-conformal framework to address the challenge of site-specific uncertainty quantification in solar and wind energy forecasting. By leveraging a heteroscedastic, asymmetric ensemble of XGBoost models, the approach provides reliable, distribution-free prediction intervals that are robust to climatic variations. Evaluated across four distinct global sites, the method achieves near-nominal coverage and significantly improves interval sharpness, outperforming existing probabilistic baselines without requiring per-site or per-horizon tuning.

## Key Contributions

- Introduces a group-conditional split-conformal framework that achieves distribution-free coverage guarantees for renewable energy forecasting without site-specific tuning.
- Demonstrates superior interval sharpness and calibration across diverse climates, reducing Interval Scores by up to 35% compared to competitive baselines.
- Maintains near-nominal coverage across multi-horizon (1-12 hours) solar irradiance and wind speed predictions using a single, fixed-specification model.

## Open Questions & Future Work

- [[conformal-prediction-non-exchangeable-time-series]]

## Key Concepts

- [[group-conditional-split-conformal-framework]]: A heteroscedastic, group-conditional conformal prediction method designed for cross-climate uncertainty quantification in renewable energy forecasting.

## Archivist Review

I have approved the group-conditional split-conformal framework as it represents a meaningful advancement in achieving model transferability for uncertainty quantification across climatologically diverse regions. The open question regarding the validity of conformal prediction in non-exchangeable settings is a fundamental theoretical bottleneck that persists in time-series literature. No datasets were approved as the paper utilizes standard, generalized renewable energy settings without introducing a novel named collection.

### Approved Concepts
- Group-Conditional Split-Conformal Framework: This method provides a novel way to ensure distribution-free coverage guarantees in solar and wind forecasting across diverse, climatologically distinct sites without per-site recalibration.

### Approved Open Questions
- Valid Conformal Prediction for Non-Exchangeable Series: Standard conformal prediction lacks formal validity guarantees for non-exchangeable time series, making this a critical theoretical and practical challenge for deploying reliable uncertainty quantification in real-world systems.

## Links

- [Abstract](https://arxiv.org/abs/2607.11470)
- [PDF](https://arxiv.org/pdf/2607.11470)


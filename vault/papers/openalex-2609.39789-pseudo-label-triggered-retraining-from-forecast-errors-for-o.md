---
# CSL-compatible fields
title: "Pseudo-Label-Triggered Retraining from Forecast Errors for Online Time Series Forecasting"
author:
  - literal: "Yeryeong Kwak"
  - literal: "Yoo-Min Jung"
  - literal: "Jonghun Park"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.39789"

# Custom fields
paper_id: "2609.39789"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "continual-learning"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "pilot"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:07:12Z"
created_at: "2026-10-03T10:07:12Z"
---

# Pseudo-Label-Triggered Retraining from Forecast Errors for Online Time Series Forecasting

**Authors**: Yeryeong Kwak, Yoo-Min Jung, Jonghun Park
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.39789](https://arxiv.org/abs/2609.39789)

## Summary

Real-world time series forecasting under non-stationary streams suffers from performance degradation, making the selection of when to retrain critical. This paper introduces PILOT, an online retraining framework that utilizes realized forecast-error dynamics to learn when to trigger retraining. By constructing pseudo-labels from future error increases, PILOT trains a lightweight scorer that acts as a plug-in module for existing forecasting architectures without requiring modification. Experiments across multivariate benchmarks with DLinear, iTransformer, and TimesNet demonstrate state-of-the-art performance among retraining policies.

## Key Contributions

- Proposes PILOT, an online retraining framework that learns when to retrain based directly on realized forecast-error dynamics without requiring ground-truth retraining labels.
- Constructs pseudo-labels from future increases in forecast error to train a lightweight scoring model for deployment triggering.
- Achieves state-of-the-art average-rank performance among retraining policies while preserving a favorable performance-efficiency trade-off across DLinear, iTransformer, and TimesNet backbones.

## Open Questions & Future Work

- [[richer-adaptation-actions-online-forecasting-retraining]]

## Key Concepts

- [[pilot]]: An online retraining trigger framework that learns when to retrain from forecast-error dynamics using pseudo-labels constructed from future error increases.

## Archivist Review

We approved the central methodological concept 'PILOT' for its reusable online retraining trigger formulation based on forecast-error dynamics. We also approved one open question concerning richer adaptation actions for online forecasting retraining. No specific named datasets were provided in the metadata, so none were approved.

### Approved Concepts
- PILOT: Central methodological contribution that defines an online retraining trigger based on forecast-error dynamics and pseudo-labeling.

### Approved Open Questions
- Richer Adaptation Actions for Retraining: Extending trigger policies to multi-action or continuous adaptation spaces is crucial for maximizing performance gains while minimizing computational overhead in online deployment.

## Links

- [Abstract](https://arxiv.org/abs/2609.39789)
- [PDF](https://arxiv.org/pdf/2609.39789)


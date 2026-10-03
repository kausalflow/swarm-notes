---
# CSL-compatible fields
title: "A Time-Aware Bag-of-Receptive-Fields for Interpretable Irregular Time Series Classification"
author:
  - literal: "Francesco Spinnato"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.39268"

# Custom fields
paper_id: "2609.39268"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretable-machine-learning"
  - "classification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "time-aware-bag-of-receptive-fields"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:08:21Z"
created_at: "2026-10-03T10:08:21Z"
---

# A Time-Aware Bag-of-Receptive-Fields for Interpretable Irregular Time Series Classification

**Authors**: Francesco Spinnato
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.39268](https://arxiv.org/abs/2609.39268)

## Summary

The paper extends the Bag-Of-Receptive-Fields (BORF) method to irregular time series by introducing a time-weighted normalization scheme that weights observations proportionally to their time delta. This approach relies on an efficient sliding-window recurrence for the time-weighted standard deviation, maintaining linear time complexity while avoiding explicit imputation. Evaluations on PYRREGULAR repository benchmarks show competitive classification accuracy paired with robust interpretability features.

## Key Contributions

- Extends the Bag-Of-Receptive-Fields (BORF) framework to handle irregular time series with non-uniform sampling intervals and missing observations.
- Introduces a time-weighted normalization scheme where observations are weighted proportionally to their time delta, capturing true temporal distributions.
- Derives an efficient sliding-window recurrence for the time-weighted standard deviation that preserves BORF's linear time complexity.
- Demonstrates competitive classification performance on PYRREGULAR repository datasets while offering built-in human interpretability.

## Open Questions & Future Work

- [[alternative-weighting-conventions-and-continuous-time-receptive-fields]]

## Key Concepts

- [[time-aware-bag-of-receptive-fields]]: An interpretable, deterministic time-series transform extended to irregular sampling intervals via time-weighted normalization.

## Archivist Review

Approved the core methodological concept extending BORF to irregular time series via time-weighted normalization and the associated open question on alternative weighting conventions and continuous-time formulations. No datasets met the strict novelty or standalone significance bar.

### Approved Concepts
- Time-Aware Bag-of-Receptive-Fields: Extends the deterministic BORF transform to irregular time series via a novel time-weighted normalization scheme.

### Approved Open Questions
- Alternative Weighting and Continuous-Time Receptive Fields: Understanding how boundary assumptions and continuous-time adaptations affect symbolic pattern extraction is crucial for generalizing dictionary-based time series classification to diverse real-world irregular domains.

## Links

- [Abstract](https://arxiv.org/abs/2609.39268)
- [PDF](https://arxiv.org/pdf/2609.39268)


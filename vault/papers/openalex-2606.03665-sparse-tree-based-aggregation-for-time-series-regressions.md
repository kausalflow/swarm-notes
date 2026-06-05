---
# CSL-compatible fields
title: "Sparse Tree-Based Aggregation for Time Series Regressions"
author:
  - literal: "Marie Corillon"
  - literal: "Stephan Smeekes"
  - literal: "Ines Wilms"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03665"

# Custom fields
paper_id: "2606.03665"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  - "startime"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:38:12Z"
created_at: "2026-06-05T08:38:12Z"
---

# Sparse Tree-Based Aggregation for Time Series Regressions

**Authors**: Marie Corillon, Stephan Smeekes, Ines Wilms
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03665](https://arxiv.org/abs/2606.03665)

## Summary

High-dimensional time series regression often suffers from dimensionality issues, typically addressed by sparse coefficient regularization. This paper proposes StarTime, a novel framework that leverages hierarchical temporal tree structures to aggregate lags at varying frequencies alongside sparse selection. By providing theoretical error bounds and empirical evidence of improved performance, StarTime offers an effective alternative for modeling complex, multi-frequency dependencies in macroeconomic and financial data.

## Key Contributions

- Introduces StarTime, a convex regularization method that performs joint temporal aggregation and sparsity selection using hierarchical tree structures.
- Derives new theoretical error bounds for the proposed estimator, establishing its statistical consistency in high-dimensional settings.
- Demonstrates superior estimation accuracy and recovery of aggregation structures in simulation studies and real-world financial/macroeconomic forecasting applications compared to standard benchmarks.

## Open Questions & Future Work

- [[structured-temporal-aggregation-inference]]

## Key Concepts

- [[startime]]: A convex penalization method that utilizes hierarchical temporal trees to aggregate and select lags in high-dimensional time series regressions.

## Archivist Review

I have approved StarTime as a distinct regularization method for time series and established an open question concerning the high-dimensional inference challenges inherent in joint aggregation and sparsity frameworks. I rejected no candidates because only one concept and one open question were proposed, both of which meet the strict criteria for vault inclusion.

### Approved Concepts
- StarTime: StarTime is a novel regularization framework that effectively addresses dimensionality in high-dimensional time series regressions by combining temporal aggregation with sparse selection.

### Approved Open Questions
- Structured Temporal Aggregation Inference: Developing high-dimensional inference is critical for moving beyond point estimation in complex models, while refined tuning methods address the performance sensitivity in finite-sample forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2606.03665)
- [PDF](https://arxiv.org/pdf/2606.03665)


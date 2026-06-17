---
# CSL-compatible fields
title: "Filtered Conformal Ellipsoids for Graph-Native Time Series"
author:
  - literal: "Yannick Limmer"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.17014"

# Custom fields
paper_id: "2606.17014"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "conformal-prediction"
  - "uncertainty-quantification"
  - "state-space-model"
  - "graph-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "filtered-conformal-ellipsoids"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:25:17Z"
created_at: "2026-06-17T09:25:17Z"
---

# Filtered Conformal Ellipsoids for Graph-Native Time Series

**Authors**: Yannick Limmer
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.17014](https://arxiv.org/abs/2606.17014)

## Summary

This paper addresses the challenge of creating accurate, valid joint prediction sets for multivariate time series by introducing Filtered Conformal Ellipsoids. The method uses a state-space filter to generate predictive mean and covariance, which then serves as input for split-conformal calibration of the Mahalanobis distance. By identifying a predictive-law quotient that ensures contraction of the learned state, the paper derives coverage bounds that hold even under dependence. Empirically, the approach achieves sharper uncertainty ellipsoids than existing baselines on graph-native traffic datasets.

## Key Contributions

- Introduced Filtered Conformal Ellipsoids, a method for uncertainty quantification that decouples predictive covariance estimation via state-space filtering from conformal radius calibration.
- Established theoretical conditions for contraction of learned predictive-law quotients under stable Bayes Gaussian-projection filters, enabling valid coverage under temporal dependence.
- Demonstrated superior volume sharpness on METRLA-20 and PEMSBAY-50 compared to static-covariance and non-filter baselines.

## Open Questions & Future Work

- [[distribution-free-filtered-conformal-prediction]]

## Key Concepts

- [[filtered-conformal-ellipsoids]]: A conformal prediction method that combines a learned state-space filter to define ellipsoid shape with split-conformal calibration to ensure empirical coverage.

## Archivist Review

The paper proposes a novel framework for multivariate conformal uncertainty quantification, decoupling learned predictive structure from empirical calibration. The core methodology and the associated theoretical bottleneck regarding distribution-free guarantees under dependence are both central to the field and sufficiently reusable to deserve standalone notes. The dataset candidates are rejected because they represent routine sub-samplings of well-known benchmarks rather than foundational datasets.

### Approved Concepts
- Filtered Conformal Ellipsoids: Provides a general framework for multivariate uncertainty quantification by combining learned predictive structure with valid conformal calibration.

### Approved Open Questions
- Distribution-Free Filtered Conformal Prediction: Reliable uncertainty quantification in safety-critical domains requires moving beyond conditional validity proofs to robust, distribution-free guarantees.

### Rejected Candidates
- [dataset] METRLA-20 (`METRLA-20`) - low_impact: This is a specific sub-selection of a standard dataset rather than a new or critical benchmark resource.
- [dataset] PEMSBAY-50 (`PEMSBAY-50`) - low_impact: This is a specific sub-selection of a standard dataset rather than a new or critical benchmark resource.

## Links

- [Abstract](https://arxiv.org/abs/2606.17014)
- [PDF](https://arxiv.org/pdf/2606.17014)


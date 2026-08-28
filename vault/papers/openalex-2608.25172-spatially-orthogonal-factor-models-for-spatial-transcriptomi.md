---
# CSL-compatible fields
title: "Spatially orthogonal factor models for spatial transcriptomics and remote sensing data"
author:
  - literal: "Dan Cunha"
  - literal: "Lukas M. Weber"
  - literal: "M. A. Friedl"
  - literal: "Luis Carvalho"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.25172"

# Custom fields
paper_id: "2608.25172"
paper_source: "openalex"
domain: "biology"
tags:
  - "multimodal"
  - "representation-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T17:01:17Z"
created_at: "2026-08-28T17:01:17Z"
---

# Spatially orthogonal factor models for spatial transcriptomics and remote sensing data

**Authors**: Dan Cunha, Lukas M. Weber, M. A. Friedl, Luis Carvalho
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.25172](https://arxiv.org/abs/2608.25172)

## Summary

The paper introduces a spatially orthogonal factor model for spatial data analysis in spatial transcriptomics and remote sensing, addressing non-orthogonality, stationarity, and scalability limitations of existing probabilistic PCA approaches. By parameterizing the model directly with orthogonal loadings and deriving an SVD transformation prior distribution, the authors formulate the MAP estimator as an eigendecomposition. Furthermore, they develop a minorization-maximization-within-EM algorithm that achieves linear-time complexity with respect to spatial locations and accommodates nonstationary prior covariances and held-out data.

## Key Contributions

- Proposes a spatially orthogonal factor model that parameterizes probabilistic PCA directly with orthogonal loadings without corrupting prior spatial information.
- Derives the sampling distribution of an SVD transformation with unique and repeated singular values to establish a nonstationary prior spatial covariance.
- Develops a minorization-maximization-within-EM algorithm achieving linear-time computational complexity with respect to the number of spatial locations.
- Demonstrates applicability on spatial transcriptomics (human brain) and remote sensing (continental-scale phenology in sub-Saharan Africa) case studies.

## Archivist Review

Reviewed the single candidate open question against the vault's high standards. The question concerns a niche estimation detail for a custom spatially orthogonal factor model and does not qualify as a broad, reusable conceptual bottleneck across the literature. No concepts or datasets were proposed.

### Rejected Candidates
- [open_question] Joint MAP Estimation for SOFM (`joint-map-estimation-sofm`) - low_impact: The question pertains to a very narrow estimation step for a specific custom factor model rather than a broad, reusable machine learning or time series forecasting research challenge.

## Links

- [Abstract](https://arxiv.org/abs/2608.25172)
- [PDF](https://arxiv.org/pdf/2608.25172)


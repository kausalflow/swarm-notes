---
# CSL-compatible fields
title: "CLUES-WEASEL: No additional clues required to choose your time series clustering algorithm"
author:
  - literal: "Johann Faouzi"
issued:
  date-parts:
    - [2026, 9, 7]
url: "https://arxiv.org/abs/2609.07606"

# Custom fields
paper_id: "2609.07606"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "unsupervised-learning"
  - "clustering"
  - "feature-extraction"
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
processed_at: "2026-09-10T09:16:04Z"
created_at: "2026-09-10T09:16:04Z"
---

# CLUES-WEASEL: No additional clues required to choose your time series clustering algorithm

**Authors**: Johann Faouzi
**Date**: 2026-09-07
**Paper ID**: [openalex:2609.07606](https://arxiv.org/abs/2609.07606)

## Summary

Time series clustering typically forces a trade-off between clustering performance and computational runtime. To address this, the paper introduces CLUES-WEASEL, an unsupervised clustering algorithm that leverages the feature extraction step of WEASEL 2.0, followed by principal component analysis and k-means clustering. Extensive empirical evaluation shows that CLUES-WEASEL achieves superior clustering performance while maintaining substantially faster runtimes than current state-of-the-art baselines. Furthermore, the modular pipeline design is shown to accommodate alternative time series feature extraction methods effectively.

## Key Contributions

- Introduces CLUES-WEASEL, a time series clustering algorithm combining unsupervised feature extraction from WEASEL 2.0, principal component analysis, and k-means clustering.
- Demonstrates through extensive experiments that CLUES-WEASEL outperforms existing time series clustering algorithms in clustering performance while being significantly faster than state-of-the-art baselines.
- Shows that the underlying architectural pipeline of CLUES-WEASEL can generalize successfully to other time series feature extraction algorithms.

## Archivist Review

Applied strict novelty and reusability standards. CLUES-WEASEL is a pipeline combination of existing components (WEASEL 2.0, PCA, k-means) rather than a broadly reusable architectural primitive. The open question is routine future work calling for more benchmarking.

### Rejected Candidates
- [concept] CLUES-WEASEL (`clues-weasel`) - not_novel: Paper-specific combination of an existing feature extractor (WEASEL 2.0), PCA, and k-means clustering.
- [open_question] Broad Domain Time Series Benchmarking (`cross-domain-time-series-clustering-benchmarks`) - low_impact: Generic future work proposing to benchmark on additional datasets without a specific algorithmic bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.07606)
- [PDF](https://arxiv.org/pdf/2609.07606)


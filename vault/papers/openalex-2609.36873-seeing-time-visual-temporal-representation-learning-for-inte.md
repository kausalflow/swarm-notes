---
# CSL-compatible fields
title: "Seeing Time: Visual-Temporal Representation Learning for Interpretable Time Series Clustering"
author:
  - literal: "Zheng Zhu"
  - literal: "Zexi Tan"
  - literal: "Yuming Deng"
  - literal: "Yiqun Zhang"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.36873"

# Custom fields
paper_id: "2609.36873"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "unsupervised-learning"
  - "clustering"
  - "representation-learning"
  - "multimodal"
  - "interpretability"
  - "explainability"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "wave"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:15:28Z"
created_at: "2026-10-01T11:15:28Z"
---

# Seeing Time: Visual-Temporal Representation Learning for Interpretable Time Series Clustering

**Authors**: Zheng Zhu, Zexi Tan, Yuming Deng, Yiqun Zhang
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.36873](https://arxiv.org/abs/2609.36873)

## Summary

This paper introduces WAVE (Waveform Aligned Visual-temporal Embedding), a visual-temporal representation learning framework for multivariate time series clustering that treats raw time series and their deterministically rendered waveform plots as complementary views. By aligning fine-grained temporal variations with holistic visual patterns and associating clusters with centroid-nearest authentic samples, WAVE provides waveform-level traceability rather than black-box decisions. Extensive experiments across 10 real-world public datasets demonstrate that WAVE achieves top-tier clustering performance and superior average ranking compared to existing baselines.

## Key Contributions

- Proposes WAVE, a visual-temporal representation learning framework that treats time series and deterministically rendered waveform plots as complementary views for multivariate time series clustering.
- Aligns fine-grained temporal variations with holistic visual patterns to produce discriminative representations with waveform-level traceability.
- Associates each discovered cluster with its centroid-nearest authentic sample to enable practitioners to visually inspect and verify temporal patterns.
- Achieves state-of-the-art performance across 10 real-world public datasets, securing the highest macro-averaged clustering performance and best average rank.

## Open Questions & Future Work

- [[adaptive-rendering-cluster-estimation]]

## Key Concepts

- [[wave]]: A visual-temporal representation learning framework for multivariate time series clustering that aligns time series with rendered waveform plots to achieve waveform-level traceability.

## Archivist Review

Approved the core dual-view representation learning framework WAVE for its novel methodology combining time series and rendered waveform plots. Also approved the open question regarding adaptive rendering and cluster estimation. All other potential items were rejected to maintain vault selectivity.

### Approved Concepts
- WAVE (Waveform Aligned Visual-temporal Embedding): WAVE introduces a novel dual-view framework aligning multivariate time series with rendered waveform plots for interpretable clustering with waveform-level traceability.

### Approved Open Questions
- Adaptive Rendering and Cluster Estimation: Overcoming the dependency on fixed rendering strategies and known cluster counts is crucial for making visual-temporal clustering applicable to fully unsupervised, dynamic real-world environments.

## Links

- [Abstract](https://arxiv.org/abs/2609.36873)
- [PDF](https://arxiv.org/pdf/2609.36873)


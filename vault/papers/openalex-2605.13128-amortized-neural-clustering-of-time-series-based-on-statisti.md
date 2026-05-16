---
# CSL-compatible fields
title: "Amortized Neural Clustering of Time Series based on Statistical Features"
author:
  - literal: "Ángel López-Oriona"
  - literal: "Ying Sun"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13128"

# Custom fields
paper_id: "2605.13128"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "clustering"
architectures:
  []
datasets:
  []
concept_slugs:
  - "amortized-neural-clustering-of-time-series"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:09:12Z"
created_at: "2026-05-16T07:09:12Z"
---

# Amortized Neural Clustering of Time Series based on Statistical Features

**Authors**: Ángel López-Oriona, Ying Sun
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13128](https://arxiv.org/abs/2605.13128)

## Summary

This paper presents an amortized neural approach to time series clustering, replacing conventional iterative algorithms with a data-driven partition estimator. By training on statistical features like autocorrelations, the method bypasses the need for explicit assumptions about cluster structure or pre-defined algorithm selection. The framework excels in complex clustering tasks and includes a variant capable of autonomously identifying the number of clusters.

## Key Contributions

- Introduces an algorithm-agnostic framework that learns to approximate optimal time series clustering partitions via amortized neural inference.
- Demonstrates the ability to determine the optimal number of clusters automatically, eliminating the need for ad-hoc selection heuristics.
- Achieves superior or competitive accuracy compared to standard K-means and hierarchical clustering methods across financial time series datasets.

## Open Questions & Future Work

- [[fuzzy-amortized-clustering]]
- [[hybrid-simulation-self-supervised-clustering]]

## Key Concepts

- [[amortized-neural-clustering-of-time-series]]: A framework that trains neural networks to learn time series clustering partitions directly from statistical feature inputs, bypassing manual selection of clustering algorithms.

## Archivist Review

The paper introduces a compelling paradigm shift in time series clustering by moving from iterative, heuristic-based algorithms (like K-means) to an amortized neural inference approach. This is a highly reusable concept for the vault. The two approved open questions address core limitations of this new approach—the need for soft assignment and the challenge of sim-to-real gap—which are critical for tracking the maturity of amortized clustering techniques in future research.

### Approved Concepts
- Amortized Neural Clustering of Time Series: The paper shifts time series clustering from iterative heuristics to a learned, amortized neural inference process that is agnostic to the underlying cluster shape.

### Approved Open Questions
- Fuzzy Amortized Neural Clustering: Extending the framework to fuzzy clustering would significantly increase its applicability to complex real-world datasets where series boundaries are not clearly defined, providing a more nuanced and accurate representation of temporal dynamics than crisp assignment.
- Hybrid Training for Clustering: Hybrid approaches could bridge the gap between idealized synthetic training data and the complexities of real-world temporal data, reducing the dependence on perfect model specification and improving generalization in practical deployment scenarios.

## Links

- [Abstract](https://arxiv.org/abs/2605.13128)
- [PDF](https://arxiv.org/pdf/2605.13128)


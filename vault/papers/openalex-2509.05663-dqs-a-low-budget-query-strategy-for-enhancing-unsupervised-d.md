---
# CSL-compatible fields
title: "DQS: a low-budget query strategy for enhancing unsupervised data-driven anomaly detection approaches"
author:
  - literal: "Lucas Correia"
  - literal: "Jan-Christoph Goos"
  - literal: "Thomas Bäck"
  - literal: "Anna V. Kononova"
issued:
  date-parts:
    - [2026, 8, 8]
url: "https://arxiv.org/abs/2509.05663"

# Custom fields
paper_id: "2509.05663"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "active-learning"
  - "unsupervised-learning"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dissimilarity-based-query-strategy"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-11T05:45:53Z"
created_at: "2026-08-11T05:45:53Z"
---

# DQS: a low-budget query strategy for enhancing unsupervised data-driven anomaly detection approaches

**Authors**: Lucas Correia, Jan-Christoph Goos, Thomas Bäck, Anna V. Kononova
**Date**: 2026-08-08
**Paper ID**: [openalex:2509.05663](https://arxiv.org/abs/2509.05663)

## Summary

This paper addresses the limitation of unsupervised time-series anomaly detection methods that rely on labelled subsets for threshold selection by introducing the Dissimilarity-based Query Strategy (DQS). DQS integrates active learning with unsupervised detectors by leveraging dynamic time warping on anomaly scores to maximize sample diversity under small annotation budgets. Experiments demonstrate that while DQS excels in low-budget settings, active learning-based threshold tuning consistently outperforms fully unsupervised thresholds even when facing annotation mislabelling.

## Key Contributions

- Introduces DQS (Dissimilarity-based Query Strategy), an active learning-based query method for multivariate time series anomaly detection threshold selection.
- Utilizes dynamic time warping to evaluate similarity between anomaly scores and maximize diversity among queried samples under low-budget scenarios.
- Explores the impact of mislabelling on active learning-based threshold selection for unsupervised anomaly detection methods.

## Limitations

Evaluated on a single dataset setting in the abstract; other benchmark strategies show higher robustness against mislabelling.

## Open Questions & Future Work

- [[robust-active-learning-mislabelling-time-series]]

## Key Concepts

- [[dissimilarity-based-query-strategy]]: An active learning query strategy that maximizes sample diversity for time series anomaly detection thresholds by evaluating anomaly score dissimilarity using dynamic time warping.

## Archivist Review

Approved the core active learning method (DQS) for time series anomaly thresholding and the open question regarding mislabelling robustness, both of which are reusable and significant contributions to the vault. No datasets were provided.

### Approved Concepts
- Dissimilarity-Based Query Strategy: DQS is the core methodological contribution of the paper, providing a dissimilarity-based active learning query strategy for multivariate time series anomaly threshold tuning.

### Approved Open Questions
- Robust Active Learning under Mislabelling: Addressing mislabelling robustness bridges the gap between simulated active learning benchmarks and noisy real-world industrial deployments.

## Links

- [Abstract](https://arxiv.org/abs/2509.05663)
- [PDF](https://arxiv.org/pdf/2509.05663)


---
# CSL-compatible fields
title: "Lead-Lag Relationships in Financial Markets: A Comparison of Multiple Clustering Algorithms"
author:
  - literal: "Ruichen Deng"
  - literal: "Yichi Zhang"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.24703"

# Custom fields
paper_id: "2608.24703"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
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
processed_at: "2026-08-28T17:00:56Z"
created_at: "2026-08-28T17:00:56Z"
---

# Lead-Lag Relationships in Financial Markets: A Comparison of Multiple Clustering Algorithms

**Authors**: Ruichen Deng, Yichi Zhang
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.24703](https://arxiv.org/abs/2608.24703)

## Summary

This paper investigates lead-lag relationships in financial time series by comparing multiple clustering algorithms, including traditional DTW-KMedoids, MiniRocket-KMeans, KShape, and an Ensemble algorithm. By optimizing the cluster count via the silhouette coefficient, the authors show that MiniRocket-KMeans yields the highest Sharpe ratio under trading strategies while the ensemble method enhances stability. Hypothesis testing further confirms the statistical validity of the lead-lag trading strategies.

## Key Contributions

- Evaluated and compared MiniRocket-KMeans, KShape, and an Ensemble algorithm against traditional DTW-KMedoids for financial lead-lag relationships.
- MiniRocket-KMeans achieved the best performance under the lead strategy with a Sharpe ratio of 0.866 and a maximum drawdown of -63.9%.
- Demonstrated that optimizing the number of clusters via the silhouette coefficient significantly enhances experimental stability and strategy robustness.

## Limitations

Computational complexity of distance metrics and sensitivity to cluster count hyperparameter tuning.

## Archivist Review

The paper investigates known financial clustering algorithms (DTW-KMedoids, KShape, MiniRocket-KMeans) for lead-lag trading strategies. Neither the proposed combination nor the listed future improvements constitute sufficiently novel or reusable contributions to the vault under strict selection criteria.

### Rejected Candidates
- [concept] Ensemble Lead-Lag Clustering Algorithm (`ensemble-lead-lag-clustering-algorithm`) - paper_local: The proposed ensemble combines specific existing algorithms (KShape and DTW-KMedoids) for a local financial application, making it too paper-local and lacking broader reusable architectural novelty.
- [open_question] Customized Lead-Lag Matrices and Ensemble Clustering (`customized-lead-lag-matrices-and-ensemble-clustering`) - low_impact: The open question is essentially a laundry list of routine improvements and future work items tailored to financial clustering metrics rather than a fundamental theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.24703)
- [PDF](https://arxiv.org/pdf/2608.24703)


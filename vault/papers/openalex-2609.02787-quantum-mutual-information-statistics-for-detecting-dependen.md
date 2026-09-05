---
# CSL-compatible fields
title: "Quantum mutual information statistics for detecting dependence-structure change points in time series"
author:
  - literal: "Jiwon Kang"
  - literal: "Yun Am Seo"
issued:
  date-parts:
    - [2026, 9, 2]
url: "https://arxiv.org/abs/2609.02787"

# Custom fields
paper_id: "2609.02787"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-05T08:41:53Z"
created_at: "2026-09-05T08:41:53Z"
---

# Quantum mutual information statistics for detecting dependence-structure change points in time series

**Authors**: Jiwon Kang, Yun Am Seo
**Date**: 2026-09-02
**Paper ID**: [openalex:2609.02787](https://arxiv.org/abs/2609.02787)

## Summary

This paper introduces a quantum mutual information (QMI) statistic for detecting dependence-structure change points in multivariate time series while remaining robust to marginal drift. By employing trace-normalised density operators on random Fourier features of ranks, the method computes von Neumann entropies from prefix sums of small matrices without requiring density estimation or parameter tuning. Evaluations show that QMI outperforms classical independence criteria such as HSIC, distance correlation, and empirical-copula statistics in statistical power and false-alarm control under marginal drift.

## Key Contributions

- Proposes a quantum mutual information (QMI) statistic derived from density operators of random Fourier features of ranks for detecting dependence-structure change points in multivariate time series without density estimation or tuned parameters.
- Develops a segment-separable cost framework for penalised optimal partitioning where the split gain corresponds to Holevo information, along with finite-sample exact calibration procedures for both independent and serially dependent series.
- Proves a weighted chi-square boundary law at the segment length for the rank-based statistic and demonstrates superior power and robustness against marginal drift compared to HSIC, distance correlation, Spearman, and empirical-copula statistics.

## Links

- [Abstract](https://arxiv.org/abs/2609.02787)
- [PDF](https://arxiv.org/pdf/2609.02787)


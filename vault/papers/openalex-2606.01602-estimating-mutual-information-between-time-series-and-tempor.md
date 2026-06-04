---
# CSL-compatible fields
title: "Estimating Mutual Information between Time Series and Temporal Event Sequences Across Diverse Analysis Tasks"
author:
  - literal: "Haoji Hu"
  - literal: "Huaqing Mao"
  - literal: "Yijun Lin"
  - literal: "Xiaowei Jia"
  - literal: "Jinwei Zhou"
  - literal: "Minoh Jeong"
  - literal: "Yao‐Yi Chiang"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.01602"

# Custom fields
paper_id: "2606.01602"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "information-extraction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "nonparametric-heterogeneous-temporal-mi-estimator"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:43:04Z"
created_at: "2026-06-04T08:43:04Z"
---

# Estimating Mutual Information between Time Series and Temporal Event Sequences Across Diverse Analysis Tasks

**Authors**: Haoji Hu, Huaqing Mao, Yijun Lin, Xiaowei Jia, Jinwei Zhou, Minoh Jeong, Yao‐Yi Chiang
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.01602](https://arxiv.org/abs/2606.01602)

## Summary

This paper presents a robust, nonparametric approach to quantifying mutual information between heterogeneous data types, specifically continuous time series and discrete temporal event sequences. By modeling continuous-discrete duality and employing latent event clustering, the method bypasses common biases introduced by quantization and event redundancy found in traditional estimators. It offers a unified dependence operator validated across causality, discovery, and feature selection tasks, providing a more principled alternative to ad hoc transformations.

## Key Contributions

- Introduced a nonparametric mutual information estimator that directly computes dependence between time series and event sequences without requiring discretization or learning.
- Developed a framework that mitigates quantization artifacts and event redundancy through continuous-discrete duality modeling and latent event clustering.
- Demonstrated consistent superiority over existing methods across causality analysis, repetition discovery, and feature selection for both forecasting and classification tasks.

## Open Questions & Future Work

- [[theoretical-bounds-for-heterogeneous-mi-estimators]]

## Key Concepts

- [[nonparametric-heterogeneous-temporal-mi-estimator]]: A nonparametric mutual information estimator that quantifies dependence between heterogeneous time series and event sequences by modeling continuous-discrete duality and latent event clustering.

## Archivist Review

The paper introduces a significant operator for quantifying dependency between heterogeneous temporal modalities. I approved the estimator as a concept and the open question regarding its theoretical bounds, as these are foundational for future temporal mining tasks. No datasets were included or found to be sufficiently central to the claims to warrant a permanent entry.

### Approved Concepts
- Nonparametric Heterogeneous Temporal Mutual Information Estimator: Provides a principled, general-purpose operator for quantifying dependence between continuous time series and discrete event sequences, bypassing ad hoc transformations and discretization.

### Approved Open Questions
- Theoretical Bounds for Heterogeneous MI Estimators: Reliable dependency estimation for causal inference and feature selection requires robust theoretical error bounds beyond empirical validation.

## Links

- [Abstract](https://arxiv.org/abs/2606.01602)
- [PDF](https://arxiv.org/pdf/2606.01602)


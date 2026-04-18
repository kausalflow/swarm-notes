---
# CSL-compatible fields
title: "Forecasting Multivariate Time Series under Predictive Heterogeneity: A Validation-Driven Clustering Framework"
author:
  - literal: "Ziling Ma"
  - literal: "Ángel López Oriona"
  - literal: "Hernando Ombao"
  - literal: "Ying Sun"
issued:
  date-parts:
    - [2026, 4, 15]
url: "https://arxiv.org/abs/2604.13748"

# Custom fields
paper_id: "2604.13748"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "validation-driven-clustering-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-18T06:06:22Z"
created_at: "2026-04-18T06:06:22Z"
---

# Forecasting Multivariate Time Series under Predictive Heterogeneity: A Validation-Driven Clustering Framework

**Authors**: Ziling Ma, Ángel López Oriona, Hernando Ombao, Ying Sun
**Date**: 2026-04-15
**Paper ID**: [openalex:2604.13748](https://arxiv.org/abs/2604.13748)

## Summary

This paper addresses the challenge of predictive heterogeneity in multivariate time series forecasting by proposing a validation-driven adaptive pooling framework. Unlike traditional methods that group series based on feature similarity, this approach partitions data according to out-of-sample validation loss, ensuring that cluster assignments directly reflect predictive risk. The framework integrates both point and probabilistic forecasting objectives and features a leakage-free fallback mechanism that defaults to global modeling when specialization fails. Experiments confirm the method's effectiveness in enhancing forecast accuracy and robustness on large-scale traffic datasets.

## Key Contributions

- Formulated adaptive pooling as a statistical decision problem to optimize for predictive risk rather than representation similarity.
- Developed an iterative validation-driven cluster update mechanism for point and probabilistic forecasting that improves robustness to heavy-tailed noise.
- Introduced a leakage-free fallback mechanism that dynamically switches to a global model to prevent negative transfer in low-heterogeneity scenarios.

## Open Questions & Future Work

- [[soft-clustering-mts-forecasting]]

## Key Concepts

- [[validation-driven-clustering-framework]]: A framework for adaptive pooling in multivariate time series that partitions data based on out-of-sample predictive performance rather than static feature similarity.

## Archivist Review

The approved concept offers a clear, reusable framework for addressing predictive heterogeneity by prioritizing empirical validation performance over static representation-based grouping, which is a significant departure from standard clustering techniques. The open question identifies a logical next step (soft assignment) that addresses the limitations of hard cluster boundaries, a common bottleneck in adaptive pooling methods. Other candidates were rejected to maintain the required scarcity and to avoid generic or low-impact inclusions.

### Approved Concepts
- Validation-Driven Clustering Framework: It addresses the core research problem of balancing global modeling efficiency with local predictive heterogeneity by using validation error as a grouping criterion.

### Approved Open Questions
- Soft Clustering for MTS Forecasting: The current hard-assignment strategy is identified by the authors as a limitation that may restrict performance when dynamics are not perfectly separable. Enabling soft membership could improve predictive accuracy and model flexibility in complex high-dimensional settings.

## Links

- [Abstract](https://arxiv.org/abs/2604.13748)
- [PDF](https://arxiv.org/pdf/2604.13748)


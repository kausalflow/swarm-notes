---
# CSL-compatible fields
title: "SDGF: Fusing Static and Multi-Scale Dynamic Correlations for Multivariate Time Series Forecasting"
author:
  - literal: "Shaoxun Wang"
  - literal: "Xingjun Zhang"
  - literal: "Qianyang Li"
  - literal: "Jiawei Cao"
  - literal: "Zhendong Tan"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2509.18135"

# Custom fields
paper_id: "2509.18135"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "graph-neural-network"
  - "gnn"
architectures:
  []
datasets:
  []
concept_slugs:
  - "static-dynamic-graph-fusion-sdgf"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T06:58:58Z"
created_at: "2026-04-24T06:58:58Z"
---

# SDGF: Fusing Static and Multi-Scale Dynamic Correlations for Multivariate Time Series Forecasting

**Authors**: Shaoxun Wang, Xingjun Zhang, Qianyang Li, Jiawei Cao, Zhendong Tan
**Date**: 2026-04-21
**Paper ID**: [openalex:2509.18135](https://arxiv.org/abs/2509.18135)

## Summary

The paper introduces the Static-Dynamic Graph Fusion (SDGF) network to improve multivariate time series forecasting by effectively capturing evolving inter-series correlations. The model employs a dual-path architecture that combines static, prior-knowledge-based dependencies with adaptively learned dynamic graphs derived from multi-level wavelet decomposition. An attention-gated module integrates these complementary sources, while multi-kernel dilated convolutions further capture complex temporal patterns. Empirical evaluations demonstrate that SDGF achieves superior performance on standard multivariate time series forecasting benchmarks.

## Key Contributions

- Introduces SDGF, a dual-path graph fusion network that jointly models static prior-knowledge dependencies and adaptive multi-scale dynamic correlations.
- Employs Multi-level Wavelet Decomposition to decompose multivariate signals and construct frequency-specific dynamic graphs.
- Incorporates an attention-gated fusion module to dynamically weight the contribution of static and dynamic graph structures for improved forecasting accuracy.

## Open Questions & Future Work

- [[integrating-static-dynamic-multiscale-dependencies-in-tsf]]

## Key Concepts

- [[static-dynamic-graph-fusion-sdgf]]: A dual-path graph fusion approach that integrates stable static dependencies with multi-scale dynamic associations for multivariate time series forecasting.

## Archivist Review

I approved the Static-Dynamic Graph Fusion concept as it represents a robust architectural pattern for multivariate forecasting that explicitly decouples long-term stable relationships from transient scale-dependent dynamics. The open question was approved for tracking how these disparate structural dependencies can be optimally fused in non-stationary settings. Standard benchmarks and internal sub-modules were rejected per the guidelines to ensure the vault remains focused on fundamental methodological contributions.

### Approved Concepts
- Static-Dynamic Graph Fusion (SDGF): Core innovation combining static prior-knowledge graphs with adaptive dynamic multi-scale graphs for inter-series correlation modeling.

### Approved Open Questions
- Integrating Static and Dynamic Multiscale Dependencies in TSF: This is a fundamental bottleneck in multivariate forecasting, as ignoring the interplay between stable long-term relations and transient, scale-dependent dynamics often limits model generalizability in non-stationary environments.

## Links

- [Abstract](https://arxiv.org/abs/2509.18135)
- [PDF](https://arxiv.org/pdf/2509.18135)


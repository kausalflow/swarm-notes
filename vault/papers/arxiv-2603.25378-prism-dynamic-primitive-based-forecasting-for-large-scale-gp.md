---
# CSL-compatible fields
title: "PRISM: Dynamic Primitive-Based Forecasting for Large-Scale GPU Cluster Workloads"
author:
  - literal: "Xin Wu"
  - literal: "Fei Teng"
  - literal: "Xingwang Li"
  - literal: "Bin Zheng"
  - literal: "Qiang Duan"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25378"

# Custom fields
paper_id: "2603.25378"
paper_source: "arxiv"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  - "Production GPU Traces"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T09:10:27Z"
created_at: "2026-03-27T09:10:27Z"
---

# PRISM: Dynamic Primitive-Based Forecasting for Large-Scale GPU Cluster Workloads

**Authors**: Xin Wu, Fei Teng, Xingwang Li, Bin Zheng, Qiang Duan
**Date**: 2026-03-26
**Paper ID**: [arxiv:2603.25378](https://arxiv.org/abs/2603.25378)

## Summary

PRISM is a novel compositional forecasting framework designed to address the volatility and heterogeneity of large-scale GPU cluster workloads by employing a dual representation. The core methodology combines dictionary-driven temporal decomposition to extract stable, interpretable workload signatures (primitives) with an adaptive spectral refinement step. Evaluated on production traces, PRISM significantly outperforms existing predictors, especially by minimizing errors during high-variability burst phases. This framework offers a robust foundation for architecture-aware dynamic resource management in modern AI platforms.

## Key Contributions

- Proposed PRISM, a primitive-based compositional forecasting framework that utilizes dictionary-driven temporal decomposition and adaptive spectral refinement.
- Developed a dual representation that effectively extracts stable and interpretable workload signatures from heterogeneous GPU job traces.
- Achieved state-of-the-art forecasting performance on large-scale production GPU workload traces, particularly reducing errors during burst phases.
- Established a robust, architecture-aware foundation for dynamic resource management in AI infrastructure based on workload prediction.

## Limitations

The paper does not explicitly detail the scalability limits of the dictionary-driven decomposition process for extremely high-dimensional or rapidly evolving workload signature sets.

## Open Questions & Future Work

- [[generalizability-of-primitive-decomposition-to-other-volatile-time-series]]

## Key Concepts

- [Primitive-Based Compositional Forecasting](../concepts/primitive-based-compositional-forecasting.md): A forecasting framework that decomposes large-scale GPU workloads into stable, interpretable temporal signatures (primitives) for improved accuracy.

## Datasets

- [Production GPU Traces](../datasets/production-gpu-traces.md)

## Limitations

The paper does not explicitly detail the scalability limits of the dictionary-driven decomposition process for extremely high-dimensional or rapidly evolving workload signature sets.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.25378)
- [PDF](https://arxiv.org/pdf/2603.25378)


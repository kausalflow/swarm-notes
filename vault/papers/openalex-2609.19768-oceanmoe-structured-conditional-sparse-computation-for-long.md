---
# CSL-compatible fields
title: "OceanMoE: Structured Conditional Sparse Computation for Long-Horizon Multivariate Ocean Forecasting"
author:
  - literal: "Yishun Zhu"
  - literal: "Jian Wang"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.19768"

# Custom fields
paper_id: "2609.19768"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "mixture-of-experts"
  - "moe"
  - "long-context"
  - "autoregressive"
architectures:
  - "decoder-only"
datasets:
  - "oras5"
concept_slugs:
  - "oceanmoe"
dataset_slugs:
  - "oras5"
skill: "TimeSeriesSkill"
processed_at: "2026-09-19T09:04:13Z"
created_at: "2026-09-19T09:04:13Z"
---

# OceanMoE: Structured Conditional Sparse Computation for Long-Horizon Multivariate Ocean Forecasting

**Authors**: Yishun Zhu, Jian Wang
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.19768](https://arxiv.org/abs/2609.19768)

## Summary

OceanMoE is a structured conditional sparse Mixture-of-Experts framework designed for long-horizon multivariate ocean forecasting, balancing shared ocean context with adaptive spatial specialization. It fuses cross-variable representations to perform content-conditioned sparse routing enhanced by spherical-harmonic geographic biases and shared seasonal pathways. Experiments on long-horizon autoregressive ORAS5 forecasting demonstrate reduced aggregate error and improved geometric-mean normalized RMSE over baseline models.

## Key Contributions

- Proposes OceanMoE, a structured conditional sparse Mixture-of-Experts framework that combines shared ocean context with target-specific adaptation for multivariate forecasting.
- Incorporates spherical-harmonic spatial bases into the decoder routing alongside shared residual and seasonal pathways to handle geographic heterogeneity.
- Demonstrates lower aggregate forecasting error and superior geometric-mean normalized RMSE on long-horizon autoregressive ORAS5 forecasting compared to baselines.

## Key Concepts

- [[oceanmoe]]: A structured conditional sparse Mixture-of-Experts framework combining shared context with adaptive spatial specialization for multivariate ocean forecasting.

## Archivist Review

Approved the overarching OceanMoE framework as a reusable Mixture-of-Experts architecture for spatiotemporal ocean forecasting, along with the ORAS5 dataset. Subcomponents like spherical-harmonic geographic bias were rejected as paper-internal implementation details.

### Approved Concepts
- OceanMoE: Central to the paper's contribution as a novel structured conditional sparse Mixture-of-Experts framework for multivariate ocean forecasting.

### Rejected Candidates
- [concept] Spherical-Harmonic Spatial Bases (`spherical-harmonic-spatial-bases`) - subcomponent_of_broader_mechanism: A routine mathematical parameterization of geographic bias, falling under paper-internal subcomponents.

## Datasets

- [[oras5]]

## Links

- [Abstract](https://arxiv.org/abs/2609.19768)
- [PDF](https://arxiv.org/pdf/2609.19768)


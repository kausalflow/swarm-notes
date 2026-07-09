---
# CSL-compatible fields
title: "CausticFlow: An Efficient Machine Learning Framework Combining Neural Differential Equations and Normalizing Flows for Binary Microlensing Parameter Inference"
author:
  - literal: "Haibin Ren"
  - literal: "Wei Zhu"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.04955"

# Custom fields
paper_id: "2607.04955"
paper_source: "openalex"
domain: "astronomy"
tags:
  - "time-series"
  - "machine-learning"
  - "astronomy"
architectures:
  []
datasets:
  - "kmtnet"
concept_slugs:
  - "causticflow"
dataset_slugs:
  - "kmtnet"
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:18:54Z"
created_at: "2026-07-09T08:18:54Z"
---

# CausticFlow: An Efficient Machine Learning Framework Combining Neural Differential Equations and Normalizing Flows for Binary Microlensing Parameter Inference

**Authors**: Haibin Ren, Wei Zhu
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.04955](https://arxiv.org/abs/2607.04955)

## Summary

CausticFlow is a machine learning framework designed for efficient binary microlensing parameter inference by combining neural controlled differential equations (NCDEs) and normalizing flows. The NCDE component enables the model to process irregularly sampled light curves and data gaps, while the normalizing flows capture complex, multimodal posterior distributions. As a proposal engine, CausticFlow accelerates parameter estimation and improves precision when paired with downstream local optimization, providing a scalable solution for high-cadence microlensing surveys.

## Key Contributions

- CausticFlow integrates neural controlled differential equations (NCDEs) and normalizing flows to enable fast, robust parameter inference in binary microlensing.
- The framework generates posterior samples in sub-second time, achieving precision improvements when used as a proposal engine for local optimization.
- Demonstrated successful recovery of parameters for 7 out of 10 real binary lensing events, showing generalizability despite simulation-reality noise and cadence mismatches.

## Open Questions & Future Work

- [[incorporating-higher-order-effects-microlensing-ml]]

## Key Concepts

- [[causticflow]]: A framework combining neural controlled differential equations and normalizing flows for efficient parameter inference in scientific time series.

## Archivist Review

I approved CausticFlow as a reusable architectural pattern combining NCDEs and normalizing flows for scientific inference. I also approved the open question regarding the inclusion of higher-order effects in microlensing simulations, as it identifies a critical bottleneck for deploying deep learning in astronomical surveys. I approved the KMTNet dataset as it is the central source of simulation data defining the model's performance claims.

### Approved Concepts
- CausticFlow: It demonstrates a reusable architectural pattern for scientific inference by combining neural controlled differential equations (for irregularly sampled time series) with normalizing flows (for multimodal posterior sampling).

### Approved Open Questions
- Incorporating Higher-Order Microlensing Effects: This bottleneck is central to transitioning deep-learning-based astronomical inference from simulated ideal conditions to robust real-world survey operations.

### Rejected Candidates
- [concept] none (`none`) - other: No other concepts were proposed.

## Datasets

- [[kmtnet]]

## Links

- [Abstract](https://arxiv.org/abs/2607.04955)
- [PDF](https://arxiv.org/pdf/2607.04955)


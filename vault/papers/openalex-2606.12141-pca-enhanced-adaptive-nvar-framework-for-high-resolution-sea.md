---
# CSL-compatible fields
title: "PCA-Enhanced Adaptive NVAR Framework for High-Resolution Sea Surface Temperature Forecasting in the East Sea"
author:
  - literal: "Sherkhon Azimov"
  - literal: "Susana Lopez-Moreno"
  - literal: "Eric Dolores-Cuenca"
  - literal: "JinYong Choi"
  - literal: "Sangil Kim"
issued:
  date-parts:
    - [2026, 6, 10]
url: "https://arxiv.org/abs/2606.12141"

# Custom fields
paper_id: "2606.12141"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-nvar"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-13T08:16:25Z"
created_at: "2026-06-13T08:16:25Z"
---

# PCA-Enhanced Adaptive NVAR Framework for High-Resolution Sea Surface Temperature Forecasting in the East Sea

**Authors**: Sherkhon Azimov, Susana Lopez-Moreno, Eric Dolores-Cuenca, JinYong Choi, Sangil Kim
**Date**: 2026-06-10
**Paper ID**: [openalex:2606.12141](https://arxiv.org/abs/2606.12141)

## Summary

This paper introduces a reduced-order forecasting framework for high-resolution Sea Surface Temperature (SST) prediction by integrating Singular Value Decomposition (SVD) with the Adaptive Next-Generation Reservoir Computing (Adaptive NVAR) model. By compressing complex SST fields into dominant low-dimensional modes, the framework efficiently models temporal dynamics while avoiding the error accumulation typical in deep learning approaches. Experimental results on regional ocean datasets demonstrate that the proposed method offers both improved accuracy and significant computational scalability compared to standard NG-RC/NVAR models.

## Key Contributions

- Introduces a reduced-order forecasting framework combining Singular Value Decomposition (SVD) and Adaptive NVAR for high-dimensional ocean data.
- Demonstrates that SVD-based latent space modeling significantly reduces computational overhead compared to standard NVAR/NG-RC.
- Achieves superior performance and reduced error accumulation for Sea Surface Temperature (SST) forecasting across multiple horizons in the East Sea.

## Open Questions & Future Work

- [[higher-dimensional-latent-forecasting]]

## Key Concepts

- [[adaptive-nvar]]: A reservoir computing framework designed for modeling temporal evolution of dynamical systems.

## Archivist Review

I approved the core reservoir-based forecasting framework and one open question regarding latent space dimensionality. I rejected 'Direct High-Resolution Grid Forecasting' as a distinct open question because the field is already extensively debating the trade-offs between latent and direct-space modeling; the request to reconstruct directly is more of a standard incremental goal rather than a novel, unresolved research bottleneck. No new datasets were requested or identified as unique enough for an entry.

### Approved Concepts
- Adaptive NVAR: The core methodology leverages a reservoir-computing-based approach for forecasting spatiotemporal dynamics.

### Approved Open Questions
- Higher-dimensional Latent Space Modeling: Determining the optimal dimensionality for latent-space models is critical for balancing the preservation of fine-scale spatiotemporal features with the computational benefits of dimensionality reduction.

## Links

- [Abstract](https://arxiv.org/abs/2606.12141)
- [PDF](https://arxiv.org/pdf/2606.12141)


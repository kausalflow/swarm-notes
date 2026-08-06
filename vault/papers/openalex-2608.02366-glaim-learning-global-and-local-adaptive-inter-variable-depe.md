---
# CSL-compatible fields
title: "GLAIM: Learning Global and Local Adaptive Inter-Variable Dependency for Multivariate Time Series Imputation"
author:
  - literal: "Mingyang Wang"
  - literal: "Ruoyan Li"
  - literal: "Xiao Wang"
  - literal: "Changjian Chen"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.02366"

# Custom fields
paper_id: "2608.02366"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:31:46Z"
created_at: "2026-08-06T07:31:46Z"
---

# GLAIM: Learning Global and Local Adaptive Inter-Variable Dependency for Multivariate Time Series Imputation

**Authors**: Mingyang Wang, Ruoyan Li, Xiao Wang, Changjian Chen
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.02366](https://arxiv.org/abs/2608.02366)

## Summary

The paper introduces GLAIM, a Global-Local Adaptive Inter-variable Dependency Modeling framework for multivariate time series imputation that combines a stable global dependency constructor with a sample-conditioned dependency refiner to handle incomplete observations robustly.

## Key Contributions

- Proposes GLAIM, a Global-Local Adaptive Inter-variable Dependency Modeling framework comprising a Stable Global Dependency Constructor and a Sample-Conditioned Dependency Refiner for robust multivariate time series imputation.
- Derives robust global inter-variable dependencies from complementary temporal representations to serve as a stable backbone less affected by missingness and noise.
- Employs a sample-conditioned dependency refiner that adapts the global backbone to individual sample temporal states and available observations for reliable local refinement under incomplete observations.
- Demonstrates state-of-the-art performance across nine real-world datasets under random and block missingness rates.

## Archivist Review

Applied strict filtering to reject paper-local framework titles (GLAIM) and boilerplate future work suggestions (complex missingness and downstream tasks). Neither candidate meets the high bar for permanent standalone vault entries.

### Rejected Candidates
- [concept] GLAIM (`glaim`) - paper_local: GLAIM is a paper-specific architecture and naming for multivariate time series imputation rather than a reusable vault concept.
- [open_question] Complex Missingness and Downstream Tasks (`complex-missingness-and-downstream-tasks`) - low_impact: This is standard boilerplate future work suggesting the extension of a specific imputation model to other tasks and missingness patterns.

## Links

- [Abstract](https://arxiv.org/abs/2608.02366)
- [PDF](https://arxiv.org/pdf/2608.02366)


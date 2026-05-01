---
# CSL-compatible fields
title: "Density-valued VAR Models with Latent Factors"
author:
  - literal: "Yasumasa Matsuda"
  - literal: "Michel F. C. Haddad"
issued:
  date-parts:
    - [2026, 4, 28]
url: "https://arxiv.org/abs/2604.25087"

# Custom fields
paper_id: "2604.25087"
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
  - "density-valued-vector-autoregression"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-01T07:22:58Z"
created_at: "2026-05-01T07:22:58Z"
---

# Density-valued VAR Models with Latent Factors

**Authors**: Yasumasa Matsuda, Michel F. C. Haddad
**Date**: 2026-04-28
**Paper ID**: [openalex:2604.25087](https://arxiv.org/abs/2604.25087)

## Summary

This paper introduces a density-valued vector autoregressive (VAR) model with latent factors to analyze multivariate time series of density functions. By mapping density estimates into Euclidean space through a generalized logit transform, the model allows for a decomposition of common trends and idiosyncratic, directed dynamics. The approach is demonstrated by identifying the predictive flow of SARS-CoV-2 viral load distributions across Brazilian regions, highlighting the importance of factor-based de-trending in directed network estimation.

## Key Contributions

- Proposes a density-valued VAR model with latent factors, mapping density functions to Euclidean space using a generalized logit transform with an isometric inner product.
- Develops an identification strategy for directed idiosyncratic dynamics using one-sided tests with Benjamini-Yekutieli false discovery rate control.
- Demonstrates that the inclusion of latent factors isolates genuine idiosyncratic dependence from common regional movements in SARS-CoV-2 Ct value distributions.

## Open Questions & Future Work

- [[modeling-general-cross-component-interactions-in-density-var]]

## Key Concepts

- [[density-valued-vector-autoregression]]: A framework for modeling the evolution of multivariate density functions by mapping them to Euclidean space and applying factor-augmented VAR.

## Archivist Review

I approved the core 'Density-Valued Vector Autoregression' concept as it represents a distinct functional extension of classical time-series models, providing a reusable framework for distributional dynamics. The open question regarding cross-component interactions in transformed density spaces was approved as a substantial bottleneck for modeling nuanced distributional evolution. I applied standard naming conventions for both to ensure consistency across the vault.

### Approved Concepts
- Density-Valued Vector Autoregression: It extends classical vector autoregression (VAR) to the functional setting of time-varying probability density functions, which is essential for analyzing distributional dynamics rather than point estimates.

### Approved Open Questions
- Modeling General Cross-Component Interactions: Enables more nuanced characterization of complex distributional dependencies and predictive flows.

### Rejected Candidates
- [open_question] Modeling General Cross-Component Interactions (`density-var-general-cross-component-interactions`) - other: The proposed slug was refined to be more descriptive and conform to standard naming conventions.
- [concept] Density-valued VAR Models with Latent Factors (`density-valued-var-models-with-latent-factors`) - other: The title was renamed to 'Density-Valued Vector Autoregression' to better match the core mechanism name.

## Links

- [Abstract](https://arxiv.org/abs/2604.25087)
- [PDF](https://arxiv.org/pdf/2604.25087)


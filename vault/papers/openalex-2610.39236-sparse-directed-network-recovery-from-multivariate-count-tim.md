---
# CSL-compatible fields
title: "Sparse Directed Network Recovery From Multivariate Count Time Series"
author:
  - literal: "Shirley Mathur"
  - literal: "Nir Keret"
  - literal: "Ali Shojaie"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2610.39236"

# Custom fields
paper_id: "2610.39236"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-01T11:33:23Z"
created_at: "2026-11-01T11:33:23Z"
---

# Sparse Directed Network Recovery From Multivariate Count Time Series

**Authors**: Shirley Mathur, Nir Keret, Ali Shojaie
**Date**: 2026-10-29
**Paper ID**: [openalex:2610.39236](https://arxiv.org/abs/2610.39236)

## Summary

The paper addresses the challenge of inferring sparse directed networks from discrete, overdispersed, and temporally dependent multivariate count time series. The authors propose a multivariate Poisson log-normal model where observed counts are driven by a latent vector autoregressive (VAR) process. To estimate the latent VAR transition matrix, they introduce two procedures: a sparse method-of-moments estimator with guaranteed high-dimensional consistency, and an L1-penalized variational inference estimator. Evaluations via simulations and an application to European freshwater macroinvertebrate abundance data demonstrate successful recovery of interpretable networks.

## Key Contributions

- Proposed a multivariate Poisson log-normal model with a latent vector autoregressive process for network recovery from discrete, overdispersed count time series.
- Established theoretical identifiability conditions and proved consistent high-dimensional sparse network recovery for a proposed method-of-moments estimator.
- Developed an L1-penalized variational inference estimator as a second approach for sparse VAR transition matrix estimation.
- Demonstrated the approach on macroinvertebrate abundance time series from European freshwater ecosystems, yielding an interpretable ecological network.

## Open Questions & Future Work

- [[asymptotic-regime-growing-trajectory-lengths]]

## Archivist Review

The paper presents a statistical framework for count time series network recovery using a multivariate Poisson log-normal model with latent VAR. No reusable machine learning concepts or specific named datasets met the strict vault standards, but the open question regarding asymptotic theory with growing trajectories is retained as a valuable theoretical research direction.

### Approved Open Questions
- Asymptotic Regime with Growing Trajectories: Theoretical results for growing trajectory lengths instead of growing sample sizes would broaden the applicability of sparse latent VAR network recovery to long-term ecological or biological time series data.

### Rejected Candidates
- [concept] Multivariate Poisson Log-Normal VAR Model (`multivariate-poisson-log-normal-var-model`) - not_reusable: The multivariate Poisson log-normal model with latent VAR is a specialized statistical formulation for count network recovery rather than a broadly reusable machine learning forecasting mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2610.39236)
- [PDF](https://arxiv.org/pdf/2610.39236)


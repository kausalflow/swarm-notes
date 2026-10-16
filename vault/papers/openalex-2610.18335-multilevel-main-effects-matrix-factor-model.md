---
# CSL-compatible fields
title: "Multilevel Main Effects Matrix Factor Model"
author:
  - literal: "Kaixin Liu"
  - literal: "Clifford Lam"
  - literal: "Zetai Cen"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.18335"

# Custom fields
paper_id: "2610.18335"
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
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:24:52Z"
created_at: "2026-10-16T09:24:52Z"
---

# Multilevel Main Effects Matrix Factor Model

**Authors**: Kaixin Liu, Clifford Lam, Zetai Cen
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.18335](https://arxiv.org/abs/2610.18335)

## Summary

The authors propose the Multilevel Main Effects Matrix Factor Model (MMEFM) to analyze groups of matrix data by extracting row and column effects. The framework handles nonstationary main effects and yields alignment-independent global common factors, supported by iterative estimation algorithms with established convergence rates and a Bootstrap detection procedure. Simulations and an empirical evaluation on U.S. equity data demonstrate the method's effectiveness over existing matrix time series approaches.

## Key Contributions

- Proposes the Multilevel Main Effects Matrix Factor Model (MMEFM) to extract row and column effects from grouped matrix data.
- Provides rigorous definitions, identification conditions, and iterative estimation algorithms with established rates of convergence for global and local components.
- Establishes that main effects can be nonstationary while remaining consistently estimable at each time point, alongside alignment-independent global common factors.
- Introduces a Bootstrap procedure for detecting the existence and identifying groups of data driven by global common factors.

## Open Questions & Future Work

- [[mefm-asymptotic-normality-inference]]

## Archivist Review

Reviewed the candidate open question on asymptotic normality and statistical inference for matrix factor models, which is an important gap for inference, while rejecting the paper-local concept as too specific. No dataset candidates were provided.

### Approved Open Questions
- Asymptotic Normality and Statistical Inference: Establishing central limit theorems and asymptotic normality is crucial for valid statistical inference, hypothesis testing, and constructing confidence intervals for the estimated parameters in matrix factor models.

### Rejected Candidates
- [concept] Multilevel Main Effects Matrix Factor Model (`mmefm`) - paper_local: Too specific and paper-local to serve as a reusable architectural or methodological primitive in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2610.18335)
- [PDF](https://arxiv.org/pdf/2610.18335)


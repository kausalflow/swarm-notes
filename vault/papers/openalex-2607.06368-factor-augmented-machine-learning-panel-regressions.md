---
# CSL-compatible fields
title: "Factor-Augmented Machine Learning Panel Regressions"
author:
  - literal: "Andrii Babii"
  - literal: "Luca Barbaglia"
  - literal: "Éric Ghysels"
  - literal: "Jonas Striaukas"
issued:
  date-parts:
    - [2026, 7, 7]
url: "https://arxiv.org/abs/2607.06368"

# Custom fields
paper_id: "2607.06368"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  - "factor-augmented-sparse-group-lasso"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-10T08:15:54Z"
created_at: "2026-07-10T08:15:54Z"
---

# Factor-Augmented Machine Learning Panel Regressions

**Authors**: Andrii Babii, Luca Barbaglia, Éric Ghysels, Jonas Striaukas
**Date**: 2026-07-07
**Paper ID**: [openalex:2607.06368](https://arxiv.org/abs/2607.06368)

## Summary

This paper addresses high-dimensional panel data regressions where cross-sectional errors are interdependent due to common latent shocks. The authors propose a factor-augmented sparse-group LASSO estimator that effectively leverages mixed-frequency group structures through MIDAS aggregation. Asymptotic analysis establishes that this approach improves prediction and estimation accuracy compared to standard LASSO models in the presence of common shocks. The framework provides a robust method for panel forecasting in environments with mixed sampling frequencies and pervasive cross-sectional dependencies.

## Key Contributions

- Develops asymptotic theory for high-dimensional panel data regressions with common-shock driven cross-sectional error dependence.
- Introduces a factor-augmented sparse-group LASSO estimator that incorporates mixed-frequency data aggregation (MIDAS).
- Demonstrates theoretical superiority of the proposed estimator over standard LASSO in both prediction and parameter estimation under cross-sectional dependence.

## Open Questions & Future Work

- [[robust-factor-augmented-regression-limits]]

## Key Concepts

- [[factor-augmented-sparse-group-lasso]]: A high-dimensional panel regression estimator that integrates MIDAS aggregation with latent factors and sparse-group LASSO regularization.

## Archivist Review

I approved the central estimator 'Factor-augmented sparse-group LASSO' as it provides a distinct, reusable methodology for mixed-frequency panel forecasting. The open question regarding robustness was approved as it addresses a fundamental limitation in applying these high-dimensional models to real-world financial data. I rejected the initial open question candidate in favor of a slightly renamed, more precise slug for the vault.

### Approved Concepts
- Factor-augmented sparse-group LASSO: This estimator integrates mixed-frequency aggregation (MIDAS) and latent factor modeling with sparse-group LASSO to handle cross-sectional dependence, serving as a core contribution to panel forecasting methodology.

### Approved Open Questions
- Robustness in Factor-Augmented Regression: This is a fundamental theoretical challenge for applying high-dimensional factor-augmented methods to volatile empirical data, where outliers and heavy tails are prevalent.

### Rejected Candidates
- [open_question] Robust Factor-Augmented Panel Regression (`robust-factor-augmented-regression`) - duplicate_existing: Renamed to adhere to more precise naming conventions for the vault.

## Links

- [Abstract](https://arxiv.org/abs/2607.06368)
- [PDF](https://arxiv.org/pdf/2607.06368)


---
# CSL-compatible fields
title: "How Fast Do Signatures Learn? Statistical Theory and Applications for Path Regression"
author:
  - literal: "Blanka Horvath"
  - literal: "Wen Su"
  - literal: "Wu Su"
  - literal: "Binnan Wang"
  - literal: "Ruixun Zhang"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.17865"

# Custom fields
paper_id: "2607.17865"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "embedding"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:27:48Z"
created_at: "2026-07-23T07:27:48Z"
---

# How Fast Do Signatures Learn? Statistical Theory and Applications for Path Regression

**Authors**: Blanka Horvath, Wen Su, Wu Su, Binnan Wang, Ruixun Zhang
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.17865](https://arxiv.org/abs/2607.17865)

## Summary

This paper establishes rigorous approximation and statistical learning theory for signature-based path regression using path signatures. The authors derive minimax optimal $L^2$ approximation rates for smooth functionals of Itô diffusions and prove the consistency of Signature-OLS, Signature-LASSO, and Signature-Logistic estimators. Empirical evaluations across finance, energy, and medicine demonstrate that path signatures provide powerful finite-dimensional feature representations for path-valued covariates.

## Key Contributions

- Established $L^2$ approximation rate for smooth functionals of Itô diffusions using path signatures and proved its minimax optimality.
- Propagated signature truncation error through Signature-OLS, Signature-LASSO, and Signature-Logistic learning procedures to establish statistical consistency.
- Demonstrated superior predictive performance on real-world tasks including foreign exchange volatility forecasting, battery end-of-life prediction, and epileptic seizure detection.

## Open Questions & Future Work

- [[nonsmooth-path-functionals-approximation]]
- [[high-dimensional-signature-dictionaries]]

## Archivist Review

In accordance with the strict filtering criteria and skill-specific review guidance, no new standalone method or architecture concepts were approved since the paper contributes foundational probability and statistical learning theory (path signature approximation rates and consistency). However, two explicit theoretical open questions regarding nonsmooth path functionals and high-dimensional signature dictionaries were approved as they pose durable mathematical research bottlenecks for time series and path regression.

### Approved Open Questions
- Approximation Theory for Nonsmooth Functionals: Extending signature approximation theory to nonsmooth functionals is technically crucial for broader simulation-based pricing, option valuation, and optimal stopping applications where payoffs or constraints are discontinuous.
- Sharper Theory for Signature Dictionaries: Sharper high-dimensional theory for structured signature dictionaries is essential for controlling estimation error and mitigating overfitting in complex real-world path regression tasks.

## Links

- [Abstract](https://arxiv.org/abs/2607.17865)
- [PDF](https://arxiv.org/pdf/2607.17865)


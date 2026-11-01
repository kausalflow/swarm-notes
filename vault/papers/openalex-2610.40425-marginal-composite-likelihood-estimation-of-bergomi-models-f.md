---
# CSL-compatible fields
title: "Marginal Composite Likelihood Estimation of Bergomi Models from High-Frequency Option Prices"
author:
  - literal: "Haruki Tomita"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2610.40425"

# Custom fields
paper_id: "2610.40425"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-01T11:34:34Z"
created_at: "2026-11-01T11:34:34Z"
---

# Marginal Composite Likelihood Estimation of Bergomi Models from High-Frequency Option Prices

**Authors**: Haruki Tomita
**Date**: 2026-10-29
**Paper ID**: [openalex:2610.40425](https://arxiv.org/abs/2610.40425)

## Summary

This paper presents a theoretical framework for estimating kernel parameters in Bergomi-type stochastic volatility models, including the rough Bergomi model, using high-frequency option-price time series. By representing cumulative forward variance via option prices on fine time-maturity grids and applying maturity differences followed by logarithmic time increments, the unobserved forward variance curve is eliminated from the leading term. The authors propose a weighted marginal composite likelihood contrast, proving its consistency and establishing stable asymptotic normality with a deterministic sandwich covariance that is invariant to measure changes.

## Key Contributions

- Developed a marginal composite likelihood estimation framework for Bergomi-type stochastic volatility models using option-price time series on fine time-maturity grids.
- Proved statistical consistency of the estimator without requiring relative rate restrictions between time and maturity meshes, even when the true parameter lies on the boundary.
- Established stable asymptotic normality with a Gaussian limit possessing a deterministic sandwich covariance independent of the terminal model sigma-field, making it invariant to equivalent measure changes.

## Open Questions & Future Work

- [[noisy-irregular-option-data-inference]]

## Archivist Review

Strictly adhered to the review policy by archiving no concepts (as none met the high standalone reusability threshold across future ML/finance literature) while preserving the single focused open question regarding noisy and irregular option data inference.

### Approved Open Questions
- Inference with Noisy Option Data: Extending high-frequency option-based inference to noisy or irregular observational setups is crucial for bridging theoretical rough volatility models with real-world financial data limitations.

### Rejected Candidates
- [open_question] Inference with Noisy Option Data (`noisy-irregular-option-data-inference`) - other: Already checked against vault; however, no concepts met the strict novelty and reusability standard for permanent standalone vault notes.

## Links

- [Abstract](https://arxiv.org/abs/2610.40425)
- [PDF](https://arxiv.org/pdf/2610.40425)


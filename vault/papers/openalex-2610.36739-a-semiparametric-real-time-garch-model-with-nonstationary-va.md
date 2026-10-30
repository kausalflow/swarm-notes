---
# CSL-compatible fields
title: "A Semiparametric Real-Time GARCH Model with Nonstationary Variance"
author:
  - literal: "Muyi Li"
  - literal: "Yajia Chen"
  - literal: "Xu Yuqing"
  - literal: "Feiyu Jiang"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.36739"

# Custom fields
paper_id: "2610.36739"
paper_source: "openalex"
domain: "finance"
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
processed_at: "2026-10-30T11:05:50Z"
created_at: "2026-10-30T11:05:50Z"
---

# A Semiparametric Real-Time GARCH Model with Nonstationary Variance

**Authors**: Muyi Li, Yajia Chen, Xu Yuqing, Feiyu Jiang
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.36739](https://arxiv.org/abs/2610.36739)

## Summary

The authors propose a semiparametric real-time GARCH (SRT-GARCH) model that accounts for nonstationary unconditional variance by decomposing volatility into a smooth deterministic long-run component and a stationary short-run process driven by contemporaneous return innovations. A two-step estimation procedure combining kernel smoothing and conditional Gaussian maximum likelihood is developed, along with proofs of asymptotic normality and consistency under geometric moment contraction. Empirical applications to FTSE 100 returns and U.S. natural gas futures highlight the model's superior forecasting capability and competitive Value-at-Risk performance over standard parametric RT-GARCH benchmarks.

## Key Contributions

- Proposed the semiparametric real-time GARCH (SRT-GARCH) model combining a smooth deterministic long-run volatility component with a stationary short-run process driven by contemporaneous innovations.
- Developed a two-step estimation procedure combining kernel smoothing with conditional Gaussian maximum likelihood and established the consistency and asymptotic normality of the short-run parameter estimator.
- Demonstrated improved volatility forecasting and competitive one-step-ahead Value-at-Risk performance on FTSE 100 returns and U.S. natural gas futures compared to the parametric RT-GARCH benchmark.

## Open Questions & Future Work

- [[non-gaussian-srt-garch-inference]]

## Archivist Review

The review strictly followed the selectivity criteria. No broadly reusable machine learning concepts or named datasets qualified for permanent standalone vault notes. The single open question was evaluated and rejected because it is highly paper-local to the semiparametric GARCH formulation.

### Approved Open Questions
- Non-Gaussian Extensions for SRT-GARCH: Important for generalizing time-series volatility models to real-world financial data that frequently exhibit non-Gaussian features, heavy tails, and asymmetries.

### Rejected Candidates
- [open_question] Non-Gaussian Extensions for SRT-GARCH (`non-gaussian-srt-garch-inference`) - paper_local: The open question is paper-specific and tailored to extending a single niche econometric formulation.

## Links

- [Abstract](https://arxiv.org/abs/2610.36739)
- [PDF](https://arxiv.org/pdf/2610.36739)


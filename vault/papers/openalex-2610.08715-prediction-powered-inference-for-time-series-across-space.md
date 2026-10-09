---
# CSL-compatible fields
title: "Prediction-powered inference for time series across space"
author:
  - literal: "Shahzar Rizvi"
  - literal: "David Burt"
  - literal: "Vishwak Srinivasan"
  - literal: "Renato Berlinghieri"
  - literal: "Stefano Del Col"
  - literal: "Tamara Broderick"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2610.08715"

# Custom fields
paper_id: "2610.08715"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:34:14Z"
created_at: "2026-10-09T11:34:14Z"
---

# Prediction-powered inference for time series across space

**Authors**: Shahzar Rizvi, David Burt, Vishwak Srinivasan, Renato Berlinghieri, Stefano Del Col, Tamara Broderick
**Date**: 2026-10-06
**Paper ID**: [openalex:2610.08715](https://arxiv.org/abs/2610.08715)

## Summary

This paper addresses the challenge of estimating expected labels and constructing valid confidence intervals in spatiotemporal settings where labeled time series are short but unlabeled covariates are available over longer periods. Standard machine learning imputation introduces bias, while classical prediction-powered inference relies on i.i.d. assumptions that fail under temporal dependencies. The authors introduce a robust procedure combining prediction-powered inference with heteroskedasticity and autocorrelation consistent (HAC) techniques to provide reliable estimates and valid confidence intervals. Empirical evaluations show that the proposed method outperforms natural baseline alternatives.

## Key Contributions

- Proposes a statistical framework for prediction-powered inference in spatiotemporal time series settings combining short labeled series, longer unlabeled series, and imperfect machine learning predictors.
- Adapts heteroskedasticity and autocorrelation consistent (HAC) procedures to handle imputed labels and temporal dependencies, yielding valid confidence intervals.
- Demonstrates superior point estimation and confidence interval coverage compared to natural alternatives on spatiotemporal forecasting tasks.

## Open Questions & Future Work

- [[non-stationary-time-series-ppi]]

## Archivist Review

Applied strict vault scarcity standards. No concepts met the high threshold for permanent standalone vault notes, and the candidate open question closely duplicates existing non-stationarity and inference tracking topics in the vault.

### Approved Open Questions
- Prediction-Powered Inference Under Non-Stationarity: Crucial for applying prediction-powered inference methods to real-world environmental and financial time series where long-term stationarity assumptions are violated.

### Rejected Candidates
- [open_question] Prediction-Powered Inference Under Non-Stationarity (`non-stationary-time-series-ppi`) - duplicate_existing: The open question is already covered by existing non-stationarity and conformal/inference open questions in the vault, or is a specific future work direction rather than a foundational vault gap.

## Links

- [Abstract](https://arxiv.org/abs/2610.08715)
- [PDF](https://arxiv.org/pdf/2610.08715)


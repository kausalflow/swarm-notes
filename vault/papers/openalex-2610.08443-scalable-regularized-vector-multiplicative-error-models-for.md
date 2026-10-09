---
# CSL-compatible fields
title: "Scalable Regularized Vector Multiplicative Error Models for Positive-valued Financial Time Series"
author:
  - literal: "Rohan Chhatre"
  - literal: "Chiranjit Dutta"
  - literal: "Налини Равишанкер"
  - literal: "Sumanta Basu"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2610.08443"

# Custom fields
paper_id: "2610.08443"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "multivariate"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:34:08Z"
created_at: "2026-10-09T11:34:08Z"
---

# Scalable Regularized Vector Multiplicative Error Models for Positive-valued Financial Time Series

**Authors**: Rohan Chhatre, Chiranjit Dutta, Налини Равишанкер, Sumanta Basu
**Date**: 2026-10-06
**Paper ID**: [openalex:2610.08443](https://arxiv.org/abs/2610.08443)

## Summary

This paper introduces scalable regularized estimation for logarithmic multiplicative error models (log-vMEM) applied to multivariate positive-valued financial time series. To address the rapid parameter growth and high computational demands in high-dimensional settings, the authors combine hierarchical lag structures with various group penalties, optimized via a blockwise coordinate descent algorithm. Additionally, GPU-accelerated quadrature integration is introduced to overcome the numerical integration bottleneck of the log-likelihood. Evaluations through simulations and intraday realized volatility measures for Microsoft demonstrate the effectiveness and scalability of the proposed approach.

## Key Contributions

- Proposes regularized estimation via hierarchical lag structures for logarithmic multiplicative error models (log-vMEM) with multivariate gamma error distributions.
- Implements an efficient blockwise coordinate descent algorithm with a Gauss-Seidel-style update scheme for parameter estimation, replacing traditional penalized maximum likelihood approaches.
- Addresses computational bottlenecks via GPU-accelerated quadrature integration to improve scalability for high-dimensional multivariate financial time series.
- Evaluates competing models across combinations of three hierarchical lag structures and four group penalties using simulation runs and intraday realized volatility measures for Microsoft (MSFT).

## Open Questions & Future Work

- [[mixture-error-distributions-log-vmems]]

## Archivist Review

Applied high selectivity standards: no overarching standalone forecasting concepts recur universally enough across different architectures to merit permanent vault notes, but the open question regarding mixture error distributions in log-vMEMs addresses a concrete methodological limitation worth tracking.

### Approved Open Questions
- Mixture Error Distributions for Log-vMEMs: Developing flexible mixture error distributions is crucial for accurately modeling extreme financial volatility shocks and tail risks without breaking tractable likelihood estimation.

### Rejected Candidates
- [open_question] Mixture Error Distributions for Log-vMEMs (`mixture-error-distributions-log-vmems`) - other: The candidate is an open question, but scarce limit and review policy require careful selection; however, this is approved since it meets quality standards. Wait, the prompt says approve at most 2 open questions and at most 2 concepts. Let's check if any concept is approved. None. Let's approve the single open question.

## Links

- [Abstract](https://arxiv.org/abs/2610.08443)
- [PDF](https://arxiv.org/pdf/2610.08443)


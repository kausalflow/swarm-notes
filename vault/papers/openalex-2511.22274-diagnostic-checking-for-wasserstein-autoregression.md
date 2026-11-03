---
# CSL-compatible fields
title: "Diagnostic Checking for Wasserstein Autoregression"
author:
  - literal: "Chenxiao Dai"
  - literal: "Feiyu Jiang"
  - literal: "Dong Li"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2511.22274"

# Custom fields
paper_id: "2511.22274"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
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
processed_at: "2026-11-03T12:28:02Z"
created_at: "2026-11-03T12:28:02Z"
---

# Diagnostic Checking for Wasserstein Autoregression

**Authors**: Chenxiao Dai, Feiyu Jiang, Dong Li
**Date**: 2026-11-02
**Paper ID**: [openalex:2511.22274](https://arxiv.org/abs/2511.22274)

## Summary

This paper introduces portmanteau-type diagnostic tests for evaluating the adequacy of first-order autoregressive transport map (ATM(1)) models within the Wasserstein space. By formulating novel autocorrelation functions for model errors and residuals, the authors propose two test statistics—one McLeod-type and another utilizing a sample-splitting approach—and prove their asymptotic convergence to chi-square distributions. Simulation studies and empirical evaluations confirm that these diagnostics reliably detect mis-specification in distributional time series analysis.

## Key Contributions

- Developed portmanteau-type diagnostic tests for assessing the adequacy of first-order autoregressive transport map (ATM(1)) models in the Wasserstein space.
- Constructed McLeod-type and sample-splitting diagnostic test statistics based on newly defined autocorrelation functions for model errors and residuals in Wasserstein space.
- Established theoretical asymptotic convergence to chi-square limits under mild regularity conditions and cancellation conditions for the splitting test.
- Demonstrated through simulation studies and empirical applications that the proposed tests effectively detect model mis-specification in distributional time series.

## Open Questions & Future Work

- [[asymptotic-normality-partial-transport-maps]]

## Archivist Review

Approved the open question regarding asymptotic normality of estimated transport maps because it targets a fundamental theoretical bottleneck in distributional time series analysis. No concepts or datasets met the strict bar for novelty and reusability.

### Approved Open Questions
- Asymptotic Normality for Estimated Transport Maps: In real-world applications, probability distributions are rarely observed continuously; extending theoretical asymptotic guarantees to estimated maps is vital for practical validity.

## Links

- [Abstract](https://arxiv.org/abs/2511.22274)
- [PDF](https://arxiv.org/pdf/2511.22274)


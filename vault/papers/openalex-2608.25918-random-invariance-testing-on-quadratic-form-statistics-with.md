---
# CSL-compatible fields
title: "Random Invariance Testing on Quadratic Form Statistics with Application to Autocorrelation"
author:
  - literal: "Amitakshar Biswas"
  - literal: "Adam B Kashlak"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.25918"

# Custom fields
paper_id: "2608.25918"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "hypothesis-testing"
  - "nonparametric"
  - "statistical-testing"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T17:00:50Z"
created_at: "2026-08-28T17:00:50Z"
---

# Random Invariance Testing on Quadratic Form Statistics with Application to Autocorrelation

**Authors**: Amitakshar Biswas, Adam B Kashlak
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.25918](https://arxiv.org/abs/2608.25918)

## Summary

This paper introduces a unified framework for invariance testing in quadratic form statistics that yields closed-form p-values via concentration inequalities on compact groups, eliminating the need for Monte Carlo simulations. The authors apply this methodology to develop a nonparametric variant of the Durbin-Watson test capable of detecting autocorrelation at arbitrary lags. Evaluations on simulated and real-world time series data demonstrate improved statistical power over classic tests like Breusch-Godfrey and Ljung-Box, including the detection of long-range cycles such as the 11-year solar intensity cycle.

## Key Contributions

- Develops a unified framework for invariance testing in quadratic form statistics with closed-form p-values derived from concentration inequalities on compact groups.
- Proposes a nonparametric variant of the Durbin-Watson test for detecting autocorrelation at arbitrary lags without requiring large-scale Monte Carlo simulations.
- Demonstrates superior statistical power over classic Breusch-Godfrey and Ljung-Box tests on simulated data, and successfully identifies long-range cyclical autocorrelation such as in monthly solar intensity data.

## Open Questions & Future Work

- [[extending-random-invariance-testing-to-other-quadratic-forms]]

## Archivist Review

The paper introduces a rigorous hypothesis testing methodology for quadratic form statistics with closed-form p-values derived from concentration inequalities on compact groups. No architectural concepts or datasets met the strict novelty and reusability standards for permanent vault notes, but the open question regarding the extension of random invariance testing to broader quadratic forms provides a valuable research trajectory.

### Approved Open Questions
- Extending Random Invariance Testing to Other Quadratic Forms: Broadening the applicability of analytical concentration-based permutation/rotation tests to other classical quadratic forms allows computation-free exact or beta-corrected p-value calculations across spatial statistics, contingency tables, and directional data.

## Links

- [Abstract](https://arxiv.org/abs/2608.25918)
- [PDF](https://arxiv.org/pdf/2608.25918)


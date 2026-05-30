---
# CSL-compatible fields
title: "From nonstationarity to stationarity via 1/f noise: discrete Fourier transforms and sample mean asymptotics for testing"
author:
  - literal: "mohamedou Ould Haye"
  - literal: "Anne Philippe"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.28339"

# Custom fields
paper_id: "2605.28339"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "1-f-noise-nonstationarity-test"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:37:08Z"
created_at: "2026-05-30T07:37:08Z"
---

# From nonstationarity to stationarity via 1/f noise: discrete Fourier transforms and sample mean asymptotics for testing

**Authors**: mohamedou Ould Haye, Anne Philippe
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.28339](https://arxiv.org/abs/2605.28339)

## Summary

This paper analyzes the asymptotic behavior of statistics for time series exhibiting long memory and nonstationarity, covering memory parameters from d = -1/2 to 3/2. It specifically investigates the 1/f noise boundary (d=1/2), identifying that logarithmic corrections are necessary to achieve non-degenerate limit distributions for sample statistics. These insights are utilized to develop a novel, parameter-free test for distinguishing nonstationarity from long-memory stationarity.

## Key Contributions

- Derives the joint limiting distribution of discrete Fourier transforms for nonstationary time series with memory parameter d in (-1/2, 3/2).
- Establishes that logarithmic corrections produce non-degenerate limits for sample mean and variance at the 1/f noise (d=1/2) boundary.
- Constructs a consistent, parameter-free statistical test to differentiate nonstationary processes from long-memory stationary processes using low-frequency periodogram ordinates.

## Open Questions & Future Work

- [[tuning-parameter-selection-for-nonstationarity-tests]]

## Key Concepts

- [[1-f-noise-nonstationarity-test]]: A parameter-free statistical test for distinguishing between long-memory stationary processes and nonstationary ones, specifically using low-frequency periodogram ordinates and logarithmic corrections at the d=1/2 boundary.

## Archivist Review

I approved the 1/f noise nonstationarity test as a significant contribution to diagnostic tools in time series analysis, along with the corresponding open question regarding the selection of tuning frequencies. I rejected the initial candidate for open questions as it was too generic, choosing instead to narrow its focus to the specific diagnostic context presented in the paper. No datasets were approved as none were identified as novel or central to the paper.

### Approved Concepts
- 1/f Noise Nonstationarity Test: Provides a rigorous, parameter-free statistical approach to distinguish between nonstationary and long-memory stationary processes, which is a common ambiguity in time series forecasting and econometrics.

### Approved Open Questions
- Tuning Parameter Selection for Nonstationarity Tests: As the primary tuning parameter for frequency-domain tests, the arbitrary or non-optimal selection of 's' fundamentally limits the reliability of nonstationarity diagnostics.

## Links

- [Abstract](https://arxiv.org/abs/2605.28339)
- [PDF](https://arxiv.org/pdf/2605.28339)


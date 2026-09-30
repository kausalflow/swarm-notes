---
# CSL-compatible fields
title: "From HL to H+L-1 Parameters: A Hankel-Toeplitz Forecaster for Long-Term Time Series Forecasting"
author:
  - literal: "Chaoqi Zhang"
  - literal: "Yu Wang"
  - literal: "Haixu Tang"
issued:
  date-parts:
    - [2026, 9, 27]
url: "https://arxiv.org/abs/2609.33984"

# Custom fields
paper_id: "2609.33984"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hankel-toeplitz-forecaster"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:48:34Z"
created_at: "2026-09-30T10:48:34Z"
---

# From HL to H+L-1 Parameters: A Hankel-Toeplitz Forecaster for Long-Term Time Series Forecasting

**Authors**: Chaoqi Zhang, Yu Wang, Haixu Tang
**Date**: 2026-09-27
**Paper ID**: [openalex:2609.33984](https://arxiv.org/abs/2609.33984)

## Summary

The paper investigates how classical stationary prediction theory can guide parameter sharing in linear forecasters, leading to the Hankel-Toeplitz Forecaster (HTF). By leveraging Hankel cross-covariance and inverse Toeplitz covariance matrices, HTF parameterizes the forecast map using only $H+L-1$ trainable coefficients. Empirical evaluations across seven benchmarks show that HTF matches dense linear performance within 1.2% MSE while reducing trainable parameters by 75 to 229 times.

## Key Contributions

- Proposes the Hankel-Toeplitz Forecaster (HTF), a parameter-efficient linear forecasting model requiring only H+L-1 trainable coefficients derived from stationary prediction theory.
- Demonstrates that HTF achieves a horizon-averaged MSE within 1.2% of Dense Linear across seven benchmarks at L=336 while using 75 to 229 times fewer trainable parameters.
- Characterizes the finite-history correction and bounds the excess risk of truncating the true filters under summability assumptions.

## Limitations

Evaluated primarily at a fixed lookback length of L=336.

## Key Concepts

- [[hankel-toeplitz-forecaster]]: A compact linear time series forecaster derived from classical stationary prediction theory that parameterizes the forecast map using H+L-1 coefficients.

## Archivist Review

Approved the core Hankel-Toeplitz Forecaster concept as a novel, principled linear forecasting architecture. No datasets or open questions met the rigorous scarcity and novelty standards.

### Approved Concepts
- Hankel-Toeplitz Forecaster: HTF introduces a principled linear forecasting architecture derived from classical stationary prediction theory that achieves competitive accuracy with orders of magnitude fewer parameters.

## Links

- [Abstract](https://arxiv.org/abs/2609.33984)
- [PDF](https://arxiv.org/pdf/2609.33984)


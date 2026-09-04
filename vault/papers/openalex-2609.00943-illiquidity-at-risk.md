---
# CSL-compatible fields
title: "Illiquidity at Risk"
author:
  - literal: "Demetrio Lacava"
  - literal: "Paolo Santucci de Magistris"
issued:
  date-parts:
    - [2026, 9, 1]
url: "https://arxiv.org/abs/2609.00943"

# Custom fields
paper_id: "2609.00943"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
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
processed_at: "2026-09-04T09:11:24Z"
created_at: "2026-09-04T09:11:24Z"
---

# Illiquidity at Risk

**Authors**: Demetrio Lacava, Paolo Santucci de Magistris
**Date**: 2026-09-01
**Paper ID**: [openalex:2609.00943](https://arxiv.org/abs/2609.00943)

## Summary

This paper introduces Illiquidity-at-Risk (IlliQaR), a novel tail-risk metric designed to quantify extreme liquidity dry-ups by leveraging high-frequency realized Amihud measures. The authors evaluate various linear and non-linear econometric models, highlighting that accounting for discontinuous jump components is essential for capturing severe liquidity evaporation during systemic stress. Empirical analysis on the S&P 500 index and 25 large U.S. equities reveals that broad market liquidity acts as a leading indicator for individual stock illiquidity extremes.

## Key Contributions

- Introduces Illiquidity-at-Risk (IlliQaR), a novel tail-risk metric for quantifying extreme liquidity dry-ups using realized Amihud measures derived from high-frequency data.
- Demonstrates that incorporating discontinuous jump components into linear and non-linear econometric models significantly improves probability coverage and IlliQaR prediction accuracy during systemic market stress.
- Establishes that S&P 500 index liquidity serves as a leading indicator for systemic individual stock liquidity dry-ups, with IlliQaR violations clustering during periods of broad market stress.

## Archivist Review

Reviewed the candidate open question regarding liquidity and price jump disentangling in financial econometrics. As it is highly domain-specific to financial risk management and lacks broader machine learning reusability, it was rejected under the low_impact criterion. No concepts or datasets qualified for permanent standalone vault notes.

### Rejected Candidates
- [open_question] Disentangling Price And Liquidity Jumps (`disentangling-price-and-liquidity-jumps`) - low_impact: The open question addresses a domain-specific financial econometrics issue rather than a broad foundational machine learning or time-series modeling bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.00943)
- [PDF](https://arxiv.org/pdf/2609.00943)


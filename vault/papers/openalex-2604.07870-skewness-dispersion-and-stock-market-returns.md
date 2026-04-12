---
# CSL-compatible fields
title: "Skewness Dispersion and Stock Market Returns"
author:
  - literal: "Mykola Babiak"
  - literal: "Jozef Barunik"
  - literal: "Josef Kurka"
  - literal: ""
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2604.07870"

# Custom fields
paper_id: "2604.07870"
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
processed_at: "2026-04-12T06:20:12Z"
created_at: "2026-04-12T06:20:12Z"
---

# Skewness Dispersion and Stock Market Returns

**Authors**: Mykola Babiak, Jozef Barunik, Josef Kurka, 
**Date**: 2026-04-09
**Paper ID**: [openalex:2604.07870](https://arxiv.org/abs/2604.07870)

## Summary

This paper introduces cross-sectional dispersion in firm-level realized skewness as a novel predictor for stock market returns. The authors demonstrate that this measure has robust out-of-sample predictive power and provides significant economic utility in portfolio allocation strategies. The analysis highlights an information-based mechanism where this dispersion captures the gradual adjustment of stock prices to macroeconomic news, particularly surrounding monetary policy announcements.

## Key Contributions

- Identifies cross-sectional dispersion in firm-level realized skewness as a robust, negative predictor of future stock market returns.
- Demonstrates that skewness dispersion offers incremental predictive power over traditional financial predictors and yields substantial economic gains in portfolio allocation.
- Provides evidence that the forecasting power of skewness dispersion is concentrated around monetary policy announcements, linking it to the information-based gradual incorporation of macro news into stock prices.

## Open Questions & Future Work

- [[kurtosis-vs-skewness-dispersion-predictability]]

## Archivist Review

I approved one open question concerning the decoupling of higher-order moment dispersions, as this addresses a fundamental research bottleneck in finance-domain time-series predictability. The proposed concept of 'skewness dispersion' was rejected because it represents a domain-specific financial indicator rather than a general-purpose forecasting mechanism, representation, or architecture suitable for the vault.

### Approved Open Questions
- Kurtosis vs. Skewness Dispersion Predictability: Disentangling the influence of return asymmetry (skewness) from broader tail-heavy risks (kurtosis) is critical for refining asset pricing models and identifying whether market predictability arises from behavioral or rational risk-adjustment mechanisms.

### Rejected Candidates
- [concept] Cross-sectional skewness dispersion (`skewness-dispersion`) - not_reusable: The metric, while interesting, functions as a domain-specific financial predictor rather than a reusable time-series forecasting mechanism or general architectural concept.

## Links

- [Abstract](https://arxiv.org/abs/2604.07870)
- [PDF](https://arxiv.org/pdf/2604.07870)


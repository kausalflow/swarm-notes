---
# CSL-compatible fields
title: "Beyond Wasserstein Proximity: Finding Better Transfer Sources"
author:
  - literal: "Gordei Verbii"
  - literal: "Georgii Killinkarov"
  - literal: "Vladimir Yafarov"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35314"

# Custom fields
paper_id: "2610.35314"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "transfer-learning"
  - "transformer"
  - "time-series"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:11:27Z"
created_at: "2026-10-29T11:11:27Z"
---

# Beyond Wasserstein Proximity: Finding Better Transfer Sources

**Authors**: Gordei Verbii, Georgii Killinkarov, Vladimir Yafarov
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35314](https://arxiv.org/abs/2610.35314)

## Summary

This paper investigates source selection for transfer learning, challenging the conventional assumption that marginal proximity (measured via Wasserstein distance) identifies the optimal pre-training source. Using a cryptocurrency volatility forecasting task across multiple forecaster families, the authors demonstrate that selecting the farthest source distributions rather than the nearest ones significantly improves transfer performance and forecast skill. Furthermore, forward pilot selection consistently outperforms random transfer, and the study explores how target heterogeneity and temporal-block sensitivity impact source utility.

## Key Contributions

- Demonstrated that selecting distant source distributions ('farthest sources') rather than nearest Wasserstein proximity sources improves forecasting skill by up to 20.90 percentage points for Transformers on cryptocurrency volatility data.
- Showed that forward pilot selection consistently outperforms random transfer across six forecaster families.
- Evaluated performance using ten Binance spot assets over a five-day cryptocurrency volatility benchmark, showing compact recurrent models achieve the lowest absolute mean errors.

## Limitations

Findings are exploratory for a fixed historical panel; retrospective screening analysis does not account for runtime savings.

## Open Questions & Future Work

- [[beyond-wasserstein-transfer-source-selection]]

## Archivist Review

We evaluated the provided candidates against the vault's strict scarcity and reusability standards. No distinct standalone concept notes met the bar for permanence, but the open question regarding transfer source selection beyond marginal Wasserstein distance is a valuable research direction to preserve in the vault. No datasets met vault criteria.

### Approved Open Questions
- Beyond Wasserstein Transfer Source Selection: Understanding how to select transfer sources beyond simple marginal distance is crucial for optimizing pretraining initialization and avoiding negative transfer in time series and neural forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2610.35314)
- [PDF](https://arxiv.org/pdf/2610.35314)


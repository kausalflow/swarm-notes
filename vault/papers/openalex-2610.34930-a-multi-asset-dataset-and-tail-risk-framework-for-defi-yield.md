---
# CSL-compatible fields
title: "A Multi-Asset Dataset and Tail-Risk Framework for DeFi Yield Trading Derivatives"
author:
  - literal: "Huaiyu Jia"
  - literal: "Jieshun You"
  - literal: "Jingyu Liu"
  - literal: "Yizhi Luo"
  - literal: "Shuo Sun"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.34930"

# Custom fields
paper_id: "2610.34930"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tail-mse"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:11:16Z"
created_at: "2026-10-29T11:11:16Z"
---

# A Multi-Asset Dataset and Tail-Risk Framework for DeFi Yield Trading Derivatives

**Authors**: Huaiyu Jia, Jieshun You, Jingyu Liu, Yizhi Luo, Shuo Sun
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.34930](https://arxiv.org/abs/2610.34930)

## Summary

This paper presents a comprehensive study of Decentralized Finance (DeFi) yield trading derivatives by introducing a large-scale 24-month benchmark dataset for the Pendle protocol covering 340 active markets. The authors uncover structural market transitions toward stablecoin-dominated flight-to-quality dynamics and propose Tail-MSE, an asymmetric loss function with dynamic penalty weighting to handle heavy-tailed yield data. Integrating Tail-MSE across six state-of-the-art time series models improves volatility forecasting robustness and yields superior risk-adjusted returns in over half of the evaluated markets.

## Key Contributions

- Constructed the first large-scale benchmark dataset for Pendle spanning 24 months across 340 active markets with complete lifecycle observations.
- Identified a structural market transition toward stablecoin-dominated flight-to-quality dynamics in DeFi yield trading.
- Proposed Tail-MSE, an asymmetric loss function prioritizing tail risk awareness through dynamic penalty weighting for heavy-tailed yield data.
- Demonstrated consistent improvements in volatility forecasting robustness and superior risk-adjusted returns across six state-of-the-art time series models.

## Open Questions & Future Work

- [[adaptive-tail-risk-penalization]]

## Key Concepts

- [[tail-mse]]: An asymmetric loss function with dynamic penalty weighting designed to prioritize tail risk awareness in heavy-tailed yield forecasting.

## Archivist Review

Approved the 'Tail-MSE' loss function concept and the associated open question on adaptive tail risk penalization as they offer reusable contributions for financial forecasting under heavy-tailed distributions. No datasets were approved since none met the strict standalone benchmark criteria.

### Approved Concepts
- Tail-MSE: It introduces a novel asymmetric loss function specifically designed for heavy-tailed yield data in DeFi derivatives.

### Approved Open Questions
- Adaptive Tail Risk Penalization: Dynamic tuning of asymmetric penalty weights is critical for generalizing tail-risk-aware models across diverse and evolving cryptocurrency market conditions.

## Links

- [Abstract](https://arxiv.org/abs/2610.34930)
- [PDF](https://arxiv.org/pdf/2610.34930)


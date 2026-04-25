---
# CSL-compatible fields
title: "Towards Event-Aware Forecasting in DeFi: Insights from On-chain Automated Market Maker Protocols"
author:
  - literal: "Huaiyu Jia"
  - literal: "Jiehshun You"
  - literal: "Yizhi Luo"
  - literal: "Jingyu Liu"
  - literal: "Shuo Sun"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20374"

# Custom fields
paper_id: "2604.20374"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "benchmark"
  - "dataset"
  - "finance"
architectures:
  []
datasets:
  []
concept_slugs:
  - "uncertainty-weighted-mean-squared-error-uwm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-25T06:15:50Z"
created_at: "2026-04-25T06:15:50Z"
---

# Towards Event-Aware Forecasting in DeFi: Insights from On-chain Automated Market Maker Protocols

**Authors**: Huaiyu Jia, Jiehshun You, Yizhi Luo, Jingyu Liu, Shuo Sun
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20374](https://arxiv.org/abs/2604.20374)

## Summary

This paper investigates the event-driven price dynamics of decentralized finance (DeFi) automated market makers, noting that current research fails to capture micro-structural, event-level behavior. To address this, the authors curate a comprehensive, fine-grained dataset of 8.9 million on-chain events across four major protocols. They further propose an Uncertainty Weighted Mean Squared Error (UWM) loss function for Time-Point Process (TPP) models, which significantly improves prediction of block intervals by incorporating uncertainty-aware regression. The results establish a new performance benchmark for modeling the discrete, event-dependent nature of on-chain price discovery.

## Key Contributions

- Constructed a large-scale DeFi event dataset containing 8.9 million records from Pendle, Uniswap v3, Aave, and Morpho protocols.
- Introduced the Uncertainty Weighted Mean Squared Error (UWM) loss function to enhance block interval prediction in Time-Point Process models.
- Achieved a 56.41% average reduction in time prediction error on TPP-based architectures while maintaining event classification accuracy.

## Open Questions & Future Work

- [[event-aware-forecasting-in-defi-amms]]

## Key Concepts

- [[uncertainty-weighted-mean-squared-error-uwm]]: A loss function for Time-Point Processes that integrates block interval regression with homoscedastic uncertainty weighting to improve event timing predictions.

## Archivist Review

The paper proposes a specialized loss function (UWM) for TPP models that is highly relevant to temporal forecasting in discrete, event-driven domains. I have approved this concept and the associated open question regarding the structural modeling of AMM price dynamics. I rejected the inclusion of the dataset as it is a specific domain collection (DeFi protocols) that does not meet the strict "critical named dataset" threshold for permanent archival compared to foundational, cross-disciplinary benchmarks.

### Approved Concepts
- Uncertainty Weighted Mean Squared Error (UWM): Provides a specialized loss function for TPP models to handle the discrete, time-varying nature of DeFi event timing, improving upon standard TPP intensity-based objectives.

### Approved Open Questions
- Event-Aware Forecasting in AMMs: Current TPP models fail to provide high-precision timing forecasts for DeFi market participants, where even block-level latency is a critical factor in arbitrage and liquidation efficiency.

## Links

- [Abstract](https://arxiv.org/abs/2604.20374)
- [PDF](https://arxiv.org/pdf/2604.20374)


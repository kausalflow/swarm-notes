---
# CSL-compatible fields
title: "When do prophets profit in prediction markets?"
author:
  - literal: "Anri Gu"
  - literal: "Nicole Kagan"
  - literal: "Alec Sun"
  - literal: "Jibang Wu"
  - literal: "Haifeng Xu"
issued:
  date-parts:
    - [2026, 7, 7]
url: "https://arxiv.org/abs/2607.06166"

# Custom fields
paper_id: "2607.06166"
paper_source: "openalex"
domain: "finance"
tags:
  - "benchmark"
architectures:
  []
datasets:
  - "kalshi"
concept_slugs:
  - "proper-betting-strategy"
dataset_slugs:
  - "kalshi"
skill: "TimeSeriesSkill"
processed_at: "2026-07-10T08:15:30Z"
created_at: "2026-07-10T08:15:30Z"
---

# When do prophets profit in prediction markets?

**Authors**: Anri Gu, Nicole Kagan, Alec Sun, Jibang Wu, Haifeng Xu
**Date**: 2026-07-07
**Paper ID**: [openalex:2607.06166](https://arxiv.org/abs/2607.06166)

## Summary

This paper resolves the tension between theoretical prediction market efficiency and practical performance in central limit order books where informed agents often underperform. The authors introduce a "proper" betting strategy that links predictive accuracy, measured via strictly proper scoring rules, to expected profit. They prove that this strategy is the unique mechanism for converting accuracy into profit and validate its effectiveness through extensive empirical testing on AI forecasts and a successful month-long live deployment on the Kalshi prediction market.

## Key Contributions

- Establishes a formal equivalence between predictive accuracy and profitability in prediction markets using proper scoring rules.
- Proves that proper betting is the unique strategy providing robust profitability guarantees regardless of specific market order book mechanisms.
- Demonstrates empirical validity of the proper betting strategy with a live deployment on Kalshi yielding +80.33% ROI and a Sharpe ratio of 3.35.

## Open Questions & Future Work

- [[optimizing-prediction-market-profitability]]

## Key Concepts

- [[proper-betting-strategy]]: A betting strategy that directly maps a forecaster's predictive accuracy under a strictly proper scoring rule to expected profit in prediction markets.

## Archivist Review

I approved the 'Proper Betting Strategy' as a foundational mechanism for linking forecasting accuracy to financial performance. I also approved the 'Kalshi' dataset as it represents a significant, live, and specific prediction market environment for evaluating such strategies. Finally, I approved an open question regarding the optimization of prediction market profitability, as it targets critical gaps in risk-adjusted performance and adaptive model selection that extend beyond this specific paper.

### Approved Concepts
- Proper Betting Strategy: It provides a theoretical and practical framework to guarantee profitability in prediction markets based on predictive accuracy, resolving discrepancies between classical theory and order book performance.

### Approved Open Questions
- Optimizing Prediction Market Profitability: Addressing these gaps is essential for bridging the discrepancy between theoretical accuracy and empirical financial performance in prediction markets.

## Datasets

- [[kalshi]]

## Links

- [Abstract](https://arxiv.org/abs/2607.06166)
- [PDF](https://arxiv.org/pdf/2607.06166)


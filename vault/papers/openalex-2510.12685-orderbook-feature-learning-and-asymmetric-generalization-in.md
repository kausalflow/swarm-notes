---
# CSL-compatible fields
title: "Orderbook feature learning and asymmetric generalization in intraday electricity markets"
author:
  - literal: "Runyao Yu"
  - literal: "Ruochen Wu"
  - literal: "Yongsheng Han"
  - literal: "Jochen Cremer"
issued:
  date-parts:
    - [2026, 6, 26]
url: "https://arxiv.org/abs/2510.12685"

# Custom fields
paper_id: "2510.12685"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "asymmetric-generalization-in-financial-markets"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-29T09:20:42Z"
created_at: "2026-06-29T09:20:42Z"
---

# Orderbook feature learning and asymmetric generalization in intraday electricity markets

**Authors**: Runyao Yu, Ruochen Wu, Yongsheng Han, Jochen Cremer
**Date**: 2026-06-26
**Paper ID**: [openalex:2510.12685](https://arxiv.org/abs/2510.12685)

## Summary

This paper addresses the challenge of probabilistic electricity price forecasting by leveraging high-dimensional orderbook data. The authors extract 384 orderbook features and evaluate a broad spectrum of models, ranging from classical statistics to deep learning, across Germany and Austria. The study highlights a novel asymmetric generalization phenomenon, identifying that model transferability between market liquidities is directional, with models moving from liquid to illiquid markets outperforming the reverse transfer. This insight provides a foundational framework for developing more robust, generalizable forecasting systems in competitive energy markets.

## Key Contributions

- Extracted and identified 384 orderbook features to improve probabilistic forecasting in intraday electricity markets.
- Established a comprehensive multi-model benchmark across two distinct markets (Germany and Austria) and two temporal product granularities (60-min and 15-min).
- Demonstrated the asymmetric generalization phenomenon, proving that liquidity-informed training transfer directions significantly impact predictive accuracy.

## Open Questions & Future Work

- [[non-linear-feature-selection-electricity-markets]]

## Key Concepts

- [[asymmetric-generalization-in-financial-markets]]: A phenomenon where predictive models transfer effectively from high-liquidity to low-liquidity domains, but suffer degradation in the reverse direction.

## Archivist Review

The paper introduces a novel empirical finding regarding 'asymmetric generalization' in electricity markets, which is highly reusable in broader time-series forecasting research involving liquidity differentials. The suggested open question on non-linear feature selection identifies a clear research gap in financial time-series modeling. The dataset was rejected as it does not constitute a standardized or widely accessible benchmarking resource.

### Approved Concepts
- Asymmetric Generalization in Financial Markets: Identifies a directional transfer property in financial data that contradicts naive model-sharing assumptions.

### Approved Open Questions
- Non-linear feature selection methods: Linear feature selection can discard features whose predictive utility is purely non-linear, thereby limiting model performance.

### Rejected Candidates
- [dataset] German-Austrian Intraday Electricity Market Data (`german-austrian-intraday-electricity-market-data`) - not_reusable: This is a specific, likely proprietary or regional compilation of market data that lacks the broad community accessibility or standardized definition to serve as a reusable benchmark dataset in the knowledge vault.

## Links

- [Abstract](https://arxiv.org/abs/2510.12685)
- [PDF](https://arxiv.org/pdf/2510.12685)


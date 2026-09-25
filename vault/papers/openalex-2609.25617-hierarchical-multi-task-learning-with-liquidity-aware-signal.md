---
# CSL-compatible fields
title: "Hierarchical Multi-Task Learning with Liquidity-Aware Signals for Stock Forecasting"
author:
  - literal: "H. L. Yang"
  - literal: "Sida Lin"
  - literal: "Yiyan Qi"
  - literal: "Yankai Chen"
  - literal: "Haohan Zhang"
  - literal: "Xianhua Peng"
  - literal: "Jian Guo"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.25617"

# Custom fields
paper_id: "2609.25617"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "mixture-of-experts"
  - "multi-task-learning"
  - "benchmark"
architectures:
  []
datasets:
  - "csi-300-index"
concept_slugs:
  []
dataset_slugs:
  - "csi-300-index"
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:54:40Z"
created_at: "2026-09-25T09:54:40Z"
---

# Hierarchical Multi-Task Learning with Liquidity-Aware Signals for Stock Forecasting

**Authors**: H. L. Yang, Sida Lin, Yiyan Qi, Yankai Chen, Haohan Zhang, Xianhua Peng, Jian Guo
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.25617](https://arxiv.org/abs/2609.25617)

## Summary

Stock price forecasting often struggles due to the conflation of inter-stock and intra-stock temporal dynamics, alongside a reliance on univariate price objectives. To address this, the authors propose LiMT, a hierarchical multi-task learning framework that features a Market Regime Encoder to separate cross-stock and temporal dynamics, and a Liquidity-Driven Learning module utilizing mixture-of-experts to jointly predict price movement, volatility, and volume. Additionally, an Adaptive Portfolio Optimization mechanism translates these multi-task forecasts into executable portfolios under transaction and liquidity constraints, significantly outperforming baselines and equal weighting on CSI300 and CSI500 benchmarks.

## Key Contributions

- Proposed LiMT, a hierarchical multi-task learning framework that decouples cross-stock dependencies and intra-stock temporal dynamics for stock forecasting.
- Introduced a Market Regime Encoder (MRE) to extract contemporaneous cross-stock dependencies followed by temporal dynamics.
- Designed a Liquidity-Driven Learning (LDL) module using a mixture-of-experts architecture with cross-task gating to jointly predict price movement, volatility, and trading volume.
- Developed an Adaptive Portfolio Optimization (APO) mechanism that translates multi-task forecasts into actionable portfolio weights under transaction-cost and liquidity constraints, improving the annualized return on CSI300 from 3.99% to 10.01% and the Sharpe ratio from 1.22 to 1.86.

## Archivist Review

Strict selectivity applied. The core framework concept is paper-local to stock forecasting, and the open question is boilerplate future work. The CSI-300 index dataset is approved as a canonical financial benchmark already in the vault.

### Rejected Candidates
- [concept] LiMT Framework (`limt-framework`) - paper_local: Paper-local architectural framework name for financial forecasting that lacks independent cross-paper currency.
- [open_question] Intraday Microstructure and Alternative Data Forecasting (`intraday-microstructure-and-alternative-data-forecasting`) - weak_evidence: Standard boilerplate future work extension into intraday data and alternative sources.

## Datasets

- [[csi-300-index]]

## Links

- [Abstract](https://arxiv.org/abs/2609.25617)
- [PDF](https://arxiv.org/pdf/2609.25617)


---
# CSL-compatible fields
title: "Pretrained Time-Series Foundation Models for Financial Return Forecasting"
author:
  - literal: "Miquel Noguer I Alonso"
  - literal: "Rodolfo Pereira Franklin"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.27100"

# Custom fields
paper_id: "2606.27100"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "pac-bayes-transfer-intuition-for-pretraining"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:15:26Z"
created_at: "2026-06-28T08:15:26Z"
---

# Pretrained Time-Series Foundation Models for Financial Return Forecasting

**Authors**: Miquel Noguer I Alonso, Rodolfo Pereira Franklin
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.27100](https://arxiv.org/abs/2606.27100)

## Summary

This paper evaluates the performance of leading time-series foundation models (TSFMs) on financial return forecasting, a domain characterized by high noise and low persistence. Through a rigorous rolling-origin evaluation against supervised baselines, the study finds that pretrained TSFMs like Moirai-2.0 and TimesFM-2.5 generally outperform locally-trained architectures in ranking metrics. However, statistical significance testing against random-walk benchmarks reveals that these models do not reliably generate excess predictive accuracy, highlighting a gap between model performance and financial alpha generation. The authors further provide a theoretical framing using PAC-Bayes transfer to explain the limits of generic pretraining in financial time series.

## Key Contributions

- Benchmarks state-of-the-art TSFMs (TimeGPT, TimesFM-2.5, Moirai-2.0, Chronos/Chronos-2) against supervised baselines (NBEATS, NHITS, PatchTST, iTransformer, KAN) in financial return forecasting.
- Demonstrates that while TSFMs dominate leaderboard rankings, their statistical advantage over random-walk benchmarks is limited to sparse cases in noisy market data.
- Establishes a theoretical foundation linking pretraining to PAC-Bayes transfer, explaining why model performance may not guarantee reliable financial alpha.

## Open Questions & Future Work

- [[financial-forecasting-predictability-limits]]

## Key Concepts

- [[pac-bayes-transfer-intuition-for-pretraining]]: A theoretical framework interpreting time-series foundation model pretraining as the acquisition of an inductive prior via PAC-Bayesian principles.

## Archivist Review

Approved the concept relating pretraining to PAC-Bayes as it provides a meaningful theoretical grounding for TSFMs. Approved the open question regarding the disconnect between generic forecasting accuracy and actionable trading alpha, as this is a central bottleneck in financial machine learning. No datasets were approved as the paper utilizes standard market instruments rather than a bespoke, reusable corpus.

### Approved Concepts
- PAC-Bayes transfer intuition for pretraining: Provides a rigorous theoretical bridge connecting the empirical performance of time-series foundation models to statistical learning theory.

### Approved Open Questions
- Predictability vs. Trading Alpha: This question is critical because it highlights the fundamental disconnection between academic time-series benchmarking and the practical requirements of financial engineering, preventing a consensus on how to properly validate models for real-world trading environments.

## Links

- [Abstract](https://arxiv.org/abs/2606.27100)
- [PDF](https://arxiv.org/pdf/2606.27100)


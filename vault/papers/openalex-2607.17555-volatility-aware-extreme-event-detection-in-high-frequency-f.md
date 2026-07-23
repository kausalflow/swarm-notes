---
# CSL-compatible fields
title: "Volatility-Aware Extreme Event Detection in High-Frequency Financial Markets"
author:
  - literal: "Maorufa Zaman"
  - literal: "Haris Md Sahed"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.17555"

# Custom fields
paper_id: "2607.17555"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
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
processed_at: "2026-07-23T07:27:40Z"
created_at: "2026-07-23T07:27:40Z"
---

# Volatility-Aware Extreme Event Detection in High-Frequency Financial Markets

**Authors**: Maorufa Zaman, Haris Md Sahed
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.17555](https://arxiv.org/abs/2607.17555)

## Summary

This study addresses the challenge of extreme price movement prediction in high-frequency financial markets by proposing a volatility-aware target formulation that combines large future returns with high-volatility regimes. Evaluated on Bitcoin limit order book data using XGBoost, the proposed target design mitigates severe class imbalance and non-stationarity, achieving a PR-AUC of 0.40 compared to 0.06 for standard formulations. The findings indicate that deliberate target design is more impactful than model complexity for detecting rare financial events.

## Key Contributions

- Proposes a volatility-aware target formulation for extreme event detection in high-frequency financial markets that incorporates both large future returns and high-volatility regimes.
- Evaluates the proposed approach using Bitcoin limit order book (LOB) data and XGBoost with time-series cross-validation.
- Demonstrates a more than sixfold improvement in Precision-Recall AUC (increasing from ~0.06 to ~0.40) over conventional baseline formulations.

## Limitations

Evaluated primarily on high-frequency Bitcoin limit order book data; generalizability across different asset classes and market structures requires further study.

## Archivist Review

The paper focuses on a target formulation redefinition (volatility-aware labeling) for financial extreme event detection. No permanent conceptual notes or open questions meet our strict novelty and reusability standards, as the proposed approach is closely tied to financial task-specific target design.

### Rejected Candidates
- [open_question] Multi-Stage Directional Extreme Prediction (`multistage-directional-extreme-prediction`) - weak_evidence: Standard future work suggesting the extension of a detection framework to directional prediction, lacking a distinct methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.17555)
- [PDF](https://arxiv.org/pdf/2607.17555)


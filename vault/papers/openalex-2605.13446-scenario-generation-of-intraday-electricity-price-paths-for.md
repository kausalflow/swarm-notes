---
# CSL-compatible fields
title: "Scenario generation of intraday electricity price paths for optimal trading in continuous markets"
author:
  - literal: "Andrzej Puć"
  - literal: "Joanna Janczura"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13446"

# Custom fields
paper_id: "2605.13446"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "support-vector-sorting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:09:47Z"
created_at: "2026-05-16T07:09:47Z"
---

# Scenario generation of intraday electricity price paths for optimal trading in continuous markets

**Authors**: Andrzej Puć, Joanna Janczura
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13446](https://arxiv.org/abs/2605.13446)

## Summary

This paper presents an ensemble forecasting framework for intraday electricity price trajectories designed to support optimal trading in continuous markets. The approach combines corrected Support Vector Regression for point prediction with scenario generation based on fundamental forecast errors to estimate predictive distributions. To efficiently manage these scenarios, the authors propose a novel 'Support Vector Sorting' procedure that selects representative paths. Empirical evaluation using German continuous intraday market data shows that this framework improves both forecast accuracy and economic performance compared to baseline models.

## Key Contributions

- Introduces a framework for ensemble forecasting of intraday electricity prices that bridges probabilistic trajectory generation with adaptive trading decisions.
- Develops a novel Support Vector Sorting procedure to optimize the selection of representative price scenarios from ensemble forecasts.
- Demonstrates that integrating kernel-based learning with scenario-driven uncertainty and dynamic reweighting outperforms standard benchmarks in both statistical accuracy and trading profitability on German intraday market data.

## Open Questions & Future Work

- [[volatility-aware-scenario-reweighting]]

## Key Concepts

- [[support-vector-sorting]]: A scenario reduction technique that selects representative paths from ensemble forecasts by leveraging the geometry of kernel-based regression models.

## Archivist Review

The paper introduces a structured approach to scenario selection and dynamic reweighting for intraday electricity markets. I approved the 'Support Vector Sorting' concept as a reusable scenario reduction mechanism and the 'Volatility-Aware Scenario Reweighting' question as a high-impact research direction for adaptive forecasting systems. No datasets were approved as none were presented as unique or highly reusable named benchmarks in the provided context.

### Approved Concepts
- Support Vector Sorting: This procedure provides a structured method for scenario reduction in probabilistic trajectory forecasting, which is a critical bottleneck in decision-focused forecasting.

### Approved Open Questions
- Volatility-Aware Scenario Reweighting: Explicitly integrating volatility dynamics into the update process is essential for risk management and performance stability in high-frequency financial markets.

## Links

- [Abstract](https://arxiv.org/abs/2605.13446)
- [PDF](https://arxiv.org/pdf/2605.13446)


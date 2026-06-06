---
# CSL-compatible fields
title: "Expectations vs. Realities: The Cost of MSE-Optimal Forecasting Under Conditional Uncertainty"
author:
  - literal: "Riku Green"
  - literal: "Zahraa S. Abdallah"
  - literal: "Telmo M Silva Filho"
issued:
  date-parts:
    - [2026, 6, 3]
url: "https://arxiv.org/abs/2606.04342"

# Custom fields
paper_id: "2606.04342"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "accuracy-realism-trade-off-in-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-06T07:39:52Z"
created_at: "2026-06-06T07:39:52Z"
---

# Expectations vs. Realities: The Cost of MSE-Optimal Forecasting Under Conditional Uncertainty

**Authors**: Riku Green, Zahraa S. Abdallah, Telmo M Silva Filho
**Date**: 2026-06-03
**Paper ID**: [openalex:2606.04342](https://arxiv.org/abs/2606.04342)

## Summary

This paper investigates the limitations of evaluating multi-step time series forecasting models primarily through mean squared error (MSE), which tends to neglect conditional uncertainty at longer horizons. The authors formalize the 'conditional uncertainty gap' and prove that MSE-optimal predictors inherently fail to match the marginal distribution of realized future outcomes. Through empirical analysis across nine datasets, the study quantifies a clear Pareto frontier between accuracy and realism, revealing that modest sacrifices in MSE can yield significant gains in realistic marginal variability.

## Key Contributions

- Identified and formalized a fundamental trade-off between MSE-optimal point accuracy and marginal distribution realism in multi-step time series forecasting.
- Quantified the 'accuracy-realism' Pareto frontier across nine benchmarks, demonstrating that a <5% relaxation in MSE can lead to >17% median improvements in marginal realism.
- Exposed structural differences in existing strategies, showing that direct multi-output predictors favor accuracy, while recursive and sample-based methods favor marginal realism.

## Open Questions & Future Work

- [[accuracy-realism-stochastic-predictors-limitations]]
- [[trajectory-realism-evaluation-metrics]]

## Key Concepts

- [[accuracy-realism-trade-off-in-forecasting]]: The mathematical trade-off between point-wise accuracy (MSE) and marginal distribution realism in multi-step time series forecasting.

## Archivist Review

The paper provides a significant theoretical contribution by formalizing the 'accuracy-realism' trade-off, which addresses a well-known structural failure of MSE-based evaluation in long-horizon forecasting. I have approved the overarching concept and two research questions that identify core challenges for future stochastic forecasting architectures and metric development. Other candidates were rejected to maintain the required scarcity of the vault.

### Approved Concepts
- Accuracy-Realism Trade-off in Forecasting: Formalizes a fundamental conflict between minimizing mean squared error and preserving realistic data distributions in long-horizon forecasting, which is a major bottleneck in the field.

### Approved Open Questions
- Stochastic Predictors Accuracy-Realism Limits: Understanding if stochastic predictors can overcome the fundamental limitations identified for deterministic models is central to advancing robust long-horizon forecasting architectures.
- Robust Trajectory Realism Metrics: Establishing specialized metrics to distinguish between different facets of forecasting quality is essential for moving beyond scalar MSE-based evaluation in complex, non-stationary real-world environments.

## Links

- [Abstract](https://arxiv.org/abs/2606.04342)
- [PDF](https://arxiv.org/pdf/2606.04342)


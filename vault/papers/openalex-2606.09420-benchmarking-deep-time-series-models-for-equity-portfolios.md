---
# CSL-compatible fields
title: "Benchmarking Deep Time Series Models for Equity Portfolios"
author:
  - literal: "Aoxin Zhang"
  - literal: "Yuhan Cheng"
  - literal: "Kwanting Leung"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.09420"

# Custom fields
paper_id: "2606.09420"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "deployment-adjusted-acceptability-index"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:07:00Z"
created_at: "2026-06-11T09:07:00Z"
---

# Benchmarking Deep Time Series Models for Equity Portfolios

**Authors**: Aoxin Zhang, Yuhan Cheng, Kwanting Leung
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.09420](https://arxiv.org/abs/2606.09420)

## Summary

This paper introduces a comprehensive benchmarking framework for deep time-series models within the context of daily equity portfolio management. By moving beyond raw forecasting metrics, the authors utilize a deployment-adjusted acceptability index that accounts for transaction costs, risk constraints, and investor preferences. Empirical results on a 2018-2024 CRSP dataset reveal that no single architecture dominates the landscape, highlighting the significant divergence between predictive accuracy and real-world trading utility. The study underscores that model selection requires rigorous diagnostics beyond pure error metrics to ensure viability in constrained portfolio environments.

## Key Contributions

- Constructed a robust benchmarking protocol for 15 time-series architectures using daily CRSP equity data spanning 2018-2024.
- Introduced the Deployment-Adjusted Acceptability Index (DAAI) to evaluate model usability under realistic portfolio constraints and transaction costs.
- Demonstrated that raw forecasting accuracy does not consistently predict portfolio performance, with TransEnc-8 emerging as the most stable performer under diverse constraints.

## Open Questions & Future Work

- [[advanced-distributionally-robust-portfolio-layers]]

## Key Concepts

- [[deployment-adjusted-acceptability-index]]: A performance metric that ranks forecasting models by integrating SMAA rank-acceptability distributions with portfolio-level regret and constraints.

## Archivist Review

I approved the Deployment-Adjusted Acceptability Index as a novel and reusable evaluation concept for finance-oriented time-series forecasting. I also approved the open question regarding distributionally robust portfolio layers, as this addresses a specific, fundamental limitation in the evaluation of forecasting-to-trading pipelines. I rejected the preference elicitation question because it is more of a domain-specific policy requirement than a core research problem for the forecasting field.

### Approved Concepts
- Deployment-adjusted acceptability index: This metric specifically addresses the gap between forecasting accuracy and real-world portfolio usability by incorporating preference-based regret.

### Approved Open Questions
- Distributionally Robust Portfolio Layers: Standard constrained-QP layers often fail to account for the full complexity of market regimes, making them a bottleneck in assessing the practical viability of deep time-series models.

### Rejected Candidates
- [open_question] Institutional Preference Elicitation Frameworks (`institutional-preference-elicitation-in-portfolio-benchmarking`) - low_impact: The prompt for preference elicitation is largely a function of user-side business requirements rather than a fundamental unresolved research problem in time-series forecasting itself.

## Links

- [Abstract](https://arxiv.org/abs/2606.09420)
- [PDF](https://arxiv.org/pdf/2606.09420)


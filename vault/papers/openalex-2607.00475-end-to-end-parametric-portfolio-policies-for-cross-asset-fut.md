---
# CSL-compatible fields
title: "End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing: When Do AI Models Beat Simple Rules?"
author:
  - literal: "Austin Pollok"
  - literal: "Kevin Robik"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00475"

# Custom fields
paper_id: "2607.00475"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "transformer"
  - "time-series"
  - "finance"
architectures:
  - "transformer"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:36:33Z"
created_at: "2026-07-04T07:36:33Z"
---

# End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing: When Do AI Models Beat Simple Rules?

**Authors**: Austin Pollok, Kevin Robik
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00475](https://arxiv.org/abs/2607.00475)

## Summary

This paper investigates end-to-end AI-based portfolio policies that directly map market states to asset weights, bypassing traditional decoupled forecasting and optimization steps. By training on sixteen liquid CME futures using a differentiable Sharpe ratio loss, the authors evaluate the performance of LSTM and transformer architectures against standard rules-based strategies. The results indicate that transformer-based policies achieve superior risk-adjusted performance and lower trading turnover, though the competitive advantage over simple heuristic rules is constrained by transaction costs.

## Key Contributions

- Introduces an end-to-end portfolio policy that maps market states directly to weights using a differentiable Sharpe ratio loss.
- Compares end-to-end AI policies (LSTM vs. Transformer) against classic rules-based benchmarks (Equal Weighting, Risk Parity, Time-Series Momentum) on 16 liquid CME futures.
- Demonstrates that while Transformers provide superior learned policies with lower turnover than LSTMs, their outperformance relative to simple rules remains sensitive to transaction costs.

## Open Questions & Future Work

- [[scaling-end-to-end-policies]]

## Archivist Review

The paper presents an empirical application of end-to-end policy learning in finance. I have rejected the higher-frequency open question as it is a standard performance improvement path rather than a novel bottleneck. I approved the scaling question as it addresses the architectural requirement of modeling heterogeneous cross-asset dependencies, which is a significant research direction for end-to-end portfolio optimization.

### Approved Open Questions
- Scaling End-to-End Portfolio Policies: This addresses a fundamental scaling bottleneck in quantitative finance where capturing meaningful patterns across an expansive, heterogeneous asset universe is essential for robust, diversified strategies.

### Rejected Candidates
- [open_question] Higher-frequency end-to-end allocation (`higher-frequency-end-to-end-allocation`) - low_impact: The question is a routine extension of frequency, which is common in time-series forecasting research rather than a fundamental theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.00475)
- [PDF](https://arxiv.org/pdf/2607.00475)


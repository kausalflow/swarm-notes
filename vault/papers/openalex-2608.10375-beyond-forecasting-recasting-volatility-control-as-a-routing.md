---
# CSL-compatible fields
title: "Beyond Forecasting: Recasting Volatility Control as a Routing Problem"
author:
  - literal: "Hongji Pu"
  - literal: "Leyang Zhou"
issued:
  date-parts:
    - [2026, 8, 11]
url: "https://arxiv.org/abs/2608.10375"

# Custom fields
paper_id: "2608.10375"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "reinforcement-learning"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "volrouter"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-14T06:07:33Z"
created_at: "2026-08-14T06:07:33Z"
---

# Beyond Forecasting: Recasting Volatility Control as a Routing Problem

**Authors**: Hongji Pu, Leyang Zhou
**Date**: 2026-08-11
**Paper ID**: [openalex:2608.10375](https://arxiv.org/abs/2608.10375)

## Summary

The paper proposes VolRouter, a modular framework that recasts volatility control as state-conditioned routing over estimator-controller pairs to better adapt risk management to changing market conditions. By summarizing market states and routing through state inference, switch review, and pair selection stages, VolRouter improves risk-adjusted returns and reduces drawdown across various equity, multi-asset, and cryptocurrency settings. Ablation analyses indicate that these improvements stem from relative policy evaluation and selective persistent switching rather than expanding the policy library.

## Key Contributions

- Proposed VolRouter, a modular framework that reformulates volatility control as state-conditioned routing over estimator-controller pairs.
- Improved Sharpe ratio on S&P 500 from 0.952 (RV + Naive Scaling) to 1.222 while reducing maximum drawdown from 15.10% to 12.58% and daily CVaR from 1.76% to 1.32%.
- Improved Sharpe ratio on Multi-Asset from 1.498 to 1.540 and reduced CVaR from 1.56% to 1.18%.
- Demonstrated through ablation and sensitivity analyses that performance gains stem from relative policy evaluation and selective persistent switching rather than library size expansion.

## Limitations

USDT provides a boundary case where simpler state-aware selectors remain competitive, indicating limited utility in low-volatility pegged assets.

## Open Questions & Future Work

- [[boundary-conditions-for-volatility-routing]]

## Key Concepts

- [[volrouter]]: A modular framework that formulates volatility control as state-conditioned routing over estimator-controller pairs.

## Archivist Review

Approved the core VolRouter framework as a distinctive and reusable methodology for risk management, along with one precise open question concerning its boundary conditions in low-volatility regimes. Rejected redundant concept restatements.

### Approved Concepts
- VolRouter: Central framework proposed in the paper that reformulates volatility control as a routing problem.

### Approved Open Questions
- Boundary Conditions for Volatility Routing: Understanding the exact boundary conditions where policy routing outperforms static or simple adaptive methods prevents over-engineering in stable or low-volatility asset classes.

### Rejected Candidates
- [concept] Volatility Control Routing (`volatility-control-routing`) - duplicate_existing: Redundant with VolRouter concept which captures the exact same methodological novelty.

## Links

- [Abstract](https://arxiv.org/abs/2608.10375)
- [PDF](https://arxiv.org/pdf/2608.10375)


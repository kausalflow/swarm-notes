---
# CSL-compatible fields
title: "Robust Unit Commitment in District Heating Networks: Chance-Constrained and CVaR Optimization Under Demand Uncertainty"
author:
  - literal: "Annika Buchholz"
  - literal: "Janina Zittel"
  - literal: "Thorsten Koch"
issued:
  date-parts:
    - [2026, 8, 11]
url: "https://arxiv.org/abs/2608.10899"

# Custom fields
paper_id: "2608.10899"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "optimization"
  - "robustness"
  - "uncertainty-quantification"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-14T06:07:42Z"
created_at: "2026-08-14T06:07:42Z"
---

# Robust Unit Commitment in District Heating Networks: Chance-Constrained and CVaR Optimization Under Demand Uncertainty

**Authors**: Annika Buchholz, Janina Zittel, Thorsten Koch
**Date**: 2026-08-11
**Paper ID**: [openalex:2608.10899](https://arxiv.org/abs/2608.10899)

## Summary

This paper addresses operational planning in district heating networks under demand uncertainty by formulating chance-constrained programming and conditional value-at-risk (CVaR) optimization for the mixed-integer unit-commitment problem. Heat demand time series are generated using a Bayesian model that provides predictive distributions to account for forecasting uncertainty. The chance-constrained approach limits the probability of unmet demand, whereas CVaR optimization penalizes severe tail shortfalls. Evaluations on real-world data from the Berlin district heating network and synthetic benchmark instances provide comparisons of solution quality, risk exposure, and computational effort.

## Key Contributions

- Adapted chance-constrained programming and conditional value-at-risk (CVaR) optimization to the mixed-integer unit-commitment problem for district heating networks under heat demand uncertainty.
- Generated heat demand time series using a Bayesian model that quantifies forecasting uncertainty to produce predictive distributions for network optimization.
- Evaluated solution quality, risk exposure, and computational effort on real-world data from the Berlin district heating network and synthetic benchmark instances.

## Archivist Review

No novel concepts or open questions met the high selectivity threshold for permanent vault notes. The paper applies established robust optimization techniques (chance constraints and CVaR) to district heating networks, and the proposed open questions are standard extensions.

### Rejected Candidates
- [open_question] Multi-Commodity Price Uncertainty Integration (`multi-commodity-price-uncertainty`) - low_impact: Standard future work extending the domain scope to additional market variables.
- [open_question] Multi-Objective Emissions Minimization (`multi-objective-emissions-minimization`) - low_impact: Standard multi-objective optimization extension without a novel methodological bottleneck.
- [open_question] Two-Stage Commitment and Dispatch Model (`two-stage-commitment-dispatch-model`) - low_impact: Standard two-stage stochastic programming formulation for unit commitment problems.

## Links

- [Abstract](https://arxiv.org/abs/2608.10899)
- [PDF](https://arxiv.org/pdf/2608.10899)


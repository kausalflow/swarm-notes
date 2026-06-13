---
# CSL-compatible fields
title: "Weibull-Stationary Stochastic Differential Equations for Conditional Long-Horizon Wind Power Forecasting"
author:
  - literal: "Luca Di Persio"
  - literal: "Mehrdad Ghadiri"
issued:
  date-parts:
    - [2026, 6, 10]
url: "https://arxiv.org/abs/2606.12097"

# Custom fields
paper_id: "2606.12097"
paper_source: "openalex"
domain: "time-series,energy"
tags:
  - "time-series"
  - "forecasting"
  - "stochastic-differential-equation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "weibull-stationary-stochastic-differential-equations"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-13T08:16:18Z"
created_at: "2026-06-13T08:16:18Z"
---

# Weibull-Stationary Stochastic Differential Equations for Conditional Long-Horizon Wind Power Forecasting

**Authors**: Luca Di Persio, Mehrdad Ghadiri
**Date**: 2026-06-10
**Paper ID**: [openalex:2606.12097](https://arxiv.org/abs/2606.12097)

## Summary

This paper presents a probabilistic forecasting framework for wind power that reconciles long-horizon statistical stationarity with short-term stochastic dynamics. The authors estimate monthly Weibull parameters using a heteroskedastic Kalman filter on a bivariate VAR(1) model and incorporate these as priors for three positive-valued SDE formulations. Experimental results on real-world turbine data show that a diffusion-first SDE model maintains high predictive accuracy while significantly outperforming alternative models in computational efficiency. The framework provides robust probabilistic inputs for downstream operational decision-making in the energy sector.

## Key Contributions

- Introduces a Weibull-stationary SDE framework for conditional, long-horizon probabilistic wind power forecasting at high temporal resolution.
- Demonstrates that a Fokker-Planck diffusion-first SDE formulation achieves equivalent probabilistic accuracy to more complex OU-Weibull models while reducing computational runtime by a factor of seven.
- Achieves high forecasting precision with exceedance-probability errors below 1.6 percentage points and Wasserstein distribution distances below 1.4% of rated turbine capacity.

## Open Questions & Future Work

- [[marginalizing-parameter-uncertainty-in-sde-forecasting]]

## Key Concepts

- [[weibull-stationary-stochastic-differential-equations]]: A framework integrating Weibull distribution parameters into SDE models to enable long-horizon probabilistic forecasting of positive, stationary wind speed processes.

## Archivist Review

I have approved the core SDE framework for wind forecasting and the open question regarding parameter marginalization, as these represent significant theoretical contributions to time-series forecasting. The proposal for alternative distributions was rejected as a boilerplate research direction, and no new datasets were added due to the scarcity requirement.

### Approved Concepts
- Weibull-Stationary Stochastic Differential Equations: Provides a theoretical bridge between long-term parametric climate statistics (Weibull) and short-term stochastic dynamics (SDEs) for non-negative wind power forecasting.

### Approved Open Questions
- Full Parameter Marginalization in SDEs: Propagating parameter uncertainty is critical for reliable decision-making in power system operations like reserve scheduling and energy storage sizing.

### Rejected Candidates
- [open_question] Alternative Distributions for Extreme Winds (`beyond-weibull-distributions-for-extreme-winds`) - weak_evidence: While important, the specific request for alternative distributions is a routine suggestion for model expansion rather than a fundamental theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2606.12097)
- [PDF](https://arxiv.org/pdf/2606.12097)


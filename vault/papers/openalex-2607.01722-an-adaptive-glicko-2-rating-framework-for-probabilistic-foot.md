---
# CSL-compatible fields
title: "An Adaptive Glicko-2 Rating Framework for Probabilistic Football Forecasting and Season Simulation"
author:
  - literal: "Bich Van Nguyen"
  - literal: "Nam Tran"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.01722"

# Custom fields
paper_id: "2607.01722"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "probabilistic-forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-glicko-2-football-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:52:41Z"
created_at: "2026-07-05T07:52:41Z"
---

# An Adaptive Glicko-2 Rating Framework for Probabilistic Football Forecasting and Season Simulation

**Authors**: Bich Van Nguyen, Nam Tran
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.01722](https://arxiv.org/abs/2607.01722)

## Summary

This paper presents an adaptive Glicko-2 rating framework specifically engineered for probabilistic football forecasting. The method improves upon classical rating systems by accounting for football-specific dynamics such as margin-of-victory, structural shocks, and home advantage within an ordered-logit model. By dynamically estimating latent team strengths, the framework generates accurate win-draw-loss probabilities, which are then used in Monte Carlo simulations to forecast the progression of full football league seasons.

## Key Contributions

- Introduces an adaptive Glicko-2 framework incorporating margin-of-victory, dominance weighting, and structural shocks for dynamic team strength estimation.
- Integrates an ordered-logit draw model to resolve the unique role of draws in football outcome distributions.
- Provides a probabilistic league-level simulator using Monte Carlo sampling to project seasonal outcomes based on dynamically updated latent team strengths.

## Open Questions & Future Work

- [[team-specific-structural-shock-modeling]]

## Key Concepts

- [[adaptive-glicko-2-football-forecasting]]: An extension of the Glicko-2 rating system tailored for football that incorporates contextual adjustments to output win-draw-loss probabilities for season-level simulations.

## Archivist Review

I have approved the core rating framework as it provides a modular, reusable approach to extending classic Bayesian rating systems for specific sports domain dynamics. I also approved the open question regarding team-specific shock modeling, as this represents a substantial bottleneck in sports forecasting where roster and management volatility significantly impact predictive accuracy.

### Approved Concepts
- Adaptive Glicko-2 Football Forecasting: Extends Glicko-2 rating system specifically for football to include margin-of-victory adjustment, dominance weighting, and structural shocks while enabling league-level Monte Carlo simulations.

### Approved Open Questions
- Team-Specific Structural Shock Modeling: Improving the responsiveness of rating systems to structural shocks is critical for maintaining the accuracy of dynamic strength estimates in professional sports.

## Links

- [Abstract](https://arxiv.org/abs/2607.01722)
- [PDF](https://arxiv.org/pdf/2607.01722)


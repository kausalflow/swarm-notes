---
# CSL-compatible fields
title: "Phase transition in a long-memory log-Gaussian Cox process"
author:
  - literal: "Masato Hisakado"
  - literal: "Shintaro Mori"
issued:
  date-parts:
    - [2026, 8, 18]
url: "https://arxiv.org/abs/2505.13822"

# Custom fields
paper_id: "2505.13822"
paper_source: "openalex"
domain: "finance"
tags:
  - "stochastic-process"
  - "time-series"
  - "anomaly-detection"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-20T05:21:23Z"
created_at: "2026-08-20T05:21:23Z"
---

# Phase transition in a long-memory log-Gaussian Cox process

**Authors**: Masato Hisakado, Shintaro Mori
**Date**: 2026-08-18
**Paper ID**: [openalex:2505.13822](https://arxiv.org/abs/2505.13822)

## Summary

This paper investigates a stochastic point process with power-law temporal correlations driven by hidden variables, demonstrating its convergence to a log-Gaussian Cox process (LGCP) via a generalized Merton model under a double-scaling limit. The authors prove that the resulting LGCP exhibits a phase transition at the critical power index gamma = 1, separating short-memory dynamics from long-memory anomalous diffusion, and show that temporal correlations persist in the Poisson limit. Furthermore, they compare this process with Hawkes processes and validate the theoretical findings using historical default data from pre-1980 credit portfolios.

## Key Contributions

- Established that a generalized Merton type model with a logistic CDF under a double-scaling limit converges to a log-Gaussian Cox process (LGCP) with log-normal intensity.
- Demonstrated that the resulting LGCP exhibits a phase transition at the critical power index gamma = 1, separating short-memory dynamics from long-memory behavior characterized by anomalous diffusion.
- Showed that temporal correlations persist even in the Poisson limit under proper scaling, unlike conventional Poisson convergence.
- Provided empirical evidence of long-memory behavior in pre-1980 credit portfolios by estimating the temporal correlation parameter from historical default data.

## Open Questions & Future Work

- [[combining-self-exciting-and-macro-driven-phase-transitions]]

## Archivist Review

Rigorously applied scarcity and novelty standards. No core machine learning concepts or architectures were introduced that warrant standalone vault notes, but the open question regarding the combination of self-exciting and macro-driven phase transitions was retained as a valuable theoretical research direction.

### Approved Open Questions
- Combining Self-Exciting and Macro-Driven Models: Combining self-excitation and macroeconomic frailty addresses a fundamental gap in credit risk modeling, bridging contagion-based models and intensity-based macro-driven models.

## Links

- [Abstract](https://arxiv.org/abs/2505.13822)
- [PDF](https://arxiv.org/pdf/2505.13822)


---
# CSL-compatible fields
title: "Real-Time Control of Sustainable Data Centers: A Two-Layer Model Predictive Control Framework with Workload Flexibility and Heat Recovery"
author:
  - literal: "Wenyu Liu"
  - literal: "Enea Figini"
  - literal: "Mario Paolone"
issued:
  date-parts:
    - [2026, 8, 17]
url: "https://arxiv.org/abs/2608.16432"

# Custom fields
paper_id: "2608.16432"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "reinforcement-learning"
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
processed_at: "2026-08-20T05:21:45Z"
created_at: "2026-08-20T05:21:45Z"
---

# Real-Time Control of Sustainable Data Centers: A Two-Layer Model Predictive Control Framework with Workload Flexibility and Heat Recovery

**Authors**: Wenyu Liu, Enea Figini, Mario Paolone
**Date**: 2026-08-17
**Paper ID**: [openalex:2608.16432](https://arxiv.org/abs/2608.16432)

## Summary

This paper proposes a two-layer model predictive control (MPC) framework for the real-time operation of sustainable data centers equipped with photovoltaic generation, battery storage, and waste heat recovery. The upper layer uses scenario-based stochastic optimization for intraday market participation and energy management, while the lower layer employs an adaptive tube-based MPC strategy to compensate for short-term disturbances. Microservice-based simulations show that this framework effectively handles photovoltaic and workload fluctuations, significantly reducing dispatch deviations and imbalance costs compared to single-layer baselines.

## Key Contributions

- Proposes a two-layer model predictive control framework combining scenario-based stochastic optimization at the upper layer and adaptive tube-based MPC at the lower layer for sustainable data centers.
- Integrates workload flexibility, on-site photovoltaic generation, battery energy storage, waste heat recovery, and district heating into a unified real-time management system.
- Demonstrates via microservice-based simulations that the adaptive lower-layer controller substantially reduces real-time dispatch deviations and imbalance costs compared to single-layer control strategies.

## Archivist Review

The paper presents a two-layer model predictive control framework for sustainable data centers, combining scenario-based stochastic optimization and adaptive tube-based MPC. Since this is primarily an optimal control and energy systems paper rather than a machine learning or time-series methodology paper, no concepts or open questions qualify for standalone vault notes under our selective knowledge criteria.

### Rejected Candidates
- [open_question] Joint Multi-Market Optimization (`joint-multi-market-optimization-data-centers`) - low_impact: Future work on extending market participation across multiple electricity markets is application-specific energy systems research rather than an unresolved ML-specific forecasting or modeling bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.16432)
- [PDF](https://arxiv.org/pdf/2608.16432)


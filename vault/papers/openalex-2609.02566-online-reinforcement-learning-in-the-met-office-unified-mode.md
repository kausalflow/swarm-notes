---
# CSL-compatible fields
title: "Online Reinforcement Learning in the Met Office Unified Model through Distributed Model-Agent Coupling"
author:
  - literal: "Pritthijit Nath"
  - literal: "Sebastian Schemm"
  - literal: "Peter Haynes"
  - literal: "Emily Shuckburgh"
  - literal: "Mark Webb"
issued:
  date-parts:
    - [2026, 9, 2]
url: "https://arxiv.org/abs/2609.02566"

# Custom fields
paper_id: "2609.02566"
paper_source: "openalex"
domain: "time-series"
tags:
  - "reinforcement-learning"
  - "forecasting"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-05T08:42:06Z"
created_at: "2026-09-05T08:42:06Z"
---

# Online Reinforcement Learning in the Met Office Unified Model through Distributed Model-Agent Coupling

**Authors**: Pritthijit Nath, Sebastian Schemm, Peter Haynes, Emily Shuckburgh, Mark Webb
**Date**: 2026-09-02
**Paper ID**: [openalex:2609.02566](https://arxiv.org/abs/2609.02566)

## Summary

This paper presents an online reinforcement learning framework coupled directly with the Met Office Unified Model (UM) using rank-local tensors for distributed agents to learn potential-temperature tendency corrections. By training across ten nudged forecasts against operational analysis and evaluating in non-nudged inference, the method maintains numerical stability and achieves substantial error reductions in geopotential height (Z500) and mean sea level pressure (MSLP) across multiple latitude bands compared to native numerical weather predictions.

## Key Contributions

- Coupled the Met Office Unified Model (UM) with distributed reinforcement learning agents via rank-local tensors for online correction of model tendencies.
- Demonstrated numerical stability and training completion across ten nudged training forecasts using operational analysis targets.
- Achieved significant error reductions in non-nudged inference, including a 45.8% reduction in Z500 MAE in the northern tropics and a 27.3% reduction in MSLP error at 0-30°N compared to native UM forecasts.

## Links

- [Abstract](https://arxiv.org/abs/2609.02566)
- [PDF](https://arxiv.org/pdf/2609.02566)


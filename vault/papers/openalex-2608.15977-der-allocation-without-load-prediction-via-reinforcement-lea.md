---
# CSL-compatible fields
title: "DER Allocation without Load Prediction via Reinforcement Learning"
author:
  - literal: "Abed AlRahman Al Makdah"
  - literal: "Aravind Ramana"
  - literal: "Shaofeng Zou"
  - literal: "Oliver Kosut"
  - literal: "Lalitha Sankar"
issued:
  date-parts:
    - [2026, 8, 17]
url: "https://arxiv.org/abs/2608.15977"

# Custom fields
paper_id: "2608.15977"
paper_source: "openalex"
domain: "time-series"
tags:
  - "reinforcement-learning"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-20T05:21:11Z"
created_at: "2026-08-20T05:21:11Z"
---

# DER Allocation without Load Prediction via Reinforcement Learning

**Authors**: Abed AlRahman Al Makdah, Aravind Ramana, Shaofeng Zou, Oliver Kosut, Lalitha Sankar
**Date**: 2026-08-17
**Paper ID**: [openalex:2608.15977](https://arxiv.org/abs/2608.15977)

## Summary

This paper presents a forecast-free reinforcement learning framework for distributed energy resource aggregation (DERA) allocation that bypasses explicit net-demand forecasting. By modeling DERA dynamics as a deterministic linear system and exogenous net load as a feature-based linear Markov process, the authors derive a closed-form expression for the optimal policy learned via least-squares value iteration (LSVI). Numerical evaluations on CAISO data show that the learned controller achieves robust tracking and regulation across heterogeneous DERs without relying on demand predictions.

## Key Contributions

- Proposed a forecast-free reinforcement learning framework for distributed energy resource aggregation (DERA) allocation that bypasses short-term net demand prediction entirely.
- Modeled DERA dynamics as a deterministic linear system and exogenous net load as a feature-based linear Markov process capturing short-range temporal dependencies.
- Derived a closed-form expression for the optimal policy learned via a least-squares value iteration (LSVI) algorithm using operational data.
- Demonstrated through numerical experiments on CAISO net-demand data that the controller achieves high tracking accuracy and stable regulation without demand prediction.

## Archivist Review

No novel architectural concepts or reusable generic components were identified that warrant vault entries beyond standard RL and control frameworks.

## Links

- [Abstract](https://arxiv.org/abs/2608.15977)
- [PDF](https://arxiv.org/pdf/2608.15977)


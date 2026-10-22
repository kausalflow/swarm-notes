---
# CSL-compatible fields
title: "ActTime: Action-Conditioned World Modeling for Time Series"
author:
  - literal: "Xinxing Zhou"
  - literal: "Xiaojie Yuan"
  - literal: "Yanlong Wen"
  - literal: "Ming Jin"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.25764"

# Custom fields
paper_id: "2610.25764"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "autonomous-agent"
  - "reinforcement-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "acttime"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:43:33Z"
created_at: "2026-10-22T09:43:33Z"
---

# ActTime: Action-Conditioned World Modeling for Time Series

**Authors**: Xinxing Zhou, Xiaojie Yuan, Yanlong Wen, Ming Jin
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.25764](https://arxiv.org/abs/2610.25764)

## Summary

The paper introduces ActTime, an action-conditioned world model for time series designed to predict how outcomes change under alternative candidate actions from the same observed history. Trained exclusively on factual trajectories without paired counterfactual outcomes, ActTime updates variable-specific latent states through action-conditioned transitions and rolls them forward for planning. Extensive evaluation across building energy, traffic, greenhouse climate, and inventory management simulators shows that ActTime ranks first in 12 of 16 domain-task settings while revealing that factual accuracy, intervention fidelity, and decision quality are distinct and non-interchangeable properties.

## Key Contributions

- Introduces ActTime, an action-conditioned world model for time series that updates variable-specific latent states via action-conditioned transitions and observation correction.
- Demonstrates that training can be performed using only factual trajectories without paired alternative-action outcomes or planning supervision.
- Constructs a simulator-grounded evaluation suite spanning building energy, traffic, greenhouse climate, and inventory management, covering factual prediction, intervention-effect prediction, offline decision making, and closed-loop planning.
- Shows that ActTime ranks first in 12 of 16 domain-task settings and highlights that factual accuracy, intervention fidelity, and decision quality are non-interchangeable objectives.

## Open Questions & Future Work

- [[out-of-distribution-action-extrapolation]]

## Key Concepts

- [[acttime]]: An action-conditioned world model for time series that predicts how outcomes change under different actions from observed history.

## Archivist Review

Approved the core concept 'ActTime' and the open question on out-of-distribution action extrapolation because they provide distinct, reusable contributions to action-conditioned time series world modeling and offline planning. All criteria regarding scarcity, formatting, and evidence were strictly enforced.

### Approved Concepts
- ActTime: Introduces a novel action-conditioned world model architecture tailored for time series prediction, intervention-effect evaluation, and decision-making under alternative candidate plans.

### Approved Open Questions
- Out-of-Distribution Action Extrapolation: Crucial for deploying world models safely in real-world environments where agents may encounter out-of-distribution control actions.

## Links

- [Abstract](https://arxiv.org/abs/2610.25764)
- [PDF](https://arxiv.org/pdf/2610.25764)


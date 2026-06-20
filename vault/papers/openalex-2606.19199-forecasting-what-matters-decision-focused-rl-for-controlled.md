---
# CSL-compatible fields
title: "Forecasting what Matters: Decision-Focused RL for Controlled EV Charging with Unknown Departure Times"
author:
  - literal: "Giuseppe Gabriele"
  - literal: "Fabio Pavirani"
  - literal: "Seyed Soroush Karimi Madahi"
  - literal: "Chris Develder"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.19199"

# Custom fields
paper_id: "2606.19199"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "reinforcement-learning"
  - "forecasting"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "decision-focused-forecasting-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:18:20Z"
created_at: "2026-06-20T08:18:20Z"
---

# Forecasting what Matters: Decision-Focused RL for Controlled EV Charging with Unknown Departure Times

**Authors**: Giuseppe Gabriele, Fabio Pavirani, Seyed Soroush Karimi Madahi, Chris Develder
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.19199](https://arxiv.org/abs/2606.19199)

## Summary

This paper addresses the challenge of managing EV charging under uncertainty, specifically when departure times are unknown. Standard forecasting models trained solely for predictive accuracy often fail to support effective downstream control policies due to error propagation. To resolve this, the authors introduce a decision-focused reinforcement learning (DF-RL) framework that trains the forecaster end-to-end with the charging policy, optimizing for decision quality rather than traditional predictive error metrics.

## Key Contributions

- Proposes a decision-focused RL (DF-RL) framework that trains a forecaster end-to-end using feedback from the downstream RL controller.
- Enables reliable EV charging control in scenarios where critical features like departure time are unknown.
- Achieves up to a 14% improvement in total reward and a 55% reduction in unsupplied energy compared to baselines lacking departure time forecasting.

## Open Questions & Future Work

- [[cooperative-df-rl-for-grid-constraints]]

## Key Concepts

- [[decision-focused-forecasting-framework]]: A framework for training a forecaster end-to-end based on the feedback from a downstream RL agent's performance.

## Archivist Review

I have approved the 'Decision-focused forecasting framework' concept and the 'Cooperative Multi-Agent DF-RL Scaling' open question. The framework is highly relevant to current trends in time-series forecasting for downstream decision tasks, and the open question addresses the practical bottleneck of scaling these methods to multi-agent grid environments. No new datasets were approved as none were explicitly provided or sufficiently described.

### Approved Concepts
- Decision-focused forecasting framework: Addresses the misalignment between standard forecasting accuracy metrics (e.g., MSE) and the utility of predictions in downstream decision-making processes.

### Approved Open Questions
- Cooperative Multi-Agent DF-RL Scaling: Developing scalable, cooperative multi-agent control is essential for moving from single-session EV charging to practical, grid-wide smart charging deployments.

### Rejected Candidates
- [concept] Decision-focused forecasting framework (`decision-focused-forecasting-framework`) - duplicate_existing: The concept is already present in the vault under the same name and slug.

## Links

- [Abstract](https://arxiv.org/abs/2606.19199)
- [PDF](https://arxiv.org/pdf/2606.19199)


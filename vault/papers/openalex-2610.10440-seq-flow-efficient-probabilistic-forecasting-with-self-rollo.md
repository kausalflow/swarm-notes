---
# CSL-compatible fields
title: "Seq-Flow: Efficient Probabilistic Forecasting with Self-Rollout Error Control"
author:
  - literal: "Yinan Huang"
  - literal: "Shitij Govil"
  - literal: "Bo Dai"
  - literal: "Pan Li"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.10440"

# Custom fields
paper_id: "2610.10440"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "probabilistic-forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "seq-flow"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:53:13Z"
created_at: "2026-10-10T10:53:13Z"
---

# Seq-Flow: Efficient Probabilistic Forecasting with Self-Rollout Error Control

**Authors**: Yinan Huang, Shitij Govil, Bo Dai, Pan Li
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.10440](https://arxiv.org/abs/2610.10440)

## Summary

Seq-Flow is a conditional flow model for efficient probabilistic time-series forecasting that updates future trajectory distributions by transporting samples from previous forecasts using an ODE. To prevent error accumulation from recursive reuse, the authors introduce self-rollout training, where a moving-average model copy initializes subsequent updates. Experiments show that Seq-Flow significantly reduces CRPS under few-step sampling budgets on particle-accelerator beam spill forecasting and remains stable over hundreds of consecutive updates.

## Key Contributions

- Introduces Seq-Flow, a conditional flow model for probabilistic forecasting that transports samples from the previous forecast distribution to the updated distribution.
- Proposes self-rollout training using a moving average copy of the model to initialize training updates and mitigate error propagation during recursive reuse.
- Reduces CRPS by 65% under a few-NFE sampling budget on particle-accelerator beam spill forecasting while maintaining robustness over hundreds of consecutive updates.

## Limitations

Trained on self-rollouts of at most four updates, though it generalizes to over 400 consecutive updates.

## Open Questions & Future Work

- [[recursive-source-distribution-error-control]]

## Key Concepts

- [[seq-flow]]: A conditional flow model that transports samples from a previous forecast distribution to an updated one using self-rollout error control.

## Archivist Review

Approved the central Seq-Flow model and the open question regarding recursive source-distribution error control for long-horizon rollouts. No specific benchmark datasets were mentioned in the abstract, so no datasets were added. Applied strict novelty and reusability criteria throughout.

### Approved Concepts
- Seq-Flow: Introduces a conditional flow model for efficient probabilistic forecasting that transports samples from the previous forecast distribution to the updated one.

### Approved Open Questions
- Recursive Source-Distribution Error Control: Understanding how errors propagate through recursive source distributions is crucial for designing stable few-step sequential generative models that do not degrade during extended autonomous operation.

## Links

- [Abstract](https://arxiv.org/abs/2610.10440)
- [PDF](https://arxiv.org/pdf/2610.10440)


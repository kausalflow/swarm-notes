---
# CSL-compatible fields
title: "TRACE-CASH: Trial-History-Conditioned Reinforcement Learning for Adaptive Configuration Exploration in Time-Series CASH"
author:
  - literal: "Yu-Han Huang"
  - literal: "Yujia Wu"
  - literal: "Vincent S. Tseng"
issued:
  date-parts:
    - [2026, 8, 17]
url: "https://arxiv.org/abs/2608.16410"

# Custom fields
paper_id: "2608.16410"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "reinforcement-learning"
  - "hyperparameter-optimization"
  - "benchmark"
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
processed_at: "2026-08-20T05:20:52Z"
created_at: "2026-08-20T05:20:52Z"
---

# TRACE-CASH: Trial-History-Conditioned Reinforcement Learning for Adaptive Configuration Exploration in Time-Series CASH

**Authors**: Yu-Han Huang, Yujia Wu, Vincent S. Tseng
**Date**: 2026-08-17
**Paper ID**: [openalex:2608.16410](https://arxiv.org/abs/2608.16410)

## Summary

The paper presents TRACE-CASH, a trial-history-conditioned reinforcement learning method for adaptive configuration exploration in time-series combined algorithm selection and hyperparameter optimization (TS-CASH). TRACE-CASH employs a hybrid sequential optimizer that integrates a model actor, three model-conditioned actors for temporal, architectural, and training actions, and model-specific decoders with rule-based heuristics. Evaluated across 41 dataset-frequency task variants against six alternative search strategies, TRACE-CASH achieves superior performance with the lowest mean ranks on both MASE and WQL metrics.

## Key Contributions

- Introduces TRACE-CASH, a trial-history-conditioned reinforcement learning framework for time-series combined algorithm selection and hyperparameter optimization (TS-CASH).
- Implements a task-local hybrid sequential optimizer combining grouped actor-critic candidate generation with fixed rules for model coverage, validation-guided exploitation, and exploration after stalled progress.
- Evaluates TRACE-CASH against six alternatives (random, Bayesian, evolutionary, multi-objective, and language-model-assisted search) across 41 dataset-frequency task variants, achieving the lowest mean rank on both MASE and WQL.

## Archivist Review

No new concepts proposed; the paper introduces TRACE-CASH, a hybrid sequential optimizer for time-series CASH that combines grouped actor-critic candidate generation with rule-based heuristics. As this is a domain-specific combination of known optimization techniques tailored to time-series CASH rather than a foundational algorithmic building block, no reusable concept note is created.

## Links

- [Abstract](https://arxiv.org/abs/2608.16410)
- [PDF](https://arxiv.org/pdf/2608.16410)


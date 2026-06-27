---
# CSL-compatible fields
title: "UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control"
author:
  - literal: "Xibai Wang"
issued:
  date-parts:
    - [2026, 6, 24]
url: "https://arxiv.org/abs/2606.25274"

# Custom fields
paper_id: "2606.25274"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty"
  - "benchmark"
  - "decision-focused-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "uc-search"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-27T07:42:55Z"
created_at: "2026-06-27T07:42:55Z"
---

# UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control

**Authors**: Xibai Wang
**Date**: 2026-06-24
**Paper ID**: [openalex:2606.25274](https://arxiv.org/abs/2606.25274)

## Summary

UC-Search is a model-agnostic test-time wrapper designed to bridge the gap between time-series forecasting and downstream decision-making under uncertainty and hard constraints. It leverages a feasibility automaton and bounded search to select risk-adjusted actions, effectively mitigating myopic decision-making common in standard control heuristics. Evaluations on extensive control suites and the M4 inventory benchmark demonstrate that UC-Search consistently outperforms classic statistical and reinforcement learning baselines in both performance and risk mitigation.

## Key Contributions

- UC-Search provides a test-time wrapper for time-series control that integrates uncertainty estimation, feasibility automata, and bounded search to improve decision-making under hard constraints.
- The paper proves a myopic-collapse/separation theorem characterizing the conditions where delayed feasible-set coupling necessitates non-myopic search over simple risk-greedy approaches.
- UC-Search outperforms strong baselines like CEM, MPPI, and risk-aware random search across diverse delayed-control suites, including ETT and M4 inventory control benchmarks, in both nominal and compute-matched settings.

## Open Questions & Future Work

- [[integrated-dynamics-planning-time-series]]

## Key Concepts

- [[uc-search]]: A model-agnostic test-time wrapper for time-series control that performs risk-adjusted bounded search over feasible trajectories.

## Archivist Review

UC-Search represents a novel paradigm for wrapping forecasting models for constrained control tasks, earning its concept status. The proposed open question accurately identifies the transition from heuristic wrappers to integrated dynamics planning as a significant research frontier. Datasets like M4 were rejected as they are routine in this field and do not require standalone vault entries.

### Approved Concepts
- UC-Search: Introduces a novel model-agnostic test-time wrapper that integrates uncertainty estimation, feasibility automata, and bounded search for decision-making under hard constraints.

### Approved Open Questions
- Integrated Dynamics Planning: This reflects a foundational shift needed in time-series decision-making to move away from post-hoc wrappers toward natively dynamics-informed planners.

## Links

- [Abstract](https://arxiv.org/abs/2606.25274)
- [PDF](https://arxiv.org/pdf/2606.25274)


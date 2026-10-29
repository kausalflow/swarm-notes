---
# CSL-compatible fields
title: "Simulation-Efficient Double-Flow Neural Posterior Estimation for Agent-Based Models"
author:
  - literal: "Junyao Zhang"
  - literal: "Jinglai Li"
  - literal: "Junqi Tang"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35442"

# Custom fields
paper_id: "2610.35442"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "bayesian"
  - "generative-model"
  - "normalizing-flow"
  - "simulation"
  - "posterior-estimation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:11:37Z"
created_at: "2026-10-29T11:11:37Z"
---

# Simulation-Efficient Double-Flow Neural Posterior Estimation for Agent-Based Models

**Authors**: Junyao Zhang, Jinglai Li, Junqi Tang
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35442](https://arxiv.org/abs/2610.35442)

## Summary

Neural posterior estimation (NPE) is challenged by the high computational cost of simulating training data for agent-based models (ABMs). This paper introduces Double-Flow Neural Posterior Estimation (DF-NPE), which integrates learned time-series summaries with two conditional normalizing flows to generate synthetic training data and estimate posteriors. Evaluated on the Brock-Hommes asset-pricing model, DF-NPE reduces direct simulation requirements by 90% while outperforming standard NPE in accuracy and runtime.

## Key Contributions

- Proposes Double-Flow Neural Posterior Estimation (DF-NPE), combining learned time-series summaries with two conditional normalizing flows for simulation-efficient Bayesian inference in agent-based models.
- Supplements direct simulations with synthetic training pairs using pooled and ordered training strategies.
- Reduces direct simulations by 90% while achieving lower mean posterior discrepancies and runtime compared to standard NPE on the Brock-Hommes asset-pricing model.

## Limitations

Performance depends on the allocation of directly simulated versus synthetic data and the chosen training strategy.

## Archivist Review

The proposed open question is entirely specific to the evaluation and validation of the paper's novel method (DF-NPE) rather than representing a general, reusable research bottleneck across multiple time series methodologies. Therefore, no candidates were approved, adhering to the high-selectivity standard.

### Rejected Candidates
- [open_question] Generalization and Misspecification in DF-NPE (`df-npe-generalization-sbc-misspecification`) - paper_local: The open question centers on paper-specific extensions and evaluation checks for DF-NPE rather than a broad, reusable bottleneck in time series or probabilistic forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2610.35442)
- [PDF](https://arxiv.org/pdf/2610.35442)


---
# CSL-compatible fields
title: "Monte Carlo Pass Search: Using Trajectory Generation for 3D Counterfactual Pass Evaluation in Football"
author:
  - literal: "Andrew Kang"
  - literal: "Priya Narasimhan"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.11120"

# Custom fields
paper_id: "2606.11120"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "agent"
  - "autonomous-agent"
  - "planning"
  - "autoregressive"
  - "dataset"
architectures:
  []
datasets:
  - "bundesliga-3d-tracking-dataset"
concept_slugs:
  - "monte-carlo-pass-search-mcps"
dataset_slugs:
  - "bundesliga-3d-tracking-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:54:53Z"
created_at: "2026-06-12T08:54:53Z"
---

# Monte Carlo Pass Search: Using Trajectory Generation for 3D Counterfactual Pass Evaluation in Football

**Authors**: Andrew Kang, Priya Narasimhan
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.11120](https://arxiv.org/abs/2606.11120)

## Summary

This paper introduces Monte Carlo Pass Search (MCPS), a framework for football pass evaluation that treats passes as counterfactual decision problems. By sampling pass variations and projecting them into the future using a ball-conditioned trajectory generator, MCPS produces a distribution of potential outcomes rather than a single point estimate. This approach allows for more robust performance analysis and player attribution using novel execution-surplus metrics. The method leverages an adapted autoregressive trajectory model to achieve efficient simulation on high-fidelity 3D ball tracking data.

## Key Contributions

- Introduces Monte Carlo Pass Search (MCPS), a framework for evaluating counterfactual football passes by simulating trajectory variants and scoring outcomes.
- Implements a distribution-aware attribution method for pass quality using both mean-based and percentile-based execution-surplus scores.
- Adapts a discrete-token, autoregressive trajectory generator (SMART) for ball-conditioned rollouts, achieving superior performance on the Bundesliga 3D tracking dataset compared to baselines.

## Open Questions & Future Work

- [[multi-interaction-horizon-evaluation]]

## Key Concepts

- [[monte-carlo-pass-search-mcps]]: A framework for sports analytics that evaluates counterfactual pass variations by simulating future trajectories using ball-conditioned world models and scoring them via value models.

## Archivist Review

The paper presents a structured Monte Carlo approach for counterfactual evaluation in sports. MCPS is approved as it provides a reusable paradigm for integrating world models and value functions in high-fidelity trajectory analysis. The open question on multi-interaction evaluation is approved as it addresses the core research trade-off between rollout horizon and model bias. One dataset is approved as it represents a specific benchmark high-fidelity source.

### Approved Concepts
- Monte Carlo Pass Search (MCPS): It provides a novel framework for counterfactual football pass evaluation by integrating trajectory generation, possession value models, and Monte Carlo sampling.

### Approved Open Questions
- Multi-interaction Horizon Evaluation: Evaluating beyond the immediate interaction is essential for a holistic understanding of play effectiveness and long-term tactical value.

### Rejected Candidates
- [open_question] Mitigating Tracking Data Noise (`tracking-data-noise-mitigation`) - low_impact: Tracking noise and synchronization issues are routine operational challenges in sensor-based sports analytics rather than fundamental research bottlenecks of the framework.

## Datasets

- [[bundesliga-3d-tracking-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2606.11120)
- [PDF](https://arxiv.org/pdf/2606.11120)


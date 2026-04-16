---
# CSL-compatible fields
title: "SLALOM: Simulation Lifecycle Analysis via Longitudinal Observation Metrics for Social Simulation"
author:
  - literal: "Juhoon Lee"
  - literal: "Joseph Seering"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11466"

# Custom fields
paper_id: "2604.11466"
paper_source: "openalex"
domain: "nlp, social-science"
tags:
  - "llm"
  - "agent"
  - "autonomous-agent"
  - "time-series"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "slalom-simulation-lifecycle-analysis"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:29:17Z"
created_at: "2026-04-16T06:29:17Z"
---

# SLALOM: Simulation Lifecycle Analysis via Longitudinal Observation Metrics for Social Simulation

**Authors**: Juhoon Lee, Joseph Seering
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11466](https://arxiv.org/abs/2604.11466)

## Summary

SLALOM addresses the validity crisis in LLM-based social simulations by moving beyond static outcome verification to focus on the plausibility of social trajectories. The framework employs Pattern-Oriented Modeling to decompose simulations into multivariate time series, which are then evaluated against empirical data using intermediate waypoint constraints. By leveraging Dynamic Time Warping, the method ensures that simulated processes align structurally with observed social dynamics, providing a rigorous metric for distinguishing meaningful social behavior from stochastic output.

## Key Contributions

- Introduces SLALOM, a framework that prioritizes process fidelity in social simulation validation over final outcome verification.
- Implements waypoint-constrained trajectory evaluation to address the 'stopped clock' problem in social science simulations.
- Utilizes Dynamic Time Warping (DTW) to quantify the structural realism of simulation paths against empirical ground truth.

## Open Questions & Future Work

- [[evaluating-non-linear-social-simulations]]

## Key Concepts

- [[slalom-simulation-lifecycle-analysis]]: A framework for validating agent-based social simulations by aligning longitudinal process trajectories with empirical benchmarks using waypoint-constrained pattern matching.

## Archivist Review

The framework 'SLALOM' is approved as it introduces a distinct, reusable methodology for validating agent simulation trajectories by replacing static outcome checks with waypoint-constrained longitudinal pattern matching. The associated open question correctly identifies a significant technical barrier—the reliance on monotonic alignment in current trajectory evaluation—that restricts the modeling of more realistic, complex social phenomena.

### Approved Concepts
- SLALOM: It addresses the 'stopped clock' problem in agent-based social simulations by formalizing trajectory-based validation rather than relying solely on end-state outcomes.

### Approved Open Questions
- Evaluating non-linear social simulations: This addresses a fundamental limitation in the current state-of-the-art for evaluating agent trajectories, allowing for more realistic and complex modeling beyond linear sequences.

## Links

- [Abstract](https://arxiv.org/abs/2604.11466)
- [PDF](https://arxiv.org/pdf/2604.11466)


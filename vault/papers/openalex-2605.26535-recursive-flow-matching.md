---
# CSL-compatible fields
title: "Recursive Flow Matching"
author:
  - literal: "Jiahe Huang"
  - literal: "Sihan Xu"
  - literal: "Sharvaree Vadgama"
  - literal: "Rose Yu"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.26535"

# Custom fields
paper_id: "2605.26535"
paper_source: "openalex"
domain: "time-series"
tags:
  - "generative-adversarial-network"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "recursive-flow-matching-recfm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:39:39Z"
created_at: "2026-05-29T08:39:39Z"
---

# Recursive Flow Matching

**Authors**: Jiahe Huang, Sihan Xu, Sharvaree Vadgama, Rose Yu
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.26535](https://arxiv.org/abs/2605.26535)

## Summary

Recursive Flow Matching (RecFM) is a generative framework designed to model complex spatiotemporal dynamics with high physical accuracy. By enforcing self-consistency across different discretization scales, the model effectively minimizes discretization errors during trajectory generation. This approach enables high-fidelity forecasting in significantly fewer steps than traditional solvers, outperforming existing diffusion-based emulators in both speed and predictive accuracy.

## Key Contributions

- Introduces Recursive Flow Matching (RecFM), a framework that leverages self-consistency across discretization scales to improve physical fidelity in scientific emulation.
- Achieves high-fidelity forecasting in 2-4 steps, matching the performance of traditional multi-step solvers while providing up to a 20x speedup over state-of-the-art diffusion-based models.
- Reduces mean squared error by over 15% compared to standard flow matching methods in spatiotemporal forecasting benchmarks.

## Open Questions & Future Work

- [[scaling-recursive-generative-models-to-natural-video]]

## Key Concepts

- [[recursive-flow-matching-recfm]]: A generative framework for spatiotemporal forecasting that enforces self-consistency across discretization scales to minimize error and increase generation speed.

## Archivist Review

Approved Recursive Flow Matching as a distinct generative framework leveraging self-consistency for efficient spatiotemporal emulation. The open question was reformulated to generalize the research challenge of applying recursive trajectory alignment to natural video domains, moving beyond the specific model label.

### Approved Concepts
- Recursive Flow Matching (RecFM): It introduces a self-consistency mechanism to align trajectories across discretization scales, addressing the computational speed-fidelity trade-off in scientific emulation.

### Approved Open Questions
- Scaling Recursive Emulation to Video: Extending high-efficiency generative emulation from controlled scientific domains to unconstrained natural video is a critical step for developing foundation models for real-world dynamics.

### Rejected Candidates
- [open_question] Scaling RecFM to Video Domains (`scaling-recfm-to-complex-video-domains`) - duplicate_existing: Refined the candidate into a more generalized version that focuses on the architectural challenge rather than the specific model name.

## Links

- [Abstract](https://arxiv.org/abs/2605.26535)
- [PDF](https://arxiv.org/pdf/2605.26535)


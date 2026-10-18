---
# CSL-compatible fields
title: "PathFM: Fast Generative Forecasting of Multivariate Trajectories"
author:
  - literal: "Jiachen Yao"
  - literal: "Xiyuan Zhang"
  - literal: "Annan Yu"
  - literal: "Boran Han"
  - literal: "Abdul Fatir Ansari"
  - literal: "Shuai Zhang"
  - literal: "Michael Bohlke‐Schneider"
  - literal: "Bernie Wang"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.22358"

# Custom fields
paper_id: "2610.22358"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "generative-model"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  - "fps-bench"
concept_slugs:
  - "pathfm"
dataset_slugs:
  - "fps-bench"
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:12:34Z"
created_at: "2026-10-18T09:12:34Z"
---

# PathFM: Fast Generative Forecasting of Multivariate Trajectories

**Authors**: Jiachen Yao, Xiyuan Zhang, Annan Yu, Boran Han, Abdul Fatir Ansari, Shuai Zhang, Michael Bohlke‐Schneider, Bernie Wang
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.22358](https://arxiv.org/abs/2610.22358)

## Summary

PathFM is a generative multivariate trajectory forecasting model based on flow matching that addresses the limitations of marginal quantile forecasting by capturing full trajectory dependence structures. By utilizing model distillation down to one or two steps and sharing history attention caches, PathFM achieves extremely fast multi-path generation competitive with single-query quantile models. The authors also introduce Forecast Path Score Bench (fps-bench) to evaluate trajectory-dependent metrics such as energy and variogram scores, showing that PathFM outperforms strong baselines on both path scores and chaotic system long-run variability.

## Key Contributions

- Introduces PathFM, a trajectory-based forecasting model using flow matching to generate complete future paths while capturing trajectory dependence structures.
- Applies model distillation to one or two steps alongside history attention cache sharing to achieve efficient multi-path generation.
- Introduces Forecast Path Score Bench (fps-bench) evaluating energy scores, variogram scores, and downstream metrics.
- Demonstrates competitive marginal accuracy on fev-bench and TIME, superior aggregate path scores on fps-bench, and sustained long-run variability on chaotic systems.

## Open Questions & Future Work

- [[invariant-distribution-recovery-chaotic-systems]]

## Key Concepts

- [[pathfm]]: A trajectory-based time series forecasting model using flow matching and distillation to generate complete future paths efficiently.

## Archivist Review

Strictly followed vault standards by approving one central framework concept (PathFM), one key dataset (fps-bench), and one open question on invariant distribution recovery in chaotic systems. Routine or external benchmarks like fev-bench were omitted to maintain vault exclusivity.

### Approved Concepts
- PathFM: Central mechanism for generative multivariate trajectory forecasting via flow matching and model distillation.

### Approved Open Questions
- Invariant Distribution Recovery in Chaos: Crucial for evaluating the physical and dynamical fidelity of generative time series foundation models across chaotic and complex real-world domains.

### Rejected Candidates
- [dataset] fev-bench (`fev-bench`) - duplicate_existing: fev-bench is already widely known or routine benchmark data, and we prioritize scarce, distinct benchmark notes.

## Datasets

- [[fps-bench]]

## Links

- [Abstract](https://arxiv.org/abs/2610.22358)
- [PDF](https://arxiv.org/pdf/2610.22358)


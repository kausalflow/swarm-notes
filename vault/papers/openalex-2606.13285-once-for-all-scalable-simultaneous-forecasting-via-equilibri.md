---
# CSL-compatible fields
title: "Once-for-All: Scalable Simultaneous Forecasting via Equilibrium State Estimation"
author:
  - literal: "Beinan Xu"
  - literal: "Andy Song"
  - literal: "Gao"
  - literal: "Feng Liu"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13285"

# Custom fields
paper_id: "2606.13285"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "equilibrium-state-estimation-ese"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:38:15Z"
created_at: "2026-06-14T08:38:15Z"
---

# Once-for-All: Scalable Simultaneous Forecasting via Equilibrium State Estimation

**Authors**: Beinan Xu, Andy Song, Gao, Feng Liu
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13285](https://arxiv.org/abs/2606.13285)

## Summary

The authors present Equilibrium State Estimation (ESE), a novel paradigm for simultaneous forecasting of multiple interacting systems. By estimating a global equilibrium state before performing holistic predictions, ESE avoids the bottleneck of sequential or independent system modeling. The method achieves linear-time complexity and delivers 10-70x speedups when integrated with existing predictors, while maintaining accuracy across economic and healthcare datasets.

## Key Contributions

- Introduced Equilibrium State Estimation (ESE), a novel paradigm that forecasts multiple interacting systems simultaneously in a single pass.
- ESE achieves linear-time complexity, outperforming existing state-of-the-art methods in scalability as the number of systems increases.
- Demonstrated a 10-70x speedup when integrated with conventional predictors while maintaining or exceeding their predictive accuracy across currency exchange and epidemic modeling benchmarks.
- Established robustness and generalizability of the ESE paradigm under diverse system perturbations.

## Open Questions & Future Work

- [[ese-robustness-shocks-phase-shifts]]

## Key Concepts

- [[equilibrium-state-estimation-ese]]: A paradigm for simultaneous forecasting of interacting systems that estimates a collective equilibrium state to enable efficient, coordinated predictions.

## Archivist Review

I approved the core ESE paradigm and its associated open question regarding stability under non-stationary shocks and phase shifts, as these represent a significant methodological contribution and a clearly defined research boundary. No datasets were approved because the paper references generic classes of problems (currency/epidemic modeling) rather than specific, novel benchmarks worth tracking as standalone entities.

### Approved Concepts
- Equilibrium State Estimation (ESE): ESE is the central methodological contribution of the paper, providing a model-agnostic paradigm for scaling simultaneous multi-system forecasting via a collective state representation.

### Approved Open Questions
- Robustness under shocks and phase-shifts: Understanding the limits of robustness under non-stationary or phase-shifted conditions is essential for extending ESE to diverse real-world systems where synchronization and shock propagation are common.

## Links

- [Abstract](https://arxiv.org/abs/2606.13285)
- [PDF](https://arxiv.org/pdf/2606.13285)


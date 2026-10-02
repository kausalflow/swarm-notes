---
# CSL-compatible fields
title: "State Transport Routing for Short-horizon Adaptation in Multi-horizon Photovoltaic Forecasting"
author:
  - literal: "Xu Yuqing"
  - literal: "Zhou Liguo"
  - literal: "Sun Ze"
  - literal: "Yu Lei"
  - literal: "Jiang Mingming"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.36926"

# Custom fields
paper_id: "2609.36926"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "adapter"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:47:36Z"
created_at: "2026-10-02T10:47:36Z"
---

# State Transport Routing for Short-horizon Adaptation in Multi-horizon Photovoltaic Forecasting

**Authors**: Xu Yuqing, Zhou Liguo, Sun Ze, Yu Lei, Jiang Mingming
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.36926](https://arxiv.org/abs/2609.36926)

## Summary

This paper introduces State Transport Routing (STR), a lightweight adapter designed to refine short-horizon photovoltaic power forecasts from frozen models without altering their long-term predictions. STR blends the base forecast with trajectories derived from recent measurements and trends using a horizon-conditioned router active over the first 120 minutes. Experiments across four public PV datasets and five neural backbones show that STR consistently improves short-term forecasting accuracy over standard residual adapters.

## Key Contributions

- Proposed state transport routing (STR), a lightweight adapter combining the original forecast with trajectories derived from recent power measurements and trends to refine frozen model predictions.
- Introduced a horizon-conditioned router that dynamically adjusts adaptation contributions over the first 120 minutes while preserving longer-horizon predictions.
- Demonstrated consistent improvements across five neural forecasting backbones on four public PV datasets, reducing normalized mean absolute error compared to parameter-matched residual adapters.

## Limitations

No reliable improvement was observed when applying STR to LightGBM.

## Archivist Review

Rigorously applied the review policy, approving no concepts or open questions because the proposed candidate was routine empirical validation work rather than a foundational theoretical question or reusable concept.

### Rejected Candidates
- [open_question] Prospective Multi-Site Deployment Evaluation (`prospective-multi-site-evaluation`) - low_impact: Boilerplate future work on multi-site validation and empirical evaluation without identifying a specific unresolved structural bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.36926)
- [PDF](https://arxiv.org/pdf/2609.36926)


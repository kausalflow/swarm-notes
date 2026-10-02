---
# CSL-compatible fields
title: "From AI weather prediction to infrastructure resilience: a real-time correction–downscaling framework for tropical cyclone impact forecasting"
author:
  - literal: "You Wu"
  - literal: "Zhenguo Wang"
  - literal: "Naiyu Wang"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2603.12828"

# Custom fields
paper_id: "2603.12828"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ai-based-correction-downscaling-framework-acdf"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:47:45Z"
created_at: "2026-10-02T10:47:45Z"
---

# From AI weather prediction to infrastructure resilience: a real-time correction–downscaling framework for tropical cyclone impact forecasting

**Authors**: You Wu, Zhenguo Wang, Naiyu Wang
**Date**: 2026-09-29
**Paper ID**: [openalex:2603.12828](https://arxiv.org/abs/2603.12828)

## Summary

The paper introduces the AI-based Correction-Downscaling Framework (ACDF) to bridge the gap between global AI weather forecasts and asset-scale infrastructure risk assessment for tropical cyclones. By decoupling storm-scale bias correction from terrain-aware refinement, ACDF mitigates error propagation while recovering sub-kilometer wind variability essential for structural loading analysis. Evaluated on 11 typhoons in Zhejiang, China, ACDF reduces station-scale wind-speed MAE by 38.8% compared to Pangu-Weather while maintaining high computational efficiency.

## Key Contributions

- Introduces the AI-based Correction-Downscaling Framework (ACDF) to translate global AI weather forecasts into asset-scale infrastructure risk intelligence for tropical cyclones.
- Separates storm-scale bias correction from terrain-aware refinement to mitigate error propagation and restore sub-kilometer wind variability governing structural loading.
- Reduces station-scale wind-speed MAE by 38.8% relative to Pangu-Weather while executing in approximately 25 s per 12-h cycle on a single GPU.
- Demonstrates operational capability by reproducing observed high-wind tails and successfully flagging the exact transmission line that failed during Typhoon Hagupit.

## Key Concepts

- [[ai-based-correction-downscaling-framework-acdf]]: A real-time correction-downscaling framework that bridges global AI weather forecasts to asset-scale infrastructure risk assessment for tropical cyclone impacts.

## Archivist Review

The review adhered strictly to high selectivity standards. ACDF was approved as a robust, reusable framework concept bridging global weather forecasts to local infrastructure resilience. Regional typhoon records and comparisons against existing models were correctly filtered out as routine application details.

### Approved Concepts
- AI-based Correction–Downscaling Framework (ACDF): Central methodological contribution that bridges global AI weather forecasts and asset-scale infrastructure risk assessment by separating storm-scale bias correction from terrain-aware refinement.

### Rejected Candidates
- [concept] Pangu-Weather (`pangu-weather`) - not_novel: Pangu-Weather is an existing pre-trained global weather prediction model, not a novel mechanism introduced or generalizable as a standalone methodological concept in this paper.
- [dataset] Zhejiang Typhoon Dataset (`zhejiang-typhoon-dataset`) - low_impact: The evaluation dataset consisting of 11 typhoons affecting Zhejiang is an unnamed, regionally sliced subset rather than a primary standardized benchmark dataset.

## Links

- [Abstract](https://arxiv.org/abs/2603.12828)
- [PDF](https://arxiv.org/pdf/2603.12828)


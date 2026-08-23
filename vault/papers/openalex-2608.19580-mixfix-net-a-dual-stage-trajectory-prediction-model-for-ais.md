---
# CSL-compatible fields
title: "Mix&Fix-Net: A Dual-Stage Trajectory Prediction Model for AIS and Vision-Derived Vessel Data"
author:
  - literal: "Md Mahmuddun Nabi Murad"
  - literal: "Bora San Turgut"
  - literal: "Yasin Yilmaz"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.19580"

# Custom fields
paper_id: "2608.19580"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "time-series"
  - "forecasting"
  - "object-detection"
  - "multimodal"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:20:06Z"
created_at: "2026-08-23T05:20:06Z"
---

# Mix&Fix-Net: A Dual-Stage Trajectory Prediction Model for AIS and Vision-Derived Vessel Data

**Authors**: Md Mahmuddun Nabi Murad, Bora San Turgut, Yasin Yilmaz
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.19580](https://arxiv.org/abs/2608.19580)

## Summary

Vessel trajectory prediction is crucial for maritime safety, yet small vessels often lack Automatic Identification System (AIS) transponders, creating monitoring gaps filled by vision-derived data. To bridge this divide, the authors propose Mix&Fix-Net, a dual-stage mixer-based model combining a primary trajectory predictor with a residual trajectory adjuster. Evaluated on both AIS data and a newly introduced video-based webcam dataset, Mix&Fix-Net outperforms existing baselines across multiple standard error metrics.

## Key Contributions

- Proposes Mix&Fix-Net, a dual-stage mixer-based trajectory prediction model integrating a Primary Trajectory Predictor and a Residual Trajectory Adjuster.
- Introduces a new video-based dataset extracted from webcam streams to represent non-AIS vessel trajectories.
- Demonstrates consistent outperformance over existing baselines across both AIS and non-AIS datasets using six evaluation metrics including MSE, MAE, SMAPE, FDE, Frechet distance, and AED.

## Open Questions & Future Work

- [[vision-derived-vessel-trajectory-smoothing]]

## Archivist Review

Evaluated the proposed concept and open question against vault standards. The model architecture is paper-local and task-specific, but the open question regarding vision-derived vessel trajectory smoothing addresses an important methodological bottleneck in bridging pixel-level tracking noise with physical motion kinematics.

### Approved Open Questions
- Vision-Derived Vessel Trajectory Smoothing: Crucial for bridging the gap between pixel-level tracking noise in vision-derived non-AIS vessel data and true physical vessel kinematics.

### Rejected Candidates
- [concept] Mix&Fix-Net (`mix-and-fix-net`) - paper_local: A paper-internal model architecture specific to maritime vessel trajectory prediction that does not represent a broadly reusable forecasting mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2608.19580)
- [PDF](https://arxiv.org/pdf/2608.19580)


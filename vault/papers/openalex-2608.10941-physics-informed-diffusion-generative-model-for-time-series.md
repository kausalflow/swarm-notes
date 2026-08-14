---
# CSL-compatible fields
title: "Physics-informed Diffusion Generative Model for Time-Series Data Synthesis in Dynamic Systems"
author:
  - literal: "Haiteng Wang"
  - literal: "Yunfei Zhu"
  - literal: "Tao Wang"
  - literal: "Yikang Li"
  - literal: "Jiabao Dong"
  - literal: "Xiaoge Zhang"
  - literal: "Lei Ren"
issued:
  date-parts:
    - [2026, 8, 11]
url: "https://arxiv.org/abs/2608.10941"

# Custom fields
paper_id: "2608.10941"
paper_source: "openalex"
domain: "time-series"
tags:
  - "diffusion-model"
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physdgm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-14T06:07:20Z"
created_at: "2026-08-14T06:07:20Z"
---

# Physics-informed Diffusion Generative Model for Time-Series Data Synthesis in Dynamic Systems

**Authors**: Haiteng Wang, Yunfei Zhu, Tao Wang, Yikang Li, Jiabao Dong, Xiaoge Zhang, Lei Ren
**Date**: 2026-08-11
**Paper ID**: [openalex:2608.10941](https://arxiv.org/abs/2608.10941)

## Summary

The paper introduces PhysDGM, a stepwise physics-embedded diffusion generative model that incorporates underlying physical laws directly into each reverse diffusion step to ensure trajectory-level physical consistency in time-series data synthesis. Evaluations across 34 diverse datasets in turbofan engines, batteries, and chemical processes demonstrate high fidelity and substantial performance gains on downstream tasks like remaining useful life prediction and fault diagnosis using significantly less real training data.

## Key Contributions

- Introduces PhysDGM, a stepwise physics-embedded diffusion generative model that embeds physical laws directly into each reverse diffusion step for trajectory-level physical consistency.
- Constructs a large-scale AI-synthetic dataset of 4.4 million samples across 34 datasets spanning turbofan engines, aero-engines, batteries, and chemical processes.
- Substantially improves downstream task performance over real data alone by 48% for remaining useful life prediction, 15% for health indicator estimation, 22% for state-of-health assessment, and 20% for fault diagnosis while requiring 10-20x less training data.

## Open Questions & Future Work

- [[non-smooth-physics-informed-generative-modeling]]

## Key Concepts

- [[physdgm]]: A stepwise physics-embedded diffusion generative model that incorporates physical laws directly into each reverse diffusion step to synthesize physically consistent time-series data.

## Archivist Review

Approved the core methodology (PhysDGM) and the primary open question on non-smooth physics-informed modeling. Rejected the diffusion efficiency question as routine acceleration work.

### Approved Concepts
- PhysDGM: PhysDGM is the core methodological contribution of the paper, introducing a stepwise physics-embedded diffusion generative model that enforces trajectory-level physical consistency during reverse diffusion steps.

### Approved Open Questions
- Non-Smooth Physics-Informed Generative Modeling: Extending physics-informed generative models to handle non-smooth and discrete physical dynamics is a fundamental challenge for applying AI safely across broader industrial engineering systems.

### Rejected Candidates
- [open_question] Efficient Diffusion Samplers for Time Series (`efficient-diffusion-samplers-for-timeseries`) - low_impact: Standard generative model distillation and efficiency bottlenecks are broad cross-domain topics rather than unique open problems exclusive to this time-series physics paper.

## Links

- [Abstract](https://arxiv.org/abs/2608.10941)
- [PDF](https://arxiv.org/pdf/2608.10941)


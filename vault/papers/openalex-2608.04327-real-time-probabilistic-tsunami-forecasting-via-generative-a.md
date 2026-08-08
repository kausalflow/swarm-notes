---
# CSL-compatible fields
title: "Real-time probabilistic tsunami forecasting via generative AI"
author:
  - literal: "Y. Oishi"
  - literal: "Takashi Furumura"
  - literal: "Fumihiko Imamura"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.04327"

# Custom fields
paper_id: "2608.04327"
paper_source: "openalex"
domain: "time-series"
tags:
  - "diffusion-model"
  - "uncertainty-quantification"
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-08T05:34:43Z"
created_at: "2026-08-08T05:34:43Z"
---

# Real-time probabilistic tsunami forecasting via generative AI

**Authors**: Y. Oishi, Takashi Furumura, Fumihiko Imamura
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.04327](https://arxiv.org/abs/2608.04327)

## Summary

This paper proposes a probabilistic ensemble model based on conditional diffusion models for real-time onshore tsunami inundation forecasting, addressing the lack of uncertainty quantification in deterministic machine learning approaches. Validated using the 2011 Tohoku-oki earthquake dataset, the framework accurately predicts inundation depth and extent while tracking decreasing postearthquake uncertainty over time. The approach demonstrates that generative AI can successfully shift tsunami forecasting from determinism to probabilism.

## Key Contributions

- Developed a probabilistic ensemble model based on a conditional diffusion model for real-time onshore tsunami inundation forecasting.
- Demonstrated uncertainty quantification that reconciles accuracy with calibration under near-field earthquake conditions.
- Validated using the 2011 Tohoku-oki earthquake data, accurately tracking postearthquake uncertainty decrease over time and predicting inundation depth and extent.

## Archivist Review

We reviewed the candidate concept and open question regarding real-time probabilistic tsunami forecasting. Both candidates are highly domain-specific to geophysical hazard modeling and physical simulations rather than generalizable machine learning or time-series methodology, so they were rejected under the domain-specificity and paper-local criteria.

### Rejected Candidates
- [concept] Conditional Diffusion Tsunami Forecasting (`conditional-diffusion-tsunami-forecasting`) - paper_local: This concept is too domain-specific to tsunamis and physical hazards, making it less reusable as a general machine learning time-series primitive.
- [open_question] Training Data Expansion for Unexpected Megathrust Earthquakes (`training-data-expansion-for-unexpected-megathrust-earthquakes`) - paper_local: This open question focuses on domain-specific physical simulation scaling and geological scenario coverage rather than a fundamental algorithmic or statistical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.04327)
- [PDF](https://arxiv.org/pdf/2608.04327)


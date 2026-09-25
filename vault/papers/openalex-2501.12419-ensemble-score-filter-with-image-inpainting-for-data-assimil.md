---
# CSL-compatible fields
title: "Ensemble Score Filter with Image Inpainting for Data Assimilation in Tracking Surface Quasi-geostrophic Dynamics with Partial Observations"
author:
  - literal: "Siming Liang"
  - literal: "Hoang Ngoc Tran"
  - literal: "F. Bao"
  - literal: "Hristo Georgiev Chipilski"
  - literal: "Peter Jan van Leeuwen"
  - literal: "Guannan Zhang"
issued:
  date-parts:
    - [2026, 9, 24]
url: "https://arxiv.org/abs/2501.12419"

# Custom fields
paper_id: "2501.12419"
paper_source: "openalex"
domain: "geoscience"
tags:
  - "diffusion-model"
  - "time-series"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ensemble-score-filter"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:54:01Z"
created_at: "2026-09-25T09:54:01Z"
---

# Ensemble Score Filter with Image Inpainting for Data Assimilation in Tracking Surface Quasi-geostrophic Dynamics with Partial Observations

**Authors**: Siming Liang, Hoang Ngoc Tran, F. Bao, Hristo Georgiev Chipilski, Peter Jan van Leeuwen, Guannan Zhang
**Date**: 2026-09-24
**Paper ID**: [openalex:2501.12419](https://arxiv.org/abs/2501.12419)

## Summary

This paper extends the ensemble score filter (EnSF)—a training-free diffusion-based data assimilation approach—to handle partial observations by integrating image inpainting techniques. While standard EnSF excels with full observations, it lacks a covariance matrix to capture dependencies between observed and unobserved variables; the authors resolve this by employing image inpainting at each filtering step to predict unobserved states. Evaluations on surface quasi-geostrophic model dynamics demonstrate the effectiveness of this framework for complex geophysical systems.

## Key Contributions

- Developed an ensemble score filter (EnSF) integrated with image inpainting to address partial observation challenges in data assimilation without requiring covariance matrices.
- Incorporated likelihood information into the diffusion score function to estimate observed states at each filtering step.
- Demonstrated successful tracking of surface quasi-geostrophic model dynamics under various partial observation scenarios.

## Open Questions & Future Work

- [[physics-constrained-inpainting-data-assimilation]]

## Key Concepts

- [[ensemble-score-filter]]: An ensemble score filter integrating image inpainting for data assimilation under partial observations.

## Archivist Review

Approved the core 'Ensemble Score Filter' concept and its associated open question regarding physics-constrained inpainting for partial observation data assimilation. Rejected auxiliary paper-internal helper mechanisms.

### Approved Concepts
- Ensemble Score Filter: Central method extending EnSF with image inpainting to handle unobserved state variables in partial observation data assimilation.

### Approved Open Questions
- Physics-Constrained Inpainting for Data Assimilation: Bridging generative data assimilation filters with physical laws and scaling them to operational weather forecasting systems is critical for real-world geoscience applications.

### Rejected Candidates
- [concept] Image Inpainting for Data Assimilation (`image-inpainting-for-data-assimilation`) - subcomponent_of_broader_mechanism: Subcomponent of the overarching Ensemble Score Filter framework.

## Links

- [Abstract](https://arxiv.org/abs/2501.12419)
- [PDF](https://arxiv.org/pdf/2501.12419)


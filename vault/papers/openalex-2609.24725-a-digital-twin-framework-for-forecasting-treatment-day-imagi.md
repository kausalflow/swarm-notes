---
# CSL-compatible fields
title: "A digital-twin framework for forecasting treatment-day imaging with contour uncertainty in adaptive proton radiotherapy"
author:
  - literal: "Yizhou Wu"
  - literal: "Jie Ding"
  - literal: "Justin Roper"
  - literal: "Minglei Kang"
  - literal: "Yuheng Li"
  - literal: "Sibo Tian"
  - literal: "David S. Yu"
  - literal: "Xiaofeng Yang"
  - literal: "Chih-Wei Chang"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24725"

# Custom fields
paper_id: "2609.24725"
paper_source: "openalex"
domain: "medicine"
tags:
  - "multimodal"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:38:54Z"
created_at: "2026-09-24T09:38:54Z"
---

# A digital-twin framework for forecasting treatment-day imaging with contour uncertainty in adaptive proton radiotherapy

**Authors**: Yizhou Wu, Jie Ding, Justin Roper, Minglei Kang, Yuheng Li, Sibo Tian, David S. Yu, Xiaofeng Yang, Chih-Wei Chang
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24725](https://arxiv.org/abs/2609.24725)

## Summary

The paper proposes a digital-twin framework for adaptive proton radiotherapy to forecast a patient's treatment-day anatomy and contour uncertainty using a library of previously treated patients. By combining a cross-patient deformable registration and a longitudinal foundation-model field, the framework generates an ensemble of predicted CTs and evaluates six-direction contour dispersion. Evaluations on ten patients show that the library effectively constrains anisotropic shape uncertainty, and early quality-assurance CTs further narrow uncertainty without requiring manual contouring.

## Key Contributions

- Introduces a digital-twin framework utilizing a library of previously treated patients to forecast treatment-day anatomy as an ensemble of predicted CTs with propagated contours.
- Develops a two-step foundation-model deformable registration method combining a cross-patient field and a longitudinal field to map patient-specific anatomical changes.
- Quantifies six-direction contour uncertainty in millimeters by resolving the dispersion of propagated contours along outward normals.
- Demonstrates on ten patients that the library fixes anisotropic uncertainty shapes while first quality-assurance CTs narrow uncertainty significantly without requiring drawn contours.

## Limitations

The contour uncertainty estimate orders directions correctly but is not Gaussian-calibrated.

## Archivist Review

The paper presents a digital-twin framework for forecasting treatment-day imaging and contour uncertainty in proton radiotherapy. No new reusable machine learning architectures or specialized ML concepts were introduced; standard deformable registration and foundation models are applied in a clinical domain. Therefore, zero concepts and zero datasets are proposed.

## Links

- [Abstract](https://arxiv.org/abs/2609.24725)
- [PDF](https://arxiv.org/pdf/2609.24725)


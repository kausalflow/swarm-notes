---
# CSL-compatible fields
title: "YingLan: A Multimodal Ocean Foundation Model for Unified Representation Learning from Heterogeneous Observations"
author:
  - literal: "Sen Jia"
  - literal: "Siqi Wei"
  - literal: "Junyu Wang"
  - literal: "Zijun Lv"
  - literal: "Pan Liu"
  - literal: "Meng Xu"
  - literal: "Xiyou Fu"
  - literal: "Yuxi Sun"
  - literal: "Qiang Liu"
  - literal: "Shuyu Zhang"
  - literal: "Lin Mu"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29313"

# Custom fields
paper_id: "2610.29313"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "forecasting"
  - "time-series"
  - "transformer"
  - "attention-mechanism"
  - "spatial-attention"
  - "representation-learning"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "spatiotemporal-increment-coupling-stic"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-24T09:12:30Z"
created_at: "2026-10-24T09:12:30Z"
---

# YingLan: A Multimodal Ocean Foundation Model for Unified Representation Learning from Heterogeneous Observations

**Authors**: Sen Jia, Siqi Wei, Junyu Wang, Zijun Lv, Pan Liu, Meng Xu, Xiyou Fu, Yuxi Sun, Qiang Liu, Shuyu Zhang, Lin Mu
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29313](https://arxiv.org/abs/2610.29313)

## Summary

YingLan is a multimodal ocean foundation model designed to unify representation learning from heterogeneous sources such as satellite imagery, gridded ocean fields, and buoy data. It employs physics-attribute-conditioned dynamic encoding and Spatiotemporal Increment Coupling (STIC) to model multiscale spatiotemporal dependencies, alongside masked observation reconstruction and temporal evolution pretraining. Evaluated on a seven-day sea surface salinity forecasting task in Shenzhen coastal waters, YingLan demonstrates lower RMSE than comparative models like LangYa, XiHe, and GloNet2.

## Key Contributions

- Proposes YingLan, a multimodal ocean foundation model for unified representation learning across heterogeneous satellite imagery, gridded fields, and buoy observations.
- Introduces physics-attribute-conditioned dynamic encoding and Spatiotemporal Increment Coupling (STIC) to capture multiscale spatiotemporal dependencies.
- Achieves an average RMSE of 0.687508 PSU on a seven-day sea surface salinity (SSS) forecasting task in Shenzhen coastal waters, outperforming LangYa, XiHe, and GloNet2.

## Limitations

Broader cross-task and cross-regional evaluations remain necessary to assess its generalization capabilities beyond regional ocean forecasting.

## Open Questions & Future Work

- [[cross-task-and-regional-ocean-generalization]]

## Key Concepts

- [[spatiotemporal-increment-coupling-stic]]: A mechanism that models multiscale spatiotemporal dependencies through cross-scale interactions of latent temporal increments.

## Archivist Review

Approved the core methodological component Spatiotemporal Increment Coupling (STIC) and the significant open question regarding cross-task and regional generalization for multimodal ocean modeling. Rejected the model name YingLan as it represents a specific paper-local foundation model implementation.

### Approved Concepts
- Spatiotemporal Increment Coupling (STIC): Provides a novel mechanism for modeling multiscale spatiotemporal dependencies across heterogeneous ocean variables.

### Approved Open Questions
- Cross-Task and Regional Ocean Generalization: Crucial for ensuring that ocean foundation models can generalize effectively beyond regional case studies and cope with missing, noisy, or sparse multi-sensor marine data.

### Rejected Candidates
- [concept] YingLan (`yinglan`) - paper_local: Paper-specific model instantiation rather than a general reusable methodological primitive.

## Links

- [Abstract](https://arxiv.org/abs/2610.29313)
- [PDF](https://arxiv.org/pdf/2610.29313)


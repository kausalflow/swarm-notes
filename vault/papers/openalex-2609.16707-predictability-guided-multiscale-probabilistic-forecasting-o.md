---
# CSL-compatible fields
title: "Predictability-Guided Multiscale Probabilistic Forecasting of Wind Direction under Extreme Shear"
author:
  - literal: "Hailong Shu"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.16707"

# Custom fields
paper_id: "2609.16707"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "probabilistic-forecasting"
  - "diffusion-model"
  - "uncertainty"
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
processed_at: "2026-09-17T09:44:20Z"
created_at: "2026-09-17T09:44:20Z"
---

# Predictability-Guided Multiscale Probabilistic Forecasting of Wind Direction under Extreme Shear

**Authors**: Hailong Shu
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.16707](https://arxiv.org/abs/2609.16707)

## Summary

Accurate multi-horizon wind direction forecasting under extreme directional shear is hindered by non-Euclidean geometry on $S^1$, multiscale dynamics, and phase lags in conventional models. To address this, the paper introduces a predictability-guided paradigm that decomposes dynamics into slow synoptic drift, intermediate turning via continuous latent differential flows, and unresolved turbulence using conditional residual diffusion. Evaluated on a multi-year benchmark, the proposed framework outperforms zero-shot foundation models on extreme turning events while maintaining calm-weather accuracy and reliable probabilistic calibration.

## Key Contributions

- Proposes a predictability-guided multiscale forecasting framework tailored for wind direction under extreme shear on $S^1$ geometry
- Combines deterministic regression for slow synoptic drift, continuous latent differential flows for intermediate turning, and conditional residual diffusion for unresolved turbulence
- Achieves a test Mean Circular Error (MCE) of 38.48 degrees during calm weather and reduces extreme-turning error to 60.69 degrees compared to 70.42 degrees for zero-shot foundation models
- Reaches a circular CRPS of 22.36 degrees with 93.88% coverage at nominal 95% on a multi-year benchmark

## Open Questions & Future Work

- [[multimodal-circular-manifold-learning]]

## Archivist Review

The paper proposes a predictability-guided multiscale framework for wind direction forecasting under extreme shear. The specific framework is too paper-local for a standalone concept note, but the open question regarding multimodal circular manifold learning addresses a clear theoretical and practical limitation in non-Euclidean probabilistic modeling.

### Approved Open Questions
- Multimodal Circular Manifold Learning: Crucial for accurate uncertainty quantification and risk-aware wind turbine control during rapid atmospheric transitions and frontal passages.

### Rejected Candidates
- [concept] Predictability-Guided Multiscale Wind Direction Forecasting (`predictability-guided-multiscale-wind-direction-forecasting`) - paper_local: Paper-local framework combining deterministic regression, latent differential flows, and residual diffusion specifically for wind direction shear, lacking broad standalone reusability across unrelated time-series domains.

## Links

- [Abstract](https://arxiv.org/abs/2609.16707)
- [PDF](https://arxiv.org/pdf/2609.16707)


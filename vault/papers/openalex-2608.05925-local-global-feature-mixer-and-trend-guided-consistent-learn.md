---
# CSL-compatible fields
title: "Local-Global Feature Mixer and Trend-Guided Consistent Learning for Remaining Useful Life Prediction of Rotating Machinery"
author:
  - literal: "Hanbyeol Park"
  - literal: "Hyerim Bae"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.05925"

# Custom fields
paper_id: "2608.05925"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "robustness"
  - "evaluation"
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
processed_at: "2026-08-09T05:41:06Z"
created_at: "2026-08-09T05:41:06Z"
---

# Local-Global Feature Mixer and Trend-Guided Consistent Learning for Remaining Useful Life Prediction of Rotating Machinery

**Authors**: Hanbyeol Park, Hyerim Bae
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.05925](https://arxiv.org/abs/2608.05925)

## Summary

This paper proposes a remaining useful life (RUL) prediction framework for rotating machinery consisting of a local-global feature mixer (LGFM) and a trend-guided rollout-consistent (TG-RC) loss. The LGFM integrates health indicator sequences with statistical and degradation-specific features to capture multi-scale degradation dynamics while mitigating high-frequency noise sensitivity. Meanwhile, the TG-RC loss combines multi-step rollout and soft dynamic time warping alignment guided by a global trend prior to prevent error accumulation and preserve irreversible degradation trajectories during recursive forecasting. Experiments across two public bearing benchmarks demonstrate superior long-term extrapolation stability and RUL accuracy compared to conventional degradation modeling methods.

## Key Contributions

- Proposes a local-global feature mixer (LGFM) that combines health indicator sequences with statistical and degradation features to suppress high-frequency noise and capture both local and global degradation states.
- Introduces a trend-guided rollout-consistent (TG-RC) loss combining recursive multi-step rollout and soft dynamic time warping alignment with a global trend prior to mitigate error accumulation and preserve irreversible degradation trends.
- Demonstrates improved long-term health indicator extrapolation stability and remaining useful life (RUL) prediction across two public bearing datasets.

## Open Questions & Future Work

- [[adaptive-trend-prior-selection-rul]]

## Archivist Review

Reviewed the paper and its extracted candidates under strict vault standards. The proposed feature mixer and loss function are application-specific subcomponents for RUL prognostics and do not qualify for permanent standalone concepts. The open question on adaptive trend prior selection in RUL prediction addresses a meaningful methodological gap regarding manual functional priors and is approved.

### Approved Open Questions
- Adaptive Trend Prior Selection: Manual specification of trend priors limits the generalizability of trend-guided consistent learning across diverse mechanical degradation regimes, making an adaptive or learnable trend-family selection method crucial for robust autonomous RUL prognostics.

### Rejected Candidates
- [concept] Local-Global Feature Mixer (LGFM) (`local-global-feature-mixer-lgfm`) - subcomponent_of_broader_mechanism: Paper-internal feature mixing module specific to machinery degradation indicators, lacking broad architectural reusability across general time-series forecasting.
- [concept] Trend-Guided Rollout-Consistent Loss (TG-RC) (`trend-guided-rollout-consistent-loss-tg-rc`) - paper_local: Domain-specific training loss formulation tailored to remaining useful life prediction rather than a generally recurring methodological paradigm.

## Links

- [Abstract](https://arxiv.org/abs/2608.05925)
- [PDF](https://arxiv.org/pdf/2608.05925)


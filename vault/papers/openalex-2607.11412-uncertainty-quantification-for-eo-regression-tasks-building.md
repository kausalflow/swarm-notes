---
# CSL-compatible fields
title: "Uncertainty Quantification for EO Regression Tasks: Building Height, Tree Canopy Height and Above-ground Biomass Estimation"
author:
  - literal: "Ritu Yadav"
  - literal: "Andrea Nascetti"
  - literal: "Yifang Ban"
issued:
  date-parts:
    - [2026, 7, 13]
url: "https://arxiv.org/abs/2607.11412"

# Custom fields
paper_id: "2607.11412"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "multimodal"
  - "uncertainty-quantification"
  - "regression"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quantile-uncertainty-estimation-for-eo-regression"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-16T07:14:56Z"
created_at: "2026-07-16T07:14:56Z"
---

# Uncertainty Quantification for EO Regression Tasks: Building Height, Tree Canopy Height and Above-ground Biomass Estimation

**Authors**: Ritu Yadav, Andrea Nascetti, Yifang Ban
**Date**: 2026-07-13
**Paper ID**: [openalex:2607.11412](https://arxiv.org/abs/2607.11412)

## Summary

This paper addresses the lack of reliability in Earth Observation regression tasks by introducing uncertainty quantification for building height, canopy height, and biomass estimation. The authors propose two methods: a Gaussian uncertainty model for standard deviations and a Quantile uncertainty model for capturing asymmetric error distributions. Using a combination of Sentinel-1 SAR and Sentinel-2 MSI time-series data, these approaches provide calibrated confidence estimates that outperform existing deterministic models and state-of-the-art uncertainty-aware baselines.

## Key Contributions

- Proposed Gaussian and Quantile-based uncertainty quantification methods for multi-modal Earth Observation regression.
- Demonstrated superior uncertainty calibration for building height, tree canopy height, and above-ground biomass estimation compared to deterministic benchmarks.
- Achieved state-of-the-art performance in uncertainty-aware canopy height estimation at 10m resolution.

## Open Questions & Future Work

- [[uncertainty-calibration-in-saturated-tails]]

## Key Concepts

- [[quantile-uncertainty-estimation-for-eo-regression]]: A regression uncertainty quantification approach estimating specific quantiles to handle asymmetric and heteroscedastic noise in Earth Observation data.

## Archivist Review

The paper's contribution of applying quantile-based uncertainty quantification to remote sensing regression tasks is well-structured and reusable for broader spatial-temporal regression problems. The open question regarding saturated target estimation is a central, recurring challenge in earth observation regression that warrants tracking. The proposed hybrid framework was rejected as it is a speculative design suggestion rather than an established research bottleneck.

### Approved Concepts
- Quantile Uncertainty Estimation for EO Regression: Provides a robust way to model non-Gaussian, asymmetric error distributions common in remote sensing regression tasks.

### Approved Open Questions
- Uncertainty calibration for saturated targets: Addressing uncertainty calibration in high-value, saturated regions is critical for the operational reliability of EO products in applications like biomass monitoring and urban planning.

### Rejected Candidates
- [open_question] Hybrid uncertainty regression modeling (`hybrid-uncertainty-regression-models`) - weak_evidence: This is a speculative future work suggestion rather than a clearly defined research bottleneck or unresolved problem.

## Links

- [Abstract](https://arxiv.org/abs/2607.11412)
- [PDF](https://arxiv.org/pdf/2607.11412)


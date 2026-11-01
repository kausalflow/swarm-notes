---
# CSL-compatible fields
title: "Observability-Aligned Evidential Masked Pretraining for Reliable VRU Motion Prediction"
author:
  - literal: "Shang Gao"
  - literal: "Franz Götz-Hahn"
  - literal: "Konrad Doll"
  - literal: "Bernhard Sick"
  - literal: "Shang Gao"
  - literal: "Franz Götz-Hahn"
  - literal: "Konrad Doll"
  - literal: "Bernhard Sick"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2610.39958"

# Custom fields
paper_id: "2610.39958"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "transformer"
  - "self-supervised-learning</i>, <i>time-series</i>, <i>forecasting</i>, <i>robustness</i>, <i>dataset</i>, <i>evaluation</i>],title:"
  - "Observability-Aligned Evidential Masked Pretraining for Reliable VRU Motion Prediction"
  - "url:"
  - "https://arxiv.org/abs/2610.39958"
  - "}"
architectures:
  []
datasets:
  - "imptc"
  - "ind"
concept_slugs:
  - "ecomae"
dataset_slugs:
  - "imptc"
  - "ind"
skill: "TimeSeriesSkill"
processed_at: "2026-11-01T11:33:53Z"
created_at: "2026-11-01T11:33:53Z"
---

# Observability-Aligned Evidential Masked Pretraining for Reliable VRU Motion Prediction

**Authors**: Shang Gao, Franz Götz-Hahn, Konrad Doll, Bernhard Sick, Shang Gao, Franz Götz-Hahn, Konrad Doll, Bernhard Sick
**Date**: 2026-10-29
**Paper ID**: [openalex:2610.39958](https://arxiv.org/abs/2610.39958)

## Summary

The paper introduces eCoMAE, an evidential masked pretraining method for multivariate time series that aligns predictive uncertainty with data observability. By coupling block-wise time-step masking and a Normal-Inverse-Gamma decoder with observability-aware constraints (such as uncertainty-weighted mean consistency, evidence suppression, and stochastic mask consistency), eCoMAE enhances reliability under partial observability and distribution shift. Evaluations on VRU intention prediction and pedestrian trajectory forecasting across IMPTC, Waymo, nuScenes, and inD demonstrate superior out-of-distribution accuracy and calibration compared to deterministic masked autoencoding baselines.

## Key Contributions

- Introduces eCoMAE, an evidential masked pretraining method integrating block-wise masking and a Normal-Inverse-Gamma decoder with observability-aware constraints for multivariate time series.
- Improves OOD accuracy from 0.7971 to 0.8068 and reduces OOD AURC from 0.0718 to 0.0648 on the IMPTC benchmark for VRU intention prediction under weather shift.
- Achieves best fine-tuning mean squared error (MSE) across IMPTC, Waymo, nuScenes, and inD pedestrian trajectory forecasting benchmarks.

## Limitations

Not explicitly discussed in the abstract, but scope is focused on pedestrian trajectory forecasting and VRU motion prediction under partial observability and distribution shifts.

## Open Questions & Future Work

- [[adaptive-balancing-multimodal-shift]]

## Key Concepts

- [[ecomae]]: An evidential masked pretraining method for multivariate time series that explicitly aligns predictive evidence with observability.

## Archivist Review

Approved the core methodological concept eCoMAE along with its central open research direction on adaptive balancing under shift. Selected two named datasets while rejecting standard subcomponents to preserve vault quality.

### Approved Concepts
- eCoMAE: Introduces a novel evidential masked autoencoding paradigm for multivariate time series that aligns predictive evidence and uncertainty with data observability.

### Approved Open Questions
- Adaptive Balancing and Shift: Understanding how to adaptively balance evidential objectives and consistency terms across diverse multimodal domains and distribution shifts is critical for scaling reliable self-supervised time-series representation learning.

### Rejected Candidates
- [concept] Normal-Inverse-Gamma Decoder (`normal-inverse-gamma-decoder`) - subcomponent_of_broader_mechanism: Subcomponent of a broader evidential modeling framework; does not warrant a standalone vault entry beyond eCoMAE.

## Datasets

- [[imptc]]
- [[ind]]

## Links

- [Abstract](https://arxiv.org/abs/2610.39958)
- [PDF](https://arxiv.org/pdf/2610.39958)


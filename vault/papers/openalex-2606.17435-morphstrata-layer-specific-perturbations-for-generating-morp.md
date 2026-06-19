---
# CSL-compatible fields
title: "MorphStrata: Layer-Specific Perturbations for Generating Morphence Students in Time-Series Moving Target Defense"
author:
  - literal: "Abhishek Bhardwaj"
  - literal: "Arnav Doshi"
  - literal: "Anusri Nagarajan"
  - literal: "Thanh Quynh Nhu Ta"
  - literal: "Mohammad Masum"
  - literal: "Robert Chun"
  - literal: "Jaydip Sen"
  - literal: "Saptarshi Sengupta"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.17435"

# Custom fields
paper_id: "2606.17435"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "time-series"
  - "adversarial-examples"
  - "robustness"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "morphstrata"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:24:27Z"
created_at: "2026-06-19T09:24:27Z"
---

# MorphStrata: Layer-Specific Perturbations for Generating Morphence Students in Time-Series Moving Target Defense

**Authors**: Abhishek Bhardwaj, Arnav Doshi, Anusri Nagarajan, Thanh Quynh Nhu Ta, Mohammad Masum, Robert Chun, Jaydip Sen, Saptarshi Sengupta
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.17435](https://arxiv.org/abs/2606.17435)

## Summary

MorphStrata is a novel student generation strategy designed to enhance the robustness of Moving Target Defense (MTD) in time-series forecasting. By applying selective, layer-specific stochastic noise to Transformer-based models, the approach creates structured heterogeneity among student models with minimal computational overhead. Extensive evaluations on climate and energy datasets demonstrate that MorphStrata consistently outperforms static baselines against common gradient-based adversarial attacks, including FGSM, BIM, and PGD.

## Key Contributions

- Introduces MorphStrata, a layer-specific stochastic noise injection strategy for generating heterogeneous students in Moving Target Defense frameworks.
- Improves adversarial RMSE on high-entropy periodic datasets (AEP) by up to 24.11% (FGSM) and 97.97% (BIM) compared to static baselines.
- Achieves significant gains in adversarial robustness with less than 1% increase in training time overhead relative to the baseline Morphence MTD approach.

## Open Questions & Future Work

- [[temporal-structure-aware-mtd-scaling]]

## Key Concepts

- [[morphstrata]]: A student generation strategy for Moving Target Defense that utilizes selective, layer-specific stochastic noise injection to improve adversarial robustness.

## Archivist Review

Approved MorphStrata as a novel MTD student generation strategy for its structured approach to model heterogeneity via layer-specific noise injection. The open question was refined to emphasize the broader challenge of adapting MTD perturbations to temporal dataset characteristics. Standard datasets were rejected as they are common benchmarks in the existing vault.

### Approved Concepts
- MorphStrata: It introduces a novel method for generating heterogeneous student models in a Moving Target Defense (MTD) framework with minimal training overhead.

### Approved Open Questions
- Temporal-Structure-Aware MTD Scaling: The effectiveness of MTD is highly dataset-dependent and tied to temporal properties; finding a systematic way to adapt to these properties is the logical next step for robust defense design.

### Rejected Candidates
- [dataset] Jena Climate (`jena-climate`) - not_reusable: This is a routine benchmark dataset commonly used in time-series research.
- [dataset] Electricity Load Diagrams (`electricity-load-diagrams`) - not_reusable: This is a routine benchmark dataset commonly used in time-series research.
- [dataset] Appliances Energy Prediction (`appliances-energy-prediction`) - not_reusable: This is a routine benchmark dataset commonly used in time-series research.

## Links

- [Abstract](https://arxiv.org/abs/2606.17435)
- [PDF](https://arxiv.org/pdf/2606.17435)


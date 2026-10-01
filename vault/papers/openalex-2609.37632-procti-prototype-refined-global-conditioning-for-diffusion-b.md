---
# CSL-compatible fields
title: "ProCTI: Prototype-Refined Global Conditioning for Diffusion-Based Time Series Imputation"
author:
  - literal: "Fariza Rashid"
  - literal: "Duc Van Le"
  - literal: "Rahat Masood"
  - literal: "Gustavo Batista"
  - literal: "Aruna Seneviratne"
  - literal: "Suranga Seneviratne"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.37632"

# Custom fields
paper_id: "2609.37632"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "diffusion-model"
  - "generative-adversarial-network"
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
processed_at: "2026-10-01T11:15:23Z"
created_at: "2026-10-01T11:15:23Z"
---

# ProCTI: Prototype-Refined Global Conditioning for Diffusion-Based Time Series Imputation

**Authors**: Fariza Rashid, Duc Van Le, Rahat Masood, Gustavo Batista, Aruna Seneviratne, Suranga Seneviratne
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.37632](https://arxiv.org/abs/2609.37632)

## Summary

ProCTI is a diffusion-based time series imputation framework that enhances traditional local context conditioning with retrieved global dataset-level priors via learned prototypes. By utilizing a hybrid conditioning mechanism during the reverse diffusion process, the framework improves reconstruction under sparse, noisy, or unrepresentative missingness. Extensive evaluations on benchmark datasets demonstrate consistent performance gains over strong baselines under random missingness. Additionally, a theoretical analysis using a latent-regime data model explicitly characterizes the advantages of combining local and global conditioning.

## Key Contributions

- Proposes ProCTI, a diffusion-imputation framework combining local conditioning with retrieved global dataset-level priors via learned prototypes.
- Integrates global context and local signals using a hybrid conditioning mechanism during reverse diffusion to handle sparse and noisy missingness.
- Provides a latent-regime data model and theoretical analysis characterizing the exact conditions where prototype-derived global conditioning improves imputation.

## Limitations

Evaluated primarily on standard missingness scenarios (random and attribute-wise); performance under extreme distribution shifts is not fully explored.

## Archivist Review

Applied strict scarcity and reusability standards. The proposed concept 'ProCTI' is paper-local nomenclature for a specific imputation architecture, and the open question is standard boilerplate future work. Thus, all candidates were rejected.

### Rejected Candidates
- [concept] ProCTI (`procti`) - paper_local: ProCTI is a paper-specific method name for a diffusion imputation framework rather than a broad, reusable standalone concept.
- [open_question] Prototype Interpretability and Non-Stationary Regimes (`prototype-interpretability-non-stationary-regimes`) - low_impact: This open question touches on standard future work directions regarding interpretability and non-stationarity without posing a precise, highly specific unresolved bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.37632)
- [PDF](https://arxiv.org/pdf/2609.37632)


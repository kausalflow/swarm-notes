---
# CSL-compatible fields
title: "VLBM: Variational Latent Basis Modeling for OOD Robust Multivariate Time Series Forecasting"
author:
  - literal: "Xudong Zhang"
  - literal: "Jierui Lei"
  - literal: "Jiacheng Li"
  - literal: "Lingdong Shen"
  - literal: "Jian Cui"
  - literal: "H.G. Tang"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.02138"

# Custom fields
paper_id: "2606.02138"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "variational-latent-basis-modeling-vlbm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:42:46Z"
created_at: "2026-06-04T08:42:46Z"
---

# VLBM: Variational Latent Basis Modeling for OOD Robust Multivariate Time Series Forecasting

**Authors**: Xudong Zhang, Jierui Lei, Jiacheng Li, Lingdong Shen, Jian Cui, H.G. Tang
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.02138](https://arxiv.org/abs/2606.02138)

## Summary

VLBM addresses the limitation of average-risk training in time series forecasting by explicitly decoupling stable dynamics from rare, high-impact OOD deviations. The model leverages a shared latent basis to define a low-rank subspace for stable patterns while isolating orthogonal residuals, enabling improved handling of OOD shifts. By aligning a future-blind inference prior with a future-aware posterior, the framework ensures consistent and robust latent representations under distributional drift. Evaluation across 12 diverse real-world and synthetic datasets demonstrates significant performance gains in both OOD robustness and ID forecasting accuracy compared to existing baselines.

## Key Contributions

- Proposes VLBM, a latent forecasting framework that explicitly separates stable ID dynamics from OOD-induced residuals using a low-rank basis subspace.
- Implements an alignment objective between a future-aware posterior and a future-blind prior to ensure robust test-time latent inference.
- Achieves state-of-the-art robustness and accuracy on 12 benchmark tasks across various domains, yielding 15.08% and 7.74% average MAE and MSE improvements.

## Open Questions & Future Work

- [[coupled-id-ood-dynamics-forecasting]]

## Key Concepts

- [[variational-latent-basis-modeling-vlbm]]: A latent forecasting framework that decomposes multivariate time series into a shared low-rank subspace for stable dynamics and orthogonal residuals for OOD-induced deviations.

## Archivist Review

I have approved the VLBM framework as a representative latent decomposition method for time series robustness and the open question regarding the coupling of ID and OOD dynamics as it highlights a fundamental limitation in current temporal forecasting research. I rejected the initial concept slug for VLBM to align better with standard naming conventions for frameworks in the vault and tightened the title of the open question for conciseness. No datasets were approved as they were described as either generic groups of tasks or unnamed construction categories.

### Approved Concepts
- Variational Latent Basis Modeling (VLBM): Provides a principled latent-space approach to decoupling stable temporal dynamics from OOD-driven residuals, improving robustness against distribution shifts.

### Approved Open Questions
- Coupled ID OOD Dynamics: This is a fundamental bottleneck for safety-critical forecasting in environments where system failures are dynamically coupled with normal behavior.

## Links

- [Abstract](https://arxiv.org/abs/2606.02138)
- [PDF](https://arxiv.org/pdf/2606.02138)


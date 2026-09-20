---
# CSL-compatible fields
title: "A physics-informed inverse modeling framework for Moose-Wolf dynamics from limited and noisy data in Isle Royale National Park"
author:
  - literal: "Anurag Singh"
  - literal: "Nitu Kumari"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.20793"

# Custom fields
paper_id: "2609.20793"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-20T09:31:10Z"
created_at: "2026-09-20T09:31:10Z"
---

# A physics-informed inverse modeling framework for Moose-Wolf dynamics from limited and noisy data in Isle Royale National Park

**Authors**: Anurag Singh, Nitu Kumari
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.20793](https://arxiv.org/abs/2609.20793)

## Summary

This paper proposes a physics-informed inverse modeling framework to study moose and wolf population dynamics in Isle Royale National Park from limited and noisy observational data. By modeling the non-autonomous prey-predator system with a self-adaptive physics-informed neural network (PINN) featuring transfer learning, the authors recover both time-dependent and constant system parameters. Results show that the ratio-dependent model accurately captures long-term trends and successfully predicts the sudden moose population decline in 2020.

## Key Contributions

- Formulates a non-autonomous prey-predator system for Moose-Wolf population dynamics in Isle Royale National Park incorporating time-varying intrinsic growth, natural death rates, and functional responses.
- Employs a self-adaptive boundary-conditioned physics-informed neural network (bc-PINN) with transfer learning to solve the inverse problem for estimating time-dependent and constant parameters from population time series data (1959-2019).
- Demonstrates that the ratio-dependent functional response model exhibits superior prediction trends beyond the training data, successfully predicting the sudden moose population decline in 2020.

## Open Questions & Future Work

- [[incorporating-discontinuous-ecological-shocks]]

## Archivist Review

Approved the open question regarding discontinuous ecological shocks because it identifies a fundamental limitation in continuous ODE/PINN modeling for real-world systems subject to abrupt perturbations. Rejected the local model architecture as a concept since it represents a routine combination of existing PINN variations applied to prey-predator dynamics.

### Approved Open Questions
- Incorporating Discontinuous Ecological Shocks: Addressing structural model misspecification caused by sudden real-world shocks (disease, translocation) is critical for advancing physics-informed machine learning applications in ecology and complex dynamical systems.

### Rejected Candidates
- [concept] bc-PINN with Transfer Learning for Ecological Inverse Problems (`bc-pinn-transfer-learning-ecosystems`) - paper_local: Paper-local combination of standard physics-informed neural network techniques applied to a specific ecological dataset.

## Links

- [Abstract](https://arxiv.org/abs/2609.20793)
- [PDF](https://arxiv.org/pdf/2609.20793)


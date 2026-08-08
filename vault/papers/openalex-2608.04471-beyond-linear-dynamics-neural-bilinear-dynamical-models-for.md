---
# CSL-compatible fields
title: "Beyond Linear Dynamics: Neural Bilinear Dynamical Models for Time Series Forecasting"
author:
  - literal: "Mengzhou Gao"
  - literal: "Huangqian Yu"
  - literal: "Pengfei Jiao"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.04471"

# Custom fields
paper_id: "2608.04471"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "state-space-model"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  - "neural-bilinear-dynamical-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-08T05:34:07Z"
created_at: "2026-08-08T05:34:07Z"
---

# Beyond Linear Dynamics: Neural Bilinear Dynamical Models for Time Series Forecasting

**Authors**: Mengzhou Gao, Huangqian Yu, Pengfei Jiao
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.04471](https://arxiv.org/abs/2608.04471)

## Summary

The paper introduces the Neural Bilinear Dynamical Model (NBDM) for time series forecasting, which overcomes the limitations of linear dynamical assumptions by lifting nonlinear dynamics into a higher-dimensional latent space using Koopman theory and modeling state evolution via a bilinear dynamical formulation. To address approximation errors and scenarios with missing control inputs, NBDM incorporates a parameterized error compensation term and a memory-enhanced controller. Extensive experiments on five real-world datasets show that NBDM outperforms existing baselines, especially for multi-step and long-horizon forecasting.

## Key Contributions

- Proposes the Neural Bilinear Dynamical Model (NBDM) to model nonlinear time series dynamics through a bilinear latent dynamical formulation in a higher-dimensional latent space.
- Incorporates a parameterized error compensation term to mitigate approximation errors introduced by bilinear representations.
- Designs a memory-enhanced controller utilizing multiplicative interactions between historical states and control signals to handle missing control inputs effectively.
- Demonstrates consistent performance improvements over competitive baselines across five real-world datasets for multi-step and long-horizon forecasting.

## Open Questions & Future Work

- [[beyond-bilinear-dynamics-uncertainty-control]]

## Key Concepts

- [[neural-bilinear-dynamical-model]]: A time series forecasting model that leverages Koopman theory and a bilinear latent dynamical formulation with error compensation to capture complex nonlinear system dynamics.

## Archivist Review

Approved the core Neural Bilinear Dynamical Model concept and its corresponding open question regarding extensions beyond bilinear approximations and uncertainty-aware control. Kept selections strictly scarce in accordance with vault standards.

### Approved Concepts
- Neural Bilinear Dynamical Model: NBDM provides a novel bilinear latent dynamical formulation combined with Koopman theory and error compensation to capture complex nonlinear behaviors in time series forecasting.

### Approved Open Questions
- Beyond Bilinear Dynamics and Uncertainty-Aware Control: Extending modeling beyond bilinear dynamics and incorporating uncertainty-aware control are crucial next steps for overcoming the representation capacity limits of current Koopman-based forecasting frameworks.

## Links

- [Abstract](https://arxiv.org/abs/2608.04471)
- [PDF](https://arxiv.org/pdf/2608.04471)


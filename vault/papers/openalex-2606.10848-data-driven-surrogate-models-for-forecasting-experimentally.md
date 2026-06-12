---
# CSL-compatible fields
title: "Data-driven surrogate models for forecasting experimentally measured fluid flows"
author:
  - literal: "Peter I. Renn"
  - literal: "Emily H. Palmer"
  - literal: "Cong Wang"
  - literal: "Morteza Gharib"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10848"

# Custom fields
paper_id: "2606.10848"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "cnn"
  - "fourier-neural-operator"
  - "time-series"
architectures:
  - "convolutional-neural-network"
datasets:
  []
concept_slugs:
  - "fourier-neural-operator"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:53:30Z"
created_at: "2026-06-12T08:53:30Z"
---

# Data-driven surrogate models for forecasting experimentally measured fluid flows

**Authors**: Peter I. Renn, Emily H. Palmer, Cong Wang, Morteza Gharib
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10848](https://arxiv.org/abs/2606.10848)

## Summary

This study investigates the efficacy of data-driven surrogate models in forecasting experimentally measured fluid flows, specifically cylinder wakes in subcritical vortex shedding regimes. The authors compare multiple architectures, including U-Nets and Fourier Neural Operators, using noisy particle image velocimetry measurements across various Reynolds numbers. The results indicate that while these models enable faster-than-real-time evaluation and capture low-frequency dynamics effectively, they often fail to preserve transient features and high-frequency content when applied to imperfect, real-world data.

## Key Contributions

- Systematic evaluation of four data-driven surrogate models (CNN, U-Net, FNO, DMD) on predicting experimentally measured cylinder wake dynamics.
- Demonstration that models successfully propagate low-frequency fluid dynamics but struggle with high-frequency energy preservation under noisy experimental conditions.
- Investigation of model robustness across a broad Reynolds number range (Re=230 to 2920) to assess the impact of turbulence on forecast quality.

## Open Questions & Future Work

- [[forecasting-turbulent-flows-with-incomplete-data]]

## Key Concepts

- [[fourier-neural-operator]]: A neural operator architecture that learns mappings between function spaces by performing convolutions in the Fourier domain.

## Archivist Review

I approved the Fourier Neural Operator as a central, reusable architectural concept and the open question regarding turbulent flow forecasting with incomplete data as it highlights a fundamental limitation in scientific machine learning. Other models listed (CNN, U-Net) were rejected as generic or standard building blocks, and no specific datasets were identified as central novel contributions or critically missing from the current vault.

### Approved Concepts
- Fourier Neural Operator: It is a standard architectural approach in scientific machine learning that the paper evaluates for fluid flow forecasting.

### Approved Open Questions
- Forecasting Turbulent Flows with Incomplete Data: This issue is a central hurdle for applying machine learning to real-world engineering fluid mechanics.

## Links

- [Abstract](https://arxiv.org/abs/2606.10848)
- [PDF](https://arxiv.org/pdf/2606.10848)


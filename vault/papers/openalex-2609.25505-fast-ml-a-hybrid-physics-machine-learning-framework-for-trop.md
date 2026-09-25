---
# CSL-compatible fields
title: "FAST-ML: A Hybrid Physics-Machine Learning Framework for Tropical Cyclone Intensity Forecasting"
author:
  - literal: "Shijie Xiao"
  - literal: "Jonathan Lin"
  - literal: "Thomas Ehrmann"
  - literal: "Ali Sarhadi"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.25505"

# Custom fields
paper_id: "2609.25505"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  - "era5"
concept_slugs:
  - "fast-ml"
dataset_slugs:
  - "era5"
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:54:46Z"
created_at: "2026-09-25T09:54:46Z"
---

# FAST-ML: A Hybrid Physics-Machine Learning Framework for Tropical Cyclone Intensity Forecasting

**Authors**: Shijie Xiao, Jonathan Lin, Thomas Ehrmann, Ali Sarhadi
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.25505](https://arxiv.org/abs/2609.25505)

## Summary

Rapid intensification of tropical cyclones remains a difficult challenge, requiring balancing the computational expense of full-physics models with the interpretability limitations of pure data-driven approaches. The authors present FAST-ML, a hybrid physics-machine learning framework that utilizes a physically informed dual-stream neural parameterization to ingest 3D ERA5 fields and diagnose ventilation controls. Optimized end-to-end through a differentiable intensity model, FAST-ML significantly reduces ensemble CRPS and cuts the rapid intensification false alarm ratio while maintaining detection skill. Furthermore, it demonstrates zero-shot cross-basin transferability on Eastern Pacific storms, offering an efficient and interpretable alternative for operational forecasting.

## Key Contributions

- Proposed FAST-ML, a hybrid physics-machine learning framework combining data-driven efficiency with physical constraints for tropical cyclone intensity forecasting.
- Developed a physically informed dual-stream neural parameterization to diagnose ventilation controls and optimize them end-to-end through a differentiable intensity model.
- Demonstrated a 31% reduction in ensemble CRPS at 60 h and nearly halved the rapid intensification false alarm ratio compared to the physical baseline.
- Showed promising zero-shot cross-basin transferability on selected Eastern Pacific storms.

## Open Questions & Future Work

- [[jointly-optimizing-physical-terms-in-governing-equations-for-tropical-cyclone-forecasting]]

## Key Concepts

- [[fast-ml]]: A hybrid physics-machine learning framework that integrates data-driven efficiency with physical constraints for tropical cyclone intensity forecasting.

## Archivist Review

Approved the central hybrid model framework (FAST-ML) and its corresponding open question on extending differentiable physical parameter optimization in governing equations. Also archived ERA5 as a key dataset used for ingestion and training. Applied rigorous selectivity to ensure long-term vault quality.

### Approved Concepts
- FAST-ML: It is the core hybrid physics-machine learning framework proposed in the paper for tropical cyclone intensity forecasting.

### Approved Open Questions
- Jointly Optimizing Physical Terms in Governing Equations: Expanding differentiable physical parameter optimization to cover additional thermodynamic and dynamic coefficients enables a more complete data-driven resolution of complex hurricane evolution processes.

## Datasets

- [[era5]]

## Links

- [Abstract](https://arxiv.org/abs/2609.25505)
- [PDF](https://arxiv.org/pdf/2609.25505)


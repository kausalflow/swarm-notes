---
# CSL-compatible fields
title: "Bayesian Tensor-on-Tensor Varying Coefficient Model for Forecasting Alzheimer's Disease Progression"
author:
  - literal: "Yajie Liu"
  - literal: "Hengrui Luo"
  - literal: "Suprateek Kundu"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2604.07764"

# Custom fields
paper_id: "2604.07764"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  - "alzheimers-disease-neuroimaging-initiative"
concept_slugs:
  - "bayesian-tensor-on-tensor-varying-coefficient-model"
dataset_slugs:
  - "alzheimers-disease-neuroimaging-initiative"
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:19:24Z"
created_at: "2026-04-12T06:19:24Z"
---

# Bayesian Tensor-on-Tensor Varying Coefficient Model for Forecasting Alzheimer's Disease Progression

**Authors**: Yajie Liu, Hengrui Luo, Suprateek Kundu
**Date**: 2026-04-09
**Paper ID**: [openalex:2604.07764](https://arxiv.org/abs/2604.07764)

## Summary

This paper introduces a Bayesian tensor-on-tensor framework designed for longitudinal neuroimaging forecasting, specifically targeting Alzheimer's disease progression. The model integrates Gaussian process priors to capture nonlinear relationships while utilizing low-rank tensor coefficients to preserve and exploit the spatial structure of volumetric data. An efficient parallel MCMC algorithm is developed to ensure scalability for high-dimensional image analysis. Validation on the ADNI dataset confirms the model's effectiveness in forecasting cortical thickness and its clinical utility for predicting brain aging.

## Key Contributions

- Introduced a Bayesian tensor-on-tensor framework that models nonlinear relationships via Gaussian process priors and maintains spatial structure through low-rank coefficients.
- Developed an efficient MCMC algorithm leveraging parallel structure for scalable voxel-specific GP sampling and low-rank tensor coefficient updates.
- Demonstrated superior performance in forecasting longitudinal cortical thickness and brain aging on ADNI MRI data compared to existing statistical and neural baselines.

## Open Questions & Future Work

- [[non-linear-gp-tot-modeling]]

## Key Concepts

- [[bayesian-tensor-on-tensor-varying-coefficient-model]]: A Bayesian modeling framework for forecasting 3D image-based neurobiological progression that captures spatial heterogeneity and nonlinear relationships using tensor-structured coefficients and GP priors.

## Archivist Review

The proposed Bayesian tensor-on-tensor model offers a significant methodological advancement for high-dimensional neuroimaging forecasting by effectively merging Gaussian process priors with low-rank tensor structures. I have approved this concept and the associated research question on non-linear GP integration, as they provide a clear, reusable framework for longitudinal volumetric data prediction. The ADNI dataset is also approved as a critical, standard-setting longitudinal clinical dataset.

### Approved Concepts
- Bayesian Tensor-on-Tensor Varying Coefficient Model: It introduces a novel framework for high-dimensional image forecasting by combining GP-based nonlinearity with low-rank tensor spatial priors.

### Approved Open Questions
- Non-linear GP Tensor Regression: This is technically important because it addresses the core modeling limitation of linearity in high-dimensional tensor regression, which is critical for accurately capturing complex biological or physical processes in longitudinal studies.

## Datasets

- [[alzheimers-disease-neuroimaging-initiative]]

## Links

- [Abstract](https://arxiv.org/abs/2604.07764)
- [PDF](https://arxiv.org/pdf/2604.07764)


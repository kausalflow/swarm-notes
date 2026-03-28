---
# CSL-compatible fields
title: "Embracing Heteroscedasticity for Probabilistic Time Series Forecasting"
author:
  - literal: "Yijun Wang"
  - literal: "Qiyuan Zhuang"
  - literal: "Xiu-Shen Wei"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24254"

# Custom fields
paper_id: "2603.24254"
paper_source: "openalex"
domain: "time-series"
tags:
  - "variational-autoencoder"
  - "time-series"
  - "forecasting"
  - "probabilistic-forecasting"
  - "heteroscedasticity"
  - "evaluation"
architectures:
  - "variational-autoencoder"
  - "vae"
datasets:
  []
concept_slugs:
  - "location-scale-gaussian-vae-lsg-vae"
  - "adaptive-attenuation-mechanism-volatility-downweighting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:28:31Z"
created_at: "2026-03-28T05:28:31Z"
---

# Embracing Heteroscedasticity for Probabilistic Time Series Forecasting

**Authors**: Yijun Wang, Qiyuan Zhuang, Xiu-Shen Wei
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24254](https://arxiv.org/abs/2603.24254)

## Summary

This paper addresses the limitation of existing non-autoregressive probabilistic time series forecasting (PTSF) models, which often implicitly assume homoscedasticity due to MSE-based objectives. The authors propose the Location-Scale Gaussian VAE (LSG-VAE), which explicitly models time-varying conditional variance using a location-scale likelihood formulation, enabling faithful capture of aleatoric uncertainty. LSG-VAE also incorporates an adaptive attenuation mechanism to robustly handle high-volatility observations during training. Experiments across nine benchmarks show LSG-VAE significantly outperforms fifteen strong generative baselines while maintaining efficiency.

## Key Contributions

- Proposed Location-Scale Gaussian VAE (LSG-VAE), a generative PTSF framework that explicitly parameterizes time-dependent variance via a location-scale likelihood, overcoming the homoscedastic bias of models like TimeVAE.
- Introduced an adaptive attenuation mechanism to automatically down-weight highly volatile observations during training, enhancing robustness in trend prediction.
- Demonstrated consistent outperformance against fifteen strong generative baselines across nine benchmark datasets in probabilistic forecasting tasks.

## Limitations

The abstract does not specify any explicit limitations or future work directions beyond the scope of the main proposal.

## Key Concepts

- [[location-scale-gaussian-vae-lsg-vae]]: A VAE framework for probabilistic time series forecasting that explicitly models time-dependent conditional variance using a location-scale likelihood formulation.
- [[adaptive-attenuation-mechanism-volatility-downweighting]]: A mechanism within LSG-VAE that automatically reduces the influence of highly volatile training observations to improve trend prediction robustness.

## Archivist Review

Two primary concepts were approved: the Location-Scale Gaussian VAE (LSG-VAE) as the core modeling framework, and the Adaptive Attenuation Mechanism as a reusable training stability technique for heteroscedastic models. No specific open questions were identified, and the single dataset mentioned (ETTh1) is a generic benchmark that does not require a unique vault entry. The review focused on approving mechanisms central to handling time-varying uncertainty in sequence generation.

### Approved Concepts
- Location-Scale Gaussian VAE (LSG-VAE): LSG-VAE is the core proposed method that explicitly models heteroscedasticity in probabilistic forecasting using a location-scale likelihood.
- Adaptive Attenuation Mechanism: This is a novel training regularization technique specifically designed to improve robustness in heteroscedastic modeling by managing the impact of high-variance points.

### Rejected Candidates
- [dataset] ETTh1 (`ETTh1`) - low_impact: ETTh1 is a common benchmark dataset that does not warrant a standalone vault entry unless the paper introduced it or showed a novel technique uniquely applicable to it.

## Links

- [Abstract](https://arxiv.org/abs/2603.24254)
- [PDF](https://arxiv.org/pdf/2603.24254)


---
# CSL-compatible fields
title: "Outperforming Self-Attention Mechanisms in Solar Irradiance Forecasting via Physics-Guided Neural Networks"
author:
  - literal: "Mohammed Ezzaldin Babiker Abdullah"
  - literal: "R. R Mohammed"
issued:
  date-parts:
    - [2026, 4, 15]
url: "https://arxiv.org/abs/2604.13455"

# Custom fields
paper_id: "2604.13455"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "physics-informed"
  - "cnn"
  - "lstm"
  - "time-series"
  - "transformer"
  - "attention-mechanism"
  - "bayesian-optimization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "complexity-paradox-meteorological-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-18T06:06:55Z"
created_at: "2026-04-18T06:06:55Z"
---

# Outperforming Self-Attention Mechanisms in Solar Irradiance Forecasting via Physics-Guided Neural Networks

**Authors**: Mohammed Ezzaldin Babiker Abdullah, R. R Mohammed
**Date**: 2026-04-15
**Paper ID**: [openalex:2604.13455](https://arxiv.org/abs/2604.13455)

## Summary

This paper introduces a physics-informed hybrid CNN-BiLSTM framework designed to improve Global Horizontal Irradiance (GHI) forecasting by prioritizing domain-engineered features over complex architectural depth. By integrating physical variables like clear-sky indices and solar zenith angles, the model effectively addresses noise in meteorological data. Experimental results using the NASA POWER dataset demonstrate significant performance gains over standard transformer-based architectures, underscoring the benefits of physics-guided approaches in real-time renewable energy management.

## Key Contributions

- Introduces a lightweight, physics-informed hybrid CNN-BiLSTM architecture that integrates 15 domain-specific features for global horizontal irradiance forecasting.
- Demonstrates that incorporating physical constraints achieves an RMSE of 19.53 W/m^2, outperforming complex attention-based baselines (RMSE 30.64 W/m^2) on the NASA POWER dataset.
- Validates the 'Complexity Paradox', showing that explicit physical guidance provides better accuracy and efficiency than deep data-driven attention mechanisms in noisy meteorological environments.

## Key Concepts

- [[complexity-paradox-meteorological-forecasting]]: The phenomenon where simpler, physics-constrained models outperform high-complexity architectures in noisy, domain-specific forecasting tasks.

## Archivist Review

I approved the 'Complexity Paradox' concept as it represents an important shift in architectural philosophy for specialized time-series domains, contrasting with the 'complexity-first' trend. I rejected the NASA POWER dataset because it is a broad atmospheric data resource rather than a specific, benchmark-defined dataset suitable for a standalone vault entry. No other candidates were provided.

### Approved Concepts
- Complexity Paradox (meteorological forecasting): It challenges the dominant trend of using increasingly complex architectures for time-series forecasting by providing a counter-argument based on the integration of domain knowledge.

### Rejected Candidates
- [dataset] NASA POWER (`nasa-power`) - not_reusable: This is a general public data portal rather than a specific, standardized benchmark dataset for research.

## Links

- [Abstract](https://arxiv.org/abs/2604.13455)
- [PDF](https://arxiv.org/pdf/2604.13455)


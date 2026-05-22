---
# CSL-compatible fields
title: "Probabilistic Multivariate Time Series Forecasting with Diffusion Copulas"
author:
  - literal: "David Huk"
  - literal: "Dongshan Wang"
  - literal: "Miha Brešar"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.19685"

# Custom fields
paper_id: "2605.19685"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "mixture-density-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "diffusion-copula-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:16:44Z"
created_at: "2026-05-22T08:16:44Z"
---

# Probabilistic Multivariate Time Series Forecasting with Diffusion Copulas

**Authors**: David Huk, Dongshan Wang, Miha Brešar
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.19685](https://arxiv.org/abs/2605.19685)

## Summary

This paper addresses the tendency of end-to-end diffusion models to underestimate tail risk in multivariate financial forecasting by introducing a Diffusion-Copula framework. The approach decouples the modeling of marginal distributions, handled by Mixture Density Networks to capture heavy tails, from the joint dependence structure, addressed via a Classification-Diffusion Copula. The resulting model improves the identification of systemic extremes, successfully capturing correlations during market contagion events where baseline models fail.

## Key Contributions

- Introduces a Diffusion-Copula framework that decouples marginal distribution learning from joint dependence structure to mitigate normality bias.
- Utilizes deep Mixture Density Networks to accurately model heavy-tailed asset dynamics in financial time series.
- Demonstrates superior performance over state-of-the-art baselines in identifying systemic extreme events ('Expected Crashes') in cryptocurrency markets.

## Open Questions & Future Work

- [[marginal-error-propagation-copula-forecasting]]

## Key Concepts

- [[diffusion-copula-framework]]: A forecasting architecture that decouples marginal distribution learning via Mixture Density Networks from dependence modeling using a Classification-Diffusion Copula.

## Archivist Review

I have approved the core methodological contribution (Diffusion-Copula framework) as it offers a reusable, modular strategy for multivariate time series forecasting that addresses the common 'normality bias'. I have also approved an open question regarding error propagation in modular copula-based systems, as this is a fundamental research challenge in probabilistic forecasting. Other items were rejected for being domain-specific or subcomponents already captured by the broader framework.

### Approved Concepts
- Diffusion-Copula framework: Addresses the common trade-off between marginal calibration and joint coherence in multivariate financial time series forecasting, particularly concerning tail risk.

### Approved Open Questions
- Mitigating marginal error propagation: This represents a fundamental trade-off between modular flexibility and error accumulation, which is critical for the reliability of risk management tools in high-dimensional multivariate systems.

## Links

- [Abstract](https://arxiv.org/abs/2605.19685)
- [PDF](https://arxiv.org/pdf/2605.19685)


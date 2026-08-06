---
# CSL-compatible fields
title: "Latent-Regime Bias Auditing for Volatility Forecasting"
author:
  - literal: "Arthur Chagas"
  - literal: "Pedro Bento"
  - literal: "Yan Aquino"
  - literal: "Arthur Buzelin"
  - literal: "Meira"
  - literal: "Wagner, Jr."
  - literal: "Cristiano Arbex Valle"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.01599"

# Custom fields
paper_id: "2608.01599"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "latent-regime-bias-auditing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:31:33Z"
created_at: "2026-08-06T07:31:33Z"
---

# Latent-Regime Bias Auditing for Volatility Forecasting

**Authors**: Arthur Chagas, Pedro Bento, Yan Aquino, Arthur Buzelin, Meira, Wagner, Jr., Cristiano Arbex Valle
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.01599](https://arxiv.org/abs/2608.01599)

## Summary

This paper proposes a model-agnostic audit framework to evaluate volatility forecast reliability across latent market regimes, addressing the limitation that aggregate metrics like RMSE and MAE hide critical conditional failures. By learning time-series representations of market-state windows and clustering them into regimes, the method uncovers regime-specific bias, tail underprediction, and economic losses. Applied to cryptocurrency and ETF datasets, the audit reveals that models boasting competitive average accuracy can still fail severely in specific market regimes.

## Key Contributions

- Proposes a model-agnostic audit framework that evaluates volatility forecasts across latent market regimes using time-series representations and clustering.
- Demonstrates through cryptocurrency and ETF asset evaluations that models with high aggregate accuracy can exhibit substantial regime-specific bias and severe tail underprediction.
- Shifts volatility forecast evaluation from average global metrics (RMSE, MAE) to regime-conditional bias, tail underprediction, and underprediction-sensitive economic losses.

## Open Questions & Future Work

- [[conditional-bias-mitigation-forecasting]]

## Key Concepts

- [[latent-regime-bias-auditing]]: A model-agnostic audit framework for evaluating volatility forecast reliability and bias across latent market regimes.

## Archivist Review

Approved the core model-agnostic auditing framework concept and the associated future research question on mitigating conditional bias in volatility forecasting. Followed vault guidelines for scrupulously scarce selection and maintained rigorous standards.

### Approved Concepts
- Latent-Regime Bias Auditing: It introduces a dedicated model-agnostic framework for auditing volatility forecasts across latent market regimes, addressing conditional failures hidden by aggregate metrics.

### Approved Open Questions
- Conditional Bias Mitigation in Volatility Forecasting: This direction bridges the gap between post-hoc model auditing and active model training, enabling the creation of risk-aware forecasting architectures tailored for extreme market conditions.

## Links

- [Abstract](https://arxiv.org/abs/2608.01599)
- [PDF](https://arxiv.org/pdf/2608.01599)


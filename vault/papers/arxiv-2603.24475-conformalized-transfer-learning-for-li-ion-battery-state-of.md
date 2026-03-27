---
# CSL-compatible fields
title: "Conformalized Transfer Learning for Li-ion Battery State of Health Forecasting under Manufacturing and Usage Variability"
author:
  - literal: "Samuel Filgueira da Silva"
  - literal: "Mehmet Fatih Ozkan"
  - literal: "Faissal El Idrissi"
  - literal: "Marcello Canova"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24475"

# Custom fields
paper_id: "2603.24475"
paper_source: "arxiv"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "transfer-learning"
  - "anomaly-detection"
  - "uncertainty-quantification"
  - "evaluation"
architectures:
  - "lstm"
datasets:
  []
skill: "GeneralMLSkill"
processed_at: "2026-03-26T06:26:46Z"
created_at: "2026-03-26T06:26:46Z"
---

# Conformalized Transfer Learning for Li-ion Battery State of Health Forecasting under Manufacturing and Usage Variability

**Authors**: Samuel Filgueira da Silva, Mehmet Fatih Ozkan, Faissal El Idrissi, Marcello Canova
**Date**: 2026-03-25
**Paper ID**: [arxiv:2603.24475](https://arxiv.org/abs/2603.24475)

## Summary

This paper introduces an uncertainty-aware transfer learning framework for forecasting the State-of-Health (SOH) of lithium-ion batteries, addressing generalization issues caused by manufacturing and usage variability. The method combines an LSTM model trained on a synthetic dataset with domain adaptation via Maximum Mean Discrepancy (MMD) to align latent features between the source and target domains. Furthermore, Conformal Prediction (CP) is integrated to provide statistically valid, distribution-free prediction intervals, thereby quantifying the forecast uncertainty. The combined approach significantly enhances the trustworthiness and generalization capability of SOH predictions across heterogeneous cell populations.

## Key Contributions

- Proposal of an uncertainty-aware transfer learning framework for SOH forecasting that integrates LSTM, MMD-based domain adaptation, and Conformal Prediction.
- Demonstration of improved generalization and trustworthiness of SOH forecasts for heterogeneous cells by mitigating domain shift between simulated and target usage/manufacturing conditions.
- Utilizing a virtual battery dataset specifically designed to capture manufacturing and usage variability to robustly pre-train the base LSTM model.
- Provision of calibrated, distribution-free prediction intervals for SOH forecasts, enhancing the reliability and safety assessment of lithium-ion batteries.

## Limitations

The reliance on a high-fidelity virtual dataset for initial training might limit performance if the simulation does not perfectly capture all real-world variability sources. The computational overhead of MMD alignment and Conformal Prediction needs to be managed for real-time applications.

## Open Questions & Future Work

- [[experimental-validation-of-srh-forecasting]]
- [[hybrid-discrepancy-learning-for-physics-informed-sfr]]

## Key Concepts

- [Conformal Prediction](../concepts/conformal-prediction.md): A post-processing technique used to provide statistically valid prediction intervals for any point prediction model without strong parametric assumptions.
- [Maximum Mean Discrepancy](../concepts/maximum-mean-discrepancy.md): A non-parametric statistical test used to measure the distance between the distributions of two sets of samples in a feature space.

## Limitations

The reliance on a high-fidelity virtual dataset for initial training might limit performance if the simulation does not perfectly capture all real-world variability sources. The computational overhead of MMD alignment and Conformal Prediction needs to be managed for real-time applications.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.24475)
- [PDF](https://arxiv.org/pdf/2603.24475)


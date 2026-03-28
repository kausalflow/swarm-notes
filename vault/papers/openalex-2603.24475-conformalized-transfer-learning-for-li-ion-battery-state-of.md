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
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "transfer-learning"
  - "conformal-prediction"
  - "domain-adaptation"
  - "anomaly-detection"
  - "evaluation"
architectures:
  - "lstm"
datasets:
  []
concept_slugs:
  - "conformalized-transfer-learning-for-soh"
  - "mmd-for-domain-adaptation-in-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:29:31Z"
created_at: "2026-03-28T05:29:31Z"
---

# Conformalized Transfer Learning for Li-ion Battery State of Health Forecasting under Manufacturing and Usage Variability

**Authors**: Samuel Filgueira da Silva, Mehmet Fatih Ozkan, Faissal El Idrissi, Marcello Canova
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24475](https://arxiv.org/abs/2603.24475)

## Summary

This paper introduces a novel, uncertainty-aware transfer learning framework to improve the generalization and reliability of lithium-ion battery State-of-Health (SOH) forecasting when deployed on new cells exhibiting manufacturing or usage variations. The approach leverages an LSTM core, incorporating domain adaptation via Maximum Mean Discrepancy (MMD) to align feature distributions between simulated source data and real-world target cells. Crucially, the framework integrates Conformal Prediction (CP) to provide rigorous, distribution-free, calibrated prediction intervals, enhancing forecast trustworthiness. The methodology successfully addresses the domain shift issue common when models trained under controlled conditions meet real-world heterogeneity.

## Key Contributions

- Proposed an uncertainty-aware transfer learning framework combining LSTM, MMD-based domain adaptation, and Conformal Prediction for SOH forecasting.
- Developed a methodology to bridge the gap between SOH models trained on lab data and real-world heterogeneous cells arising from manufacturing and usage variability.
- Achieved improved generalization and calibrated trustworthiness of SOH forecasts across diverse lithium-ion cells using distribution-free prediction intervals from CP.

## Limitations

The framework is calibrated on a virtual battery dataset designed to capture variability, implying its performance is bounded by the fidelity of the simulation used for the source domain.

## Key Concepts

- [[conformalized-transfer-learning-for-soh]]: A transfer learning framework for SOH forecasting that integrates domain adaptation via MMD and uncertainty quantification via Conformal Prediction.
- [[mmd-for-domain-adaptation-in-forecasting]]: Using the Maximum Mean Discrepancy metric to minimize the distribution shift between feature representations of source and target domains in transfer learning.

## Archivist Review

Two key technical contributions were approved: the specific integration of Conformal Prediction (CP) and MMD within a transfer learning setup for SOH forecasting, and the standalone use of MMD for feature distribution alignment in domain adaptation. The combined concept was rejected as too specific to the SOH task, favoring the individual, reusable components. No datasets or open questions met the strict criteria for approval.

### Approved Concepts
- Conformalized Transfer Learning: It is the core methodological novelty, combining uncertainty quantification (CP) with domain adaptation (MMD) in a transfer learning setup for SOH forecasting.
- Maximum Mean Discrepancy (MMD) for Domain Adaptation: MMD is explicitly used as the mechanism to align feature distributions between the source (simulated) and target (new cells) domains, mitigating the primary challenge of generalization.

### Rejected Candidates
- [concept] Conformalized Transfer Learning (`conformalized-transfer-learning-for-soh`) - paper_local: The proposed concept is too specific to the SOH forecasting task; while the components are reusable, the combination in a named framework should be generalized or the components approved separately. Re-evaluating based on the component review below. Since the components MMD and CP are approved, this combined concept is overly specific.
- [concept] Maximum Mean Discrepancy (MMD) for Domain Adaptation (`mmd-for-domain-adaptation-in-forecasting`) - generic: MMD is a standard technique, but its specific application *for domain adaptation in time-series forecasting* makes it a strong, reusable mechanism worth noting in this context. (Self-correction: Approved as a concept below).

## Links

- [Abstract](https://arxiv.org/abs/2603.24475)
- [PDF](https://arxiv.org/pdf/2603.24475)


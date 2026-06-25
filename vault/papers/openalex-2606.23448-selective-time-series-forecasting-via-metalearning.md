---
# CSL-compatible fields
title: "Selective Time Series Forecasting via Metalearning"
author:
  - literal: "Ricardo Inácio"
  - literal: "Vitor Cerqueira"
  - literal: "Marília Barandas"
  - literal: "Carlos Soares"
issued:
  date-parts:
    - [2026, 6, 22]
url: "https://arxiv.org/abs/2606.23448"

# Custom fields
paper_id: "2606.23448"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "meta-learning"
  - "uncertainty"
architectures:
  []
datasets:
  []
concept_slugs:
  - "selective-forecasting-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:16:26Z"
created_at: "2026-06-25T08:16:26Z"
---

# Selective Time Series Forecasting via Metalearning

**Authors**: Ricardo Inácio, Vitor Cerqueira, Marília Barandas, Carlos Soares
**Date**: 2026-06-22
**Paper ID**: [openalex:2606.23448](https://arxiv.org/abs/2606.23448)

## Summary

This paper addresses the challenge of sample-specific prediction uncertainty in deep learning time-series forecasting by introducing a selective forecasting framework. Unlike existing methods that rely on domain-specific proxies like prediction interval width, the authors propose modeling the empirical percentile of forecast errors using structural features extracted via meta-learning. This decoupling of the rejection decision from the forecast enables robust abstention across heterogeneous time-series domains. Experimental results validate that this approach effectively identifies and rejects difficult-to-predict samples, leading to improved accuracy.

## Key Contributions

- Introduces a meta-learning based selective forecasting framework that models empirical error percentiles for domain-agnostic abstention.
- Demonstrates that grounding the rejection decision in structural features extracted from time-series lags enables effective transfer of abstention strategies across heterogeneous datasets.
- Shows that the proposed framework consistently improves overall forecasting accuracy across various coverage levels in both in-domain and transfer learning settings.

## Open Questions & Future Work

- [[calibrated-selective-forecasting]]

## Key Concepts

- [[selective-forecasting-framework]]: A meta-learning based approach that enables selective forecasting by predicting the empirical percentile of forecasting errors using structural time-series features.

## Archivist Review

The paper proposes a modular, meta-learning-based selective forecasting approach that decouples the rejection decision from the underlying base model, which is a highly reusable concept for time-series forecasting. The proposed open question regarding the calibration of selective forecasting addresses a fundamental bottleneck in making these risk-estimation techniques statistically rigorous for safety-critical applications. No datasets were approved as none were highlighted as specific, novel, or uniquely critical contributions compared to standard practice.

### Approved Concepts
- Selective Forecasting Framework: Provides a novel, domain-agnostic mechanism for abstaining from high-risk time series predictions by modeling error percentiles rather than relying on prediction interval widths.

### Approved Open Questions
- Calibrated Selective Forecasting: This is technically important because it bridges the gap between empirical risk-based rejection and rigorous statistical reliability, which is essential for deployment in safety-critical domains where point estimates and relative rankings are insufficient.

## Links

- [Abstract](https://arxiv.org/abs/2606.23448)
- [PDF](https://arxiv.org/pdf/2606.23448)


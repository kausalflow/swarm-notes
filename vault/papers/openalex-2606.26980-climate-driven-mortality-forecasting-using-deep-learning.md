---
# CSL-compatible fields
title: "Climate-Driven Mortality Forecasting Using Deep Learning"
author:
  - literal: "Kenrick So"
  - literal: "Karim Barigou"
  - literal: "Jens Robben"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.26980"

# Custom fields
paper_id: "2606.26980"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "cnn-lstm-time-series-hybrid"
architectures:
  []
datasets:
  []
concept_slugs:
  - "climate-driven-mortality-forecasting-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:15:58Z"
created_at: "2026-06-28T08:15:58Z"
---

# Climate-Driven Mortality Forecasting Using Deep Learning

**Authors**: Kenrick So, Karim Barigou, Jens Robben
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.26980](https://arxiv.org/abs/2606.26980)

## Summary

This paper introduces a two-step mortality forecasting framework that improves upon traditional models by capturing the impact of climate extremes on mortality spikes. The approach integrates a Lee-Carter baseline with either a CNN-LSTM or a GNN-LSTM architecture to account for region-specific temporal dynamics and spatial dependency propagation. Empirical evaluation on French regional data shows significant performance gains over both the Lee-Carter baseline and existing state-of-the-art models like MortFCNet, particularly at older ages. The inclusion of quantile LSTM extensions provides realistic, time-varying prediction intervals critical for assessing climate-related longevity exposure.

## Key Contributions

- Introduced a two-step mortality forecasting framework combining the Lee-Carter baseline with deep learning to capture both secular trends and climate-shock spikes.
- Developed CNN-LSTM and GNN-LSTM architectures to model region-specific temporal responses and spatial dependency propagation of climate impacts.
- Demonstrated an approximately 24% reduction in test MSE compared to the MortFCNet baseline on French regional mortality data (1990-2019).
- Enabled superior risk management through a quantile LSTM extension that provides time-varying prediction intervals for extreme mortality events.

## Open Questions & Future Work

- [[separating-transient-climate-shocks-from-structural-mortality-trends]]

## Key Concepts

- [[climate-driven-mortality-forecasting-framework]]: A hybrid two-step mortality forecasting approach that combines a traditional actuarial trend baseline with climate-aware deep learning architectures for excess mortality prediction.

## Archivist Review

I approved the overarching hybrid framework as it defines a novel approach for integrating classical actuarial baseline models with climate-conditioned neural residuals. The open question was approved for its relevance to longevity risk management and actuarial science. All other candidates were rejected as they were either local implementation details (CNN-LSTM, GNN-LSTM) or covered by more general existing concepts.

### Approved Concepts
- Climate-Driven Mortality Forecasting Framework: This framework provides a clear hybrid methodology for integrating actuarial baseline models with climate-conditioned deep learning to capture mortality residuals, a common challenge in insurance-linked forecasting.

### Approved Open Questions
- Separating Climate Shocks from Trends: The separation of structural from shock-driven trends is essential for both interpretability and the accuracy of long-term longevity-linked liability projections.

## Links

- [Abstract](https://arxiv.org/abs/2606.26980)
- [PDF](https://arxiv.org/pdf/2606.26980)


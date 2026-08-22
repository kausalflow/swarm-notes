---
# CSL-compatible fields
title: "RNN(p) for power consumption forecasting"
author:
  - literal: "Roberto Baviera"
  - literal: "Pietro Manzoni"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2209.01378"

# Custom fields
paper_id: "2209.01378"
paper_source: "openalex"
domain: "time-series"
tags:
  - "recurrent-neural-network"
  - "rnn"
  - "forecasting"
  - "time-series"
architectures:
  - "recurrent-neural-network"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-22T05:16:33Z"
created_at: "2026-08-22T05:16:33Z"
---

# RNN(p) for power consumption forecasting

**Authors**: Roberto Baviera, Pietro Manzoni
**Date**: 2026-08-20
**Paper ID**: [openalex:2209.01378](https://arxiv.org/abs/2209.01378)

## Summary

The paper introduces RNN(p), an elementary recurrent neural network operating on p time lags that generalizes the linear autoregressive ARX(p) model for time series with multi-scale seasonal patterns. The authors analyze the computational complexity of its learning algorithms and evaluate its performance on power consumption forecasting. Experimental results demonstrate that RNN(p) achieves high forecasting accuracy while retaining interpretability suitable for energy and financial decision-making.

## Key Contributions

- Introduces RNN(p), an elementary recurrent neural network operating on p time lags as a natural generalization of the ARX(p) model for time series with multi-scale seasonal patterns.
- Provides a rigorous analysis of computational complexity and training performance for various learning algorithms applied to RNN(p) models.
- Demonstrates the effectiveness of RNN(p) models in two power consumption forecasting applications, achieving excellent forecasting accuracy and high interpretability.

## Open Questions & Future Work

- [[rnn-numerical-stability-gradient-dynamics]]

## Archivist Review

Evaluated the paper on RNN(p) models for power consumption forecasting. No concepts met the high bar for permanent standalone vault notes as they relate to elementary recurrent generalizations and standard ARX models. The open question candidate was carefully reviewed and rejected due to its generic nature concerning gradient stability.

### Approved Open Questions
- RNN Numerical Stability and Gradient Dynamics: Critical for understanding how multi-lag recurrent neural network architectures handle gradient vanishing/exploding behaviors over extended sequences during training.

### Rejected Candidates
- [open_question] RNN Numerical Stability and Gradient Dynamics (`rnn-numerical-stability-gradient-dynamics`) - weak_evidence: Although presented as an open question candidate, it is standard generic future work on gradient dynamics and numerical stability rather than a distinct structural bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2209.01378)
- [PDF](https://arxiv.org/pdf/2209.01378)


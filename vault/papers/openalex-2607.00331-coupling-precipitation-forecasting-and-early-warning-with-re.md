---
# CSL-compatible fields
title: "Coupling Precipitation Forecasting and Early Warning with Reverse-Martingale Recurrent Neural Networks"
author:
  - literal: "Hui-Mean Foo"
  - literal: "Yuan‐chin Ivan Chang"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00331"

# Custom fields
paper_id: "2607.00331"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "recurrent-neural-network"
  - "rnn"
architectures:
  []
datasets:
  []
concept_slugs:
  - "reverse-martingale-regularized-recurrent-network"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:36:14Z"
created_at: "2026-07-04T07:36:14Z"
---

# Coupling Precipitation Forecasting and Early Warning with Reverse-Martingale Recurrent Neural Networks

**Authors**: Hui-Mean Foo, Yuan‐chin Ivan Chang
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00331](https://arxiv.org/abs/2607.00331)

## Summary

This paper presents a novel recurrent neural network architecture for precipitation forecasting that simultaneously serves as an early-warning system for drought. By incorporating a reverse-martingale penalty that forces backward-in-time hidden state coherence, the model produces a reconstruction error signal capable of detecting abnormal regime shifts. Evaluations across four distinct climatic regions demonstrate that the model maintains forecasting skill comparable to standard RNNs while providing earlier warnings than the conventional SPI-3 index.

## Key Contributions

- Introduces the reverse-martingale regularization penalty, which enables recurrent neural networks to generate an online drought early-warning signal from the reconstruction defect without degrading forecast performance.
- Demonstrates that the proposed model provides lead-time advantages over the standard SPI-3 index across diverse hydroclimatic regimes in Taiwan, Texas, Germany, and Turkey.
- Provides a conservative, dual-purpose design that maintains baseline forecasting skill while adding structural stability and actionable diagnostic signaling to the hidden state.

## Open Questions & Future Work

- [[hydroclimatic-drought-warning-lead-predictability]]

## Key Concepts

- [[reverse-martingale-regularized-recurrent-network]]: A recurrent neural network architecture augmented with a backward-coherence penalty that uses the resulting reconstruction defect as an online regime-change warning signal.

## Archivist Review

The proposed concept of using reverse-martingale regularization to generate an interpretable anomaly warning signal from a recurrent network's hidden state is highly novel and reusable. I have approved the concept and the related open question regarding the hydroclimatic predictability of the warning lead time, as it addresses a fundamental limitation in the paper's experimental findings. No datasets were approved as the paper utilizes standard regional station records rather than a named, standalone benchmark dataset.

### Approved Concepts
- Reverse-Martingale Regularized Recurrent Network: This architecture provides a dual-purpose framework for simultaneous point forecasting and diagnostic anomaly detection without compromising predictive accuracy.

### Approved Open Questions
- Predicting Drought-Warning Lead Across Climates: This is critical for operationalizing drought monitoring and understanding the limits of neural-network-derived warning signals in diverse global environments.

## Links

- [Abstract](https://arxiv.org/abs/2607.00331)
- [PDF](https://arxiv.org/pdf/2607.00331)


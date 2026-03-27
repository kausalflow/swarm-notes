---
# CSL-compatible fields
title: "Hybrid Quantum Neural Network for Multivariate Clinical Time Series Forecasting"
author:
  - literal: "Irene Iele"
  - literal: "Floriano Caprio"
  - literal: "P. Soda"
  - literal: "Matteo Tortora"
issued:
  date-parts:
    - [2026, 3, 9]
url: "https://arxiv.org/abs/2603.08072"

# Custom fields
paper_id: "2603.08072"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "rnn"
  - "gru"
  - "hybrid-quantum-neural-network"
  - "evaluation"
architectures:
  - "rnn"
datasets:
  - "BIDMC PPG and Respiration dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:08:41Z"
created_at: "2026-03-27T14:08:41Z"
---

# Hybrid Quantum Neural Network for Multivariate Clinical Time Series Forecasting

**Authors**: Irene Iele, Floriano Caprio, P. Soda, Matteo Tortora
**Date**: 2026-03-09
**Paper ID**: [openalex:2603.08072](https://arxiv.org/abs/2603.08072)

## Summary

This paper introduces a hybrid quantum-classical architecture for multivariate, multi-horizon forecasting of physiological time series, including heart rate and respiratory rate, up to 60 seconds ahead. The model embeds a Variational Quantum Circuit (VQC) within a Gated Recurrent Unit (GRU) encoder, where the historical window is first summarized, and then quantum angles derived from this latent space parameterize the VQC. The quantum layer functions as a crucial non-linear feature mixer to model cross-variable dependencies before the final prediction layer. Evaluations on the BIDMC PPG and Respiration dataset show competitive accuracy and enhanced robustness against noise compared to established deep learning baselines, suggesting utility in small-cohort clinical forecasting.

## Key Contributions

- Proposed a novel hybrid quantum-classical architecture integrating a Variational Quantum Circuit (VQC) into a GRU encoder for multivariate multi-horizon physiological time series forecasting.
- Achieved competitive forecasting accuracy against classical and deep learning baselines for heart rate, oxygen saturation, pulse rate, and respiratory rate at 15s, 30s, and 60s horizons.
- Demonstrated superior robustness to input noise and missing data compared to conventional deep learning models.
- Validated the approach using a Leave-One-Patient-Out cross-validation protocol on clinical time series data.

## Limitations

The generalizability and scalability of the quantum component across larger and more diverse clinical datasets remain to be fully explored.

## Open Questions & Future Work

- [[evaluate-hybrid-model-on-larger-datasets]]
- [[assess-nisq-hardware-robustness]]

## Key Concepts

- [Hybrid Quantum Neural Network](../concepts/hybrid-quantum-neural-network.md): A neural network architecture that integrates a Variational Quantum Circuit (VQC) within a classical recurrent neural network backbone for time series forecasting.

## Datasets

- [BIDMC PPG and Respiration dataset](../datasets/bidmc-ppg-and-respiration-dataset.md)

## Limitations

The generalizability and scalability of the quantum component across larger and more diverse clinical datasets remain to be fully explored.

## Links

- [Abstract](https://arxiv.org/abs/2603.08072)
- [PDF](https://arxiv.org/pdf/2603.08072)


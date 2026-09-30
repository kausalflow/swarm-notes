---
# CSL-compatible fields
title: "SpikeLite: Lightweight Spiking Neural Networks for Time-Series Forecasting"
author:
  - literal: "Bang Hu"
  - literal: "Changze Lv"
  - literal: "Mingjie Li"
  - literal: "Xiaoqing Zheng"
  - literal: "Wei Cao"
  - literal: "Fan Zhang"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.35097"

# Custom fields
paper_id: "2609.35097"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:48:18Z"
created_at: "2026-09-30T10:48:18Z"
---

# SpikeLite: Lightweight Spiking Neural Networks for Time-Series Forecasting

**Authors**: Bang Hu, Changze Lv, Mingjie Li, Xiaoqing Zheng, Wei Cao, Fan Zhang
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.35097](https://arxiv.org/abs/2609.35097)

## Summary

SpikeLite is a lightweight spiking neural network framework designed for energy-efficient time-series forecasting without sacrificing predictive accuracy. It comprises a Frequency-Selective Spiking Encoder (FSSE) that utilizes LIF dynamics for frequency-sensitive temporal encoding and a Sparse Spiking Channel Attention (SSCA) module that learns binary masks for selective cross-channel interactions. Extensive evaluations across twelve standard benchmarks demonstrate superior predictive performance and the lowest reported energy consumption compared to existing spiking forecasters.

## Key Contributions

- Introduces SpikeLite, a lightweight spiking neural network framework for time-series forecasting that balances accuracy and energy efficiency.
- Proposes the Frequency-Selective Spiking Encoder (FSSE), leveraging leaky integrate-and-fire (LIF) dynamics for frequency-sensitive temporal decomposition.
- Proposes the Sparse Spiking Channel Attention (SSCA) module, employing binary masks for selective and efficient cross-channel interactions.
- Achieves top aggregate performance across four multivariate and eight long-term forecasting benchmarks under SeqSNN and SpikF protocols, alongside superior energy efficiency on the ECL dataset.

## Archivist Review

The proposed concept candidates and open questions were evaluated against vault standards. The sole open question mentions routine future work items (irregular time series, missing data, online prediction, cross-dataset transfer) commonly listed in forecasting papers, lacking the specific depth required for a standalone vaulted research question note. No distinct permanent concepts warranted vaulting.

### Rejected Candidates
- [open_question] Irregular and Missing-Data SNN Forecasting (`irregular-missing-data-time-series-snn-forecasting`) - weak_evidence: Standard future work mentioning multiple routine extensions (irregular time series, missing data, online prediction, cross-dataset transfer) without a deep, standalone unresolved theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.35097)
- [PDF](https://arxiv.org/pdf/2609.35097)


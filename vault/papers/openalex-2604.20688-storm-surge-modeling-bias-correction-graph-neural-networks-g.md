---
# CSL-compatible fields
title: "Storm Surge Modeling, Bias Correction, Graph Neural Networks, Graph Convolution Networks"
author:
  - literal: "Noujoud Nader"
  - literal: "Stefanos Giaremis"
  - literal: "Clint Dawson"
  - literal: "Carola Kaiser"
  - literal: "Karame Mohammadiporshokooh"
  - literal: "Hartmut Kaiser"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20688"

# Custom fields
paper_id: "2604.20688"
paper_source: "openalex"
domain: "time-series"
tags:
  - "graph-neural-network"
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "lstm"
architectures:
  - "graph-neural-network"
datasets:
  []
concept_slugs:
  - "stormnet"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-25T06:16:06Z"
created_at: "2026-04-25T06:16:06Z"
---

# Storm Surge Modeling, Bias Correction, Graph Neural Networks, Graph Convolution Networks

**Authors**: Noujoud Nader, Stefanos Giaremis, Clint Dawson, Carola Kaiser, Karame Mohammadiporshokooh, Hartmut Kaiser
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20688](https://arxiv.org/abs/2604.20688)

## Summary

This paper presents StormNet, a novel spatio-temporal graph neural network designed to correct biases in numerical storm surge forecasts by leveraging spatial dependencies between water-level gauge stations. By integrating GCN and GAT mechanisms with LSTM components, the model effectively captures the complex dynamics of tropical cyclone-induced surges. Evaluated on Hurricane Idalia (2023), StormNet significantly reduces prediction errors and surpasses traditional LSTM baselines, offering a scalable solution for real-time coastal flood forecasting.

## Key Contributions

- Introduces StormNet, a spatio-temporal GNN combining GCN, GAT, and LSTM for storm surge forecast bias correction.
- Reduces RMSE in water-level predictions by >70% for 48-hour and >50% for 72-hour forecasts compared to numerical model outputs.
- Outperforms sequential LSTM baselines, particularly for extended prediction horizons, while maintaining low training time for operational efficiency.

## Open Questions & Future Work

- [[bias-correction-ungauged-locations]]

## Key Concepts

- [[stormnet]]: A spatio-temporal graph neural network architecture integrating GCN, GAT, and LSTM components for bias correction in sensor-based forecasting.

## Archivist Review

I approved the StormNet architecture as a representative GNN-based framework for sensor network bias correction and identified the bias correction for ungauged locations as a significant unresolved challenge in this domain. Other candidates were rejected as they were either generic machine learning terms or paper-local implementation details.

### Approved Concepts
- StormNet: It is the core proposed framework for spatio-temporal bias correction of storm surges using GNNs, specifically combining GCN, GAT, and LSTM.

### Approved Open Questions
- Bias correction at ungauged locations: Extending bias correction to ungauged locations is essential for comprehensive coastal flood risk management, as gauge networks are spatially sparse.

## Links

- [Abstract](https://arxiv.org/abs/2604.20688)
- [PDF](https://arxiv.org/pdf/2604.20688)


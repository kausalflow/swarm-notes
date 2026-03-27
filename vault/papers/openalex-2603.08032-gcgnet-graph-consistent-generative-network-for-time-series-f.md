---
# CSL-compatible fields
title: "GCGNet: Graph-Consistent Generative Network for Time Series Forecasting with Exogenous Variables"
author:
  - literal: "Zhengyu Li"
  - literal: "Xiangfei Qiu"
  - literal: "Yuhan Zhu"
  - literal: "Xingjian Wu"
  - literal: "Jilin Hu"
  - literal: "Chenjuan Guo"
  - literal: "Bin Yang"
issued:
  date-parts:
    - [2026, 3, 9]
url: "https://arxiv.org/abs/2603.08032"

# Custom fields
paper_id: "2603.08032"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "time-series"
  - "graph-learning"
  - "variational-autoencoder"
architectures:
  []
datasets:
  - "12 real-world datasets"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:08:47Z"
created_at: "2026-03-27T14:08:47Z"
---

# GCGNet: Graph-Consistent Generative Network for Time Series Forecasting with Exogenous Variables

**Authors**: Zhengyu Li, Xiangfei Qiu, Yuhan Zhu, Xingjian Wu, Jilin Hu, Chenjuan Guo, Bin Yang
**Date**: 2026-03-09
**Paper ID**: [openalex:2603.08032](https://arxiv.org/abs/2603.08032)

## Summary

GCGNet is proposed for time series forecasting with exogenous variables, aiming to capture joint temporal and channel correlations more effectively than methods that model them sequentially. It utilizes a Variational Generator to create initial coarse forecasts, which are then guided by a Graph Structure Aligner that checks consistency against robust graph representations of the true data correlations. A final Graph Refiner module is employed to refine these predictions, prevent output degeneration, and boost overall accuracy. Extensive experiments across 12 real-world datasets confirm that GCGNet surpasses existing state-of-the-art forecasting baselines.

## Key Contributions

- Proposing GCGNet, a novel architecture that models joint temporal and channel correlations simultaneously using a graph-based consistency alignment mechanism, overcoming the limitations of traditional two-step methods.
- Introducing a Graph Structure Aligner that enforces consistency between the generated coarse predictions and robust graph representations of true correlations derived from the data.
- Designing a Graph Refiner module within the network framework to stabilize the generative process and prevent prediction degeneration, leading to improved final accuracy.
- Demonstrating state-of-the-art performance across 12 diverse real-world time series forecasting tasks that incorporate exogenous variables.

## Limitations

The paper focuses on leveraging available future exogenous variables; performance when future exogenous variables are unknown or require complex forecasting themselves might be impacted. The specifics of the graph representation's noise robustness mechanism beyond just "being robust to noises" need further detail.

## Open Questions & Future Work

- [[vae-degeneration-prevention-in-graph-alignment]]

## Key Concepts

- [Graph-Consistent Generative Network](../concepts/graph-consistent-generative-network.md): A network architecture that explicitly models and enforces consistency between learned temporal/channel correlations (represented as graphs) and the generated forecasts to improve robustness and accuracy in time series forecasting with exogenous variables.

## Datasets

- [12 real-world datasets](../datasets/12-real-world-datasets.md)

## Limitations

The paper focuses on leveraging available future exogenous variables; performance when future exogenous variables are unknown or require complex forecasting themselves might be impacted. The specifics of the graph representation's noise robustness mechanism beyond just "being robust to noises" need further detail.

## Links

- [Abstract](https://arxiv.org/abs/2603.08032)
- [PDF](https://arxiv.org/pdf/2603.08032)


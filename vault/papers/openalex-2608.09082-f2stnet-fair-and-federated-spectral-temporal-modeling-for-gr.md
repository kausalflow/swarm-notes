---
# CSL-compatible fields
title: "F2STNet: Fair and Federated Spectral-Temporal Modeling for Graph Forecasting"
author:
  - literal: "Jiayi Zhang"
  - literal: "Jinfeng Xu"
  - literal: "Hewei Wang"
  - literal: "Siyuan Cen"
  - literal: "Haidong Huang"
  - literal: "Yiyao Zhan"
  - literal: "Zheyu Chen"
  - literal: "Jinjiang You"
  - literal: "Ai Jian"
  - literal: "Edith C. H. Ngai"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09082"

# Custom fields
paper_id: "2608.09082"
paper_source: "openalex"
domain: "time-series"
tags:
  - "graph-neural-network"
  - "state-space-model"
  - "ssm"
  - "federated-learning"
  - "forecasting"
  - "time-series"
architectures:
  - "state-space-model"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:09:09Z"
created_at: "2026-08-13T06:09:09Z"
---

# F2STNet: Fair and Federated Spectral-Temporal Modeling for Graph Forecasting

**Authors**: Jiayi Zhang, Jinfeng Xu, Hewei Wang, Siyuan Cen, Haidong Huang, Yiyao Zhan, Zheyu Chen, Jinjiang You, Ai Jian, Edith C. H. Ngai
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09082](https://arxiv.org/abs/2608.09082)

## Summary

F2STNet is a federated spatiotemporal graph forecasting framework designed to handle decentralized and heterogeneous data. It combines truncated graph-Fourier features, a lightweight diagonal state-space temporal encoder, graph convolutions, and a Fairness-aware Federated Aggregation (FFA) mechanism. Experiments across PeMS04, HZMetro, and KnowAir benchmarks show strong forecasting accuracy, while federated evaluations on PeMS04 improve worst-client and client-dispersion metrics.

## Key Contributions

- F2STNet combines truncated graph-Fourier features, a lightweight diagonal state-space temporal encoder, graph convolution, and Fairness-aware Federated Aggregation (FFA) for federated spatiotemporal graph forecasting.
- The spectral branch exposes graph-frequency structure while the state-space layer models long temporal dependencies with linear complexity.
- Fairness-aware Federated Aggregation (FFA) adjusts the FedAvg prior using client validation losses and an increasing fairness schedule to improve client dispersion and worst-client performance.
- Experiments on PeMS04, HZMetro, and KnowAir demonstrate favorable forecasting accuracy, with federated evaluations on PeMS04 improving worst-client and client-dispersion metrics.

## Open Questions & Future Work

- [[robust-history-aware-federated-weighting]]

## Archivist Review

The paper presents F2STNet, combining graph Fourier features, diagonal SSMs, and a fairness-aware federated aggregation mechanism. No standalone concepts qualify as sufficiently novel or distinct vault entries, as they combine standard components (SSMs, GNNs, FedAvg extensions). However, the open question concerning robust history-aware federated weighting in heterogeneous spatiotemporal forecasting is approved as a valuable long-term research direction.

### Approved Open Questions
- Robust History-Aware Federated Weighting: Addressing sensitivity to noise and outliers in federated fairness-aware aggregation is critical for robust deployment in real-world decentralized sensor networks.

## Links

- [Abstract](https://arxiv.org/abs/2608.09082)
- [PDF](https://arxiv.org/pdf/2608.09082)


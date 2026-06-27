---
# CSL-compatible fields
title: "Sequential and Generative Models for Vehicular Distributed MIMO Channel Prediction"
author:
  - literal: "Malek Abida"
  - literal: "Rafik Zayani"
  - literal: "Eric Simon"
  - literal: "Davy Gaillot"
issued:
  date-parts:
    - [2026, 6, 24]
url: "https://arxiv.org/abs/2606.25864"

# Custom fields
paper_id: "2606.25864"
paper_source: "openalex"
domain: "nlp"
tags:
  - "language-model"
  - "gpt"
  - "long-context"
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  - "mamimosa"
concept_slugs:
  - "channelgpt"
dataset_slugs:
  - "mamimosa"
skill: "TimeSeriesSkill"
processed_at: "2026-06-27T07:43:50Z"
created_at: "2026-06-27T07:43:50Z"
---

# Sequential and Generative Models for Vehicular Distributed MIMO Channel Prediction

**Authors**: Malek Abida, Rafik Zayani, Eric Simon, Davy Gaillot
**Date**: 2026-06-24
**Paper ID**: [openalex:2606.25864](https://arxiv.org/abs/2606.25864)

## Summary

This paper presents a novel vehicular channel prediction framework that addresses the high-capacity, low-latency requirements of 6G systems under fast-fading conditions. The researchers introduce ChannelGPT, a generative model capable of predicting time-varying channel state information while maintaining essential spatiotemporal dynamics and non-stationarity. Evaluated on the MaMIMOSA measurement dataset, the model significantly outperforms standard architectures like LSTM and CNN-Transformer in both accuracy and computational efficiency, ultimately enabling high-fidelity system-level performance assessment for distributed MIMO communications.

## Key Contributions

- Introduces an end-to-end framework for training and benchmarking sequential and generative models for vehicular channel state information (CSI) prediction.
- Develops ChannelGPT, which reduces NMSE by over 94% compared to LSTM and decreases inference latency by 39% relative to CNN-Transformer baselines.
- Demonstrates that ChannelGPT-predicted channels allow spectral efficiency (SE) distributions in vehicular distributed MIMO systems that are nearly indistinguishable from real-world measurements.

## Open Questions & Future Work

- [[vehicular-channel-model-generalization]]

## Key Concepts

- [[channelgpt]]: A generative model designed for vehicular channel state information prediction that balances accuracy, computational efficiency, and spatiotemporal dynamic preservation.

## Archivist Review

I have approved ChannelGPT as a concept representing a specialized generative architecture for channel state information (CSI) prediction, as this represents a clear application of generative modeling to a physical, time-varying domain. I approved the MaMIMOSA dataset as it is the central evaluation corpus for this new approach. Finally, I approved the open question regarding cross-environment generalization, as it addresses a fundamental bottleneck in the field of data-driven wireless channel modeling that goes beyond standard model performance improvement.

### Approved Concepts
- ChannelGPT: The paper proposes ChannelGPT as a specialized generative model for vehicular MIMO channel prediction, which significantly outperforms classical deep learning baselines in both accuracy and computational efficiency.

### Approved Open Questions
- Cross-Environment Channel Generalization: Generalization is a critical bottleneck for data-driven channel models. Without evaluating on broader datasets, it is difficult to determine if high performance in a single campaign translates to the high-reliability requirements of global 6G vehicular connectivity.

## Datasets

- [[mamimosa]]

## Links

- [Abstract](https://arxiv.org/abs/2606.25864)
- [PDF](https://arxiv.org/pdf/2606.25864)


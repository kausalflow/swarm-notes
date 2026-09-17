---
# CSL-compatible fields
title: "AsyncCouple-Flow: Asynchronous Cross-Modal Coupling and Flow Matching for Spatio-Temporal Forecasting"
author:
  - literal: "Zhixiang Wu"
  - literal: "Yining Liu"
  - literal: "Bo Zhao"
  - literal: "Szu-Yu Chen"
  - literal: "Hao-yu Duan"
  - literal: "Chu Lin"
  - literal: "Chuanguang Yang"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.16573"

# Custom fields
paper_id: "2609.16573"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "spatio-temporal"
  - "flow-matching"
  - "graph-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "asynccouple-flow"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:44:44Z"
created_at: "2026-09-17T09:44:44Z"
---

# AsyncCouple-Flow: Asynchronous Cross-Modal Coupling and Flow Matching for Spatio-Temporal Forecasting

**Authors**: Zhixiang Wu, Yining Liu, Bo Zhao, Szu-Yu Chen, Hao-yu Duan, Chu Lin, Chuanguang Yang
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.16573](https://arxiv.org/abs/2609.16573)

## Summary

The authors propose AsyncCouple-Flow, a novel framework for multi-modal spatio-temporal forecasting that addresses asynchronous sampling rates, missing modalities, and autoregressive drift. The method combines Modality-Aware Token Sparsification (MATS), an Asynchronous Cross-Modal Coupling Graph (ACCG) encoding time offsets and physical priors, and a Flow-Matching Forecasting Head formulated as a conditional ODE. Extensive experiments on weather forecasting and traffic prediction demonstrate superior robustness and accuracy over state-of-the-art baselines under missing data conditions.

## Key Contributions

- Introduces AsyncCouple-Flow, a novel framework for multi-modal spatio-temporal forecasting (MM-STF) handling asynchronous sampling rates and missing modalities.
- Proposes Modality-Aware Token Sparsification (MATS) for scale-aware tokenization and top-k selection across heterogeneous sequences.
- Develops an Asynchronous Cross-Modal Coupling Graph (ACCG) and a Flow-Matching Forecasting Head to mitigate autoregressive error accumulation and handle sensor outages.
- Demonstrates superior performance on ERA5+GOES+ISD weather forecasting and PEMS-BAY traffic prediction compared to state-of-the-art baselines.

## Limitations

The method requires careful tuning of modality dropout rates and importance scoring thresholds to handle severe missingness.

## Key Concepts

- [[asynccouple-flow]]: An asynchronous cross-modal coupling and flow matching framework for robust multi-modal spatio-temporal forecasting.

## Archivist Review

Approved the overarching framework AsyncCouple-Flow while rejecting paper-local subcomponents such as MATS and ACCG per our subcomponent policy. No datasets or open questions met the strict standalone criteria.

### Approved Concepts
- AsyncCouple-Flow: It is the core framework introduced for multi-modal spatio-temporal forecasting under asynchrony and missingness.

### Rejected Candidates
- [concept] Modality-Aware Token Sparsification (`modality-aware-token-sparsification`) - subcomponent_of_broader_mechanism: Subcomponent of the broader AsyncCouple-Flow framework.
- [concept] Asynchronous Cross-Modal Coupling Graph (`asynchronous-cross-modal-coupling-graph`) - subcomponent_of_broader_mechanism: Subcomponent of the broader AsyncCouple-Flow framework.

## Links

- [Abstract](https://arxiv.org/abs/2609.16573)
- [PDF](https://arxiv.org/pdf/2609.16573)


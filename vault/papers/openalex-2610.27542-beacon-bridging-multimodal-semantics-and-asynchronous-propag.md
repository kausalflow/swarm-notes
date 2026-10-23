---
# CSL-compatible fields
title: "BEACON: Bridging Multimodal Semantics and Asynchronous Propagation for Cloud System Anomaly Detection"
author:
  - literal: "Zhe Li"
  - literal: "Tengxue Zhang"
  - literal: "Yang Shu"
  - literal: "Tung Kieu"
  - literal: "Lunting Fan"
  - literal: "Y. Zhang"
  - literal: "Bin Yang"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.27542"

# Custom fields
paper_id: "2610.27542"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "multimodal"
  - "time-series"
  - "graph-neural-network"
  - "attention-mechanism"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:40:55Z"
created_at: "2026-10-23T09:40:55Z"
---

# BEACON: Bridging Multimodal Semantics and Asynchronous Propagation for Cloud System Anomaly Detection

**Authors**: Zhe Li, Tengxue Zhang, Yang Shu, Tung Kieu, Lunting Fan, Y. Zhang, Bin Yang
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.27542](https://arxiv.org/abs/2610.27542)

## Summary

Modern cloud systems generate massive multimodal observability data (metrics, logs, and dependency graphs) requiring robust anomaly detection. Existing methods often fail to bridge the semantic gaps between modalities and overlook asynchronous spatio-temporal dependencies across system instances. To address this, the authors propose BEACON, which integrates a Dynamic Interpretable Multimodal Aggregator (DIMA) for cross-modal prototype alignment and an Asynchronous Spatio-Temporal Propagator (ASTP) for topology-aware multi-scale temporal propagation. Extensive experiments on three real-world cloud datasets confirm BEACON's superior performance over state-of-the-art baselines.

## Key Contributions

- Proposes BEACON, a novel framework bridging multimodal semantics and asynchronous propagation for cloud system anomaly detection.
- Introduces the Dynamic Interpretable Multimodal Aggregator (DIMA) utilizing an information-bottleneck mechanism to align metrics and logs in a shared prototype space.
- Develops the Asynchronous Spatio-Temporal Propagator (ASTP) combining multi-scale temporal attention and topology-aware aggregation to capture asynchronous dependencies across system instances.
- Demonstrates consistent outperformance over state-of-the-art baselines across three real-world cloud system datasets.

## Archivist Review

The proposed concepts (DIMA and ASTP) are paper-local architectural modules designed specifically for cloud anomaly detection, making them subcomponents rather than broadly recurring methodological primitives. Similarly, the open question focuses tightly on cloud anomaly detection rather than a generalizable foundational limitation in time-series analysis or forecasting. Following strict scarcity and reusability standards, all candidates are rejected.

### Rejected Candidates
- [concept] Dynamic Interpretable Multimodal Aggregator (`dynamic-interpretable-multimodal-aggregator`) - subcomponent_of_broader_mechanism: This is a specific subcomponent/module of the BEACON framework tailored for cloud logs and metrics, lacking general reusability across diverse time-series forecasting or general ML tasks.
- [concept] Asynchronous Spatio-Temporal Propagator (`asynchronous-spatio-temporal-propagator`) - subcomponent_of_broader_mechanism: This is a paper-internal module for cloud anomaly propagation, representing a specialized subcomponent rather than a broadly recurring standalone architectural paradigm.
- [open_question] Multimodal Asynchronous Cloud Anomaly Detection (`multimodal-asynchronous-cloud-anomaly-detection`) - low_impact: This open question is excessively domain-specific to cloud systems and serverless monitoring, offering limited generalizability across broader time-series or machine learning literature.

## Links

- [Abstract](https://arxiv.org/abs/2610.27542)
- [PDF](https://arxiv.org/pdf/2610.27542)


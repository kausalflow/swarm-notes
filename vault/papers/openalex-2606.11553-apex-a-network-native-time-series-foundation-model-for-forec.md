---
# CSL-compatible fields
title: "APEX: A Network-Native Time-Series Foundation Model for Forecasting and Anomaly Detection for Wireless Edge Operations"
author:
  - literal: "Swadhin Pradhan"
  - literal: "Niloo Bahadori"
  - literal: "Peiman Amini"
issued:
  date-parts:
    - [2026, 6, 10]
url: "https://arxiv.org/abs/2606.11553"

# Custom fields
paper_id: "2606.11553"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "model-compression"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "network-native-pre-training"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-13T08:15:43Z"
created_at: "2026-06-13T08:15:43Z"
---

# APEX: A Network-Native Time-Series Foundation Model for Forecasting and Anomaly Detection for Wireless Edge Operations

**Authors**: Swadhin Pradhan, Niloo Bahadori, Peiman Amini
**Date**: 2026-06-10
**Paper ID**: [openalex:2606.11553](https://arxiv.org/abs/2606.11553)

## Summary

APEX is a network-native, decoder-only transformer foundation model designed to address the poor performance of generic models on bursty, zero-inflated wireless telemetry. Pre-trained on 100K multivariate time series from 4,500 production wireless networks, the model is provided in two scales: APEX-Large for cloud forecasting and APEX-Edge for on-device inference. Evaluation on a 192-step DHCP degradation benchmark demonstrates that APEX significantly outperforms both statistical baselines and existing foundation models while maintaining high anomaly detection accuracy.

## Key Contributions

- Introduces APEX, a network-native transformer model architecture designed for multivariate wireless telemetry.
- Achieves a 38% reduction in MAE over SARIMA and 18% over the Toto baseline on a 192-step DHCP degradation forecasting benchmark.
- Demonstrates effective dual-scale deployment with APEX-Large for cloud-based tasks and APEX-Edge for sub-second, privacy-preserving inference on resource-constrained hardware.

## Open Questions & Future Work

- [[cross-domain-telemetry-generalization]]

## Key Concepts

- [[network-native-pre-training]]: A domain-specific pre-training strategy tailored to the unique statistical properties of bursty, zero-inflated wireless network telemetry.

## Archivist Review

I approved the concept of network-native pre-training because it represents a distinct approach to domain-specific foundation modeling that is likely to recur in industrial settings. I also approved the open question regarding cross-domain telemetry generalization as it highlights a fundamental limitation in current network-focused forecasting research. Other candidates were not deemed sufficiently distinct or were already covered by broader concepts in the vault.

### Approved Concepts
- Network-Native Pre-training: Distinguishes the model from generic time-series foundation models by training specifically on domain-coupled, bursty wireless telemetry.

### Approved Open Questions
- Generalizing across heterogeneous telemetry: The current research is siloed within a single network protocol. Proving that the model's architectural principles generalize across different protocol layers is essential for establishing it as a true general-purpose foundation model for network operations.

## Links

- [Abstract](https://arxiv.org/abs/2606.11553)
- [PDF](https://arxiv.org/pdf/2606.11553)


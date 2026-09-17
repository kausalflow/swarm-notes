---
# CSL-compatible fields
title: "Robust Fault Detection in Mechanical Multimodal Time Series via Self-Supervised Cross-Modal Reconstruction"
author:
  - literal: "Magnus Munk Jensen"
  - literal: "Dorte Hammershøi"
  - literal: "Rafał Wiśniewski"
  - literal: "Olga Fink"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.16314"

# Custom fields
paper_id: "2609.16314"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "multimodal"
  - "time-series"
  - "self-supervised-learning"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:43:37Z"
created_at: "2026-09-17T09:43:37Z"
---

# Robust Fault Detection in Mechanical Multimodal Time Series via Self-Supervised Cross-Modal Reconstruction

**Authors**: Magnus Munk Jensen, Dorte Hammershøi, Rafał Wiśniewski, Olga Fink
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.16314](https://arxiv.org/abs/2609.16314)

## Summary

This paper introduces a self-supervised multimodal anomaly detection framework for industrial systems that leverages cross-modal reconstruction of heterogeneous time-series sensor data. By reconstructing each modality from the others, the model exploits complementary information across sensing channels without requiring explicit temporal alignment or identical sampling rates. To handle distribution shifts in real-world deployments, anomalies are identified using reconstruction error coupled with an adaptive test-time thresholding mechanism. Experiments across three industrial case studies demonstrate superior fault detection performance and heightened robustness under out-of-distribution conditions.

## Key Contributions

- Proposes a self-supervised multimodal anomaly detection framework based on cross-modal reconstruction of heterogeneous time-series sensor data to capture underlying physical process dynamics.
- Integrates cross-modal information without requiring explicit temporal alignment or identical sampling rates, improving robustness to sensor noise and missing measurements.
- Introduces an adaptive test-time thresholding mechanism based on cross-modal reconstruction error to maintain fault detection performance under out-of-distribution conditions and distribution shifts.

## Archivist Review

Evaluated the single candidate open question against the vault criteria. The open question was rejected because it proposes routine future work (extending discrete models to continuous parameters) rather than a foundational unresolved mechanism or theoretical bottleneck. No concepts or datasets were proposed or approved.

### Rejected Candidates
- [open_question] Adaptation to Continuously Varying Parameters (`continuous-operational-parameter-adaptation`) - low_impact: Routine future work direction proposing extension to continuous parameters rather than addressing an intrinsic technical bottleneck or unresolved paradox.

## Links

- [Abstract](https://arxiv.org/abs/2609.16314)
- [PDF](https://arxiv.org/pdf/2609.16314)


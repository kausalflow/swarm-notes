---
# CSL-compatible fields
title: "T-SAR-JEPA: Self-Supervised Temporal Anomaly Detection in SAR Amplitude Stacks via Latent Prediction"
author:
  - literal: "Kerod Woldesenbet"
  - literal: "Abem Woldesenbet"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.05700"

# Custom fields
paper_id: "2606.05700"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "self-supervised-learning"
  - "anomaly-detection"
  - "transformer"
  - "vision-transformer"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  - "dfc-2026-dataset"
concept_slugs:
  - "t-sar-jepa"
dataset_slugs:
  - "dfc-2026-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:19:39Z"
created_at: "2026-06-07T08:19:39Z"
---

# T-SAR-JEPA: Self-Supervised Temporal Anomaly Detection in SAR Amplitude Stacks via Latent Prediction

**Authors**: Kerod Woldesenbet, Abem Woldesenbet
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.05700](https://arxiv.org/abs/2606.05700)

## Summary

T-SAR-JEPA is a self-supervised framework for detecting temporal anomalies in Synthetic Aperture Radar (SAR) amplitude stacks by forecasting future latent states. The model utilizes a domain-adapted ViT-Base encoder and a temporal transformer that processes K=7 acquisitions to identify deviations from expected temporal patterns. It significantly outperforms traditional baselines such as RX, PaDiM, and LSTM on the DFC 2026 dataset, demonstrating high spatial coherence and predictive accuracy for real-world environmental monitoring tasks like eruption detection.

## Key Contributions

- Introduces T-SAR-JEPA, a self-supervised framework for temporal anomaly detection in SAR amplitude stacks using latent prediction.
- Outperforms traditional anomaly detection baselines (RX, PaDiM) and time-series models (Linear AR, LSTM) on the DFC 2026 Hawaii eruption dataset, reaching 77.0% ROC-AUC.
- Demonstrates the effectiveness of local masked reconstruction with gradient feature prediction for domain-adapting Vision Transformers to SAR data.

## Open Questions & Future Work

- [[coherence-pseudo-gt-limitations]]

## Key Concepts

- [[t-sar-jepa]]: A self-supervised framework for temporal anomaly detection in SAR amplitude stacks through latent state forecasting.

## Archivist Review

I approved the T-SAR-JEPA framework as it offers a distinct, reusable methodology for latent-space anomaly detection in geospatial time-series. The DFC 2026 dataset was approved under a standardized slug, and the open question regarding the limitations of coherence-based pseudo-ground-truth was accepted due to its broad relevance to the field of SAR-based environmental monitoring.

### Approved Concepts
- T-SAR-JEPA: Provides a novel approach to unsupervised change detection in remote sensing by combining latent state forecasting with self-supervised feature adaptation.

### Approved Open Questions
- Limitations of Coherence Pseudo-GT: The reliance on noisy proxies like coherence for ground-truth limits the robustness and interpretability of anomaly detection benchmarks in remote sensing.

### Rejected Candidates
- [dataset] DFC 2026 (`DFC 2026`) - paper_local: The dataset name is generic/short-lived competition-style; using a standardized slug 'dfc-2026-dataset' instead.

## Datasets

- [[dfc-2026-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2606.05700)
- [PDF](https://arxiv.org/pdf/2606.05700)


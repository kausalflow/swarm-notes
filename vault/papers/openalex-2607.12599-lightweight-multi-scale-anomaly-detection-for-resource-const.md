---
# CSL-compatible fields
title: "Lightweight Multi-Scale Anomaly Detection for Resource-Constrained Edge Devices"
author:
  - literal: "Raheen Junaid Wani"
  - literal: "Smruti R. Sarangi"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2607.12599"

# Custom fields
paper_id: "2607.12599"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "model-compression"
  - "edge-computing"
architectures:
  []
datasets:
  []
concept_slugs:
  - "lmsae-lightweight-multiscale-autoencoder"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:10:08Z"
created_at: "2026-07-17T07:10:08Z"
---

# Lightweight Multi-Scale Anomaly Detection for Resource-Constrained Edge Devices

**Authors**: Raheen Junaid Wani, Smruti R. Sarangi
**Date**: 2026-07-14
**Paper ID**: [openalex:2607.12599](https://arxiv.org/abs/2607.12599)

## Summary

This paper addresses the challenge of deploying high-accuracy time-series anomaly detection models on resource-constrained edge devices. The authors propose the Lightweight MultiScale AutoEncoder (LMSAE), which utilizes Discrete Wavelet Transform (DWT) to efficiently capture multi-scale temporal features. By employing a specialized multi-scale loss function, the model maintains high detection sensitivity for subtle anomalies while keeping the parameter count and model footprint extremely low. Experimental results on edge hardware, specifically the NVIDIA Jetson Nano, validate its superior power and latency efficiency for real-time monitoring.

## Key Contributions

- Introduces the Lightweight MultiScale AutoEncoder (LMSAE), achieving high anomaly detection performance while maintaining a model size under 500 KB.
- Improves multi-scale anomaly sensitivity by integrating Discrete Wavelet Transform (DWT) feature extraction with a multi-scale loss function.
- Demonstrates significant deployment efficiency on edge hardware (NVIDIA Jetson Nano), achieving a 9x reduction in inference latency and 2x reduction in power consumption compared to baseline models.

## Open Questions & Future Work

- [[adaptive-multi-scale-loss-weighting]]

## Key Concepts

- [[lmsae-lightweight-multiscale-autoencoder]]: A compact autoencoder architecture that uses Discrete Wavelet Transform for multi-scale feature extraction and a tailored multi-scale loss function for efficient time-series anomaly detection.

## Archivist Review

I approved the LMSAE architecture as it provides a clear, reusable pattern for constrained-resource anomaly detection using wavelets. The open question regarding adaptive loss weighting was approved as it represents a fundamental bottleneck in multi-scale time-series modeling. The wavelet selection question was rejected as it is a specific implementation nuance rather than a general system-level challenge.

### Approved Concepts
- Lightweight MultiScale AutoEncoder (LMSAE): It is the core architectural innovation of the paper, addressing the conflict between anomaly detection sensitivity and edge resource constraints.

### Approved Open Questions
- Adaptive loss function weighting: Manual tuning of loss weights is a significant bottleneck for deploying anomaly detection models in real-world scenarios where data statistics may shift or vary.

### Rejected Candidates
- [open_question] Wavelet selection and edge effects (`wavelet-selection-edge-effects-analysis`) - subcomponent_of_broader_mechanism: This is a domain-specific implementation detail regarding wavelet transform properties rather than a foundational research bottleneck for forecasting systems.

## Links

- [Abstract](https://arxiv.org/abs/2607.12599)
- [PDF](https://arxiv.org/pdf/2607.12599)


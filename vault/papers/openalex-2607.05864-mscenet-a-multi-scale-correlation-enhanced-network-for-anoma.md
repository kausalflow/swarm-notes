---
# CSL-compatible fields
title: "MSCENet: A Multi-Scale Correlation Enhanced Network for Anomaly Detection"
author:
  - literal: "L Zhao"
  - literal: "Shixun Ji"
  - literal: "Zhipeng Wang"
  - literal: "Bin Cheng"
  - literal: "Bin He"
issued:
  date-parts:
    - [2026, 7, 7]
url: "https://arxiv.org/abs/2607.05864"

# Custom fields
paper_id: "2607.05864"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "graph-neural-network"
  - "convolutional-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-10T08:15:48Z"
created_at: "2026-07-10T08:15:48Z"
---

# MSCENet: A Multi-Scale Correlation Enhanced Network for Anomaly Detection

**Authors**: L Zhao, Shixun Ji, Zhipeng Wang, Bin Cheng, Bin He
**Date**: 2026-07-07
**Paper ID**: [openalex:2607.05864](https://arxiv.org/abs/2607.05864)

## Summary

MSCENet is a novel framework for multivariate time series anomaly detection that addresses the challenge of modeling complex cross-series dependencies and temporal dynamics. The model integrates a fine-grained temporal convolution module for multi-scale temporal pattern extraction with a Mixhop graph convolution structure to capture adaptive inter-series relationships. A multi-scale gated convolution module further fuses these spatial and temporal attributes to enhance the detection of subtle anomalies. Experiments demonstrate that MSCENet provides high-performance and adaptable detection capabilities across standard benchmarks such as SMD, PSM, and SWaT.

## Key Contributions

- Introduces MSCENet, a multivariate time series anomaly detection framework that utilizes multi-scale spatial-temporal modeling to address complex dependencies.
- Implements a fine-grained temporal convolution module using dilated convolutions to capture multi-scale temporal dynamics.
- Uses Mixhop graph convolutions to adaptively model intricate inter-series correlations across varying time scales.
- Achieves superior detection performance on standard anomaly detection benchmarks including SMD, PSM, and SWaT.

## Open Questions & Future Work

- [[computational-efficiency-in-anomaly-detection]]

## Archivist Review

The proposed framework components and benchmarks are standard practices in current time series anomaly detection literature and do not meet the novelty or reusability requirements for permanent vault entries. The open question regarding computational efficiency is approved as it addresses a persistent, critical challenge for deploying complex graph-based anomaly detection models in real-world environments.

### Approved Open Questions
- Enhancing Computational Efficiency and Scalability: Computational bottlenecks remain a significant barrier to transitioning complex graph-based anomaly detection models from research to real-world, time-critical operational environments.

### Rejected Candidates
- [concept] MSCENet Framework (`mscenet`) - subcomponent_of_broader_mechanism: The framework is a collection of standard architectural components rather than a distinct, reusable methodology or paradigm.
- [concept] Fine-grained Temporal Convolution Module (`fine-grained-temporal-convolution-module`) - not_novel: This is a standard implementation of dilated convolutions, which is already a widely used technique in time series modeling.
- [concept] Multi-scale Gated Convolution Module (`multi-scale-gated-convolution-module`) - generic: Gated mechanisms and multi-scale convolutions are generic architectural patterns in deep learning rather than reusable architectural primitives specific to this paper's contribution.
- [dataset] SMD Dataset (`smd-dataset`) - not_novel: SMD is a standard, widely-used benchmark in time series anomaly detection.
- [dataset] PSM Dataset (`psm-dataset`) - not_novel: PSM is a common benchmark in time series anomaly detection research.
- [dataset] SWaT Dataset (`swat-dataset`) - not_novel: SWaT is a routine benchmark dataset for time series anomaly detection.

## Links

- [Abstract](https://arxiv.org/abs/2607.05864)
- [PDF](https://arxiv.org/pdf/2607.05864)


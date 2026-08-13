---
# CSL-compatible fields
title: "LITEWAY: LIghtweight HAR via Temporal Efficient highWAY"
author:
  - literal: "Dominique Nshimyimana"
  - literal: "Vítor Fortes Rey"
  - literal: "Mengxi Liu"
  - literal: "Bo Zhou"
  - literal: "Paul Lukowicz"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09421"

# Custom fields
paper_id: "2608.09421"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "convolutional-neural-network"
  - "model-compression"
  - "efficiency"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:10:14Z"
created_at: "2026-08-13T06:10:14Z"
---

# LITEWAY: LIghtweight HAR via Temporal Efficient highWAY

**Authors**: Dominique Nshimyimana, Vítor Fortes Rey, Mengxi Liu, Bo Zhou, Paul Lukowicz
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09421](https://arxiv.org/abs/2608.09421)

## Summary

Wearable human activity recognition (HAR) is constrained by the high computational and energy demands of deep learning models on resource-limited devices. To address this, the authors propose LITEWAY, a modality-agnostic, fully convolutional framework that replaces recurrent temporal modeling with structured convolutional decomposition, lightweight blocks, and convolution-attention pooling. Evaluated across 16 HAR datasets, LITEWAY achieves competitive macro F1 scores while substantially reducing model size and energy consumption compared to baselines like TinyHAR, TinierHAR, and MLP-HAR.

## Key Contributions

- Proposes LITEWAY, a modality-agnostic, fully convolutional framework for multichannel sensor time series that replaces recurrent temporal modeling with structured convolutional decomposition.
- Combines lightweight convolutional blocks, strided temporal processing, and convolution-attention pooling to capture temporal dependencies while reducing computational complexity.
- Reduces model size by 4.06x-9.52x (Light) and 3.87x-9.07x (Full) compared with TinyHAR and TinierHAR across 16 HAR datasets while maintaining competitive macro F1.
- Achieves energy reductions of 2.29x-3.14x (Light) and 1.46x-2.01x (Full) compared with TinierHAR and MLP-HAR in deployment experiments.

## Archivist Review

The proposed concept and open question are paper-local architectural terms and standard edge-deployment future work, lacking the broad theoretical novelty required for permanent vault inclusion.

### Rejected Candidates
- [concept] LITEWAY (`liteway`) - paper_local: Paper-specific architecture name for a lightweight sensor HAR model, not a widely reusable foundational concept.
- [open_question] Hardware-Aware Optimization for Edge HAR (`hardware-aware-optimization-and-generalization-for-edge-har`) - low_impact: Standard future work regarding hardware deployment, quantization, and pruning for edge microcontrollers rather than a fundamental theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.09421)
- [PDF](https://arxiv.org/pdf/2608.09421)


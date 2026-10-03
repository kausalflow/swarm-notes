---
# CSL-compatible fields
title: "WinoTS: Wavelet-based Self-Distillation for Time Series Models"
author:
  - literal: "Noam Major"
  - literal: "Kathy Razmadze"
  - literal: "Yoli Shavit"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.39337"

# Custom fields
paper_id: "2609.39337"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "self-supervised-learning"
  - "pre-training"
  - "zero-shot-learning"
  - "representation-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "winots"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:07:45Z"
created_at: "2026-10-03T10:07:45Z"
---

# WinoTS: Wavelet-based Self-Distillation for Time Series Models

**Authors**: Noam Major, Kathy Razmadze, Yoli Shavit
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.39337](https://arxiv.org/abs/2609.39337)

## Summary

WinoTS is a wavelet-based self-distillation framework for time series pre-training that replaces vision-style spatial augmentations with principled time-frequency augmentations. By constructing multi-scale structural views without distorting underlying signal dynamics, WinoTS avoids wasting capacity on high-frequency noise. Extensive evaluations show that WinoTS surpasses state-of-the-art methods in long-term forecasting, cross-domain zero-shot transfer, and unsupervised anomaly detection.

## Key Contributions

- Introduces WinoTS, an invariance-based self-distillation pre-training paradigm using time-frequency augmentations to avoid point-wise noise and capture multi-scale temporal structures.
- Outperforms state-of-the-art baselines across long-term forecasting, cross-domain zero-shot transfer, and unsupervised anomaly detection.
- Demonstrates that linear probing on frozen WinoTS representations frequently surpasses fully supervised models trained from scratch.
- Establishes through systematic ablations that WinoTS is an architecture-agnostic framework compatible with various time series backbones.

## Open Questions & Future Work

- [[adaptive-wavelet-bases-multimodal-ts]]

## Key Concepts

- [[winots]]: A wavelet-based self-distillation pre-training paradigm for time series that constructs multi-scale structural views via time-frequency augmentations.

## Archivist Review

Approved the core WinoTS framework concept and its corresponding open question regarding adaptive wavelet bases and multi-modal temporal systems, following strict scarcity and relevance criteria. No datasets were provided or required.

### Approved Concepts
- WinoTS: Core self-supervised pre-training framework introducing wavelet-based time-frequency augmentations for time series self-distillation.

### Approved Open Questions
- Adaptive Wavelet Bases and Multi-Modal Temporal Systems: This is a concrete, multi-faceted direction that proposes specific technical extensions (learnable wavelet bases and scale-free multi-modal systems) to address limitations in current time-series self-supervised learning.

## Links

- [Abstract](https://arxiv.org/abs/2609.39337)
- [PDF](https://arxiv.org/pdf/2609.39337)


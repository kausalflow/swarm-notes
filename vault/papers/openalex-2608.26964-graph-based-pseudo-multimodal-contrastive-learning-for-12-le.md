---
# CSL-compatible fields
title: "Graph-Based Pseudo-multimodal Contrastive Learning for 12-Lead ECG Representations"
author:
  - literal: "Mengyu Wang"
  - literal: "Kozo Okada"
  - literal: "Takafumi Goto"
  - literal: "Natsuko Jinba"
  - literal: "Hiroki Yamaya"
  - literal: "Kiyoshi Hibi"
  - literal: "Tomoki Hamagami"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.26964"

# Custom fields
paper_id: "2608.26964"
paper_source: "openalex"
domain: "biology"
tags:
  - "self-supervised-learning"
  - "contrastive-learning"
  - "graph-neural-network"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "graph-cmmc"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-30T10:11:28Z"
created_at: "2026-08-30T10:11:28Z"
---

# Graph-Based Pseudo-multimodal Contrastive Learning for 12-Lead ECG Representations

**Authors**: Mengyu Wang, Kozo Okada, Takafumi Goto, Natsuko Jinba, Hiroki Yamaya, Kiyoshi Hibi, Tomoki Hamagami
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.26964](https://arxiv.org/abs/2608.26964)

## Summary

This paper introduces Graph-CMMC, a graph-based pseudo-multimodal contrastive learning framework for 12-lead ECG representations. By transforming ECG waveforms into Gramian Angular Difference Field (GADF) images and leveraging a graph-based relational module, the method effectively captures inter-lead dependencies and global waveform patterns. Evaluated on a multi-label coronary artery occlusion classification task, Graph-CMMC achieves competitive performance against supervised baselines.

## Key Contributions

- Proposes Graph-CMMC, a graph-based pseudo-multimodal contrastive learning framework for 12-lead ECG representations.
- Transforms ECG waveforms into Gramian Angular Difference Field (GADF) images to establish a pseudo-multimodal learning setting.
- Employs a graph-based relational module to model inter-lead dependency and structural consistency during self-supervised contrastive learning.
- Demonstrates competitive performance on a multi-label coronary artery occlusion classification task compared to fully supervised baselines.

## Open Questions & Future Work

- [[clinical-interpretability-and-scaling-of-ecg-graph-models]]

## Key Concepts

- [[graph-cmmc]]: A graph-based pseudo-multimodal contrastive learning framework for 12-lead ECG representation learning.

## Archivist Review

Approved the overarching Graph-CMMC concept and a core open question regarding the clinical interpretability and scaling of graph-based ECG models, while adhering to strict scarity and criteria limits. No named dataset was introduced.

### Approved Concepts
- Graph-CMMC: Introduces a novel framework for 12-lead ECG representation learning via graph-based pseudo-multimodal contrastive learning.

### Approved Open Questions
- Clinical Interpretability and Scaling of ECG Graph Models: Crucial for validating the generalizability and clinical interpretability of data-driven graph structures in multi-lead ECG analysis.

## Links

- [Abstract](https://arxiv.org/abs/2608.26964)
- [PDF](https://arxiv.org/pdf/2608.26964)


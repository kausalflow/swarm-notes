---
# CSL-compatible fields
title: "A Lightweight Self-Supervised Learning Framework for Multivariate Time Series using Hierarchical-JEPA on ECG Data"
author:
  - literal: "S K Kim"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.01145"

# Custom fields
paper_id: "2607.01145"
paper_source: "openalex"
domain: "medicine"
tags:
  - "self-supervised-learning"
  - "time-series"
  - "vision-transformer"
  - "vit"
  - "medical"
architectures:
  []
datasets:
  - "st-mem"
concept_slugs:
  - "er-jepa"
dataset_slugs:
  - "st-mem"
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:35:57Z"
created_at: "2026-07-04T07:35:57Z"
---

# A Lightweight Self-Supervised Learning Framework for Multivariate Time Series using Hierarchical-JEPA on ECG Data

**Authors**: S K Kim
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.01145](https://arxiv.org/abs/2607.01145)

## Summary

The paper introduces the Event Reconstruction Joint-Embedding Predictive Architecture (ER-JEPA), a lightweight self-supervised framework for multivariate time series analysis. By utilizing a two-stage hierarchical design with a Vision Transformer backbone, ER-JEPA effectively encodes abstract representations across multiple levels, inspired by clinical cardiological practices. Evaluations on 12-lead ECG recordings demonstrate that the model achieves state-of-the-art downstream performance on the ST-MEM benchmark with significantly reduced computational requirements.

## Key Contributions

- Introduces ER-JEPA, a hierarchical self-supervised learning framework designed for efficient representation learning in multivariate time series.
- Employs a two-stage hierarchical architecture that processes interval-level representations as univariate series, improving interpretability and prediction.
- Achieves state-of-the-art performance on the ST-MEM benchmark for 12-lead ECG analysis while maintaining computational efficiency.

## Open Questions & Future Work

- [[mitigating-representation-collapse-in-hierarchical-jepa]]

## Key Concepts

- [[er-jepa]]: A hierarchical self-supervised learning framework that encodes time series via a two-stage process, constructing interval-level representations before hierarchical JEPA integration.

## Archivist Review

I approved the ER-JEPA architecture as it introduces a distinct, hierarchical self-supervised learning approach for time-series that is potentially reusable. The open question regarding representation collapse in such hierarchical architectures is a significant technical bottleneck for future scaling. Other candidates were rejected for being either standard architectural choices (ViT) or specific analytical procedures local to the paper's experiments.

### Approved Concepts
- Event Reconstruction Joint-Embedding Predictive Architecture (ER-JEPA): The framework provides a novel hierarchical approach to representation learning that balances computational efficiency with the ability to encode multi-scale temporal abstractions.

### Approved Open Questions
- Mitigating Representation Collapse in Hierarchical-JEPA: Mitigating collapse is essential for the practical scaling and deployment of hierarchical self-supervised learning architectures in time-series domains.

### Rejected Candidates
- [concept] Vision Transformer Backbone (`vit-backbone-for-time-series`) - not_novel: Using a standard ViT for time-series is a common architectural choice and does not constitute a novel concept here.
- [concept] Hierarchical Representation Sensitivity Analysis (`hierarchical-representation-sensitivity`) - paper_local: This is an analytical procedure specific to the study of the proposed model rather than a core, reusable methodological framework.

## Datasets

- [[st-mem]]

## Links

- [Abstract](https://arxiv.org/abs/2607.01145)
- [PDF](https://arxiv.org/pdf/2607.01145)


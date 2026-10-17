---
# CSL-compatible fields
title: "TEX-MEX: Similarity-Guided Temporal Contrastive Learning for Time Series"
author:
  - literal: "Aditya Radhakrishnan"
  - literal: "Maxwell A. Xu"
  - literal: "Wanting Mao"
  - literal: "Santosh Kumar"
  - literal: "Harish Haresamudram"
  - literal: "James Matthew Rehg"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.19557"

# Custom fields
paper_id: "2610.19557"
paper_source: "openalex"
domain: "time-series"
tags:
  - "self-supervised-learning"
  - "contrastive-learning"
  - "time-series"
  - "representation-learning"
  - "foundation-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tex-mex"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:54:44Z"
created_at: "2026-10-17T08:54:44Z"
---

# TEX-MEX: Similarity-Guided Temporal Contrastive Learning for Time Series

**Authors**: Aditya Radhakrishnan, Maxwell A. Xu, Wanting Mao, Santosh Kumar, Harish Haresamudram, James Matthew Rehg
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.19557](https://arxiv.org/abs/2610.19557)

## Summary

The paper introduces TEX-MEX, a novel self-supervised contrastive learning method for time series that unifies structural and temporal similarity. By identifying structurally similar or dissimilar windows and pulling/pushing them relative to temporally shifted versions, TEX-MEX learns robust representations and achieves state-of-the-art performance across diverse modalities like PPG, EEG, ECG, accelerometry, and continuous glucose monitoring.

## Key Contributions

- Introduces TEX-MEX, a novel similarity-guided temporal contrastive learning approach that unifies structural and temporal similarity for time series representation learning.
- Achieves state-of-the-art performance across diverse physiological and physical time series modalities including PPG, EEG, ECG, accelerometry, and continuous glucose monitoring.
- Trains a 560K-parameter PPG foundation model that outperforms much larger unimodal baselines across downstream benchmarks.

## Key Concepts

- [[tex-mex]]: A self-supervised time series representation learning framework that unifies structural and temporal similarity into a single contrastive relationship.

## Archivist Review

Approved the core method TEX-MEX as a reusable contrastive learning framework unifying structural and temporal similarity. Rejected the open question because expanding pretraining corpora is a routine dataset engineering task rather than a fundamental theoretical bottleneck.

### Approved Concepts
- TEX-MEX: Unifies structural and temporal similarity into a single contrastive relationship for time series self-supervised learning.

### Rejected Candidates
- [open_question] Expanding Pretraining Corpora for Sleep Tasks (`expanding-pretraining-corpora-for-sleep-tasks`) - low_impact: Specifies a routine dataset curation direction rather than a foundational theoretical or methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.19557)
- [PDF](https://arxiv.org/pdf/2610.19557)


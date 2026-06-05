---
# CSL-compatible fields
title: "State of Health Estimation of Batteries Using a Time-Informed Dynamic Sequence-Inverted Transformer"
author:
  - literal: "Janak M. Patel"
  - literal: "Milad Ramezankhani"
  - literal: "Anirudh Deodhar"
  - literal: "Dagnachew Birru"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2507.18320"

# Custom fields
paper_id: "2507.18320"
paper_source: "openalex"
domain: "time-series,"
tags:
  - "transformer"
  - "time-series"
  - "attention-mechanism"
  - "benchmark"
  - "dataset"
architectures:
  - "encoder-only"
datasets:
  - "nasa-battery-degradation-dataset"
concept_slugs:
  - "time-informed-dynamic-sequence-inverted-transformer-tidsit"
dataset_slugs:
  - "nasa-battery-degradation-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:39:55Z"
created_at: "2026-06-05T08:39:55Z"
---

# State of Health Estimation of Batteries Using a Time-Informed Dynamic Sequence-Inverted Transformer

**Authors**: Janak M. Patel, Milad Ramezankhani, Anirudh Deodhar, Dagnachew Birru
**Date**: 2026-06-02
**Paper ID**: [openalex:2507.18320](https://arxiv.org/abs/2507.18320)

## Summary

TIDSIT addresses the limitations of standard sequence models in battery State of Health (SoH) estimation by handling irregular, non-uniform time intervals and variable-length sequences. The architecture employs continuous time embeddings and temporal attention mechanisms to preserve sequence integrity, avoiding the information loss associated with manual feature extraction. Experiments on the NASA battery degradation dataset show TIDSIT significantly improves prediction accuracy over existing LSTMs and standard transformer baselines.

## Key Contributions

- Introduces TIDSIT, a transformer architecture tailored for irregular battery discharge cycles.
- Uses continuous time embeddings to process non-uniformly sampled sensor readings without information loss.
- Achieves 43% reduction in SoH prediction error compared to established baselines, reaching an RMSE% of 0.58% on the NASA battery dataset.

## Open Questions & Future Work

- [[scalable-interpretable-real-time-battery-prognostics]]

## Key Concepts

- [[time-informed-dynamic-sequence-inverted-transformer-tidsit]]: A transformer-based architecture using continuous time embeddings and temporal attention to process irregularly sampled, variable-length time series.

## Archivist Review

I have approved the TIDSIT architecture as a distinct mechanism for handling irregular time series through continuous time embeddings and temporal attention. The NASA dataset is approved as it is a widely utilized domain-standard for battery degradation. The open question is approved for its focus on the transition from research performance to deployment-constrained BMS requirements, which is a substantial bottleneck in the field.

### Approved Concepts
- Time Informed Dynamic Sequence Inverted Transformer (TIDSIT): It proposes a concrete architectural solution to the problem of processing irregularly sampled, variable-length time series in the context of SoH estimation.

### Approved Open Questions
- Scalable and Interpretable Battery Prognostics: Transitioning to more efficient, real-time-capable models is a critical bottleneck for deploying deep learning in edge-deployed battery management systems.

## Datasets

- [[nasa-battery-degradation-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2507.18320)
- [PDF](https://arxiv.org/pdf/2507.18320)


---
# CSL-compatible fields
title: "TempTPI: Informer-Based trajectory prediction for maritime vessels"
author:
  - literal: "Kevin Ferneding"
  - literal: "Veronika Lietavcova"
  - literal: "Aleksandra M. Blachowiak"
  - literal: "Peder Heiselberg"
issued:
  date-parts:
    - [2026, 9, 9]
url: "https://arxiv.org/abs/2609.09840"

# Custom fields
paper_id: "2609.09840"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "self-attention"
  - "time-series"
  - "forecasting"
  - "long-context"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-12T08:56:00Z"
created_at: "2026-09-12T08:56:00Z"
---

# TempTPI: Informer-Based trajectory prediction for maritime vessels

**Authors**: Kevin Ferneding, Veronika Lietavcova, Aleksandra M. Blachowiak, Peder Heiselberg
**Date**: 2026-09-09
**Paper ID**: [openalex:2609.09840](https://arxiv.org/abs/2609.09840)

## Summary

The paper introduces TempTPI, an Informer-based trajectory prediction framework designed for maritime vessels using Automatic Identification System (AIS) data. By incorporating a ProbSparse self-attention mechanism to mitigate quadratic complexity and a multi-channel temporal encoder with Fourier-like frequency expansions, the model effectively captures cyclic behavioral patterns. Evaluated on AIS data from Danish waters, TempTPI outperforms state-of-the-art baselines like TPTrans, achieving a 55% improvement in MSE at a 5-hour forecasting horizon.

## Key Contributions

- Proposes TempTPI, a maritime vessel trajectory prediction framework integrating an Informer-based encoder with multi-channel temporal encoding.
- Leverages ProbSparse self-attention to reduce quadratic computational complexity while focusing on significant long-range dependencies.
- Employs Fourier-like frequency expansions to capture complex hourly, daily, and seasonal cyclic patterns in vessel movement.
- Achieves a 55% improvement in Mean Squared Error (MSE) compared to the state-of-the-art TPTrans architecture on AIS data from Danish waters over a 5-hour forecasting horizon.

## Limitations

Evaluated specifically on Automatic Identification System (AIS) data from Danish waters; generalization to other maritime regions or dynamic oceanic traffic conditions requires further validation.

## Open Questions & Future Work

- [[land-avoidance-penalized-training-trajectory-prediction]]

## Archivist Review

Enforced strict selectivity by rejecting the paper-specific framework note (TempTPI) as a paper-local model instance of Informer. Approved the open question on land avoidance and penalized training since it addresses a concrete physical constraint limitation in trajectory prediction. No datasets qualified for standalone vault entry.

### Approved Open Questions
- Land Avoidance and Penalized Training: Ensuring that predicted maritime paths respect physical geography is critical for collision avoidance and operational safety, yet standard regression losses often fail to enforce these constraints without destabilizing training.

### Rejected Candidates
- [concept] TempTPI (`temptpi`) - paper_local: TempTPI is a paper-specific application of the existing Informer architecture to maritime vessel trajectories, lacking broad methodological novelty beyond standard domain adaptation.

## Links

- [Abstract](https://arxiv.org/abs/2609.09840)
- [PDF](https://arxiv.org/pdf/2609.09840)


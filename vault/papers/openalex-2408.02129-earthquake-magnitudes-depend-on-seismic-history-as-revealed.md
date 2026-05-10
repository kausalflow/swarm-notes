---
# CSL-compatible fields
title: "Earthquake magnitudes depend on seismic history, as revealed by a neural network analysis"
author:
  - literal: "Neri Berman"
  - literal: "Oleg Zlydenko"
  - literal: "Oren Gilon"
  - literal: "Yossi Matias"
  - literal: "Yohai Bar‐Sinai"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2408.02129"

# Custom fields
paper_id: "2408.02129"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
  - "lstm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "magnet-magnitude-neural-estimation-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:22:10Z"
created_at: "2026-05-10T07:22:10Z"
---

# Earthquake magnitudes depend on seismic history, as revealed by a neural network analysis

**Authors**: Neri Berman, Oleg Zlydenko, Oren Gilon, Yossi Matias, Yohai Bar‐Sinai
**Date**: 2026-05-07
**Paper ID**: [openalex:2408.02129](https://arxiv.org/abs/2408.02129)

## Summary

Earthquake magnitude forecasting has historically relied on the assumption that magnitudes are independent of seismic history, following a time-independent Gutenberg-Richter distribution. This paper challenges this view by introducing MAGNET, a multi-encoder LSTM-based neural model that leverages spatiotemporal patterns in past hypocenter catalogs. Empirical results from three major seismic regions demonstrate that MAGNET achieves a consistent information gain over traditional statistical models, indicating that future earthquake magnitudes are more predictable than previously assumed.

## Key Contributions

- Introduces MAGNET, a multi-encoder LSTM neural model that proves seismic history contains extractable information for predicting future earthquake magnitudes.
- Demonstrates a persistent information gain of ~0.07 bits per earthquake over the conventional time-independent Gutenberg-Richter (GR) distribution benchmark.
- Provides empirical evidence across Southern California, Japan, and New Zealand datasets that challenges the long-standing assumption that earthquake magnitudes are independent of preceding seismic history.

## Open Questions & Future Work

- [[interpretability-of-seismic-magnitude-prediction-features]]

## Key Concepts

- [[magnet-magnitude-neural-estimation-model]]: A multi-encoder LSTM-based neural network architecture for probabilistic magnitude forecasting by processing spatiotemporal patterns in seismic history.

## Archivist Review

I approved the MAGNET architecture as a representative model for challenging the magnitude-history separability assumption in seismology, and the associated open question regarding feature interpretability. The datasets mentioned in the paper (Southern California, Japan, and New Zealand catalogs) were rejected as they are standard geophysical data sources rather than specific, novel, or uniquely defined benchmark artifacts requiring standalone notes. I applied strict criteria to ensure only substantively novel mechanisms and critical, non-boilerplate research questions were retained.

### Approved Concepts
- MAGNET (MAGnitude Neural EsTimation model): MAGNET introduces a novel neural approach to challenge the standard assumption that earthquake magnitudes are independent of seismic history.

### Approved Open Questions
- Interpretability of seismic magnitude prediction features: Ablation studies are critical for transitioning from black-box predictive models to physically informed, interpretable seismic models, enabling researchers to distinguish between mere statistical artifacts and genuine physical precursors.

## Links

- [Abstract](https://arxiv.org/abs/2408.02129)
- [PDF](https://arxiv.org/pdf/2408.02129)


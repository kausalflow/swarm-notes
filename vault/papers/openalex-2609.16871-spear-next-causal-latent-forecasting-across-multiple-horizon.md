---
# CSL-compatible fields
title: "SPEAR NeXT Causal Latent Forecasting Across Multiple Horizons for Spectral Temporal Earth Representation Learning"
author:
  - literal: "Rajiv Ranjan"
  - literal: "Udaiveer Singh"
  - literal: "Shashank Tamaskar"
  - literal: "Dharmendra Saraswat"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.16871"

# Custom fields
paper_id: "2609.16871"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "transformer"
  - "self-attention"
  - "multimodal"
  - "time-series"
  - "forecasting"
  - "pre-training"
  - "rotary-position-embedding"
  - "rope"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:17:39Z"
created_at: "2026-09-18T09:17:39Z"
---

# SPEAR NeXT Causal Latent Forecasting Across Multiple Horizons for Spectral Temporal Earth Representation Learning

**Authors**: Rajiv Ranjan, Udaiveer Singh, Shashank Tamaskar, Dharmendra Saraswat
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.16871](https://arxiv.org/abs/2609.16871)

## Summary

SPEAR NeXT is introduced as a compact pixel-wise multimodal spectral temporal foundation model that frames temporal self-supervision as past-only, multi-horizon latent Earth state prediction. The model encodes instantaneous multi-sensor observations into low-dimensional embeddings and uses a causally masked Transformer with Rotary Position Embeddings alongside seasonal and interannual context embeddings to model their temporal evolution.

## Key Contributions

- Introduces SPEAR NeXT, a compact pixel-wise multimodal spectral temporal foundation model for Earth observation.
- Formulates temporal self-supervision as past-only, multi-horizon latent Earth state prediction.
- Incorporates Rotary Position Embeddings for relative temporal order and month/year embeddings for seasonal and interannual context.

## Open Questions & Future Work

- [[biophysical-interpretation-latent-forecasting]]

## Archivist Review

Approved the open question on biophysical interpretability of latent forecasting as it captures a fundamental limitation in grounding abstract temporal predictions to physical Earth observation processes. Rejected all specific architecture names as paper-local.

### Approved Open Questions
- Biophysical Interpretation of Latent Forecasting: Important for bridging the gap between abstract latent forecasting performance and physically interpretable Earth-observation models that can handle real-world irregular sensor availability.

### Rejected Candidates
- [concept] SPEAR NeXT (`spear-next`) - paper_local: Paper-local architecture name for a specific multimodal earth observation foundation model.

## Links

- [Abstract](https://arxiv.org/abs/2609.16871)
- [PDF](https://arxiv.org/pdf/2609.16871)


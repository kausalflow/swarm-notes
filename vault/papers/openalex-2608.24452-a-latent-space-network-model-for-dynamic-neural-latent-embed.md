---
# CSL-compatible fields
title: "A latent space network model for dynamic neural latent embedding"
author:
  - literal: "Riccardo Rastelli"
  - literal: "Shizhe Chen"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.24452"

# Custom fields
paper_id: "2608.24452"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "graph-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T17:00:44Z"
created_at: "2026-08-28T17:00:44Z"
---

# A latent space network model for dynamic neural latent embedding

**Authors**: Riccardo Rastelli, Shizhe Chen
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.24452](https://arxiv.org/abs/2608.24452)

## Summary

The paper introduces a latent space network model to analyze multivariate time series of neural spike-train data, modeling regional firing rates and hidden interactions simultaneously. By embedding the interaction network in a geometric latent space, the framework enables interpretable visualizations and intuitive node eigen-centrality interpretations. Furthermore, a nested hidden Markov structure is incorporated to capture non-linear temporal shifts from changing experimental conditions, backed by theoretical conditions to prevent model degeneracy.

## Key Contributions

- Introduces a latent space network model for analyzing multivariate neural spike-train time series and region interactions.
- Incorporates a nested hidden Markov structure to capture non-linear temporal shifts induced by changing experimental conditions.
- Establishes theoretical properties and sufficient conditions preventing model degeneracy.

## Open Questions & Future Work

- [[scalable-inference-latent-space-networks]]

## Archivist Review

The paper presents a latent space network model for neural spike trains with a nested hidden Markov structure. The open question candidate on scalable inference for latent space networks overlaps with existing computational scaling questions in the vault, so no new items met the strict novelty and scarcity standards.

### Approved Open Questions
- Scalable Inference for Latent Space Networks: Computational scaling is the primary limitation preventing latent space network models from analyzing massive, unaggregated neural recordings or dense socio-economic networks.

### Rejected Candidates
- [open_question] Scalable Inference for Latent Space Networks (`scalable-inference-latent-space-networks`) - duplicate_existing: A very similar open question already exists in the vault regarding computational scaling of latent network and graph models.

## Links

- [Abstract](https://arxiv.org/abs/2608.24452)
- [PDF](https://arxiv.org/pdf/2608.24452)


---
# CSL-compatible fields
title: "Latent Inference-Time Guidance of Time Series Foundation Models"
author:
  - literal: "Chloé Hashimoto-Cullen"
  - literal: "Amaury Durand"
  - literal: "Laurent Bozzi"
  - literal: "Benjamin Guedj"
  - literal: "Yannig Goude"
  - literal: "Sylvain Le Corff"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.38058"

# Custom fields
paper_id: "2609.38058"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "foundation-model"
  - "in-context-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "latent-inference-time-guidance"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:14:59Z"
created_at: "2026-10-01T11:14:59Z"
---

# Latent Inference-Time Guidance of Time Series Foundation Models

**Authors**: Chloé Hashimoto-Cullen, Amaury Durand, Laurent Bozzi, Benjamin Guedj, Yannig Goude, Sylvain Le Corff
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.38058](https://arxiv.org/abs/2609.38058)

## Summary

Time Series Foundation Models (TSFMs) achieve state-of-the-art results using in-context learning, but their forecast quality is highly sensitive to input context selection, creating a need for principled ensembling. This paper proposes Latent Inference-Time Guidance, a novel framework that adaptively combines a pool of TSFM forecasts using a time-dependent latent space with independent components. The approach comes with formal identifiability and reconstruction guarantees while preserving the off-the-shelf nature of foundation models. Experiments across diverse domains and frequencies demonstrate that the proposed method is highly competitive with traditional ensembling approaches.

## Key Contributions

- Introduces Latent Inference-Time Guidance for time series foundation models to adaptively combine multiple TSFM forecasts via a time-dependent latent space.
- Provides theoretical identifiability and reconstruction guarantees for the latent space formulation while preserving the off-the-shelf utility of foundation models.
- Demonstrates through experiments across multiple domains and frequencies that the approach is competitive with traditional time series ensembling techniques.

## Key Concepts

- [[latent-inference-time-guidance]]: An adaptive ensembling framework that combines time series foundation model forecasts through a time-dependent latent space with independent components.

## Archivist Review

Evaluated the paper strictly against the vault's high standards. Approved the core concept 'Latent Inference-Time Guidance' because it introduces a distinct, principled, and reusable mechanism for ensembling time series foundation models in a time-dependent latent space. No datasets or open questions met the strict standalone criteria, so none were approved.

### Approved Concepts
- Latent Inference-Time Guidance: Provides a principled, adaptive ensembling approach for time series foundation models via a time-dependent latent space.

## Links

- [Abstract](https://arxiv.org/abs/2609.38058)
- [PDF](https://arxiv.org/pdf/2609.38058)


---
# CSL-compatible fields
title: "ProtoFlow: Prototype-Guided Flow Matching for Multivariate Time Series Forecasting"
author:
  - literal: "Shibo Feng"
  - literal: "Wanjin Feng"
  - literal: "Yang Qiu"
  - literal: "Deheng Ye"
  - literal: "Peilin Zhao"
  - literal: "Chunyan Miao"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01320"

# Custom fields
paper_id: "2610.01320"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "generative-adversarial-network"
  - "diffusion-model"
  - "autoregressive"
  - "vector-database"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "protoflow"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:48:01Z"
created_at: "2026-10-04T10:48:01Z"
---

# ProtoFlow: Prototype-Guided Flow Matching for Multivariate Time Series Forecasting

**Authors**: Shibo Feng, Wanjin Feng, Yang Qiu, Deheng Ye, Peilin Zhao, Chunyan Miao
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01320](https://arxiv.org/abs/2610.01320)

## Summary

ProtoFlow is a multivariate time series forecasting framework that combines vector-quantized autoencoding with a prototype-prior flow matching mechanism. Instead of initializing transport from a generic Gaussian prior or relying on error-prone autoregressive token generation, ProtoFlow utilizes the learned VQ codebook prototypes as a structured prior to guide a DiT-based rectified flow. Extensive experiments show that this approach achieves superior forecasting accuracy and efficient inference while avoiding rollout mismatch.

## Key Contributions

- Proposes ProtoFlow, a multivariate time series forecasting framework that leverages vector-quantized codebook prototypes as a structured prior for flow matching.
- Replaces autoregressive token generation with DiT-based rectified flow to avoid exposure bias and training-inference mismatch.
- Demonstrates consistent superior forecasting performance and efficient inference across benchmark datasets.

## Open Questions & Future Work

- [[context-dependent-prototype-weighting-flow-matching]]

## Key Concepts

- [[protoflow]]: A multivariate time series forecasting framework combining vector-quantized autoencoding with a structured prototype prior for flow matching.

## Archivist Review

Approved the overarching framework concept 'ProtoFlow' and the explicit open question regarding context-dependent prototype prior adaptation. Applied strict scarcity and quality filters to maintain a clean knowledge vault.

### Approved Concepts
- ProtoFlow: ProtoFlow is the central methodological contribution of the paper, introducing prototype-guided flow matching for multivariate time series forecasting.

### Approved Open Questions
- Context-Dependent Prototype Prior Adaptation: Addressing static prior initialization can bridge the gap between global codebook representations and localized temporal uncertainties, potentially improving probabilistic forecasting quality across diverse and non-stationary regimes.

## Links

- [Abstract](https://arxiv.org/abs/2610.01320)
- [PDF](https://arxiv.org/pdf/2610.01320)


---
# CSL-compatible fields
title: "ManifoldFormer: Geometric Deep Learning for Neural Dynamics on Riemannian Manifolds"
author:
  - literal: "Yihang Fu"
  - literal: "Lifang He"
  - literal: "Qingyu Chen"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2511.16828"

# Custom fields
paper_id: "2511.16828"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "attention-mechanism"
  - "vae"
  - "time-series"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "riemannianvae"
  - "geometrictransformer"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T07:01:29Z"
created_at: "2026-04-24T07:01:29Z"
---

# ManifoldFormer: Geometric Deep Learning for Neural Dynamics on Riemannian Manifolds

**Authors**: Yihang Fu, Lifang He, Qingyu Chen
**Date**: 2026-04-21
**Paper ID**: [openalex:2511.16828](https://arxiv.org/abs/2511.16828)

## Summary

ManifoldFormer is a novel deep learning framework that models neural signals as dynamics on Riemannian manifolds rather than treating them as generic Euclidean time series. It utilizes RiemannianVAE for structured manifold embedding, a GeometricTransformer with geodesic-aware attention, and a DynamicsPredictor based on Neural ODEs to ensure manifold-constrained temporal evolution. The approach significantly outperforms state-of-the-art EEG models in both predictive accuracy and cross-subject generalization by aligning model architecture with neurophysiological principles.

## Key Contributions

- Introduces ManifoldFormer, a geometric deep learning framework for EEG modeling that explicitly incorporates manifold constraints.
- Achieves 4.6–4.8% accuracy and 6.2–10.2% Cohen's Kappa improvements over state-of-the-art EEG methods across four benchmarks.
- Demonstrates that manifold-constrained temporal evolution via Neural ODEs significantly enhances cross-subject generalization for brain signal analysis.

## Open Questions & Future Work

- [[automated-manifold-geometry-selection]]

## Key Concepts

- [[riemannianvae]]: A variational autoencoder framework designed to embed data while explicitly preserving its underlying Riemannian manifold structure.
- [[geometrictransformer]]: A transformer variant featuring geodesic-aware attention mechanisms that compute relationships directly on neural manifolds.

## Archivist Review

Approved the two core geometric mechanisms (RiemannianVAE and GeometricTransformer) as they represent a cohesive approach to non-Euclidean time-series modeling. Added the question on automated manifold selection as it identifies a clear bottleneck in moving toward more generalized geometric foundation models. No datasets were approved as none were explicitly provided in the analysis input.

### Approved Concepts
- RiemannianVAE: It provides a formal mechanism for embedding high-dimensional time series into structured Riemannian latent spaces.
- GeometricTransformer: It replaces traditional Euclidean self-attention with geodesic-aware mechanisms to account for non-Euclidean connectivity.

### Approved Open Questions
- Automated Riemannian manifold selection: Mismatched manifold geometry can introduce significant representational bias, hindering the performance of geometric foundation models across different physiological domains.

## Links

- [Abstract](https://arxiv.org/abs/2511.16828)
- [PDF](https://arxiv.org/pdf/2511.16828)


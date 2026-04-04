---
# CSL-compatible fields
title: "Super-Resolving Coarse-Resolution Weather Forecasts With Flow Matching"
author:
  - literal: "Aymeric Delefosse"
  - literal: "Anastase Charantonis"
  - literal: "Dominique Béréziat"
  - literal: ""
issued:
  date-parts:
    - [2026, 4, 1]
url: "https://arxiv.org/abs/2604.00897"

# Custom fields
paper_id: "2604.00897"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "generative-adversarial-network"
  - "diffusion-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "generative-weather-super-resolution"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-04T05:49:27Z"
created_at: "2026-04-04T05:49:27Z"
---

# Super-Resolving Coarse-Resolution Weather Forecasts With Flow Matching

**Authors**: Aymeric Delefosse, Anastase Charantonis, Dominique Béréziat, 
**Date**: 2026-04-01
**Paper ID**: [openalex:2604.00897](https://arxiv.org/abs/2604.00897)

## Summary

This paper introduces a modular framework for super-resolving coarse-resolution weather forecasts using generative flow matching as a post-processing step. By treating super-resolution as a stochastic inverse problem with a residual formulation, the method preserves large-scale physical structures while effectively reconstructing unresolved small-scale variability. Evaluation across medium-range global forecasts shows that the approach achieves competitive probabilistic skill at 0.25° resolution compared to operational ensemble baselines at a fraction of the computational cost.

## Key Contributions

- Proposes a modular post-processing framework that decouples forecasting from spatial resolution, significantly reducing computational requirements compared to end-to-end high-resolution models.
- Formulates super-resolution as a stochastic inverse problem using a residual formulation, enabling the reconstruction of physically consistent small-scale variability.
- Demonstrates that the flow matching model achieves competitive probabilistic skill at 0.25° resolution compared to operational ensemble baselines while maintaining large-scale structural consistency.

## Open Questions & Future Work

- [[integrated-super-resolution-forecasting-feedback]]
- [[efficient-generative-weather-inference]]

## Key Concepts

- [[generative-weather-super-resolution]]: A modular post-processing framework that uses flow matching to super-resolve coarse weather forecasts while preserving large-scale physical structure.

## Archivist Review

The concepts and open questions were selected based on their relevance to the growing field of AI-based weather forecasting, specifically regarding the modular decoupling of resolution and time-series forecasting. The approved concepts represent a reusable architectural pattern, while the open questions target fundamental bottlenecks in the field. Other potential concepts were rejected for being too generic or paper-specific.

### Approved Concepts
- Generative Weather Super-Resolution: It defines the core methodological novelty: a decoupled, modular approach to super-resolving weather forecasts using flow matching to address high computational costs.

### Approved Open Questions
- Integrated Super-Resolution Forecasting Feedback: Understanding the interaction between downscaling and autoregressive forecasting is essential for developing computationally efficient, high-resolution global weather prediction systems.
- Efficient Generative Weather Inference: Computational efficiency is a major bottleneck for the operational use of high-resolution AI-based weather models, particularly for ensemble forecasting where many realizations are required.

## Links

- [Abstract](https://arxiv.org/abs/2604.00897)
- [PDF](https://arxiv.org/pdf/2604.00897)


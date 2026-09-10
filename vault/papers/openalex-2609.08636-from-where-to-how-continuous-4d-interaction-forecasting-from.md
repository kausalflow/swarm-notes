---
# CSL-compatible fields
title: "From Where to How: Continuous 4D Interaction Forecasting from Egocentric Video"
author:
  - literal: "Qiaohui Chu"
  - literal: "Haoyu Zhang"
  - literal: "Meng Liu"
  - literal: "Haoxiang Shi"
  - literal: "Dongmei Jiang"
  - literal: "Liqiang Nie"
issued:
  date-parts:
    - [2026, 9, 8]
url: "https://arxiv.org/abs/2609.08636"

# Custom fields
paper_id: "2609.08636"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "vision-language-model"
  - "action-conditioned-latent-world-model"
architectures:
  []
datasets:
  - "Coherent4D"
concept_slugs:
  - "higflow"
dataset_slugs:
  - "coherent4d"
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:16:49Z"
created_at: "2026-09-10T09:16:49Z"
---

# From Where to How: Continuous 4D Interaction Forecasting from Egocentric Video

**Authors**: Qiaohui Chu, Haoyu Zhang, Meng Liu, Haoxiang Shi, Dongmei Jiang, Liqiang Nie
**Date**: 2026-09-08
**Paper ID**: [openalex:2609.08636](https://arxiv.org/abs/2609.08636)

## Summary

This paper introduces Coherent4D, a large-scale egocentric dataset for continuous 4D interaction forecasting, and proposes HIGFlow, a Hand Interaction Guided Residual Flow framework that unifies the prediction of 3D interaction locations with full-body pose forecasting. By modeling forecasting as a cascaded where-to-how process, HIGFlow first predicts continuous interaction locations and then uses them to condition residual Flow Matching for diverse yet structurally consistent motion forecasting. Extensive experiments demonstrate consistent performance gains across multiple domains.

## Key Contributions

- Introduces Coherent4D, a large-scale egocentric dataset comprising approximately 233K samples across three domains for continuous 4D interaction forecasting.
- Proposes HIGFlow, a cascaded where-to-how framework that unifies continuous future 3D interaction location forecasting with full-body pose forecasting.
- Demonstrates consistent improvements over representative baselines across all three domains on both location and pose forecasting tasks.

## Open Questions & Future Work

- [[human-intent-modeling-and-contact-aware-conditioning]]

## Key Concepts

- [[higflow]]: A Hand Interaction Guided Residual Flow framework for continuous 4D interaction forecasting from egocentric video.

## Archivist Review

Approved the core framework 'HIGFlow' and dataset 'Coherent4D' as they represent reusable contributions to egocentric 4D interaction forecasting. Also approved the open question regarding human intent and contact-aware conditioning for longer horizons.

### Approved Concepts
- HIGFlow: Core proposed framework modeling egocentric 4D interaction forecasting as a cascaded where-to-how process combining hand interaction guidance with residual flow matching.

### Approved Open Questions
- Human Intent and Contact Conditioning: Addressing human intent and detailed contact constraints is critical for bridging the gap between coarse spatial trajectory forecasts and physically plausible human-object manipulations in robotics and assistant systems.

## Datasets

- [[coherent4d]]

## Links

- [Abstract](https://arxiv.org/abs/2609.08636)
- [PDF](https://arxiv.org/pdf/2609.08636)


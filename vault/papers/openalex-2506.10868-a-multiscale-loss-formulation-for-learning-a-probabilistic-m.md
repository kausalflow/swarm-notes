---
# CSL-compatible fields
title: "A multi‐scale loss formulation for learning a probabilistic model with proper score optimisation"
author:
  - literal: "Simon Lang"
  - literal: "Martin Leutbecher"
  - literal: "Pedro Maciel"
issued:
  date-parts:
    - [2026, 9, 4]
url: "https://arxiv.org/abs/2506.10868"

# Custom fields
paper_id: "2506.10868"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multi-scale-loss-formulation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-07T09:49:02Z"
created_at: "2026-09-07T09:49:02Z"
---

# A multi‐scale loss formulation for learning a probabilistic model with proper score optimisation

**Authors**: Simon Lang, Martin Leutbecher, Pedro Maciel
**Date**: 2026-09-04
**Paper ID**: [openalex:2506.10868](https://arxiv.org/abs/2506.10868)

## Summary

This paper evaluates a multi‐scale loss formulation for training probabilistic machine-learned weather forecasting models, specifically within the AIFS-CRPS model at ECMWF. By directly optimizing the almost fair continuous ranked probability score, the approach effectively constrains small-scale variability without degrading forecast skill. This formulation offers a promising avenue for scale-aware model training in geophysical and meteorological forecasting.

## Key Contributions

- Assessed the impact of a multi-scale loss formulation for training probabilistic machine-learned weather forecasting models within AIFS-CRPS.
- Demonstrated that optimizing the almost fair continuous ranked probability score with a multi-scale loss better constrains small-scale variability.
- Showed that small-scale variability constraints are achieved without negatively impacting overall forecast skill.

## Open Questions & Future Work

- [[optimal-multiscale-loss-hyperparameters]]

## Key Concepts

- [[multi-scale-loss-formulation]]: A loss formulation designed to train probabilistic models across multiple spatial or temporal scales using proper score optimization.

## Archivist Review

The approved concept and open question represent the core methodological contribution of multi-scale loss formulation and its hyperparameters for probabilistic spatial forecasting. No specific canonical dataset was proposed for vault inclusion.

### Approved Concepts
- Multi-Scale Loss Formulation: Introduces a multi-scale loss formulation designed to constrain small-scale variability in probabilistic machine-learned weather forecasting models.

### Approved Open Questions
- Optimal Multi-Scale Loss Hyperparameters: Crucial for extending multi-scale proper score optimization to diverse meteorological applications and spatial resolutions without manual hyper-parameter tuning bottlenecks.

## Links

- [Abstract](https://arxiv.org/abs/2506.10868)
- [PDF](https://arxiv.org/pdf/2506.10868)


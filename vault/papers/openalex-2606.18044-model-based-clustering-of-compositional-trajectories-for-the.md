---
# CSL-compatible fields
title: "Model-based clustering of compositional trajectories for the analysis of mobility data"
author:
  - literal: "Andrea Panarotto"
  - literal: "Manuela Cattelan"
  - literal: "Ruggero Bellio"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.18044"

# Custom fields
paper_id: "2606.18044"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "clustering"
  - "state-space-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "compositional-trajectory-modeling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:25:33Z"
created_at: "2026-06-19T09:25:33Z"
---

# Model-based clustering of compositional trajectories for the analysis of mobility data

**Authors**: Andrea Panarotto, Manuela Cattelan, Ruggero Bellio
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.18044](https://arxiv.org/abs/2606.18044)

## Summary

This paper presents a novel statistical framework for analyzing and clustering urban mobility trajectories derived from noisy telephonic data. The authors represent movements compositionally, encoding the proportions of different road types at each location as a point in a simplex to handle measurement uncertainty. A state-space model is then used to capture the temporal dynamics of the latent mobility process, and a mixture model is employed to cluster these trajectories into meaningful mobility behaviors. The approach is validated on mobility data from the municipality of Padova, demonstrating its utility for urban planning.

## Key Contributions

- Introduces a compositional representation for mobility trajectories that maps noisy location data onto the simplex based on road network proportions.
- Develops a state-space framework for compositional time series that decouples measurement error from latent mobility dynamics.
- Proposes a model-based clustering approach using mixtures of state-space models to identify interpretable, population-level mobility patterns.

## Open Questions & Future Work

- [[dynamic-spatial-uncertainty-modeling]]

## Key Concepts

- [[compositional-trajectory-modeling]]: A framework for representing trajectories as proportions of road types within a simplex to account for measurement uncertainty.

## Archivist Review

I approved the compositional trajectory modeling concept as it provides a distinct, reusable methodology for handling spatio-temporal uncertainty. The dynamic spatial uncertainty modeling open question was approved for its focus on a specific, unresolved architectural limitation within this type of mobility representation. Bayesian mixture trajectory clustering was rejected as it describes a general, well-known challenge in Bayesian statistics rather than a unique problem within this study.

### Approved Concepts
- Compositional Trajectory Modeling: Provides a novel way to encode spatial and categorical uncertainty in mobility data by mapping observations onto the simplex, enabling state-space modeling.

### Approved Open Questions
- Dynamic Spatial Uncertainty Modeling: Ensuring the compositional representation accurately reflects the underlying spatial uncertainty is fundamental to the reliability of mobility pattern extraction.

### Rejected Candidates
- [open_question] Bayesian Mixture Trajectory Clustering (`bayesian-mixture-trajectory-clustering`) - not_novel: While important, this is a standard open problem in Bayesian mixture modeling rather than a specific research question unique to the paper's mobility context.

## Links

- [Abstract](https://arxiv.org/abs/2606.18044)
- [PDF](https://arxiv.org/pdf/2606.18044)


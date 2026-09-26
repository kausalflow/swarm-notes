---
# CSL-compatible fields
title: "Kairos: Grounded Forecasting of Presence and Directional Flow in 4D Scene Graphs"
author:
  - literal: "Iacopo Catalano"
  - literal: "Julio A. Placed"
  - literal: "Javier Civera"
  - literal: "Jorge Peña Queralta"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.27467"

# Custom fields
paper_id: "2609.27467"
paper_source: "openalex"
domain: "robotics"
tags:
  - "robotics"
  - "spatio-temporal"
  - "forecasting"
  - "scene-graph"
  - "uncertainty-quantification"
  - "uncertainty"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  - "kairos"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-26T09:37:35Z"
created_at: "2026-09-26T09:37:35Z"
---

# Kairos: Grounded Forecasting of Presence and Directional Flow in 4D Scene Graphs

**Authors**: Iacopo Catalano, Julio A. Placed, Javier Civera, Jorge Peña Queralta
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.27467](https://arxiv.org/abs/2609.27467)

## Summary

Kairos is a predictive directional-flow memory framework that extends hierarchical 3D scene graphs into 4D scene graphs (4DSGs) to model and forecast pedestrian presence and directional motion distributions over time. By combining per-voxel directional mixtures, presence rates, and spectral predictors, Kairos enables continuous-time querying of future pedestrian dynamics and calibrated uncertainty bounds. Evaluated across three real-world pedestrian datasets, Kairos achieves competitive forecasting performance from sparse robot observations and enhances downstream encounter-probability robot planning.

## Key Contributions

- Kairos extends hierarchical 3D scene graphs to 4D scene graphs (4DSG) via a predictive directional-flow memory that stores directional mixtures and presence rates per voxel.
- Spectral predictors forecast future presence probability and full directional motion distributions for any query time while outputting calibrated credible intervals.
- Pairwise flow dependence between adjacent voxels supports conditional queries and consistent state maintenance under loop-closure corrections.
- Evaluation on three real pedestrian environments demonstrates robust forecasting competitive with full-stream models despite learning from sparse patrolling observations, improving downstream encounter-probability planning.

## Open Questions & Future Work

- [[adaptive-change-detection-in-scene-graphs-under-permanent-environmental-shifts]]

## Key Concepts

- [[kairos]]: A predictive directional-flow memory extending 3D scene graphs to 4D scene graphs to forecast presence rates and directional motion distributions over time.

## Archivist Review

Approved the central 4D scene graph framework 'Kairos' and one open question regarding non-stationary change detection in dynamic scene graphs, while rejecting a more localized subcomponent extension question. No datasets were approved because none were specifically named as primary evaluation benchmarks in the abstract.

### Approved Concepts
- Kairos: Introduces the core 4D scene graph predictive directional-flow memory representation.

### Approved Open Questions
- Adaptive Change Detection in Dynamic Scene Graphs: Crucial for deploying robots in non-stationary real-world environments where pedestrian patterns undergo abrupt or permanent shifts rather than purely periodic oscillations.

### Rejected Candidates
- [open_question] Topological Evidence Sharing for Flow Modeling (`topological-evidence-sharing-and-flow-coupling-in-scene-graphs`) - subcomponent_of_broader_mechanism: The question focuses on specific subcomponent extensions rather than a broad, standalone theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.27467)
- [PDF](https://arxiv.org/pdf/2609.27467)

